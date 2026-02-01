"""Weather Agent Card - OASF 格式的 Agent 描述"""

from a2a.types import AgentCapabilities, AgentCard, AgentSkill

from config.config import config


AGENT_CARD = AgentCard(
    name="weather-agent",
    version="1.0.0",
    description="Provides weather information for specified locations",
    url=f"http://{config.host}:{config.port}",
    default_input_modes=["text/plain"],
    default_output_modes=["text/plain"],
    capabilities=AgentCapabilities(),
    skills=[
        AgentSkill(
            id="get_weather",
            name="Get Weather",
            description="Get current weather for a location",
            tags=["weather", "demo"],
            examples=["What's the weather in Beijing?"],
        )
    ],
)
