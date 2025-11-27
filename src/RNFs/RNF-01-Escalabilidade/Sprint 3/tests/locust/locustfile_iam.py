"""Script de carga Locust para IAM"""
from locust import HttpUser, task, between
import random


class IAMUser(HttpUser):
    """Simula usuário fazendo requisições ao IAM"""
    
    wait_time = between(1, 3)
    host = "http://localhost:8005"
    
    users = ["user1", "user2", "user3"]
    
    @task(weight=5)
    def authenticate(self):
        """Tarefa de autenticação"""
        username = random.choice(self.users)
        
        with self.client.post(
            "/authenticate",
            params={"username": username, "password": "pass123"},
            catch_response=True,
            name="/authenticate"
        ) as response:
            if response.status_code == 200:
                response.success()
                # Armazena token para usar em autorização
                self.token = response.json().get("token")
            elif response.status_code == 401:
                response.failure("Authentication failed")
            else:
                response.failure(f"Failed with status {response.status_code}")
    
    @task(weight=10)
    def authorize(self):
        """Tarefa de autorização"""
        if not hasattr(self, 'token'):
            self.authenticate()
        
        resources = ["proj1", "proj2", "document1", "document2"]
        actions = ["read", "write", "delete"]
        
        with self.client.post(
            "/authorize",
            params={
                "token": getattr(self, 'token', 'mock_token'),
                "resource": random.choice(resources),
                "action": random.choice(actions)
            },
            catch_response=True,
            name="/authorize"
        ) as response:
            if response.status_code == 200:
                response.success()
            elif response.status_code == 403:
                response.failure("Access denied")
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
