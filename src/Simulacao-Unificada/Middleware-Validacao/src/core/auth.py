"""
Módulo de Autenticação e Autorização

Gerencia usuários, tokens e permissões de acesso por projeto.
Utiliza os dados do users.csv da API mockada.
"""
import csv
import os
from datetime import datetime, timedelta
from typing import Optional, Dict, List
from pathlib import Path

from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext


# Configurações de segurança
SECRET_KEY = "metrô-sp-middleware-secret-key-dev-2025"  # Em produção, usar variável de ambiente
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 480  # 8 horas

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    """Modelo de usuário baseado no CSV da API"""
    user_id: str
    display_name: str
    email: str
    department: str
    role: str
    risk_level: str
    is_active: bool
    mfa_enabled: bool
    tenant_id: str
    projects: List[str] = []  # Projetos que o usuário tem acesso


class Token(BaseModel):
    """Token de acesso"""
    access_token: str
    token_type: str
    user_id: str
    projects: List[str]


class UserDatabase:
    """Gerenciador de usuários mockados"""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.user_projects: Dict[str, List[str]] = {}  # user_id -> list of project_ids
        self._load_users()
        self._assign_mock_projects()
    
    def _load_users(self):
        """Carrega usuários do CSV da API mockada"""
        csv_path = Path(__file__).parent.parent.parent.parent / "API" / "data" / "users.csv"
        
        if not csv_path.exists():
            print(f"⚠️  CSV não encontrado em: {csv_path}")
            print("Usando usuários mockados padrão...")
            self._load_default_users()
            return
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user = User(
                        user_id=row['user_id'],
                        display_name=row['display_name'],
                        email=row['email'],
                        department=row['department'],
                        role=row['role'],
                        risk_level=row['risk_level'],
                        is_active=row['is_active'].lower() == 'true',
                        mfa_enabled=row['mfa_enabled'].lower() == 'true',
                        tenant_id=row['tenant_id']
                    )
                    self.users[user.user_id] = user
            
            print(f"✅ {len(self.users)} usuários carregados do CSV")
        
        except Exception as e:
            print(f"❌ Erro ao carregar CSV: {e}")
            self._load_default_users()
    
    def _load_default_users(self):
        """Carrega usuários padrão caso o CSV não esteja disponível"""
        default_users = [
            {
                "user_id": "u001",
                "display_name": "Ana Souza",
                "email": "ana.souza@empresa.com",
                "department": "TI",
                "role": "Administrador",
                "risk_level": "high",
                "is_active": True,
                "mfa_enabled": True,
                "tenant_id": "tenant-01"
            },
            {
                "user_id": "u002",
                "display_name": "Carlos Lima",
                "email": "carlos.lima@empresa.com",
                "department": "Finanças",
                "role": "Analista",
                "risk_level": "medium",
                "is_active": True,
                "mfa_enabled": True,
                "tenant_id": "tenant-01"
            },
            {
                "user_id": "u003",
                "display_name": "Mariana Silva",
                "email": "mariana.silva@empresa.com",
                "department": "Marketing",
                "role": "Colaborador",
                "risk_level": "low",
                "is_active": True,
                "mfa_enabled": False,
                "tenant_id": "tenant-01"
            }
        ]
        
        for user_data in default_users:
            user = User(**user_data)
            self.users[user.user_id] = user
        
        print(f"✅ {len(self.users)} usuários padrão carregados")
    
    def _assign_mock_projects(self):
        """Atribui projetos mockados aos usuários baseado em seus departamentos/roles"""
        
        # Mapeamento de projetos por departamento
        project_mapping = {
            "TI": ["proj-001", "proj-002", "proj-003", "proj-004", "proj-005"],
            "Finanças": ["proj-001", "proj-002", "proj-006"],
            "Marketing": ["proj-003", "proj-007"],
            "RH": ["proj-004", "proj-008"],
            "Vendas": ["proj-005", "proj-007"],
            "Jurídico": ["proj-001", "proj-002", "proj-006"],
            "Operações": ["proj-004", "proj-005", "proj-009"],
            "Compliance": ["proj-001", "proj-002", "proj-006", "proj-010"],
            "Segurança": ["proj-001", "proj-002", "proj-003", "proj-010"],
        }
        
        for user_id, user in self.users.items():
            # Atribui projetos baseado no departamento
            projects = project_mapping.get(user.department, ["proj-001"])
            
            # Administradores têm acesso a todos os projetos
            if user.role.lower() in ["administrador", "gestor"]:
                projects = list(set([p for ps in project_mapping.values() for p in ps]))
            
            self.user_projects[user_id] = projects
            user.projects = projects
    
    def get_user(self, user_id: str) -> Optional[User]:
        """Busca usuário por ID"""
        return self.users.get(user_id)
    
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Busca usuário por email"""
        for user in self.users.values():
            if user.email == email:
                return user
        return None
    
    def get_user_projects(self, user_id: str) -> List[str]:
        """Retorna lista de projetos que o usuário tem acesso"""
        return self.user_projects.get(user_id, [])
    
    def user_has_project_access(self, user_id: str, project_id: str) -> bool:
        """Verifica se usuário tem acesso a um projeto específico"""
        user_projects = self.user_projects.get(user_id, [])
        return project_id in user_projects


# Instância global do banco de usuários
user_db = UserDatabase()


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Cria token JWT de acesso"""
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def verify_token(token: str) -> Optional[Dict]:
    """Verifica e decodifica token JWT"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        
        if user_id is None:
            return None
        
        return payload
    
    except JWTError:
        return None


def authenticate_user(user_id: str) -> Optional[User]:
    """
    Autentica usuário (versão simplificada para simulação)
    Em produção, verificaria senha/credenciais
    """
    user = user_db.get_user(user_id)
    
    if not user:
        return None
    
    if not user.is_active:
        return None
    
    return user


def login(user_id: str) -> Optional[Token]:
    """
    Realiza login e retorna token de acesso
    Versão simplificada para simulação (sem verificação de senha)
    """
    user = authenticate_user(user_id)
    
    if not user:
        return None
    
    # Cria token com informações do usuário
    access_token = create_access_token(
        data={
            "sub": user.user_id,
            "email": user.email,
            "department": user.department,
            "role": user.role,
            "tenant_id": user.tenant_id,
            "projects": user.projects
        }
    )
    
    return Token(
        access_token=access_token,
        token_type="bearer",
        user_id=user.user_id,
        projects=user.projects
    )


def get_current_user(token: str) -> Optional[User]:
    """Obtém usuário atual a partir do token"""
    payload = verify_token(token)
    
    if not payload:
        return None
    
    user_id = payload.get("sub")
    return user_db.get_user(user_id)


def check_project_access(user_id: str, project_id: str) -> bool:
    """Verifica se usuário tem acesso ao projeto"""
    return user_db.user_has_project_access(user_id, project_id)
