"""Testes unitários para o mock de Auditoria"""
import pytest
from fastapi.testclient import TestClient

from src.mocks.audit_mock import app
from src.common.models import AuditLog
from src.common.trace import generate_trace_id


client = TestClient(app)


def test_health_check():
    """Testa o endpoint de health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["service"] == "audit-mock"


def test_create_audit_log():
    """Testa criação de log de auditoria"""
    trace_id = generate_trace_id()
    log_data = AuditLog(
        trace_id=trace_id,
        event_type="access",
        user_id="user1",
        resource="document1",
        action="read",
        status="success"
    ).dict()
    
    response = client.post("/log", json=log_data)
    assert response.status_code == 200
    
    data = response.json()
    assert data["trace_id"] == trace_id
    assert data["status"] == "SUCCESS"


def test_get_logs_by_trace():
    """Testa recuperação de logs por trace_id"""
    trace_id = generate_trace_id()
    
    # Cria um log
    log_data = AuditLog(
        trace_id=trace_id,
        event_type="access",
        user_id="user1",
        resource="document1",
        action="read",
        status="success"
    ).dict()
    client.post("/log", json=log_data)
    
    # Recupera logs
    response = client.get(f"/logs/{trace_id}")
    assert response.status_code == 200
    
    logs = response.json()
    assert len(logs) >= 1
    assert logs[0]["trace_id"] == trace_id


def test_metrics_endpoint():
    """Testa o endpoint de métricas"""
    response = client.get("/metrics")
    assert response.status_code == 200
    
    data = response.json()
    assert "counters" in data
    assert "total_logs" in data
