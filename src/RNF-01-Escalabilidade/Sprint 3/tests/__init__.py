"""
Tests - Suite de Testes de Escalabilidade

Estrutura de testes completa para validação de RNF-01:
- unit/: Testes unitários de cada componente mock
- integration/: Testes end-to-end de fluxos completos
- locust/: Scripts de carga para testes de performance

Critérios de Aceitação (SLOs):
- Taxa de sucesso: ≥ 99.5%
- Latência p95: < 800ms (ingestor), < 600ms (orchestrator)
- Taxa de erro: < 1%
- Rastreabilidade: 100% com trace_id
- MTTR: < 2 minutos
- Integridade: 0 corrupções de dados
"""

import sys
from pathlib import Path

# Adiciona src ao PYTHONPATH para imports relativos
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

__version__ = "1.0.0"

# Configurações de teste
TEST_CONFIG = {
    "timeout": 30,  # segundos
    "max_retries": 3,
    "base_url": "http://localhost",
    "mock_ports": {
        "ingestor": 8001,
        "orchestrator": 8002,
        "sharepoint": 8003,
        "audit": 8004,
        "iam": 8005,
    },
}

# Thresholds de performance (SLOs)
PERFORMANCE_THRESHOLDS = {
    "success_rate_min": 99.5,  # %
    "error_rate_max": 1.0,  # %
    "ingestor_p95_ms": 800,
    "ingestor_p99_ms": 1500,
    "orchestrator_p95_ms": 600,
    "orchestrator_p99_ms": 1200,
    "sharepoint_p95_ms": 2000,
    "audit_p95_ms": 150,
    "iam_p95_ms": 100,
    "mttr_seconds": 120,
}

__all__ = [
    "TEST_CONFIG",
    "PERFORMANCE_THRESHOLDS",
]
