"""Simple test to verify the weather agent works."""

import asyncio
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.weather.agent import WeatherAgent


async def test_weather_agent():
    """Test Weather Agent functionality."""
    print("Testing Weather Agent...")
    print("-" * 60)

    agent = WeatherAgent()

    # Test 1: Beijing weather
    print("\n1. Testing Beijing weather (Celsius):")
    result = await agent.get_weather("Beijing", "celsius")
    print(f"   Location: {result['location']}")
    print(f"   Temperature: {result['temperature']}{result['units']}")
    print(f"   Condition: {result['condition']}")
    print(f"   Description: {result['description']}")

    # Test 2: New York weather
    print("\n2. Testing New York weather (Fahrenheit):")
    result = await agent.get_weather("New York", "fahrenheit")
    print(f"   Location: {result['location']}")
    print(f"   Temperature: {result['temperature']}{result['units']}")
    print(f"   Condition: {result['condition']}")
    print(f"   Description: {result['description']}")

    print("\n" + "-" * 60)
    print("✅ Weather Agent tests passed!")


if __name__ == "__main__":
    asyncio.run(test_weather_agent())
