---
title: "摘要-agent-hallucination-governance"
type: source
tags: [来源, Agent, 幻觉, 可靠性, 治理]
sources: [raw/01-articles/2026-10-10 - Agent 出现幻觉怎么治理？.md]
last_updated: 2026-10-12
---

## 核心摘要
文章从面试题切入，指出幻觉源头虽在模型，但一旦进入 Agent 执行流程就"从说错变成做错"，表现为错误的工具调用、错误的上下文压缩、错误的长期记忆检索；引用 2025 年 9 月中科院信息工程所等十几家机构的论文《LLM-based Agents Suffer from Hallucinations》，将 Agent 幻觉按发生阶段分为推理、执行、感知、记忆、通信五类。治理思路只有一条：**让 Agent 执行的每一步都去真实环境核对一遍，把错误当作工具结果交还给模型让它自己改正**——工具不存在/参数校验失败要报错回灌（Pi 的 TypeBox 校验、isError 标记）、文件编辑必须匹配磁盘上的原文（Claude Code 的 old_string 精确唯一匹配、Codex 的 apply_patch 报错、Pi 每次从磁盘重读）。记忆分两类治理：压缩时用代码从工具调用记录中提取文件清单而非让模型总结（Pi）、压缩后从磁盘重读文件与 CLAUDE.md（Claude Code）；长期记忆则标注写入时间并遵循"Memory is not proof of current behavior"。执行幻觉用确定性检查（Stop hook 跑测试不过就 block，最多 8 次）与"验证的人不能是干活的人"（全新上下文的 Sub-agent 审查 diff）解决；多 Agent 协作时下游会把上游幻觉当事实（通信幻觉），传递结论必须附证据（文件路径、行号、原始输出）。

## 关联连接
- [[Agent幻觉]] — 本文整理的五类分类与治理框架
- [[幻觉]] — 上位概念：模型幻觉
- [[AI幻觉]] — 相邻概念
- [[Tool幻觉]] — 五类中的工具调用侧表现
- [[ClaudeCode]] — old_string 校验、Stop hook、压缩后重读、Sub-agent 审查
- [[Codex]] — apply_patch 原文匹配、记忆提示词原则
- [[PiAgent]] / [[ArminRonacher]] — TypeBox 参数校验、错误回灌、磁盘重读
- [[AgentHarness]] — 文中引用的 Harness 五要素（Evaluation 只认客观物证）
- [[Subagent]] — 全新上下文的审查者模式
- [[Hooks]] — Stop hook 确定性检查
- [[error-feedback-self-healing]] — 错误回灌自愈机制
- [[RAG]] — 面试回答中被否定的常见方案之一
- [[零幻觉]] — 相邻的治理目标概念
