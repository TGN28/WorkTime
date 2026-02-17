# WorkTime
Zeiterfassungs-App

## Übersicht

WorkTime ist eine Anwendung zur Zeiterfassung, die es Benutzern ermöglicht, ihre Arbeitszeiten zu erfassen, zu verwalten und auszuwerten.

## Geplante Features

- ⏱️ **Zeiterfassung**: Start/Stopp von Zeiteinträgen
- 📊 **Projekt-Verwaltung**: Organisation nach Projekten und Aufgaben
- 📈 **Berichte**: Übersichten und Statistiken über erfasste Zeiten
- 💾 **Daten-Export**: Export als CSV oder PDF
- 👤 **Benutzerverwaltung**: Mehrere Benutzer und Teams

## Nächste Schritte

Um mit der Entwicklung zu beginnen:

1. **Technologie-Stack wählen**: Entscheide dich für eine Technologie (z.B. Python, Node.js, Java)
2. **Projekt-Struktur erstellen**: Richte Ordner für Quellcode, Tests und Dokumentation ein
3. **Datenmodell definieren**: Erstelle Modelle für Zeiteinträge, Projekte und Benutzer
4. **Basisfunktionen implementieren**: Beginne mit der Zeiterfassung
5. **Benutzeroberfläche entwickeln**: Web-Interface oder CLI

## Installation

### Voraussetzungen
- Python 3.7 oder höher

### Schnellstart
```bash
# Repository klonen
git clone https://github.com/TGN28/WorkTime.git
cd WorkTime

# Direkt verwenden (keine Installation nötig)
python src/worktime.py status
```

## Verwendung

### Grundlegende Befehle

```bash
# Zeiteintrag starten
python src/worktime.py start "Beschreibung der Aufgabe" [Projektname]

# Zeiteintrag stoppen
python src/worktime.py stop

# Aktuellen Status anzeigen
python src/worktime.py status

# Heutige Einträge anzeigen
python src/worktime.py today
```

### Beispiel
```bash
# Arbeit beginnen
python src/worktime.py start "Meeting vorbereiten" "Projekt Alpha"

# Status prüfen
python src/worktime.py status

# Aufgabe beenden
python src/worktime.py stop

# Tagesübersicht
python src/worktime.py today
```

Weitere Beispiele findest du in [examples/USAGE.md](examples/USAGE.md).

## Tests ausführen

```bash
python -m pytest tests/
# oder
python tests/test_worktime.py
```

## Mitwirken

Beiträge sind willkommen! Weitere Informationen folgen.

## Lizenz

MIT License - siehe [LICENSE](LICENSE) Datei für Details
