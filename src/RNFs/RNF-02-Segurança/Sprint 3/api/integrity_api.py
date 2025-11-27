"""
API de Verificação de Integridade de Dados
"""
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

from services.integrity_service import integrity_service
from storage.incident_repository import incident_repository

router = APIRouter(prefix="/integrity", tags=["Integridade"])


class IntegrityCheckRequest(BaseModel):
    """Requisição de verificação de integridade"""
    project_id: str
    miro_data: str
    sharepoint_data: str
    data_type: str = "cronograma"


@router.post("/validate")
async def validate_integrity(request: IntegrityCheckRequest):
    """
    Valida integridade entre dados do Miro e SharePoint
    
    Este endpoint simula a verificação automática de consistência
    entre dados exportados do Miro e armazenados no SharePoint.
    """
    result = integrity_service.validate_data_integrity(
        project_id=request.project_id,
        miro_data=request.miro_data,
        sharepoint_data=request.sharepoint_data,
        data_type=request.data_type
    )
    
    return {
        "project_id": request.project_id,
        "data_type": request.data_type,
        "result": result
    }


@router.post("/compare")
async def compare_data(miro_data: str, sharepoint_data: str):
    """
    Compara dados com detalhes das diferenças (para debug)
    """
    result = integrity_service.compare_data_with_details(
        miro_data=miro_data,
        sharepoint_data=sharepoint_data
    )
    
    return result


@router.get("/checksum-validations")
async def get_checksum_validations(project_id: Optional[str] = None):
    """
    Lista validações de checksum
    """
    filter_by = {"project_id": project_id} if project_id else None
    validations = incident_repository.get_checksum_validations(filter_by)
    
    return {
        "total": len(validations),
        "validations": validations
    }


@router.get("/integrity-checks")
async def get_integrity_checks(project_id: Optional[str] = None):
    """
    Lista verificações de integridade
    """
    filter_by = {"project_id": project_id} if project_id else None
    checks = incident_repository.get_integrity_checks(filter_by)
    
    return {
        "total": len(checks),
        "checks": checks
    }


