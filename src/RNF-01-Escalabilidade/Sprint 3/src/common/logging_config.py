"""Configuração de logs estruturados"""
import logging
import sys
from typing import Any, Dict
import json
from datetime import datetime
from .trace import get_trace_id


class StructuredFormatter(logging.Formatter):
    """Formatador para logs estruturados em JSON"""
    
    def format(self, record: logging.LogRecord) -> str:
        log_data: Dict[str, Any] = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "trace_id": get_trace_id(),
        }
        
        # Adiciona informações extras do record
        if hasattr(record, 'extra'):
            log_data.update(record.extra)
        
        # Adiciona informações de exceção se houver
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        return json.dumps(log_data)


def setup_logging(level: str = "INFO") -> None:
    """
    Configura o sistema de logging estruturado.
    
    Args:
        level: Nível de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(StructuredFormatter())
    
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        handlers=[handler]
    )


def get_logger(name: str) -> logging.Logger:
    """
    Obtém um logger configurado.
    
    Args:
        name: Nome do logger (geralmente __name__ do módulo)
    
    Returns:
        logging.Logger: Logger configurado
    """
    return logging.getLogger(name)
