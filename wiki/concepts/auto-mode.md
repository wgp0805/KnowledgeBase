---
title: "auto-mode"
type: concept
tags: [AI编程, 权限, Claude Code, 安全]
sources:
  - raw/09-archive/面试官坏笑：“你用ClaudeCode写代码，不怕它把项目搞炸？”，我：“怕，所以CLAUDE.md、权限和验证，一个都不能少。”.md
  - raw/01-articles/Agent 的权限模式（Permission Mode）了解吗？.md
last_updated: 2026-10-15
---

## 定义

Auto Mode 是 [[ClaudeCode]] 的权限自动模式，用独立分类器判断操作风险：低风险自动放行，高风险（下载执行陌生代码、发送敏感内容、生产部署、强推、直接 push 到 main）阻断或转人工确认。它解决的是"少点确认"，不负责隔离文件系统、网络和凭据。

## 关键信息

- 切换：CLI 中 Shift+Tab 切换权限模式；需账号/模型/provider/组织设置均满足才出现 auto
- 不提供安全沙箱，高风险任务仍需容器、临时账号、最小权限、deny 规则、[[Hooks]] 和人工 Review
- v2.1.142+ 忽略项目级 .claude/settings.json 中的 auto 设置，防止仓库自启 Auto Mode；应放用户级或组织 managed settings
- Bedrock/Vertex AI/Microsoft Foundry 等 provider 需额外设 CLAUDE_CODE_ENABLE_AUTO_MODE=1
- `--dangerously-skip-permissions` 不建议日常使用，除非文件系统/网络/凭据已隔离
- **分类器内部机制（2.1.210+，2026-10-14 补充）**：分类器默认跑在 Sonnet 5（不随 /model 变）；输入含用户消息、工具调用、CLAUDE.md，**剔除工具结果**（防网页/文件恶意指令）与 **Claude 自己的输出**（防说服分类器放行）；先输出单 token 快速判断，可疑再用思维链复核；连续拦截 3 次或累计 20 次自动暂停退回人工弹窗；正常操作误拦率 0.4%、越权放行率 17%（官方 "the honest number"）。详见 [[权限模式]]
- 2.1.284 起未手动配置权限模式时，终端交互会话默认进入 auto

## 关联连接

- [[ClaudeCode]] - 所属工具
- [[CLAUDEmd]] - 配合的项目规范
- [[Hooks]] - deny 规则的补充拦截
- [[权限模式]] - 权限模式总概念
- [[code-review]] - 安全审查实践
- [[摘要-claude-code-实战防搞炸]] - 来源
- [[摘要-agent-permission-mode深度解析]] - 2026-10-14 分类器内部机制来源
