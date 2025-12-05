"""
Endpoints de Validação e Integração

Implementa os cenários dos RNFs:
- Validação de acesso ao Miro
- Sincronização Miro → SharePoint com checksum
- Guardrails para agentes de IA
"""
from fastapi import APIRouter, HTTPException, Header, Depends
from typing import Optional, Dict, Any
from pydantic import BaseModel
import uuid

from ..core.auth import get_current_user, User
from ..core.permissions import check_access
from ..services.api_client import miro_client, sharepoint_client, sentinel_client
from ..services.validator import data_validator
from ..monitoring.logger import log_event, log_incident, EventType


router = APIRouter(prefix="/validation", tags=["Validação e Integração"])


class MiroAccessRequest(BaseModel):
    """Request para validar acesso ao Miro"""
    board_id: str
    action: str = "read"  # read ou write


class MiroToSharePointSync(BaseModel):
    """Request para sincronizar dados Miro → SharePoint"""
    board_id: str
    site_id: str
    project_id: str


class AIPromptRequest(BaseModel):
    """Request para validar prompt de IA"""
    prompt: str
    project_id: str
    session_id: Optional[str] = None


@router.post("/miro/validate-access")
async def validate_miro_access(
    request: MiroAccessRequest,
    authorization: Optional[str] = Header(None)
):
    """
    Valida se usuário tem acesso a um board do Miro
    
    Implementa RNF-01: Cenário 2 - Acesso indevido ao Miro
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token não fornecido")
    
    token = authorization.replace("Bearer ", "")
    user = get_current_user(token)
    
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    trace_id = str(uuid.uuid4())
    
    # Verifica permissões usando o sistema de controle de acesso
    access_decision = check_access(
        user_id=user.user_id,
        user_role=user.role,
        user_projects=user.projects,
        resource_type="miro",
        resource_id=request.board_id,
        action=request.action
    )
    
    if not access_decision.allowed:
        # Acesso negado - registra incidente
        log_incident(
            incident_type="miro_access_denied",
            severity="high",
            user_id=user.user_id,
            resource_id=request.board_id,
            description=access_decision.reason,
            details={
                "action": request.action,
                "user_role": user.role,
                "user_projects": user.projects
            },
            trace_id=trace_id
        )
        
        raise HTTPException(
            status_code=403,
            detail={
                "access_denied": True,
                "reason": access_decision.reason,
                "trace_id": trace_id
            }
        )
    
    # Acesso permitido - registra log
    log_event(
        event_type=EventType.MIRO_BOARD_ACCESS,
        user_id=user.user_id,
        resource_type="miro",
        resource_id=request.board_id,
        action=request.action,
        status="success",
        details={
            "user_role": user.role,
            "projects": user.projects
        },
        trace_id=trace_id
    )
    
    return {
        "access_granted": True,
        "user_id": user.user_id,
        "board_id": request.board_id,
        "action": request.action,
        "trace_id": trace_id
    }


@router.post("/miro-to-sharepoint/sync")
async def sync_miro_to_sharepoint(
    request: MiroToSharePointSync,
    authorization: Optional[str] = Header(None)
):
    """
    Sincroniza dados do Miro para SharePoint com validação de integridade
    
    Implementa RNF-01: Cenário 3 - Inconsistências entre Miro e SharePoint
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token não fornecido")
    
    token = authorization.replace("Bearer ", "")
    user = get_current_user(token)
    
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    trace_id = str(uuid.uuid4())
    correlation_id = str(uuid.uuid4())
    
    # Verifica permissão de leitura no Miro
    miro_access = check_access(
        user_id=user.user_id,
        user_role=user.role,
        user_projects=user.projects,
        resource_type="miro",
        resource_id=request.board_id,
        action="read"
    )
    
    if not miro_access.allowed:
        log_incident(
            incident_type="sync_access_denied_miro",
            severity="medium",
            user_id=user.user_id,
            resource_id=request.board_id,
            description=miro_access.reason,
            trace_id=trace_id
        )
        raise HTTPException(status_code=403, detail=miro_access.reason)
    
    # Verifica permissão de escrita no SharePoint
    sharepoint_access = check_access(
        user_id=user.user_id,
        user_role=user.role,
        user_projects=user.projects,
        resource_type="sharepoint",
        resource_id=request.site_id,
        action="write"
    )
    
    if not sharepoint_access.allowed:
        log_incident(
            incident_type="sync_access_denied_sharepoint",
            severity="medium",
            user_id=user.user_id,
            resource_id=request.site_id,
            description=sharepoint_access.reason,
            trace_id=trace_id
        )
        raise HTTPException(status_code=403, detail=sharepoint_access.reason)
    
    # Busca dados do Miro via API mockada
    log_event(
        event_type=EventType.MIRO_BOARD_READ,
        user_id=user.user_id,
        resource_type="miro",
        resource_id=request.board_id,
        action="read",
        status="success",
        trace_id=trace_id,
        correlation_id=correlation_id
    )
    
    miro_data = await miro_client.get_board_activities(
        board_id=request.board_id,
        user_id=user.user_id
    )
    
    if miro_data.get("error"):
        raise HTTPException(
            status_code=502,
            detail=f"Erro ao acessar Miro: {miro_data.get('message')}"
        )
    
    # Busca dados do SharePoint via API mockada
    sharepoint_data = await sharepoint_client.get_site_documents(
        site_id=request.site_id,
        user_id=user.user_id
    )
    
    if sharepoint_data.get("error"):
        raise HTTPException(
            status_code=502,
            detail=f"Erro ao acessar SharePoint: {sharepoint_data.get('message')}"
        )
    
    # Valida consistência entre os dados
    validation_result = data_validator.validate_miro_to_sharepoint(
        miro_data=miro_data.get("data", {}),
        sharepoint_data=sharepoint_data.get("data", {})
    )
    
    # Log da validação de dados
    log_event(
        event_type=EventType.DATA_CHECKSUM,
        user_id=user.user_id,
        resource_type="sync",
        resource_id=f"{request.board_id}→{request.site_id}",
        action="validate",
        status="success" if validation_result["is_consistent"] else "failed",
        details={
            "miro_checksum": validation_result["miro_checksum"],
            "sharepoint_checksum": validation_result["sharepoint_checksum"],
            "is_consistent": validation_result["is_consistent"]
        },
        trace_id=trace_id,
        correlation_id=correlation_id
    )
    
    # Se houver inconsistência, registra incidente
    if not validation_result["is_consistent"]:
        log_incident(
            incident_type="data_mismatch",
            severity="high",
            user_id=user.user_id,
            resource_id=f"{request.board_id}→{request.site_id}",
            description="Inconsistência detectada entre dados do Miro e SharePoint",
            details={
                "validation": validation_result,
                "project_id": request.project_id
            },
            trace_id=trace_id
        )
        
        return {
            "sync_completed": False,
            "validation_failed": True,
            "reason": "Inconsistência entre dados",
            "validation_result": validation_result,
            "trace_id": trace_id,
            "correlation_id": correlation_id
        }
    
    # Sincronização bem-sucedida
    log_event(
        event_type=EventType.SHAREPOINT_SYNC,
        user_id=user.user_id,
        resource_type="sync",
        resource_id=f"{request.board_id}→{request.site_id}",
        action="sync",
        status="success",
        details={"project_id": request.project_id},
        trace_id=trace_id,
        correlation_id=correlation_id
    )
    
    return {
        "sync_completed": True,
        "validation_passed": True,
        "validation_result": validation_result,
        "trace_id": trace_id,
        "correlation_id": correlation_id
    }


