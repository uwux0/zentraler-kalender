import requests
from ics import Calendar

# ICS-Feeds mit Kategorien
feeds = {
    "Skisprung": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=JP&categorycode=WC",
    "Freestyle": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=FS&categorycode=WC",
    "Langlauf": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=CC&categorycode=WC",
    "Nordisch": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=NK&categorycode=WC",
    "Ski Alpin": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=AL&categorycode=WC",
    "Snowboard": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=SB&categorycode=WC"
}

merged_calendar = Calendar()

for category, url in feeds.items():
    print(f"Lade {category}...")
    response = requests.get(url)
    if response.status_code == 200:
        cal = Calendar(response.text)
        for event in cal.events:
            event.categories = {category}  # Kategorie hinzufügen
            merged_calendar.events.add(event)
    else:
        print(f"Fehler beim Laden von {category}: {response.status_code}")

# Speichern in docs/zentral.ics
with open("docs/zentral.ics", "w", encoding="utf-8") as f:
    f.writelines(merged_calendar.serialize_iter())
