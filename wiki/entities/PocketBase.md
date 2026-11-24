---
title: "PocketBase"
type: entity
tags: [工具, Docker, Serverless, 后端]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
PocketBase 是一个单可执行文件的轻量后端（常被称作"自托管版 BaaS/Serverless"），内置数据存储、文件存储、用户授权体系、管理后台与 REST API。

## 关键信息
- 单文件部署：内嵌 SQLite，无需外部数据库与中间件
- 自带能力：集合（表）管理、用户登录/注册与权限规则、文件上传、实时订阅（SSE）、Admin UI、REST API
- 适合：个人开发者/小团队快速搭后端，原型期验证想法，把"写 CRUD 后端"的时间省掉
- 最小启动：`-p 8090:8090 -v $PWD/pb_data:/pb_data ghcr.io/muchobien/pocketbase:latest`
- 边界：单机 SQLite 决定了它不适合高并发写入与多实例横向扩展；上量后要换 [[PostgreSQL]] / [[MySQL]] + 正经后端
- 与 [[Supabase]] 的差别：PocketBase 是单二进制零依赖，Supabase 是 Postgres 全家桶

## 关联连接
- [[Docker]] — 分发方式
- [[SQLite]] — 内嵌存储引擎
- [[Supabase]] — 托管 BaaS 对照
- [[摘要-8个docker神器]] — 来源
