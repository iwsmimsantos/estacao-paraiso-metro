"""Mock do Serviço de Auditoria"""
from fastapi import FastAPI, HTTPException
from typing import Dict, Any, List
import random
import time

from ..common.models import AuditLog, TransactionResponse
from ..common.trace import get_trace_id, set_trace_id
from ..common.logging_config import get_logger
from ..common.metrics import metrics_collector

logger = get_logger(__name__)
app = FastAPI(title="Audit Service Mock")

# Armazena logs em memória (simulação)
audit_logs: List[AuditLog] = []


@app.post("/log", response_model=TransactionResponse)
async def create_audit_log(log: AuditLog) -> TransactionResponse:
    """
    Registra um log de auditoria.
    
    Args:
        log: Dados do log de auditoria
    
    Returns:
        TransactionResponse: Resposta do registro
    """
    set_trace_id(log.trace_id)
    start_time = time.time()
    
    logger.info(f"Registro de auditoria para trace_id: {log.trace_id}")
    metrics_collector.increment_counter("audit_logs_total")
    
    try:
        # Simula processamento rápido (10-50ms)
        processing_time = random.uniform(0.01, 0.05)
        time.sleep(processing_time)
        
        # Simula falha em 0.5% dos casos
        if random.random() < 0.005:
            metrics_collector.increment_counter("audit_errors_total")
            raise HTTPException(status_code=500, detail="Audit log storage error")
        
        # Armazena o log
        audit_logs.append(log)
        
        response = TransactionResponse(
            trace_id=log.trace_id,
            status="SUCCESS",
            message="Audit log recorded",
            data={"log_id": len(audit_logs)}
        )
        
        elapsed = time.time() - start_time
        metrics_collector.record_metric("audit_request_duration_seconds", elapsed)
        metrics_collector.increment_counter("audit_success_total")
        
        logger.info(f"Auditoria registrada para trace_id: {log.trace_id} em {elapsed:.3f}s")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro inesperado na auditoria: {str(e)}")
        metrics_collector.increment_counter("audit_errors_total")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/logs/{trace_id}")
async def get_logs_by_trace(trace_id: str) -> List[AuditLog]:
    """
    Recupera logs de auditoria por trace_id.
    
    Args:
        trace_id: ID de rastreamento
    
    Returns:
        List[AuditLog]: Logs encontrados
    """
    return [log for log in audit_logs if log.trace_id == trace_id]


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "healthy", "service": "audit-mock"}


@app.get("/metrics")
async def get_metrics() -> Dict[str, Any]:
    """Endpoint de métricas"""
    return {
        **metrics_collector.get_summary(),
        "total_logs": len(audit_logs)
    }
