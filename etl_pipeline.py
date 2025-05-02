import pandas as pd
import re
from pathlib import Path

# Daten einlesen
df1 = pd.read_csv("data/user_data_part1.csv")
df2 = pd.read_csv("data/user_data_part2.csv")

# Zusammenführen beider Dateien über 'userid'
df = pd.merge(df1, df2, on="userid", how="inner")

# Entferne Zeilen mit fehlenden Pflichtdaten
df.dropna(subset=["username", "email", "address", "phone", "country"], inplace=True)

# E-Mail-Bereinigung: einfache Regex für gültige E-Mails
def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", str(email)))

df = df[df["email"].apply(is_valid_email)]

# Telefonnummer-Bereinigung anhand des Landes (vereinfachte Prüfung)
def phone_matches_country(phone, country):
    if country == "DE":
        return phone.startswith("+49")
    elif country == "US":
        return phone.startswith("+1")
    elif country == "FR":
        return phone.startswith("+33")
    return False

df = df[df.apply(lambda row: phone_matches_country(row["phone"], row["country"]), axis=1)]

# Optional: Reset Index nach dem Filtern
df.reset_index(drop=True, inplace=True)

# Speichern der bereinigten Daten
output_path = Path("output/cleaned_user_data.csv")
output_path.parent.mkdir(exist_ok=True)
df.to_csv(output_path, index=False)

print(f"ETL abgeschlossen. Bereinigte Daten gespeichert unter: {output_path}")
