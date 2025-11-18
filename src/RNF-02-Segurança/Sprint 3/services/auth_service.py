"""
Serviço de autenticação e validação de tokens
"""
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
from uuid import uuid4

from models.security_models import AuthenticationToken
from storage.incident_repository import incident_repository


class AuthService:
    """Serviço de autenticação e validação de tokens"""
    
    def __init__(self):
        self.repository = incident_repository
        self.valid_tokens: Dict[str, AuthenticationToken] = {}
    
    def validate_token(self, token: str) -> Dict[str, Any]:
        """
        Valida um token de autenticação
        
        Returns:
            Dict com status da validação e informações do usuário
        """
        # Simula validação do token
        # Em produção, validaria com Microsoft Entra ID
        
        # Procura token válido
        auth_token = self.valid_tokens.get(token)
        
        if not auth_token:
            return {
                "valid": False,
                "error": "Token não encontrado ou inválido",
                "user_id": None,
                "user_email": None
            }
        
        # Verifica expiração
        if datetime.now() > auth_token.expires_at:
            return {
                "valid": False,
                "error": "Token expirado",
                "user_id": auth_token.user_id,
                "user_email": auth_token.user_email
            }
        
        # Verifica se token está marcado como inválido
        if not auth_token.is_valid:
            return {
                "valid": False,
                "error": "Token revogado",
                "user_id": auth_token.user_id,
                "user_email": auth_token.user_email
            }
        
        return {
            "valid": True,
            "user_id": auth_token.user_id,
            "user_email": auth_token.user_email,
            "token_id": auth_token.token_id
        }
    
    def register_token(self, user_id: str, user_email: str, 
                      source: str = "Microsoft Entra ID") -> Dict[str, Any]:
        """
        Registra um novo token de autenticação
        
        Args:
            user_id: ID do usuário
            user_email: Email do usuário
            source: Fonte do token
        
        Returns:
            Dict com token_value e AuthenticationToken
        """
        token_id = str(uuid4())
        token_value = f"TOKEN-{token_id[:8].upper()}"
        
        auth_token = AuthenticationToken(
            token_id=token_id,
            user_email=user_email,
            user_id=user_id,
            issued_at=datetime.now(),
            expires_at=datetime.now() + timedelta(hours=8),
            is_valid=True,
            source=source
        )
        
        self.valid_tokens[token_value] = auth_token
        
        return {
            "token_value": token_value,
            "auth_token": auth_token
        }
    
    def revoke_token(self, token: str) -> bool:
        """Revoga um token"""
        auth_token = self.valid_tokens.get(token)
        if auth_token:
            auth_token.is_valid = False
            return True
        return False


# Singleton
auth_service = AuthService()

