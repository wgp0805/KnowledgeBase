---
title: "摘要-agent-permission-mode深度解析"
type: source
tags: [Agent, 权限模式, ClaudeCode, 安全, 沙箱, 面试题]
sources: ["raw/09-archive/Agent 的权限模式（Permission Mode）了解吗？.md"]
last_updated: 2026-10-15
---

## 核心摘要

沉默王二以面试题形式深度解析 Agent 的权限模式（Permission Mode）：权限模式决定 Agent 动手之前问不问人，弹窗只是其中一种结果。DeepSeek Harness 有三种权限模式（仅查看/工作区内修改/完全权限）；Claude Code 有六种（Manual/acceptEdits/plan/auto/dontAsk/bypassPermissions），2.1.284 起交互会话默认 auto。auto 模式由跑在 Sonnet 5 上的分类器审查每个动作：能看到用户消息、工具调用和 CLAUDE.md，但剔除工具结果（防网页/文件恶意指令）与 Claude 自己的输出（防说服分类器）；先输出单 token 快速判断，可疑再用思维链复核；连续拦截 3 次或累计 20 次则退回人工弹窗；正常操作误拦率 0.4%、越权放行率 17%（官方称 "the honest number"）。安全底线是 deny 规则 + 沙箱：权限规则分 allow/ask/deny，先 deny 再 ask 后 allow，deny 在任何模式（含 bypassPermissions）下都生效；命令跑起来后靠操作系统沙箱限制文件与网络。Pi（MarioZechner）则没有内置权限系统，官方主张真正的边界是资源访问限制，推荐容器/VM/沙箱运行，审批需求用 permission-gate.ts 扩展自行实现。

## 关联连接
- [[权限模式]] — 提炼的核心概念
- [[ClaudeCode]] — 六种权限模式与 auto 分类器实现
- [[auto-mode]] — auto 模式的增量细节
- [[DeepSeekHarness]] — 三种权限模式
- [[Pi]] — 无内置权限系统的反面立场
- [[沙箱]] — 权限模式之外的真正安全边界
- [[沉默王二]] — 作者
- [[YOLO模式]] / [[安全剧场]] — 相关的安全立场概念
