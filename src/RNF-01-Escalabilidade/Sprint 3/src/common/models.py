"""Modelos Pydantic compartilhados"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
from datetime import datetime


class TransactionRequest(BaseModel):
    """Modelo para requisições de transação"""
    trace_id: str = Field(..., description="ID de rastreamento da transação")
    user_id: str = Field(..., description="ID do usuário")
    action: str = Field(..., description="Ação a ser executada")
    payload: Dict[str, Any] = Field(default_factory=dict, description="Dados da requisição")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp da requisição")


class TransactionResponse(BaseModel):
    """Modelo para respostas de transação"""
    trace_id: str = Field(..., description="ID de rastreamento da transação")
    status: str = Field(..., description="Status da transação (SUCCESS, FAILED, PENDING)")
    message: Optional[str] = Field(None, description="Mensagem descritiva")
    data: Optional[Dict[str, Any]] = Field(None, description="Dados de resposta")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp da resposta")


class AuditLog(BaseModel):
    """Modelo para logs de auditoria"""
    trace_id: str = Field(..., description="ID de rastreamento")
    event_type: str = Field(..., description="Tipo de evento")
    user_id: str = Field(..., description="ID do usuário")
    resource: str = Field(..., description="Recurso acessado")
    action: str = Field(..., description="Ação realizada")
    status: str = Field(..., description="Status da operação")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Timestamp do evento")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadados adicionais")
