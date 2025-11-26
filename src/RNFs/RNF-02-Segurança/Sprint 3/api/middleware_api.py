"""
API do Middleware de Segurança
"""
from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import Optional

from models.security_models import AccessRequest, MiroAccessRequest
from services.auth_service import auth_service
from services.access_control_service import access_control_service
from services.mock_data_generator import mock_generator

router = APIRouter(prefix="/middleware", tags=["Middleware"])


@router.post("/access/check")
async def check_access(request: AccessRequest):
    """
    Verifica acesso de usuário a recursos do projeto
    
    Este endpoint simula o middleware que valida tokens e permissões
    antes de permitir acesso a documentos, cronogramas, etc.
    """
    result = access_control_service.check_access(request)
    
    return {
        "request_id": request.request_id,
        "timestamp": request.timestamp,
        "result": result
    }


@router.post("/miro/access/check")
async def check_miro_access(request: MiroAccessRequest):
    """
    Verifica acesso ao Miro
    
    Este endpoint simula o middleware que intercepta requisições ao Miro
    e valida autenticação e permissões antes de permitir acesso.
    """
    result = access_control_service.check_miro_access(request)
    
    return {
        "request_id": request.request_id,
        "timestamp": request.timestamp,
        "result": result
    }


@router.post("/auth/token/register")
async def register_token(user_email: str, user_id: Optional[str] = None):
    """
    Registra um novo token de autenticação
    
    Simula o processo de autenticação via Microsoft Entra ID
    """
    if not user_id:
        user = mock_generator.generate_user()
        user_id = user["user_id"]
        user_email = user["email"]
    
    token_result = auth_service.register_token(
        user_id=user_id,
        user_email=user_email
    )
    
    token = token_result["auth_token"]
    
    return {
        "token": token_result["token_value"],
        "token_id": token.token_id,
        "user_id": token.user_id,
        "user_email": token.user_email,
        "issued_at": token.issued_at,
        "expires_at": token.expires_at,
        "source": token.source
    }


@router.post("/auth/token/validate")
async def validate_token(token: str):
    """
    Valida um token de autenticação
    """
    result = auth_service.validate_token(token)
    
    return result


@router.post("/permissions/register")
async def register_permission(
    user_email: str,
    user_id: str,
    project_id: str,
    permission_level: str = "Colaborador"
):
    """
    Registra permissão de usuário em um projeto
    """
    from models.security_models import ProjectPermission
    
    permission = ProjectPermission(
        user_email=user_email,
        user_id=user_id,
        project_id=project_id,
        permission_level=permission_level
    )
    
    registered = access_control_service.register_permission(permission)
    
    return {
        "permission_id": registered.permission_id,
        "user_email": registered.user_email,
        "user_id": registered.user_id,
        "project_id": registered.project_id,
        "permission_level": registered.permission_level,
        "granted_at": registered.granted_at,
        "is_active": registered.is_active
    }


@router.get("/incidents")
async def get_incidents(
    project_id: Optional[str] = None,
    incident_type: Optional[str] = None,
    resolved: Optional[bool] = None
):
    """
    Lista incidentes da incident queue
    """
    from storage.incident_repository import incident_repository
    
    filter_by = {}
    if project_id:
        filter_by["project_id"] = project_id
    if incident_type:
        filter_by["incident_type"] = incident_type
    if resolved is not None:
        filter_by["resolved"] = resolved
    
    incidents = incident_repository.get_incidents(filter_by if filter_by else None)
    
    return {
        "total": len(incidents),
        "incidents": incidents
    }


@router.get("/statistics")
async def get_statistics():
    """
    Retorna estatísticas de segurança
    """
    from storage.incident_repository import incident_repository
    
    stats = incident_repository.get_statistics()
    
    return {
        "timestamp": datetime.now().isoformat(),
        "statistics": stats
    }

