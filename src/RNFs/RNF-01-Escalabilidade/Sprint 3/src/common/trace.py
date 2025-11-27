"""Geração de trace_id para rastreabilidade"""
import uuid
from contextvars import ContextVar

# Context var para armazenar trace_id da requisição atual
current_trace_id: ContextVar[str] = ContextVar('trace_id', default=None)


def generate_trace_id() -> str:
    """
    Gera um trace_id único para rastreamento de transações.
    
    Returns:
        str: UUID v4 como string
    """
    return str(uuid.uuid4())


def get_trace_id() -> str:
    """
    Obtém o trace_id da requisição atual ou gera um novo.
    
    Returns:
        str: trace_id atual ou novo
    """
    trace_id = current_trace_id.get()
    if not trace_id:
        trace_id = generate_trace_id()
        current_trace_id.set(trace_id)
    return trace_id


def set_trace_id(trace_id: str) -> None:
    """
    Define o trace_id para a requisição atual.
    
    Args:
        trace_id: ID de rastreamento a ser definido
    """
    current_trace_id.set(trace_id)
