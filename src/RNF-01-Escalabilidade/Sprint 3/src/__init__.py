"""
Sprint 3 - RNF-01 Escalabilidade
Testes de Escalabilidade para Sistema Metro-SP
Miro → Processamento/IA → SharePoint

Este pacote contém a implementação dos componentes de teste de escalabilidade:
- Mocks controláveis para simular componentes do sistema
- Utilitários comuns (tracing, logging, metrics)
- Helpers de teste e retry logic
"""

__version__ = "1.0.0"
__author__ = "Inteli - Metro SP Project"
__description__ = "Scalability Testing Framework - Sprint 3"

# Facilita imports diretos do pacote raiz
from src.common.models import TransactionRequest, TransactionResponse, AuditLog
from src.common.trace import generate_trace_id, get_trace_id, set_trace_id
from src.common.logging_config import setup_logging
from src.common.metrics import metrics_collector

__all__ = [
    "TransactionRequest",
    "TransactionResponse", 
    "AuditLog",
    "generate_trace_id",
    "get_trace_id",
    "set_trace_id",
    "setup_logging",
    "metrics_collector",
]
