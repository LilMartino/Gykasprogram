sport = "Badminton"
capacity = 4

print(sport, capacity)

def create_event(sport, capacity):
    return {"sport": sport, "capacity": capacity}

event = create_event("Badminton", 4)
print(event)

second_event = create_event("Badminton", 8)
print(second_event)