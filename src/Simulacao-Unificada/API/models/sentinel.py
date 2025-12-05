"""
Modelos Pydantic específicos da API do Microsoft Sentinel.
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class SentinelIncident(BaseModel):
    """Incidente de segurança do Sentinel."""
    incident_id: str = Field(..., description="ID único do incidente")
    title: str = Field(..., description="Título do incidente")
    severity: str = Field(..., description="Severidade: Low, Medium, High ou Critical")
    status: str = Field(..., description="Status: Active ou Resolved")
    owner_user_id: str = Field(..., description="ID do responsável")
    created_at_utc: str = Field(..., description="Data de criação")
    updated_at_utc: str = Field(..., description="Data de atualização")
    related_alert_ids: List[str] = Field(..., description="IDs de alertas relacionados")
    tenant_id: str = Field(..., description="ID do tenant")
    description: str = Field(..., description="Descrição do incidente")
    
    class Config:
        json_schema_extra = {
            "example": {
                "incident_id": "incident-001",
                "title": "Acesso não autorizado a dados financeiros",
                "severity": "High",
                "status": "Active",
                "owner_user_id": "u001",
                "created_at_utc": "2025-11-27T08:15:00Z",
                "updated_at_utc": "2025-11-27T10:30:00Z",
                "related_alert_ids": ["alert-001", "alert-002", "alert-003"],
                "tenant_id": "tenant-01",
                "description": "Múltiplas tentativas de acesso a documentos financeiros confidenciais"
            }
        }


class SentinelAlert(BaseModel):
    """Alerta de segurança do Sentinel."""
    alert_id: str = Field(..., description="ID único do alerta")
    timestamp_utc: str = Field(..., description="Timestamp do alerta")
    source_service: str = Field(..., description="Serviço de origem")
    description: str = Field(..., description="Descrição do alerta")
    user_id: str = Field(..., description="ID do usuário envolvido")
    risk_level: str = Field(..., description="Nível de risco")
    related_resource_type: str = Field(..., description="Tipo de recurso relacionado")
    related_resource_id: str = Field(..., description="ID do recurso relacionado")
    correlation_id: str = Field(..., description="ID de correlação")
    ip_address: str = Field(..., description="Endereço IP")
    device_id: str = Field(..., description="ID do dispositivo")
    tenant_id: str = Field(..., description="ID do tenant")
    
    class Config:
        json_schema_extra = {
            "example": {
                "alert_id": "alert-001",
                "timestamp_utc": "2025-11-27T08:15:00Z",
                "source_service": "sharepoint",
                "description": "Download massivo de documentos confidenciais",
                "user_id": "u003",
                "risk_level": "high",
                "related_resource_type": "Document",
                "related_resource_id": "doc-025",
                "correlation_id": "corr-12345",
                "ip_address": "192.168.0.99",
                "device_id": "device-linux-555",
                "tenant_id": "tenant-01"
            }
        }


class SentinelEvent(BaseModel):
    """Evento de segurança normalizado do Sentinel."""
    event_id: str = Field(..., description="ID único do evento")
    timestamp_utc: str = Field(..., description="Timestamp do evento")
    source_service: str = Field(..., description="Serviço de origem")
    user_id: str = Field(..., description="ID do usuário")
    operation: str = Field(..., description="Operação realizada")
    status: str = Field(..., description="Status: Success ou Failure")
    ip_address: str = Field(..., description="Endereço IP")
    device_id: str = Field(..., description="ID do dispositivo")
    tenant_id: str = Field(..., description="ID do tenant")
    resource_type: Optional[str] = Field(None, description="Tipo de recurso")
    resource_id: Optional[str] = Field(None, description="ID do recurso")
    
    class Config:
        json_schema_extra = {
            "example": {
                "event_id": "evt-sentinel-001",
                "timestamp_utc": "2025-11-27T10:15:00Z",
                "source_service": "office",
                "user_id": "u002",
                "operation": "EmailSent",
                "status": "Success",
                "ip_address": "192.168.0.15",
                "device_id": "device-win-789",
                "tenant_id": "tenant-01",
                "resource_type": "Email",
                "resource_id": "email-045"
            }
        }

