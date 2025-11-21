"""
Gerador de dados mockados para testes de segurança
"""
import random
from datetime import datetime, timedelta
from faker import Faker
from typing import List, Optional

fake = Faker('pt_BR')


class MockDataGenerator:
    """Gera dados mockados para simulação de eventos de segurança"""
    
    def __init__(self):
        self.users = self._generate_users()
        self.projects = self._generate_projects()
        self.portfolios = self._generate_portfolios()
        self.miro_boards = self._generate_miro_boards()
    
    def _generate_users(self) -> List[dict]:
        """Gera lista de usuários com IDs e emails"""
        departments = ["PMO", "TI", "Financeiro", "Operações", "Engenharia", "Segurança"]
        users = []
        for i in range(20):
            name = fake.name()
            dept = random.choice(departments)
            email = f"{name.lower().replace(' ', '.')}.{dept.lower()}@metrosp.com.br"
            user_id = f"USER-{str(i+1).zfill(4)}"
            users.append({
                "user_id": user_id,
                "email": email,
                "name": name,
                "department": dept
            })
        return users
    
    def _generate_projects(self) -> List[dict]:
        """Gera lista de projetos do Metrô"""
        project_types = [
            "Expansão de Linha",
            "Modernização de Estação",
            "Implementação de Sistema",
            "Manutenção de Infraestrutura",
            "Projeto de Segurança",
            "Automação de Processos"
        ]
        
        lines = ["Linha 1-Azul", "Linha 2-Verde", "Linha 3-Vermelha", 
                 "Linha 4-Amarela", "Linha 5-Lilás"]
        
        projects = []
        for i in range(15):
            proj_type = random.choice(project_types)
            line = random.choice(lines) if "Linha" in proj_type or "Estação" in proj_type else ""
            
            projects.append({
                "project_id": f"PROJ-METRO-{2024}-{str(i+1).zfill(4)}",
                "name": f"{proj_type} {line}".strip(),
                "portfolio_id": f"PORTFOLIO-{random.randint(1, 3)}",
                "is_active": True
            })
        return projects
    
    def _generate_portfolios(self) -> List[dict]:
        """Gera portfólios"""
        return [
            {"portfolio_id": "PORTFOLIO-1", "name": "Portfólio de Expansão"},
            {"portfolio_id": "PORTFOLIO-2", "name": "Portfólio de Modernização"},
            {"portfolio_id": "PORTFOLIO-3", "name": "Portfólio de Manutenção"}
        ]
    
    def _generate_miro_boards(self) -> List[dict]:
        """Gera boards do Miro"""
        boards = []
        for i, project in enumerate(self.projects[:10]):
            boards.append({
                "board_id": f"MIRO-BOARD-{str(i+1).zfill(4)}",
                "project_id": project["project_id"],
                "link": f"https://miro.com/app/board/{random.randint(1000000000, 9999999999)}/",
                "is_locked": False
            })
        return boards
    
    def generate_user(self) -> dict:
        """Retorna um usuário aleatório"""
        return random.choice(self.users)
    
    def generate_project_id(self) -> str:
        """Retorna um project_id aleatório"""
        return random.choice(self.projects)["project_id"]
    
    def generate_portfolio_id(self) -> str:
        """Retorna um portfolio_id aleatório"""
        return random.choice(self.portfolios)["portfolio_id"]
    
    def generate_miro_board(self, project_id: Optional[str] = None) -> dict:
        """Retorna um board do Miro, opcionalmente vinculado a um projeto"""
        if project_id:
            board = next((b for b in self.miro_boards if b["project_id"] == project_id), None)
            if board:
                return board
        return random.choice(self.miro_boards)
    
    def generate_token(self, user: dict, valid: bool = True) -> dict:
        """Gera um token de autenticação"""
        expires_at = datetime.now() + timedelta(hours=8) if valid else datetime.now() - timedelta(hours=1)
        return {
            "token": f"TOKEN-{random.randint(100000, 999999)}-{user['user_id']}",
            "user_id": user["user_id"],
            "user_email": user["email"],
            "issued_at": datetime.now(),
            "expires_at": expires_at,
            "is_valid": valid
        }
    
    def generate_permission(self, user: dict, project_id: str, 
                           permission_level: str = "Colaborador") -> dict:
        """Gera uma permissão de projeto"""
        return {
            "user_email": user["email"],
            "user_id": user["user_id"],
            "project_id": project_id,
            "permission_level": permission_level,
            "is_active": True
        }


# Singleton
mock_generator = MockDataGenerator()


