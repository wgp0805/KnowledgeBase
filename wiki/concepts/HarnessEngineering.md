---
title: "Harness Engineering"
type: concept
tags: ["Harness-Engineering", "AI-Agent"]
sources:
  - raw/09-archive/2026-09-07-对话OpenRouter CEO：Harness 正在取代超级 App，未来所有软件都只是 Agent 的后台工具.md
  - raw/09-archive/2026-10-15-你的游戏本身就是 Harness ：如何让 AI Agent 读懂游戏并十倍加速迭代？ - leikooo.md
last_updated: 2026-10-15
---

# Harness Engineering

Harness Engineering 是为 LLM 搭建「外壳」的工程实践——工具注册、上下文管理、循环控制、错误恢复、安全边界。Harness 是 Agent 与 ChatBot 的分水岭：Claude Code 和 Codex 本质都是 Harness。2026 年模型能力趋同，Harness 成为差异化关键。

## Alex Atallah / OpenRouter CEO 视角（2026-09-07）
- **Harness 不会随模型变强而消失**：将成为模型之上的可组合工作界面，也是没有自研模型的创业公司掌握用户关系的重要一层
- **Harness vs App 的区别在于可组合性**：一个 Harness 可以调用另一个 Harness，也可以在云端沙箱里启动另一个 Harness
- **Harness 通常建立在 Unix 环境上**：模型对 Unix/bash 训练充分，比围绕复杂 App 做编排更可靠更确定
- **让 Agent 操作普通 App** 会遇到登录/密码/虚拟浏览器/寻找 API/阅读文档等未知问题；进入 Harness 则更容易检查内部发生了什么
- 模型变强后，系统提示词里塞进的大量杂物反而可能拖累表现；Anthropic 曾展示删掉部分系统提示词内容后模型矛盾变少、表现更好

## 领域定制 Harness：你的游戏本身就是 Harness（2026-10-15）

来自 [[摘要-你的游戏本身就是Harness]]（Kyle Kukshtel）。通用 Harness（Claude Code、Cursor）有一个致命短板：**它们根本无法与你的游戏内核对话**——游戏对它们是一个严密焊死的黑盒，模型唯一能看见的仅是代码编辑器里的文本字符。

文章的核心论断是：让 LLM 胜任游戏开发，**本质上是一个上下文工程问题**，而非游戏或 LLM 在先天基因上互斥。破解方式是把游戏里所有"暗物质"（状态、资源、物理、表现）转化为 LLM 能理解与操纵的具象载体，让游戏内部对模型处处透明、处处可寻址。具体落到七条工程原则上：

固定随机性（[[确定性]]）→ 截图 + [[图像差分]] → [[FatStruct]] 单一结构体 → [[命令模式]] → [[外部化数据管理]] → [[无头模拟内核]] → [[纯文本性能分析]]，最终串成 [[Agent迭代飞轮]]，把一次 Agent 迭代从数十分钟压缩到数秒。

这条路线与既有 Harness 讨论的关系：本页与 [[Harness]] 讲的是"围绕模型搭外壳"，而本文讲的是"**把被改造的对象本身改造成适合 Agent 作业的形态**"——后者是前者在垂直领域（游戏）的延伸，也是"领域定制 Harness"的典型样本。作者强调：即便完全抛开 AI，这些原则也是极佳的游戏工程实践。

## 关联连接
[[Claude-Code]], [[Codex]], [[LoopEngineering]], [[ContextEngineering]], [[沉默王二]], [[Harness]], [[AgentHarness]], [[AlexAtallah]], [[OpenRouter]], [[摘要-对话OpenRouter-CEO-Harness取代超级App]], [[摘要-你的游戏本身就是Harness]], [[Agent迭代飞轮]], [[确定性]], [[命令模式]], [[FatStruct]], [[无头模拟内核]], [[纯文本性能分析]], [[KyleKukshtel]]
