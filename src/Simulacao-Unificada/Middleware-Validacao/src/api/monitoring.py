"""
Endpoints de Monitoramento e Logs

Rotas para consultar logs, incident queue e métricas do sistema.
"""
from fastapi import APIRouter, Query
from typing import Optional, List, Dict, Any

from ..monitoring.logger import logger, EventType


router = APIRouter(prefix="/monitoring", tags=["Monitoramento"])


@router.get("/logs")
async def get_logs(
    limit: int = Query(50, ge=1, le=500, description="Número máximo de logs"),
    user_id: Optional[str] = Query(None, description="Filtrar por usuário"),
    event_type: Optional[str] = Query(None, description="Filtrar por tipo de evento"),
    status: Optional[str] = Query(None, description="Filtrar por status (success, failed, denied)")
):
    """
    Recupera logs de auditoria com filtros opcionais
    
    Retorna os logs mais recentes primeiro
    """
    logs = logger.get_logs(
        limit=limit,
        user_id=user_id,
        event_type=event_type,
        status=status
    )
    
    return {
        "total": len(logs),
        "limit": limit,
        "filters": {
            "user_id": user_id,
            "event_type": event_type,
            "status": status
        },
        "logs": logs
    }


@router.get("/logs/trace/{trace_id}")
async def get_log_by_trace(trace_id: str):
    """Busca log específico por trace_id"""
    log = logger.get_log_by_trace_id(trace_id)
    
    if not log:
        return {
            "found": False,
            "trace_id": trace_id,
            "message": "Log não encontrado"
        }
    
    return {
        "found": True,
        "log": log
    }


@router.get("/logs/correlation/{correlation_id}")
async def get_logs_by_correlation(correlation_id: str):
    """
    Busca todos os logs de uma mesma transação (correlation_id)
    
    Útil para rastrear uma operação completa que gerou múltiplos eventos
    """
    logs = logger.get_logs_by_correlation_id(correlation_id)
    
    return {
        "correlation_id": correlation_id,
        "total": len(logs),
        "logs": logs
    }


@router.get("/incidents")
async def get_incidents(
    limit: int = Query(50, ge=1, le=500, description="Número máximo de incidentes"),
    severity: Optional[str] = Query(None, description="Filtrar por severidade (low, medium, high, critical)")
):
    """
    Recupera incident queue com incidentes de segurança
    
    Incidentes incluem:
    - Tentativas de acesso negado
    - Violações de guardrails de IA
    - Inconsistências de dados (mismatch)
    - Erros críticos do sistema
    """
    incidents = logger.get_incidents(
        limit=limit,
        severity=severity
    )
    
    return {
        "total": len(incidents),
        "limit": limit,
        "severity_filter": severity,
        "incidents": incidents
    }


@router.get("/stats")
async def get_statistics():
    """
    Retorna estatísticas gerais do sistema
    
    Inclui contadores de eventos, taxa de erro, usuários ativos, etc.
    """
    all_logs = logger.get_logs(limit=1000)
    all_incidents = logger.get_incidents(limit=1000)
    
    # Conta eventos por tipo
    event_counts = {}
    status_counts = {"success": 0, "failed": 0, "denied": 0, "incident": 0}
    user_activity = {}
    
    for log in all_logs:
        # Verifica se é um dict válido (ignora dados corrompidos)
        if not isinstance(log, dict):
            continue
            
        event_type = log.get("event_type", "unknown")
        event_counts[event_type] = event_counts.get(event_type, 0) + 1
        
        status = log.get("status", "unknown")
        if status in status_counts:
            status_counts[status] += 1
        
        user_id = log.get("user_id")
        if user_id:
            user_activity[user_id] = user_activity.get(user_id, 0) + 1
    
    # Conta incidentes por severidade
    incident_severity = {"low": 0, "medium": 0, "high": 0, "critical": 0}
    for incident in all_incidents:
        # Verifica se é um dict válido
        if not isinstance(incident, dict):
            continue
            
        severity = incident.get("details", {}).get("severity", "unknown")
        if severity in incident_severity:
            incident_severity[severity] += 1
    
    # Calcula taxa de erro
    total_operations = sum(status_counts.values())
    error_rate = 0
    if total_operations > 0:
        error_rate = round((status_counts["failed"] + status_counts["denied"]) / total_operations * 100, 2)
    
    return {
        "summary": {
            "total_logs": len(all_logs),
            "total_incidents": len(all_incidents),
            "total_operations": total_operations,
            "error_rate_percent": error_rate
        },
        "status_counts": status_counts,
        "event_counts": event_counts,
        "incident_severity": incident_severity,
        "top_users": sorted(user_activity.items(), key=lambda x: x[1], reverse=True)[:10]
    }


@router.get("/event-types")
async def get_event_types():
    """Lista todos os tipos de eventos suportados pelo sistema"""
    return {
        "event_types": [
            {
                "name": event.name,
                "value": event.value,
                "category": event.value.split('.')[0]
            }
            for event in EventType
        ]
    }
