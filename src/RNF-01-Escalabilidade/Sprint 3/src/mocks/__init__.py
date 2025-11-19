"""
Mocks - Componentes Simulados para Testes de Escalabilidade

Este pacote contém mocks controláveis de todos os componentes críticos:
- ingestor_mock: Simula ingestão de dados do Miro
- orchestrator_mock: Simula orquestração de agentes IA
- sharepoint_mock: Simula uploads para SharePoint
- audit_mock: Simula serviço de auditoria/logging
- iam_mock: Simula autenticação e autorização

Cada mock implementa:
- Endpoints REST compatíveis com a arquitetura real
- Simulação de latências realistas
- Injeção de falhas controladas (erros, throttling)
- Rastreabilidade via trace_id
- Métricas de observabilidade
"""

from src.mocks.ingestor_mock import app as ingestor_app
from src.mocks.orchestrator_mock import app as orchestrator_app
from src.mocks.sharepoint_mock import app as sharepoint_app
from src.mocks.audit_mock import app as audit_app
from src.mocks.iam_mock import app as iam_app

__all__ = [
    "ingestor_app",
    "orchestrator_app",
    "sharepoint_app",
    "audit_app",
    "iam_app",
]

# Configuração padrão dos mocks
MOCK_PORTS = {
    "ingestor": 8001,
    "orchestrator": 8002,
    "sharepoint": 8003,
    "audit": 8004,
    "iam": 8005,
}

MOCK_HOSTS = {
    "ingestor": "http://localhost:8001",
    "orchestrator": "http://localhost:8002",
    "sharepoint": "http://localhost:8003",
    "audit": "http://localhost:8004",
    "iam": "http://localhost:8005",
}
