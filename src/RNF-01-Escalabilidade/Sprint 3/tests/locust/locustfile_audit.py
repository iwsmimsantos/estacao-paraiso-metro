"""Script de carga Locust para Auditoria"""
from locust import HttpUser, task, between
from datetime import datetime

from src.common.trace import generate_trace_id


class AuditUser(HttpUser):
    """Simula usuário fazendo requisições de auditoria"""
    
    wait_time = between(0.5, 2)
    host = "http://localhost:8004"
    
    @task(weight=10)
    def create_audit_log(self):
        """Tarefa de criação de log de auditoria"""
        trace_id = generate_trace_id()
        
        payload = {
            "trace_id": trace_id,
            "event_type": "access",
            "user_id": f"user_{self.environment.runner.user_count}",
            "resource": f"resource_{self.environment.runner.user_count % 20}",
            "action": "read",
            "status": "success",
            "timestamp": datetime.utcnow().isoformat(),
            "metadata": {
                "ip": "192.168.1.1",
                "user_agent": "LoadTest/1.0"
            }
        }
        
        with self.client.post(
            "/log",
            json=payload,
            catch_response=True,
            name="/log"
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
