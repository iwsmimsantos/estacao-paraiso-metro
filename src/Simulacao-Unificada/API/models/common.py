"""
Modelos Pydantic comuns compartilhados entre todas as APIs.
Define o envelope de resposta padrão e estruturas de metadados.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class SecurityContext(BaseModel):
    """Contexto de segurança da requisição."""
    user_id: str = Field(..., description="ID do usuário que fez a requisição")
    tenant_id: str = Field(..., description="ID do tenant")
    mfa_required: bool = Field(..., description="Se MFA é obrigatório")
    mfa_enabled: bool = Field(..., description="Se o usuário tem MFA habilitado")
    ip_address: str = Field(..., description="Endereço IP de origem")
    device_id: str = Field(..., description="ID do dispositivo")
    auth_method: str = Field(default="OAuth2_Bearer", description="Método de autenticação")
    scopes: List[str] = Field(default_factory=list, description="Escopos de permissão")
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "u001",
                "tenant_id": "tenant-01",
                "mfa_required": True,
                "mfa_enabled": True,
                "ip_address": "192.168.0.10",
                "device_id": "device-xyz-123",
                "auth_method": "OAuth2_Bearer",
                "scopes": ["Files.Read.All", "Sites.Read.All"]
            }
        }


class TraceabilityContext(BaseModel):
    """Contexto de rastreabilidade para correlação entre sistemas."""
    trace_id: str = Field(..., description="ID de trace distribuído")
    span_id: str = Field(..., description="ID do span atual")
    source_system: str = Field(default="mock-api", description="Sistema de origem")
    ingested_at_utc: str = Field(..., description="Timestamp de ingestão em UTC")
    
    class Config:
        json_schema_extra = {
            "example": {
                "trace_id": "550e8400-e29b-41d4-a716-446655440000",
                "span_id": "660e8400-e29b-41d4-a716-446655440001",
                "source_system": "mock-api",
                "ingested_at_utc": "2025-11-27T10:15:00Z"
            }
        }


class PerformanceMetrics(BaseModel):
    """Métricas de performance simuladas."""
    processing_time_ms: int = Field(..., description="Tempo de processamento em ms")
    items_in_response: int = Field(..., description="Número de itens na resposta")
    
    class Config:
        json_schema_extra = {
            "example": {
                "processing_time_ms": 23,
                "items_in_response": 10
            }
        }


class ResponseMeta(BaseModel):
    """Metadados da resposta incluindo paginação e contextos."""
    page: Optional[int] = Field(None, description="Número da página atual")
    page_size: Optional[int] = Field(None, description="Tamanho da página")
    total_items: Optional[int] = Field(None, description="Total de itens disponíveis")
    security_context: SecurityContext = Field(..., description="Contexto de segurança")
    traceability: TraceabilityContext = Field(..., description="Contexto de rastreabilidade")
    performance: PerformanceMetrics = Field(..., description="Métricas de performance")


class StandardResponse(BaseModel):
    """
    Envelope padrão de resposta usado por todas as APIs.
    Garante consistência e facilita o consumo pelo middleware.
    """
    request_id: str = Field(..., description="ID único da requisição")
    service: str = Field(..., description="Nome do serviço que respondeu")
    timestamp_utc: str = Field(..., description="Timestamp da resposta em UTC")
    correlation_id: str = Field(..., description="ID de correlação entre serviços")
    data: Any = Field(..., description="Dados específicos da resposta")
    meta: ResponseMeta = Field(..., description="Metadados da resposta")
    
    class Config:
        json_schema_extra = {
            "example": {
                "request_id": "req-123456",
                "service": "sharepoint",
                "timestamp_utc": "2025-11-27T10:15:00Z",
                "correlation_id": "corr-789012",
                "data": {},
                "meta": {
                    "page": 1,
                    "page_size": 20,
                    "total_items": 120,
                    "security_context": {
                        "user_id": "u001",
                        "tenant_id": "tenant-01",
                        "mfa_required": True,
                        "mfa_enabled": True,
                        "ip_address": "192.168.0.10",
                        "device_id": "device-xyz-123",
                        "auth_method": "OAuth2_Bearer",
                        "scopes": ["Files.Read.All"]
                    },
                    "traceability": {
                        "trace_id": "trace-001",
                        "span_id": "span-001",
                        "source_system": "mock-api",
                        "ingested_at_utc": "2025-11-27T10:15:00Z"
                    },
                    "performance": {
                        "processing_time_ms": 23,
                        "items_in_response": 10
                    }
                }
            }
        }


class User(BaseModel):
    """Modelo de usuário baseado no CSV."""
    user_id: str
    display_name: str
    email: str
    department: str
    role: str
    risk_level: str
    is_active: bool
    last_login_utc: str
    mfa_enabled: bool
    tenant_id: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "u001",
                "display_name": "Ana Souza",
                "email": "ana.souza@empresa.com",
                "department": "TI",
                "role": "Administrador",
                "risk_level": "high",
                "is_active": True,
                "last_login_utc": "2025-11-20T13:45:00Z",
                "mfa_enabled": True,
                "tenant_id": "tenant-01"
            }
        }


class AuditEvent(BaseModel):
    """Evento de auditoria genérico."""
    event_id: str
    timestamp_utc: str
    user_id: str
    action: str
    resource_type: str
    resource_id: str
    ip_address: str
    device_id: str
    success: bool
    reason: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "event_id": "evt-001",
                "timestamp_utc": "2025-11-27T10:15:00Z",
                "user_id": "u001",
                "action": "FileViewed",
                "resource_type": "Document",
                "resource_id": "doc-123",
                "ip_address": "192.168.0.10",
                "device_id": "device-xyz-123",
                "success": True,
                "reason": None
            }
        }

