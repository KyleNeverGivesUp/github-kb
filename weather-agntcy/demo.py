"""Simple demo script showing the complete workflow."""

import asyncio
from agents.supervisor.supervisor_agent import SupervisorAgent


async def demo():
    """Run a simple demo of the weather agent system."""
    print("\n" + "="*70)
    print("Weather AGNTCY Demo - Simplified Multi-Agent System")
    print("="*70)
    print("\nThis demo shows how AGNTCY components work together:")
    print("  1. Supervisor Agent (A2A Client) receives user query")
    print("  2. LangGraph workflow parses the query")
    print("  3. Supervisor calls Weather Agent (A2A Server) via SLIM")
    print("  4. Weather Agent returns data")
    print("  5. Supervisor formats and displays response")
    print("\n" + "="*70 + "\n")

    supervisor = SupervisorAgent()

    # Demo queries
    queries = [
        "What's the weather in Beijing?",
        "上海今天天气怎么样？",
        "Tell me about the weather in New York"
    ]

    for i, query in enumerate(queries, 1):
        print(f"\n{'='*70}")
        print(f"Demo Query {i}: {query}")
        print('='*70)

        response = await supervisor.query_weather(query)
        print(f"\n{response}\n")

        await asyncio.sleep(1)  # Pause between queries

    print("\n" + "="*70)
    print("Demo completed! You can now run interactive mode:")
    print("  python agents/supervisor/supervisor_agent.py")
    print("="*70 + "\n")


if __name__ == "__main__":
    asyncio.run(demo())
