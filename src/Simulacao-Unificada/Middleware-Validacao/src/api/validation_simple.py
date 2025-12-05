"""
Endpoints de Validação com Autenticação Simplificada

Versão simplificada para demonstração sem JWT.
Simula autenticação corporativa (Microsoft Entra ID).
"""
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import Optional

from ..core.dev_auth import get_current_user_simple
from ..core.auth import User
from ..core.permissions import check_access, Permission
from ..services.api_client import miro_client, sharepoint_client, copilot_client
from ..services.validator import data_validator
from ..monitoring.logger import logger, EventType


router = APIRouter(prefix="/simple/validation", tags=["Validação (Modo Simples)"])


@router.get("/test")
async def test_endpoint():
    """Endpoint de teste para verificar se a rota está funcionando"""
    return {"status": "ok", "message": "Endpoint de validação simples está funcionando!"}


class MiroAccessRequest(BaseModel):
    board_id: str
    project_id: str


class SyncValidationRequest(BaseModel):
    board_id: str
    site_id: str
    project_id: str


class AIPromptRequest(BaseModel):
    prompt: str
    project_id: str
    session_id: Optional[str] = None


@router.post("/miro/validate-access")
async def validate_miro_access_simple(
    request: MiroAccessRequest,
    user: User = Depends(get_current_user_simple)
):
    """
    Valida se usuário tem permissão para acessar board do Miro
    
    **Cenário RNF-01:** Controle de acesso granular por projeto
    
    🔹 Simulação de SSO: Use header X-User-Id (ex: u001)
    """
    try:
        # Debug
        print(f"🔍 Validando acesso - User: {user.user_id}, Role: {user.role}, Projects: {user.projects}")
        print(f"🔍 Request - Board: {request.board_id}, Project: {request.project_id}")
        
        # Verifica permissão
        access_decision = check_access(
            user_id=user.user_id,
            user_role=user.role,
            user_projects=user.projects if user.projects else [],
            resource_type="miro",
            resource_id=f"{request.project_id}-board-{request.board_id}",
            action="read"
        )
        
        print(f"🔍 Access decision: allowed={access_decision.allowed}, reason={access_decision.reason}")
        
        if not access_decision.allowed:
            # Log do incidente
            logger.log_incident(
                incident_type="access_denied",
                severity="medium",
                user_id=user.user_id,
                resource_id=request.board_id,
                description=f"Acesso negado ao board {request.board_id}",
                details={
                    "board_id": request.board_id,
                    "project_id": request.project_id,
                    "reason": access_decision.reason
                }
            )
            
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Acesso negado ao board {request.board_id}: {access_decision.reason}"
            )
        
        # Verifica se tem permissão de escrita também
        write_decision = check_access(
            user_id=user.user_id,
            user_role=user.role,
            user_projects=user.projects if user.projects else [],
            resource_type="miro",
            resource_id=f"{request.project_id}-board-{request.board_id}",
            action="write"
        )
        
        # Log de sucesso
        logger.log(
            event_type=EventType.MIRO_BOARD_ACCESS,
            user_id=user.user_id,
            resource_type="miro",
            resource_id=request.board_id,
            action="read",
            details={"project_id": request.project_id, "board_id": request.board_id},
            status="success"
        )
        
        return {
            "access_granted": True,
            "board_id": request.board_id,
            "user_id": user.user_id,
            "permissions": ["read", "write"] if write_decision.allowed else ["read"]
        }
    
    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Erro inesperado: {type(e).__name__}: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro interno: {str(e)}"
        )


