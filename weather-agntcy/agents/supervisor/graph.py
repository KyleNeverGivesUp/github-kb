"""Simplified Supervisor Agent Graph - without LangChain dependencies.

This is a simplified version that demonstrates the workflow concept
without requiring LangChain/LangGraph installation.
"""

from typing import Dict, Any
from config.logging_config import setup_logging

logger = setup_logging(__name__)


class SupervisorGraph:
    """Simplified workflow for Supervisor Agent."""

    def __init__(self, weather_client):
        """Initialize Supervisor Graph.

        Args:
            weather_client: Client to communicate with Weather Agent.
        """
        self.weather_client = weather_client
        logger.info("Supervisor Graph initialized (simplified mode)")

    async def run(self, query: str) -> str:
        """Run the workflow with a query.

        This simulates a LangGraph workflow with three steps:
        1. Parse query to extract location
        2. Call Weather Agent via A2A
        3. Format response

        Args:
            query: User weather query.

        Returns:
            Formatted response string.
        """
        logger.info(f"[Step 1/3] Parsing query: {query}")

        # Step 1: Parse query
        location = self._extract_location(query)
        units = "celsius" if "celsius" in query.lower() or "摄氏" in query else "celsius"
        logger.info(f"  → Extracted location: {location}, units: {units}")

        # Step 2: Call Weather Agent
        logger.info(f"[Step 2/3] Calling Weather Agent via A2A")
        logger.info(f"  → A2A Request: agent_id='weather-agent', tool='get_weather'")
        logger.info(f"  → Parameters: location='{location}', units='{units}'")

        weather_data = await self.weather_client.get_weather(location, units)

        logger.info(f"  → A2A Response received: success={weather_data.get('success')}")

        # Step 3: Format response
        logger.info(f"[Step 3/3] Formatting response")

        if weather_data.get("success"):
            data = weather_data["data"]
            response = (
                f"📍 {data['location']}\n"
                f"🌡️  Temperature: {data['temperature']}{data['units']}\n"
                f"☁️  Condition: {data['condition']}\n"
                f"💧 Humidity: {data['humidity']}%\n"
                f"💨 Wind Speed: {data['wind_speed']} km/h\n\n"
                f"{data['description']}"
            )
        else:
            response = f"❌ Error: {weather_data.get('error', 'Unknown error')}"

        logger.info(f"  → Response formatted successfully")
        return response

    def _extract_location(self, query: str) -> str:
        """Extract location from query.

        Args:
            query: User query string.

        Returns:
            Extracted location.
        """
        query_lower = query.lower()

        # Common city names
        cities = [
            ("beijing", "北京", "Beijing"),
            ("shanghai", "上海", "Shanghai"),
            ("guangzhou", "广州", "Guangzhou"),
            ("shenzhen", "深圳", "Shenzhen"),
            ("new york", "纽约", "New York"),
            ("london", "伦敦", "London"),
            ("tokyo", "东京", "Tokyo"),
            ("paris", "巴黎", "Paris"),
            ("singapore", "新加坡", "Singapore"),
        ]

        for city_tuple in cities:
            for city_variant in city_tuple[:-1]:
                if city_variant in query_lower:
                    return city_tuple[-1]

        # Default fallback
        return "Beijing"
