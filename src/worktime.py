"""
WorkTime - Einfache CLI-Zeiterfassung
Beispiel-Implementation in Python
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict
import uuid


class TimeEntry:
    """Repräsentiert einen Zeiteintrag"""
    
    def __init__(self, description: str, project: Optional[str] = None, 
                 start_time: Optional[datetime] = None, entry_id: Optional[str] = None):
        self.id = entry_id or str(uuid.uuid4())
        self.description = description
        self.project = project
        self.start_time = start_time or datetime.now()
        self.end_time: Optional[datetime] = None
        self.tags: List[str] = []
    
    def stop(self):
        """Stoppt den Zeiteintrag"""
        self.end_time = datetime.now()
    
    def duration_minutes(self) -> Optional[float]:
        """Berechnet die Dauer in Minuten"""
        if self.end_time:
            return (self.end_time - self.start_time).total_seconds() / 60
        return None
    
    def is_running(self) -> bool:
        """Prüft ob der Eintrag noch läuft"""
        return self.end_time is None
    
    def to_dict(self) -> Dict:
        """Konvertiert zu Dictionary für Speicherung"""
        return {
            'id': self.id,
            'description': self.description,
            'project': self.project,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'tags': self.tags
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'TimeEntry':
        """Erstellt TimeEntry aus Dictionary"""
        entry = cls(
            description=data['description'],
            project=data.get('project'),
            start_time=datetime.fromisoformat(data['start_time']),
            entry_id=data['id']
        )
        if data.get('end_time'):
            entry.end_time = datetime.fromisoformat(data['end_time'])
        entry.tags = data.get('tags', [])
        return entry


class WorkTimeApp:
    """Hauptanwendung für Zeiterfassung"""
    
    def __init__(self, data_file: str = 'worktime_data.json'):
        self.data_file = Path(data_file)
        self.entries: List[TimeEntry] = []
        self.load_data()
    
    def load_data(self):
        """Lädt gespeicherte Zeiteinträge"""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if content:
                        data = json.loads(content)
                        self.entries = [TimeEntry.from_dict(e) for e in data.get('entries', [])]
            except (json.JSONDecodeError, IOError):
                # Bei Fehler leere Liste verwenden
                self.entries = []
    
    def save_data(self):
        """Speichert Zeiteinträge"""
        data = {'entries': [e.to_dict() for e in self.entries]}
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def start_entry(self, description: str, project: Optional[str] = None) -> TimeEntry:
        """Startet einen neuen Zeiteintrag"""
        # Stoppe laufende Einträge
        self.stop_running_entries()
        
        entry = TimeEntry(description, project)
        self.entries.append(entry)
        self.save_data()
        return entry
    
    def stop_running_entries(self):
        """Stoppt alle laufenden Einträge"""
        for entry in self.entries:
            if entry.is_running():
                entry.stop()
        self.save_data()
    
    def get_running_entry(self) -> Optional[TimeEntry]:
        """Gibt den aktuell laufenden Eintrag zurück"""
        for entry in self.entries:
            if entry.is_running():
                return entry
        return None
    
    def get_entries_today(self) -> List[TimeEntry]:
        """Gibt alle Einträge von heute zurück"""
        today = datetime.now().date()
        return [e for e in self.entries if e.start_time.date() == today]
    
    def total_time_today(self) -> float:
        """Berechnet die Gesamtzeit von heute in Minuten"""
        entries = self.get_entries_today()
        total = 0.0
        for entry in entries:
            if entry.end_time:
                total += entry.duration_minutes() or 0
        return total


def main():
    """Hauptfunktion für CLI"""
    import sys
    
    app = WorkTimeApp()
    
    if len(sys.argv) < 2:
        print("WorkTime - Zeiterfassung")
        print("\nVerwendung:")
        print("  python worktime.py start <beschreibung> [projekt]  - Startet Zeiteintrag")
        print("  python worktime.py stop                             - Stoppt laufenden Eintrag")
        print("  python worktime.py status                           - Zeigt aktuellen Status")
        print("  python worktime.py today                            - Zeigt heutige Einträge")
        return
    
    command = sys.argv[1].lower()
    
    if command == 'start':
        if len(sys.argv) < 3:
            print("Fehler: Beschreibung erforderlich")
            return
        description = sys.argv[2]
        project = sys.argv[3] if len(sys.argv) > 3 else None
        entry = app.start_entry(description, project)
        print(f"✓ Zeiteintrag gestartet: {description}")
        if project:
            print(f"  Projekt: {project}")
        print(f"  Start: {entry.start_time.strftime('%H:%M:%S')}")
    
    elif command == 'stop':
        running = app.get_running_entry()
        if running:
            app.stop_running_entries()
            duration = running.duration_minutes()
            print(f"✓ Zeiteintrag gestoppt: {running.description}")
            print(f"  Dauer: {duration:.1f} Minuten ({duration/60:.2f} Stunden)")
        else:
            print("Kein laufender Zeiteintrag")
    
    elif command == 'status':
        running = app.get_running_entry()
        if running:
            elapsed = (datetime.now() - running.start_time).total_seconds() / 60
            print(f"⏱  Laufender Eintrag: {running.description}")
            if running.project:
                print(f"   Projekt: {running.project}")
            print(f"   Gestartet: {running.start_time.strftime('%H:%M:%S')}")
            print(f"   Dauer: {elapsed:.1f} Minuten")
        else:
            print("Kein laufender Zeiteintrag")
            total = app.total_time_today()
            print(f"\nHeute erfasst: {total:.1f} Minuten ({total/60:.2f} Stunden)")
    
    elif command == 'today':
        entries = app.get_entries_today()
        if not entries:
            print("Heute noch keine Einträge")
            return
        
        print(f"Heutige Einträge ({len(entries)}):\n")
        total = 0.0
        for entry in entries:
            duration = entry.duration_minutes()
            status = "läuft" if entry.is_running() else f"{duration:.1f} min"
            project_info = f" [{entry.project}]" if entry.project else ""
            print(f"  {entry.start_time.strftime('%H:%M')} - {status:>12} : {entry.description}{project_info}")
            if duration:
                total += duration
        
        print(f"\nGesamt: {total:.1f} Minuten ({total/60:.2f} Stunden)")
    
    else:
        print(f"Unbekannter Befehl: {command}")


if __name__ == '__main__':
    main()
