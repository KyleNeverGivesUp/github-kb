"""极简 Weather Agent - 提供天气信息的核心逻辑"""

import logging
import random
from typing import Dict, Any

logger = logging.getLogger(__name__)


class WeatherAgent:
    """Weather Agent - 提供天气信息"""

    def __init__(self):
        logger.info("Weather Agent initialized")

    async def get_weather(self, location: str) -> str:
        """获取天气信息

        Args:
            location: 城市名称

        Returns:
            天气描述文本
        """
        logger.info(f"Getting weather for: {location}")

        # 模拟天气数据
        conditions = ["Sunny", "Cloudy", "Rainy", "Partly Cloudy"]
        temp = random.randint(-5, 35)
        condition = random.choice(conditions)

        result = f"The weather in {location} is {condition.lower()} with a temperature of {temp}°C."
        logger.info(f"Weather result: {result}")

        return result
