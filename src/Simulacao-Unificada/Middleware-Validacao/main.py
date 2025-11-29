from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

from src.api import auth as auth_routes
from src.api import monitoring as monitoring_routes
from src.api import validation_simple as validation_simple_routes
from src.api import workflows as workflow_routes

app = FastAPI(
    title="Middleware de Validação - Metrô SP",
    description="""
    Middleware responsável por:
    - Validação de autenticação e autorização (SSO simulado)
    - Controle de acesso por projeto
    - Validação de integridade de dados (checksum)
    - Rastreabilidade de ações
    - Guardrails para agentes de IA
    
    Integra-se com a API mockada para simular o ambiente real do Metrô.
    
    **Integrações:**
    - 🎨 Miro: Boards e planejamento
    - 📁 SharePoint: Documentos e sites
    - 🤖 Microsoft 365 Copilot: IA e assistência
    - 📧 Microsoft 365 Office: Documentos, emails e calendário
    - 🛡️ Microsoft Sentinel: Auditoria e segurança
    
    ---
    
    **🚀 Como usar:**
    
    Todos os endpoints de validação usam **autenticação simplificada** que simula SSO corporativo.
    Basta adicionar o header `X-User-Id` nas requisições!
    
    **👤 Usuários de teste:**
    - `u001` - Admin (acesso total)
    - `u010` - Manager (gerenciamento)
    - `u025` - Analyst (análise)
    - `u050` - Viewer (apenas leitura - vai gerar incidentes!)
    
    ---
    
    **📊 Recursos:**
    - **Dashboard em tempo real:** [/dashboard](/dashboard)
    - **Documentação interativa:** [/docs](/docs)
    - **Health check:** [/health](/health)
    
    **Em produção real:** Seria usado Microsoft Entra ID (Azure AD) com SSO automático.
    """,
    version="1.0.0"
)

# Registra rotas
app.include_router(auth_routes.router)
app.include_router(monitoring_routes.router)
app.include_router(validation_simple_routes.router)  # Validação simplificada (SSO simulado)
app.include_router(workflow_routes.router)


@app.get("/", response_class=HTMLResponse)
async def root():
    """Página inicial com informações do middleware"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Middleware de Validação - Metrô SP</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            }
            h1 {
                text-align: center;
                margin-bottom: 10px;
            }
            .subtitle {
                text-align: center;
                opacity: 0.9;
                margin-bottom: 30px;
            }
            .status {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin: 30px 0;
            }
            .status-card {
                background: rgba(255, 255, 255, 0.2);
                padding: 20px;
                border-radius: 10px;
                text-align: center;
            }
            .status-card h3 {
                margin: 0 0 10px 0;
                font-size: 1.2em;
            }
            .status-indicator {
                font-size: 2em;
                margin: 10px 0;
            }
            .links {
                display: flex;
                gap: 15px;
                justify-content: center;
                flex-wrap: wrap;
                margin-top: 30px;
            }
            .link-button {
                background: rgba(255, 255, 255, 0.3);
                padding: 12px 24px;
                border-radius: 8px;
                text-decoration: none;
                color: white;
                font-weight: bold;
                transition: all 0.3s;
            }
            .link-button:hover {
                background: rgba(255, 255, 255, 0.5);
                transform: translateY(-2px);
            }
            .features {
                margin-top: 30px;
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 15px;
            }
            .feature {
                background: rgba(255, 255, 255, 0.15);
                padding: 15px;
                border-radius: 8px;
                border-left: 4px solid rgba(255, 255, 255, 0.5);
            }
            .feature h4 {
                margin: 0 0 8px 0;
            }
            .feature p {
                margin: 0;
                opacity: 0.9;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🔒 Middleware de Validação</h1>
            <p class="subtitle">Sistema de Gestão de Projetos - Metrô de São Paulo</p>
            
            <div class="status">
                <div class="status-card">
                    <h3>Status do Sistema</h3>
                    <div class="status-indicator">✅</div>
                    <p>Operacional</p>
                </div>
                <div class="status-card">
                    <h3>API Mockada</h3>
                    <div class="status-indicator">🔗</div>
                    <p>Conectado</p>
                </div>
                <div class="status-card">
                    <h3>Rastreabilidade</h3>
                    <div class="status-indicator">📊</div>
                    <p>Ativa</p>
                </div>
            </div>

            <div class="features">
                <div class="feature">
                    <h4>🔐 RNF-01: Segurança</h4>
                    <p>Autenticação, controle de acesso, validação de integridade e guardrails de IA</p>
                </div>
                <div class="feature">
                    <h4>📈 RNF-02: Escalabilidade</h4>
                    <p>Rate limiting, circuit breaker e monitoramento de performance</p>
                </div>
                <div class="feature">
                    <h4>🔍 RNF-03: Rastreabilidade</h4>
                    <p>Logs estruturados, incident queue e auditoria completa</p>
                </div>
            </div>

            <div class="links">
                <a href="/docs" class="link-button">📚 Documentação da API</a>
                <a href="/health" class="link-button">💚 Health Check</a>
                <a href="/dashboard" class="link-button">📊 Dashboard</a>
            </div>
        </div>
    </body>
    </html>
    """


