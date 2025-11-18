"""
Serviço de Guardrails para Agentes de IA

NOTA: Este serviço é um STUB (esboço) que simula a ausência de implementação.
Todos os métodos retornam que a funcionalidade não está implementada,
fazendo com que os testes falhem conforme esperado.

Quando o sistema estiver pronto, este serviço deverá:
- Validar semanticamente as requisições de IA
- Verificar permissões do agente
- Detectar tentativas de acesso fora do escopo
- Bloquear inferências e vazamentos indiretos
- Registrar incidentes na incident queue
"""
from datetime import datetime
from typing import Dict, Any, List
from uuid import uuid4

from models.security_models import (
    AIAgentRequest,
    AIAgentResponse,
    SecurityIncident
)
from storage.incident_repository import incident_repository


class AIGuardrailsService:
    """
    Serviço de segurança para agentes de IA
    
    IMPORTANTE: Esta é uma implementação STUB.
    O serviço sempre retorna que não está implementado,
    fazendo os testes falharem conforme esperado.
    """
    
    def __init__(self):
        self.repository = incident_repository
        self.implemented = False  # Flag indicando que não está implementado
    
    def validate_ai_request(self, ai_request: AIAgentRequest) -> Dict[str, Any]:
        """
        Valida uma requisição de agente de IA
        
        STUB: Sempre retorna que não está implementado
        
        Quando implementado, deve:
        1. Analisar a intenção da requisição (validação semântica)
        2. Verificar se o prompt tenta acessar dados fora do escopo
        3. Detectar comandos ambíguos ou manipulativos
        4. Bloquear tentativas de bypass dos guardrails
        
        Args:
            ai_request: Requisição do agente de IA
        
        Returns:
            Dict indicando que não está implementado
        """
        return {
            "validated": False,
            "implemented": False,
            "error": "Guardrails de IA não implementados",
            "message": "O sistema ainda não possui validação semântica de requisições de IA",
            "request_id": ai_request.request_id
        }
    
    def analyze_ai_response(self, ai_response: AIAgentResponse, 
                           allowed_project_id: str,
                           blocked_project_ids: List[str]) -> Dict[str, Any]:
        """
        Analisa a resposta gerada por um agente de IA
        
        STUB: Sempre retorna que não está implementado
        
        Quando implementado, deve:
        1. Verificar se a resposta contém dados de projetos bloqueados
        2. Detectar inferências ou deduções indevidas
        3. Identificar vazamento semântico
        4. Bloquear respostas que extrapolem o escopo permitido
        
        Args:
            ai_response: Resposta gerada pela IA
            allowed_project_id: ID do projeto permitido
            blocked_project_ids: IDs dos projetos bloqueados
        
        Returns:
            Dict indicando que não está implementado
        """
        return {
            "safe": False,
            "implemented": False,
            "error": "Análise de resposta de IA não implementada",
            "message": "O sistema ainda não possui detecção de vazamento semântico",
            "response_id": ai_response.response_id
        }
    
    def check_scope_violation(self, prompt: str, allowed_project_id: str,
                             blocked_project_ids: List[str]) -> Dict[str, Any]:
        """
        Verifica se um prompt tenta violar o escopo permitido
        
        STUB: Sempre retorna que não está implementado
        
        Quando implementado, deve detectar tentativas como:
        - "Compare o andamento deste projeto com outros projetos"
        - "Resuma tudo o que você sabe relacionado ao orçamento"
        - "Liste padrões comuns entre projetos similares"
        - "Verifique se existe algum documento com a palavra X nos diretórios"
        
        Args:
            prompt: Comando/pergunta do usuário
            allowed_project_id: Projeto permitido
            blocked_project_ids: Projetos bloqueados
        
        Returns:
            Dict indicando que não está implementado
        """
        return {
            "violation_detected": False,
            "implemented": False,
            "error": "Detecção de violação de escopo não implementada",
            "message": "O sistema ainda não possui validação semântica de prompts"
        }
    
    def register_ai_incident(self, incident_type: str, agent_id: str,
                            description: str, prompt: str,
                            response: str, project_id: str,
                            severity: str = "critical") -> Dict[str, Any]:
        """
        Registra um incidente de segurança relacionado a IA
        
        STUB: Retorna que não pode registrar porque o sistema não está implementado
        
        Quando implementado, deve registrar:
        - Comando recebido
        - Resposta gerada pela IA
        - Data/hora
        - Agente responsável
        - Motivo da falha (ex.: vazamento indireto)
        
        Args:
            incident_type: Tipo do incidente
            agent_id: ID do agente de IA
            description: Descrição do incidente
            prompt: Comando que causou o incidente
            response: Resposta gerada
            project_id: ID do projeto
            severity: Severidade do incidente
        
        Returns:
            Dict indicando que não foi registrado
        """
        return {
            "registered": False,
            "implemented": False,
            "error": "Registro de incidentes de IA não implementado",
            "message": "O sistema ainda não possui incident queue para eventos de IA"
        }


# Singleton
ai_guardrails_service = AIGuardrailsService()
