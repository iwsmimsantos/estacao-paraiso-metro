"""
Modelos Pydantic específicos da API do Miro.
"""

from pydantic import BaseModel, Field


class MiroBoard(BaseModel):
    """Board do Miro."""
    board_id: str = Field(..., description="ID único do board")
    name: str = Field(..., description="Nome do board")
    owner_user_id: str = Field(..., description="ID do proprietário")
    created_at_utc: str = Field(..., description="Data de criação")
    last_activity_utc: str = Field(..., description="Data da última atividade")
    access_level: str = Field(..., description="Nível de acesso: private, team ou public")
    sensitivity_label: str = Field(..., description="Label de sensibilidade")
    tenant_id: str = Field(..., description="ID do tenant")
    
    class Config:
        json_schema_extra = {
            "example": {
                "board_id": "board-001",
                "name": "Sprint Planning Q4",
                "owner_user_id": "u004",
                "created_at_utc": "2025-10-01T09:00:00Z",
                "last_activity_utc": "2025-11-26T16:45:00Z",
                "access_level": "team",
                "sensitivity_label": "Internal",
                "tenant_id": "tenant-01"
            }
        }


class MiroActivity(BaseModel):
    """Atividade em um board do Miro."""
    activity_id: str = Field(..., description="ID único da atividade")
    timestamp_utc: str = Field(..., description="Timestamp da atividade")
    user_id: str = Field(..., description="ID do usuário")
    action: str = Field(..., description="Ação realizada")
    details: str = Field(..., description="Detalhes da ação")
    ip_address: str = Field(..., description="Endereço IP")
    device_id: str = Field(..., description="ID do dispositivo")
    
    class Config:
        json_schema_extra = {
            "example": {
                "activity_id": "miro-act-001",
                "timestamp_utc": "2025-11-26T16:45:00Z",
                "user_id": "u004",
                "action": "CardCreated",
                "details": "Card 'Implementar API Gateway' criado na coluna To Do",
                "ip_address": "192.168.0.25",
                "device_id": "device-mac-456"
            }
        }


class MiroAuditLog(BaseModel):
    """Log de auditoria do Miro."""
    event_id: str = Field(..., description="ID único do evento")
    timestamp_utc: str = Field(..., description="Timestamp do evento")
    user_id: str = Field(..., description="ID do usuário")
    action: str = Field(..., description="Ação realizada")
    resource_type: str = Field(..., description="Tipo de recurso")
    resource_id: str = Field(..., description="ID do recurso")
    ip_address: str = Field(..., description="Endereço IP")
    device_id: str = Field(..., description="ID do dispositivo")
    success: bool = Field(..., description="Se a ação foi bem-sucedida")
    
    class Config:
        json_schema_extra = {
            "example": {
                "event_id": "miro-evt-001",
                "timestamp_utc": "2025-11-26T16:45:00Z",
                "user_id": "u004",
                "action": "BoardShared",
                "resource_type": "Board",
                "resource_id": "board-001",
                "ip_address": "192.168.0.25",
                "device_id": "device-mac-456",
                "success": True
            }
        }

