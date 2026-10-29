---
title: "code_mode_only"
type: concept
tags: [Agent, Codex, 工具调用, V8沙箱, OpenAI]
sources: [raw/09-archive/GPT-6.1 Terra 发布！扒完 Codex 最新源码，我发现了 OpenAI 藏起来的三个大招.md]
last_updated: 2026-10-28
---

## 定义

code_mode_only 是 Codex 为 [[GPT-6.1-Terra]] 默认开启的**纯代码执行模式**：把传统"一次调用一个工具"的 JSON 往返模式，变成 V8 沙箱里的**并发脚本编程**。模型不再逐个调工具，而是写一段 JavaScript 交给沙箱执行，在代码内部并发完成多步操作。

## 关键信息

### 传统模式的问题（JSON 往返）

- 排查问题需要十次只读操作 → 与大模型来回交互十轮
- 每一轮都要把前面历史上下文重新发一遍：**慢 + 上下文窗口被塞满**

### code_mode_only 的解法

1. **工具隐藏**：把零散工具全部隐藏，只向模型暴露一个运行在独立 V8 沙箱里的 `exec` 工具
2. **全局挂载**：文件读写、终端命令、外部 MCP 插件全部挂载到沙箱全局 `tools` 对象
3. **延迟加载（Tool Search）**：几十个工具签名塞进初始提示词会浪费上下文 → Terra 先调 `tool_search`，底层用 **BM25 实时检索**当前需要的工具并取 TypeScript 签名
4. **并发执行**：拿到签名后在同一段 JS 里用 `Promise.allSettled` 把多个互不依赖的文件搜索、代码读取**一次性并发完成**

### 效果

- Terra 执行任务比 Sol/Astra 快 **3 倍以上**（第一变化）
- 对比意义：工具调用范式从"串行 JSON 往返"演进为"沙箱内并发脚本"

## 关联连接
- [[摘要-gpt6.1-terra-codex三招]] — 来源
- [[GPT-6.1-Terra]] — 默认开启此模式的模型
- [[Codex]] — 实现此模式的 Agent 客户端
- [[ToolSearch]] — tool_search 延迟加载机制（BM25 检索工具签名）
- [[BM25]] — 底层检索算法
- [[沙箱]] — V8 沙箱执行环境
- [[思考强度]] — 同篇源码中的隐藏 ultra 档位
- [[ContextWindow]] — 上下文窗口（本文档解决窗口被塞满问题）
- [[沉默王二]] — 作者
