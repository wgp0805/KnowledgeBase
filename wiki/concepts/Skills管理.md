---
title: "Skills管理"
type: concept
tags: [概念, Skills, 管理, 技术]
sources: [raw/01-articles/2026-09-01-DeepSeekHarness-MCP-Manager 一款DSH超好用的MCP管理跟Skills管理插件 - xxxyz.md]
last_updated: 2026-09-01
---

## 定义
对Agent Skills进行管理的功能，包括技能的浏览、搜索、启用、停用等操作。

## 关键信息
- 浏览/搜索：列出全部技能，按来源分组（项目级/运行时/自定义/用户级/内置/插件自带）
- 启用/停用：一键切换任意技能的启用状态
- 通过rank-0 override provider实现，任何来源层级都能禁用
- 持久化到dsh-skill-manager.json，重启后保留
- 改动经HMR即时生效

## 关联连接
- [[摘要-DeepSeekHarness-MCP-Manager插件]] — 来源文章
- [[DeepSeekHarness]] — 插件所属的Agent平台
- [[MCP管理]] — 插件的另一核心功能
- [[AgentSkills]] — 相关概念
