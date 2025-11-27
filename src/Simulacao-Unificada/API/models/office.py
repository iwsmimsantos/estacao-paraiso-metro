"""
Modelos Pydantic específicos da API do Microsoft 365 Office (Word, Excel, PowerPoint, Outlook).
"""

from typing import List, Optional
from pydantic import BaseModel, Field


class OfficeDocument(BaseModel):
    """Documento do Office (Word, Excel, PowerPoint)."""
    document_id: str = Field(..., description="ID único do documento")
    type: str = Field(..., description="Tipo: Word, Excel ou PowerPoint")
    owner_user_id: str = Field(..., description="ID do proprietário")
    created_at_utc: str = Field(..., description="Data de criação")
    last_modified_at_utc: str = Field(..., description="Última modificação")
    sensitivity_label: str = Field(..., description="Label de sensibilidade")
    retention_policy: str = Field(..., description="Política de retenção")
    is_shared_externally: bool = Field(..., description="Se compartilhado externamente")
    last_access_by_user_id: str = Field(..., description="Último acesso por usuário")
    name: str = Field(..., description="Nome do documento")
    
    class Config:
        json_schema_extra = {
            "example": {
                "document_id": "office-doc-001",
                "type": "Excel",
                "owner_user_id": "u002",
                "created_at_utc": "2025-10-15T10:00:00Z",
                "last_modified_at_utc": "2025-11-26T14:20:00Z",
                "sensitivity_label": "Confidential",
                "retention_policy": "3y",
                "is_shared_externally": False,
                "last_access_by_user_id": "u008",
                "name": "Budget_2026.xlsx"
            }
        }


class Email(BaseModel):
    """E-mail do Outlook."""
    email_id: str = Field(..., description="ID único do e-mail")
    subject: str = Field(..., description="Assunto do e-mail")
    sender_user_id: str = Field(..., description="ID do remetente")
    recipient_user_ids: List[str] = Field(..., description="IDs dos destinatários")
    sent_at_utc: str = Field(..., description="Data de envio")
    has_attachments: bool = Field(..., description="Se tem anexos")
    sensitivity_label: str = Field(..., description="Label de sensibilidade")
    is_phishing_suspected: bool = Field(..., description="Se suspeita de phishing")
    
    class Config:
        json_schema_extra = {
            "example": {
                "email_id": "email-001",
                "subject": "Revisão do Orçamento Trimestral",
                "sender_user_id": "u008",
                "recipient_user_ids": ["u001", "u002", "u005"],
                "sent_at_utc": "2025-11-27T08:30:00Z",
                "has_attachments": True,
                "sensitivity_label": "Confidential",
                "is_phishing_suspected": False
            }
        }


class CalendarEvent(BaseModel):
    """Evento de calendário do Outlook."""
    event_id: str = Field(..., description="ID único do evento")
    organizer_user_id: str = Field(..., description="ID do organizador")
    start_utc: str = Field(..., description="Início do evento")
    end_utc: str = Field(..., description="Fim do evento")
    subject: str = Field(..., description="Assunto do evento")
    attendee_user_ids: List[str] = Field(..., description="IDs dos participantes")
    location: Optional[str] = Field(None, description="Localização")
    is_online_meeting: bool = Field(..., description="Se é reunião online")
    meeting_url: Optional[str] = Field(None, description="URL da reunião")
    sensitivity_label: str = Field(..., description="Label de sensibilidade")
    
    class Config:
        json_schema_extra = {
            "example": {
                "event_id": "cal-evt-001",
                "organizer_user_id": "u001",
                "start_utc": "2025-11-28T14:00:00Z",
                "end_utc": "2025-11-28T15:00:00Z",
                "subject": "Reunião de Planejamento Estratégico",
                "attendee_user_ids": ["u001", "u005", "u007", "u010"],
                "location": "Sala de Conferência 3A",
                "is_online_meeting": True,
                "meeting_url": "https://teams.microsoft.com/meet/abc123",
                "sensitivity_label": "Confidential"
            }
        }

