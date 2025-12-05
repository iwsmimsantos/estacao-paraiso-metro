"""
Middleware Principal - Sistema de Rastreabilidade RNF-03
Simulação do ecossistema Microsoft 365 com Sentinel
"""
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from datetime import datetime
import uvicorn

from api.sharepoint_api import router as sharepoint_router
from api.sentinel_api import router as sentinel_router

# Inicializa aplicação FastAPI
app = FastAPI(
    title="RNF-03 Rastreabilidade - Middleware de Correlação",
    description="""
    Sistema de simulação de rastreabilidade e auditoria para o ecossistema Microsoft 365.
    
    Este middleware simula a integração entre:
    - Microsoft SharePoint (Listas de Projetos)
    - Microsoft Sentinel (SIEM)
    - Power Automate (Fluxos de automação)
    - Microsoft Teams (Notificações)
    
    ## Componentes Simulados
    
    1. **API SharePoint**: Eventos de mudança em listas e formulários
    2. **API Sentinel**: Logs de segurança, alertas e correlação
    3. **Middleware de Correlação**: Normalização, hash e rastreabilidade
    4. **Repositório de Logs**: Armazenamento simulado em JSON
    
    ## Cenários Implementados
    
    1. Bloqueio de mudança sem justificativa
    2. Registro automático da mudança
    3. Validação de integridade e consistência dos logs
    4. Consulta e auditoria de mudanças
    5. Alerta de tentativas inválidas
    
    **Nota**: Esta é uma simulação mockada. Nenhuma conexão real com serviços Microsoft é estabelecida.
    """,
    version="1.0.0",
    contact={
        "name": "Companhia do Metrô - PMO",
        "email": "pmo@metrosp.com.br"
    }
)

# Registra routers das APIs
app.include_router(sharepoint_router)
app.include_router(sentinel_router)


@app.get("/")
async def root():
    """Endpoint raiz com informações do sistema"""
    return {
        "service": "RNF-03 Rastreabilidade - Middleware de Correlação",
        "version": "1.0.0",
        "status": "online",
        "timestamp": datetime.now().isoformat(),
        "description": "Sistema de simulação de rastreabilidade Microsoft 365",
        "endpoints": {
            "sharepoint": "/sharepoint",
            "sentinel": "/sentinel",
            "scenarios": "/scenarios",
            "docs": "/docs"
        },
        "components": {
            "sharepoint_api": "Simulação de eventos SharePoint/OfficeActivity",
            "sentinel_api": "Simulação de logs e alertas do Microsoft Sentinel",
            "middleware": "Correlação, normalização e rastreabilidade",
            "storage": "Repositório JSON de logs"
        }
    }


@app.get("/health")
async def health_check():
    """Verificação de saúde do sistema"""
    from storage.log_repository import log_repository
    
    stats = log_repository.get_statistics()
    
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "components": {
            "sharepoint_api": "ok",
            "sentinel_api": "ok",
            "middleware": "ok",
            "storage": "ok"
        },
        "statistics": stats
    }


@app.get("/scenarios")
async def list_scenarios():
    """Lista os 5 cenários simulados"""
    return {
        "scenarios": [
            {
                "id": "cenario_1",
                "name": "Bloqueio de mudança sem justificativa",
                "description": "Valida se o fluxo no Power Automate impede a atualização nas listas do SharePoint quando o campo 'Justificativa da mudança' estiver vazio",
                "endpoint": "POST /sharepoint/events/simulate-change?with_justification=false&scenario=cenario_1",
                "expected_result": "Mudança bloqueada, evento registrado no Sentinel, alerta gerado"
            },
            {
                "id": "cenario_2",
                "name": "Registro automático da mudança",
                "description": "Verifica se cada alteração aprovada gera um registro na lista 'Histórico de Alterações' no SharePoint e um evento correspondente no Sentinel",
                "endpoint": "POST /sharepoint/events/simulate-change?with_justification=true&scenario=cenario_2",
                "expected_result": "Mudança aprovada, registrada no histórico, log criado no Sentinel com correlationId"
            },
            {
                "id": "cenario_3",
                "name": "Validação de integridade e consistência dos logs",
                "description": "Testa se o Sentinel consegue correlacionar os eventos de origem (SharePoint / Power Automate) com os registros do Log Analytics",
                "endpoint": "GET /sentinel/integrity/verify?sharepoint_event_id={id}&sentinel_log_id={id}",
                "expected_result": "Comparação de hashes, status de integridade (ok/divergente)"
            },
            {
                "id": "cenario_4",
                "name": "Consulta e auditoria de mudanças",
                "description": "Avalia se as alterações podem ser rastreadas e auditadas no Sentinel, com trilha completa entre origem e destino",
                "endpoint": "POST /sentinel/audit-trail/create?correlation_id={id}",
                "expected_result": "Trilha de auditoria completa, pronta para visualização no Power BI"
            },
            {
                "id": "cenario_5",
                "name": "Alerta de tentativas inválidas",
                "description": "Confirma que tentativas de alteração sem justificativa ou fora do fluxo geram alertas automáticos no Sentinel e notificações via Teams",
                "endpoint": "POST /sentinel/simulate-invalid-attempt",
                "expected_result": "Alerta crítico gerado, notificação Teams enviada (simulado)"
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
    ╔═══════════════════════════════════════════════════════════════╗
    ║  RNF-03 Rastreabilidade - Middleware de Correlação           ║
    ║  Sistema de Simulação - Companhia do Metrô                   ║
    ╚═══════════════════════════════════════════════════════════════╝
    
    Iniciando servidor...
    
    Acesse a documentação interativa em:
    - Swagger UI: http://localhost:8000/docs
    - ReDoc: http://localhost:8000/redoc
    
    Cenários disponíveis em: http://localhost:8000/scenarios
    """)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )

