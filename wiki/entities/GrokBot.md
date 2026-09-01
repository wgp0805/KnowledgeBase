---
title: "GrokBot"
type: entity
tags: [AI产品, Agent, xAI]
sources: [raw/01-articles/2026-08-26-Claude Code 与 Grok Bot 被拆开后：AI Agent 真正难复制的是什么？.md]
last_updated: 2026-08-27
---

## 定义
Grok Bot 是 2026 年 8 月 11 日以 Early Beta 形式推出的 AI Agent 产品，定位为长期在线的 AI 同事，能在云电脑中登录工具和应用、执行跨系统任务，并在用户离开后继续工作。

## 关键信息
- **发布**：2026-08-11 Early Beta
- **定位**：长期在线的 AI 同事，云电脑中登录工具和应用，执行跨系统任务
- **核心能力**：Skill、Routine、审批、共享电脑
- **共享电脑架构**：一名用户创建的所有 Bot 实际共享一台持久化云电脑，文件/浏览器登录状态/命令行凭证可在 Bot 之间使用，不应当成彼此隔离的安全边界
- **运行层重建事件**：外部开发者依据 0.18.0 客户端 Source Map 重建运行层，新增 Claude Code/Codex/OpenRouter 路由和本地 Docker 沙箱
- **官方建议**：先完成一次任务使流程可靠 → 保存为 Skill → 设置为定时/事件触发的 Routine；重试应保持幂等，数据缺失和部分完成要明确报告
- **企业能力**：团队身份、MCP 策略、共享规则、费用查看、云电脑管理（截至 2026-08-25 仍在逐步推出，Bot 行为审计视图即将推出，尚未提供专属支出上限）
- **审批原则**：审批只能控制即将执行的动作，不能反转已完成的工作；Auto Review 属于模型驱动辅助判断，不能替代最小权限和明确边界

## 关联连接
- [[摘要-Claude-Code与Grok-Bot被拆开后]] — 来源
- [[ClaudeCode]] — 同期被拆开的对标产品
- [[SourceMap]] — 运行层重建的技术载体
- [[TaskDelegationSystem]] — 分析其产品能力的框架
- [[OpenRouter]] — 重建项目新增路由
- [[Codex]] — 重建项目新增路由
- [[Docker]] — 重建项目可选沙箱
- [[Skills]] — 核心能力
- [[Hooks]] — 对比 Claude Code 的确定性护栏
- [[MCP]] — 企业策略
- [[AutoMemory]] — 对比 Claude Code 的记忆能力
- [[Checkpoint]] — 对比 Claude Code 的恢复能力
- [[Subagent]] — 对比 Claude Code 的子 Agent
