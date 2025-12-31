"""
Budget Estimation Tool
"""

def estimate_budget(flight_price, hotel_price, days):
    food_and_local = 800 * days

    return {
        "flight_cost": flight_price,
        "hotel_cost": hotel_price * days,
        "food_and_local": food_and_local,
        "total_cost": flight_price + (hotel_price * days) + food_and_local
    }
