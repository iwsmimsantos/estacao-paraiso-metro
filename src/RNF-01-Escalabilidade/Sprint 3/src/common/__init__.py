"""
Common - Componentes Compartilhados
Código reutilizável entre todos os mocks e testes.

Componentes:
- models: Pydantic models para validação de dados
- trace: Sistema de rastreabilidade distribuída (trace_id)
- logging_config: Logging estruturado em JSON
- metrics: Coletor de métricas de performance
"""

from src.common.models import TransactionRequest, TransactionResponse, AuditLog
from src.common.trace import generate_trace_id, get_trace_id, set_trace_id
from src.common.logging_config import setup_logging, StructuredFormatter
from src.common.metrics import metrics_collector, MetricsCollector

__all__ = [
    # Models
    "TransactionRequest",
    "TransactionResponse",
    "AuditLog",
    # Tracing
    "generate_trace_id",
    "get_trace_id",
    "set_trace_id",
    # Logging
    "setup_logging",
    "StructuredFormatter",
    # Metrics
    "metrics_collector",
    "MetricsCollector",
]
