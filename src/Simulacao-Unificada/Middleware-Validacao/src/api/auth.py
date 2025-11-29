"""
Endpoints de Autenticação

Rotas para login, logout e gerenciamento de tokens.
"""
from fastapi import APIRouter, HTTPException, Depends, Header
from typing import Optional

from ..core.auth import login, get_current_user, user_db, Token, User
from ..monitoring.logger import log_event, log_incident, EventType


router = APIRouter(prefix="/auth", tags=["Autenticação"])


@router.post("/login", response_model=Token)
async def login_endpoint(user_id: str):
    """
    Login simplificado usando apenas user_id
    
    Em produção, receberia email/password e validaria credenciais
    """
    token = login(user_id)
    
    # Log de autenticação
    if token:
        log_event(
            event_type=EventType.AUTH_LOGIN,
            user_id=user_id,
            action="login",
            status="success",
            details={"projects": token.projects}
        )
    else:
        log_incident(
            incident_type="auth_failed",
            severity="medium",
            user_id=user_id,
            description=f"Tentativa de login falhou para user_id: {user_id}"
        )
    
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Usuário não encontrado ou inativo"
        )
    
    return token


@router.get("/me", response_model=User)
async def get_current_user_endpoint(authorization: Optional[str] = Header(None)):
    """Retorna informações do usuário autenticado"""
    
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Token não fornecido"
        )
    
    token = authorization.replace("Bearer ", "")
    user = get_current_user(token)
    
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Token inválido ou expirado"
        )
    
    return user


@router.get("/users")
async def list_users():
    """Lista todos os usuários disponíveis (para fins de desenvolvimento)"""
    users = []
    
    for user_id, user in user_db.users.items():
        users.append({
            "user_id": user.user_id,
            "display_name": user.display_name,
            "email": user.email,
            "department": user.department,
            "role": user.role,
            "projects": user.projects,
            "is_active": user.is_active
        })
    
    return {
        "total": len(users),
        "users": users
    }


@router.get("/users/{user_id}/projects")
async def get_user_projects(user_id: str):
    """Lista projetos que um usuário tem acesso"""
    user = user_db.get_user(user_id)
    
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return {
        "user_id": user.user_id,
        "display_name": user.display_name,
        "projects": user.projects,
        "total_projects": len(user.projects)
    }
