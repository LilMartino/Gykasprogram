import json
from pathlib import Path
def create_event(sport, capacity):
    return {"sport": sport, "capacity": capacity}


sport = input("Jaký sport? ")

while True:
    try:
        capacity = int(input("Kolik míst? "))
        if capacity > 0:
            break
        print("Počet míst musí být větší než nula.")
    except ValueError:
        print("Zadej celé číslo, například 4.")

event = create_event(sport, capacity)
print("Vytvořená událost:", event)

file_path = Path(__file__).with_name("event.json")

with file_path.open("w", encoding="utf-8") as file:
    json.dump(event, file, ensure_ascii=False, indent=2)

print("Událost je uložená.")