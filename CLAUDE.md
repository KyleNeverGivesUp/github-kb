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

# GitHub Knowledge Rules

When the user asks about GitHub repositories, issues, or pull requests:

- Prefer using `gh` CLI instead of guessing
- Use `gh search repos` to find projects
- Use `gh search issues` to find issues
- Use `gh search prs` to find pull requests
- Summarize results clearly after running commands

Do not hallucinate GitHub data.
