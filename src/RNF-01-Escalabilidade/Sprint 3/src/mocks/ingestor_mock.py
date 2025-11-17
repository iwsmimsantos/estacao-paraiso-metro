"""Mock do Ingestor Miro"""
from fastapi import FastAPI, HTTPException
from typing import Dict, Any
import random
import time

from ..common.models import TransactionRequest, TransactionResponse
from ..common.trace import get_trace_id, set_trace_id
from ..common.logging_config import get_logger
from ..common.metrics import metrics_collector

logger = get_logger(__name__)
app = FastAPI(title="Ingestor Miro Mock")


@app.post("/ingest", response_model=TransactionResponse)
async def ingest_data(request: TransactionRequest) -> TransactionResponse:
    """
    Simula a ingestão de dados do Miro.
    
    Args:
        request: Dados da requisição
    
    Returns:
        TransactionResponse: Resposta da ingestão
    """
    set_trace_id(request.trace_id)
    start_time = time.time()
    
    logger.info(f"Ingestão iniciada para trace_id: {request.trace_id}")
    metrics_collector.increment_counter("ingestor_requests_total")
    
    try:
        # Simula processamento (50-200ms)
        processing_time = random.uniform(0.05, 0.2)
        time.sleep(processing_time)
        
        # Simula falha em 2% dos casos
        if random.random() < 0.02:
            metrics_collector.increment_counter("ingestor_errors_total")
            raise HTTPException(status_code=500, detail="Simulated processing error")
        
        # Simula throttling em 1% dos casos
        if random.random() < 0.01:
            metrics_collector.increment_counter("ingestor_throttled_total")
            raise HTTPException(status_code=429, detail="Rate limit exceeded")
        
        response = TransactionResponse(
            trace_id=request.trace_id,
            status="SUCCESS",
            message="Data ingested successfully",
            data={"processed_items": random.randint(1, 10)}
        )
        
        elapsed = time.time() - start_time
        metrics_collector.record_metric("ingestor_request_duration_seconds", elapsed)
        metrics_collector.increment_counter("ingestor_success_total")
        
        logger.info(f"Ingestão concluída para trace_id: {request.trace_id} em {elapsed:.3f}s")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro inesperado na ingestão: {str(e)}")
        metrics_collector.increment_counter("ingestor_errors_total")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "healthy", "service": "ingestor-mock"}


@app.get("/metrics")
async def get_metrics() -> Dict[str, Any]:
    """Endpoint de métricas"""
    return metrics_collector.get_summary()
