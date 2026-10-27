---
title: "摘要-codex-computer-use原理"
type: source
tags: [来源, 原始文件, Codex, ComputerUse, Agent, 安全]
sources: [raw/09-archive/说说 Codex 的 Computer Use 原理。.md]
last_updated: 2026-10-26
---

## 核心摘要

沉默王二从 Codex 源码层面拆解 Computer Use 的底层实现。核心观点：Computer Use 不是给模型暴露 `click`/`type` 原子工具，而是内置 `cua_repl` MCP 插件暴露一个 `js` 工具，让模型直接写 JavaScript 调用全局 `cua` 对象，在持久化 Node.js REPL 里编排整个桌面动作串——一次调用执行完一串操作，省掉逐动作推理与高清截图重传，同时保护 KV Cache（系统提示词不塞接口文档，写错方法名报 Script error 时才拼接 API 文档）。安全侧三板斧：①按操作系统原生标识做应用黑白名单（macOS 绑 bundle_ids、Windows 绑 aumids + 签名）；②四级敏感动作确认策略，脚本运行中途通过 `elicitation/create` 实时挂起高危动作（普通点击静默放行）；③Guardian 安全围栏防屏幕内容提示注入——截图存入 8M 证据缓冲区打"不可信证据"标签，Guardian V2 自适应模式配合 LunaSampler 后台异步风险打分，低风险快速放行、高风险切同步阻塞审查。

## 关联连接

- [[ComputerUse]] — 主题概念（已并入"Codex 底层实现原理"章节）
- [[Codex]] — 实现主体
- [[BrowserUse]] — 对照物：网页靠无障碍树编号，桌面靠屏幕画面 + 系统状态
- [[DeepSeekHarness]] — 文章演示中被 Codex 接管操控的桌面 Agent
- [[PromptInjection]] — 屏幕恶意内容劫持风险的本质
- [[KV Cache]] — 设计取舍的两大动因之一（延迟/Token 消耗之外）
- [[MCP]] — cua_repl 的插件暴露协议与 elicitation 审批通道
- [[Node.js]] — cua_repl 的持久化 REPL 运行环境
- [[HITL]] — 敏感动作移交用户确认的人机协同本质
- [[沉默王二]] — 来源作者
