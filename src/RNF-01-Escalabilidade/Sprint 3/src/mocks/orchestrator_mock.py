"""Mock do Orquestrador IA"""
from fastapi import FastAPI, HTTPException
from typing import Dict, Any
import random
import time

from ..common.models import TransactionRequest, TransactionResponse
from ..common.trace import get_trace_id, set_trace_id
from ..common.logging_config import get_logger
from ..common.metrics import metrics_collector

logger = get_logger(__name__)
app = FastAPI(title="Orchestrator IA Mock")


@app.post("/orchestrate", response_model=TransactionResponse)
async def orchestrate(request: TransactionRequest) -> TransactionResponse:
    """
    Simula a orquestração de tarefas pela IA.
    
    Args:
        request: Dados da requisição
    
    Returns:
        TransactionResponse: Resposta da orquestração
    """
    set_trace_id(request.trace_id)
    start_time = time.time()
    
    logger.info(f"Orquestração iniciada para trace_id: {request.trace_id}")
    metrics_collector.increment_counter("orchestrator_requests_total")
    
    try:
        # Simula processamento mais longo (100-500ms)
        processing_time = random.uniform(0.1, 0.5)
        time.sleep(processing_time)
        
        # Simula falha em 3% dos casos
        if random.random() < 0.03:
            metrics_collector.increment_counter("orchestrator_errors_total")
            raise HTTPException(status_code=500, detail="AI processing error")
        
        response = TransactionResponse(
            trace_id=request.trace_id,
            status="SUCCESS",
            message="Task orchestrated successfully",
            data={
                "tasks_created": random.randint(1, 5),
                "estimated_completion": f"{random.randint(10, 60)} minutes"
            }
        )
        
        elapsed = time.time() - start_time
        metrics_collector.record_metric("orchestrator_request_duration_seconds", elapsed)
        metrics_collector.increment_counter("orchestrator_success_total")
        
        logger.info(f"Orquestração concluída para trace_id: {request.trace_id} em {elapsed:.3f}s")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro inesperado na orquestração: {str(e)}")
        metrics_collector.increment_counter("orchestrator_errors_total")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "healthy", "service": "orchestrator-mock"}


@app.get("/metrics")
async def get_metrics() -> Dict[str, Any]:
    """Endpoint de métricas"""
    return metrics_collector.get_summary()
