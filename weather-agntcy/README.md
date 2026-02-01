# Weather AGNTCY - 使用真实 AGNTCY SDK

一个极简的天气查询多智能体系统，使用真实的 AGNTCY SDK 实现。

## 🎯 核心特点

- ✅ **真实 AGNTCY SDK**: 使用 `agntcy-app-sdk` 和 `a2a-python`
- ✅ **极简实现**: 只保留核心功能，代码清晰易懂
- ✅ **两种模式**: 支持 A2A HTTP 直连和 SLIM 传输层
- ✅ **完整的 A2A 协议**: Server 和 Client 实现

## 📦 架构

```
Supervisor Agent (A2A Client)
         ↓
    [AGNTCY SDK]
         ↓
   Transport Layer (A2A HTTP 或 SLIM)
         ↓
    [AGNTCY SDK]
         ↓
Weather Agent (A2A Server)
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

依赖包括：
- `agntcy-app-sdk`: AGNTCY 核心 SDK
- `a2a-python`: A2A 协议实现
- `uvicorn`, `fastapi`: Web 服务器

### 2. 配置环境

```bash
cp .env.example .env
```

默认使用 A2A HTTP 模式（无需额外配置）：
```bash
TRANSPORT=A2A
HOST=localhost
PORT=8000
```

### 3. 启动 Weather Agent (Server)

```bash
python3 agents/weather/weather_server.py
```

你会看到：
```
============================================================
Weather Agent Server - AGNTCY SDK
============================================================
Agent ID: weather-agent
Agent Name: Weather Agent
Transport: A2A
============================================================
Starting A2A HTTP Server on localhost:8000
```

### 4. 启动 Supervisor Agent (Client)

在另一个终端：

```bash
python3 agents/supervisor/supervisor_agent.py
```

然后输入查询：
```
You: What's the weather in Beijing?
Agent: The weather in Beijing is sunny with a temperature of 15°C.

You: 上海今天天气怎么样？
Agent: The weather in Shanghai is cloudy with a temperature of 20°C.
```

## 📁 项目结构（极简版）

```
weather-agntcy/
├── agents/
│   ├── weather/                    # Weather Agent (Server)
│   │   ├── agent.py               # 核心逻辑（30行）
│   │   ├── agent_executor.py      # A2A 请求处理（80行）
│   │   ├── card.py                # Agent Card（25行）
│   │   └── weather_server.py      # Server 启动（115行）
│   └── supervisor/                 # Supervisor Agent (Client)
│       └── supervisor_agent.py    # Client 实现（120行）
├── config/
│   └── config.py                  # 配置（20行）
├── requirements.txt               # 依赖
└── README.md
```

**总代码量：约 400 行**（包含注释）

## 🔑 核心代码解析

### Weather Agent Server (agents/weather/weather_server.py)

```python
# 1. 创建 AGNTCY Factory
factory = AgntcyFactory("weather-agent", enable_tracing=False)

# 2. 创建 Request Handler
request_handler = DefaultRequestHandler(
    agent_executor=WeatherAgentExecutor(),  # 你的业务逻辑
    task_store=InMemoryTaskStore(),
)

# 3. 创建 A2A Server
server = A2AStarletteApplication(
    agent_card=AGENT_CARD,  # Agent 描述
    http_handler=request_handler
)

# 4. 启动服务（A2A HTTP 模式）
uvicorn_config = Config(app=server.build(), host="localhost", port=8000)
userver = Server(uvicorn_config)
await userver.serve()
```

### Agent Executor (agents/weather/agent_executor.py)

```python
class WeatherAgentExecutor(AgentExecutor):
    """处理 A2A 请求"""

    async def execute(self, context: RequestContext, event_queue: EventQueue):
        # 1. 提取用户消息
        user_prompt = context.message.parts[0].text

        # 2. 调用业务逻辑
        result = await self.agent.get_weather(location)

        # 3. 发送响应
        response_message = new_agent_text_message(result)
        await event_queue.put(response_message)
