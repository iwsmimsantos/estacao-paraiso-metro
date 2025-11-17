"""Mock do SharePoint"""
from fastapi import FastAPI, HTTPException
from typing import Dict, Any
import random
import time

from ..common.models import TransactionRequest, TransactionResponse
from ..common.trace import get_trace_id, set_trace_id
from ..common.logging_config import get_logger
from ..common.metrics import metrics_collector

logger = get_logger(__name__)
app = FastAPI(title="SharePoint Mock")


@app.post("/upload", response_model=TransactionResponse)
async def upload_document(request: TransactionRequest) -> TransactionResponse:
    """
    Simula upload de documento no SharePoint.
    
    Args:
        request: Dados da requisição
    
    Returns:
        TransactionResponse: Resposta do upload
    """
    set_trace_id(request.trace_id)
    start_time = time.time()
    
    logger.info(f"Upload iniciado para trace_id: {request.trace_id}")
    metrics_collector.increment_counter("sharepoint_requests_total")
    
    try:
        # Simula processamento (100-300ms)
        processing_time = random.uniform(0.1, 0.3)
        time.sleep(processing_time)
        
        # Simula throttling mais frequente (5% dos casos)
        if random.random() < 0.05:
            metrics_collector.increment_counter("sharepoint_throttled_total")
            raise HTTPException(status_code=429, detail="SharePoint throttling")
        
        # Simula falha em 2% dos casos
        if random.random() < 0.02:
            metrics_collector.increment_counter("sharepoint_errors_total")
            raise HTTPException(status_code=500, detail="Storage error")
        
        response = TransactionResponse(
            trace_id=request.trace_id,
            status="SUCCESS",
            message="Document uploaded successfully",
            data={
                "document_id": f"doc_{random.randint(1000, 9999)}",
                "version": "1.0"
            }
        )
        
        elapsed = time.time() - start_time
        metrics_collector.record_metric("sharepoint_request_duration_seconds", elapsed)
        metrics_collector.increment_counter("sharepoint_success_total")
        
        logger.info(f"Upload concluído para trace_id: {request.trace_id} em {elapsed:.3f}s")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro inesperado no upload: {str(e)}")
        metrics_collector.increment_counter("sharepoint_errors_total")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "healthy", "service": "sharepoint-mock"}


@app.get("/metrics")
async def get_metrics() -> Dict[str, Any]:
    """Endpoint de métricas"""
    return metrics_collector.get_summary()
