"""
Serviço de verificação de integridade de dados entre Miro e SharePoint
"""
import hashlib
import re
from datetime import datetime
from typing import Dict, Any, Optional
from uuid import uuid4

from models.security_models import (
    ChecksumValidation,
    DataIntegrityCheck,
    SecurityIncident
)
from storage.incident_repository import incident_repository


class IntegrityService:
    """Serviço de verificação de integridade e consistência de dados"""
    
    def __init__(self):
        self.repository = incident_repository
    
    def normalize_whitespace(self, text: str) -> str:
        """
        Normaliza whitespace (espaços, quebras de linha, tabs)
        Remove espaços extras e normaliza quebras de linha
        """
        # Remove espaços múltiplos
        text = re.sub(r' +', ' ', text)
        # Remove quebras de linha múltiplas
        text = re.sub(r'\n+', '\n', text)
        # Remove tabs
        text = text.replace('\t', ' ')
        # Remove espaços no início e fim de linhas
        lines = [line.strip() for line in text.split('\n')]
        # Remove linhas vazias
        lines = [line for line in lines if line]
        return '\n'.join(lines)
    
    def generate_checksum(self, data: str, normalize: bool = True) -> str:
        """
        Gera checksum SHA-256 do conteúdo
        
        Args:
            data: Dados para gerar checksum
            normalize: Se deve normalizar whitespace antes
        
        Returns:
            Hash SHA-256 em hexadecimal
        """
        if normalize:
            data = self.normalize_whitespace(data)
        
        return hashlib.sha256(data.encode('utf-8')).hexdigest()
    
    def validate_data_integrity(
        self,
        project_id: str,
        miro_data: str,
        sharepoint_data: str,
        data_type: str = "cronograma"
    ) -> Dict[str, Any]:
        """
        Valida integridade entre dados do Miro e SharePoint
        
        Args:
            project_id: ID do projeto
            miro_data: Dados exportados do Miro
            sharepoint_data: Dados armazenados no SharePoint
            data_type: Tipo de dado (cronograma, documento, etc.)
        
        Returns:
            Dict com resultado da validação
        """
        # Gera checksums normalizados (ignorando whitespace)
        miro_hash = self.generate_checksum(miro_data, normalize=True)
        sharepoint_hash = self.generate_checksum(sharepoint_data, normalize=True)
        
        # Compara checksums
        match_status = "match" if miro_hash == sharepoint_hash else "mismatch"
        
        # Cria validação de checksum
        checksum_validation = ChecksumValidation(
            project_id=project_id,
            miro_data_hash=miro_hash,
            sharepoint_data_hash=sharepoint_hash,
            miro_data_content=miro_data[:500],  # Primeiros 500 chars para log
            sharepoint_data_content=sharepoint_data[:500],
            match_status=match_status,
            whitespace_normalized=True,
            mismatch_details=None if match_status == "match" else "Dados divergem entre Miro e SharePoint"
        )
        
        # Cria verificação de integridade
        integrity_status = "ok" if match_status == "match" else "mismatch"
        sync_blocked = match_status == "mismatch"
        
        integrity_check = DataIntegrityCheck(
            source_system="Miro",
            target_system="SharePoint",
            data_type=data_type,
            project_id=project_id,
            checksum_validation=checksum_validation,
            integrity_status=integrity_status,
            sync_blocked=sync_blocked
        )
        
        # Se houver mismatch, registra incidente
        if match_status == "mismatch":
            incident = SecurityIncident(
                incident_type="inconsistencia_dados",
                severity="high",
                project_id=project_id,
                description=f"Inconsistência detectada entre dados do Miro e SharePoint para {data_type}",
                action_blocked="Sincronização bloqueada até correção",
                source="Middleware",
                metadata={
                    "data_type": data_type,
                    "miro_hash": miro_hash[:16] + "...",
                    "sharepoint_hash": sharepoint_hash[:16] + "...",
                    "checksum_validation_id": checksum_validation.validation_id
                }
            )
            
            incident_dict = incident.model_dump(mode='json')
            self.repository.add_incident(incident_dict)
        
        # Armazena validações
        checksum_dict = checksum_validation.model_dump(mode='json')
        integrity_dict = integrity_check.model_dump(mode='json')
        
        self.repository.add_checksum_validation(checksum_dict)
        self.repository.add_integrity_check(integrity_dict)
        
        return {
            "integrity_status": integrity_status,
            "match_status": match_status,
            "sync_blocked": sync_blocked,
            "checksum_validation_id": checksum_validation.validation_id,
            "integrity_check_id": integrity_check.check_id,
            "miro_hash": miro_hash,
            "sharepoint_hash": sharepoint_hash,
            "incident_id": incident.incident_id if match_status == "mismatch" else None,
            "timestamp": datetime.now().isoformat()
        }
    
    def compare_data_with_details(
        self,
        miro_data: str,
        sharepoint_data: str
    ) -> Dict[str, Any]:
        """
        Compara dados com detalhes das diferenças (para debug)
        
        Args:
            miro_data: Dados do Miro
            sharepoint_data: Dados do SharePoint
        
        Returns:
            Dict com detalhes da comparação
        """
        miro_normalized = self.normalize_whitespace(miro_data)
        sharepoint_normalized = self.normalize_whitespace(sharepoint_data)
        
        miro_hash = self.generate_checksum(miro_data, normalize=True)
        sharepoint_hash = self.generate_checksum(sharepoint_data, normalize=True)
        
        match = miro_hash == sharepoint_hash
        
        differences = []
        if not match:
            # Compara linha por linha
            miro_lines = miro_normalized.split('\n')
            sharepoint_lines = sharepoint_normalized.split('\n')
            
            max_lines = max(len(miro_lines), len(sharepoint_lines))
            for i in range(max_lines):
                miro_line = miro_lines[i] if i < len(miro_lines) else None
                sharepoint_line = sharepoint_lines[i] if i < len(sharepoint_lines) else None
                
                if miro_line != sharepoint_line:
                    differences.append({
                        "line": i + 1,
                        "miro": miro_line,
                        "sharepoint": sharepoint_line
                    })
        
        return {
            "match": match,
            "miro_hash": miro_hash,
            "sharepoint_hash": sharepoint_hash,
            "differences_count": len(differences),
            "differences": differences[:10],  # Limita a 10 diferenças
            "miro_length": len(miro_data),
            "sharepoint_length": len(sharepoint_data),
            "miro_normalized_length": len(miro_normalized),
            "sharepoint_normalized_length": len(sharepoint_normalized)
        }


# Singleton
integrity_service = IntegrityService()


