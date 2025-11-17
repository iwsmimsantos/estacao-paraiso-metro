"""Cálculo de hashes para verificação de integridade"""
import hashlib
import json
from typing import Any, Dict


def calculate_sha256(data: str) -> str:
    """
    Calcula hash SHA-256 de uma string.
    
    Args:
        data: String para calcular hash
    
    Returns:
        str: Hash SHA-256 em hexadecimal
    """
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def calculate_payload_hash(payload: Dict[str, Any]) -> str:
    """
    Calcula hash SHA-256 de um payload JSON.
    
    Args:
        payload: Dicionário para calcular hash
    
    Returns:
        str: Hash SHA-256 em hexadecimal
    """
    # Serializa o payload de forma determinística
    json_str = json.dumps(payload, sort_keys=True, separators=(',', ':'))
    return calculate_sha256(json_str)


def verify_hash(data: str, expected_hash: str) -> bool:
    """
    Verifica se o hash de uma string corresponde ao esperado.
    
    Args:
        data: String para verificar
        expected_hash: Hash esperado
    
    Returns:
        bool: True se o hash corresponde, False caso contrário
    """
    actual_hash = calculate_sha256(data)
    return actual_hash == expected_hash


def verify_payload_hash(payload: Dict[str, Any], expected_hash: str) -> bool:
    """
    Verifica se o hash de um payload corresponde ao esperado.
    
    Args:
        payload: Dicionário para verificar
        expected_hash: Hash esperado
    
    Returns:
        bool: True se o hash corresponde, False caso contrário
    """
    actual_hash = calculate_payload_hash(payload)
    return actual_hash == expected_hash
