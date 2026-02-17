# WorkTime - Architektur-Übersicht

## Technologie-Stack (Vorschlag)

### Backend-Optionen
1. **Python + Flask/FastAPI**
   - Vorteile: Schnelle Entwicklung, gute Libraries
   - Empfohlen für: Schneller Prototyp, REST API

2. **Node.js + Express**
   - Vorteile: JavaScript überall, große Community
   - Empfohlen für: Full-Stack JavaScript

3. **Java + Spring Boot**
   - Vorteile: Enterprise-ready, robust
   - Empfohlen für: Größere Anwendungen

### Datenbank-Optionen
- **SQLite**: Für einfache lokale Nutzung
- **PostgreSQL**: Für Production-Ready Anwendungen
- **MySQL/MariaDB**: Alternative relationale DB

### Frontend-Optionen
1. **CLI (Command Line Interface)**
   - Schnellste Implementierung
   - Gut für Power-User

2. **Web-Interface**
   - React, Vue.js oder Vanilla JavaScript
   - Zugänglich für alle Benutzer

3. **Desktop-App**
   - Electron oder native Frameworks
   - Offline-Fähigkeit

## Datenmodell (Konzept)

### TimeEntry (Zeiteintrag)
```
- id: UUID
- user_id: UUID
- project_id: UUID (optional)
- start_time: DateTime
- end_time: DateTime (optional, null wenn aktiv)
- description: String
- tags: Array<String>
- created_at: DateTime
- updated_at: DateTime
```

### Project (Projekt)
```
- id: UUID
- name: String
- description: String
- color: String (für UI)
- created_at: DateTime
- updated_at: DateTime
```

### User (Benutzer)
```
- id: UUID
- name: String
- email: String
- created_at: DateTime
- updated_at: DateTime
```

## API-Endpunkte (Konzept)

### Zeiteinträge
- `POST /api/time-entries` - Neuer Zeiteintrag
- `GET /api/time-entries` - Liste aller Einträge
- `GET /api/time-entries/:id` - Spezifischer Eintrag
- `PUT /api/time-entries/:id` - Eintrag aktualisieren
- `DELETE /api/time-entries/:id` - Eintrag löschen
- `POST /api/time-entries/start` - Zeitmessung starten
- `POST /api/time-entries/stop` - Zeitmessung stoppen

### Projekte
- `POST /api/projects` - Neues Projekt
- `GET /api/projects` - Liste aller Projekte
- `GET /api/projects/:id` - Spezifisches Projekt
- `PUT /api/projects/:id` - Projekt aktualisieren
- `DELETE /api/projects/:id` - Projekt löschen

### Berichte
- `GET /api/reports/daily` - Tagesbericht
- `GET /api/reports/weekly` - Wochenbericht
- `GET /api/reports/monthly` - Monatsbericht
- `GET /api/reports/export` - Daten exportieren

## Nächste Entscheidungen

1. **Technologie-Stack wählen**: Basierend auf Anforderungen und Erfahrung
2. **Deployment-Strategie**: Lokal, Server, oder Cloud
3. **Authentifizierung**: Falls Multi-User Support gewünscht
