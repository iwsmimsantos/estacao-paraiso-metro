"""Mock do IAM (Identity and Access Management)"""
from fastapi import FastAPI, HTTPException, Header
from typing import Dict, Any, Optional
import random
import time

from src.common.trace import generate_trace_id, set_trace_id
from src.common.logging_config import get_logger
from src.common.metrics import metrics_collector

logger = get_logger(__name__)
app = FastAPI(title="IAM Mock")

# Usuários simulados
MOCK_USERS = {
    "user1": {"roles": ["admin", "user"], "projects": ["proj1", "proj2"]},
    "user2": {"roles": ["user"], "projects": ["proj1"]},
    "user3": {"roles": ["viewer"], "projects": ["proj2"]},
}


@app.post("/authenticate")
async def authenticate(
    username: str,
    password: str,
    authorization: Optional[str] = Header(None)
) -> Dict[str, Any]:
    """
    Simula autenticação de usuário.
    
    Args:
        username: Nome do usuário
        password: Senha
        authorization: Header de autorização opcional
    
    Returns:
        Dict: Token e informações do usuário
    """
    trace_id = generate_trace_id()
    set_trace_id(trace_id)
    start_time = time.time()
    
    logger.info(f"Autenticação iniciada para usuário: {username}")
    metrics_collector.increment_counter("iam_auth_requests_total")
    
    try:
        # Simula processamento (50-150ms)
        processing_time = random.uniform(0.05, 0.15)
        time.sleep(processing_time)
        
        # Simula falha de autenticação em 5% dos casos
        if random.random() < 0.05 or username not in MOCK_USERS:
            metrics_collector.increment_counter("iam_auth_failures_total")
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        user_data = MOCK_USERS[username]
        
        response = {
            "trace_id": trace_id,
            "token": f"mock_token_{random.randint(10000, 99999)}",
            "user": {
                "username": username,
                "roles": user_data["roles"],
                "projects": user_data["projects"]
            }
        }
        
        elapsed = time.time() - start_time
        metrics_collector.record_metric("iam_auth_duration_seconds", elapsed)
        metrics_collector.increment_counter("iam_auth_success_total")
        
        logger.info(f"Autenticação bem-sucedida para usuário: {username} em {elapsed:.3f}s")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro inesperado na autenticação: {str(e)}")
        metrics_collector.increment_counter("iam_auth_errors_total")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/authorize")
async def authorize(
    token: str,
    resource: str,
    action: str
) -> Dict[str, Any]:
    """
    Simula autorização de acesso a recurso.
    
    Args:
        token: Token de autenticação
        resource: Recurso a ser acessado
        action: Ação a ser realizada
    
    Returns:
        Dict: Resultado da autorização
    """
    trace_id = generate_trace_id()
    set_trace_id(trace_id)
    start_time = time.time()
    
    logger.info(f"Autorização iniciada para recurso: {resource}")
    metrics_collector.increment_counter("iam_authz_requests_total")
    
    try:
        # Simula processamento rápido (20-80ms)
        processing_time = random.uniform(0.02, 0.08)
        time.sleep(processing_time)
        
        # Simula negação de acesso em 10% dos casos
        authorized = random.random() > 0.1
        
        if not authorized:
            metrics_collector.increment_counter("iam_authz_denied_total")
            raise HTTPException(status_code=403, detail="Access denied")
        
        response = {
            "trace_id": trace_id,
            "authorized": True,
            "resource": resource,
            "action": action
        }
        
        elapsed = time.time() - start_time
        metrics_collector.record_metric("iam_authz_duration_seconds", elapsed)
        metrics_collector.increment_counter("iam_authz_success_total")
        
        logger.info(f"Autorização concedida para recurso: {resource} em {elapsed:.3f}s")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Erro inesperado na autorização: {str(e)}")
        metrics_collector.increment_counter("iam_authz_errors_total")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """Health check endpoint"""
    return {"status": "healthy", "service": "iam-mock"}


@app.get("/metrics")
async def get_metrics() -> Dict[str, Any]:
    """Endpoint de métricas"""
    return metrics_collector.get_summary()
