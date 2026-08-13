---
title: "摘要-loop-vs-prompt-engineering"
type: source
tags: [Loop Engineering, Prompt Engineering, Context Engineering, Harness Engineering, AI Agent, 方法论]
sources: [raw/01-articles/面试官坏笑：“本周我们只要 Loop Engineering 不要 Prompt Engineering 了。”我：“不就是 loop goal，谁不会啊！”.md]
last_updated: 2026-08-13
---

## 核心摘要
沉默王二从面试辨析角度梳理了 AI 工程范式演进：Prompt Engineering（写好单次输入）→ Context Engineering（管好上下文窗口）→ Harness Engineering（设计 Agent 执行框架）→ Loop Engineering（让框架自己转起来）。Loop 站在 Harness 之上，核心不是"再写一句 Prompt"，而是用一套复杂提示词让 Agent 在循环中自找信息、自验结果、自调方案，直到完成目标。

文章提出 Loop 的六大组件技术栈——**定时任务、Worktree、Skill、MCP、Sub-agent、Memory**，缺一不可：定时任务（Claude Code `/loop`）触发 Agent 会话而非确定性脚本；Worktree 提供多 Agent 并行的文件隔离；Skill 持久化项目工作规范；MCP 连接外部系统（GitHub/飞书等）；Sub-agent 实现 maker-checker 写查分离；Memory 让 loop 跨轮次积累经验。

实战部分用 `/loop 30m` 自动回复 PaiAgent 仓库未答 issue 的案例，拆解了"心跳频率 + 任务描述 + 防重机制"的提示词结构，并对照六大组件说明哪些场景用到哪些组件。文末点出 Loop 的三大代价：Token 消耗（需熔断与最大迭代次数）、安全边界（凌晨自动推生产代码的风险）、场景适配（仅适合高频重复、规则明确、有自动化验证手段的场景，如代码审查/CI 修复/文档同步/依赖升级/安全扫描）。

## 关联连接
- [[LoopEngineering]] — 循环工程方法论，本文是其面试辨析视角的来源之一
- [[摘要-loop-engineering-guide]] — Loop Engineering 实战指南（三文件/三级循环/Skill 体系）
- [[摘要-loop-engineering-pitfalls]] — 生产级 Loop 五大坑与可观测性补平方案
- [[ContextEngineering]] — 范式演进的上一环：管好上下文窗口
- [[Harness]] — Loop 之下的执行框架基础设施
- [[Skill]] — Loop 六大组件之一，工作规范持久化
- [[MCP]] — Loop 六大组件之一，外部系统连接器
- [[Worktree]] — Loop 六大组件之一，多 Agent 文件隔离
- [[subagent-driven-development]] — Sub-agent maker-checker 模式
- [[AutoMemory]] — Loop 跨轮次记忆机制
- [[ClaudeCode]] — `/loop` 命令的宿主平台
- [[PiAgent]] — 文章实战案例中被自动回复 issue 的仓库
