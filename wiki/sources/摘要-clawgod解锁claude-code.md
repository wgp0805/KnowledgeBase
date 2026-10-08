---
title: "摘要-clawgod解锁claude-code"
type: source
tags: [来源, 原始文件, ClaudeCode, 开源工具, 权限]
sources: [raw/01-articles/2026-10-01-一行命令，解锁 Claude Code 全部权限-ClawGod - 绝不原创的飞龙.md]
last_updated: 2026-10-08
---

## 核心摘要
ClawGod 是开源（GPL-3.0）的 Claude Code 本地补丁工具，一行命令安装（约 30 秒，保留 claude.orig 原版备份、可一键卸载），把官方关闭的功能全部打开：①模型解锁——伪装用户类型 external→ant（Anthropic 内部），让订阅等级不再限制模型，专业版即可用 Opus 4.6 + 1M 上下文；②Agent Teams 多智能体协作客户端解锁（移除条件检查强制开启）；③删除三条内部限制指令——CYBER_RISK_INSTRUCTION（安全研究话题拒答）、URL 生成限制、操作审慎指令（破坏性操作强确认）；④通过 CLAUDE_INTERNAL_FC_OVERRIDES 注入本地 JSON 覆盖 GrowthBook 远程功能开关；⑤自定义 API 地址/模型（支持代理、中转、兼容 API）。作者强调它不动账号、不绕服务端限流，只改本地客户端行为；补丁生效后终端主题变绿色（原版橙色）。风险提示：安全研究解禁与确认框移除会放大 prompt 注入与误操作风险，且属于第三方非官方修改。

## 关联连接
- [[ClawGod]] — 文章介绍的补丁工具
- [[ClaudeCode]] — 被修改的目标工具
- [[Anthropic]] — 官方厂商
