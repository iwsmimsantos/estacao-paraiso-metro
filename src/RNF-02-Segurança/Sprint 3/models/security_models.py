"""
Modelos de dados para eventos e incidentes de segurança
"""
from datetime import datetime
from typing import Optional, Literal, List
from pydantic import BaseModel, Field
from uuid import uuid4


class AuthenticationToken(BaseModel):
    """Token de autenticação do usuário"""
    token_id: str = Field(default_factory=lambda: str(uuid4()))
    user_email: str
    user_id: str
    issued_at: datetime = Field(default_factory=datetime.now)
    expires_at: datetime
    is_valid: bool = True
    source: Literal["Microsoft Entra ID", "Token Registrado"] = "Microsoft Entra ID"
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ProjectPermission(BaseModel):
    """Permissão de usuário em um projeto específico"""
    permission_id: str = Field(default_factory=lambda: str(uuid4()))
    user_email: str
    user_id: str
    project_id: str
    portfolio_id: Optional[str] = None
    permission_level: Literal["Administrador", "Colaborador", "Visualizador"]
    granted_at: datetime = Field(default_factory=datetime.now)
    revoked_at: Optional[datetime] = None
    is_active: bool = True
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class AccessRequest(BaseModel):
    """Requisição de acesso a recursos do sistema"""
    request_id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    user_email: str
    user_id: str
    token: str
    requested_project_id: str
    requested_resource: str  # "documentos", "cronograma", "relatorios", etc.
    action: Literal["read", "write", "delete", "update"]
    source: str = "Middleware"
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class MiroAccessRequest(BaseModel):
    """Requisição de acesso ao Miro"""
    request_id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    user_email: Optional[str] = None
    user_id: Optional[str] = None
    token: Optional[str] = None
    miro_board_id: str
    miro_link: str
    project_id: str
    is_authenticated: bool = False
    source: str = "Miro Middleware"
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class ChecksumValidation(BaseModel):
    """Validação de checksum entre Miro e SharePoint"""
    validation_id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    project_id: str
    miro_data_hash: str
    sharepoint_data_hash: str
    miro_data_content: str
    sharepoint_data_content: str
    match_status: Literal["match", "mismatch", "pending"]
    whitespace_normalized: bool = True
    mismatch_details: Optional[str] = None
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class DataIntegrityCheck(BaseModel):
    """Verificação de integridade de dados entre sistemas"""
    check_id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    source_system: str  # "Miro", "SharePoint"
    target_system: str
    data_type: str  # "cronograma", "documento", "relatorio"
    project_id: str
    checksum_validation: Optional[ChecksumValidation] = None
    integrity_status: Literal["ok", "mismatch", "corrupted", "pending"]
    sync_blocked: bool = False
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class SecurityIncident(BaseModel):
    """Incidente de segurança registrado na incident queue"""
    incident_id: str = Field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = Field(default_factory=datetime.now)
    incident_type: Literal[
        "acesso_negado",
        "tentativa_acesso_indevedo",
        "inconsistencia_dados",
        "link_publico_bloqueado",
        "token_invalido",
        "permissao_incorreta"
    ]
    severity: Literal["low", "medium", "high", "critical"]
    user_email: Optional[str] = None
    user_id: Optional[str] = None
    project_id: Optional[str] = None
    description: str
    action_blocked: str
    source: str  # "Middleware", "Miro", "SharePoint"
    incident_queue_id: str = Field(default_factory=lambda: str(uuid4()))
    resolved: bool = False
    resolved_at: Optional[datetime] = None
    resolution_notes: Optional[str] = None
    metadata: Optional[dict] = None
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


