---
title: "DockerCompose生产配置"
type: concept
tags: [Docker, Docker Compose, 生产环境, 部署, 最佳实践]
sources: [raw/01-articles/2026-09-16-Ubuntu 22.04 Docker 从零部署全栈项目实录：Next.js + FastAPI + PostgreSQL 一次跑通 - 码农刚子.md]
last_updated: 2026-09-17
---

## 定义
Docker Compose 生产配置指在 `docker-compose.prod.yml` 中应用的生产级最佳实践，与开发环境（带 `--reload`、暴露端口、宽松变量）区分。核心要点：API 多进程、端口只绑本地、环境变量强制必填、数据持久化、反向代理统一入口。

## 关键信息

### 生产配置要点
1. **API 去掉 `--reload`，加 `--workers 4`**：开发用 `--reload` 热重载，生产用多进程提升吞吐
2. **Web/Api 只绑 `127.0.0.1`**：避免直接暴露，由 Nginx 反向代理统一入口
3. **用 `${VAR:?}` 强制必填环境变量**：缺失即报错停止，避免用默认值跑生产
4. **PostgreSQL 数据持久化到命名卷**：`pgdata:/var/lib/postgresql/data`，容器销毁数据不丢
5. **Nginx 反向代理**：80 端口统一入口，转发到 api 和 web

### 典型结构
```
services:
  postgres:  # 数据库（命名卷持久化）
  api:       # 后端（多进程，绑 127.0.0.1）
  web:       # 前端（绑 127.0.0.1）
  nginx:     # 反向代理（80 端口统一入口）
volumes:
  pgdata:
networks:
  backend:
```

### 启动与验证
- `docker compose -f docker-compose.prod.yml up -d --build`
- 等 20 秒冷启动完成后验证：`docker compose ps` / `curl http://127.0.0.1:8000/health`
- 正常返回 `{"status":"ok","env":"prod"}`

### 常见踩坑
- `COPY /app/public not found`：[[Next.js]] standalone 模式需 `public` 目录，建 `frontend/public/.gitkeep`
- `/health` 空响应：API 冷启动慢，等 20 秒或加健康检查重试
- 时区 aware/naive 报错：[[PostgreSQL]] 列是 naive，代码写 aware，统一用 `datetime.utcnow()` 或落库前 `replace(tzinfo=None)`

## 关联连接
- [[Docker]] — 主要工具
- [[码农刚子]] — 实践者
- [[摘要-ubuntu-docker-全栈部署实录]] — 来源
- [[国内源三件套]] — 配套的国内网络配置
- [[DaoCloud加速器]] — 镜像加速
- [[Next.js]] / [[FastAPI]] / [[PostgreSQL]] / [[Nginx]] — 典型组合
