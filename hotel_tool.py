"""
Hotel Recommendation Tool
"""

import json

def recommend_hotel(city, min_stars=3):
    with open("travel_planner_agent/data/hotels.json", "r") as f:
        hotels = json.load(f)

    filtered = [
        hotel for hotel in hotels
        if hotel["city"].lower() == city.lower()
        and hotel["stars"] >= min_stars
    ]

    if not filtered:
        return None

    return sorted(filtered, key=lambda x: (x["price_per_night"], -x["stars"]))[0]
