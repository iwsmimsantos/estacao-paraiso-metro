"""
API simulada do SharePoint/OfficeActivity
"""
from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import Optional

from models.log_models import SharePointChangeEvent, ChangeRequest
from services.mock_data_generator import mock_generator
from services.correlation_service import correlation_service

router = APIRouter(prefix="/sharepoint", tags=["SharePoint"])


@router.post("/events/change")
async def create_change_event(request: ChangeRequest):
    """
    Simula criação de evento de mudança no SharePoint
    
    Este endpoint representa a captura de uma mudança em uma lista do SharePoint,
    que seria normalmente acionada via Power Automate
    """
    # Cria evento do SharePoint
    event = SharePointChangeEvent(
        user=request.user,
        project_id=request.project_id,
        change_type=request.change_type,
        justification=request.justification,
        field_changed=request.field_to_change,
        old_value=None,  # Seria recuperado do SharePoint real
        new_value=request.new_value,
        source="SharePoint"
    )
    
    # Processa através do middleware de correlação
    result = correlation_service.process_sharepoint_event(event)
    
    return {
        "message": "Evento de mudança processado",
        "event_id": event.event_id,
        "timestamp": event.timestamp,
        "result": result
    }


@router.post("/events/simulate-change")
async def simulate_random_change(
    with_justification: bool = True,
    scenario: str = "default"
):
    """
    Simula uma mudança aleatória realista no SharePoint
    
    Args:
        with_justification: Se deve incluir justificativa
        scenario: Cenário de teste (cenario_1 a cenario_5)
    """
    # Gera dados mockados realistas
    user = mock_generator.generate_user()
    project_id = mock_generator.generate_project_id()
    change_type = mock_generator.generate_change_type()
    field, old_val, new_val = mock_generator.generate_field_change()
    justification = mock_generator.generate_justification(with_justification)
    
    # Cria evento
    event = SharePointChangeEvent(
        user=user,
        project_id=project_id,
        change_type=change_type,
        justification=justification,
        field_changed=field,
        old_value=old_val,
        new_value=new_val,
        source="SharePoint"
    )
    
    # Processa
    result = correlation_service.process_sharepoint_event(event, scenario)
    
    return {
        "message": "Mudança simulada processada",
        "event_id": event.event_id,
        "timestamp": event.timestamp,
        "details": {
            "user": user,
            "project_id": project_id,
            "change_type": change_type,
            "field_changed": field,
            "old_value": old_val,
            "new_value": new_val,
            "justification": justification,
            "blocked": result.get("blocked", False)
        },
        "result": result
    }


@router.get("/events")
async def list_sharepoint_events(
    project_id: Optional[str] = None,
    user: Optional[str] = None,
    limit: int = 50
):
    """Lista eventos do SharePoint"""
    from storage.log_repository import log_repository
    
    filter_by = {}
    if project_id:
        filter_by["project_id"] = project_id
    if user:
        filter_by["user"] = user
    
    events = log_repository.get_sharepoint_events(filter_by)
    
    return {
        "total": len(events),
        "events": events[:limit]
    }


@router.get("/historico-alteracoes")
async def get_historico_alteracoes(
    project_id: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 50
):
    """
    Recupera histórico de alterações do SharePoint
    
    Simula a lista "Histórico de Alterações" mencionada no cenário
    """
    from storage.log_repository import log_repository
    
    filter_by = {}
    if project_id:
        filter_by["project_id"] = project_id
    if status:
        filter_by["status"] = status
    
    historico = log_repository.get_historico_alteracoes(filter_by)
    
    return {
        "total": len(historico),
        "historico": historico[:limit],
        "message": "Histórico de Alterações recuperado do SharePoint"
    }


@router.post("/lists/update-project")
async def update_project_field(
    project_id: str,
    field: str,
    new_value: str,
    user: str,
    justification: Optional[str] = None
):
    """
    Simula atualização direta de campo em lista do SharePoint
    
    Representa a operação que seria bloqueada se não houver justificativa
    """
    if not justification or justification.strip() == "":
        return {
            "success": False,
            "blocked": True,
            "message": "Atualização bloqueada - justificativa obrigatória",
            "power_automate_action": "Fluxo impediu a atualização"
        }
    
    # Simula atualização bem-sucedida
    event = SharePointChangeEvent(
        user=user,
        project_id=project_id,
        change_type="atualizacao",
        justification=justification,
        field_changed=field,
        old_value="valor_anterior",  # Seria recuperado do SharePoint
        new_value=new_value,
        source="SharePoint"
    )
    
    result = correlation_service.process_sharepoint_event(event)
    
    return {
        "success": True,
        "blocked": False,
        "message": f"Campo '{field}' atualizado com sucesso no projeto {project_id}",
        "event_id": event.event_id,
        "correlation_id": result.get("correlation_id"),
        "power_automate_action": "Fluxo registrou mudança e notificou Sentinel"
    }

