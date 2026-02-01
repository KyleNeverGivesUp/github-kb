"""Supervisor Agent - A2A Client 使用 AGNTCY SDK

这是一个极简的 A2A Client 实现，展示如何调用 Weather Agent。
"""

from pathlib import Path
from uuid import uuid4
import sys
import asyncio
import logging
from dotenv import load_dotenv
import httpx

from a2a.client.legacy import A2AClient
from a2a.types import (
    JSONRPCErrorResponse,
    Message,
    MessageSendConfiguration,
    MessageSendParams,
    Part,
    Role,
    SendMessageRequest,
    Task,
    TextPart,
)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.config import config

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

load_dotenv()


class SupervisorAgent:
    """Supervisor Agent - 协调天气查询"""

    def __init__(self):
        """初始化 Supervisor Agent"""
        logger.info("Initializing Supervisor Agent")

        if config.transport != "A2A":
            raise RuntimeError(
                "SupervisorAgent only supports A2A HTTP transport in this demo."
            )

        self.endpoint = f"http://{config.host}:{config.port}"
        self.http_client = httpx.AsyncClient(timeout=30.0)
        self.client = A2AClient(self.http_client, url=self.endpoint)
        logger.info("Supervisor Agent initialized")

    async def query_weather(self, prompt: str) -> str:
        """查询天气

        Args:
            prompt: 用户提示词，如 "What's the weather in Beijing?"

        Returns:
            天气信息
        """
        logger.info(f"User query: {prompt}")
        logger.info("Calling Weather Agent via A2A...")

        try:
            # 调用 Weather Agent
            # 目标 topic 是 Weather Agent 的 agent_id
            message = Message(
                role=Role.user,
                parts=[Part(root=TextPart(text=prompt))],
                message_id=str(uuid4()),
            )
            request = SendMessageRequest(
                id=str(uuid4()),
                params=MessageSendParams(
                    message=message,
                    configuration=MessageSendConfiguration(
                        accepted_output_modes=["text/plain"],
                        blocking=True,
                        history_length=1,
                    ),
                ),
            )

            response = await self.client.send_message(request)

            if isinstance(response.root, JSONRPCErrorResponse):
                error = response.root.error
                logger.error(f"Received error response: {error}")
                return f"Error: {error.message}"

            result = response.root.result
            result_text = self._result_to_text(result)
            logger.info(f"Received response: {result_text}")
            return result_text

        except Exception as e:
            logger.error(f"Error calling Weather Agent: {e}")
            return f"Error: {str(e)}"

    @staticmethod
    def _message_to_text(message: Message) -> str:
        for part in message.parts:
            root = part.root
            if isinstance(root, TextPart):
                return root.text
            if hasattr(root, "text"):
                return str(root.text)
        return ""

    def _result_to_text(self, result: Message | Task) -> str:
        if isinstance(result, Message):
            return self._message_to_text(result)

        if result.status and result.status.message:
            text = self._message_to_text(result.status.message)
            if text:
                return text

        if result.history:
            for message in reversed(result.history):
                text = self._message_to_text(message)
                if text:
                    return text

        return f"Task {result.id} status: {result.status.state.value}"

    async def interactive_mode(self):
        """交互模式"""
        logger.info("\n" + "="*60)
        logger.info("Weather AGNTCY - Supervisor Agent (A2A Client)")
        logger.info("="*60)
        logger.info(f"Transport: {config.transport}")
        logger.info(f"Endpoint: {self.endpoint}")
        logger.info("\nType your weather queries (or 'quit' to exit)")
        logger.info("Examples:")
        logger.info("  - What's the weather in Beijing?")
        logger.info("  - 上海今天天气怎么样？")
        logger.info("="*60 + "\n")

        try:
            while True:
                try:
                    query = input("You: ").strip()

                    if not query:
                        continue

                    if query.lower() in ["quit", "exit", "q"]:
                        logger.info("Goodbye!")
                        break

                    response = await self.query_weather(query)
                    print(f"\nAgent: {response}\n")

                except KeyboardInterrupt:
                    logger.info("\nGoodbye!")
                    break
                except Exception as e:
                    logger.error(f"Error: {e}")
        finally:
            await self.http_client.aclose()


async def main():
    """主入口"""
    supervisor = SupervisorAgent()
    await supervisor.interactive_mode()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("\nShutting down gracefully")
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)
