---
title: "摘要-spring-ai-2-1-苏三解读"
type: source
tags: [来源, SpringAI, Java, Agent, HITL]
sources: ["raw/09-archive/夯爆了，Spring AI 2.1 正式发布！.md"]
last_updated: 2026-11-27
---

## 核心摘要

[[苏三]] 2026-11-27 解读 Spring AI 2.1.0（文中明确 **2026 年 11 月 19 日正式发布**，距 2.0 GA 约半年）。与 [[摘要-spring-ai-2-1发布]]（[[锋哥]] 版，按特性清单逐条铺开）不同，苏三这篇的组织方式是**「先讲痛点再讲机制」**，围绕一个核心问题展开：**模型调用工具，到底该不该无条件信任？**

**引子场景**：智能客服 Agent 能查订单、改地址、发起退款，测试一切正常，上线后模型「心情不好」把不该退的款退了——日志显示工具调用和参数都对，就是判断错了。这不是模型笨，是**框架层缺少一道人工确认的闸门**。2.1 把这闸门做成了正式能力。

### 一、Tool Call Confirmation（RC1 引入）

**以前为什么痛苦**：想在工具调用前加确认只能自己 hack——在 `ToolCallingManager` 外面包一层，拦截工具调用请求、暂停循环、等人工决策、再把结果塞回去。写起来不难，**写对很难**：暂停时的状态存哪里？服务重启怎么办？多实例部署时决策请求打到另一台机器，怎么找到暂停的上下文？大部分团队的做法是「不做了」——高危工具要么直接禁用，要么在 Prompt 里写一句「请谨慎操作」祈祷模型听话。

**2.1 的做法**：

```java
@Tool(description = "Book a flight", requiresConfirmation = true)
String bookFlight(String flightNumber) {
    return bookingService.book(flightNumber);
}
```

模型要调用该工具时，**整个工具调用循环在执行任何调用之前暂停**，把回复返回给应用并列出所有等待确认的调用；应用收集每个调用的 `ToolCallDecision`（allow，或 deny 并附带一条消息），再调 `ToolCallingManager.executeToolCalls(prompt, reply, decisions)` 执行，结果作为下一次请求发回。被拒绝的调用会把消息返回给模型，而不是真正执行。

**关键设计**：循环在等待时不保留任何状态——暂停是一次普通的响应返回，恢复是一次普通的请求发送。只要应用保存了对话，**服务重启也能恢复**，多实例部署也不怕决策打错机器。

**哪些调用需要确认**由 `ToolCallConfirmationPolicy` 决定：默认策略读工具元数据；`forTools(...)` 用来指定你不拥有的工具（如 [[MCP协议|MCP]] 工具）；lambda 可检查参数（如只确认超过某个金额的转账）。

**边界**：Tool Call Confirmation 是 2.1 核心项目的一部分，有正式发布和支持；但「跨多个 Agent 等待人工」属 [[SpringAI|Spring AI Agent]] 的规划范围，不在 2.1 核心能力内。

### 二、Message Parts：让推理过程不再丢失（M1 引入）

**以前的结构问题**：`AssistantMessage` 是「一个文本字段 + `toolCalls`、`media` 几个独立列表」，**无法表达「推理 → 工具调用 → 文本」的真实交错顺序**。而 Anthropic、Google Gemini、DeepSeek 的推理模型返回内容时，推理与工具调用本就是交错的；顺序乱了或在回放时丢了推理内容，模型可能报错或推理质量下降。

**Anthropic 的硬约束**：工具使用轮次里 Claude **要求 thinking blocks 原样返回**，不能重排、不能编辑、不能部分丢弃，改过的块直接 HTTP 400。2.1 之前 Spring AI 把工具轮次重建成「文本 → thinking → 工具」，不管 Claude 实际用什么顺序。

**2.1 的做法**：消息内容改为**有序的 `MessagePart` 列表**，Part 保持模型产出的原始顺序，一轮对话可忠实往返。`getText()`/`getMedia()`/`getToolCalls()`/`getReasoning()` 降为对 Parts 的视图，旧构造器与 Builder 仍在。

