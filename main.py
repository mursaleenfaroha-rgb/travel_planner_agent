"""
Main Entry Point - Travel Planner
"""

from tools.flight_tool import search_flight
from tools.hotel_tool import recommend_hotel
from tools.places_tool import get_places
from tools.budget_tool import estimate_budget

def main():
    source = input("Enter source city: ")
    destination = input("Enter destination city: ")
    days = int(input("Number of days: "))

    flight = search_flight(source, destination)
    hotel = recommend_hotel(destination)
    places = get_places(destination)
    budget = estimate_budget(flight["price"], hotel["price_per_night"], days)

    print("\n✈️ Flight Selected:", flight)
    print("\n🏨 Hotel Recommended:", hotel)
    print("\n📍 Places to Visit:")
    for p in places:
        print("-", p["name"])

    print("\n💰 Budget Breakdown:")
    for k, v in budget.items():
        print(f"{k}: ₹{v}")

if __name__ == "__main__":
    main()
