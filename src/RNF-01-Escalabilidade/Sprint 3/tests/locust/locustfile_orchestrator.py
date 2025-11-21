"""Script de carga Locust para o Orchestrator"""
from locust import HttpUser, task, between
from datetime import datetime

from src.common.trace import generate_trace_id


class OrchestratorUser(HttpUser):
    """Simula usuário fazendo requisições ao Orchestrator"""
    
    wait_time = between(2, 5)
    host = "http://localhost:8002"
    
    @task(weight=10)
    def orchestrate_task(self):
        """Tarefa de orquestração"""
        trace_id = generate_trace_id()
        
        payload = {
            "trace_id": trace_id,
            "user_id": f"user_{self.environment.runner.user_count}",
            "action": "orchestrate",
            "payload": {
                "project_id": f"proj_{self.environment.runner.user_count % 10}",
                "tasks": ["validate", "process", "store"],
                "priority": "normal"
            },
            "timestamp": datetime.utcnow().isoformat()
        }
        
        with self.client.post(
            "/orchestrate",
            json=payload,
            catch_response=True,
            name="/orchestrate"
        ) as response:
            if response.status_code == 200:
                response.success()
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
