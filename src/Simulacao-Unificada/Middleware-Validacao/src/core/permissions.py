"""
Módulo de Controle de Permissões

Gerencia permissões de acesso a projetos, recursos e ações.
Implementa políticas de controle de acesso baseadas em roles e projetos.
"""
from enum import Enum
from typing import Optional, List, Set
from pydantic import BaseModel


class Permission(str, Enum):
    """Tipos de permissão no sistema"""
    # Permissões de leitura
    READ_PROJECT = "read:project"
    READ_MIRO = "read:miro"
    READ_SHAREPOINT = "read:sharepoint"
    READ_LOGS = "read:logs"
    
    # Permissões de escrita
    WRITE_PROJECT = "write:project"
    WRITE_MIRO = "write:miro"
    WRITE_SHAREPOINT = "write:sharepoint"
    
    # Permissões de administração
    ADMIN_USERS = "admin:users"
    ADMIN_PROJECTS = "admin:projects"
    ADMIN_SYSTEM = "admin:system"
    
    # Permissões de IA
    USE_AI_AGENT = "ai:use"
    ADMIN_AI_AGENT = "ai:admin"


class Role(str, Enum):
    """Roles do sistema"""
    ADMIN = "Administrador"
    MANAGER = "Gerente"
    ANALYST = "Analista"
    COLLABORATOR = "Colaborador"
    VIEWER = "Visualizador"


class AccessControl:
    """Controle de acesso baseado em roles e permissões"""
    
    # Mapeamento de roles para permissões
    ROLE_PERMISSIONS = {
        Role.ADMIN: {
            Permission.READ_PROJECT,
            Permission.READ_MIRO,
            Permission.READ_SHAREPOINT,
            Permission.READ_LOGS,
            Permission.WRITE_PROJECT,
            Permission.WRITE_MIRO,
            Permission.WRITE_SHAREPOINT,
            Permission.ADMIN_USERS,
            Permission.ADMIN_PROJECTS,
            Permission.ADMIN_SYSTEM,
            Permission.USE_AI_AGENT,
            Permission.ADMIN_AI_AGENT,
        },
        Role.MANAGER: {
            Permission.READ_PROJECT,
            Permission.READ_MIRO,
            Permission.READ_SHAREPOINT,
            Permission.READ_LOGS,
            Permission.WRITE_PROJECT,
            Permission.WRITE_MIRO,
            Permission.WRITE_SHAREPOINT,
            Permission.USE_AI_AGENT,
        },
        Role.ANALYST: {
            Permission.READ_PROJECT,
            Permission.READ_MIRO,
            Permission.READ_SHAREPOINT,
            Permission.WRITE_PROJECT,
            Permission.WRITE_MIRO,
            Permission.USE_AI_AGENT,
        },
        Role.COLLABORATOR: {
            Permission.READ_PROJECT,
            Permission.READ_MIRO,
            Permission.WRITE_MIRO,
        },
        Role.VIEWER: {
            Permission.READ_PROJECT,
            Permission.READ_MIRO,
            Permission.READ_SHAREPOINT,
        }
    }
    
    @classmethod
    def get_permissions_for_role(cls, role: str) -> Set[Permission]:
        """Retorna permissões de um role"""
        # Tenta mapear o role string para o enum
        for role_enum in Role:
            if role_enum.value.lower() == role.lower():
                return cls.ROLE_PERMISSIONS.get(role_enum, set())
        
        # Se não encontrar, retorna permissões mínimas
        return {Permission.READ_PROJECT}
    
    @classmethod
    def user_has_permission(cls, user_role: str, required_permission: Permission) -> bool:
        """Verifica se usuário tem uma permissão específica"""
        user_permissions = cls.get_permissions_for_role(user_role)
        return required_permission in user_permissions
    
    @classmethod
    def user_can_access_project(cls, user_role: str, user_projects: List[str], project_id: str) -> bool:
        """Verifica se usuário pode acessar um projeto"""
        # Administradores têm acesso a todos os projetos
        if user_role.lower() == "administrador":
            return True
        
        # Verifica se projeto está na lista de projetos do usuário
        return project_id in user_projects
    
    @classmethod
    def user_can_access_miro(cls, user_role: str, board_id: str, user_projects: List[str]) -> bool:
        """Verifica se usuário pode acessar um board do Miro"""
        # Verifica permissão de leitura do Miro
        if not cls.user_has_permission(user_role, Permission.READ_MIRO):
            return False
        
        # Extrai project_id do board_id (assumindo formato: proj-XXX-board-YYY)
        if "-board-" in board_id:
            project_id = board_id.split("-board-")[0]
            return cls.user_can_access_project(user_role, user_projects, project_id)
        
        return False
    
    @classmethod
    def user_can_write_sharepoint(cls, user_role: str, project_id: str, user_projects: List[str]) -> bool:
        """Verifica se usuário pode escrever no SharePoint de um projeto"""
        # Verifica permissão de escrita no SharePoint
        if not cls.user_has_permission(user_role, Permission.WRITE_SHAREPOINT):
            return False
        
        # Verifica acesso ao projeto
        return cls.user_can_access_project(user_role, user_projects, project_id)
    
    @classmethod
    def user_can_use_ai(cls, user_role: str) -> bool:
        """Verifica se usuário pode usar agentes de IA"""
        return cls.user_has_permission(user_role, Permission.USE_AI_AGENT)


