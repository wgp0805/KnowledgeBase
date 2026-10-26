---
title: "Next.js"
type: entity
tags: [前端框架, React, 全栈, Vercel]
sources: [raw/09-archive/2026-09-16-Ubuntu 22.04 Docker 从零部署全栈项目实录：Next.js + FastAPI + PostgreSQL 一次跑通 - 码农刚子.md]
last_updated: 2026-09-17
---

## 定义
Next.js 是基于 [[React]] 的全栈前端框架，由 Vercel 开发维护，支持服务端渲染（SSR）、静态生成（SSG）、API 路由等能力，常与 [[FastAPI]]/[[SpringBoot]] 等后端搭配构成全栈项目。

## 关键信息
- **生产部署坑**：Next.js standalone 模式需要 `public` 目录存在，否则 Docker 构建 `COPY /app/public not found` 报错；解决方法是建 `frontend/public/.gitkeep`
- **国内部署**：Dockerfile 加 `ENV npm_config_registry=https://registry.npmmirror.com`（淘宝 npm 源）加速依赖安装
- **典型组合**：[[Next.js]] 前端 + [[FastAPI]] 后端 + [[PostgreSQL]] 数据库 + [[Nginx]] 反向代理，用 [[Docker]] Compose 编排

## 关联连接
- [[摘要-ubuntu-docker-全栈部署实录]] — 来源
- [[React]] — 底层库
- [[FastAPI]] — 常搭后端
- [[PostgreSQL]] — 常搭数据库
- [[Docker]] — 部署工具
- [[Nginx]] — 反向代理
- [[码农刚子]] — 部署实录作者
