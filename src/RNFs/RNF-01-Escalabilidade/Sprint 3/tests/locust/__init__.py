"""
Locust Load Tests - Testes de Carga e Performance

Scripts Locust para cada componente crítico:
- locustfile_ingestor: Teste de pico de submissões (1000 req)
- locustfile_orchestrator: Concorrência de workflows (200 paralelos)
- locustfile_sharepoint: Uploads concomitantes (500 simultâneos)
- locustfile_audit: Burst de eventos (10k eventos/s)
- locustfile_iam: Sessões ativas (50k tokens)

Métricas coletadas:
- Throughput (req/s)
- Latência (p50, p95, p99)
- Taxa de erro (%)
- Distribuição de respostas por status code

Execução recomendada (headless):
```bash
locust -f tests/locust/locustfile_ingestor.py \\
    --headless -u 150 -r 10 -t 10m \\
    --csv=results/ingestor_run \\
    --host=http://localhost:8001
```
"""

from locust import HttpUser, task, between
import json
import random
import string

# Configurações compartilhadas
LOCUST_CONFIG = {
    "min_wait": 1,  # segundos entre requests
    "max_wait": 5,
    "payload_size_kb": 200,
    "task_weight_main": 10,
    "task_weight_health": 1,
}

# Helper functions para geração de payloads
def generate_random_payload(size_kb: int = 200) -> dict:
    """Gera payload aleatório com tamanho aproximado especificado."""
    # Aproximadamente size_kb de dados
    data_size = size_kb * 1024 // 2  # chars aproximados
    random_data = ''.join(random.choices(string.ascii_letters + string.digits, k=data_size))
    
    return {
        "board_id": f"board-{random.randint(1000, 9999)}",
        "content": random_data,
        "metadata": {
            "source": "locust_load_test",
            "timestamp": "2025-01-01T00:00:00Z",
            "size_kb": size_kb,
        }
    }

def generate_trace_id() -> str:
    """Gera trace_id para rastreabilidade em testes de carga."""
    import uuid
    return f"locust-{uuid.uuid4()}"

__all__ = [
    "LOCUST_CONFIG",
    "generate_random_payload",
    "generate_trace_id",
    "HttpUser",
    "task",
    "between",
]