class AccessDecision(BaseModel):
    """Resultado de uma decisão de acesso"""
    allowed: bool
    reason: str
    required_permission: Optional[str] = None
    user_role: Optional[str] = None


def check_access(
    user_id: str,
    user_role: str,
    user_projects: List[str],
    resource_type: str,
    resource_id: str,
    action: str
) -> AccessDecision:
    """
    Verifica acesso a um recurso e retorna decisão estruturada
    
    Args:
        user_id: ID do usuário
        user_role: Role do usuário
        user_projects: Lista de projetos do usuário
        resource_type: Tipo de recurso (project, miro, sharepoint, etc)
        resource_id: ID do recurso
        action: Ação desejada (read, write, admin)
    
    Returns:
        AccessDecision com resultado da verificação
    """
    
    # Determina permissão necessária baseada no recurso e ação
    permission_map = {
        ("project", "read"): Permission.READ_PROJECT,
        ("project", "write"): Permission.WRITE_PROJECT,
        ("miro", "read"): Permission.READ_MIRO,
        ("miro", "write"): Permission.WRITE_MIRO,
        ("sharepoint", "read"): Permission.READ_SHAREPOINT,
        ("sharepoint", "write"): Permission.WRITE_SHAREPOINT,
        ("logs", "read"): Permission.READ_LOGS,
        ("ai", "use"): Permission.USE_AI_AGENT,
    }
    
    required_permission = permission_map.get((resource_type, action))
    
    if not required_permission:
        return AccessDecision(
            allowed=False,
            reason=f"Ação '{action}' não reconhecida para recurso '{resource_type}'",
            user_role=user_role
        )
    
    # Verifica se usuário tem a permissão
    has_permission = AccessControl.user_has_permission(user_role, required_permission)
    
    if not has_permission:
        return AccessDecision(
            allowed=False,
            reason=f"Usuário não possui permissão '{required_permission.value}'",
            required_permission=required_permission.value,
            user_role=user_role
        )
    
    # Verifica acesso ao projeto específico (se aplicável)
    if resource_type in ["project", "miro", "sharepoint"]:
        # Extrai project_id
        project_id = resource_id
        if resource_type == "miro" and "-board-" in resource_id:
            project_id = resource_id.split("-board-")[0]
        
        has_project_access = AccessControl.user_can_access_project(
            user_role, user_projects, project_id
        )
        
        if not has_project_access:
            return AccessDecision(
                allowed=False,
                reason=f"Usuário não tem acesso ao projeto '{project_id}'",
                user_role=user_role
            )
    
    # Acesso permitido
    return AccessDecision(
        allowed=True,
        reason="Acesso autorizado",
        required_permission=required_permission.value,
        user_role=user_role
    )
