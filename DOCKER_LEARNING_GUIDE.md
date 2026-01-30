# Docker & Docker Compose 学习指南

## 📚 已下载的学习资源

### 1. docker-tutorial (中文教程)
**位置**: `/Users/kyle/Projects/github-kb/docker-tutorial`
**特点**: 完整的中文教程，包含视频讲解和实战项目

### 2. Compose-Examples (实战示例)
**位置**: `/Users/kyle/Projects/github-kb/Compose-Examples`
**特点**: 300+ 个真实项目的 Docker Compose 配置示例

---

## 🎯 学习路径（推荐顺序）

### 第一阶段：Docker 基础概念 (1-2天)

#### 1. 理解核心概念
阅读 `docker-tutorial/README.md` 的以下章节：
- 什么是 Docker
- 为什么要使用 Docker
- Docker 概念：Image、Container、Registry

**关键理解**:
- **Image (镜像)**: 只读的模板，类似于虚拟机的快照
- **Container (容器)**: 从镜像创建的运行实例，可读写
- **Registry (仓库)**: 存储镜像的地方，如 Docker Hub

#### 2. 安装 Docker
根据你的操作系统，参考 `docker-tutorial/README.md` 的安装章节

验证安装:
```bash
docker --version
docker-compose --version
```

---

### 第二阶段：Docker 基本命令 (2-3天)

#### 1. 镜像操作
```bash
# 搜索镜像
docker search nginx

# 拉取镜像
docker pull nginx

# 查看本地镜像
docker images

# 删除镜像
docker rmi <image-id>
```

#### 2. 容器操作
```bash
# 运行容器
docker run -d -p 8080:80 --name my-nginx nginx

# 查看运行中的容器
docker ps

# 查看所有容器（包括停止的）
docker ps -a

# 停止容器
docker stop my-nginx

# 启动容器
docker start my-nginx

# 删除容器
docker rm my-nginx

# 进入容器
docker exec -it my-nginx /bin/bash

# 查看容器日志
docker logs my-nginx
```

#### 3. 实践练习
在 `Compose-Examples/examples` 中尝试简单的单容器示例：
- `nginx-php/` - Web 服务器
- `portainer/` - Docker 管理界面

---

### 第三阶段：Dockerfile 编写 (3-4天)

#### 1. Dockerfile 基础语法

**常用指令**:
```dockerfile
# 基础镜像
FROM ubuntu:20.04

# 维护者信息
LABEL maintainer="your-email@example.com"

# 设置工作目录
WORKDIR /app

# 复制文件
COPY . /app

# 安装依赖
RUN apt-get update && apt-get install -y python3

# 设置环境变量
ENV APP_ENV=production

# 暴露端口
EXPOSE 8000

# 容器启动命令
CMD ["python3", "app.py"]
```

#### 2. Dockerfile 最佳实践

**优化技巧**:
- 使用 `.dockerignore` 排除不需要的文件
- 合并 RUN 命令减少层数
- 使用多阶段构建减小镜像大小
- 使用特定版本的基础镜像（避免用 `latest`）
- 清理缓存和临时文件

**示例 - 多阶段构建**:
```dockerfile
# 构建阶段
FROM node:16 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 运行阶段
FROM node:16-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
CMD ["node", "dist/index.js"]
```

#### 3. 实践项目
参考 `docker-tutorial/api/` 目录：
- 查看 Dockerfile 示例
- 尝试构建自己的镜像
- 理解 entrypoint 和 cmd 的区别

**构建和运行**:
```bash
# 构建镜像
docker build -t my-app:v1.0 .

# 运行容器
docker run -d -p 8000:8000 my-app:v1.0
```

---

### 第四阶段：Docker Compose (4-5天)

#### 1. Docker Compose 基础

**为什么需要 Docker Compose?**
- 管理多容器应用
- 定义服务之间的依赖关系
- 一键启动/停止整个应用栈
- 统一管理网络和数据卷

#### 2. docker-compose.yml 语法

**基本结构**:
```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
    networks:
      - frontend
    depends_on:
      - api

  api:
    build: ./api
    environment:
      - DATABASE_URL=postgresql://db:5432/mydb
    networks:
      - frontend
      - backend
    depends_on:
      - db

  db:
    image: postgres:14
    environment:
      POSTGRES_PASSWORD: secret
      POSTGRES_DB: mydb
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend

networks:
  frontend:
  backend:

volumes:
  db-data:
```

#### 3. 常用命令
```bash
# 启动所有服务
docker-compose up -d

# 查看服务状态
docker-compose ps

# 查看日志
docker-compose logs -f

# 停止所有服务
docker-compose stop

# 停止并删除容器、网络
docker-compose down

# 停止并删除容器、网络、数据卷
docker-compose down -v

# 重启服务
docker-compose restart

# 构建或重新构建服务
docker-compose build

# 执行命令
docker-compose exec web sh
```

#### 4. 实践项目

**初级练习** - 在 `Compose-Examples/examples` 中尝试：
- `wordpress/` - WordPress + MySQL
- `nextcloud/` - Nextcloud + PostgreSQL
- `nginx-proxy-manager/` - 反向代理

**中级练习**:
- `grafana-monitoring/` - Grafana + Loki + Promtail
- `authelia/` - 认证服务 + Redis
- `gitea/` - Git 服务 + PostgreSQL

**高级练习**:
- `arr-suite/` - 完整的媒体服务器栈（多个服务）
- 自己设计一个多服务应用

#### 5. 深入主题

