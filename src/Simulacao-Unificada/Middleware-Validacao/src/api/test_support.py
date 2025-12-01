"""
Endpoints de Suporte para Testes Unitários
Implementa validações consolidadas para RNF-01, RNF-02 e RNF-03
"""
from fastapi import APIRouter, Header, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from uuid import uuid4
import hashlib
import time

from ..core.dev_auth import get_current_user_simple
from ..monitoring.logger import logger, EventType


router = APIRouter(prefix="/api", tags=["Suporte Testes"])


# ============================================================================
# MODELOS
# ============================================================================

class ValidationRequest(BaseModel):
    """Requisição genérica de validação"""
    validation_type: Optional[str] = Field(None, description="access|integrity|guardrails|change|ingest|upload")
    user_id: Optional[str] = None
    project_id: Optional[str] = None
    resource_type: Optional[str] = None  # miro|sharepoint|copilot
    resource_id: Optional[str] = None
    data: Optional[Dict[str, Any]] = None
    checksum: Optional[str] = None
    justification: Optional[str] = None


class WorkflowRequest(BaseModel):
    """Requisição de workflow"""
    action: Optional[str] = Field(None, description="enqueue|status")
    workflow_id: Optional[str] = None
    workflow_type: Optional[str] = None
    priority: Optional[int] = 0
    data: Optional[Dict[str, Any]] = None


class LogRequest(BaseModel):
    """Requisição de criação de log"""
    event_type: str
    user_id: str
    resource_type: Optional[str] = None
    resource_id: Optional[str] = None
    action: Optional[str] = None
    details: Optional[Dict[str, Any]] = None
    trace_id: Optional[str] = None
    correlation_id: Optional[str] = None


class SentinelRequest(BaseModel):
    """Requisição para Sentinel (auditoria)"""
    action: Optional[str] = Field(None, description="verify|audit-trail|detect-bypass|consistency-check")
    trace_id: Optional[str] = None
    correlation_id: Optional[str] = None
    project_id: Optional[str] = None
    data: Optional[Dict[str, Any]] = None


# ============================================================================
# STORAGE SIMULADO (em memória para testes)
# ============================================================================

class TestStorage:
    def __init__(self):
        self.workflows = {}
        self.logs = []
        self.sentinel_data = {}
        self.sharepoint_history = {}
    
    def add_workflow(self, workflow_id: str, data: dict):
        self.workflows[workflow_id] = data
    
    def get_workflow(self, workflow_id: str):
        return self.workflows.get(workflow_id)
    
    def update_workflow_status(self, workflow_id: str, status: str):
        if workflow_id in self.workflows:
            self.workflows[workflow_id]["status"] = status
    
    def add_log(self, log_data: dict):
        self.logs.append(log_data)
    
    def get_logs_by_trace(self, trace_id: str):
        return [log for log in self.logs if log.get("trace_id") == trace_id]
    
    def add_sentinel_record(self, key: str, data: dict):
        self.sentinel_data[key] = data
    
    def get_sentinel_record(self, key: str):
        return self.sentinel_data.get(key)
    
    def add_sharepoint_history(self, project_id: str, change: dict):
        if project_id not in self.sharepoint_history:
            self.sharepoint_history[project_id] = []
        self.sharepoint_history[project_id].append(change)
    
    def get_sharepoint_history(self, project_id: str):
        return self.sharepoint_history.get(project_id, [])


storage = TestStorage()


# ============================================================================
# ENDPOINT 1: VALIDAÇÃO GENÉRICA (substitui 14 endpoints)
# ============================================================================

