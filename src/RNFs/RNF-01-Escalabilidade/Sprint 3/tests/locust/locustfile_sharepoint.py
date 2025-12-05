"""Script de carga Locust para o SharePoint"""
from locust import HttpUser, task, between
from datetime import datetime

from src.common.trace import generate_trace_id


class SharePointUser(HttpUser):
    """Simula usuário fazendo requisições ao SharePoint"""
    
    wait_time = between(1, 4)
    host = "http://localhost:8003"
    
    @task(weight=10)
    def upload_document(self):
        """Tarefa de upload de documento"""
        trace_id = generate_trace_id()
        
        payload = {
            "trace_id": trace_id,
            "user_id": f"user_{self.environment.runner.user_count}",
            "action": "upload",
            "payload": {
                "filename": f"document_{self.environment.runner.user_count}.pdf",
                "size": 1024 * (self.environment.runner.user_count % 100),
                "project_id": f"proj_{self.environment.runner.user_count % 10}"
            },
            "timestamp": datetime.utcnow().isoformat()
        }
        
        with self.client.post(
            "/upload",
            json=payload,
            catch_response=True,
            name="/upload"
        ) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code == 429:
                response.failure("SharePoint throttled")
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
