---
title: "摘要-OpenSpec规范驱动AI编程框架"
type: source
tags: [来源, 原始文件]
sources: [raw/01-articles/同事："Claude Code都能自动写代码了，还要什么Spec Coding？" 我反问："屎山代码你来维护？".md]
last_updated: 2026-06-24
---

## 核心摘要

OpenSpec 是一个面向 AI 编程的规范驱动框架，核心思想是"先对齐需求，再写代码"。每次功能变更会先生成提案、需求规格、技术设计和任务清单等规划文档，经人工确认后再让 AI 实现，让 AI 编程的结果更加符合预期。目前在 GitHub 上已有 53k+ star，提供了中文版本。

核心工作流包括四个阶段：探索模式（/opsx:explore）通过对话理清需求；提案模式（/opsx:propose）生成规划制品（proposal、specs、design、tasks）；应用模式（/opsx:apply）按清单逐项实现生成代码；归档模式（/opsx:archive）完成后将规划文档移入 archive 目录。

## 关联连接

- [[OpenSpec]] — 核心框架实体
- [[AICoding]] — AI 辅助编程范式
- [[OpenCode]] — 支持 OpenSpec 的编程工具
- [[Skill]] — 技能扩展机制
- [[ClaudeCode]] — AI 编程工具
