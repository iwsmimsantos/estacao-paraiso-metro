"""
Middleware Principal - Sistema de Segurança RNF-02
Simulação do ecossistema Microsoft 365 com controles de segurança
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import uvicorn

from api.middleware_api import router as middleware_router
from api.integrity_api import router as integrity_router

# Inicializa aplicação FastAPI
app = FastAPI(
    title="RNF-02 Segurança - Middleware de Controle de Acesso",
    description="""
    Sistema de simulação de segurança e controle de acesso para o ecossistema Microsoft 365.
    
    Este middleware simula a integração entre:
    - Microsoft Entra ID (Autenticação)
    - Middleware de Controle de Acesso (Autorização)
    - Miro (Quadros de brainstorming)
    - Microsoft SharePoint (Documentos e cronogramas)
    - Incident Queue (Fila de incidentes de segurança)
    
    ## Componentes Simulados
    
    1. **Serviço de Autenticação**: Validação de tokens e credenciais
    2. **Serviço de Controle de Acesso**: Verificação de permissões por projeto
    3. **Serviço de Integridade**: Validação de checksum entre Miro e SharePoint
    4. **Repositório de Incidentes**: Armazenamento de incidentes de segurança
    
    ## Cenários Implementados
    
    1. Cadastro incorreto de usuário no projeto ou portfólio
    2. Acesso indevido ao Miro antes do bloqueio
    3. Inconsistências entre dados do Miro e SharePoint
    
    **Nota**: Esta é uma simulação mockada. Nenhuma conexão real com serviços Microsoft é estabelecida.
    """,
    version="1.0.0",
    contact={
        "name": "Companhia do Metrô - PMO",
        "email": "pmo@metrosp.com.br"
    }
)

# Registra routers das APIs
app.include_router(middleware_router)
app.include_router(integrity_router)


@app.get("/")
async def root():
    """Endpoint raiz com informações do sistema"""
    return {
        "service": "RNF-02 Segurança - Middleware de Controle de Acesso",
        "version": "1.0.0",
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "description": "Sistema de simulação de segurança Microsoft 365",
        "endpoints": {
            "middleware": "/middleware",
            "integrity": "/integrity",
            "scenarios": "/scenarios",
            "docs": "/docs"
        },
        "components": {
            "auth_service": "Validação de tokens e autenticação",
            "access_control_service": "Controle de acesso baseado em permissões",
            "integrity_service": "Verificação de integridade de dados",
            "incident_repository": "Repositório de incidentes de segurança"
        }
    }


@app.get("/health")
async def health_check():
    """Verificação de saúde do sistema"""
    from storage.incident_repository import incident_repository
    
    stats = incident_repository.get_statistics()
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "components": {
            "auth_service": "ok",
            "access_control_service": "ok",
            "integrity_service": "ok",
            "incident_repository": "ok"
        },
        "statistics": stats
    }


@app.get("/scenarios")
async def list_scenarios():
    """Lista os 3 cenários simulados"""
    return {
        "scenarios": [
            {
                "id": "cenario_1",
                "name": "Cadastro incorreto de usuário no projeto ou portfólio",
                "description": "Verifica se o sistema impede o acesso de usuários não vinculados ao projeto ou portfólio correto",
                "endpoint": "POST /middleware/access/check",
                "expected_result": "Acesso bloqueado, incidente registrado na incident queue"
            },
            {
                "id": "cenario_2",
                "name": "Acesso indevido ao Miro antes do bloqueio",
                "description": "Garante que apenas usuários autenticados possam acessar os quadros do Miro relacionados aos projetos ativos",
                "endpoint": "POST /middleware/miro/access/check",
                "expected_result": "Acesso bloqueado para links públicos, tokens inválidos e usuários sem permissão"
            },
            {
                "id": "cenario_3",
                "name": "Inconsistências entre dados do Miro e SharePoint",
                "description": "Garante que os dados transmitidos entre Miro e SharePoint permaneçam idênticos, evitando divergências",
                "endpoint": "POST /integrity/validate",
                "expected_result": "Inconsistências detectadas, sincronização bloqueada, incidente registrado"
            }
        ]
    }


@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Tratamento global de exceções"""
    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc),
            "timestamp": datetime.now().isoformat(),
            "message": "Erro interno do sistema"
        }
    )


if __name__ == "__main__":
    print("""
    ===============================================================
      RNF-02 Seguranca - Middleware de Controle de Acesso
      Sistema de Simulacao - Companhia do Metro
    ===============================================================
    
    Iniciando servidor...
    
    Acesse a documentacao interativa em:
    - Swagger UI: http://localhost:8000/docs
    - ReDoc: http://localhost:8000/redoc
    
    Cenarios disponiveis em: http://localhost:8000/scenarios
    """)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

