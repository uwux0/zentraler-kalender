import requests

feeds = {
    "Skisprung": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=JP&categorycode=WC",
    "Freestyle": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=FS&categorycode=WC",
    "Langlauf": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=CC&categorycode=WC",
    "Nordisch": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=NK&categorycode=WC",
    "Ski Alpin": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=AL&categorycode=WC",
    "Snowboard": "https://data.fis-ski.com/services/public/icalendar-feed-fis-events.html?seasoncode=2026&sectorcode=SB&categorycode=WC"
}

merged = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//FIS Combined Calendar//EN"]

for category, url in feeds.items():
    print(f"Lade {category}...")
    r = requests.get(url)
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            if line.startswith("BEGIN:VEVENT"):
                merged.append(line)
            elif line.startswith("END:VEVENT"):
                merged.append("CATEGORIES:" + category)
                merged.append(line)
            elif not line.startswith("BEGIN:VCALENDAR") and not line.startswith("END:VCALENDAR"):
                merged.append(line)
    else:
        print(f"Fehler bei {category}: {r.status_code}")

merged.append("END:VCALENDAR")

with open("docs/zentral.ics", "w", encoding="utf-8") as f:
    f.write("\n".join(merged))
