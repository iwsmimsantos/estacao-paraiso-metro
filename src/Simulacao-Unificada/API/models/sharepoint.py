"""
Modelos Pydantic específicos da API do SharePoint.
"""

from typing import Optional
from pydantic import BaseModel, Field


class SharePointSite(BaseModel):
    """Site do SharePoint."""
    site_id: str = Field(..., description="ID único do site")
    name: str = Field(..., description="Nome do site")
    url: str = Field(..., description="URL do site")
    owner_user_id: str = Field(..., description="ID do usuário proprietário")
    created_at_utc: str = Field(..., description="Data de criação em UTC")
    sensitivity_label: str = Field(..., description="Label de sensibilidade")
    retention_policy: str = Field(..., description="Política de retenção")
    is_active: bool = Field(..., description="Se o site está ativo")
    
    class Config:
        json_schema_extra = {
            "example": {
                "site_id": "site-001",
                "name": "Portal de TI",
                "url": "https://empresa.sharepoint.com/sites/ti",
                "owner_user_id": "u001",
                "created_at_utc": "2025-01-15T10:00:00Z",
                "sensitivity_label": "Internal",
                "retention_policy": "3y",
                "is_active": True
            }
        }


class SharePointDocument(BaseModel):
    """Documento no SharePoint."""
    doc_id: str = Field(..., description="ID único do documento")
    site_id: str = Field(..., description="ID do site onde o documento está")
    name: str = Field(..., description="Nome do documento")
    path: str = Field(..., description="Caminho do documento")
    version: str = Field(..., description="Versão do documento")
    last_modified_at_utc: str = Field(..., description="Data da última modificação")
    last_modified_by_user_id: str = Field(..., description="ID do usuário que modificou")
    sensitivity_label: str = Field(..., description="Label de sensibilidade")
    checked_out_by_user_id: Optional[str] = Field(None, description="ID do usuário que fez checkout")
    is_encrypted_at_rest: bool = Field(..., description="Se está criptografado em repouso")
    sharing_links_count: int = Field(..., description="Número de links de compartilhamento")
    
    class Config:
        json_schema_extra = {
            "example": {
                "doc_id": "doc-001",
                "site_id": "site-001",
                "name": "Relatório Financeiro Q3.xlsx",
                "path": "/Documentos Compartilhados/Financeiro/",
                "version": "2.3",
                "last_modified_at_utc": "2025-11-20T14:30:00Z",
                "last_modified_by_user_id": "u002",
                "sensitivity_label": "Confidential",
                "checked_out_by_user_id": None,
                "is_encrypted_at_rest": True,
                "sharing_links_count": 2
            }
        }


class SharePointAuditLog(BaseModel):
    """Log de auditoria do SharePoint."""
    event_id: str = Field(..., description="ID único do evento")
    timestamp_utc: str = Field(..., description="Timestamp do evento")
    user_id: str = Field(..., description="ID do usuário")
    action: str = Field(..., description="Ação realizada")
    resource_type: str = Field(..., description="Tipo de recurso")
    resource_id: str = Field(..., description="ID do recurso")
    ip_address: str = Field(..., description="Endereço IP")
    device_id: str = Field(..., description="ID do dispositivo")
    success: bool = Field(..., description="Se a ação foi bem-sucedida")
    reason: Optional[str] = Field(None, description="Razão de falha, se aplicável")
    
    class Config:
        json_schema_extra = {
            "example": {
                "event_id": "sp-evt-001",
                "timestamp_utc": "2025-11-27T10:15:00Z",
                "user_id": "u001",
                "action": "FileDownloaded",
                "resource_type": "Document",
                "resource_id": "doc-001",
                "ip_address": "192.168.0.10",
                "device_id": "device-win-123",
                "success": True,
                "reason": None
            }
        }

