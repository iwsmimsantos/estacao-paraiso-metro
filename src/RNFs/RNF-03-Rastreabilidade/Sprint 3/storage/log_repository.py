"""
Repositório de armazenamento de logs em JSON
"""
import json
import os
from typing import List, Optional, Dict, Any
from datetime import datetime
from pathlib import Path


class LogRepository:
    """Gerencia armazenamento e recuperação de logs"""
    
    def __init__(self, data_dir: str = "data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        
        self.files = {
            "sharepoint_events": self.data_dir / "sharepoint_events.json",
            "sentinel_logs": self.data_dir / "sentinel_logs.json",
            "correlated_logs": self.data_dir / "correlated_logs.json",
            "historico_alteracoes": self.data_dir / "historico_alteracoes.json",
            "alertas": self.data_dir / "alertas.json",
            "audit_trails": self.data_dir / "audit_trails.json"
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
    
    def add_sharepoint_event(self, event: dict):
        """Adiciona evento do SharePoint"""
        events = self._read_json(self.files["sharepoint_events"])
        events.append(event)
        self._write_json(self.files["sharepoint_events"], events)
        return event
    
    def add_sentinel_log(self, log: dict):
        """Adiciona log do Sentinel"""
        logs = self._read_json(self.files["sentinel_logs"])
        logs.append(log)
        self._write_json(self.files["sentinel_logs"], logs)
        return log
    
    def add_correlated_log(self, log: dict):
        """Adiciona log correlacionado"""
        logs = self._read_json(self.files["correlated_logs"])
        logs.append(log)
        self._write_json(self.files["correlated_logs"], logs)
        return log
    
    def add_historico_alteracao(self, historico: dict):
        """Adiciona registro ao histórico de alterações"""
        historicos = self._read_json(self.files["historico_alteracoes"])
        historicos.append(historico)
        self._write_json(self.files["historico_alteracoes"], historicos)
        return historico
    
    def add_alerta(self, alerta: dict):
        """Adiciona alerta"""
        alertas = self._read_json(self.files["alertas"])
        alertas.append(alerta)
        self._write_json(self.files["alertas"], alertas)
        return alerta
    
    def add_audit_trail(self, trail: dict):
        """Adiciona trilha de auditoria"""
        trails = self._read_json(self.files["audit_trails"])
        trails.append(trail)
        self._write_json(self.files["audit_trails"], trails)
        return trail
    
    def get_sharepoint_events(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera eventos do SharePoint"""
        events = self._read_json(self.files["sharepoint_events"])
        if filter_by:
            events = [e for e in events if all(e.get(k) == v for k, v in filter_by.items())]
        return events
    
    def get_sentinel_logs(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera logs do Sentinel"""
        logs = self._read_json(self.files["sentinel_logs"])
        if filter_by:
            logs = [l for l in logs if all(l.get(k) == v for k, v in filter_by.items())]
        return logs
    
    def get_correlated_logs(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera logs correlacionados"""
        logs = self._read_json(self.files["correlated_logs"])
        if filter_by:
            logs = [l for l in logs if all(l.get(k) == v for k, v in filter_by.items())]
        return logs
    
    def get_historico_alteracoes(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera histórico de alterações"""
        historicos = self._read_json(self.files["historico_alteracoes"])
        if filter_by:
            historicos = [h for h in historicos if all(h.get(k) == v for k, v in filter_by.items())]
        return historicos
    
    def get_alertas(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera alertas"""
        alertas = self._read_json(self.files["alertas"])
        if filter_by:
            alertas = [a for a in alertas if all(a.get(k) == v for k, v in filter_by.items())]
        return alertas
    
    def get_audit_trails(self, filter_by: Optional[dict] = None) -> List[dict]:
        """Recupera trilhas de auditoria"""
        trails = self._read_json(self.files["audit_trails"])
        if filter_by:
            trails = [t for t in trails if all(t.get(k) == v for k, v in filter_by.items())]
        return trails
    
    def get_by_correlation_id(self, correlation_id: str) -> dict:
        """Recupera todos os logs relacionados a um correlation_id"""
        return {
            "correlation_id": correlation_id,
            "sharepoint_events": self.get_sharepoint_events(),
            "sentinel_logs": self.get_sentinel_logs({"correlation_id": correlation_id}),
            "correlated_logs": self.get_correlated_logs({"correlation_id": correlation_id}),
            "historico_alteracoes": self.get_historico_alteracoes({"correlation_id": correlation_id}),
            "alertas": self.get_alertas({"correlation_id": correlation_id})
        }
    
    def get_by_project_id(self, project_id: str) -> dict:
        """Recupera todos os logs relacionados a um projeto"""
        return {
            "project_id": project_id,
            "sharepoint_events": self.get_sharepoint_events({"project_id": project_id}),
            "sentinel_logs": self.get_sentinel_logs({"project_id": project_id}),
            "correlated_logs": self.get_correlated_logs({"project_id": project_id}),
            "historico_alteracoes": self.get_historico_alteracoes({"project_id": project_id}),
            "alertas": self.get_alertas({"affected_project": project_id})
        }
    
    def clear_all(self):
        """Limpa todos os dados (útil para testes)"""
        for file_path in self.files.values():
            self._write_json(file_path, [])
    
    def get_statistics(self) -> dict:
        """Retorna estatísticas gerais do repositório"""
        return {
            "total_sharepoint_events": len(self._read_json(self.files["sharepoint_events"])),
            "total_sentinel_logs": len(self._read_json(self.files["sentinel_logs"])),
            "total_correlated_logs": len(self._read_json(self.files["correlated_logs"])),
            "total_historico_alteracoes": len(self._read_json(self.files["historico_alteracoes"])),
            "total_alertas": len(self._read_json(self.files["alertas"])),
            "total_audit_trails": len(self._read_json(self.files["audit_trails"]))
        }


# Singleton
log_repository = LogRepository()