参考 `docker-tutorial` 中的专题教程：
- `docker-compose-override/` - 覆盖配置
- `docker-compose-profiles/` - 配置文件
- `docker-env-tutorial/` - 环境变量管理
- `docker-yaml-anchors/` - YAML 锚点复用

---

### 第五阶段：进阶主题 (持续学习)

#### 1. Docker 网络
- Bridge 网络（默认）
- Host 网络
- Overlay 网络（Swarm）
- 自定义网络

**实践**:
```bash
# 创建网络
docker network create my-network

# 查看网络
docker network ls

# 查看网络详情
docker network inspect my-network
```

#### 2. 数据卷管理
- Named volumes（命名卷）
- Bind mounts（绑定挂载）
- tmpfs mounts（临时文件系统）

**实践**:
```bash
# 创建数据卷
docker volume create my-data

# 查看数据卷
docker volume ls

# 查看数据卷详情
docker volume inspect my-data

# 清理未使用的数据卷
docker volume prune
```

#### 3. 健康检查
参考 `docker-tutorial` 中的 Health Check 章节

**Dockerfile 中的健康检查**:
```dockerfile
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
```

**docker-compose.yml 中的健康检查**:
```yaml
services:
  web:
    image: nginx
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost"]
      interval: 30s
      timeout: 3s
      retries: 3
      start_period: 5s
```

#### 4. 日志管理
- 查看容器日志
- 配置日志驱动
- 日志轮转

参考 `docker-tutorial` 中的日志管理章节

#### 5. 安全最佳实践
- 不要以 root 用户运行容器
- 使用官方镜像或可信来源
- 定期更新镜像
- 扫描镜像漏洞
- 使用 secrets 管理敏感信息

---

## 🛠️ 实战项目建议

### 项目 1: 个人博客系统
**技术栈**: WordPress + MySQL + Nginx Proxy
**学习目标**:
- 多容器编排
- 数据持久化
- 反向代理配置

### 项目 2: 开发环境
**技术栈**: Code-Server + PostgreSQL + Redis
**学习目标**:
- 开发工具容器化
- 网络隔离
- 环境变量管理

### 项目 3: 监控系统
**技术栈**: Grafana + Prometheus + Node Exporter
**学习目标**:
- 服务发现
- 数据采集
- 可视化配置

### 项目 4: 完整 Web 应用
**技术栈**:
- Frontend: React (Nginx)
- Backend: Node.js/Python
- Database: PostgreSQL
- Cache: Redis
- Proxy: Traefik

**学习目标**:
- 完整应用架构
- 服务间通信
- 负载均衡
- SSL 证书管理

---

## 📖 推荐学习资源

### 官方文档
- [Docker 官方文档](https://docs.docker.com/)
- [Docker Compose 文档](https://docs.docker.com/compose/)
- [Dockerfile 参考](https://docs.docker.com/engine/reference/builder/)

### 视频教程
- `docker-tutorial` 仓库中的 YouTube 视频链接
- Docker 官方 YouTube 频道

### 实践平台
- [Play with Docker](https://labs.play-with-docker.com/) - 在线练习环境
- [Docker Hub](https://hub.docker.com/) - 镜像仓库

---

## 🎓 学习检查清单

### Docker 基础
- [ ] 理解 Image、Container、Registry 概念
- [ ] 能够拉取和运行镜像
- [ ] 掌握基本的容器操作命令
- [ ] 能够查看容器日志和进入容器

### Dockerfile
- [ ] 理解 Dockerfile 的作用
- [ ] 掌握常用指令（FROM, RUN, COPY, CMD, EXPOSE 等）
- [ ] 能够编写简单的 Dockerfile
- [ ] 了解多阶段构建
- [ ] 知道如何优化镜像大小

### Docker Compose
- [ ] 理解 Docker Compose 的作用
- [ ] 掌握 docker-compose.yml 语法
- [ ] 能够定义多服务应用
- [ ] 理解服务依赖关系
- [ ] 掌握常用的 compose 命令

### 进阶主题
- [ ] 理解 Docker 网络模型
- [ ] 掌握数据卷管理
- [ ] 能够配置健康检查
- [ ] 了解日志管理
- [ ] 知道安全最佳实践

### 实战能力
- [ ] 能够容器化一个简单应用
- [ ] 能够部署多容器应用栈
- [ ] 能够调试容器问题
- [ ] 能够优化 Docker 配置
- [ ] 能够编写生产级别的配置

---

## 💡 学习建议

1. **动手实践**: Docker 是实践性很强的技术，一定要多动手
2. **循序渐进**: 从简单示例开始，逐步增加复杂度
3. **阅读文档**: 遇到问题先查官方文档
4. **查看示例**: `Compose-Examples` 中有大量实际项目可以参考
5. **理解原理**: 不要只记命令，要理解背后的原理
6. **记录笔记**: 记录遇到的问题和解决方案
7. **持续学习**: Docker 生态在不断发展，保持学习

---

## 🚀 快速开始

```bash
# 1. 进入 docker-tutorial 目录，阅读 README
cd /Users/kyle/Projects/github-kb/docker-tutorial
cat README.md

# 2. 尝试第一个容器
docker run -d -p 8080:80 nginx
# 访问 http://localhost:8080

# 3. 查看 Compose-Examples 中的简单示例
cd /Users/kyle/Projects/github-kb/Compose-Examples/examples/nginx-php
cat docker-compose.yml

# 4. 运行你的第一个 compose 项目
docker-compose up -d
```

祝学习顺利！🎉
