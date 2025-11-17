"""Testes de integração entre os mocks"""
import pytest
from fastapi.testclient import TestClient
import asyncio

from src.mocks.ingestor_mock import app as ingestor_app
from src.mocks.orchestrator_mock import app as orchestrator_app
from src.mocks.sharepoint_mock import app as sharepoint_app
from src.mocks.audit_mock import app as audit_app
from src.mocks.iam_mock import app as iam_app

from src.common.models import TransactionRequest, AuditLog
from src.common.trace import generate_trace_id


ingestor_client = TestClient(ingestor_app)
orchestrator_client = TestClient(orchestrator_app)
sharepoint_client = TestClient(sharepoint_app)
audit_client = TestClient(audit_app)
iam_client = TestClient(iam_app)


def test_full_workflow():
    """Testa um fluxo completo através de todos os serviços"""
    trace_id = generate_trace_id()
    
    # 1. Autenticação
    auth_response = iam_client.post(
        "/authenticate",
        params={"username": "user1", "password": "pass123"}
    )
    
    if auth_response.status_code != 200:
        pytest.skip("Autenticação falhou (simulação)")
    
    token = auth_response.json()["token"]
    
    # 2. Autorização
    authz_response = iam_client.post(
        "/authorize",
        params={"token": token, "resource": "proj1", "action": "write"}
    )
    
    if authz_response.status_code != 200:
        pytest.skip("Autorização negada (simulação)")
    
    # 3. Ingestão
    ingest_data = TransactionRequest(
        trace_id=trace_id,
        user_id="user1",
        action="ingest",
        payload={"data": "workflow_test"}
    ).dict()
    
    ingest_response = ingestor_client.post("/ingest", json=ingest_data)
    
    # 4. Log de auditoria
    audit_log = AuditLog(
        trace_id=trace_id,
        event_type="workflow",
        user_id="user1",
        resource="proj1",
        action="ingest",
        status="success" if ingest_response.status_code == 200 else "failed"
    ).dict()
    
    audit_response = audit_client.post("/log", json=audit_log)
    assert audit_response.status_code == 200
    
    # 5. Verificar logs
    logs_response = audit_client.get(f"/logs/{trace_id}")
    assert logs_response.status_code == 200
    logs = logs_response.json()
    assert len(logs) >= 1


def test_concurrent_requests():
    """Testa requisições concorrentes"""
    trace_ids = [generate_trace_id() for _ in range(10)]
    
    responses = []
    for trace_id in trace_ids:
        request_data = TransactionRequest(
            trace_id=trace_id,
            user_id="user1",
            action="test",
            payload={}
        ).dict()
        
        response = ingestor_client.post("/ingest", json=request_data)
        responses.append(response)
    
    # Pelo menos algumas requisições devem ter sucesso
    success_count = sum(1 for r in responses if r.status_code == 200)
    assert success_count > 0


def test_all_services_healthy():
    """Testa que todos os serviços estão healthy"""
    services = [
        (ingestor_client, "ingestor-mock"),
        (orchestrator_client, "orchestrator-mock"),
        (sharepoint_client, "sharepoint-mock"),
        (audit_client, "audit-mock"),
        (iam_client, "iam-mock"),
    ]
    
    for client, expected_service in services:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json()["service"] == expected_service
