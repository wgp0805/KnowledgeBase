---
title: "Harness Engineering"
type: concept
tags: ["Harness-Engineering", "AI-Agent"]
sources:
  - raw/01-articles/2026-09-07-对话OpenRouter CEO：Harness 正在取代超级 App，未来所有软件都只是 Agent 的后台工具.md
last_updated: 2026-09-08
---

# Harness Engineering

Harness Engineering 是为 LLM 搭建「外壳」的工程实践——工具注册、上下文管理、循环控制、错误恢复、安全边界。Harness 是 Agent 与 ChatBot 的分水岭：Claude Code 和 Codex 本质都是 Harness。2026 年模型能力趋同，Harness 成为差异化关键。

## Alex Atallah / OpenRouter CEO 视角（2026-09-07）
- **Harness 不会随模型变强而消失**：将成为模型之上的可组合工作界面，也是没有自研模型的创业公司掌握用户关系的重要一层
- **Harness vs App 的区别在于可组合性**：一个 Harness 可以调用另一个 Harness，也可以在云端沙箱里启动另一个 Harness
- **Harness 通常建立在 Unix 环境上**：模型对 Unix/bash 训练充分，比围绕复杂 App 做编排更可靠更确定
- **让 Agent 操作普通 App** 会遇到登录/密码/虚拟浏览器/寻找 API/阅读文档等未知问题；进入 Harness 则更容易检查内部发生了什么
- 模型变强后，系统提示词里塞进的大量杂物反而可能拖累表现；Anthropic 曾展示删掉部分系统提示词内容后模型矛盾变少、表现更好

## 关联连接
[[Claude-Code]], [[Codex]], [[LoopEngineering]], [[ContextEngineering]], [[沉默王二]], [[Harness]], [[AgentHarness]], [[AlexAtallah]], [[OpenRouter]], [[摘要-对话OpenRouter-CEO-Harness取代超级App]]
