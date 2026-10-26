---
title: "OpenClaw"
type: entity
tags: [实体, AI Agent, 开源项目]
sources: [raw/09-archive/小龙虾（OpenClaw）教程汇总.md, raw/01-articles/2026-08-02-MCP 第五版 × OpenClaw.NET：从协议升级到生态编排 - 张善友.md, raw/09-archive/2026-09-24-体验完Meta的Muse，原来这才是我们想要的AI助理.md, raw/09-archive/2026-09-30-从“登顶GitHub历史第一”到“大厂集体撤退”：OpenClaw的Agent浪潮，为什么“养虾”养不活.md, raw/01-articles/2026-10-01-Personal Agent 神仙打架 用五个维度看懂六条海外路线.md]
last_updated: 2026-10-08
---

## 定义
OpenClaw（小龙虾）是一个开源的 AI Agent 项目，由 Peter Steinberger 创建，允许用户通过终端与 AI 模型交互并执行复杂任务。

## 关键信息
- **创始人**：Peter Steinberger（"龙虾之父"，月烧 940 万 token）
- **核心特点**：
  - 终端 AI Agent，类似 Claude Code
  - 支持 Skill 扩展机制
  - 开源免费，社区活跃

### OpenClaw.NET MetaSKILL 编排引擎
OpenClaw.NET 提供基于 YAML 声明式 DAG 的 MetaSKILL 编排引擎，用于生产级 AI 工作流编排：

- **设计范式**：声明即编排（Declaration-as-Orchestration），编排逻辑是 YAML 声明的 DAG
- **运行环境**：OpenClaw.NET Gateway 服务器进程内
- **触发方式**：自然语言触发器匹配 + `meta_invoke` 工具
- **7 种步骤类型**：覆盖不同执行需求（llm_chat、agent、fan_out、skill_exec、user_input、route 等）
- **核心特性**：
  - `depends_on` 声明 DAG 依赖
  - `fan_out` 动态展开并行子步骤，wave-based 调度
  - `routes` / `when` 条件路由分支
  - `on_failure` 声明式失败替换步骤
  - `user_input` 人机交互暂停点（审批检查点）
  - `output_contract` 每步 JSON Schema 输出校验
  - `tool_allowlist` + `capabilities` + `MetaSkill.Enabled` 三步安全门禁
- **安全体系**：4 层超时保护（step / retry / session contract / agent loop）
- **审计能力**：持久化审计记录 + CLI replay/reconstruct
- **双运行时**：AgentRuntime + MafAgentRuntime
- **适用场景**：生产环境 CI/CD 工作流、需要人机交互审批、多人长期维护的重复任务
- **与 Claude Code Workflows 对比**：MetaSKILL 安全审计完善适合生产，Workflows 灵活度高适合探索

- **生态系统**：
  - 一站式部署平台：WorkBuddy、QoderWork、QClaw
  - 微信接入：ClawBot（腾讯官方插件）
  - 大量第三方 Skill
- **注意事项**：
  - Token 消耗较大
  - 需要从正规渠道安装，避免安全隐患

- **Pi Agent 作为运行时**：Pi Agent（Armin Ronacher 创建）是 OpenClaw 的 Agent 运行时。OpenClaw 不把 Pi 当子进程或 RPC 服务调用，而是直接嵌入 Pi SDK——会话状态、工具执行、消息历史都在 OpenClaw 进程内运行，无序列化/反序列化开销。详见 [[摘要-pi-agent-4工具极简主义]]。

### 启发 Meta Muse（2026-09）
Meta 超级智能实验室产品负责人 Nat Friedman 公开承认 [[MetaMuse]] 的产品思路受 OpenClaw 很深启发：团队内部很早就大量使用 OpenClaw，想做一个类似的东西再改造成几亿甚至几十亿用户都容易接触的产品。OpenClaw 早已在极客群体验证了"一个 Agent 长期在线、拥有自己的电脑、可调用工具、替用户持续处理任务"的体验；Muse 降低门槛做的就是不让普通用户意识到自己在调用多少 Agent 能力。详见 [[摘要-meta-muse-个人ai助理体验]]。

