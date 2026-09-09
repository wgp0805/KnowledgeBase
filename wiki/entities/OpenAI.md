---
title: "OpenAI"
type: entity
tags: [AI公司, OpenAI]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/连 Karpathy 都开始恐慌：AI 正在重新定义「程序员」｜ 硅基时间.md, raw/01-articles/2026-09-06-实测GPT-6 Astra：曾经的那个OpenAI，回来了。.md, raw/01-articles/2026-09-05 - GPT-6 最让人后背发凉的，不是它变强了，而是它开始自己训练自己.md, raw/01-articles/2026-09-07-"GPT-6 Astra 正式登场"会怎样改变现有技术栈？.md]
last_updated: 2026-09-09
---

## 定义
美国 AI 研究公司，推出了 Codex（桌面 Agent）和 ChatGPT 等产品。联合创始人包括 Andrej Karpathy。

## 关键信息
- 推出 Codex 桌面端 Agent，支持 Browser Use、Computer Use、image2 生图
- ChatGPT 手机端可远程操控电脑上的 Codex
- 提供 GPT-4o 系列模型
- Codex Pro 会员 $20/月，额度较大方
- **Vibe Engineering 内部实践**：
  - 工程师对 Codex 采用率超过 92%
  - 所有内部 PR 都由 Codex 审核
  - 用 Codex 的工程师产出的合并 PR 比不用的人多 70%
- **核心团队成员**：Romain Huet（开发者体验负责人）、Aaron Friel（工程师）
- **GPT-6 Astra**（2026-09-03 发布）：详见 [[GPT-6]]，ARC-AGI-3 从 7.8% 提升至 99.9%，总裁 Brockman 称"Welcome to the AGI era"，首款让前代模型参与训练监督的前沿大模型
- **Stargate 基地**：得州，GPT-6 预训练动用超 10 万块 GPU（GPT-4 约 2.5 万块）
- **GPT-6 Astra 技术栈影响**（2026-09-07 分析）：只支持 [[ResponsesApi]]，推动后端升级为 [[AgentRuntime]]、前端升级为 [[TaskConsole]]、安全升级为 [[AIControlPlane]] 独立层，成本管理从 Token 转向 [[任务级成本]]（详见 [[摘要-GPT-6-Astra改变技术栈]]）
- **Codex 公开用户里程碑**（2026-09-08 统计，各阶段口径不完全一致）：5 月底 500 万 → 7 月 22 日 1000 万 → 8 月底 2500 万。同期 4—8 月共 36 次公开额度重置，其中 61.1% 并非故障补偿，而是庆祝、产品节点与临时重置，构成一套[[事件营销]]机制（详见 [[摘要-codex重置的真正原因]]）

## 关联连接
- [[Codex]] — OpenAI 的 Agent 产品
- [[Tibo]] — Codex 负责人，额度重置的执行者
- [[事件营销]] — Codex 重置机制的本质
- [[摘要-codex重置的真正原因]] — 来源（重置机制与用户里程碑）
- [[Anthropic]] — 竞品，同期出现封号风波
- [[ClaudeCode]] — 竞品
- [[Anthropic]] — 竞争对手
- [[AndrejKarpathy]] — 联合创始人
- [[RomainHuet]] — 开发者体验负责人
- [[AaronFriel]] — 工程师
- [[VibeEngineering]] — 内部实践的编程模式
- [[摘要-vibe-engineering-era]] — Vibe Engineering 内部分享来源
- [[GPT-6]] — GPT-6 Astra 新一代模型
- [[摘要-gpt6-astra实测体验]] — GPT-6 Astra 实测来源
- [[摘要-gpt6-自训练信号]] — GPT-6 自训练信号分析来源
- [[摘要-GPT-6-Astra改变技术栈]] — GPT-6 Astra 技术栈影响分析来源
- [[AgentRuntime]] — 后端升级方向
- [[TaskConsole]] — 前端升级方向
- [[AIControlPlane]] — 安全控制独立层
- [[ResponsesApi]] — Astra 唯一支持接口
- [[任务级成本]] — 成本管理方向
