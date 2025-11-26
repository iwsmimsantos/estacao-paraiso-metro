"""
Repositório de armazenamento de incidentes e logs de segurança
"""
import json
import os
from typing import List, Optional, Dict, Any
from datetime import datetime
from pathlib import Path


class IncidentRepository:
    """Gerencia armazenamento e recuperação de incidentes e logs de segurança"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        self.files = {
            "incidents": self.data_dir / "security_incidents.json",
            "checksum_validations": self.data_dir / "checksum_validations.json",
            "integrity_checks": self.data_dir / "integrity_checks.json",
            "access_logs": self.data_dir / "access_logs.json"
        }
        
        # Inicializa arquivos se não existirem
        for file_path in self.files.values():
            if not file_path.exists():
                self._write_json(file_path, [])
    
    def _read_json(self, file_path: Path) -> List[Dict[Any, Any]]:
        """Lê arquivo JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _write_json(self, file_path: Path, data: List[Dict[Any, Any]]):
        """Escreve arquivo JSON"""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
    
    def add_incident(self, incident: dict):
        """Adiciona incidente à incident queue"""
        incidents = self._read_json(self.files["incidents"])
        incidents.append(incident)
        self._write_json(self.files["incidents"], incidents)
        return incident
    
    def add_checksum_validation(self, validation: dict):
        """Adiciona validação de checksum"""
        validations = self._read_json(self.files["checksum_validations"])
        validations.append(validation)
        self._write_json(self.files["checksum_validations"], validations)
        return validation
    
    def add_integrity_check(self, check: dict):
        """Adiciona verificação de integridade"""
        checks = self._read_json(self.files["integrity_checks"])
        checks.append(check)
        self._write_json(self.files["integrity_checks"], checks)
        return check
    
    def add_access_log(self, log: dict):
        """Adiciona log de acesso"""
        logs = self._read_json(self.files["access_logs"])
        logs.append(log)
        self._write_json(self.files["access_logs"], logs)
        return log
    
    def get_incidents(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera incidentes da incident queue"""
        incidents = self._read_json(self.files["incidents"])
        if filter_by:
            incidents = [i for i in incidents if all(i.get(k) == v for k, v in filter_by.items())]
        return incidents
    
    def get_checksum_validations(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera validações de checksum"""
        validations = self._read_json(self.files["checksum_validations"])
        if filter_by:
            validations = [v for v in validations if all(v.get(k) == val for k, val in filter_by.items())]
        return validations
    
    def get_integrity_checks(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera verificações de integridade"""
        checks = self._read_json(self.files["integrity_checks"])
        if filter_by:
            checks = [c for c in checks if all(c.get(k) == v for k, v in filter_by.items())]
        return checks
    
    def get_access_logs(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera logs de acesso"""
        logs = self._read_json(self.files["access_logs"])
        if filter_by:
            logs = [l for l in logs if all(l.get(k) == v for k, v in filter_by.items())]
        return logs
    
    def get_statistics(self) -> dict:
        """Retorna estatísticas do repositório"""
        incidents = self._read_json(self.files["incidents"])
        checksum_validations = self._read_json(self.files["checksum_validations"])
        integrity_checks = self._read_json(self.files["integrity_checks"])
        access_logs = self._read_json(self.files["access_logs"])
        
        # Conta por tipo de incidente
        incident_types = {}
        for incident in incidents:
            incident_type = incident.get("incident_type", "unknown")
            incident_types[incident_type] = incident_types.get(incident_type, 0) + 1
        
        # Conta por severidade
        severities = {}
        for incident in incidents:
            severity = incident.get("severity", "unknown")
            severities[severity] = severities.get(severity, 0) + 1
        
        # Conta incidentes não resolvidos
        unresolved = len([i for i in incidents if not i.get("resolved", False)])
        
        # Conta validações de checksum
        mismatches = len([v for v in checksum_validations if v.get("match_status") == "mismatch"])
        matches = len([v for v in checksum_validations if v.get("match_status") == "match"])
        
        return {
            "total_incidents": len(incidents),
            "unresolved_incidents": unresolved,
            "resolved_incidents": len(incidents) - unresolved,
            "incidents_by_type": incident_types,
            "incidents_by_severity": severities,
            "total_checksum_validations": len(checksum_validations),
            "checksum_matches": matches,
            "checksum_mismatches": mismatches,
            "total_integrity_checks": len(integrity_checks),
            "total_access_logs": len(access_logs)
        }
    
    def clear_all(self):
        """Limpa todos os dados (para testes)"""
        for file_path in self.files.values():
            self._write_json(file_path, [])


# Singleton
incident_repository = IncidentRepository()