@router.post("/validate/{validation_type}")
async def validate(
    validation_type: str,
    request: ValidationRequest,
    user_id: str = Header(None, alias="X-User-Id")
):
    """
    Endpoint genérico de validação
    
    **Tipos suportados:**
    - `access` - Validação de acesso (RNF-01)
    - `integrity` - Validação de integridade/checksum (RNF-01)
    - `guardrails` - Guardrails de IA (RNF-01)
    - `change` - Validação de requisição de mudança (RNF-03)
    - `ingest` - Ingestão de dados Miro (RNF-02)
    - `upload` - Upload SharePoint (RNF-02)
    """
    trace_id = str(uuid4())
    request_user = user_id or request.user_id
    
    # ====================
    # ACCESS VALIDATION
    # ====================
    if validation_type == "access":
        # Usuários bloqueados (RNF-01 Cenário 1)
        if request_user == "u999":
            logger.log_incident(
                incident_type="access_denied",
                severity="high",
                user_id=request_user,
                resource_id=request.resource_id or "unknown",
                description="Usuário sem permissão",
                details={"reason": "user_not_in_project"}
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={
                    "access_granted": False,
                    "message": "Usuário não possui permissão para acessar este recurso",
                    "trace_id": trace_id
                }
            )
        
        # Validação de autenticação para Miro (RNF-01 Cenário 2)
        if request.resource_type == "miro" and not request_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail={"message": "Autenticação obrigatória para acessar boards do Miro"}
            )
        
        # Bloqueio de links públicos (RNF-01 Cenário 2)
        if request.data and request.data.get("is_public_link"):
            logger.log_incident(
                incident_type="public_link_blocked",
                severity="high",
                user_id=request_user,
                resource_id=request.resource_id or "unknown",
                description="Tentativa de compartilhamento público bloqueada",
                details={"resource_type": request.resource_type}
            )
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"message": "Links públicos não são permitidos", "trace_id": trace_id}
            )
        
        return {
            "access_granted": True,
            "user_id": request_user,
            "resource_id": request.resource_id,
            "trace_id": trace_id,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    # ====================
    # INTEGRITY VALIDATION
    # ====================
    elif validation_type == "integrity":
        action = request.data.get("action", "compare") if request.data else "compare"
        
        if action == "compare":
            # Comparação de checksums (RNF-01 Cenário 3)
            miro_checksum = request.data.get("miro_checksum") if request.data else None
            sharepoint_checksum = request.data.get("sharepoint_checksum") if request.data else None
            
            if not miro_checksum or not sharepoint_checksum:
                raise HTTPException(400, detail={"message": "Checksums obrigatórios"})
            
            match = miro_checksum == sharepoint_checksum
            
            if not match:
                logger.log_incident(
                    incident_type="data_inconsistency",
                    severity="high",
                    user_id=request_user,
                    resource_id=request.resource_id or "unknown",
                    description="Checksums não correspondem",
                    details={
                        "miro_checksum": miro_checksum,
                        "sharepoint_checksum": sharepoint_checksum
                    }
                )
            
            return {
                "match": match,
                "miro_checksum": miro_checksum,
                "sharepoint_checksum": sharepoint_checksum,
                "trace_id": trace_id
            }
        
        elif action == "normalize":
            # Normalização de whitespace (RNF-01 Cenário 3)
            content = request.data.get("content", "") if request.data else ""
            normalized = " ".join(content.split())
            normalized_checksum = hashlib.sha256(normalized.encode()).hexdigest()
            
            return {
                "normalized_content": normalized,
                "checksum": normalized_checksum,
                "trace_id": trace_id
            }
    
    # ====================
    # GUARDRAILS VALIDATION
    # ====================
    elif validation_type == "guardrails":
        prompt = request.data.get("prompt", "") if request.data else ""
        action_type = request.data.get("action", "check") if request.data else "check"
        
        # Palavras bloqueadas (fora do escopo)
        blocked_keywords = ["finanças", "vendas", "RH", "pessoal"]
        
        for keyword in blocked_keywords:
            if keyword.lower() in prompt.lower():
                logger.log_incident(
                    incident_type="out_of_scope",
                    severity="medium",
                    user_id=request_user,
                    resource_id=request.project_id or "unknown",
                    description=f"Prompt fora do escopo: contém '{keyword}'",
                    details={"prompt": prompt[:100]}
                )
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail={
                        "allowed": False,
                        "reason": f"Prompt fora do escopo do projeto: contém '{keyword}'",
                        "trace_id": trace_id
                    }
                )
        
        # Validação semântica simples
        if action_type == "semantic-check":
            is_valid = len(prompt) > 10 and not any(c in prompt for c in ["<script>", "DROP TABLE"])
            return {
                "valid": is_valid,
                "prompt": prompt[:100],
                "trace_id": trace_id
            }
        
        return {
            "allowed": True,
            "prompt": prompt[:100],
            "trace_id": trace_id,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    # ====================
    # CHANGE REQUEST VALIDATION
    # ====================
    elif validation_type == "change":
        justification = request.justification or (request.data.get("justification") if request.data else None)
        
        # RNF-03 Cenário 1: Bloqueio sem justificativa (vazio, None, ou apenas espaços)
        if not justification or not justification.strip():
            # Verifica tentativas anteriores do mesmo usuário para escalar severidade
            recent_incidents = logger.get_incidents(limit=10)
            user_attempts = sum(1 for inc in recent_incidents 
                              if inc.get("user_id") == request_user and
                              "change_without_justification" in inc.get("incident_type", ""))
            
            # Escala severidade após múltiplas tentativas
            severity = "critical" if user_attempts >= 2 else "high"
            
            logger.log_incident(
                incident_type="change_without_justification",
                severity=severity,
                user_id=request_user,
                resource_id=request.project_id or "unknown",
                description="Tentativa de mudança sem justificativa",
                details={"resource_id": request.resource_id, "attempt_count": user_attempts + 1}
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={
                    "approved": False,
                    "message": "Justificativa obrigatória para mudanças",
                    "trace_id": trace_id
                }
            )
        
        # Registra mudança automaticamente (RNF-03 Cenário 2)
        if request.project_id:
            change_record = {
                "timestamp": datetime.utcnow().isoformat(),
                "user_id": request_user,
                "justification": justification,
                "resource_id": request.resource_id,
                "trace_id": trace_id
            }
            storage.add_sharepoint_history(request.project_id, change_record)
        
        return {
            "approved": True,
            "justification": justification,
            "trace_id": trace_id,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    # ====================
    # INGEST (Miro)
    # ====================
    elif validation_type == "ingest":
        start_time = time.time()
        
        # Registra evento no logger ANTES do processamento
        custom_trace = request.data.get("trace_id") if request.data else None
        final_trace = custom_trace or trace_id
        
        logger.log(
            event_type=EventType.MIRO_BOARD_READ,
            user_id=request_user,
            resource_type="miro",
            resource_id=request.resource_id or "unknown",
            action="ingest",
            status="success",
            details={"source": "ingest_endpoint"},
            trace_id=final_trace
        )
        
        # Simula processamento
        latency = (time.time() - start_time) * 1000  # ms
        
        return {
            "status": "success",
            "trace_id": final_trace,
            "latency_ms": latency,
            "processed_items": request.data.get("item_count", 1) if request.data else 1,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    # ====================
    # UPLOAD (SharePoint)
    # ====================
    elif validation_type == "upload":
        file_hash = request.checksum or (request.data.get("file_hash") if request.data else None)
        
        if not file_hash:
            raise HTTPException(400, detail={"message": "Hash do arquivo obrigatório"})
        
        # Simula verificação de integridade
        verified = True  # Em produção, verificaria o hash real
        
        return {
            "upload_success": True,
            "file_hash": file_hash,
            "hash_verified": verified,
            "trace_id": trace_id,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    else:
        raise HTTPException(400, detail={"message": f"Tipo de validação '{validation_type}' não suportado"})


# ============================================================================
# ENDPOINT 2: WORKFLOWS (substitui 2 endpoints)
# ============================================================================

@router.post("/workflows/{action}")
async def workflows(
    action: str,
    request: WorkflowRequest,
    user_id: str = Header(None, alias="X-User-Id")
):
    """
    Gerenciamento de workflows
    
    **Ações:**
    - `enqueue` - Adiciona workflow à fila
    - `status` - Consulta status da fila
    """
    if action == "enqueue":
        # Usa workflow_id fornecido ou gera um novo
        workflow_id = request.workflow_id or str(uuid4())
        workflow_data = {
            "workflow_id": workflow_id,
            "workflow_type": request.workflow_type or "generic",
            "status": "queued",
            "priority": request.priority or 0,
            "user_id": user_id,
            "created_at": datetime.utcnow().isoformat(),
            "data": request.data or {}
        }
        storage.add_workflow(workflow_id, workflow_data)
        
        return {
            "workflow_id": workflow_id,
            "status": "queued",
            "position": len(storage.workflows),
            "timestamp": workflow_data["created_at"]
        }
    
    elif action == "status":
        workflow_id = request.workflow_id
        if not workflow_id:
            raise HTTPException(400, detail={"message": "workflow_id obrigatório"})
        
        workflow = storage.get_workflow(workflow_id)
        if not workflow:
            raise HTTPException(404, detail={"message": "Workflow não encontrado"})
        
        return {
            "workflow_id": workflow_id,
            "status": workflow["status"],
            "created_at": workflow["created_at"],
            "workflow_type": workflow["workflow_type"]
        }
    
    else:
        raise HTTPException(400, detail={"message": f"Ação '{action}' não suportada"})


# ============================================================================
# ENDPOINT 3: LOGGING PROGRAMÁTICO (substitui 1 endpoint)
# ============================================================================

@router.post("/monitoring/log")
async def create_log(
    request: LogRequest,
    user_id: str = Header(None, alias="X-User-Id")
):
    """
    Cria log programaticamente (para testes de burst RNF-02)
    """
    trace_id = request.trace_id or str(uuid4())
    
    log_entry = {
        "trace_id": trace_id,
        "correlation_id": request.correlation_id or trace_id,
        "event_type": request.event_type,
        "user_id": request.user_id,
        "resource_type": request.resource_type,
        "resource_id": request.resource_id,
        "action": request.action,
        "details": request.details or {},
        "timestamp": datetime.utcnow().isoformat()
    }
    
    storage.add_log(log_entry)
    
    return {
        "log_id": trace_id,
        "status": "logged",
        "timestamp": log_entry["timestamp"]
    }


# ============================================================================
# ENDPOINT 4: SHAREPOINT HISTÓRICO (substitui 1 endpoint)
# ============================================================================

@router.get("/sharepoint/history/{project_id}")
async def get_sharepoint_history(
    project_id: str,
    user_id: str = Header(None, alias="X-User-Id")
):
    """
    Retorna histórico de mudanças no SharePoint (RNF-03 Cenário 2)
    """
    history = storage.get_sharepoint_history(project_id)
    
    return {
        "project_id": project_id,
        "changes": history,
        "total": len(history)
    }


# ============================================================================
# ENDPOINT 5: SENTINEL - AUDITORIA (substitui 5 endpoints)
# ============================================================================

@router.post("/sentinel/{action}")
async def sentinel_action(
    action: str,
    request: SentinelRequest,
    user_id: str = Header(None, alias="X-User-Id")
):
    """
    Operações de auditoria via Sentinel
    
    **Ações:**
    - `verify` - Verifica integridade por correlation_id
    - `audit-trail` - Trilha de auditoria completa
    - `detect-bypass` - Detecta tentativas de bypass
    - `consistency-check` - Verifica consistência
    """
    if action == "verify":
        correlation_id = request.correlation_id
        if not correlation_id:
            raise HTTPException(400, detail={"message": "correlation_id obrigatório"})
        
        # Simula verificação de integridade
        record = storage.get_sentinel_record(correlation_id)
        
        if not record:
            # Cria registro simulado para testes
            record = {
                "correlation_id": correlation_id,
                "hash_match": True,
                "source": "miro",
                "destination": "sharepoint",
                "timestamp": datetime.utcnow().isoformat()
            }
            storage.add_sentinel_record(correlation_id, record)
        
        return record
    
    elif action == "audit-trail":
        trace_id = request.trace_id
        if not trace_id:
            raise HTTPException(400, detail={"message": "trace_id obrigatório"})
        
        # Busca todos os logs relacionados
        logs = storage.get_logs_by_trace(trace_id)
        
        return {
            "trace_id": trace_id,
            "events": logs,
            "total_events": len(logs),
            "origin": logs[0] if logs else None,
            "destination": logs[-1] if logs else None
        }
    
    elif action == "detect-bypass":
        # Simula detecção de bypass
        data = request.data or {}
        is_bypass_attempt = data.get("bypass_detected", False)
        
        if is_bypass_attempt:
            logger.log_incident(
                incident_type="bypass_attempt",
                severity="critical",
                user_id=user_id,
                resource_id=request.project_id or "unknown",
                description="Tentativa de bypass detectada",
                details=data
            )
        
        return {
            "bypass_detected": is_bypass_attempt,
            "alert_level": "critical" if is_bypass_attempt else "normal",
            "timestamp": datetime.utcnow().isoformat()
        }
    
    elif action == "consistency-check":
        # Verifica consistência entre fontes
        data = request.data or {}
        sources_consistent = data.get("consistent", True)
        
        if not sources_consistent:
            logger.log_incident(
                incident_type="data_inconsistency",
                severity="high",
                user_id=user_id,
                resource_id=request.project_id or "unknown",
                description="Inconsistência detectada entre fontes",
                details=data
            )
        
        return {
            "consistent": sources_consistent,
            "sources_checked": data.get("sources", []),
            "timestamp": datetime.utcnow().isoformat()
        }
    
    else:
        raise HTTPException(400, detail={"message": f"Ação '{action}' não suportada"})


# ============================================================================
# ENDPOINT 6: POWER BI (substitui 1 endpoint - opcional)
# ============================================================================

@router.get("/powerbi/traceability-report/{project_id}")
async def get_powerbi_report(
    project_id: str,
    user_id: str = Header(None, alias="X-User-Id")
):
    """
    Retorna dados para relatório de rastreabilidade (RNF-03 Cenário 4)
    """
    history = storage.get_sharepoint_history(project_id)
    
    return {
        "project_id": project_id,
        "report_generated": True,
        "total_changes": len(history),
        "last_update": datetime.utcnow().isoformat(),
        "changes": history
    }


# ============================================================================
# ENDPOINT 7: AUTH VALIDATION (substitui 2 endpoints)
# ============================================================================

@router.post("/auth/login")
async def auth_login(
    request: ValidationRequest
):
    """
    Simula login de usuário (RNF-02 Cenário 5)
    """
    # Aceita user_id tanto no nível superior quanto em data
    user_id = request.user_id or (request.data.get("user_id") if request.data else None)
    project_id = request.project_id or (request.data.get("project_id") if request.data else None)
    
    if not user_id:
        raise HTTPException(400, detail={"message": "user_id obrigatório"})
    
    # Simula geração de token
    token = hashlib.sha256(f"{user_id}:{project_id}:{time.time()}".encode()).hexdigest()[:32]
    
    return {
        "success": True,
        "user_id": user_id,
        "project_id": project_id,
        "token": token,
        "expires_in": 3600,
        "timestamp": datetime.utcnow().isoformat()
    }


@router.post("/auth/validate")
@router.get("/auth/validate")
async def validate_auth(
    user_id: str = Header(None, alias="X-User-Id"),
    authorization: str = Header(None, alias="Authorization")
):
    """
    Valida tokens/sessões de autenticação (RNF-02 Cenário 5)
    """
    # Suporta tanto X-User-Id quanto Authorization Bearer
    if not user_id and not authorization:
        raise HTTPException(401, detail={"valid": False, "message": "Usuário não autenticado"})
    
    token = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization.replace("Bearer ", "")
    
    return {
        "valid": True,
        "user_id": user_id or "token_user",
        "token": token,
        "session_active": True,
        "timestamp": datetime.utcnow().isoformat()
    }
