"""Supervisor Agent Card - OASF compliant agent description."""

from typing import Dict, Any


def get_supervisor_agent_card() -> Dict[str, Any]:
    """Get Supervisor Agent card following OASF schema.

    Returns:
        Agent card dictionary with metadata and capabilities.
    """
    return {
        "agent_id": "supervisor-agent",
        "name": "Supervisor Agent",
        "version": "1.0.0",
        "description": "Coordinates weather queries by communicating with Weather Agent",
        "capabilities": [
            {
                "name": "query_weather",
                "description": "Process natural language weather queries",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "Natural language weather query (e.g., 'What's the weather in Beijing?')"
                        }
                    },
                    "required": ["query"]
                }
            }
        ],
        "protocol": "a2a",
        "transport": "slim",
        "dependencies": [
            {
                "agent_id": "weather-agent",
                "capabilities": ["get_weather"]
            }
        ],
        "tags": ["supervisor", "coordinator", "demo"]
    }
