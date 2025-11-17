"""Testes unitários para o mock do SharePoint"""
import pytest
from fastapi.testclient import TestClient

from src.mocks.sharepoint_mock import app
from src.common.models import TransactionRequest
from src.common.trace import generate_trace_id


client = TestClient(app)


def test_health_check():
    """Testa o endpoint de health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["service"] == "sharepoint-mock"


def test_upload_success():
    """Testa upload bem-sucedido"""
    trace_id = generate_trace_id()
    request_data = TransactionRequest(
        trace_id=trace_id,
        user_id="user1",
        action="upload",
        payload={"filename": "test.pdf", "size": 1024}
    ).dict()
    
    response = client.post("/upload", json=request_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["trace_id"] == trace_id
    assert data["status"] == "SUCCESS"
    assert "document_id" in data["data"]
    assert "version" in data["data"]


def test_metrics_endpoint():
    """Testa o endpoint de métricas"""
    response = client.get("/metrics")
    assert response.status_code == 200
    
    data = response.json()
    assert "counters" in data
    assert "metrics_count" in data
