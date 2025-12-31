"""
Places Discovery Tool
"""

import json

def get_places(city, min_rating=4.0):
    with open("travel_planner_agent/data/places.json", "r") as f:
        places = json.load(f)

    recommended = [
        place for place in places
        if place["city"].lower() == city.lower()
        and place["rating"] >= min_rating
    ]

    return recommended[:5]
