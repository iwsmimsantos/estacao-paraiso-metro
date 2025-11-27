"""
Unit Tests - Testes Unitários dos Componentes

Testes isolados de cada mock service:
- test_ingestor_mock: Validação do endpoint de ingestão Miro
- test_orchestrator_mock: Validação do orquestrador de IA
- test_sharepoint_mock: Validação de uploads SharePoint
- test_audit_mock: Validação do serviço de auditoria
- test_iam_mock: Validação de autenticação/autorização

Cobertura esperada: > 80% de code coverage
"""

import pytest
from fastapi.testclient import TestClient

# Fixtures compartilhadas entre testes unitários
@pytest.fixture
def mock_trace_id():
    """Fixture que retorna um trace_id válido para testes."""
    return "test-trace-id-12345678"

@pytest.fixture
def mock_user_id():
    """Fixture que retorna um user_id válido para testes."""
    return "user-test-001"

@pytest.fixture
def mock_payload():
    """Fixture que retorna payload de teste padrão."""
    return {
        "board_id": "board-123",
        "content": "Test content",
        "metadata": {"source": "unit_test"}
    }

__all__ = [
    "mock_trace_id",
    "mock_user_id",
    "mock_payload",
]
