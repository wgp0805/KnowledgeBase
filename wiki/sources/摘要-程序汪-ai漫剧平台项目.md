---
title: "摘要-程序汪-ai漫剧平台项目"
type: source
tags: [来源, 私活项目, AI漫剧, 程序汪, SaaS]
sources: [raw/09-archive/2026-11-05 - 程序汪5万30天接的AI漫剧项目.md]
last_updated: 2026-11-09
---

## 核心摘要
程序汪私活小团队以 **5 万元 / 30 天 / 2 人**接下的「AI 漫剧创作平台」SaaS 项目：面向短剧编剧/MCN/个人创作者，输入一个故事主题，系统通过**九阶段流水线**自动生成从意图、大纲、小说、剧本、资产、分镜到视频的完整漫剧内容，并配套无限画布节点编排、资产库、多模型统一网关、代理分销与充值计费商业闭环。技术栈为 **Python FastAPI（模块化单体）+ Vue 3/Vite/TS + PostgreSQL（JSONB 存草稿与画布）+ Redis + Celery 异步任务**，AI 辅助开发用 Codex 出方案、TRAE 写代码。项目用 7 个开发 Skill（后端架构/数据库建模/任务队列/第三方模型接入/API 测试/安全权限/前端设计）驱动。业务合规要求：ICP 备案、AI 生成内容标注、广电总局短剧审核、代理分润需法务审核。

## 关键信息
- **报价与配置**：5 万整体费用（正规合同）、2 人、30 天、云服务器 2 台、维护费 5000/年；月成本估算约 ¥1000（不含模型 API 调用费）
- **AI 工具**：Codex 出方案，TRAE（deepseek/kimi 等）写代码
- **六项创新点**：九阶段生成流水线、多模型统一网关（文本/生图/生视频）、无限画布节点编排、原子扣费+异步任务（数据库行锁防超扣）、代理分销体系、PostgreSQL JSONB 混合存储
- **九阶段**：0 输入→1 意图→2 方向→3 大纲→4 小说→5 剧本→6 资产→7 分镜→8 视频（每阶段独立可编辑、可重生成、草稿自动保存）
- **数据库**：users/sessions/projects(contents jsonb 九阶段草稿)/models/jobs/assets/canvases(body jsonb 节点连线)/ledger/orders(支付回调幂等键 order_no)/agents(代理申请+邀请码)
- **安全**：全站 HTTPS、JWT 2 小时+刷新、Redis 令牌桶限流 60 次/分、手机号加密存储、余额原子扣减、支付验签+order_no 幂等+日终对账+失败自动退款、API 密钥只存后端
- **7 个开发 Skill**：ai-drama-backend-architect、ai-drama-db-modeler、ai-generation-job-queue（最关键，异步任务）、ai-provider-integration（OpenArt/Runway/HeyGen/OpenAI/Replicate）、backend-api-test-suite、saas-auth-rbac-security、frontend-design

## 关联连接
- [[AI漫剧创作平台]] — 实体
- [[AI漫剧工作流]] — 概念（九阶段平台化落地）
- [[程序汪]] — 作者
- [[FastAPI]] — 后端框架
- [[Vue3]] — 前端框架
- [[Celery]] — 异步任务队列
- [[PostgreSQL]] — 数据库（JSONB）
- [[微短剧]] — 内容产业语境
- [[代理分销]] — 概念
- [[LLM网关]] — 多模型统一网关
