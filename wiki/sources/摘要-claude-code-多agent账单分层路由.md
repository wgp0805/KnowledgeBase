---
title: "摘要-claude-code-多agent账单分层路由"
type: source
tags: [来源, 原始文件]
sources: [raw/01-articles/2026-09-23-开多个 Agent 后 Claude Code 账单翻了 4 倍，一个配置解决了 - 码哥字节.md]
last_updated: 2026-09-28
---

# 摘要-claude-code-多agent账单分层路由

## 核心摘要

Claude Code 的多 Agent 不是手动启动的，而是它自动决策拆分的：一次任务会开出 3-5 个独立子 Agent，每个实例有自己的上下文与计费，账单可达单 Agent 的 3-5 倍。文章的解法是重指 Claude Code 内部「模型级别 → 实际模型」的路由层：通过 `ANTHROPIC_BASE_URL` 指向 DeepSeek 的 Anthropic 兼容端点，主 Agent（Opus/Sonnet 级）绑定 `deepseek-v4-pro[1m]`，子 Agent（Haiku 级）用 `ANTHROPIC_DEFAULT_HAIKU_MODEL` 与 `CLAUDE_CODE_SUBAGENT_MODEL` 显式绑定 `deepseek-v4-flash`。实测同一 240 万 token 的 Spring Boot 重构任务，全用 Sonnet 4.6 需 $22.4，分层路由折扣后仅 $1.29（约为前者的 1/17）。文中记录 5 个坑：兼容端点不支持图片输入、模型名写错会静默 fallback 到 Flash、`[1m]` 不加只有 200K 上下文、Agent YAML 的 `model` 字段区分大小写、base URL 末尾不能加 `/v1`。

## 关联连接
- [[ClaudeCode]] — 配置所针对的 AI 编程 Agent
- [[Claude-Code]] — 实体存根
- [[模型路由]] — 该文实践的分层路由概念
- [[Subagent]] — 账单翻倍的根源：自动创建的子 Agent
- [[DeepSeek]] — 提供 Anthropic 兼容端点的模型方
- [[码哥字节]] — 文章作者
- [[摘要-claude-code-deepseek-v4-agent]] — 相关：Claude Code + DeepSeek V4 组合评测
