---
title: "Umami"
type: entity
tags: [工具, Docker, 网站统计, 隐私]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
Umami 是开源的网站访问统计工具，作为 Google Analytics 的隐私友好替代品：自己部署、数据自己掌握、默认不采集个人数据。

## 关键信息
- 完全开源可定制，不把访问数据交给第三方
- 隐私友好：不做跨站追踪、不收集个人身份信息，无 Cookie 弹窗负担
- 适用：个人博客、小型站点、注重合规与隐私的产品
- 部署注意：镜像 `ghcr.io/umami-software/umami:postgresql-latest` 必须有 PostgreSQL；文章里的 compose 只给了 `DATABASE_URL` 与 `depends_on: db`，`db` 服务需自行补全
- 最小启动：`-p 3000:3000 ghcr.io/umami-software/umami:postgresql-latest`
- 边界：轻量统计，不覆盖全链路埋点/归因分析

## 关联连接
- [[Docker]] — 分发方式
- [[PostgreSQL]] — 必需的数据存储
- [[摘要-8个docker神器]] — 来源
