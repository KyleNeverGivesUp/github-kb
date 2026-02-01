# Weather AGNTCY - 极简使用指南

## 🎯 这是什么？

一个**极简的**天气查询多智能体系统，使用**真实的 AGNTCY SDK**。

- **总代码量**: 约 580 行（包含注释和空行）
- **核心文件**: 只有 6 个 Python 文件
- **学习时间**: 30 分钟理解全部代码

## 📦 核心组件

### 1. Weather Agent (Server 端)

**文件**: `agents/weather/`

- `agent.py` (35行): 业务逻辑 - 返回天气信息
- `agent_executor.py` (80行): A2A 请求处理器
- `card.py` (25行): Agent 描述（OASF 格式）
- `weather_server.py` (115行): 启动 A2A Server

### 2. Supervisor Agent (Client 端)

**文件**: `agents/supervisor/`

- `supervisor_agent.py` (120行): A2A Client，调用 Weather Agent

### 3. 配置

**文件**: `config/config.py` (20行)

## 🚀 3 步运行

### 步骤 1: 安装依赖

```bash
pip install agntcy-app-sdk a2a-python python-dotenv uvicorn fastapi
```

### 步骤 2: 启动 Server

```bash
python3 agents/weather/weather_server.py
```

看到这个就成功了：
```
============================================================
Weather Agent Server - AGNTCY SDK
============================================================
Agent ID: weather-agent
Transport: A2A
Starting A2A HTTP Server on localhost:8000
```

### 步骤 3: 启动 Client（新终端）

```bash
python3 agents/supervisor/supervisor_agent.py
```

然后输入：
```
You: What's the weather in Beijing?
```

## 🔑 核心 API 用法

### Server 端（3 步）

```python
# 1. 创建 Factory
factory = AgntcyFactory("weather-agent")

# 2. 创建 A2A Server
server = A2AStarletteApplication(
    agent_card=AGENT_CARD,
    http_handler=DefaultRequestHandler(
        agent_executor=WeatherAgentExecutor()
    )
)

# 3. 启动
await Server(Config(app=server.build())).serve()
```

### Client 端（3 步）

```python
# 1. 创建 Factory
factory = AgntcyFactory("supervisor-agent")

# 2. 创建 A2A Client
transport = factory.create_transport("A2A", endpoint="http://localhost:8000")
client = A2AClient(transport=transport)

# 3. 发送消息
response = await client.send_message(
    topic="weather-agent",
    message="What's the weather in Beijing?"
)
```

## 📖 代码阅读顺序

1. `agents/weather/card.py` - 看 Agent 如何描述自己
2. `agents/weather/agent.py` - 看业务逻辑（最简单）
3. `agents/weather/agent_executor.py` - 看如何处理 A2A 请求
4. `agents/weather/weather_server.py` - 看如何启动 Server
5. `agents/supervisor/supervisor_agent.py` - 看如何调用 Server

**每个文件都很短，很容易理解！**

## 🎓 关键概念

### Agent Card (OASF)

描述 Agent 的能力：

```python
AGENT_CARD = {
    "agent_id": "weather-agent",
    "name": "Weather Agent",
    "capabilities": [
        {
            "name": "get_weather",
            "description": "Get weather for a location"
        }
    ]
}
```

### AgentExecutor

处理 A2A 请求的核心：

```python
class WeatherAgentExecutor(AgentExecutor):
    async def execute(self, context, event_queue):
        # 1. 获取用户消息
        prompt = context.message.parts[0].text

        # 2. 处理业务逻辑
        result = await self.agent.get_weather(location)

        # 3. 返回响应
        await event_queue.put(new_agent_text_message(result))
```

### A2A Client

调用其他 Agent：

```python
client = A2AClient(transport=transport)
response = await client.send_message(
    topic="weather-agent",  # 目标 Agent ID
    message="Your query here"
)
```

## 🔧 常见修改

### 修改返回格式

编辑 `agents/weather/agent.py`:

```python
async def get_weather(self, location: str) -> str:
    return f"🌡️ {location}: {temp}°C, {condition}"
```

### 添加新功能

在 `agents/weather/agent.py` 添加方法：

```python
async def get_forecast(self, location: str) -> str:
    return f"Forecast for {location}: ..."
```

在 `agent_executor.py` 中调用它。

### 切换到 SLIM 传输

创建 `.env`:
```bash
TRANSPORT=slim
TRANSPORT_ENDPOINT=localhost:50051
```

重启 Server 和 Client。

## ❓ 故障排除

**Q: 端口 8000 被占用**
```bash
# 修改 .env
PORT=8001
```

**Q: 找不到模块**
```bash
pip install agntcy-app-sdk a2a-python
```

**Q: Client 连接失败**
- 确保 Server 已启动
- 检查端口是否正确

## 📚 下一步

1. ✅ 运行成功 → 阅读代码
2. ✅ 理解代码 → 修改功能
3. ✅ 修改成功 → 添加新 Agent
4. ✅ 多个 Agent → 学习 CoffeeAGNTCY
5. ✅ 高级功能 → 添加 LangGraph、可观测性

## 🎉 总结

这个项目展示了 AGNTCY SDK 的**最核心用法**：

- ✅ 如何创建 A2A Server
- ✅ 如何创建 A2A Client
- ✅ 如何定义 Agent Card
- ✅ 如何处理请求和响应

**代码简洁、注释清晰、易于理解！**
