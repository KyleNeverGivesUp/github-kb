# GitHub Knowledge Base

This directory contains a local knowledge base of GitHub projects.

---

## Chat Bots

### [ClaudeBot](/ClaudeBot)
A general-purpose IRC bot powered by GitHub's Hubot, integrating multiple web API functionalities.
**Updated:** 2026-01-27

- **Tech Stack**: Node.js, Hubot, IRC
- **Key Features**:
  - IRC adapter support, deployed on FyreChat network
  - Redis persistence for brain data (in-memory key-value store)
  - Integrates multiple Hubot plugins: Google search/translate/images, YouTube, Wikipedia, Steam, Twitch, etc.
  - Supports custom script extensions (CoffeeScript)
- **Deployment**: Configured for Heroku deployment, supports local execution
- **Repository**: https://github.com/ClaudeBot/ClaudeBot

---

## Docker & Container Learning

### [docker-tutorial](/docker-tutorial)
Docker 基础教程 - 从零开始学习 Docker 和 Dockerfile，包含完整的中文视频教程和实战项目。
**Updated:** 2026-01-28

- **Tech Stack**: Docker, Docker Compose, Django, PostgreSQL
- **Key Features**:
  - 完整的 Docker 基础概念讲解（Image, Container, Registry）
  - Dockerfile 编写教程和最佳实践
  - Docker Compose 多容器应用编排
  - 实战项目：Django + PostgreSQL 完整部署
  - 涵盖 Docker 网络、数据卷、环境变量等核心概念
  - 包含 Portainer GUI 管理工具教程
  - Docker Hub 镜像推送教程
  - 配套中文视频教程（YouTube）
- **学习路径**:
  1. 基础概念和安装
  2. Docker 命令和 Dockerfile 编写
  3. Docker Compose 多容器编排
  4. 实战项目部署
- **Repository**: https://github.com/twtrubiks/docker-tutorial

### [Compose-Examples](/Compose-Examples)
A comprehensive collection of 300+ Docker Compose examples covering various self-hosted FOSS and proprietary projects.
**Updated:** 2026-01-28

- **Tech Stack**: Docker, Docker Compose
- **Key Features**:
  - 300+ ready-to-use Docker Compose examples organized by category
  - Covers wide range of applications: web servers, databases, monitoring, media servers, development tools, etc.
  - Each example includes docker-compose.yml with detailed comments and configuration notes
  - Categories include: Analytics, Automation, Backups, Blogging, Communication, DNS, File Transfer, Identity Management, Monitoring, Password Managers, Proxies, Security, VPN, Wikis, and more
  - Practical examples for learning Docker networking, volumes, environment variables, and multi-container applications
- **Learning Path**: Start with simple examples (nginx, databases) then progress to complex multi-container stacks (monitoring, media servers)
- **Repository**: https://github.com/Haxxnet/Compose-Examples

---

## Internship & Job Search

### [Summer2026-Internships](/Summer2026-Internships)
Comprehensive collection of Summer 2026 tech internships tracked by Pitt CSC & Simplify.
**Updated:** 2026-01-29

- **Coverage**: 1,205+ internship positions across 800+ companies
- **Categories**:
  - Software Engineering: 303 positions
  - Data Science/AI/ML: 652 positions
  - Product Management: 91 positions
  - Quantitative Finance: 8 positions
  - Hardware Engineering: 151 positions
- **Key Features**:
  - Daily updates with new postings
  - Direct application links for each position
  - Company tags (🔥 FAANG+, 🛂 No sponsorship, 🇺🇸 US citizenship required)
  - Age tracking (shows how recently posted)
  - Covers major tech companies (FAANG), finance (JP Morgan, Citadel), and startups
- **Usage**: Check daily for new "0d" (today) postings, use Simplify extension for auto-fill
- **Repository**: https://github.com/SimplifyJobs/Summer2026-Internships

