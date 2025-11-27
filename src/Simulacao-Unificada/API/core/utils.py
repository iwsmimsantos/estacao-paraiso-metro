"""
Utilitários comuns para todas as APIs.
Inclui carregamento de CSV, geração de dados mockados e helpers.
"""

import csv
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from uuid import uuid4

from .config import USERS_CSV_PATH, MIN_PROCESSING_TIME_MS, MAX_PROCESSING_TIME_MS


def load_users_from_csv() -> List[Dict[str, str]]:
    """
    Carrega usuários do arquivo CSV compartilhado.
    
    Returns:
        Lista de dicionários com dados dos usuários
    """
    users = []
    with open(USERS_CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Converte string boolean para bool
            row['is_active'] = row['is_active'].lower() == 'true'
            row['mfa_enabled'] = row['mfa_enabled'].lower() == 'true'
            users.append(row)
    return users


def get_user_by_id(user_id: str) -> Optional[Dict[str, str]]:
    """
    Busca um usuário específico pelo ID.
    
    Args:
        user_id: ID do usuário a buscar
        
    Returns:
        Dicionário com dados do usuário ou None se não encontrado
    """
    users = load_users_from_csv()
    for user in users:
        if user['user_id'] == user_id:
            return user
    return None


def filter_users(
    tenant_id: Optional[str] = None,
    department: Optional[str] = None,
    role: Optional[str] = None
) -> List[Dict[str, str]]:
    """
    Filtra usuários por critérios opcionais.
    
    Args:
        tenant_id: ID do tenant para filtrar
        department: Departamento para filtrar
        role: Papel/função para filtrar
        
    Returns:
        Lista filtrada de usuários
    """
    users = load_users_from_csv()
    
    if tenant_id:
        users = [u for u in users if u['tenant_id'] == tenant_id]
    if department:
        users = [u for u in users if u['department'] == department]
    if role:
        users = [u for u in users if u['role'] == role]
    
    return users


def generate_uuid() -> str:
    """Gera um UUID aleatório como string."""
    return str(uuid4())


def generate_processing_time() -> int:
    """
    Gera um tempo de processamento fictício em milissegundos.
    
    Returns:
        Tempo em ms entre MIN_PROCESSING_TIME_MS e MAX_PROCESSING_TIME_MS
    """
    return random.randint(MIN_PROCESSING_TIME_MS, MAX_PROCESSING_TIME_MS)


def generate_random_datetime(
    days_ago_min: int = 1,
    days_ago_max: int = 30
) -> str:
    """
    Gera uma data/hora aleatória no passado em formato ISO UTC.
    
    Args:
        days_ago_min: Mínimo de dias no passado
        days_ago_max: Máximo de dias no passado
        
    Returns:
        String no formato ISO 8601 UTC
    """
    days_ago = random.randint(days_ago_min, days_ago_max)
    hours_ago = random.randint(0, 23)
    minutes_ago = random.randint(0, 59)
    
    dt = datetime.utcnow() - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def generate_random_ip() -> str:
    """Gera um endereço IP privado fictício."""
    return f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"


def generate_device_id() -> str:
    """Gera um ID de dispositivo fictício."""
    return f"device-{random.choice(['win', 'mac', 'linux', 'ios', 'android'])}-{random.randint(100, 999)}"


def paginate_items(
    items: List[any],
    page: int = 1,
    page_size: int = 20
) -> tuple[List[any], int]:
    """
    Pagina uma lista de itens.
    
    Args:
        items: Lista completa de itens
        page: Número da página (começa em 1)
        page_size: Tamanho da página
        
    Returns:
        Tupla com (itens_da_pagina, total_de_itens)
    """
    total = len(items)
    start = (page - 1) * page_size
    end = start + page_size
    
    return items[start:end], total


def get_random_users(count: int = 1) -> List[Dict[str, str]]:
    """
    Retorna usuários aleatórios do CSV.
    
    Args:
        count: Número de usuários a retornar
        
    Returns:
        Lista de dicionários de usuários
    """
    users = load_users_from_csv()
    return random.sample(users, min(count, len(users)))


def get_random_user() -> Dict[str, str]:
    """Retorna um usuário aleatório do CSV."""
    return get_random_users(1)[0]

