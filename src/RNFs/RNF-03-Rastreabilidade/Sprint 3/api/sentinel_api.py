"""
API simulada do Microsoft Sentinel (SIEM)
"""
from fastapi import APIRouter, HTTPException
from datetime import datetime
from typing import Optional, List

from storage.log_repository import log_repository
from services.correlation_service import correlation_service

router = APIRouter(prefix="/sentinel", tags=["Sentinel"])


@router.get("/logs")
async def get_sentinel_logs(
    correlation_id: Optional[str] = None,
    project_id: Optional[str] = None,
    event_type: Optional[str] = None,
    severity: Optional[str] = None,
    limit: int = 100
):
    """
    Recupera logs do Sentinel
    
    Simula consulta ao Log Analytics Workspace do Sentinel
    """
    filter_by = {}
    if correlation_id:
        filter_by["correlation_id"] = correlation_id
    if project_id:
        filter_by["project_id"] = project_id
    if event_type:
        filter_by["event_type"] = event_type
    if severity:
        filter_by["severity"] = severity
    
    logs = log_repository.get_sentinel_logs(filter_by)
    
    return {
        "total": len(logs),
        "logs": logs[:limit],
        "workspace": "log-analytics-metrosp-prod",
        "query_time": datetime.now().isoformat()
    }


@router.get("/logs/{log_id}")
async def get_log_by_id(log_id: str):
    """Recupera log específico por ID"""
    logs = log_repository.get_sentinel_logs({"log_id": log_id})
    
    if not logs:
        raise HTTPException(status_code=404, detail="Log não encontrado")
    
    return {
        "log": logs[0],
        "workspace": "log-analytics-metrosp-prod"
    }


@router.get("/alerts")
async def get_alerts(
    severity: Optional[str] = None,
    project_id: Optional[str] = None,
    limit: int = 50
):
    """
    Lista alertas do Sentinel
    
    Simula os alertas de segurança e auditoria gerados pelo Sentinel
    """
    filter_by = {}
    if severity:
        filter_by["severity"] = severity
    if project_id:
        filter_by["affected_project"] = project_id
    
    alertas = log_repository.get_alertas(filter_by)
    
    # Agrupa por severidade
    by_severity = {
        "critical": len([a for a in alertas if a.get("severity") == "critical"]),
        "high": len([a for a in alertas if a.get("severity") == "high"]),
        "medium": len([a for a in alertas if a.get("severity") == "medium"]),
        "low": len([a for a in alertas if a.get("severity") == "low"])
    }
    
    return {
        "total": len(alertas),
        "by_severity": by_severity,
        "alerts": alertas[:limit],
        "workspace": "log-analytics-metrosp-prod"
    }


@router.get("/alerts/{alert_id}")
async def get_alert_by_id(alert_id: str):
    """Recupera alerta específico"""
    alertas = log_repository.get_alertas({"alert_id": alert_id})
    
    if not alertas:
        raise HTTPException(status_code=404, detail="Alerta não encontrado")
    
    return {
        "alert": alertas[0],
        "workspace": "log-analytics-metrosp-prod"
    }


@router.post("/simulate-invalid-attempt")
async def simulate_invalid_attempt(
    user: str,
    project_id: str,
    reason: str = "Tentativa de alteração fora do fluxo autorizado"
):
    """
    Simula detecção de tentativa inválida pelo Sentinel
    
    Representa quando o Sentinel detecta uma anomalia ou tentativa não autorizada
    """
    result = correlation_service.generate_alert_for_invalid_attempt(
        user=user,
        project_id=project_id,
        reason=reason
    )
    
    return {
        "message": "Tentativa inválida detectada e alertada",
        "alert_generated": True,
        "result": result,
        "sentinel_action": "Alerta crítico gerado e Teams notificado"
    }


@router.get("/correlation/{correlation_id}")
async def get_correlated_events(correlation_id: str):
    """
    Recupera todos os eventos correlacionados por ID
    
    Simula a capacidade do Sentinel de correlacionar eventos de múltiplas fontes
    """
    related = log_repository.get_by_correlation_id(correlation_id)
    
    if not related.get("sentinel_logs"):
        raise HTTPException(
            status_code=404,
            detail=f"Nenhum evento encontrado para correlation_id: {correlation_id}"
        )
    
    return {
        "correlation_id": correlation_id,
        "events_found": {
            "sharepoint": len(related["sharepoint_events"]),
            "sentinel_logs": len(related["sentinel_logs"]),
            "correlated_logs": len(related["correlated_logs"]),
            "historico": len(related["historico_alteracoes"]),
            "alerts": len(related["alertas"])
        },
        "data": related,
        "message": "Eventos correlacionados recuperados com sucesso"
    }


