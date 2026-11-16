---
title: "摘要-cot思维链与deepseek-harness"
type: source
tags: [来源, CoT, 思维链, DeepSeekHarness, 推理]
sources: [raw/09-archive/2026-11-11 - 搞懂 CoT 思维链，你就掌控 DeepSeek Harness 的神。.md]
last_updated: 2026-11-16
---

## 核心摘要
二哥狗腿子 2026-11-11 的科普文，从 DeepSeek Harness 界面出发讲透 CoT 思维链的原理与工程实现。核心原理：大模型自回归逐 Token 输出，若要求第一个 Token 就是复杂数学题答案，等于要求在一个 Token 的计算量里完成多步推导——**思维链就是把上下文窗口当草稿纸，用更多输出 Token 换更多推理计算量**；中间步骤写入 KV Cache，生成最终答案时自注意力可读取这些中间结论。工程呈现：现代模型经后训练强化学习获得推理能力（先假设再验算、走不通推翻重来），DSH 在协议层把输出拆成 text 文本块与 reasoning 思考块两种独立内容，UI 上三层折叠（"已完成用时×秒"→"已完成分析"→"思考"）。推理深度控制：四档推理等级 Off/Low/High/Max（默认 High），Off 发 thinking:disabled。多轮与压缩时思考块的三种处理：①同模型多轮——思考块连同加密签名 signature 原样回传服务端（保证工具连续调用可见上一步推理 + KV Cache 前缀不变可复用），同时过滤 user/工具消息里的思考块；②中途切换模型——签名与生成模型绑定，换模型则丢弃签名只发思考内容避免报错；③上下文压缩——生成摘要的思考块直接丢弃，只有摘要正文进 `<compacted-summary>` 写入检查点。内容已并入 [[CoT]] 与 [[DeepSeekHarness]]。

## 关联连接
- [[CoT]] — 本篇主角概念（增量更新工程实现章节）
- [[DeepSeekHarness]] — 观察载体（增量更新）
- [[KV Cache]] — 思维链的物理载体
- [[上下文压缩]] — 第三种思考块处理场景
- [[LLM]] — 自回归生成原理
- [[思维链]] / [[ChainOfThought]] — 同域概念页
- [[ReAct]] — 相关推理范式
