"""Testes unitários para o mock do Orchestrator"""
import pytest
from fastapi.testclient import TestClient

from src.mocks.orchestrator_mock import app
from src.common.models import TransactionRequest
from src.common.trace import generate_trace_id


client = TestClient(app)


def test_health_check():
    """Testa o endpoint de health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["service"] == "orchestrator-mock"


def test_orchestrate_success():
    """Testa orquestração (pode ter erro simulado em 3% dos casos)"""
    trace_id = generate_trace_id()
    request_data = TransactionRequest(
        trace_id=trace_id,
        user_id="user1",
        action="orchestrate",
        payload={"tasks": ["task1", "task2"]}
    ).model_dump(mode='json')
    
    response = client.post("/orchestrate", json=request_data)
    
    # Aceita tanto sucesso quanto erro simulado (3% de chance)
    assert response.status_code in [200, 500]
    
    if response.status_code == 200:
        data = response.json()
        assert data["trace_id"] == trace_id
        assert data["status"] == "SUCCESS"
        assert "tasks_created" in data["data"]
        assert "estimated_completion" in data["data"]


def test_metrics_endpoint():
    """Testa o endpoint de métricas"""
    response = client.get("/metrics")
    assert response.status_code == 200
    
    data = response.json()
    assert "counters" in data
    assert "metrics_count" in data
