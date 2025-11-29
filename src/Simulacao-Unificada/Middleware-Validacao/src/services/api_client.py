"""
Cliente HTTP para integração com a API Mockada

Gerencia comunicação com os serviços mockados:
- Miro (boards e atividades)
- SharePoint (documentos e sites)
- Sentinel (incidentes e alertas)
- Copilot (sessões e mensagens)
"""
import httpx
from typing import Optional, Dict, Any, List
from datetime import datetime


class APIClient:
    """Cliente base para comunicação com API mockada"""
    
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.timeout = 30.0
    
    async def _request(
        self,
        method: str,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Faz requisição HTTP para a API mockada"""
        url = f"{self.base_url}{endpoint}"
        
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    json=json_data
                )
                response.raise_for_status()
                return response.json()
            
            except httpx.HTTPStatusError as e:
                return {
                    "error": True,
                    "status_code": e.response.status_code,
                    "message": f"HTTP Error: {e.response.status_code}",
                    "detail": str(e)
                }
            
            except httpx.RequestError as e:
                return {
                    "error": True,
                    "message": "API não acessível",
                    "detail": str(e),
                    "suggestion": "Certifique-se de que a API mockada está rodando na porta 8000"
                }
            
            except Exception as e:
                return {
                    "error": True,
                    "message": "Erro inesperado",
                    "detail": str(e)
                }


class MiroClient(APIClient):
    """Cliente para API do Miro"""
    
    async def get_boards(
        self,
        user_id: Optional[str] = None,
        tenant_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Lista boards do Miro"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        if tenant_id:
            params["tenant_id"] = tenant_id
        
        return await self._request("GET", "/miro/boards", params=params)
    
    async def get_board_activities(
        self,
        board_id: str,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtém atividades de um board específico"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request(
            "GET",
            f"/miro/boards/{board_id}/activities",
            params=params
        )
    
    async def get_audit_logs(
        self,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtém logs de auditoria do Miro"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request("GET", "/miro/audit-logs", params=params)


class SharePointClient(APIClient):
    """Cliente para API do SharePoint"""
    
    async def get_sites(
        self,
        user_id: Optional[str] = None,
        tenant_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Lista sites do SharePoint"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        if tenant_id:
            params["tenant_id"] = tenant_id
        
        return await self._request("GET", "/sharepoint/sites", params=params)
    
    async def get_site_documents(
        self,
        site_id: str,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Lista documentos de um site"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request(
            "GET",
            f"/sharepoint/sites/{site_id}/documents",
            params=params
        )
    
    async def get_audit_logs(
        self,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtém logs de auditoria do SharePoint"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request("GET", "/sharepoint/audit-logs", params=params)


class SentinelClient(APIClient):
    """Cliente para API do Sentinel"""
    
    async def get_incidents(
        self,
        user_id: Optional[str] = None,
        severity: Optional[str] = None
    ) -> Dict[str, Any]:
        """Lista incidentes de segurança"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        if severity:
            params["severity"] = severity
        
        return await self._request("GET", "/sentinel/incidents", params=params)
    
    async def get_alerts(
        self,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Lista alertas agregados"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request("GET", "/sentinel/alerts", params=params)
    
    async def get_events(
        self,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Lista eventos normalizados"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request("GET", "/sentinel/events", params=params)


class CopilotClient(APIClient):
    """Cliente para API do Copilot"""
    
    async def get_sessions(
        self,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Lista sessões do Copilot"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request("GET", "/copilot/sessions", params=params)
    
    async def get_session_messages(
        self,
        session_id: str,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtém mensagens de uma sessão"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request(
            "GET",
            f"/copilot/sessions/{session_id}/messages",
            params=params
        )
    
    async def get_audit_events(
        self,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Obtém eventos de auditoria do Copilot"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request("GET", "/copilot/audit-events", params=params)


# Instâncias globais dos clientes
miro_client = MiroClient()
sharepoint_client = SharePointClient()
sentinel_client = SentinelClient()
copilot_client = CopilotClient()


# Importa Office client
try:
    from .office_client import office_client
except ImportError:
    office_client = None
