# ETL-Pipeline-Demo

Dieses Projekt zeigt eine einfache, praxisnahe ETL-Pipeline in Python. Ziel ist es, Nutzerdaten aus zwei Rohdatenquellen zusammenzuführen, zu validieren und bereinigt zu exportieren.

## Funktionen

- Einlesen von Benutzerdaten aus zwei CSV-Dateien
- Zusammenführung anhand der `userid`
- Validierung von E-Mail-Adressen
- Prüfung von Telefonnummern auf passende Ländervorwahl (DE, US, FR)
- Entfernen unvollständiger oder fehlerhafter Datensätze
- Export der bereinigten Daten als neue CSV-Datei

## Datenstruktur

- `data/user_data_part1.csv`: enthält `userid`, `username`, `email`, `country`
- `data/user_data_part2.csv`: enthält `userid`, `phone`, `address`

## Setup & Ausführung

```bash
pip install -r requirements.txt
python etl_pipeline.py