@app.get("/health")
async def health_check():
    """Endpoint de health check"""
    return {
        "status": "healthy",
        "service": "middleware-validacao",
        "version": "1.0.0",
        "components": {
            "authentication": "operational",
            "logging": "operational",
            "api_integration": "operational"
        }
    }


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    """Dashboard de monitoramento em tempo real"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Dashboard - Middleware</title>
        <meta charset="UTF-8">
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                padding: 20px;
                background: #0f0f23;
                color: #eee;
            }
            .header {
                text-align: center;
                margin-bottom: 30px;
            }
            h1 {
                color: #00d9ff;
                margin-bottom: 10px;
            }
            .refresh-info {
                color: #888;
                font-size: 0.9em;
            }
            .refresh-btn {
                background: #00d9ff;
                color: #000;
                border: none;
                padding: 8px 20px;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
                margin-left: 10px;
            }
            .refresh-btn:hover {
                background: #00bfe6;
            }
            .dashboard {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }
            .card {
                background: #1a1a2e;
                border-radius: 12px;
                padding: 20px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
                border: 1px solid #2a2a4e;
            }
            .card.full-width {
                grid-column: 1 / -1;
            }
            .card h2 {
                margin: 0 0 15px 0;
                color: #00d9ff;
                font-size: 1.3em;
                display: flex;
                align-items: center;
                gap: 10px;
            }
            .integration-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 15px;
            }
            .integration-card {
                background: rgba(0, 217, 255, 0.05);
                padding: 15px;
                border-radius: 8px;
                text-align: center;
                border: 2px solid transparent;
                transition: all 0.3s;
            }
            .integration-card.healthy {
                border-color: #00ff88;
            }
            .integration-card.unhealthy {
                border-color: #ff4444;
            }
            .integration-icon {
                font-size: 2.5em;
                margin-bottom: 8px;
            }
            .integration-name {
                font-weight: bold;
                margin-bottom: 5px;
            }
            .integration-status {
                font-size: 0.85em;
                padding: 4px 8px;
                border-radius: 4px;
                display: inline-block;
            }
            .status-healthy {
                background: rgba(0, 255, 136, 0.2);
                color: #00ff88;
            }
            .status-unhealthy {
                background: rgba(255, 68, 68, 0.2);
                color: #ff4444;
            }
            .log-container {
                max-height: 400px;
                overflow-y: auto;
                background: #0a0a16;
                padding: 15px;
                border-radius: 8px;
            }
            .log-entry {
                background: rgba(0, 217, 255, 0.08);
                padding: 12px;
                margin: 8px 0;
                border-radius: 6px;
                border-left: 3px solid #00d9ff;
                font-size: 0.9em;
                font-family: 'Consolas', monospace;
            }
            .log-entry.incident {
                border-left-color: #ff4444;
                background: rgba(255, 68, 68, 0.1);
            }
            .log-timestamp {
                color: #888;
                font-size: 0.85em;
                margin-bottom: 4px;
            }
            .log-event {
                color: #00d9ff;
                font-weight: bold;
                margin-bottom: 4px;
            }
            .log-user {
                color: #ffaa00;
            }
            .log-details {
                color: #aaa;
                font-size: 0.85em;
                margin-top: 6px;
            }
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(4, 1fr);
                gap: 15px;
            }
            .stat-box {
                background: rgba(0, 217, 255, 0.05);
                padding: 20px;
                border-radius: 8px;
                text-align: center;
            }
            .stat-value {
                font-size: 2.5em;
                font-weight: bold;
                color: #00d9ff;
                margin: 10px 0;
            }
            .stat-label {
                color: #888;
                font-size: 0.9em;
            }
            .no-data {
                text-align: center;
                padding: 40px;
                color: #666;
            }
            ::-webkit-scrollbar {
                width: 8px;
            }
            ::-webkit-scrollbar-track {
                background: #0a0a16;
            }
            ::-webkit-scrollbar-thumb {
                background: #00d9ff;
                border-radius: 4px;
            }
            .loading {
                text-align: center;
                padding: 20px;
                color: #00d9ff;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 Dashboard de Monitoramento</h1>
            <div class="refresh-info">
                Última atualização: <span id="last-update">Carregando...</span>
                <button class="refresh-btn" onclick="loadAllData()">🔄 Atualizar</button>
            </div>
        </div>

        <div class="dashboard">
            <!-- Integrações -->
            <div class="card full-width">
                <h2>🔗 Status das Integrações</h2>
                <div id="integrations-container" class="integration-grid">
                    <div class="loading">Carregando status das integrações...</div>
                </div>
            </div>

            <!-- Estatísticas -->
            <div class="card full-width">
                <h2>📈 Estatísticas Gerais</h2>
                <div id="stats-container" class="stats-grid">
                    <div class="loading">Carregando estatísticas...</div>
                </div>
            </div>

            <!-- Logs Recentes -->
            <div class="card full-width">
                <h2>📋 Logs Recentes</h2>
                <div id="logs-container" class="log-container">
                    <div class="loading">Carregando logs...</div>
                </div>
            </div>

            <!-- Incidentes -->
            <div class="card full-width">
                <h2>⚠️ Incident Queue</h2>
                <div id="incidents-container" class="log-container">
                    <div class="loading">Carregando incidentes...</div>
                </div>
            </div>
        </div>

        <script>
            // Ícones para cada integração
            const integrationIcons = {
                miro: '🎨',
                sharepoint: '📁',
                copilot: '🤖',
                office: '📧',
                sentinel: '🛡️'
            };

            // Atualizar timestamp
            function updateTimestamp() {
                const now = new Date();
                document.getElementById('last-update').textContent = now.toLocaleString('pt-BR');
            }

            // Carregar status das integrações
            async function loadIntegrations() {
                try {
                    const response = await fetch('/workflows/integration/health');
                    const data = await response.json();
                    
                    const container = document.getElementById('integrations-container');
                    container.innerHTML = '';

                    for (const [name, status] of Object.entries(data.integrations)) {
                        const isHealthy = status === 'healthy';
                        const card = document.createElement('div');
                        card.className = `integration-card ${isHealthy ? 'healthy' : 'unhealthy'}`;
                        card.innerHTML = `
                            <div class="integration-icon">${integrationIcons[name] || '🔌'}</div>
                            <div class="integration-name">${name.toUpperCase()}</div>
                            <div class="integration-status ${isHealthy ? 'status-healthy' : 'status-unhealthy'}">
                                ${isHealthy ? '✓ Online' : '✗ Offline'}
                            </div>
                        `;
                        container.appendChild(card);
                    }
                } catch (error) {
                    console.error('Erro ao carregar integrações:', error);
                    document.getElementById('integrations-container').innerHTML = 
                        '<div class="no-data">Erro ao carregar status das integrações</div>';
                }
            }

            // Carregar estatísticas
            async function loadStats() {
                try {
                    const response = await fetch('/monitoring/stats');
                    const data = await response.json();
                    
                    const summary = data.summary || {};
                    const topUsers = data.top_users || [];
                    
                    const container = document.getElementById('stats-container');
                    container.innerHTML = `
                        <div class="stat-box">
                            <div class="stat-label">Total de Logs</div>
                            <div class="stat-value">${summary.total_logs || 0}</div>
                        </div>
                        <div class="stat-box">
                            <div class="stat-label">Incidentes</div>
                            <div class="stat-value" style="color: ${(summary.total_incidents || 0) > 0 ? '#ff4444' : '#00ff88'}">
                                ${summary.total_incidents || 0}
                            </div>
                        </div>
                        <div class="stat-box">
                            <div class="stat-label">Usuários Únicos</div>
                            <div class="stat-value">${topUsers.length || 0}</div>
                        </div>
                        <div class="stat-box">
                            <div class="stat-label">Taxa de Erro</div>
                            <div class="stat-value" style="color: ${(summary.error_rate_percent || 0) > 10 ? '#ff4444' : '#00ff88'}">
                                ${summary.error_rate_percent || 0}%
                            </div>
                        </div>
                    `;
                } catch (error) {
                    console.error('Erro ao carregar estatísticas:', error);
                    document.getElementById('stats-container').innerHTML = 
                        '<div class="no-data">Erro ao carregar estatísticas</div>';
                }
            }

            // Carregar logs recentes
            async function loadLogs() {
                try {
                    const response = await fetch('/monitoring/logs?limit=10');
                    const data = await response.json();
                    const logs = data.logs || [];
                    
                    const container = document.getElementById('logs-container');
                    
                    if (logs.length === 0) {
                        container.innerHTML = '<div class="no-data">Nenhum log registrado ainda</div>';
                        return;
                    }

                    container.innerHTML = logs.map(log => {
                        const timestamp = log.timestamp || 'N/A';
                        const eventType = log.event_type || 'unknown';
                        const userId = log.user_id || 'N/A';
                        const status = log.status || 'unknown';
                        const projectId = log.project_id || null;
                        const traceId = log.trace_id || null;
                        
                        // Cor do status
                        let statusColor = '#888';
                        if (status === 'success') statusColor = '#00ff88';
                        if (status === 'failed') statusColor = '#ff4444';
                        if (status === 'denied') statusColor = '#ffaa00';
                        
                        return `
                        <div class="log-entry">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                <div class="log-timestamp">${new Date(timestamp).toLocaleString('pt-BR')}</div>
                                <div style="background: ${statusColor}20; color: ${statusColor}; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; font-weight: bold;">
                                    ${status.toUpperCase()}
                                </div>
                            </div>
                            <div class="log-event">${eventType}</div>
                            <div class="log-user">👤 ${userId}</div>
                            ${projectId ? `<div class="log-details">📁 Projeto: ${projectId}</div>` : ''}
                            ${traceId ? `<div class="log-details">🔍 Trace: ${traceId.substring(0, 12)}...</div>` : ''}
                        </div>
                    `}).join('');
                } catch (error) {
                    console.error('Erro ao carregar logs:', error);
                    document.getElementById('logs-container').innerHTML = 
                        '<div class="no-data">Erro ao carregar logs</div>';
                }
            }

            // Carregar incidentes
            async function loadIncidents() {
                try {
                    const response = await fetch('/monitoring/incidents?limit=20');
                    const data = await response.json();
                    const incidents = data.incidents || [];
                    
                    const container = document.getElementById('incidents-container');
                    
                    if (incidents.length === 0) {
                        container.innerHTML = '<div class="no-data">✅ Nenhum incidente registrado - Sistema operando normalmente</div>';
                        return;
                    }

                    container.innerHTML = incidents.map(incident => {
                        const timestamp = incident.timestamp || 'N/A';
                        const eventType = incident.event_type || 'unknown';
                        const userId = incident.user_id || 'N/A';
                        const reason = incident.reason || incident.details?.reason || null;
                        const severity = incident.details?.severity || 'medium';
                        const traceId = incident.trace_id || null;
                        
                        // Cor por severidade
                        let severityColor = '#ffaa00';
                        if (severity === 'critical' || severity === 'high') severityColor = '#ff4444';
                        if (severity === 'low') severityColor = '#00d9ff';
                        
                        return `
                        <div class="log-entry incident">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
                                <div class="log-timestamp">${new Date(timestamp).toLocaleString('pt-BR')}</div>
                                <div style="background: ${severityColor}20; color: ${severityColor}; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; font-weight: bold;">
                                    ${severity.toUpperCase()}
                                </div>
                            </div>
                            <div class="log-event">⚠️ ${eventType}</div>
                            <div class="log-user">👤 ${userId}</div>
                            ${reason ? `<div class="log-details">📝 ${reason}</div>` : ''}
                            ${traceId ? `<div class="log-details">🔍 Trace: ${traceId.substring(0, 12)}...</div>` : ''}
                        </div>
                    `}).join('');
                } catch (error) {
                    console.error('Erro ao carregar incidentes:', error);
                    document.getElementById('incidents-container').innerHTML = 
                        '<div class="no-data">Erro ao carregar incidentes</div>';
                }
            }

            // Carregar todos os dados
            async function loadAllData() {
                updateTimestamp();
                await Promise.all([
                    loadIntegrations(),
                    loadStats(),
                    loadLogs(),
                    loadIncidents()
                ]);
            }

            // Auto-refresh a cada 10 segundos
            setInterval(loadAllData, 10000);

            // Carregar dados iniciais
            loadAllData();
        </script>
    </body>
    </html>
    """


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8001,
        reload=True
    )
