"""
Tests für WorkTime
"""

import unittest
import os
import tempfile
from datetime import datetime, timedelta
from pathlib import Path
import sys

# Füge src zum Path hinzu
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from worktime import TimeEntry, WorkTimeApp


class TestTimeEntry(unittest.TestCase):
    """Tests für TimeEntry Klasse"""
    
    def test_create_entry(self):
        """Test: TimeEntry erstellen"""
        entry = TimeEntry("Arbeiten", "TestProjekt")
        self.assertIsNotNone(entry.id)
        self.assertEqual(entry.description, "Arbeiten")
        self.assertEqual(entry.project, "TestProjekt")
        self.assertTrue(entry.is_running())
    
    def test_stop_entry(self):
        """Test: TimeEntry stoppen"""
        entry = TimeEntry("Arbeiten")
        entry.stop()
        self.assertFalse(entry.is_running())
        self.assertIsNotNone(entry.end_time)
    
    def test_duration(self):
        """Test: Dauer berechnen"""
        start = datetime.now()
        entry = TimeEntry("Arbeiten", start_time=start)
        entry.end_time = start + timedelta(minutes=30)
        duration = entry.duration_minutes()
        self.assertAlmostEqual(duration, 30.0, places=1)
    
    def test_to_dict(self):
        """Test: Serialisierung zu Dictionary"""
        entry = TimeEntry("Arbeiten", "TestProjekt")
        data = entry.to_dict()
        self.assertEqual(data['description'], "Arbeiten")
        self.assertEqual(data['project'], "TestProjekt")
        self.assertIsNotNone(data['start_time'])
    
    def test_from_dict(self):
        """Test: Deserialisierung von Dictionary"""
        data = {
            'id': 'test-id',
            'description': 'Arbeiten',
            'project': 'TestProjekt',
            'start_time': datetime.now().isoformat(),
            'end_time': None,
            'tags': []
        }
        entry = TimeEntry.from_dict(data)
        self.assertEqual(entry.id, 'test-id')
        self.assertEqual(entry.description, 'Arbeiten')


class TestWorkTimeApp(unittest.TestCase):
    """Tests für WorkTimeApp Klasse"""
    
    def setUp(self):
        """Erstellt temporäre Datei für Tests"""
        self.temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json')
        self.temp_file.close()
        self.app = WorkTimeApp(self.temp_file.name)
    
    def tearDown(self):
        """Löscht temporäre Datei"""
        if os.path.exists(self.temp_file.name):
            os.unlink(self.temp_file.name)
    
    def test_start_entry(self):
        """Test: Eintrag starten"""
        entry = self.app.start_entry("Test", "Projekt")
        self.assertEqual(len(self.app.entries), 1)
        self.assertEqual(entry.description, "Test")
        self.assertTrue(entry.is_running())
    
    def test_stop_running_entries(self):
        """Test: Laufende Einträge stoppen"""
        self.app.start_entry("Test1")
        self.app.stop_running_entries()
        self.assertIsNone(self.app.get_running_entry())
    
    def test_get_running_entry(self):
        """Test: Laufenden Eintrag abrufen"""
        entry = self.app.start_entry("Test")
        running = self.app.get_running_entry()
        self.assertIsNotNone(running)
        self.assertEqual(running.id, entry.id)
    
    def test_save_and_load(self):
        """Test: Speichern und Laden"""
        self.app.start_entry("Test", "Projekt")
        self.app.save_data()
        
        # Neue App-Instanz mit gleicher Datei
        app2 = WorkTimeApp(self.temp_file.name)
        self.assertEqual(len(app2.entries), 1)
        self.assertEqual(app2.entries[0].description, "Test")
    
    def test_total_time_today(self):
        """Test: Gesamtzeit heute"""
        entry = self.app.start_entry("Test")
        entry.end_time = entry.start_time + timedelta(minutes=30)
        total = self.app.total_time_today()
        self.assertAlmostEqual(total, 30.0, places=1)


if __name__ == '__main__':
    unittest.main()