**不同模型的回放要求不一样**（框架层抹平差异）：Anthropic 要求 thinking blocks 带签名按序返回；Google GenAI 要求每个 thought signature 回到它原来所在的 Part，否则 Gemini 3+ 函数调用返回 400；OpenAI Responses 要求推理项带上加密的 `encrypted_content` 一起回放。

**版本差异（重要）**：Message Parts 是 2.1.0-M1 引入的，但 **M1 里只有 `OpenAiResponsesChatModel` 原生产出和消费 Parts**；Ollama、Anthropic、OpenAI Chat Completions 等实现是 **RC1** 才重构完成。用非 Responses 端点时，Parts 的完整回放能力要看 RC1 之后的版本。

### 三、OpenAI Responses API

**为什么需要新端点**：Spring AI 原来用 Chat Completions（`/v1/chat/completions`），普通对话没问题，但**从 GPT-5.4 开始它不支持「工具调用 + 非 none 的推理强度」组合**——Agent 想让模型调工具前先深度推理（reasoning effort 设 high/medium），Chat Completions 直接拒绝。Responses API（`/v1/responses`）原生支持工具调用与推理组合，推理内容可通过加密 reasoning item 在工具调用轮次间保留。

**怎么切**：只改一个属性 `spring.ai.openai.chat.api=responses`，`api-key`/`base-url`/`model` 全不变，`OpenAiResponsesChatModel` 自动启用。

**关键设计**：`OpenAiResponsesChatModel` 是**无状态的**——每次调用发完整 Prompt，所以 [[ChatMemory]]、Advisors、RAG 的工作方式跟 `OpenAiChatModel` 完全一样，不依赖 OpenAI 服务端保存对话，所有状态在客户端。

**注意**：两个端点**互斥**，默认只配一个。要同时用（如 Chat Completions 做便宜分类、Responses 做 Agent）需用 Builder 显式声明第二个。

### 四、Decision Model（RC2 引入）

**要解决什么**：很多场景不需要模型「生成一段话」，只需要它**做一个判断**——评论正负面、代码有无安全风险、文档与查询是否相关。用 ChatModel 做可行，但成本和延迟都不划算：ChatModel 的强项是生成，不是分类。

**2.1 的做法**：`DecisionModel` 接口专做「带概率的判断」，三种答案类型 `Choice`（从选项里选）、`Noul`（是/否概率）、`Score`（按等级打分）：

```java
DecisionResponse response = decisionModel.evaluate(
    "客户说'我被重复扣款了，请尽快处理'",
    DecisionRequest.builder()
        .choice("category", "工单分类", "billing", "technical", "other")
        .noul("is_urgent", "是否紧急")
        .build()
);
if (response.getNoul("is_urgent").isYes(0.9)) {
    escalateToHuman();
}
```

**三种实现**：`OpenAiDecisionModel`（背后是 OpenAI Decisions API，由 OpenAI starter 在 `spring.ai.openai.decision` 下自动配置）、`OllamaDecisionModel`（默认 `d1-omni:600m`，本地跑不需 API Key）、`SystemOneDecisionModel`（基于 TypeSafe Java SDK，兼容 Jev、Laya 等 [[SystemOne|System One]] 协议服务器，**不是自动配置的**，需手动创建 `TypeSafeClient`）。

**核心差异**：ChatModel 返回文本，你要自己解析自己判断；DecisionModel 返回**校准过的概率**，代码直接 `isYes(0.9)` 决定是否触发动作。但**它仍是机器学习模型不是规则引擎**——答案不确定、概率不绝对，需自己设阈值并接受一定比例误判。

### 五、其他值得关注的变化

