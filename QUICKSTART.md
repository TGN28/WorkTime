# WorkTime - Schnellstart-Anleitung

## Installation in 2 Minuten

### Schritt 1: Repository klonen
```bash
git clone https://github.com/TGN28/WorkTime.git
cd WorkTime
```

### Schritt 2: Python prüfen
```bash
python3 --version
# Sollte Python 3.7 oder höher anzeigen
```

### Schritt 3: Erste Zeiterfassung
```bash
# Arbeit beginnen
python src/worktime.py start "Projekt-Planung" "MeinProjekt"

# Status anzeigen (zeigt laufende Zeit)
python src/worktime.py status

# Arbeit beenden
python src/worktime.py stop

# Tagesübersicht
python src/worktime.py today
```

## Typischer Arbeitstag

```bash
# 09:00 - Arbeitstag beginnen
python src/worktime.py start "E-Mails bearbeiten"

# 09:30 - Aufgabe wechseln (stoppt automatisch vorherige)
python src/worktime.py start "Entwicklung Feature X" "Projekt Alpha"

# 11:00 - Pause
python src/worktime.py stop

# 11:15 - Weiterarbeiten
python src/worktime.py start "Code Review" "Projekt Alpha"

# 12:00 - Mittagspause
python src/worktime.py stop

# 13:00 - Nach der Pause
python src/worktime.py start "Meeting Protokoll" "Projekt Beta"

# 17:00 - Feierabend, Tagesübersicht
python src/worktime.py stop
python src/worktime.py today
```

Ausgabe:
```
Heutige Einträge (4):

  09:00 -     30.0 min : E-Mails bearbeiten
  09:30 -     90.0 min : Entwicklung Feature X [Projekt Alpha]
  11:15 -     45.0 min : Code Review [Projekt Alpha]
  13:00 -    240.0 min : Meeting Protokoll [Projekt Beta]

Gesamt: 405.0 Minuten (6.75 Stunden)
```

## Alle Befehle auf einen Blick

| Befehl | Beschreibung | Beispiel |
|--------|--------------|----------|
| `start` | Zeiterfassung starten | `python src/worktime.py start "Aufgabe" "Projekt"` |
| `stop` | Aktuelle Zeiterfassung stoppen | `python src/worktime.py stop` |
| `status` | Aktuellen Status anzeigen | `python src/worktime.py status` |
| `today` | Heutige Einträge + Gesamtzeit | `python src/worktime.py today` |

## Tipps

1. **Projekt ist optional**: `python src/worktime.py start "Aufgabe"` funktioniert auch ohne Projekt
2. **Auto-Stop**: Wenn du einen neuen Eintrag startest, wird der vorherige automatisch gestoppt
3. **Daten-Speicherort**: Alle Daten werden in `worktime_data.json` gespeichert
4. **Backup**: Kopiere regelmäßig `worktime_data.json` für ein Backup

## Tests ausführen

```bash
python tests/test_worktime.py
```

## Nächste Schritte

- Lies [NEXT_STEPS.md](NEXT_STEPS.md) für geplante Features
- Siehe [ARCHITECTURE.md](ARCHITECTURE.md) für technische Details
- Schau dir [examples/USAGE.md](examples/USAGE.md) für mehr Beispiele an

## Probleme?

- Stelle sicher, dass Python 3.7+ installiert ist
- Bei Windows: Verwende `python` statt `python3`
- Bei Problemen: Erstelle ein Issue auf GitHub

---

**Viel Erfolg! 🎯**
