---
title: "摘要-大厂补harness-agent从模型转向运行时"
type: source
tags: [Harness, Agent, Anthropic, OpenAI, DeepSeek, Pi, 运行时, 框架对比]
sources: [raw/01-articles/2026-08-29-为什么大厂都在补 Harness？Agent 的竞争正在从模型转向运行时.md]
last_updated: 2026-08-31
---

## 核心主旨

论证 Agent 竞争正从"模型层"转向"运行时层（Harness）"，定义 Harness 的边界，并对比 Anthropic、OpenAI、DeepSeek、Pi Agent 四家的 Harness 技术路线差异。核心公式：**Agent = Model + Harness**。

## 关键信息

### Harness 边界定义
- Harness = 模型之外的一切：工具调用、记忆、上下文控制、MCP、Skills、子 Agent 编排、安全沙箱
- 模型负责"推理"，Harness 负责"把推理变成可执行的工程化操作"
- 类比：模型是发动机，Harness 是底盘+变速箱+转向系统

### 四家技术路线对比

| 厂商 | Harness 路线 | 核心特征 |
|------|-------------|---------|
| **Anthropic** | Claude Code | 本地执行 + 协作子 Agent，透明输出每一步，敏感操作需确认 |
| **OpenAI** | Codex | 云端沙箱 + 并行子 Agent（最多 8 个），隔离安全，批量任务强 |
| **DeepSeek** | DeepSeek Harness | 一切皆插件，MIT 开源，社区插件生态爆发 |
| **Pi Agent** | Pi | 极简 Harness，系统提示词仅 200 Token，上下文工程化 |

### 竞争转向的逻辑
1. 模型层趋同：头部模型能力差距缩小，单靠模型难分胜负
2. 运行时差异化：Harness 决定"模型能力如何落地"，成为新战场
3. 生态壁垒：插件/Skill/MCP 生态形成网络效应，迁移成本上升

## 关联连接
- [[Harness]] — 核心概念
- [[DeepSeekHarness]] — DeepSeek 路线
- [[ClaudeCode]] — Anthropic 路线
- [[Codex]] — OpenAI 路线
- [[PiAgent]] — Pi 路线
- [[摘要-大厂争相开源harness背后的商业阳谋]] — 同主题深度分析
- [[摘要-DeepSeek-Harness任务管理方法]] — 同期同主题文章
- [[摘要-mimo-code发布]] — 小米 MiMo Code 的 Harness 架构
