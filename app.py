import streamlit as st

from travel_planner_agent.tools.flight_tool import search_flight
from travel_planner_agent.tools.hotel_tool import recommend_hotel
from travel_planner_agent.tools.places_tool import get_places
from travel_planner_agent.tools.budget_tool import estimate_budget


st.set_page_config(page_title="AI Travel Planner", layout="centered")

st.title("✈️ Agentic AI Travel Planner")
st.write("Plan your trip intelligently using AI tools")

# User Inputs
source = st.text_input("From City")
destination = st.text_input("To City")
days = st.number_input("Number of Days", min_value=1, max_value=10, value=3)

if st.button("Generate Travel Plan"):
    if not source or not destination:
        st.error("Please enter both source and destination")
    else:
        flight = search_flight(source, destination)
        hotel = recommend_hotel(destination)
        places = get_places(destination)
        budget = estimate_budget(flight["price"], hotel["price_per_night"], days)

        st.subheader("✈️ Flight Selected")
        st.json(flight)

        st.subheader("🏨 Hotel Recommended")
        st.json(hotel)

        st.subheader("📍 Places to Visit")
        for p in places:
            st.write(f"- {p['name']} (⭐ {p['rating']})")

        st.subheader("💰 Budget Breakdown")
        st.json(budget)
