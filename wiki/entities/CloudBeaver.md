---
title: "CloudBeaver"
type: entity
tags: [工具, Docker, 数据库管理, Web]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
CloudBeaver 是 DBeaver 团队出品的 Web 版数据库管理工具，在浏览器里统一管理多种数据库。

## 关键信息
- 多库支持：MySQL、PostgreSQL、SQLite 等（DBeaver 驱动体系）
- 相比 PhpMyAdmin 的体验提升：常用快捷键、SQL 面板、智能提示（弱于桌面客户端但仍可用）
- 适合场景：不想在每台机器装 Navicat 类客户端、需要在隔离环境/临时设备上连库排查
- 最小启动：`docker run -d --name cloudbeaver -p 8978:8978 dbeaver/cloudbeaver:latest`，工作区卷映射到 `/opt/cloudbeaver/workspace`
- 默认 8978 端口；生产使用务必改初始密码并限制来源网段

## 关联连接
- [[Docker]] — 分发方式
- [[MySQL]] / [[PostgreSQL]] / [[SQLite]] — 可管理的数据源
- [[Navicat]] — 桌面客户端对照
- [[摘要-8个docker神器]] — 来源
