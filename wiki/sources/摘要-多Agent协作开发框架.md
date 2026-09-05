---
title: "摘要-多Agent协作开发框架"
type: source
tags: [AI, Agent, 协作模式, 角色隔离, 代码评审]
sources: [raw/09-archive/multi-agent-collaboration.md]
last_updated: 2026-08-06
---

## 核心摘要

本文提出了一套通用的多 Agent 协作开发框架，解决多 AI agent 分工开发时的三个核心痛点：角色越界、靠对话记忆协作、同源模型互相包容。框架定义了三个角色（Planner/Coder/Reviewer），通过文件显式交接、工具白名单物理隔离、对抗性 prompt 评审机制来实现闭环协作。提供跨工具协作（如 Claude Code + Codex）和单工具多子 agent 两套可照搬方案，并在防"互相包容"问题上给出了从客观验收闸门到异构模型的六层防御体系。

## 关联连接

- [[multi-agent-collaboration]] — 多 Agent 协作模式（Skill 驱动 + 三角色框架）
- [[role-isolation]] — 角色隔离机制（工具白名单 + 硬约束）
- [[adversarial-review]] — 对抗性评审
- [[subagent-driven-development]] — 子代理驱动开发
- [[Agent工作流编排]] — 相关工作流编排