"""
Cliente para Microsoft 365 Office

Gerencia integração com Office (Word, Excel, PowerPoint, Outlook)
"""
from typing import Optional, Dict, Any
from .api_client import APIClient


class OfficeClient(APIClient):
    """Cliente para API do Office"""
    
    async def get_documents(
        self,
        user_id: Optional[str] = None,
        document_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Lista documentos do Office (Word/Excel/PowerPoint)
        
        Args:
            user_id: Filtrar por usuário
            document_type: Tipo de documento (word, excel, powerpoint)
        """
        params = {}
        if user_id:
            params["user_id"] = user_id
        if document_type:
            params["document_type"] = document_type
        
        return await self._request("GET", "/office/documents", params=params)
    
    async def get_emails(
        self,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Lista e-mails do Outlook"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request("GET", "/office/emails", params=params)
    
    async def get_calendar_events(
        self,
        user_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """Lista eventos de calendário"""
        params = {}
        if user_id:
            params["user_id"] = user_id
        
        return await self._request("GET", "/office/calendar-events", params=params)


# Instância global
office_client = OfficeClient()
