---
title: "OpenMuse"
type: entity
tags: [AI-Agent, 个人Agent, 浏览器自动化, 开源]
sources: [raw/09-archive/为什么越来越多人用OpenMuse？.md, raw/01-articles/2026-10-08 - 轻量开源版 Muse 来了！.md, "raw/01-articles/2026-10-09 - 3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。.md"]
last_updated: 2026-10-12
---

## 定义
OpenMuse 是 CopilotKit 团队于 2026 年 9 月开源的个人 AI Agent（MIT 协议），定位"Agent 的工位"：为单个 Agent 提供持久浏览器、隔离终端与文件系统的完整执行环境，并支持人工随时接管实时浏览器会话。

## 关键信息
- 与 AutoGen/CrewAI 的区别：那些解决"多 Agent 怎么协作"，OpenMuse 解决"一个 Agent 怎么真正动手完成任务"
- 执行环境：Playwright Chromium 持久化 profile（cookies/登录态/历史保留）+ 隔离 Linux 终端 + 文件系统
- 核心差异化"Take control"：Agent 卡在验证码/双因素认证/复杂页面时，人接管的是**同一个实时浏览器会话**，交还后 Agent 从当前状态继续，不重启不重登
- 持久化任务引擎：任务支持暂停、恢复、取消、重试，关闭浏览器后继续执行；每次外部写入需审批
- 技术栈 TypeScript（Node.js 24 LTS + pnpm 11.19.0），暴露 REST + WebSocket API，Java 侧可经 HTTP 任务导向调用（无官方 SDK）
- 内置零配置演示模式（pnpm dev，8081 端口），跨 iOS/Android/Web
- 缺点：Alpha 阶段接口不稳、配置较复杂、Chromium 约 0.25-0.48GB 内存、单所有者无多租户认证
- 上线不到一个月 GitHub 4.2K Star；适用网页调研、价格监控、PDF 表单自动化
- **架构补全（2026-10-08，详见 [[摘要-openmuse-轻量muse复刻]]）**：客户端 Expo/React Native 三端同码，前后端走 AG-UI 协议（CopilotKit 推出的事件流规范）；服务端 Hono + CopilotKit runtime（`pnpm dev` 单进程同时起 HTTP 接口与后台 Worker），数据库用进程内 Postgres PGlite，浏览器是独立 Playwright 服务、Linux 电脑是 Docker 容器；DeepSeek 需借 `openai/` 前缀并设 `OPENAI_CHAT_COMPLETIONS=true`
- **可靠性设计**：任务每步写检查点（state.source/state.filledId），Worker 每秒扫任务表、最多并发 3 个，用 Postgres JSONB `@>` 实现 CAS 抢占，60 秒租约 + 20 秒心跳续租，续租失败即中止——与 MySQL 乐观锁同构；崩溃后租约过期自动重领任务并跳过已完成步骤
- **安全边界**：浏览器服务防 SSRF——仅允许 80/443 公网地址、拦截 localhost/local/internal/home/lan 域名、本地代理固定校验时解析的 IP 阻断 DNS 重绑定；遥测默认全量上报（`COPILOTKIT_TELEMETRY_DISABLED=true` 关闭）、网页搜索默认走 Parallel 的 Search MCP
- **能力差距**：浏览器只能读网页（`page.evaluate` 固定读取 body 文本），不能像 [[MetaMuse]] 那样订行程下单付款
- **开源平替盘点视角（2026-10-09，详见 [[摘要-personal-agent-open-source-alternatives]]）**：媒体将其直接称为"最近爆火的 Meta 的 Muse 的开源平替"——支持 iOS/Android/Web 查资料、处理邮件与 PDF，在同一应用查看任务计划与执行进度；可**定期检查公开页面**，内容变化、可用状态变化或价格达到设定阈值时发出提醒；任务计划与状态持久保存，支持暂停/继续/取消，只要后端服务持续运行，关闭前端后后台工作仍继续；Alpha 阶段需自行部署并连接模型、Intelligence 和相关服务

## 关联连接
- [[摘要-personal-agent-open-source-alternatives]] — 来源（三款 Personal Agent 开源平替盘点）
- [[Rakazo]] — 同文的 Grok Bot 开源平替
- [[OpenDots]] — 同文的 Dots 开源平替
- [[摘要-openmuse-agent工位与浏览器接管]] — 来源
- [[摘要-openmuse-轻量muse复刻]] — 来源（架构、租约/CAS 与 SSRF 防护拆解）
- [[MetaMuse]] — 同名系个人 Agent 产品对照
- [[personal-ai-agent]] — 所属赛道
- [[WorkBuddy]] — 同类可接管/本地执行 Agent
