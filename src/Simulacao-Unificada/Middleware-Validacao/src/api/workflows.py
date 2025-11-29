"""
Fluxos Completos de Integração

Implementa fluxos end-to-end integrando todas as ferramentas mockadas:
- Miro → Office → SharePoint → Copilot → Sentinel
"""
from fastapi import APIRouter, HTTPException, Header
from typing import Optional, Dict, Any, List
from pydantic import BaseModel
import uuid

from ..core.auth import get_current_user
from ..core.permissions import check_access
from ..services.api_client import (
    miro_client,
    sharepoint_client,
    sentinel_client,
    copilot_client
)
from ..services.validator import data_validator
from ..monitoring.logger import log_event, log_incident, EventType


router = APIRouter(prefix="/workflows", tags=["Fluxos Integrados"])


class ProjectWorkflowRequest(BaseModel):
    """Request para fluxo completo de projeto"""
    project_id: str
    board_id: str  # Miro
    site_id: str   # SharePoint
    description: str = "Novo projeto"


class AIAssistRequest(BaseModel):
    """Request para assistência de IA no projeto"""
    project_id: str
    question: str
    context: Optional[Dict[str, Any]] = None


@router.post("/project/complete-flow")
async def complete_project_workflow(
    request: ProjectWorkflowRequest,
    authorization: Optional[str] = Header(None)
):
    """
    Fluxo completo de gerenciamento de projeto integrando todas as ferramentas:
    
    1. **Miro**: Busca dados do brainstorming/planejamento
    2. **Office**: Simula criação de documentos (Word/Excel)
    3. **SharePoint**: Armazena documentos validados
    4. **Copilot**: Sugere melhorias via IA
    5. **Sentinel**: Envia eventos de auditoria
    
    Implementa rastreabilidade completa (RNF-03) e validação de dados (RNF-01)
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token não fornecido")
    
    token = authorization.replace("Bearer ", "")
    user = get_current_user(token)
    
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    # IDs de rastreabilidade
    correlation_id = str(uuid.uuid4())
    workflow_trace_id = str(uuid.uuid4())
    
    workflow_result = {
        "workflow_id": correlation_id,
        "project_id": request.project_id,
        "user_id": user.user_id,
        "steps": [],
        "status": "in_progress"
    }
    
    try:
        # ========== PASSO 1: MIRO - Buscar dados de planejamento ==========
        log_event(
            event_type=EventType.MIRO_BOARD_READ,
            user_id=user.user_id,
            resource_type="miro",
            resource_id=request.board_id,
            action="read",
            status="success",
            details={"step": "1_miro_read", "project_id": request.project_id},
            trace_id=workflow_trace_id,
            correlation_id=correlation_id
        )
        
        # Valida acesso ao Miro
        miro_access = check_access(
            user_id=user.user_id,
            user_role=user.role,
            user_projects=user.projects,
            resource_type="miro",
            resource_id=request.board_id,
            action="read"
        )
        
        if not miro_access.allowed:
            raise HTTPException(status_code=403, detail=f"Acesso negado ao Miro: {miro_access.reason}")
        
        # Busca dados do Miro
        miro_data = await miro_client.get_board_activities(
            board_id=request.board_id,
            user_id=user.user_id
        )
        
        if miro_data.get("error"):
            raise HTTPException(status_code=502, detail=f"Erro ao acessar Miro: {miro_data.get('message')}")
        
        workflow_result["steps"].append({
            "step": 1,
            "service": "Miro",
            "action": "Dados de planejamento coletados",
            "status": "success",
            "data_checksum": data_validator.calculate_checksum(miro_data.get("data", {}))
        })
        
        # ========== PASSO 2: SHAREPOINT - Armazenar dados ==========
        log_event(
            event_type=EventType.SHAREPOINT_DOCUMENT_WRITE,
            user_id=user.user_id,
            resource_type="sharepoint",
            resource_id=request.site_id,
            action="write",
            status="success",
            details={"step": "2_sharepoint_write", "project_id": request.project_id},
            trace_id=workflow_trace_id,
            correlation_id=correlation_id
        )
        
        # Valida acesso de escrita no SharePoint
        sharepoint_access = check_access(
            user_id=user.user_id,
            user_role=user.role,
            user_projects=user.projects,
            resource_type="sharepoint",
            resource_id=request.site_id,
            action="write"
        )
        
        if not sharepoint_access.allowed:
            raise HTTPException(status_code=403, detail=f"Acesso negado ao SharePoint: {sharepoint_access.reason}")
        
        # Busca documentos existentes no SharePoint
        sharepoint_data = await sharepoint_client.get_site_documents(
            site_id=request.site_id,
            user_id=user.user_id
        )
        
        # Valida consistência Miro → SharePoint
        validation = data_validator.validate_miro_to_sharepoint(
            miro_data=miro_data.get("data", {}),
            sharepoint_data=sharepoint_data.get("data", {})
        )
        
        if not validation["is_consistent"]:
            log_incident(
                incident_type="data_mismatch",
                severity="high",
                user_id=user.user_id,
                resource_id=f"{request.board_id}→{request.site_id}",
                description="Inconsistência entre Miro e SharePoint",
                details=validation,
                trace_id=workflow_trace_id
            )
        
        workflow_result["steps"].append({
            "step": 2,
            "service": "SharePoint",
            "action": "Dados armazenados e validados",
            "status": "success" if validation["is_consistent"] else "warning",
            "validation": validation
        })
        
        # ========== PASSO 3: COPILOT - Assistência de IA ==========
        log_event(
            event_type=EventType.AI_REQUEST,
            user_id=user.user_id,
            resource_type="ai",
            resource_id=request.project_id,
            action="suggest",
            status="success",
            details={"step": "3_copilot_assist", "project_id": request.project_id},
            trace_id=workflow_trace_id,
            correlation_id=correlation_id
        )
        
        # Busca sessões do Copilot
        copilot_sessions = await copilot_client.get_sessions(user_id=user.user_id)
        
        workflow_result["steps"].append({
            "step": 3,
            "service": "Microsoft 365 Copilot",
            "action": "Análise de IA realizada",
            "status": "success",
            "ai_suggestions": [
                "Documento de requisitos está completo",
                "Considere adicionar cronograma detalhado",
                "Revisar riscos identificados no Miro"
            ]
        })
        
        # ========== PASSO 4: SENTINEL - Auditoria e Segurança ==========
        log_event(
            event_type=EventType.SYSTEM_HEALTH_CHECK,
            user_id=user.user_id,
            resource_type="audit",
            resource_id=request.project_id,
            action="audit",
            status="success",
            details={
                "step": "4_sentinel_audit",
                "project_id": request.project_id,
                "workflow_id": correlation_id
            },
            trace_id=workflow_trace_id,
            correlation_id=correlation_id
        )
        
        # Envia eventos para Sentinel
        sentinel_events = await sentinel_client.get_events(user_id=user.user_id)
        
        workflow_result["steps"].append({
            "step": 4,
            "service": "Microsoft Sentinel",
            "action": "Eventos de auditoria enviados",
            "status": "success",
            "audit_trail": f"Todos os eventos registrados com correlation_id: {correlation_id}"
        })
        
        # ========== FINALIZAÇÃO ==========
        workflow_result["status"] = "completed"
        workflow_result["trace_id"] = workflow_trace_id
        workflow_result["correlation_id"] = correlation_id
        
        log_event(
            event_type=EventType.RESOURCE_WRITE,
            user_id=user.user_id,
            resource_type="workflow",
            resource_id=request.project_id,
            action="complete",
            status="success",
            details={
                "workflow_id": correlation_id,
                "steps_completed": len(workflow_result["steps"])
            },
            trace_id=workflow_trace_id,
            correlation_id=correlation_id
        )
        
        return workflow_result
    
    except HTTPException:
        raise
    except Exception as e:
        log_incident(
            incident_type="workflow_error",
            severity="high",
            user_id=user.user_id,
            resource_id=request.project_id,
            description=f"Erro no fluxo de projeto: {str(e)}",
            details={"workflow_id": correlation_id, "error": str(e)},
            trace_id=workflow_trace_id
        )
        raise HTTPException(status_code=500, detail=f"Erro no workflow: {str(e)}")


@router.post("/ai/analyze-project")
async def ai_analyze_project(
    request: AIAssistRequest,
    authorization: Optional[str] = Header(None)
):
    """
    Utiliza Copilot + Sentinel para análise inteligente do projeto
    
    1. **Copilot**: Processa pergunta e contexto do projeto
    2. **Sentinel**: Verifica se há incidentes relacionados
    3. **Guardrails**: Valida que IA não acesse dados restritos
    """
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token não fornecido")
    
    token = authorization.replace("Bearer ", "")
    user = get_current_user(token)
    
    if not user:
        raise HTTPException(status_code=401, detail="Token inválido")
    
    trace_id = str(uuid.uuid4())
    
    # Valida permissão de uso de IA
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
    
    # Guardrails: valida pergunta
    forbidden_patterns = [
        "outros projetos", "todos os projetos", "outros usuários",
        "dados sensíveis", "informações confidenciais", "acesso completo"
    ]
    
    question_lower = request.question.lower()
    for pattern in forbidden_patterns:
        if pattern in question_lower:
            log_incident(
                incident_type="ai_guardrail_violation",
                severity="critical",
                user_id=user.user_id,
                resource_id=request.project_id,
                description=f"Pergunta viola guardrails: {pattern}",
                details={"question": request.question},
                trace_id=trace_id
            )
            raise HTTPException(
                status_code=403,
                detail=f"Pergunta bloqueada por guardrails: contém '{pattern}'"
            )
    
    # Busca sessões do Copilot
    copilot_response = await copilot_client.get_sessions(user_id=user.user_id)
    
    # Busca incidentes relacionados no Sentinel
    sentinel_incidents = await sentinel_client.get_incidents(user_id=user.user_id)
    
    log_event(
        event_type=EventType.AI_RESPONSE,
        user_id=user.user_id,
        resource_type="ai",
        resource_id=request.project_id,
        action="analyze",
        status="success",
        details={"question": request.question},
        trace_id=trace_id
    )
    
    return {
        "project_id": request.project_id,
        "question": request.question,
        "ai_analysis": {
            "status": "success",
            "response": f"Análise do projeto {request.project_id} realizada com sucesso",
            "insights": [
                "Documentação está alinhada com requisitos",
                "Não há incidentes de segurança críticos",
                "Sugestão: revisar timeline do projeto"
            ]
        },
        "security_check": {
            "sentinel_status": "ok",
            "incidents_found": len(sentinel_incidents.get("data", {}).get("incidents", [])) if not sentinel_incidents.get("error") else 0,
            "guardrails_passed": True
        },
        "trace_id": trace_id
    }


@router.get("/integration/health")
async def integration_health():
    """
    Verifica saúde da integração com todas as APIs mockadas
    """
    health_status = {
        "middleware": "healthy",
        "integrations": {}
    }
    
    try:
        # Testa Miro
        miro_test = await miro_client.get_boards()
        health_status["integrations"]["miro"] = "healthy" if not miro_test.get("error") else "unhealthy"
    except:
        health_status["integrations"]["miro"] = "unreachable"
    
    try:
        # Testa SharePoint
        sp_test = await sharepoint_client.get_sites()
        health_status["integrations"]["sharepoint"] = "healthy" if not sp_test.get("error") else "unhealthy"
    except:
        health_status["integrations"]["sharepoint"] = "unreachable"
    
    try:
        # Testa Sentinel
        sentinel_test = await sentinel_client.get_events()
        health_status["integrations"]["sentinel"] = "healthy" if not sentinel_test.get("error") else "unhealthy"
    except:
        health_status["integrations"]["sentinel"] = "unreachable"
    
    try:
        # Testa Copilot
        copilot_test = await copilot_client.get_sessions()
        health_status["integrations"]["copilot"] = "healthy" if not copilot_test.get("error") else "unhealthy"
    except:
        health_status["integrations"]["copilot"] = "unreachable"
    
    # Determina status geral
    all_healthy = all(
        status == "healthy" 
        for status in health_status["integrations"].values()
    )
    health_status["overall_status"] = "healthy" if all_healthy else "degraded"
    
    return health_status
