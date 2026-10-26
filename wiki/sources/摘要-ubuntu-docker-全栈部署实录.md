---
title: "摘要-ubuntu-docker-全栈部署实录"
type: source
tags: [Docker, Ubuntu, Next.js, FastAPI, PostgreSQL, Docker Compose, 国内源, 部署, DevOps]
sources: [raw/09-archive/2026-09-16-Ubuntu 22.04 Docker 从零部署全栈项目实录：Next.js + FastAPI + PostgreSQL 一次跑通 - 码农刚子.md]
last_updated: 2026-09-17
---

## 核心摘要
作者记录在 [[Ubuntu]] 22.04 LTS（阿贝云免费云服务器）上从零安装 [[Docker]]、配置国内镜像源、编写 `docker-compose.prod.yml`，最终把一个 [[Next.js]] 前端 + [[FastAPI]] 后端 + [[PostgreSQL]] 数据库的全栈项目跑上线的完整过程。核心经验是「[[国内源三件套]]」配置（DaoCloud 镜像加速 + 清华 pip 源 + 淘宝 npm 源）基本能覆盖国内大部分镜像拉取和包安装场景。

## 部署流水线

### 一、安装 Docker 与 Docker Compose
- Ubuntu 22.04 默认源的 `docker.io` 能装但 `docker-compose-plugin` 经常找不到
- 建议换阿里云 Docker CE 源：添加 GPG key + sources.list
- 安装 `docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin`
- 验证：`docker --version`（24.x）/ `docker compose version`（v2.x）

### 二、配置国内 Docker 镜像加速器
- 国内直接拉 `docker.io` 容易超时
- 踩过腾讯/163/阿里云专属加速器几个坑，最后 **DaoCloud 公共加速器** 最稳
- `daemon.json` 配置 `"registry-mirrors": ["https://docker.m.daocloud.io"]`
- **坑**：地址末尾不要加斜杠，否则可能报 403

### 三、生产级 docker-compose.prod.yml 要点
- API 去掉 `--reload`，加 `--workers 4`（生产多进程）
- Web/Api 只绑 `127.0.0.1`，避免直接暴露
- 用 `${VAR:?}` 强制必填环境变量（缺失即报错停止）
- PostgreSQL 数据持久化到命名卷（`pgdata`）
- Nginx 作为反向代理，80 端口统一入口

### 四、Dockerfile 国内源
- 后端 `ARG PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple`
- 前端 `ENV npm_config_registry=https://registry.npmmirror.com`
- 三件套（DaoCloud + 清华 pip + 淘宝 npm）覆盖大部分国内场景

### 五、启动与验证
- `docker compose -f docker-compose.prod.yml up -d --build`
- 等 20 秒冷启动完成后验证：`docker compose ps` / `curl http://127.0.0.1:8000/health`
- 正常返回 `{"status":"ok","env":"prod"}`

## 踩坑总结

| 现象 | 原因 | 解决 |
|------|------|------|
| `Unable to locate package docker-compose-plugin` | 默认源没这个包 | 换阿里云 Docker CE 源 |
| 拉镜像 `i/o timeout` | docker.io 被墙/慢 | 配 DaoCloud 镜像加速器 |
| pip/npm install 超时 | 境外源 | Dockerfile 里加清华/淘宝源 |
| `COPY /app/public not found` | Next.js standalone 需要 public 目录 | 建 `frontend/public/.gitkeep` |
| `/health` 一开始空响应 | API 冷启动慢 | 等 20 秒或加健康检查重试 |
| 时区 aware/naive 报错 | PostgreSQL 列是 naive，代码写 aware | 统一用 `datetime.utcnow()` 或落库前 `replace(tzinfo=None)` |

## 关联连接
- [[Docker]] — 主要工具
- [[FastAPI]] — 后端框架
- [[PostgreSQL]] — 数据库
- [[Next.js]] — 前端框架（新实体）
- [[Ubuntu]] — 操作系统（新实体）
- [[Nginx]] — 反向代理
- [[国内源三件套]] — 概念页
- [[DaoCloud加速器]] — Docker 镜像加速
- [[DockerCompose生产配置]] — 概念页
- [[码农刚子]] — 文章作者
