"""Lógica de retry/backoff para operações com falhas transitórias"""
import time
import random
from typing import Callable, Any, Optional, Type
from functools import wraps

from ..common.logging_config import get_logger

logger = get_logger(__name__)


def exponential_backoff(
    attempt: int,
    base_delay: float = 0.1,
    max_delay: float = 60.0,
    jitter: bool = True
) -> float:
    """
    Calcula o tempo de espera usando backoff exponencial.
    
    Args:
        attempt: Número da tentativa (1-based)
        base_delay: Delay base em segundos
        max_delay: Delay máximo em segundos
        jitter: Se True, adiciona jitter aleatório
    
    Returns:
        float: Tempo de espera em segundos
    """
    delay = min(base_delay * (2 ** (attempt - 1)), max_delay)
    
    if jitter:
        # Adiciona jitter de ±25%
        jitter_range = delay * 0.25
        delay = delay + random.uniform(-jitter_range, jitter_range)
    
    return max(0, delay)


def retry_with_backoff(
    max_attempts: int = 3,
    base_delay: float = 0.1,
    max_delay: float = 60.0,
    exceptions: tuple = (Exception,),
    on_retry: Optional[Callable[[Exception, int], None]] = None
):
    """
    Decorator para retry com backoff exponencial.
    
    Args:
        max_attempts: Número máximo de tentativas
        base_delay: Delay base em segundos
        max_delay: Delay máximo em segundos
        exceptions: Tupla de exceções que devem acionar retry
        on_retry: Callback chamado em cada retry (exception, attempt)
    
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                    
                except exceptions as e:
                    last_exception = e
                    
                    if attempt == max_attempts:
                        logger.error(
                            f"Função {func.__name__} falhou após {max_attempts} tentativas",
                            extra={"error": str(e)}
                        )
                        raise
                    
                    delay = exponential_backoff(attempt, base_delay, max_delay)
                    
                    logger.warning(
                        f"Tentativa {attempt}/{max_attempts} falhou para {func.__name__}. "
                        f"Aguardando {delay:.2f}s antes de tentar novamente",
                        extra={"error": str(e), "attempt": attempt}
                    )
                    
                    if on_retry:
                        on_retry(e, attempt)
                    
                    time.sleep(delay)
            
            raise last_exception
        
        return wrapper
    return decorator


class RetryableError(Exception):
    """Exceção base para erros que devem acionar retry"""
    pass


class ThrottlingError(RetryableError):
    """Exceção para erros de throttling/rate limiting"""
    pass


class TransientError(RetryableError):
    """Exceção para erros transitórios (rede, timeout, etc.)"""
    pass
