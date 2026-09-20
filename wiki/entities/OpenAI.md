---
title: "OpenAI"
type: entity
tags: [AI公司, OpenAI]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/连 Karpathy 都开始恐慌：AI 正在重新定义「程序员」｜ 硅基时间.md, raw/01-articles/2026-09-06-实测GPT-6 Astra：曾经的那个OpenAI，回来了。.md, raw/01-articles/2026-09-05 - GPT-6 最让人后背发凉的，不是它变强了，而是它开始自己训练自己.md, raw/01-articles/2026-09-07-"GPT-6 Astra 正式登场"会怎样改变现有技术栈？.md, raw/01-articles/2026-09-15-OpenAI 总裁最新采访：现在所有人对 AI 的预测，大概率都是错的.md, raw/01-articles/2026-09-18-为什么中美头部Agent，不约而同走向开放？.md]
last_updated: 2026-09-20
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
- **Greg Brockman 访谈（2026-09 a16z）**：详见 [[摘要-OpenAI总裁Brockman最新采访]]
  - **AGI 时代已到来**：Astra 能连续运行 24 小时、跨越非常广泛的领域完成任务
  - **15→10→9 年推算**：2016-2017 与 Ilya Sutskever 推算顺利 15 年/大规模投入 10 年，实际约 8-9 年
  - **Astra 跃升关键在 [[ComputerUse]]**：让 AI 直接用人类界面，不需任何特殊 API 或重新设计系统，2015-11 内部会议就讨论过
  - **10000 agent 并行解决 [[NavierStokes]]** 并形式化成 [[Lean]] 格式——AI 开始创造新知识而非整合已有知识
  - **[[DefenderWindow]] 防御者窗口**：Hugging Face 事件后 AI 网络攻击能力已强，现在是防御者黄金期。Brockman 用 Codex 对个人网站做渗透 15 分钟找到 13 个漏洞、45 分钟自动修复。OpenAI 抽调 25% 生产工程师做安全升级，目标建 [[DefenseFactory]]
  - **[[FrontlineDefenders]] 10 亿美元计划**：为医院、水务公司、政府关键基础设施提供免费/折扣 AI 安全工具
  - **AI 真正形态不是文本框**：语音优先 + 持久记忆 + 主动 + 可依赖；北极星"简单"
  - **10 亿周活 + 15 亿弃用用户**是重要信号——AI 应主动告诉用户"我可以在这件事上帮你"
  - **就业判断**："AI 发展几乎不按逻辑推断方式发展，你对未来的预测大概率是错的，而且会以你没想到的方式错"。创业浪潮会来，[[问责制]] 是人类应保留的
  - **精力分配**：2026 年取消了 [[Sora]] 项目以解放专注力，遵循《The Score Takes Care of Itself》哲学

### 开放 Codex Harness（2026-09-10）
OpenAI 将 Codex 背后的 [[Harness]] 做成托管服务开放公测（一个月前已开源核心代码），把原本只供自家产品使用的系统变成别人开发 Agent 的起点。开放路径是"模型+Harness+托管运行连成一体"（Agent 的 AWS 时刻）。与 [[Anthropic]]（Claude Code SDK 扩展为通用 Agent SDK）、[[腾讯]]（开放 WorkBuddy 基座）方向一致。详见 [[摘要-中美头部agent走向开放]]。

## 关联连接
- [[Codex]] — OpenAI 的 Agent 产品
- [[Tibo]] — Codex 负责人，额度重置的执行者
- [[事件营销]] — Codex 重置机制的本质
- [[摘要-codex重置的真正原因]] — 来源（重置机制与用户里程碑）
- [[摘要-中美头部agent走向开放]] — 来源（开放 Harness）
- [[Anthropic]] — 竞品，同期出现封号风波
- [[ClaudeCode]] — 竞品
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
- [[GregBrockman]] — 联合创始人兼总裁
- [[摘要-OpenAI总裁Brockman最新采访]] — 来源（AGI 时代 + Navier-Stokes + 安全计划）
- [[Astra]] — GPT-6 旗舰模型
- [[ComputerUse]] — Astra 跃升关键能力
- [[NavierStokes]] — 10000 agent 解决的方程
- [[Lean]] — 数学证明形式化语言
- [[DefenderWindow]] — 防御者窗口
- [[DefenseFactory]] — 防御工厂范式
- [[FrontlineDefenders]] — 10 亿美元安全计划
- [[HuggingFace]] — 触发安全讨论的事件方
- [[Sora]] — 2026 年被取消的项目
- [[问责制]] — 人类应保留的价值
- [[IlyaSutskever]] — 2016-17 年共同推算者
- [[Harness]] — 开放的核心系统
- [[腾讯]] — 同步开放基座
