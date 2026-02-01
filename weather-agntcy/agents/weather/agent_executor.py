"""Weather Agent Executor - 处理 A2A 请求"""

import logging
from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.types import JSONRPCResponse, ContentTypeNotSupportedError
from a2a.utils import new_agent_text_message

from agents.weather.agent import WeatherAgent

logger = logging.getLogger(__name__)


class WeatherAgentExecutor(AgentExecutor):
    """处理 Weather Agent 的 A2A 请求"""

    def __init__(self):
        self.agent = WeatherAgent()

    def _validate_request(self, context: RequestContext) -> JSONRPCResponse | None:
        """验证请求"""
        if not context or not context.message or not context.message.parts:
            logger.error("Invalid request")
            return JSONRPCResponse(error=ContentTypeNotSupportedError())
        first_part = context.message.parts[0]
        if not hasattr(first_part, "root") or not getattr(first_part.root, "text", None):
            logger.error("Unsupported message part")
            return JSONRPCResponse(error=ContentTypeNotSupportedError())
        return None

    async def execute(self, context: RequestContext, event_queue: EventQueue) -> None:
        """执行请求

        Args:
            context: 请求上下文，包含用户消息
            event_queue: 事件队列，用于发送响应
        """
        logger.info(f"Received request: {context.message}")

        # 验证请求
        validation_error = self._validate_request(context)
        if validation_error:
            await event_queue.enqueue_event(validation_error)
            return

        # 提取用户提示词
        user_prompt = context.message.parts[0].root.text
        logger.info(f"User prompt: {user_prompt}")

        try:
            # 简单提取城市名（实际应用中可以用 LLM）
            location = self._extract_location(user_prompt)

            # 调用 Weather Agent
            result = await self.agent.get_weather(location)

            # 发送响应
            response_message = new_agent_text_message(result)
            await event_queue.enqueue_event(response_message)
            logger.info("Response sent successfully")

        except Exception as e:
            logger.error(f"Error: {e}")
            error_message = new_agent_text_message(f"Error: {str(e)}")
            await event_queue.enqueue_event(error_message)

    async def cancel(self, context: RequestContext, event_queue: EventQueue) -> None:
        """取消请求（当前不支持）"""
        logger.info("Cancellation requested; no-op for WeatherAgentExecutor")
        await event_queue.enqueue_event(new_agent_text_message("Request cancelled."))

    def _extract_location(self, prompt: str) -> str:
        """从提示词中提取城市名"""
        prompt_lower = prompt.lower()

        cities = {
            "beijing": "Beijing", "北京": "Beijing",
            "shanghai": "Shanghai", "上海": "Shanghai",
            "new york": "New York", "纽约": "New York",
            "london": "London", "伦敦": "London",
        }

        for key, value in cities.items():
            if key in prompt_lower:
                return value

        return "Beijing"  # 默认
