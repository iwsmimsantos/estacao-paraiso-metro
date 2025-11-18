"""Exportadores de métricas para observabilidade"""
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime, timezone
from collections import defaultdict
import threading


@dataclass
class Metric:
    """Representa uma métrica coletada"""
    name: str
    value: float
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    labels: Dict[str, str] = field(default_factory=dict)


class MetricsCollector:
    """Coletor de métricas thread-safe"""
    
    def __init__(self):
        self._metrics: Dict[str, List[Metric]] = defaultdict(list)
        self._counters: Dict[str, float] = defaultdict(float)
        self._lock = threading.Lock()
    
    def record_metric(self, name: str, value: float, labels: Optional[Dict[str, str]] = None) -> None:
        """
        Registra uma métrica.
        
        Args:
            name: Nome da métrica
            value: Valor da métrica
            labels: Labels adicionais para a métrica
        """
        with self._lock:
            metric = Metric(name=name, value=value, labels=labels or {})
            self._metrics[name].append(metric)
    
    def increment_counter(self, name: str, value: float = 1.0) -> None:
        """
        Incrementa um contador.
        
        Args:
            name: Nome do contador
            value: Valor a incrementar (padrão: 1.0)
        """
        with self._lock:
            self._counters[name] += value
    
    def get_counter(self, name: str) -> float:
        """
        Obtém o valor de um contador.
        
        Args:
            name: Nome do contador
        
        Returns:
            float: Valor atual do contador
        """
        with self._lock:
            return self._counters.get(name, 0.0)
    
    def get_metrics(self, name: str) -> List[Metric]:
        """
        Obtém todas as métricas de um nome específico.
        
        Args:
            name: Nome da métrica
        
        Returns:
            List[Metric]: Lista de métricas
        """
        with self._lock:
            return self._metrics.get(name, []).copy()
    
    def reset(self) -> None:
        """Reseta todas as métricas e contadores"""
        with self._lock:
            self._metrics.clear()
            self._counters.clear()
    
    def get_summary(self) -> Dict[str, any]:
        """
        Obtém um resumo de todas as métricas.
        
        Returns:
            Dict: Resumo das métricas
        """
        with self._lock:
            return {
                "counters": dict(self._counters),
                "metrics_count": {name: len(metrics) for name, metrics in self._metrics.items()}
            }


# Instância global do coletor de métricas
metrics_collector = MetricsCollector()
