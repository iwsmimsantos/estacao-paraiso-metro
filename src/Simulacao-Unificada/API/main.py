from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from routers import sharepoint, miro, copilot, office, sentinel

# Inicializa aplicação FastAPI
app = FastAPI(
    title="APIs Unificadas - Simulação Ambiente Metrô",
    description="""
     APIs Mockadas 
    
     1. SharePoint
    - Sites, documentos e logs de auditoria
    - Políticas de retenção e sensibilidade
    - Rastreamento de acesso e modificações
    
     2. Miro
    - Boards colaborativos
    - Atividades e histórico de edições
    - Compartilhamento e permissões
    
     3. Microsoft 365 Copilot
    - Sessões de IA
    - Mensagens e prompts
    - Contexto de sensibilidade e auditoria
    
     4. Microsoft 365 Office
    - Documentos (Word, Excel, PowerPoint)
    - E-mails (Outlook)
    - Eventos de calendário
    
     5. Microsoft Sentinel
    - Incidentes de segurança
    - Alertas agregados
    - Eventos normalizados de todos os serviços
    
    
    
     Dados Mockados
    
    Todos os dados são gerados a partir de um CSV (`data/users.csv`) contendo:
    - Usuários de diferentes departamentos
    - Tenants múltiplos
    - Níveis de risco e configurações de MFA
    
    
    
     Recursos
    
    - Documentação Interativa: `/docs` (Swagger UI)
    - Esquema OpenAPI: `/openapi.json`
    - Redirecionamento: `/` → `/docs`
    
    
    
     Resposta Padrão
    
    Todas as respostas seguem o formato:
    
    ```json
    {
      "request_id": "uuid",
      "service": "sharepoint|miro|copilot|office|sentinel",
      "timestamp_utc": "2025-11-27T10:15:00Z",
      "correlation_id": "uuid",
      "data": { ... },
      "meta": {
        "page": 1,
        "page_size": 20,
        "total_items": 100,
        "security_context": { ... },
        "traceability": { ... },
        "performance": { ... }
      }
    }
    ```
    """,
    version="1.0.0",
    contact={
        "name": "Equipe de Desenvolvimento",
        "email": "dev@empresa.com"
    },
    license_info={
        "name": "MIT"
    },
    openapi_tags=[
        {
            "name": "SharePoint",
            "description": "Operações relacionadas a sites e documentos do SharePoint"
        },
        {
            "name": "Miro",
            "description": "Operações relacionadas a boards colaborativos do Miro"
        },
        {
            "name": "Copilot",
            "description": "Operações relacionadas a sessões e mensagens do Microsoft 365 Copilot"
        },
        {
            "name": "Office",
            "description": "Operações relacionadas a documentos, e-mails e calendário do Microsoft 365"
        },
        {
            "name": "Sentinel",
            "description": "Operações relacionadas a incidentes, alertas e eventos de segurança"
        }
    ]
)

# Registra routers das APIs
app.include_router(sharepoint.router)
app.include_router(miro.router)
app.include_router(copilot.router)
app.include_router(office.router)
app.include_router(sentinel.router)


@app.get("/", include_in_schema=False)
async def root():
    """
    Redireciona para a documentação Swagger.
    """
    return RedirectResponse(url="/docs")


@app.get("/health")
async def health_check():
    """
    Endpoint de health check para monitoramento.
    """
    return {
        "status": "healthy",
        "services": [
            "sharepoint",
            "miro",
            "copilot",
            "office",
            "sentinel"
        ],
        "version": "1.0.0"
    }


if __name__ == "__main__":
    import uvicorn
    
    # Inicia servidor de desenvolvimento
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

