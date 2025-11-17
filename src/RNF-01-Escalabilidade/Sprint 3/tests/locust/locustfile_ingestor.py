"""Script de carga Locust para o Ingestor"""
from locust import HttpUser, task, between
import json
from datetime import datetime

from src.common.trace import generate_trace_id


class IngestorUser(HttpUser):
    """Simula usuário fazendo requisições ao Ingestor"""
    
    wait_time = between(1, 3)
    host = "http://localhost:8001"
    
    @task(weight=10)
    def ingest_data(self):
        """Tarefa de ingestão de dados"""
        trace_id = generate_trace_id()
        
        payload = {
            "trace_id": trace_id,
            "user_id": f"user_{self.environment.runner.user_count}",
            "action": "ingest",
            "payload": {
                "data": "load_test",
                "timestamp": datetime.utcnow().isoformat()
            },
            "timestamp": datetime.utcnow().isoformat()
        }
        
        with self.client.post(
            "/ingest",
            json=payload,
            catch_response=True,
            name="/ingest"
        ) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code == 429:
                response.failure("Rate limited")
            else:
                response.failure(f"Failed with status {response.status_code}")
    
    @task(weight=1)
    def health_check(self):
        """Tarefa de health check"""
        with self.client.get("/health", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Health check failed: {response.status_code}")
    
    @task(weight=1)
    def get_metrics(self):
        """Tarefa de consulta de métricas"""
        with self.client.get("/metrics", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Metrics failed: {response.status_code}")
