---
title: "Hooks"
type: concept
tags: [Agent扩展, 自动化, 防护机制]
sources: [raw/01-articles/Anthropic 工程师总结的 9 条血泪经验.md]
last_updated: 2026-05-28
---

## 定义
Claude Code 的一种扩展机制，指在特定条件下自动触发的防护或操作流程，只在 Skill 被调用时生效，会话结束就消失。

## 关键信息
- 激活条件：只在 Skill 被调用时生效
- 生命周期：会话结束就消失
- 适用场景：场景化防护，如禁止危险命令、限制文件修改范围
- 示例：
  - `/careful`：禁止 `rm -rf`、`DROP TABLE`、强制推送等
  - `/freeze`：限制只能在特定目录下修改文件

## 关联连接
- [[Skill]] — Hooks 可以内嵌在 Skill 中
- [[ClaudeCode]] — Hooks 的运行平台
- [[摘要-anthropic-engineer-skills]] — 来源