import json

def search_flight(source, destination):
    with open("travel_planner_agent/data/flights.json", "r") as f:
        flights = json.load(f)

    filtered = [
        f for f in flights
        if f["from"].lower() == source.lower()
        and f["to"].lower() == destination.lower()
    ]

    if not filtered:
        return "No flights found"

    return min(filtered, key=lambda x: x["price"])