### [New-Grad-Positions-2027](/New-Grad-Positions-2027)
Full-time entry-level positions for 2026/2027 new graduates in SWE, Quant, and PM roles.
**Updated:** 2026-01-29

- **Coverage**: 361+ full-time positions
- **Categories**:
  - Software Engineering: 246 positions
  - Data Science/AI/ML: 53 positions
  - Product Management: 11 positions
  - Quantitative Finance: 11 positions
  - Hardware Engineering: 40 positions
- **Key Features**:
  - Daily updates maintained by Coder Quad and Simplify
  - Direct application links
  - Same tagging system as internship repo
  - Email alerts available via SWEList.com
- **Usage**: For 2027 Spring graduates seeking full-time roles
- **Repository**: https://github.com/SimplifyJobs/New-Grad-Positions

### [job-scraper](/job-scraper)
Python tool to scrape SWE new grad and internship postings from LinkedIn, GitHub, and Simplify.jobs.
**Updated:** 2026-01-29

- **Tech Stack**: Python, Selenium, BeautifulSoup, Discord webhooks, SMTP
- **Key Features**:
  - Board Scraper: Monitors LinkedIn, GitHub (SimplifyJobs), Simplify.jobs every 2 hours
  - Company Scraper: Monitors 10+ company career pages every 30 seconds
  - Discord notifications for new board postings
  - Email alerts for new company postings
  - Duplicate detection with JSON tracking
  - Targets Canada, US, and remote roles
- **Setup**: Requires Discord webhook and Gmail app password
- **Repository**: https://github.com/rabiuk/job-scraper

### [SimplifyJobsDaemon](/SimplifyJobsDaemon)
Go daemon that monitors SimplifyJobs repos, scrapes job descriptions, analyzes with local LLM, and auto-generates tailored resumes.
**Updated:** 2026-01-29

- **Tech Stack**: Go, Local LLM integration
- **Key Features**:
  - Monitors SimplifyJobs GitHub repos for updates
  - Scrapes full job descriptions from posting URLs
  - Analyzes requirements using local LLM (GPT-OSS)
  - Auto-generates customized resumes per job
  - Desktop notifications (swaync for Linux)
  - Caching to avoid re-processing
  - Sponsorship checker
  - Separates internships and full-time opportunities
- **Setup**: Requires Go installation and local LLM setup
- **Repository**: https://github.com/Matrix030/SimplifyJobsDaemon

---

## AI Agent Infrastructure

### [agntcy-docs](/agntcy-docs)
Official documentation for AGNTCY - the open-source Internet of Agents (IoA) infrastructure project under Linux Foundation.
**Updated:** 2026-01-31

- **Tech Stack**: Material for MkDocs, Python, Go
- **Project Origin**: Started by Outshift by Cisco in March 2025, donated to Linux Foundation in July 2025 with 75+ companies
- **Core Mission**: Build open, interoperable infrastructure enabling AI agents to discover, compose, deploy, and evaluate multi-agent systems at scale
- **Key Capabilities**:
  1. **DISCOVER**: Find and evaluate agents for specific tasks
  2. **COMPOSE**: Connect agents into workflows across any framework/vendor
  3. **DEPLOY**: Run multi-agent systems securely at scale
  4. **EVALUATE**: Monitor performance and improve over time
- **Core Components**:
  - **OASF (Open Agent Schema Framework)**: OCI-based extensible data model for describing agents (A2A, MCP servers, etc.)
  - **Agent Directory**: Discover and announce agents/multi-agent apps, forming IoA inventory
  - **SLIM (Secure Low-latency Interactive Messaging)**: Protocol for secure agent-to-agent communication with MLS/quantum-safe encryption, extends gRPC for pub/sub
  - **Identity**: Decentralized identity management for agents and tools with verifiable credentials
  - **Observability & Evaluation**: Telemetry and monitoring for multi-agent applications
  - **Security**: Trust and protection tools for multi-agent systems