@router.post("/miro-to-sharepoint/sync")
async def validate_sync_simple(
    request: SyncValidationRequest,
    user: User = Depends(get_current_user_simple)
):
    """
    Valida sincronização entre Miro e SharePoint via checksum
    
    **Cenário RNF-01:** Detecção de modificações não autorizadas
    
    🔹 Simulação de SSO: Use header X-User-Id (ex: u001)
    """
    # Verifica permissões
    miro_access = check_access(
        user_id=user.user_id,
        user_role=user.role,
        user_projects=user.projects,
        resource_type="miro",
        resource_id=f"{request.project_id}-board-{request.board_id}",
        action="read"
    )
    
    sharepoint_access = check_access(
        user_id=user.user_id,
        user_role=user.role,
        user_projects=user.projects,
        resource_type="sharepoint",
        resource_id=f"{request.project_id}-site-{request.site_id}",
        action="read"
    )
    
    if not (miro_access.allowed and sharepoint_access.allowed):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Sem permissão para validar sincronização"
        )
    
    # Busca dados de ambas as fontes
    miro_data = await miro_client.get_board_activities(request.board_id, user.user_id)
    sharepoint_data = await sharepoint_client.get_site_documents(request.site_id, user.user_id)
    
    # Valida checksums
    validation_result = data_validator.validate_miro_to_sharepoint(
        miro_data=miro_data,
        sharepoint_data=sharepoint_data
    )
    
    if not validation_result["is_consistent"]:
        # Log de incidente
        logger.log_incident(
            incident_type="data_mismatch",
            severity="high",
            user_id=user.user_id,
            resource_id=f"{request.board_id}-{request.site_id}",
            description="Checksum mismatch - possível modificação não autorizada",
            details={
                "project_id": request.project_id,
                "board_id": request.board_id,
                "site_id": request.site_id,
                "miro_checksum": validation_result["miro_checksum"],
                "sharepoint_checksum": validation_result["sharepoint_checksum"]
            }
        )
    else:
        logger.log(
            event_type=EventType.DATA_VALIDATION,
            user_id=user.user_id,
            resource_type="sync",
            resource_id=f"{request.board_id}-{request.site_id}",
            action="validate",
            details={**validation_result, "project_id": request.project_id},
            status="success"
        )
    
    return {
        "is_valid": validation_result["is_consistent"],
        "miro_checksum": validation_result["miro_checksum"],
        "sharepoint_checksum": validation_result["sharepoint_checksum"],
        "mismatch_detected": not validation_result["is_consistent"],
        "message": "Dados consistentes entre Miro e SharePoint" if validation_result["is_consistent"] else "ALERTA: Checksums não correspondem - possível modificação não autorizada"
    }


@router.post("/ai/validate-prompt")
async def validate_ai_prompt_simple(
    request: AIPromptRequest,
    user: User = Depends(get_current_user_simple)
):
    """
    Valida prompt antes de enviar ao Copilot (Guardrails)
    
    **Cenário RNF-01:** Prevenção de vazamento de dados sensíveis
    
    🔹 Simulação de SSO: Use header X-User-Id (ex: u001)
    """
    # Lista de palavras proibidas (guardrails)
    forbidden_keywords = [
        "senha", "password", "token", "secret", "api_key",
        "confidencial", "restrito", "sigiloso", "privado",
        "cpf", "cnpj", "cartão", "conta bancária"
    ]
    
    # Verifica prompt
    prompt_lower = request.prompt.lower()
    violations = [kw for kw in forbidden_keywords if kw in prompt_lower]
    
    if violations:
        # Log de incidente
        logger.log_incident(
            incident_type="guardrail_violation",
            severity="high",
            user_id=user.user_id,
            resource_id=request.session_id or "no-session",
            description="Prompt contém informações sensíveis",
            details={
                "project_id": request.project_id,
                "prompt_preview": request.prompt[:100],
                "violations": violations
            }
        )
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "error": "Prompt bloqueado pelos guardrails de IA",
                "violations": violations,
                "message": "Remova informações sensíveis do prompt"
            }
        )
    
    # Log de sucesso
    logger.log(
        event_type=EventType.AI_REQUEST,
        user_id=user.user_id,
        resource_type="ai",
        resource_id=request.session_id or "no-session",
        action="validate_prompt",
        details={"project_id": request.project_id, "session_id": request.session_id},
        status="success"
    )
    
    return {
        "prompt_valid": True,
        "guardrails_passed": True,
        "session_id": request.session_id,
        "message": "Prompt aprovado - pode prosseguir com o Copilot"
    }
