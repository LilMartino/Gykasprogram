import json
from pathlib import Path

file_path = Path(__file__).with_name("event.json")

with file_path.open("r", encoding="utf-8") as file:
    event = json.load(file)

print("Sport:", event["sport"])
print("Počet míst:", event["capacity"])