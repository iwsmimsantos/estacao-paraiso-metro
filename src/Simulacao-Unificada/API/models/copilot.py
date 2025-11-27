"""
Modelos Pydantic específicos da API do Microsoft 365 Copilot.
"""

from typing import Optional, Dict
from pydantic import BaseModel, Field


class CopilotSession(BaseModel):
    """Sessão de uso do Copilot."""
    session_id: str = Field(..., description="ID único da sessão")
    user_id: str = Field(..., description="ID do usuário")
    tenant_id: str = Field(..., description="ID do tenant")
    started_at_utc: str = Field(..., description="Início da sessão")
    ended_at_utc: Optional[str] = Field(None, description="Fim da sessão")
    source_app: str = Field(..., description="Aplicativo de origem")
    total_prompts: int = Field(..., description="Total de prompts enviados")
    total_tokens_input: int = Field(..., description="Total de tokens de entrada")
    total_tokens_output: int = Field(..., description="Total de tokens de saída")
    sensitivity_context: Dict[str, bool] = Field(..., description="Contexto de sensibilidade")
    
    class Config:
        json_schema_extra = {
            "example": {
                "session_id": "copilot-sess-001",
                "user_id": "u002",
                "tenant_id": "tenant-01",
                "started_at_utc": "2025-11-27T09:00:00Z",
                "ended_at_utc": "2025-11-27T09:45:00Z",
                "source_app": "Excel",
                "total_prompts": 15,
                "total_tokens_input": 2340,
                "total_tokens_output": 1820,
                "sensitivity_context": {
                    "AccessedFinancialData": True,
                    "AccessedPII": False,
                    "AccessedConfidentialDocs": True
                }
            }
        }


class CopilotMessage(BaseModel):
    """Mensagem em uma sessão do Copilot."""
    message_id: str = Field(..., description="ID único da mensagem")
    timestamp_utc: str = Field(..., description="Timestamp da mensagem")
    role: str = Field(..., description="Papel: user, assistant ou system")
    content: str = Field(..., description="Conteúdo da mensagem")
    tokens_input: int = Field(..., description="Tokens de entrada")
    tokens_output: int = Field(..., description="Tokens de saída")
    related_resource_type: Optional[str] = Field(None, description="Tipo de recurso relacionado")
    related_resource_id: Optional[str] = Field(None, description="ID do recurso relacionado")
    
    class Config:
        json_schema_extra = {
            "example": {
                "message_id": "msg-001",
                "timestamp_utc": "2025-11-27T09:05:00Z",
                "role": "user",
                "content": "Crie uma tabela dinâmica com os dados de vendas por região",
                "tokens_input": 156,
                "tokens_output": 0,
                "related_resource_type": "Document",
                "related_resource_id": "doc-excel-001"
            }
        }


class CopilotAuditEvent(BaseModel):
    """Evento de auditoria do Copilot."""
    event_id: str = Field(..., description="ID único do evento")
    timestamp_utc: str = Field(..., description="Timestamp do evento")
    user_id: str = Field(..., description="ID do usuário")
    action: str = Field(..., description="Ação realizada")
    session_id: str = Field(..., description="ID da sessão")
    resource_type: Optional[str] = Field(None, description="Tipo de recurso")
    resource_id: Optional[str] = Field(None, description="ID do recurso")
    ip_address: str = Field(..., description="Endereço IP")
    device_id: str = Field(..., description="ID do dispositivo")
    success: bool = Field(..., description="Se a ação foi bem-sucedida")
    risk_detected: bool = Field(..., description="Se risco foi detectado")
    
    class Config:
        json_schema_extra = {
            "example": {
                "event_id": "copilot-evt-001",
                "timestamp_utc": "2025-11-27T09:05:00Z",
                "user_id": "u002",
                "action": "AccessedSensitiveData",
                "session_id": "copilot-sess-001",
                "resource_type": "Document",
                "resource_id": "doc-excel-001",
                "ip_address": "192.168.0.15",
                "device_id": "device-win-789",
                "success": True,
                "risk_detected": False
            }
        }

