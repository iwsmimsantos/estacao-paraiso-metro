"""
Gerador de dados mockados realistas para simulação de eventos
"""
import hashlib
import random
from datetime import datetime, timedelta
from faker import Faker
from typing import List, Optional

fake = Faker('pt_BR')


class MockDataGenerator:
    """Gera dados mockados consistentes e realistas"""
    
    def __init__(self):
        self.users = self._generate_users()
        self.projects = self._generate_projects()
        self.change_types = [
            "criacao",
            "atualizacao",
            "exclusao",
            "status_change"
        ]
        self.fields = [
            "status",
            "prazo",
            "responsavel",
            "orcamento",
            "escopo",
            "prioridade",
            "fase"
        ]
        self.status_values = [
            "Em Planejamento",
            "Em Andamento",
            "Em Análise",
            "Aguardando Aprovação",
            "Concluído",
            "Cancelado",
            "Pausado"
        ]
        self.justifications_templates = [
            "Alteração necessária devido a mudança de escopo aprovada pela diretoria",
            "Ajuste de prazo conforme reunião com stakeholders do dia {date}",
            "Correção de informação cadastrada incorretamente no sistema",
            "Atualização de responsável por mudança organizacional",
            "Modificação de orçamento aprovada pelo comitê financeiro",
            "Mudança de prioridade conforme alinhamento estratégico",
            "Alteração técnica identificada durante revisão do projeto",
            "Adequação às novas diretrizes corporativas de {month}",
            "Atualização solicitada pelo gestor do projeto via e-mail",
            "Correção de fase do projeto após análise de cronograma"
        ]
    
    def _generate_users(self) -> List[str]:
        """Gera lista de usuários realistas"""
        departments = ["PMO", "TI", "Financeiro", "Operações", "Engenharia"]
        users = []
        for _ in range(15):
            name = fake.name()
            dept = random.choice(departments)
            email = f"{name.lower().replace(' ', '.')}.{dept.lower()}@metrosp.com.br"
            users.append(email)
        return users
    
    def _generate_projects(self) -> List[dict]:
        """Gera lista de projetos realistas da Companhia do Metrô"""
        project_types = [
            "Expansão de Linha",
            "Modernização de Estação",
            "Implementação de Sistema",
            "Manutenção de Infraestrutura",
            "Projeto de Segurança",
            "Automação de Processos"
        ]
        
        lines = ["Linha 1-Azul", "Linha 2-Verde", "Linha 3-Vermelha", "Linha 4-Amarela", "Linha 5-Lilás"]
        
        projects = []
        for i in range(20):
            proj_type = random.choice(project_types)
            line = random.choice(lines) if "Linha" in proj_type or "Estação" in proj_type else ""
            
            project = {
                "project_id": f"PROJ-METRO-{2024}-{str(i+1).zfill(4)}",
                "name": f"{proj_type} {line}".strip(),
                "manager": random.choice(self.users),
                "start_date": fake.date_between(start_date="-2y", end_date="today"),
                "budget": random.randint(500000, 50000000)
            }
            projects.append(project)
        return projects
    
    def generate_user(self) -> str:
        """Retorna um usuário aleatório da lista"""
        return random.choice(self.users)
    
    def generate_project_id(self) -> str:
        """Retorna um project_id aleatório da lista"""
        return random.choice(self.projects)["project_id"]
    
    def generate_justification(self, with_justification: bool = True) -> Optional[str]:
        """Gera uma justificativa realista ou None"""
        if not with_justification:
            return None
        
        template = random.choice(self.justifications_templates)
        
        # Substitui placeholders se existirem
        if "{date}" in template:
            date = fake.date_between(start_date="-30d", end_date="today")
            template = template.replace("{date}", date.strftime("%d/%m/%Y"))
        
        if "{month}" in template:
            months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
                     "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
            template = template.replace("{month}", random.choice(months))
        
        return template
    
    def generate_change_type(self) -> str:
        """Retorna um tipo de mudança"""
        return random.choice(self.change_types)
    
    def generate_field_change(self) -> tuple[str, str, str]:
        """Gera campo, valor antigo e novo valor"""
        field = random.choice(self.fields)
        
        if field == "status":
            old_val = random.choice(self.status_values)
            new_val = random.choice([s for s in self.status_values if s != old_val])
        elif field == "prazo":
            old_date = fake.date_between(start_date="+30d", end_date="+180d")
            new_date = old_date + timedelta(days=random.randint(-30, 60))
            old_val = old_date.strftime("%d/%m/%Y")
            new_val = new_date.strftime("%d/%m/%Y")
        elif field == "responsavel":
            old_val = random.choice(self.users)
            new_val = random.choice([u for u in self.users if u != old_val])
        elif field == "orcamento":
            old_val = f"R$ {random.randint(100000, 10000000):,.2f}"
            new_val = f"R$ {random.randint(100000, 10000000):,.2f}"
        elif field == "prioridade":
            priorities = ["Baixa", "Média", "Alta", "Crítica"]
            old_val = random.choice(priorities)
            new_val = random.choice([p for p in priorities if p != old_val])
        elif field == "fase":
            phases = ["Iniciação", "Planejamento", "Execução", "Monitoramento", "Encerramento"]
            old_val = random.choice(phases)
            new_val = random.choice([p for p in phases if p != old_val])
        else:
            old_val = fake.sentence(nb_words=3)
            new_val = fake.sentence(nb_words=3)
        
        return field, old_val, new_val
    
    def generate_hash(self, data: str) -> str:
        """Gera hash SHA-256 para simular integridade"""
        return hashlib.sha256(data.encode()).hexdigest()
    
    def generate_timestamp_with_offset(self, base_time: datetime, 
                                       min_seconds: int = 1, 
                                       max_seconds: int = 300) -> datetime:
        """Gera timestamp com offset aleatório (simula latência de rede)"""
        offset = timedelta(seconds=random.randint(min_seconds, max_seconds))
        return base_time + offset
    
    def should_have_justification(self, scenario: str) -> bool:
        """Define se o evento deve ter justificativa baseado no cenário"""
        # Cenário 1: sem justificativa
        if scenario == "cenario_1":
            return False
        # Cenário 5: 30% sem justificativa (tentativas inválidas)
        elif scenario == "cenario_5":
            return random.random() > 0.3
        # Outros cenários: sempre com justificativa
        else:
            return True
    
    def simulate_integrity_issue(self, probability: float = 0.1) -> bool:
        """Simula problema de integridade com probabilidade definida"""
        return random.random() < probability


# Singleton
mock_generator = MockDataGenerator()

