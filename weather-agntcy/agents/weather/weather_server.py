"""Weather Agent Server - A2A Server 使用 AGNTCY SDK

这是一个极简的 A2A Server 实现，展示如何使用 AGNTCY SDK。
"""

from pathlib import Path
import sys
import asyncio
import logging
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from uvicorn import Config, Server

from agntcy_app_sdk.factory import AgntcyFactory
from agntcy_app_sdk.app_sessions import AppContainer
from agntcy_app_sdk.semantic.a2a.protocol import A2AProtocol

from agents.weather.card import AGENT_CARD
from agents.weather.agent_executor import WeatherAgentExecutor
from config.config import config

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()

# 初始化 AGNTCY Factory
factory = AgntcyFactory("weather-agent", enable_tracing=False)


async def main():
    """启动 Weather Agent Server

    支持两种模式：
    1. A2A 模式：直接通过 HTTP 暴露服务（用于测试）
    2. SLIM 模式：通过 SLIM 传输层暴露服务（生产环境）
    """

    logger.info("="*60)
    logger.info("Weather Agent Server - AGNTCY SDK")
    logger.info("="*60)
    logger.info(f"Agent Name: {AGENT_CARD.name}")
    logger.info(f"Agent Version: {AGENT_CARD.version}")
    logger.info(f"Transport: {config.transport}")
    logger.info("="*60)

    # 创建 Request Handler
    request_handler = DefaultRequestHandler(
        agent_executor=WeatherAgentExecutor(),
        task_store=InMemoryTaskStore(),
    )

    # 创建 A2A Server Application
    server = A2AStarletteApplication(
        agent_card=AGENT_CARD,
        http_handler=request_handler
    )

    if config.transport == "A2A":
        # 模式 1: 直接通过 HTTP 暴露（用于测试）
        logger.info(f"Starting A2A HTTP Server on {config.host}:{config.port}")
        logger.info("Use this for testing without SLIM")

        uvicorn_config = Config(
            app=server.build(),
            host=config.host,
            port=config.port,
            loop="asyncio"
        )
        userver = Server(uvicorn_config)
        await userver.serve()

    else:
        # 模式 2: 通过 SLIM 传输层暴露（生产环境）
        logger.info(f"Starting with {config.transport} transport")
        logger.info(f"Connecting to: {config.transport_endpoint}")

        # 创建传输层
        transport = factory.create_transport(
            config.transport,
            endpoint=config.transport_endpoint,
            name=f"default/default/{A2AProtocol.create_agent_topic(AGENT_CARD)}"
        )

        # 创建应用会话
        app_session = factory.create_app_session()

        # 添加 Weather Agent 容器
        app_session.add_app_container(
            "weather-agent",
            AppContainer(
                server,
                transport=transport,
                topic=A2AProtocol.create_agent_topic(AGENT_CARD),
            )
        )

        logger.info("Weather Agent is ready to receive requests")
        logger.info("Press Ctrl+C to stop")

        # 启动会话（保持运行）
        await app_session.start_session("weather-agent", keep_alive=True)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("\nShutting down gracefully")
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
