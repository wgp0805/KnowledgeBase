---
title: "摘要-openmuse-轻量muse复刻"
type: source
tags: [来源, PersonalAgent, 开源, CopilotKit]
sources: [raw/09-archive/2026-10-08 - 轻量开源版 Muse 来了！.md]
last_updated: 2026-10-09
---

## 核心摘要
Meta 发布 Personal Agent 产品 Muse（云端专属 Muse Secure VM + Sentinel 审批 Agent）两周后，做 AG-UI 协议的 CopilotKit 开源了 OpenMuse：MIT 协议、一套 React Native 代码跑 iOS/Android/Web，具备浏览器、Linux 终端、文件、后台任务等 Muse 同款能力。架构上客户端用 Expo/RN，前后端走 AG-UI 事件流，服务端 Hono + CopilotKit runtime，数据库用进程内 Postgres（PGlite），浏览器为独立 Playwright 服务。文章重点拆解了其可靠性设计：任务每步写检查点（checkpoint）、Worker 基于 SQL 租约 + Postgres JSONB `@>` 实现 CAS 抢占与续租（60 秒租约、20 秒心跳），进程崩溃后任务可自动重领并跳过已完成步骤；浏览器服务带 SSRF 防护（端口/域名校验 + 本地代理阻断 DNS 重绑定）。局限：浏览器仅能读网页、遥测默认全量上报、需 CopilotKit API Key。

## 关联连接
- [[OpenMuse]] — 文章主角
- [[MetaMuse]] — 被复刻的原产品
- [[personal-ai-agent]] — 所属赛道
- [[DeepSeek-V4.1-Flash]] — 文中配置的模型
- [[乐观锁]] — CAS 租约机制的同族概念
- [[检查点机制]] — 任务恢复依赖的机制
