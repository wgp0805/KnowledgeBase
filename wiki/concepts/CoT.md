---
title: "CoT"
type: concept
tags: [概念, 提示工程, 推理, 思维链]
sources: [raw/09-archive/2026-09-20 - 万字详解 10 道 AI Agent 高频面试题.md, raw/09-archive/2026-11-11 - 搞懂 CoT 思维链，你就掌控 DeepSeek Harness 的神。.md]
last_updated: 2026-11-16
---

## 定义
CoT（Chain of Thought，思维链）是让模型在回答前先展示中间推理步骤的提示技术，通过引导模型"想清楚再答"提升复杂推理任务的准确率。

## 关键信息
- **核心思想**：把隐式的推理过程显式化，让模型逐步推导而非直接给答案
- **底层原理（2026-11-11，详见 [[摘要-cot思维链与deepseek-harness]]）**：大模型自回归逐 Token 输出，每生成一个 Token 经过的 Transformer 层数与矩阵运算量固定——要求第一个 Token 就是复杂数学题答案，等于要求在一个 Token 的计算量里完成多步推导，必然出错。**思维链就是把上下文窗口当草稿纸：先逐字输出中间推理步骤（进入上下文窗口、K/V 向量存入 KV Cache），生成最终答案时自注意力读取这些中间结论——用更多输出 Token 换更多推理计算量**。代价是草稿越多 Token 消耗越大
- **提示词时代 vs 后训练时代**：早期模型需在提示词末尾加"让我们一步步思考"引导，推导与答案混在一起；现在模型经后训练强化学习获得推理能力，会先提出假设再验算、走不通推翻重来，推理过程由协议层独立传递
- **与 ReAct 关系**：CoT 管"想"，ReAct 在 CoT 基础上加"做"（行动）
- **与 Plan-and-Execute 关系**：CoT 是单步推理，Plan-and-Execute 先想全局再执行
- **与 Self-Refine 关系**：CoT 是推理前引导，Self-Refine 是推理后审查
- **选型**：CoT 管想、ReAct 加做、Plan 先想全局、Refine 做完再审，生产环境混着用

### 在 DeepSeek Harness 中的工程实现（2026-11-11）
- **协议层拆分**：输出拆成 `text` 文本块与 `reasoning` 思考块两种独立内容；UI 三层折叠（"已完成，用时×秒"→"已完成分析"→"思考"）
- **推理等级四档**：`Off` / `Low` / `High` / `Max`（默认 High）；Low~Max 发 `thinking: enabled` 并经 `output_config` 传等级，Off 发 `thinking: disabled`
- **多轮对话的思考块处理**：服务端流式返回思考块时附加密签名 signature，客户端拼完整签名；下一轮请求把 assistant 思考块**连同签名原样回传**（①连续工具调用时模型可见上一步推理；②历史消息 Token 序列不变，服务端可复用已缓存的 KV Cache），同时过滤 user 消息与工具返回里的思考块
- **跨模型切换**：签名与生成模型绑定，换模型（如 v4-pro → flash）签名过不了校验——组装请求前检查消息来源模型，不一致则丢弃签名只发思考内容，避免接口报错
- **上下文压缩**：把较早历史发给模型生成摘要，该次调用返回的思考块直接丢弃，只有摘要正文进 `<compacted-summary>` 标签写入检查点——生成摘要的思考不占后续上下文

## 关联连接
- [[摘要-10道ai-agent高频面试题]] — 来源
- [[摘要-cot思维链与deepseek-harness]] — 来源（底层原理与 DeepSeek Harness 工程实现）
- [[DeepSeekHarness]] — 工程实现载体（reasoning 块/签名回传/推理等级）
- [[KVCache]] — 思维链的物理载体（中间结论存 K/V 向量）
- [[上下文压缩]] — 思考块丢弃场景
- [[LLM]] — 自回归生成原理
- [[思维链]] — 同义概念页
- [[ChainOfThought]] — 同域概念页
- [[ReAct]] — 加"做"的范式
- [[Plan-and-Execute]] — 先想全局的范式
- [[Self-Refine]] — 做完再审的范式
- [[Agent]] — 应用场景