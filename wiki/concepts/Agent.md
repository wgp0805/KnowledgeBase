---
title: "Agent"
type: concept
tags: [AI, Agent, 自主系统]
sources: [raw/01-articles/40分钟学会Codex！"零基础"终级教程～【附完整文档】.md, raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/2026-06-29-AI native Casebook 面向 AI Agent 时代的测试用例工程化工作流 - 虫师.md, raw/01-articles/LangChain4j 和 LangGraph4j，哪个更好？.md, raw/01-articles/DeepSeek、Gemini、Qwen、Step 3.7 Flash实测，谁才是国产黑马？.md, raw/01-articles/Claude Code 最佳学习路线：从“手敲代码”到“指挥AI打工”，强的离谱！！.md]
last_updated: 2026-06-30
---

## 定义
能自主做计划、调用工具、看到结果后再决定下一步的 AI 程序，循环往复直到完成任务。与对话式 AI 一问一答不同，Agent 自主性强得多。

## 关键信息

### LLM Loop 机制
Agent 的核心运行机制是 LLM Loop：接收指令→制定计划→调用工具→观察结果→决定下一步→循环直到完成。

### Harness 工程
Harness 是大模型之外让 Agent 表现更好的设计总称。同样一个大模型，harness 不同效果差别极大。Claude Code 和 Codex 都是 harness 集大成者。

### 交互模式分类
不同 Agent 工具对交互模式有不同划分：
- **Claude Code**：Plan（给计划等确认）/ 默认模式（智能判断）/ 危险模式（一路绿灯）
- **DeepSeek TUI**：Plan（只读分析）/ Agent（任务执行需审批）/ YOLO（自动执行无需审批）
- 共性趋势：越来越注重让用户把控风险，同时保留完全自动化的选项

### 从"问 AI"到"管理 AI"
使用 Agent 需要范式转变：给它准备上下文和工作环境、指明任务目标、检查计划、监督过程、验收结果。工程师从执行者变为管理者。

### Agent 的扩展能力
- **Skill**：专业领域的操作手册/技能包
- **MCP**：外部服务转接头
- **SubAgent**：并行处理的子 agent
- **Hook**：条件反射式自动触发
- **CLI**：命令行工具扩展

## 关联连接
- [[Codex]] — OpenAI 的 Agent
- [[ClaudeCode]] — Anthropic 的 Agent
- [[DeepSeekTUI]] — 基于 DeepSeek V4 的开源 Agent
- [[AgentHarness]] — harness 设计
- [[Skill]] — 技能扩展
- [[MCP]] — 外部服务协议
- [[n8n-complete-guide]] — n8n 工作流自动化平台指南
- [[Casebook]] — AI Agent 维护测试用例资产的案例
- [[LangGraph4j]] — 多 Agent 工作流编排框架
- [[Step3Flash]] — Agent 执行层模型案例
- [[摘要-claude-code-learning-roadmap]] — Claude Code Agent 学习路线
