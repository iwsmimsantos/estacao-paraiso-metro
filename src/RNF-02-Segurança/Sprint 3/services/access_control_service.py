"""
Serviço de controle de acesso baseado em permissões de projeto
"""
from datetime import datetime
from typing import Dict, Any, Optional, List
from uuid import uuid4

from models.security_models import (
    AccessRequest,
    ProjectPermission,
    SecurityIncident,
    MiroAccessRequest
)
from storage.incident_repository import incident_repository
from services.auth_service import auth_service


class AccessControlService:
    """Middleware de controle de acesso a projetos e recursos"""
    
    def __init__(self):
        self.repository = incident_repository
        self.project_permissions: Dict[str, List[ProjectPermission]] = {}
    
    def register_permission(self, permission: ProjectPermission) -> ProjectPermission:
        """
        Registra uma permissão de usuário em um projeto
        
        Args:
            permission: Permissão a ser registrada
        
        Returns:
            Permissão registrada
        """
        project_id = permission.project_id
        
        if project_id not in self.project_permissions:
            self.project_permissions[project_id] = []
        
        # Remove permissões antigas do mesmo usuário no projeto
        self.project_permissions[project_id] = [
            p for p in self.project_permissions[project_id]
            if p.user_id != permission.user_id
        ]
        
        self.project_permissions[project_id].append(permission)
        
        return permission
    
    def check_access(self, access_request: AccessRequest) -> Dict[str, Any]:
        """
        Verifica se um usuário tem permissão para acessar um projeto
        
        Args:
            access_request: Requisição de acesso
        
        Returns:
            Dict com resultado da verificação
        """
        # 1. Valida token
        token_validation = auth_service.validate_token(access_request.token)
        
        if not token_validation["valid"]:
            return self._deny_access(
                access_request,
                "token_invalido",
                f"Token inválido: {token_validation.get('error')}",
                severity="high"
            )
        
        user_id = token_validation["user_id"]
        user_email = token_validation["user_email"]
        
        # 2. Verifica se usuário tem permissão no projeto
        project_id = access_request.requested_project_id
        permissions = self.project_permissions.get(project_id, [])
        
        user_permission = next(
            (p for p in permissions 
             if p.user_id == user_id and p.is_active and not p.revoked_at),
            None
        )
        
        if not user_permission:
            return self._deny_access(
                access_request,
                "permissao_incorreta",
                f"Usuário {user_email} não possui permissão no projeto {project_id}",
                severity="critical",
                user_id=user_id,
                user_email=user_email
            )
        
        # 3. Verifica nível de permissão necessário
        required_levels = {
            "read": ["Visualizador", "Colaborador", "Administrador"],
            "write": ["Colaborador", "Administrador"],
            "update": ["Colaborador", "Administrador"],
            "delete": ["Administrador"]
        }
        
        required = required_levels.get(access_request.action, [])
        if user_permission.permission_level not in required:
            return self._deny_access(
                access_request,
                "permissao_incorreta",
                f"Usuário {user_email} não possui nível de permissão suficiente "
                f"({user_permission.permission_level}) para ação {access_request.action}",
                severity="high",
                user_id=user_id,
                user_email=user_email
            )
        
        # Acesso permitido
        return {
            "allowed": True,
            "user_id": user_id,
            "user_email": user_email,
            "permission_level": user_permission.permission_level,
            "project_id": project_id,
            "resource": access_request.requested_resource,
            "action": access_request.action,
            "timestamp": datetime.now().isoformat()
        }
    
    def check_miro_access(self, miro_request: MiroAccessRequest) -> Dict[str, Any]:
        """
        Verifica acesso ao Miro
        
        Args:
            miro_request: Requisição de acesso ao Miro
        
        Returns:
            Dict com resultado da verificação
        """
        # 1. Verifica se há autenticação
        if not miro_request.is_authenticated or not miro_request.token:
            return self._deny_miro_access(
                miro_request,
                "link_publico_bloqueado",
                "Tentativa de acesso ao Miro sem autenticação",
                severity="critical"
            )
        
        # 2. Valida token
        token_validation = auth_service.validate_token(miro_request.token)
        
        if not token_validation["valid"]:
            return self._deny_miro_access(
                miro_request,
                "token_invalido",
                f"Token inválido: {token_validation.get('error')}",
                severity="high"
            )
        
        user_id = token_validation["user_id"]
        user_email = token_validation["user_email"]
        
        # 3. Verifica se o board está vinculado a um projeto ativo
        project_id = miro_request.project_id
        
        # 4. Verifica permissão no projeto
        permissions = self.project_permissions.get(project_id, [])
        user_permission = next(
            (p for p in permissions 
             if p.user_id == user_id and p.is_active and not p.revoked_at),
            None
        )
        
        if not user_permission:
            return self._deny_miro_access(
                miro_request,
                "tentativa_acesso_indevedo",
                f"Usuário {user_email} não possui permissão no projeto {project_id}",
                severity="critical",
                user_id=user_id,
                user_email=user_email
            )
        
        # Acesso permitido
        return {
            "allowed": True,
            "user_id": user_id,
            "user_email": user_email,
            "project_id": project_id,
            "miro_board_id": miro_request.miro_board_id,
            "miro_link": miro_request.miro_link,
            "timestamp": datetime.now().isoformat()
        }
    
    def _deny_access(self, access_request: AccessRequest, incident_type: str,
                    description: str, severity: str = "high",
                    user_id: Optional[str] = None,
                    user_email: Optional[str] = None) -> Dict[str, Any]:
        """Registra acesso negado e cria incidente"""
        incident = SecurityIncident(
            incident_type=incident_type,
            severity=severity,
            user_email=user_email or access_request.user_email,
            user_id=user_id or access_request.user_id,
            project_id=access_request.requested_project_id,
            description=description,
            action_blocked=f"{access_request.action} em {access_request.requested_resource}",
            source="Middleware",
            metadata={
                "request_id": access_request.request_id,
                "resource": access_request.requested_resource,
                "action": access_request.action
            }
        )
        
        incident_dict = incident.model_dump(mode='json')
        self.repository.add_incident(incident_dict)
        
        return {
            "allowed": False,
            "reason": description,
            "incident_id": incident.incident_id,
            "incident_queue_id": incident.incident_queue_id,
            "timestamp": datetime.now().isoformat()
        }
    
    def _deny_miro_access(self, miro_request: MiroAccessRequest, incident_type: str,
                         description: str, severity: str = "high",
                         user_id: Optional[str] = None,
                         user_email: Optional[str] = None) -> Dict[str, Any]:
        """Registra acesso negado ao Miro e cria incidente"""
        incident = SecurityIncident(
            incident_type=incident_type,
            severity=severity,
            user_email=user_email or miro_request.user_email,
            user_id=user_id or miro_request.user_id,
            project_id=miro_request.project_id,
            description=description,
            action_blocked=f"Acesso ao Miro board {miro_request.miro_board_id}",
            source="Miro Middleware",
            metadata={
                "request_id": miro_request.request_id,
                "miro_board_id": miro_request.miro_board_id,
                "miro_link": miro_request.miro_link
            }
        )
        
        incident_dict = incident.model_dump(mode='json')
        self.repository.add_incident(incident_dict)
        
        return {
            "allowed": False,
            "reason": description,
            "incident_id": incident.incident_id,
            "incident_queue_id": incident.incident_queue_id,
            "timestamp": datetime.now().isoformat()
        }


# Singleton
access_control_service = AccessControlService()


