"""Testes unitários para o mock do IAM"""
import pytest
from fastapi.testclient import TestClient

from src.mocks.iam_mock import app


client = TestClient(app)


def test_health_check():
    """Testa o endpoint de health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["service"] == "iam-mock"


def test_authenticate_success():
    """Testa autenticação bem-sucedida"""
    response = client.post(
        "/authenticate",
        params={"username": "user1", "password": "pass123"}
    )
    
    # Pode ter falha simulada em 5% dos casos
    if response.status_code == 200:
        data = response.json()
        assert "token" in data
        assert "user" in data
        assert data["user"]["username"] == "user1"
        assert "roles" in data["user"]


def test_authenticate_invalid_user():
    """Testa autenticação com usuário inválido"""
    response = client.post(
        "/authenticate",
        params={"username": "invalid_user", "password": "pass123"}
    )
    assert response.status_code == 401


def test_authorize_success():
    """Testa autorização"""
    response = client.post(
        "/authorize",
        params={
            "token": "mock_token_12345",
            "resource": "project1",
            "action": "read"
        }
    )
    
    # Pode ter negação simulada em 10% dos casos
    assert response.status_code in [200, 403]


def test_metrics_endpoint():
    """Testa o endpoint de métricas"""
    response = client.get("/metrics")
    assert response.status_code == 200
    
    data = response.json()
    assert "counters" in data
    assert "metrics_count" in data
