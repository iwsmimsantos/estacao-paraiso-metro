"""
Integration Tests - Testes End-to-End

Testes de fluxos completos do sistema:
- Fluxo completo: IAM → Ingestor → Orchestrator → Audit
- Requisições concorrentes entre serviços
- Health checks de todos os mocks
- Rastreabilidade distribuída (trace_id propagation)
- Recuperação de falhas parciais

Cenários validados:
1. Workflow completo com sucesso
2. Concorrência e paralelismo
3. Propagação de trace_id
4. Integridade de dados (hashes)
5. Resiliência e retry logic
"""

import pytest
import asyncio
from typing import Dict, Any

# Configuração de ambiente de integração
INTEGRATION_CONFIG = {
    "concurrent_requests": 10,
    "timeout_seconds": 60,
    "retry_attempts": 3,
    "health_check_interval": 5,
}

# Helper para executar testes assíncronos
@pytest.fixture(scope="session")
def event_loop():
    """Cria event loop para testes assíncronos."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def integration_trace_id():
    """Gera trace_id único para testes de integração."""
    from src.common.trace import generate_trace_id
    return generate_trace_id()

__all__ = [
    "INTEGRATION_CONFIG",
    "event_loop",
    "integration_trace_id",
]
