---
title: "摘要-codex-vs-claude-code-对比"
type: source
tags: [来源, 原始文件, AI编程, 工具对比]
sources: [raw/01-articles/Codex 和 Claude Code，到底哪个更好？.md]
last_updated: 2026-06-29
---

## 核心摘要
苏三《Codex 和 Claude Code，到底哪个更好？》系统对比 2026 年 6 月两大终端 AI 编程 Agent 的差异：本质区别不在底层模型（Claude 4 vs GPT-5.5），而在 **Harness 架构**——Codex 采用云端沙箱+并行子 Agent（最多 8 个）的"委派式"哲学，Claude Code 采用本地执行+协作子 Agent 的"并肩作战"哲学。基准测试方面：Claude Code 在 SWE-bench Pro 领先 5.7 个百分点，Codex 在 Terminal-Bench 2.0 大幅领先 13.3 个百分点；Codex Token 效率约为 Claude Code 的 3 倍（构建 Figma 插件：150 万 vs 620 万）。功能演进上 24 项共有功能中 18 项由 Claude Code 先发，Codex 先发 4 项（沙箱、云端异步、并行团队、Goal mode）。结论：两者非"谁更强"而是"谁更适合工作方式"——Codex 像"项目经理"派任务等结果，Claude Code 像"结对编程的资深工程师"。

## 关联连接
- [[ClaudeCode]] — 对比主角 A
- [[Codex]] — 对比主角 B
- [[HarnessAgent]] — 核心架构差异
- [[AICoding]] — 所属范式
- [[Anthropic]] — Claude Code 厂商
- [[OpenAI]] — Codex 厂商
- [[子Agent编排]] — 两者均依赖
- [[跨模型工作流]] — 两者组合使用范式
