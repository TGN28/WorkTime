# Beispiele für WorkTime

## Basis-Verwendung

### Zeiteintrag starten
```bash
python src/worktime.py start "Meeting vorbereiten"
python src/worktime.py start "Code Review" "WebApp-Projekt"
```

### Zeiteintrag stoppen
```bash
python src/worktime.py stop
```

### Status anzeigen
```bash
python src/worktime.py status
```

### Heutige Einträge anzeigen
```bash
python src/worktime.py today
```

## Beispiel-Workflow

```bash
# Morgen: Arbeit beginnen
$ python src/worktime.py start "E-Mails bearbeiten"
✓ Zeiteintrag gestartet: E-Mails bearbeiten
  Start: 09:00:00

# Nach 30 Minuten: Aufgabe wechseln
$ python src/worktime.py start "Meeting" "Projekt Alpha"
✓ Zeiteintrag gestartet: Meeting
  Projekt: Projekt Alpha
  Start: 09:30:00

# Nach dem Meeting: Status prüfen
$ python src/worktime.py status
⏱  Laufender Eintrag: Meeting
   Projekt: Projekt Alpha
   Gestartet: 09:30:00
   Dauer: 60.0 Minuten

# Pause machen
$ python src/worktime.py stop
✓ Zeiteintrag gestoppt: Meeting
  Dauer: 60.0 Minuten (1.00 Stunden)

# Tagesübersicht anzeigen
$ python src/worktime.py today
Heutige Einträge (2):

  09:00 -     30.0 min : E-Mails bearbeiten
  09:30 -     60.0 min : Meeting [Projekt Alpha]

Gesamt: 90.0 Minuten (1.50 Stunden)
```

## Daten-Verwaltung

Die Zeiteinträge werden in der Datei `worktime_data.json` gespeichert.

### Backup erstellen
```bash
cp worktime_data.json worktime_data_backup_$(date +%Y%m%d).json
```

### Daten löschen (Neustart)
```bash
rm worktime_data.json
```
