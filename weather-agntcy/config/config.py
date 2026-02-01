"""简化的配置文件"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """应用配置"""

    # 传输模式: "A2A" (HTTP直连) 或 "slim" (SLIM传输层)
    transport = os.getenv("TRANSPORT", "A2A")

    # A2A HTTP 模式配置
    host = os.getenv("HOST", "localhost")
    port = int(os.getenv("PORT", "8000"))

    # SLIM 传输层配置
    transport_endpoint = os.getenv("TRANSPORT_ENDPOINT", "localhost:50051")


# 全局配置实例
config = Config()
