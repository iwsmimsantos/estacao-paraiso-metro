"""
Utils - Utilitários de Suporte

Funções auxiliares para resiliência e integridade:
- retry: Lógica de retry com exponential backoff
- hash_utils: Verificação de integridade de dados
"""

from src.utils.retry import (
    exponential_backoff,
    retry_with_backoff,
    RetryableError,
    ThrottlingError,
    TransientError,
)
from src.utils.hash_utils import (
    calculate_sha256,
    calculate_payload_hash,
    verify_hash,
    verify_payload_hash,
)

__all__ = [
    # Retry mechanisms
    "exponential_backoff",
    "retry_with_backoff",
    "RetryableError",
    "ThrottlingError",
    "TransientError",
    # Hash utilities
    "calculate_sha256",
    "calculate_payload_hash",
    "verify_hash",
    "verify_payload_hash",
]
