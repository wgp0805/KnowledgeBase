---
title: "摘要-claude-code-hooks-防危险命令"
type: source
tags: [来源, ClaudeCode, Hooks, 安全, 程序汪]
sources: [raw/01-articles/2026-08-28 - 面试官坏笑：“你都用ClaudeCode写代码半年了，怎么保证它不会执行危险命令？”，我：“CLAUDE.md”，面试官：“回去等通知吧！”.md]
last_updated: 2026-08-28
---

## 核心摘要

程序汪基于 Claude Code 官方文档 Hooks reference 的实战教程，回答面试题"怎么保证 Claude Code 不会执行危险命令"。核心论点：**Prompt 约束（CLAUDE.md）无法保证每次生效，必须用 Hooks 在生命周期节点上做强制检查**。文章系统讲解 Hooks 的五类 handler（command/http/mcp_tool/prompt/agent）、常用生命周期事件（SessionStart/UserPromptSubmit/PreToolUse/PermissionRequest/PostToolUse/Notification/Stop/PreCompact/PostCompact）、输入输出契约（stdin JSON、退出码 0/1/2 语义、stdout JSON 纪律）、多 Hook 并行合并规则，并给出三个最小可用示例（Notification 通知、PostToolUse 自动格式化、PreToolUse 拦截危险命令和敏感文件）及排查清单。最后澄清 Hooks 与 Skills 的分工：能写成确定脚本的规则交 Hooks，需要结合上下文判断的复杂流程交 Skills。

## 关键信息

- **面试题答案**：CLAUDE.md 只是 Prompt 提醒，依赖上下文和模型记忆，无法保证每次生效；Hooks 才是把"禁止 rm -rf""改完格式化""不碰 .env"变成可审计、可阻断硬约束的正确手段
- **Handler 选型原则**：优先 `command`（可独立调试、易纳入代码审查）→ 团队审计用 `http` → 复用 MCP 用 `mcp_tool` → 语义判断才用 `prompt`/`agent`（后者仍 experimental）
- **退出码语义**：`exit 0` + JSON stdout = 精细决策；`exit 2` = 阻断（PermissionRequest 例外）；`exit 1` 是最易踩坑——对多数事件只是非阻断错误，流程继续
- **三个最小示例**：Notification（低风险先配）→ PostToolUse 格式化（自动化收益）→ PreToolUse 拦截（安全底线）
- **安全边界**：命令黑名单只能识别已知形式，`/bin/rm`、`find -delete` 等变体可绕过；必须路径限制+权限配置+Hooks+Sandbox+CI+人工 Review 多重防护
- **排查顺序**：`/hooks` 确认加载 → 脚本单独运行测试退出码 → 记录实际事件数据 → 一次只启用一个 Hook
- **Hooks vs Skills**：Hooks 生命周期自动触发、适合固定动作和硬阻断；Skills 按需加载、适合复杂流程；两者可接同一条工作流

## 关联连接
- [[Hooks]] — 核心概念（本来源已覆盖旧描述）
- [[ClaudeCode]] — Hooks 运行平台
- [[程序汪]] — 作者
- [[Skill]] — 与 Hooks 并列的扩展机制
- [[CLAUDEmd]] — Prompt 约束载体（软约束 vs 硬约束对比）
- [[PreToolUse]] — 安全拦截核心事件
- [[PostToolUse]] — 格式化收尾事件
- [[PermissionRequest]] — 权限决定事件
- [[SessionStart]] — 会话开始事件
- [[Stop]] — 响应停止事件
- [[PreCompact]] — 上下文压缩前事件