### 登顶 GitHub 历史第一与封装层困境（2026-03 至 2026-09）
来自 [[摘要-openclaw-agent浪潮养虾养不活]]。2026 年 3 月，这个把 Claude Code 接进 WhatsApp 的周末项目以超过 **24.8 万星登顶 GitHub 历史第一**（把 Linux 踩在脚下）。但"价值沉淀在开源协议与生态层"：所有基于它做封装的 C 端产品本质是流量二道贩子——不掌握模型也不掌握框架，汉化界面、预装技能、补贴算力三件事只构成成本不构成壁垒；原作者 [[PeterSteinberger]] 2026 年 2 月加入 [[OpenAI]] 负责下一代个人智能体、项目移交独立基金会，封装层生意从一开始就没写进路线图。国内跟进的 [[QClaw]] 等产品九个月内集体撤退。大厂涌入被形容为"给开源生态做了一次昂贵的地推"——教育了用户"Agent 可以做什么"，但用户真想用时会去用 OpenClaw 本身或 Steinberger 的新产品。OpenClaw 证明了"Agent 可以干活"，但没证明"用户愿意为 Agent 干活付费"。

### "所有权"路线解读（2026-10-01）
来自 [[摘要-personal-agent六条海外路线]]。官方文档将 OpenClaw 描述为 local-first、模型无关、可扩展、可自托管的开放系统：助手运行在用户自己的基础设施上，经常用消息渠道访问，Gateway 作为持续在线控制层；用户可选模型提供商甚至本地模型让数据留在自己设备上。在 [[默认委托权]] 争夺中，它竞争的不是最低学习成本而是**所有权**——系统跑在哪、用哪个模型、接什么渠道、怎样配置多 Agent 与工具都由用户决定，也可检查修改系统本身。代价是自托管只是把责任从厂商转移给使用者（安装、升级、密钥、网络暴露、插件质量、模型成本、备份），官方建议外联和广告投放等动作保持人在回路。版本提示：2026 年 8 月 v2026.8.1 曾以"OpenClaw 2.0"发布，截至 10 月 1 日官方版本目录已出现 v2026.9.6，2.0 并非当前最新版。

### 热度参照物（2026-10-19）
[[REA]] 爆火时被用作对比基准：发文时 REA 两天内从 15 万涨到 24.1 万 Star，博主称其"全民逆向"热度不亚于当年"全民养虾"的 OpenClaw，增速连 OpenClaw 也自愧不如（见 [[摘要-霸榜github-ai逆向神器-rea-archify]]）。

## 关联连接
- [[摘要-OpenClaw小龙虾教程汇总]] — 来源
- [[摘要-meta-muse-个人ai助理体验]] — 来源（启发 Meta Muse）
- [[MetaMuse]] — 受其启发的消费级产品
- [[personal-ai-agent]] — 其验证的个人 Agent 形态
- [[PeterSteinberger]] — 创始人
- [[ArminRonacher]] — Pi Agent 创建者（Pi 是 OpenClaw 的 Agent 运行时）
- [[ClaudeCode]] — 类似 AI Agent
- [[Skill]] — 技能扩展机制
- [[WorkBuddy]] — 部署平台
- [[ClawBot]] — 微信接入插件
- [[meta-skill]] — 元技能概念
- [[dynamic-workflow]] — 动态工作流对比概念
- [[摘要-Claude-Code-Workflows-vs-MetaSKILL]] — 来源
- [[OpenClawNET]] — .NET 生态版本（MCP 编排层）
- [[MCP]] — 核心协议
- [[摘要-mcp-v5-openclaw-net]] — 来源（MCP 第五版 × OpenClaw.NET）
- [[摘要-openclaw-agent浪潮养虾养不活]] — 来源（登顶 GitHub 历史第一与封装层退潮）
- [[QClaw]] — 撤退的国内封装产品
- [[Agent边际成本]] — 封装产品失败的成本结构原因
- [[摘要-personal-agent六条海外路线]] — 来源（"所有权"路线解读）
- [[默认委托权]] — 六条路线争夺的目标
- [[摘要-霸榜github-ai逆向神器-rea-archify]] — 来源（热度参照：REA 增速对比）