- **流式工具调用参数**：模型流式输出工具调用时参数是一块块来的，2.1 之前只暴露完整调用；2.1 把参数增量也流式暴露，UI 可在模型还在「写」参数时就展示。带 partial 标记的 `ToolCallPart` 会被 `getToolCalls()`、`ToolCallingManager` 忽略，完整调用仍在同一 index 上随后到来
- **向量库自定义 Embedding 扩展**：M1 引入 `VectorStore.upsert()` 写自算向量，RC1 加 `similaritySearch(float[], SearchRequest)` 用自算查询向量检索，RC2 扩展到 Neo4j、MongoDB Atlas、Typesense、MariaDB、Chroma
- **Session API 演进**：`ChatMemory` 及类型标记弃用，迁 Session API——提供 **Turn** 概念（一次 `UserMessage` 加后续所有事件）与可组合 compaction 触发器/策略（滑动窗口、按 Turn 窗口、Token 计数、递归摘要）；`SessionMemoryAdvisor` 可透明接入 `ChatClient`，`conversation_search` 工具对压缩后历史做关键词检索。官方 Session API 文档目前**没有多 Agent 章节**

### 六、优缺点与适用场景

**优点**：① 工具调用确认——框架级暂停/恢复，不依赖应用层 hack，重启与多实例都能正确恢复；② Message Parts——有序 Part 忠实还原交错顺序，Anthropic/Gemini/DeepSeek 的回放需求都满足；③ Responses API——Agent 场景的正确端点；④ DecisionModel——概率是一等公民；⑤ 流式工具参数——UI 体验更好。

**缺点**：① 迁移成本（`ChatMemory` 弃用 + 自定义 Message 处理逻辑可能要改）；② Parts 完整支持有 M1→RC1 版本差异；③ DecisionModel 的 System One 实现需手动配；④ 多 Agent 场景还在路上。

| 场景 | 推荐度 | 理由 |
| --- | --- | --- |
| 企业级 Agent，高危工具需人工确认 | 强烈推荐 | Tool Call Confirmation 是刚需 |
| 需完整回放模型推理过程 | 强烈推荐 | Message Parts 保留顺序与签名 |
| 用 OpenAI 旗舰模型做 Agent | 强烈推荐 | Responses API 是正确端点 |
| 工单分类/风控判断/相关性打分 | 强烈推荐 | DecisionModel 比 ChatModel 更合适 |
| 需流式展示工具调用参数 | 推荐 | 参数增量流式暴露 |
| 已有 ChatMemory 的重度用户 | 需评估 | 要迁到 Session API |
| 多 Agent 场景需人工流转 | 需评估 | 等 Spring AI Agent 后续版本 |

**结论判断**：2.1 解决的不是「能不能调模型」，而是「**模型调错了怎么办**」。这些能力叠加指向同一方向——**Spring AI 正在从「AI 接入层」变成「Agent 运行时」**：2.0 解决「怎么调」，2.1 开始解决「怎么调得稳、调得对、调得可控」。对正在把 Agent 往生产推的团队，迁移门槛换来的是实打实的安全感。

> 参考：Spring AI 2.1.0-M1 发布公告 https://spring.io/blog/2026/09/25/spring-ai-2-1-0-M1-available-now

## 关联连接
- [[SpringAI]] — 本篇主角（已增量合并苏三视角）
- [[摘要-spring-ai-2-1发布]] — 同一事件另一作者版本（[[锋哥]]/特性清单式），两篇互链
- [[锋哥]] — 另一版本的作者
- [[苏三]] — 本文作者
- [[ToolCallConfirmation]] — 本篇重点展开的框架级暂停/恢复机制
- [[MessageParts]] — 本篇重点展开的有序消息片段模型
- [[DecisionModel]] — 带概率的判断模型（本篇给出 Choice/Noul/Score 口径）
- [[ResponsesApi]] — OpenAI 新端点（GPT-5.4 起工具调用+推理的必经之路）
- [[ChatMemory]] — 被 Session API 取代的旧机制
- [[ToolCalling]] — 工具调用机制总概念
- [[HITL]] — 工具确认的上位人机协同概念
- [[审批设计]] — 审批信息要素与失败即拒绝
- [[MCP协议]] — `forTools(...)` 覆盖的外部工具来源
- [[SystemOne]] — SystemOneDecisionModel 的协议来源
- [[Ollama]] — 本地跑 d1-omni:600m 演示 DecisionModel
- [[SpringBoot]] — 2.1 的构建基线 4.2
- [[VectorStore]] — 自带向量 upsert / 自定义查询向量
- [[AgentRuntime]] — 「Spring AI 变成 Agent 运行时」的定位归属
