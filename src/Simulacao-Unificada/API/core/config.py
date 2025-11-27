"""
Configurações centrais da aplicação de APIs mockadas.
Define caminhos, constantes e parâmetros gerais do sistema.
"""

from pathlib import Path

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Caminho para o arquivo CSV de usuários
USERS_CSV_PATH = BASE_DIR / "data" / "users.csv"

# Configurações de paginação padrão
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# Configurações de performance simulada (em ms)
MIN_PROCESSING_TIME_MS = 5
MAX_PROCESSING_TIME_MS = 120

# Nomes dos serviços
SERVICES = {
    "sharepoint": "sharepoint",
    "miro": "miro",
    "copilot": "copilot",
    "office": "office",
    "sentinel": "sentinel"
}

# Labels de sensibilidade disponíveis
SENSITIVITY_LABELS = ["Public", "Internal", "Confidential", "Highly Confidential"]

# Políticas de retenção disponíveis
RETENTION_POLICIES = ["30d", "90d", "1y", "3y", "7y", "indefinite"]

