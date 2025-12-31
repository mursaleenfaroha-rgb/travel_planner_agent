"""
LangChain Agent Setup
"""

from langchain_openai import ChatOpenAI
from langchain.agents import Tool, initialize_agent

from tools.flight_tool import search_flight
from tools.hotel_tool import recommend_hotel
from tools.places_tool import get_places

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

tools = [
    Tool(
        name="Flight Search",
        func=lambda x: search_flight(*x.split(",")),
        description="Find cheapest flight. Input: source,destination"
    ),
    Tool(
        name="Hotel Recommendation",
        func=recommend_hotel,
        description="Recommend hotel in a city"
    ),
    Tool(
        name="Places Search",
        func=get_places,
        description="Find top attractions in a city"
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)
