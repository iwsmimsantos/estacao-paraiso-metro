"""
Autenticação Simplificada para Desenvolvimento/Demonstração

Em produção real, seria substituído por Microsoft Entra ID (Azure AD) com SSO corporativo.
Para fins de demonstração, permite autenticação simples via user_id nos headers.
"""
from typing import Optional
from fastapi import Header, HTTPException, status
from .auth import UserDatabase, User

# Instância do banco de usuários
user_db = UserDatabase()


async def get_current_user_simple(
    x_user_id: Optional[str] = Header(None, description="ID do usuário (simulação de SSO)")
) -> User:
    """
    Autenticação simplificada para demonstração
    
    Em produção, isso seria substituído por:
    - Microsoft Entra ID (Azure AD)
    - OAuth 2.0 / OpenID Connect
    - Token automático via SSO corporativo
    
    Para demonstração, aceita user_id no header X-User-Id
    """
    if not x_user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário não autenticado. Forneça X-User-Id no header (simulação de SSO corporativo)",
            headers={"WWW-Authenticate": "X-User-Id"},
        )
    
    user = user_db.get_user(x_user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Usuário {x_user_id} não encontrado"
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuário inativo"
        )
    
    return user


def get_user_info(user_id: str) -> Optional[User]:
    """Helper para buscar informações de usuário"""
    return user_db.get_user(user_id)
