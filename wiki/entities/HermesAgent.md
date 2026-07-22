---
title: "HermesAgent"
type: entity
tags: [AI, Agent, 开源, 自学, NousResearch]
sources: [raw/09-archive/OpenClaw vs Hermes：万字深入讲解两大通用 Agent.md, raw/01-articles/2026-07-21-Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜.md]
last_updated: 2026-07-22
---

## 定义
Hermes Agent 是由 [[NousResearch]] 开发的开源通用 AI Agent 系统，定位为 **self-improving AI agent**（自我进化的 AI 智能体）。它是唯一内置闭环学习循环（closed learning loop）的 Agent 框架——能从每次任务中学习，自动创建技能文档，在使用中改进技能，并在会话间持久化记忆。

## 核心定位
> Hermes 的核心资产是**学习型执行循环**。它强调 self-improving agent、closed learning loop、自动创建和修补 skills、FTS5 会话搜索、Honcho 用户建模，以及六种执行后端。

## 安装与使用
- **CLI 命令行**：支持 uv 包管理一键安装
- **桌面版**：提供 GUI 图形界面
- **Web 界面**：内置 Web 管理面板
- **Android Termux**：支持移动端运行

## 会话管理
- **SQLite + FTS5**：数据库存储会话，支持跨会话全文搜索
- **上下文压缩**：自动压缩长上下文，支持 threshold/target_ratio/protect_last_n 配置
- **Session Search v0.15**：重建搜索索引，性能提升约 4500x

## 上下文文件系统
- **启动加载**：启动时自动加载 `.hermes.md` / `AGENTS.md` / `CLAUDE.md` / `SOUL.md` 等上下文文件
- **渐进加载**：按需逐步加载上下文，避免一次性消耗过多 Token
- **安全扫描**：对上下文文件进行安全扫描，防止提示词注入和凭证外泄

## 持久记忆系统
- **MEMORY.md / USER.md**：跨会话持久化记忆文件
- **8 种外部记忆提供商**：Honcho、Mem0、Hindsight、Holographic、OpenViking、Byterover、RetainDB、Supermemory

## 工具集
- **7 类工具**：Web/终端/浏览器/媒体/编排/记忆等
- **7 种终端后端**：支持多种终端模拟器
- **并行执行**：多工具并行调用
- **Smart Approvals**：智能审批，学习安全命令模式，自动放行可信操作

## MCP 协议集成
- **stdio/HTTP 传输**：支持标准输入输出和 HTTP 两种传输方式
- **Server Mode**：反向模式，允许外部连接 Hermes 的 MCP 服务
- **Nous-Approved 目录**：官方审核通过的 MCP 服务器清单

## 技能系统（SKILL）
- **166+ 已追踪技能**：来自 Skills Hub（agentskills.io）的丰富技能库
- **Skill Bundles**：技能包批量管理
- **Curator 维护系统**：技能自动维护与归档
- **条件激活**：根据工具可用性和操作系统平台自动筛选有效技能

## 扩展机制
- **Hooks 钩子系统**：Shell/Plugin/Gateway 三种类型，支持 pre_tool_call 等生命周期拦截
- **Plugins 插件系统**：基于 `__init__.py` + `plugin.yaml` 的扩展模块
- **Cron 定时任务**：自然语言调度，支持投递至 23+ 平台，No-Agent 模式（无需 LLM 推理）

## 消息网关（Gateway）
- **23+ 平台**：Telegram/微信/邮箱/Discord/Slack 等多平台消息接入
- **配对与权限控制**：细粒度的消息路由和权限管理

## 多实例管理
- **Profile 隔离**：独立 home 目录，通过命令别名管理多 Agent 实例
- **多 Agent 隔离**：不同 Profile 拥有独立的配置、记忆和工具集

## 多 Agent 协作
- **Delegation 任务委派**：单任务委派或并行批量委派，子 Agent 上下文可控
- **Kanban 多 Agent 集群协作**：三层架构（Dispatcher/Orchestrator/Worker），9 种状态流转（backlog/ready/in_progress/blocked/review/done/archived/failed/cancelled），6 种协作模式（fan-out/fan-in/pipeline/human-in-the-loop/stale-recovery/atomic-claim）
- **Mixture-of-Agents**：v0.18 一等公民特性，参考模型 + 聚合器模式，多模型协作推理，支持预设配置和推理过程可视化

## 技术栈
- **语言**：Python 3.11
- **后端**：uv 包管理，支持 venv 虚拟环境
- **搜索**：SQLite + FTS5 全文检索
- **安全**：安全扫描模块（防注入/防凭证外泄）
- **协议**：支持 OpenAI API 兼容格式，MCP 协议

## 关联连接
- [[NousResearch]] — Hermes 背后的团队
- [[OpenClaw]] — 通用 Agent 对标项目
- [[MCP]] — 模型上下文协议集成
- [[ClaudeCode]] — 终端 AI Agent（互补工具）
- [[Agent]] — AI Agent 核心概念
- [[context-compression]] — 上下文压缩机制
- [[persistent-memory]] — 跨会话持久记忆
- [[mixture-of-agents]] — 多模型协作模式
- [[kanban-swarm]] — 多 Agent 集群协作
- [[gateway-messaging]] — 消息网关架构
- [[task-delegation]] — 任务委派机制
- [[摘要-hermes-agent-complete-guide]] — Hermes Agent 完全指南来源
- [[摘要-HermesAgent小白入门指南]] — 小白入门指南来源
