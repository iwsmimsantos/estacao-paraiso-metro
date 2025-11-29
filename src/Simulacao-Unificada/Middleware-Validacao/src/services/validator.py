"""
Serviço de Validação de Dados

Implementa validação de integridade entre Miro e SharePoint:
- Checksum de dados
- Detecção de mismatch
- Normalização de whitespace
"""
import hashlib
import json
import re
from typing import Dict, Any, Optional, Tuple


class DataValidator:
    """Validador de integridade de dados"""
    
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """
        Normaliza whitespace para evitar falsos positivos
        
        Remove espaços extras, tabs e quebras de linha inconsistentes
        """
        if not isinstance(text, str):
            text = str(text)
        
        # Remove espaços no início e fim
        text = text.strip()
        
        # Substitui múltiplos espaços por um único
        text = re.sub(r'\s+', ' ', text)
        
        # Normaliza quebras de linha
        text = text.replace('\r\n', '\n')
        
        return text
    
    @staticmethod
    def calculate_checksum(data: Any) -> str:
        """
        Calcula checksum SHA-256 de dados
        
        Args:
            data: Dados para calcular checksum (dict, str, list, etc)
        
        Returns:
            Hash SHA-256 em hexadecimal
        """
        if isinstance(data, dict):
            # Serializa dict de forma ordenada para consistência
            content = json.dumps(data, sort_keys=True, ensure_ascii=False)
        elif isinstance(data, str):
            content = data
        else:
            content = str(data)
        
        # Normaliza whitespace antes de calcular hash
        content = DataValidator.normalize_whitespace(content)
        
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
    
    @staticmethod
    def compare_data(
        source_data: Any,
        target_data: Any,
        ignore_whitespace: bool = True
    ) -> Tuple[bool, Optional[str]]:
        """
        Compara dois conjuntos de dados
        
        Args:
            source_data: Dados de origem (ex: Miro)
            target_data: Dados de destino (ex: SharePoint)
            ignore_whitespace: Se True, ignora diferenças de whitespace
        
        Returns:
            Tupla (is_equal, difference_message)
        """
        source_checksum = DataValidator.calculate_checksum(source_data)
        target_checksum = DataValidator.calculate_checksum(target_data)
        
        is_equal = source_checksum == target_checksum
        
        if is_equal:
            return True, None
        
        # Calcula diferença
        difference_msg = f"Checksum mismatch: source={source_checksum[:16]}... target={target_checksum[:16]}..."
        
        return False, difference_msg
    
    @staticmethod
    def validate_miro_to_sharepoint(
        miro_data: Dict[str, Any],
        sharepoint_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Valida consistência entre dados do Miro e SharePoint
        
        Args:
            miro_data: Dados exportados do Miro
            sharepoint_data: Dados no SharePoint
        
        Returns:
            Resultado da validação com detalhes
        """
        result = {
            "validation_passed": False,
            "miro_checksum": None,
            "sharepoint_checksum": None,
            "is_consistent": False,
            "differences": [],
            "timestamp": None
        }
        
        try:
            # Calcula checksums
            miro_checksum = DataValidator.calculate_checksum(miro_data)
            sharepoint_checksum = DataValidator.calculate_checksum(sharepoint_data)
            
            result["miro_checksum"] = miro_checksum
            result["sharepoint_checksum"] = sharepoint_checksum
            
            # Compara
            is_equal, diff_msg = DataValidator.compare_data(miro_data, sharepoint_data)
            result["is_consistent"] = is_equal
            
            if not is_equal:
                result["differences"].append(diff_msg)
            
            result["validation_passed"] = True
            
        except Exception as e:
            result["error"] = str(e)
        
        return result


# Instância global do validador
data_validator = DataValidator()
