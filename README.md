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

1. **App ausprobieren**: Siehe [QUICKSTART.md](QUICKSTART.md) für eine 2-Minuten-Anleitung
2. **Weitere Features**: Siehe [NEXT_STEPS.md](NEXT_STEPS.md) für geplante Erweiterungen
3. **Technische Details**: Siehe [ARCHITECTURE.md](ARCHITECTURE.md) für Architektur-Übersicht
4. **Mitwirken**: Siehe [CONTRIBUTING.md](CONTRIBUTING.md) für Contribution-Guidelines

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