- **Reference Implementation**: CoffeeAGNTCY demonstrates core components in action
- **Formative Members**: Cisco, Dell Technologies, Google Cloud, Oracle, Red Hat
- **Repository**: https://github.com/agntcy/docs

### [agntcy-identity](/agntcy-identity)
AGNTCY Identity system for onboarding, creating, and verifying identities for Agents, MCP Servers, and Multi-Agent Systems.
**Updated:** 2026-01-31

- **Tech Stack**: Decentralized identity technologies, Verifiable Credentials
- **Key Features**:
  - Decentralized identity management for AI agents and tools
  - Verifiable credentials issuance and verification
  - Secure and trustworthy agent interactions
  - Integration with AGNTCY ecosystem components
  - Support for MCP server identity verification
  - Policy-based access control
- **Use Cases**: Agent authentication, MCP server verification, multi-agent system trust establishment
- **Repository**: https://github.com/agntcy/identity

### [coffeeAgntcy](/coffeeAgntcy)
Official AGNTCY reference implementation demonstrating multi-agent system patterns through a coffee company scenario.
**Updated:** 2026-01-31

- **Tech Stack**: AGNTCY App SDK, SLIM, NATS, A2A, MCP, LangGraph, Observe SDK, Identity Service
- **Demo Applications**:
  - **Corto**: Simple 2-agent demo (Supervisor + Q Grader) with A2A over SLIM
  - **Lungo**: Advanced multi-agent system with two setups:
    - Pub/Sub pattern: Auction supervisor + multiple farm agents + MCP servers
    - Group Communication: Logistics workflow with shipper, accountant, helpdesk agents
- **Key Features**:
  - Request-reply, unicast, pub/sub, and group communication patterns
  - Streaming responses support
  - MCP integration (Weather, Payment servers)
  - Identity Service with TBAC (Tool-Based Access Control)
  - Observability via Observe SDK
  - Transport-agnostic design (SLIM/NATS switchable)
- **Learning Path**: Start with Corto for basics, then explore Lungo for advanced patterns
- **Repository**: https://github.com/agntcy/coffeeAgntcy

### [weather-agntcy](/weather-agntcy)
极简天气查询多智能体系统，使用真实 AGNTCY SDK 实现，专注于展示核心 API 用法。
**Updated:** 2026-01-31

- **Tech Stack**: AGNTCY App SDK, A2A Protocol, Python asyncio
- **代码量**: 约 580 行（含注释），6 个核心文件
- **Architecture**: 2-agent system with real A2A communication
  - Weather Agent: A2A Server (agent.py 35行 + agent_executor.py 80行 + weather_server.py 115行)
  - Supervisor Agent: A2A Client (supervisor_agent.py 120行)
- **Key Features**:
  - 真实的 AGNTCY SDK 集成（AgntcyFactory, A2AClient, A2AStarletteApplication）
  - OASF 标准的 Agent Card
  - 支持两种传输模式：A2A HTTP（测试）和 SLIM（生产）
  - 完整的 AgentExecutor 实现
  - 详细的代码注释和日志
- **学习价值**:
  - 最简单的 AGNTCY SDK 使用示例
  - 每个文件都很短，易于理解
  - 展示 Server 和 Client 的完整实现
  - 比 CoffeeAGNTCY 简单 3 倍（400行 vs 1500行）
- **Usage**:
  - Server: `python3 agents/weather/weather_server.py`
  - Client: `python3 agents/supervisor/supervisor_agent.py`
- **文档**: README.md（完整说明）+ QUICKSTART.md（快速上手）
- **Repository**: Local project at /Users/kyle/Projects/github-kb/weather-agntcy

---

# GitHub Knowledge Rules

When the user asks about GitHub repositories, issues, or pull requests:

- Prefer using `gh` CLI instead of guessing
- Use `gh search repos` to find projects
- Use `gh search issues` to find issues
- Use `gh search prs` to find pull requests
- Summarize results clearly after running commands

Do not hallucinate GitHub data.
