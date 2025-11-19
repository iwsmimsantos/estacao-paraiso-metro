"""Testes unitários para o mock do Ingestor"""
import pytest
from fastapi.testclient import TestClient

from src.mocks.ingestor_mock import app
from src.common.models import TransactionRequest
from src.common.trace import generate_trace_id


client = TestClient(app)


def test_health_check():
    """Testa o endpoint de health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["service"] == "ingestor-mock"


def test_ingest_success():
    """Testa ingestão bem-sucedida"""
    trace_id = generate_trace_id()
    request_data = TransactionRequest(
        trace_id=trace_id,
        user_id="user1",
        action="ingest",
        payload={"data": "test"}
    ).model_dump(mode='json')
    
    response = client.post("/ingest", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["trace_id"] == trace_id
    assert data["status"] == "SUCCESS"
    assert "processed_items" in data["data"]


def test_metrics_endpoint():
    """Testa o endpoint de métricas"""
    response = client.get("/metrics")
    assert response.status_code == 200
    
    data = response.json()
    assert "counters" in data
    assert "metrics_count" in data


@pytest.mark.parametrize("iteration", range(5))
def test_multiple_ingestions(iteration):
    """Testa múltiplas ingestões"""
    trace_id = generate_trace_id()
    request_data = TransactionRequest(
        trace_id=trace_id,
        user_id=f"user{iteration}",
        action="ingest",
        payload={"iteration": iteration}
    ).model_dump(mode='json')
    
    response = client.post("/ingest", json=request_data)
    assert response.status_code in [200, 429, 500]  # Pode ter throttling ou erro simulado
