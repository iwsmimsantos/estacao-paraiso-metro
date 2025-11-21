"""
Modelos de dados para logs e eventos do sistema de rastreabilidade
"""
from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field
from uuid import uuid4


class SharePointChangeEvent(BaseModel):
    """Evento de mudança originado do SharePoint/OfficeActivity"""
    event_id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    user: str
    project_id: str
    change_type: Literal["criacao", "atualizacao", "exclusao", "status_change"]
    justification: Optional[str] = None
    field_changed: Optional[str] = None
    old_value: Optional[str] = None
    new_value: Optional[str] = None
    source: str = "SharePoint"
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class SentinelLogEvent(BaseModel):
    """Evento de log no Microsoft Sentinel"""
    log_id: str = Field(default_factory=lambda: str(uuid4()))
    correlation_id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    event_type: Literal[
        "mudanca_aprovada",
        "tentativa_invalida",
        "bloqueio",
        "alerta",
        "auditoria"
    ]
    severity: Literal["low", "medium", "high", "critical"]
    user: str
    project_id: str
    description: str
    source_system: str
    hash_value: str
    metadata: Optional[dict] = None
    status: Literal["processado", "pendente", "falha", "inconsistente"] = "processado"
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class CorrelatedLog(BaseModel):
    """Log correlacionado entre SharePoint e Sentinel"""
    correlation_id: str = Field(default_factory=lambda: str(uuid4()))
    sharepoint_event_id: Optional[str] = None
    sentinel_log_id: Optional[str] = None
    timestamp_created: datetime = Field(default_factory=datetime.now)
    integrity_status: Literal["ok", "correlacionado", "divergente", "pendente", "inconsistente"]
    hash_comparison: bool
    user: str
    project_id: str
    change_description: str
    justification: Optional[str] = None
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class HistoricoAlteracoes(BaseModel):
    """Registro no histórico de alterações do SharePoint"""
    historico_id: str = Field(default_factory=lambda: str(uuid4()))
    correlation_id: str
    timestamp: datetime = Field(default_factory=datetime.now)
    user: str
    project_id: str
    change_type: str
    justification: str
    status: Literal["aprovado", "bloqueado", "pendente"]
    sentinel_log_id: Optional[str] = None
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class AlertaSentinel(BaseModel):
    """Alerta gerado pelo Sentinel"""
    alert_id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    severity: Literal["low", "medium", "high", "critical"]
    title: str
    description: str
    affected_user: str
    affected_project: str
    correlation_id: Optional[str] = None
    recommended_action: str
    teams_notification_sent: bool = False
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class AuditTrail(BaseModel):
    """Trilha de auditoria completa"""
    audit_id: str = Field(default_factory=lambda: str(uuid4()))
    correlation_id: str
    timestamp_inicio: datetime
    timestamp_fim: datetime
    origem: str
    destino: str
    user: str
    project_id: str
    eventos_relacionados: list[str]
    status_final: str
    integridade_verificada: bool
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ChangeRequest(BaseModel):
    """Requisição de mudança vinda do Forms/SharePoint"""
    request_id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    user: str
    project_id: str
    change_type: str
    justification: Optional[str] = None
    field_to_change: str
    new_value: str
    approved: bool = False
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }

