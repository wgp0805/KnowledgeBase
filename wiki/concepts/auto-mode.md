---
title: "auto-mode"
type: concept
tags: [AI编程, 权限, Claude Code, 安全]
sources:
  - raw/01-articles/面试官坏笑：“你用ClaudeCode写代码，不怕它把项目搞炸？”，我：“怕，所以CLAUDE.md、权限和验证，一个都不能少。”.md
last_updated: 2026-07-09
---

## 定义

Auto Mode 是 [[ClaudeCode]] 的权限自动模式，用独立分类器判断操作风险：低风险自动放行，高风险（下载执行陌生代码、发送敏感内容、生产部署、强推、直接 push 到 main）阻断或转人工确认。它解决的是"少点确认"，不负责隔离文件系统、网络和凭据。

## 关键信息

- 切换：CLI 中 Shift+Tab 切换权限模式；需账号/模型/provider/组织设置均满足才出现 auto
- 不提供安全沙箱，高风险任务仍需容器、临时账号、最小权限、deny 规则、[[Hooks]] 和人工 Review
- v2.1.142+ 忽略项目级 .claude/settings.json 中的 auto 设置，防止仓库自启 Auto Mode；应放用户级或组织 managed settings
- Bedrock/Vertex AI/Microsoft Foundry 等 provider 需额外设 CLAUDE_CODE_ENABLE_AUTO_MODE=1
- `--dangerously-skip-permissions` 不建议日常使用，除非文件系统/网络/凭据已隔离

## 关联连接

- [[ClaudeCode]] - 所属工具
- [[CLAUDEmd]] - 配合的项目规范
- [[Hooks]] - deny 规则的补充拦截
- [[code-review]] - 安全审查实践
- [[摘要-claude-code-实战防搞炸]] - 来源