@router.post("/ai/validate-prompt")
async def validate_ai_prompt(
    request: AIPromptRequest,
    authorization: Optional[str] = Header(None)
):
    """
    Valida prompt de IA aplicando guardrails
    
    Implementa RNF-01: Cenário 4 - Ação indevida por agente de IA
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token não fornecido")
    
    token = authorization.replace("Bearer ", "")
    user = get_current_user(token)
    
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    trace_id = str(uuid.uuid4())
    
    # Verifica se usuário pode usar IA
    ai_access = check_access(
        user_id=user.user_id,
        user_role=user.role,
        user_projects=user.projects,
        resource_type="ai",
        resource_id=request.project_id,
        action="use"
    )
    
    if not ai_access.allowed:
        log_incident(
            incident_type="ai_access_denied",
            severity="medium",
            user_id=user.user_id,
            resource_id=request.project_id,
            description=ai_access.reason,
            trace_id=trace_id
        )
        raise HTTPException(status_code=403, detail=ai_access.reason)
    
    # Guardrails: palavras/padrões proibidos
    forbidden_patterns = [
        "compare o andamento deste projeto com outros projetos",
        "resuma tudo o que você sabe relacionado",
        "liste padrões comuns entre projetos",
        "verifique se existe algum documento",
        "mostre todos os projetos",
        "acesse outros projetos",
        "dados de outros usuários"
    ]
    
    prompt_lower = request.prompt.lower()
    violations = []
    
    for pattern in forbidden_patterns:
        if pattern in prompt_lower:
            violations.append(pattern)
    
    # Se houver violações, bloqueia e registra incidente
    if violations:
        log_incident(
            incident_type="ai_guardrail_violation",
            severity="critical",
            user_id=user.user_id,
            resource_id=request.project_id,
            description="Tentativa de bypass dos guardrails de IA",
            details={
                "prompt": request.prompt,
                "violations": violations,
                "session_id": request.session_id
            },
            trace_id=trace_id
        )
        
        return {
            "validation_passed": False,
            "blocked": True,
            "reason": "Prompt viola guardrails de segurança",
            "violations": violations,
            "trace_id": trace_id
        }
    
    # Prompt válido
    log_event(
        event_type=EventType.AI_REQUEST,
        user_id=user.user_id,
        resource_type="ai",
        resource_id=request.project_id,
        action="validate_prompt",
        status="success",
        details={
            "prompt_length": len(request.prompt),
            "session_id": request.session_id
        },
        trace_id=trace_id
    )
    
    return {
        "validation_passed": True,
        "blocked": False,
        "prompt_safe": True,
        "trace_id": trace_id
    }