```

### Supervisor Agent Client (agents/supervisor/supervisor_agent.py)

```python
# 1. 创建传输层
transport = factory.create_transport(
    "A2A",
    endpoint="http://localhost:8000"
)

# 2. 创建 A2A Client
client = A2AClient(transport=transport)

# 3. 发送消息
response = await client.send_message(
    topic="weather-agent",  # 目标 Agent
    message="What's the weather in Beijing?"
)
```

## 🔄 两种传输模式

### 模式 1: A2A HTTP（默认，用于测试）

```bash
# .env
TRANSPORT=A2A
HOST=localhost
PORT=8000
```

- ✅ 无需额外服务
- ✅ 直接 HTTP 通信
- ✅ 适合开发和测试

### 模式 2: SLIM 传输层（生产环境）

```bash
# .env
TRANSPORT=slim
TRANSPORT_ENDPOINT=localhost:50051
```

- ✅ 安全加密通信
- ✅ 支持 Pub/Sub
- ✅ 适合生产环境
- ⚠️ 需要运行 SLIM 服务

## 📚 与 CoffeeAGNTCY 对比

| 特性 | Weather AGNTCY | CoffeeAGNTCY Corto |
|------|----------------|---------------------|
| 代码量 | ~400 行 | ~1500 行 |
| Agent 数量 | 2 个 | 2 个 |
| LangGraph | ❌ | ✅ |
| 可观测性 | ❌ | ✅ |
| LLM 集成 | ❌ | ✅ |
| 核心功能 | ✅ | ✅ |

**Weather AGNTCY 专注于展示 AGNTCY SDK 的核心用法，去除了所有非必要功能。**

## 🎓 学习路径

1. **理解架构**: 阅读本 README
2. **查看 Agent Card**: `agents/weather/card.py` (25行)
3. **查看业务逻辑**: `agents/weather/agent.py` (35行)
4. **查看 Server**: `agents/weather/weather_server.py` (115行)
5. **查看 Client**: `agents/supervisor/supervisor_agent.py` (120行)
6. **运行测试**: 启动 Server 和 Client
7. **修改代码**: 尝试添加新功能

## 🔧 扩展建议

### 添加真实天气 API

修改 `agents/weather/agent.py`:

```python
import httpx

async def get_weather(self, location: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={"q": location, "appid": "YOUR_API_KEY"}
        )
        data = response.json()
        return f"Temperature: {data['main']['temp']}°C"
```

### 使用 SLIM 传输层

1. 启动 SLIM 服务（参考 AGNTCY 文档）
2. 修改 `.env`:
   ```bash
   TRANSPORT=slim
   TRANSPORT_ENDPOINT=localhost:50051
   ```
3. 重启 Server 和 Client

### 添加更多 Agent

参考 Weather Agent 的结构：
1. 创建 `agents/new_agent/`
2. 实现 `agent.py`, `agent_executor.py`, `card.py`, `server.py`
3. 在 Supervisor 中调用

## 📖 参考资源

- [AGNTCY 文档](https://github.com/agntcy/docs)
- [AGNTCY App SDK](https://github.com/agntcy/app-sdk)
- [A2A Protocol](https://github.com/a2aproject/a2a-python)
- [CoffeeAGNTCY](https://github.com/agntcy/coffeeAgntcy)

## ❓ 常见问题

**Q: 为什么不用 LangGraph？**
A: 为了保持极简，专注于 AGNTCY SDK 的使用。你可以轻松添加 LangGraph。

**Q: 如何调试？**
A: 查看日志输出，所有关键步骤都有日志记录。

**Q: 可以用于生产吗？**
A: 这是教学示例。生产环境需要添加错误处理、监控、安全等功能。

**Q: 如何添加身份验证？**
A: 参考 CoffeeAGNTCY Lungo 的 Identity Service 集成。
