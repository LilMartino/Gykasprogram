import json
from pathlib import Path
def create_event(sport, capacity):
    return {"sport": sport, "capacity": capacity}


sport = input("Jaký sport? ")
capacity = int(input("Kolik míst? "))

event = create_event(sport, capacity)
print("Vytvořená událost:", event)

file_path = Path(__file__).with_name("event.json")

with file_path.open("w", encoding="utf-8") as file:
    json.dump(event, file, ensure_ascii=False, indent=2)

print("Událost je uložená.")