@router.get("/integrity/verify")
async def verify_integrity(
    sharepoint_event_id: str,
    sentinel_log_id: str
):
    """
    Verifica integridade entre evento SharePoint e log Sentinel
    
    Simula a validação de hash e correlação que o Sentinel realizaria
    """
    result = correlation_service.verify_integrity(
        sharepoint_event_id=sharepoint_event_id,
        sentinel_log_id=sentinel_log_id
    )
    
    return {
        "verification": result,
        "sentinel_action": "Verificação de integridade executada",
        "workspace": "log-analytics-metrosp-prod"
    }


@router.post("/audit-trail/create")
async def create_audit_trail(correlation_id: str):
    """
    Cria trilha de auditoria completa para um correlation_id
    
    Simula a geração de um relatório de auditoria no Sentinel
    """
    result = correlation_service.create_audit_trail(correlation_id)
    
    if not result.get("success"):
        raise HTTPException(status_code=404, detail=result.get("message"))
    
    return {
        "message": "Trilha de auditoria criada",
        "result": result,
        "sentinel_action": "Audit trail gerada e disponível para Power BI"
    }


@router.get("/audit-trails")
async def get_audit_trails(
    project_id: Optional[str] = None,
    user: Optional[str] = None,
    limit: int = 50
):
    """Lista trilhas de auditoria"""
    filter_by = {}
    if project_id:
        filter_by["project_id"] = project_id
    if user:
        filter_by["user"] = user
    
    trails = log_repository.get_audit_trails(filter_by)
    
    return {
        "total": len(trails),
        "audit_trails": trails[:limit],
        "workspace": "log-analytics-metrosp-prod"
    }


@router.get("/dashboard/statistics")
async def get_dashboard_statistics():
    """
    Retorna estatísticas para dashboards do Sentinel
    
    Simula dados que seriam visualizados no Sentinel Workbook ou Power BI
    """
    stats = log_repository.get_statistics()
    
    alertas = log_repository.get_alertas()
    alertas_by_severity = {
        "critical": len([a for a in alertas if a.get("severity") == "critical"]),
        "high": len([a for a in alertas if a.get("severity") == "high"]),
        "medium": len([a for a in alertas if a.get("severity") == "medium"]),
        "low": len([a for a in alertas if a.get("severity") == "low"])
    }
    
    logs = log_repository.get_sentinel_logs()
    logs_by_type = {
        "mudanca_aprovada": len([l for l in logs if l.get("event_type") == "mudanca_aprovada"]),
        "bloqueio": len([l for l in logs if l.get("event_type") == "bloqueio"]),
        "tentativa_invalida": len([l for l in logs if l.get("event_type") == "tentativa_invalida"]),
        "alerta": len([l for l in logs if l.get("event_type") == "alerta"]),
        "auditoria": len([l for l in logs if l.get("event_type") == "auditoria"])
    }
    
    correlated = log_repository.get_correlated_logs()
    integrity_status = {
        "ok": len([c for c in correlated if c.get("integrity_status") == "ok"]),
        "correlacionado": len([c for c in correlated if c.get("integrity_status") == "correlacionado"]),
        "divergente": len([c for c in correlated if c.get("integrity_status") == "divergente"]),
        "pendente": len([c for c in correlated if c.get("integrity_status") == "pendente"]),
        "inconsistente": len([c for c in correlated if c.get("integrity_status") == "inconsistente"])
    }
    
    return {
        "timestamp": datetime.now().isoformat(),
        "workspace": "log-analytics-metrosp-prod",
        "statistics": stats,
        "alertas_by_severity": alertas_by_severity,
        "logs_by_type": logs_by_type,
        "integrity_status": integrity_status,
        "message": "Estatísticas agregadas do Sentinel"
    }


@router.delete("/data/clear")
async def clear_all_data():
    """
    Limpa todos os dados do repositório (útil para testes)
    """
    log_repository.clear_all()
    
    return {
        "message": "Todos os dados foram limpos",
        "sentinel_action": "Log Analytics limpo (apenas simulação)"
    }

