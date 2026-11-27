---
title: "夯爆了，Spring AI 2.1 正式发布！"
source: "https://mp.weixin.qq.com/s/PaupuTGj43imISjsw8xUfQ"
author:
  - "[[苏三]]"
published:
created: 2026-11-27
description:
tags:
  - "clippings"
---
苏三 苏三说技术 *2026年11月27日 08:20*

## 大家好，我是苏三，又跟大家见面了。

文末留言送书啦！！！

## 前言

**2026年11月19日，Spring AI 2.1.0 正式发布了。**

说实话，这次发布让我有点意外。

Spring AI 2.0 GA 才过去半年，2.1 就来了。而且这一版不是“修修补补”，是 **冲着 Agent 落地的深水区去的** 。

为什么这么说？

因为 2.1 解决了一个所有做企业级 Agent 的人都绕不开的问题： **模型调用工具，到底该不该无条件信任？**

> 有些小伙伴在工作中可能遇到过这种情况：你做了一个智能客服 Agent，能查订单、能改地址、能发起退款。测试的时候一切正常，上线之后有一天模型“心情不好”，把一笔不该退的款给退了。你翻日志，发现它确实调了退款工具，参数也是对的，就是判断错了。

这不是模型笨，是 **框架层缺少一道“人工确认”的闸门** 。

2.1 把这个闸门做成了正式能力。

今天这篇文章就专门跟大家一起聊聊Spring AI 2.1，希望对你会有所帮助。

## 一、核心变化

### 1.1 以前怎么做，为什么痛苦

在 2.1 之前，如果你想在工具调用前加一道确认，只能自己 hack。

你要在 `ToolCallingManager` 外面包一层，拦截模型的工具调用请求，暂停循环，等人工决策，再把结果塞回去。

这套逻辑写起来不难，但 **写对很难** 。

暂停时的状态存哪里？

服务重启了怎么办？

多实例部署时，决策请求打到了另一台机器上，怎么找到暂停的上下文？

**大部分团队的做法是：不做了。**

高危工具要么直接禁用，要么靠“Prompt 里写一句‘请谨慎操作’”来祈祷模型听话。

### 1.2 2.1 的做法：框架级的暂停与恢复

2.1 在 RC1 中正式引入了 **Tool Call Confirmation** 。

你在工具方法上加一个注解：

```
@Tool(description = "Book a flight", requiresConfirmation = true)
String bookFlight(String flightNumber) {
    return 
            bookingService.book(flightNumber);
          
}
```

模型要调用这个工具时， **整个工具调用循环会在执行任何调用之前暂停** ，把回复返回给应用，列出所有等待确认的调用。

应用收集每个调用的 `ToolCallDecision`（allow，或者 deny 并附带一条消息），然后调用 `             ToolCallingManager.executeToolCalls(prompt,            reply, decisions)` 执行回复里的调用，再把结果作为下一次请求发回去。

被拒绝的调用会把你的消息返回给模型，而不是真正执行。

**关键设计** ：循环在等待时不保留任何状态。

暂停是一次普通的响应返回，恢复是一次普通的请求发送。

只要你的应用保存了对话， **服务重启也能恢复** 。

哪些调用需要确认由 `ToolCallConfirmationPolicy` 决定：默认策略读取工具元数据，`forTools(...)` 用来指定你不拥有的工具（比如 MCP 工具），lambda 可以检查参数（比如只确认超过某个金额的转账）。

> **需要注意的一点** ：Tool Call Confirmation 是 Spring AI 2.1 核心项目的一部分，有正式的发布和支持。但“跨多个 Agent 等待人工”的流程，属于 Spring AI Agent 的规划范围，不在 2.1 的核心能力里。如果你需要多 Agent 场景的确认流转，需要等后续版本或自己在上层编排。

### 1.3 底层原理：暂停时到底发生了什么？

![Mermaid 流程图：用户提问](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%8CSpring%20AI%202.1%20%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%EF%BC%81/4b088e0db733342d875ddce08e8500ee_MD5.png)

**核心差异** ：正常流程里，`ToolCallingManager` 拿到模型返回后直接执行。需要确认的流程里，它先检查每个调用的 `requiresConfirmation` 标记，如果有任何一个需要确认，就整段暂停，把决策权交给应用。

## 二、Message Parts：让“推理过程”不再丢失

### 2.1 以前的问题：消息是“文本 + 一堆旁挂列表”

在 2.1 之前，Spring AI 的 `AssistantMessage` 结构是这样的：一个文本字段，加上几个独立的列表——`toolCalls`、`media`。

**它无法表达“推理 → 工具调用 → 文本”这种真实的交错顺序。**

为什么这很重要？

因为现在的模型（尤其是 Anthropic、Google Gemini、DeepSeek 的推理模型）在返回内容时， **推理过程和工具调用是交错排列的** 。

如果你把顺序搞乱了，或者在回放时丢了推理内容，模型可能会报错，或者推理质量下降。

以 Anthropic 为例，在工具使用轮次里，Claude **要求把它的 thinking blocks 原样返回** ，不能重排、不能编辑、不能部分丢弃。

修改过的块会被直接拒绝（HTTP 400）。

2.1 之前，Spring AI 把工具轮次重建成“文本 → thinking → 工具”，不管 Claude 实际用的什么顺序。

### 2.2 2.1 的做法：有序的 MessagePart 列表

2.1 把消息内容改成了 **有序的 `MessagePart` 列表** 。

每个 Part 是一个独立的片段：

| Part 类型 | 内容 |
| --- | --- |
| `TextPart` | 文本 |
| `ReasoningPart` | 推理过程（可携带 OpaquePayload，比如 Anthropic 的 thinking signature） |
| `ToolCallPart` | 工具调用 |
| `ToolResultPart` | 工具结果 |
| `MediaPart` | 图片/音频/PDF |
| `UnknownPart` | 未知块（保留原始 JSON，不静默丢弃） |

**Parts 保持模型产出的原始顺序** ，所以一轮对话可以忠实地往返。

`getText()`、`getMedia()`、`getToolCalls()`、`getReasoning()` 这些方法现在是对 Parts 的视图，旧的构造器和 Builder 也还在。

```
UserMessage question = 
            UserMessage.builder()
          
    .part(
            TextPart.of(
          "这两张图有什么区别？"))
    .part(
            MediaPart.of(firstChart))
          
    .part(
            MediaPart.of(secondChart))
          
    .build();

AssistantMessage answer = 
            chatModel.call(
          new Prompt(question)).getResult().getOutput();
for (ReasoningPart reasoning : 
            answer.getReasoning())
           {
    
            System.out.println(
          "推理: " + 
            reasoning.text());
          
}

            System.out.println(answer.getText());
```

> **一个重要的版本差异** ：Message Parts 是 2.1.0-M1 引入的，但 M1 里 **只有 `OpenAiResponsesChatModel` 原生产出和消费 Parts** 。其他 ChatModel 的实现（Ollama、Anthropic、OpenAI Chat Completions 等）是在 **RC1** 才重构完成、开始用 Parts 的。如果你用的是非 Responses 端点的模型，Parts 的完整回放能力要看 RC1 之后的版本。

### 2.3 底层原理

![Mermaid 流程图：toolCalls](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%8CSpring%20AI%202.1%20%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%EF%BC%81/880a3bea78f5272538c27260e1d723b5_MD5.png)

**不同模型对回放的要求不一样** ：Anthropic 要求 thinking blocks 带签名按顺序返回；Google GenAI 要求每个 thought signature 回到它原来所在的那个 Part，否则 Gemini 3+ 的函数调用会返回 400；OpenAI Responses 要求推理项带上加密的 `encrypted_content` 一起回放。

Parts 的设计让这些差异在框架层被抹平，你不需要为每个模型写一套回放逻辑。

## 三、OpenAI Responses API

### 3.1 为什么需要一个新的端点

Spring AI 原来用的是 OpenAI 的 **Chat Completions** 端点（`/v1/chat/completions`）。这个端点在普通的对话场景下没问题，但 **从 [GPT-5.4](http://GPT-5.4) 开始，它不支持“工具调用 + 非 none 的推理强度”的组合** 。

如果你在做一个 Agent，希望模型在调用工具之前先进行深度推理（reasoning effort 设为 high 或 medium），Chat Completions 会直接拒绝。

**Responses API** （`/v1/responses`）解决了这个问题。

它原生支持工具调用和推理的组合，并且推理内容可以通过加密的 reasoning item 在工具调用轮次之间保留。

### 3.2 怎么切换

只需要改一个属性：

```
spring.ai.openai.chat.api=responses
```

其他的连接配置（`api-key`、`base-url`、`model`）全部不变。`OpenAiResponsesChatModel` 会自动启用。

**关键设计** ：`OpenAiResponsesChatModel` 是 **无状态的** 。每次调用都发送完整的 Prompt，所以 `ChatMemory`、Advisors、RAG 的工作方式跟 `OpenAiChatModel` 完全一样。它不依赖 OpenAI 服务端保存对话，所有状态都在客户端。

**注意** ：两个 OpenAI 端点（Chat Completions 和 Responses）是 **互斥的** ，默认只配置一个。如果你确实想同时用两个，比如用 Chat Completions 做便宜的分类、用 Responses 做 Agent，需要用 Builder 显式声明第二个。

## 四、Decision Model

### 4.1 它解决什么问题

有些场景下，你不需要让大模型“生成一段话”，你需要它 **做一个判断** ：这条评论是正面的还是负面的？这段代码有没有安全风险？这个文档跟查询相关吗？

用 ChatModel 做这件事是可行的，但成本和延迟都不划算。ChatModel 的强项是生成，不是分类。

### 4.2 2.1 的做法：专门的 DecisionModel

2.1 在 RC2 中引入了 `DecisionModel` 接口，专门做“带概率的判断”。它支持三种答案类型：`Choice`（从选项里选）、`Noul`（是/否概率）、`Score`（按等级打分）。

```
// 判断工单是否需要升级
DecisionResponse response = 
            decisionModel.evaluate(
          
    "客户说‘我被重复扣款了，请尽快处理’",
    
            DecisionRequest.builder()
          
        .choice("category", "工单分类", 
                "billing", "technical", "other")
        .noul("is_urgent", "是否紧急")
        .build()
);

// 根据概率做决策
if (
            response.getNoul(
          "is_urgent").isYes(0.9)) {
    escalateToHuman();
}
```

**三种实现** ：

- **OpenAI**

	：`OpenAiDecisionModel`，背后是 OpenAI Decisions API，由 OpenAI starter 在 `              spring.ai.openai.decision            ` 下自动配置
- **Ollama**

	：`OllamaDecisionModel`，默认用 `d1-omni:600m`，本地跑，不需要 API Key
- **System One**

	：`SystemOneDecisionModel`，基于 TypeSafe Java SDK，兼容 Jev、Laya 等 System One 协议的服务器。 **不是自动配置的** ，需要手动创建 `TypeSafeClient`

### 4.3 底层原理

![Mermaid 流程图：输入 Prompt](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%8CSpring%20AI%202.1%20%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%EF%BC%81/fd7fb1b15994a716c6151c2f061a5d53_MD5.png)

**核心差异** ：ChatModel 返回的是文本，你需要自己解析、自己判断。DecisionModel 返回的是 **校准过的概率** ，你的代码可以直接用 `isYes(0.9)` 这样的判断，决定是否触发某个动作。

**注意** ：DecisionModel 仍然是机器学习模型，不是规则引擎。它的答案不是确定性的，概率也不是绝对的。你需要自己设定阈值，并接受一定比例的误判。官方文档专门说明了如何思考阈值和错误答案。

## 五、其他值得关注的变化

### 5.1 流式工具调用参数

模型在流式输出工具调用时，参数是一块一块传过来的。

2.1 之前，Spring AI 只暴露完整的调用。

2.1 把参数增量也流式暴露出来，UI 可以在模型还在“写”参数的时候就展示出来。

带 partial 标记的 `ToolCallPart` 会被 `getToolCalls()`、`ToolCallingManager` 忽略，完整调用仍然会在同一个 index 上跟着到来。

### 5.2 更多向量库支持自定义 Embedding

M1 引入了 `              VectorStore.upsert()            ` 来写入你自己计算的向量，RC1 加了 `similaritySearch(float[], SearchRequest)` 来用你自己的查询向量搜索。

RC2 把这两个能力扩展到了 Neo4j、MongoDB Atlas、Typesense、MariaDB、Chroma 等更多向量库。

### 5.3 Session API 的演进

`ChatMemory` 及相关类型在 2.1 中被标记为弃用，需要迁移到 Session API。Session API 提供了 Turn 的概念（一次 UserMessage 加上后续所有事件），以及可组合的 compaction 触发器和策略（滑动窗口、按 Turn 窗口、Token 计数、递归摘要）。

`SessionMemoryAdvisor` 可以透明地接入 ChatClient，`conversation_search` 工具支持对压缩后的历史做关键词检索。

**但要注意** ：Session API 的官方文档里目前没有多 Agent 章节，社区文档需要自己适配。跨 Agent 的确认流转属于 Spring AI Agent 的规划范围。

## 六、优缺点

### 优点

**1\. 工具调用确认，高危操作有了闸门**  
框架级的暂停/恢复机制，不依赖应用层 hack。服务重启、多实例部署都能正确恢复。

**2\. Message Parts，推理不再丢失**  
有序的 Part 列表，忠实还原模型输出的交错顺序。Anthropic、Gemini、DeepSeek 的推理回放需求都能满足。

**3\. OpenAI Responses API**  
Agent 场景的正确端点，支持工具调用 + 推理强度的组合。

**4\. DecisionModel，分类任务专用**  
概率是一等公民，代码直接基于概率做决策，不需要解析文本。

**5\. 流式工具参数**  
UI 可以在模型写参数的过程中就展示工具调用，体验更好。

### 缺点

**1\. 迁移成本**  
`ChatMemory` 及相关类型在 2.1 中被标记为弃用，需要迁移到 Session API。Message Parts 的引入意味着自定义的 Message 处理逻辑可能需要调整。

**2\. Parts 的完整支持有版本差异**  
M1 只有 `OpenAiResponsesChatModel` 原生产出和消费 Parts，其他模型在 RC1 才完成重构。如果你用的是非 OpenAI 模型，Parts 的完整能力要看 RC1 之后的版本。

**3\. DecisionModel 需要额外配置**  
System One 的 `SystemOneDecisionModel` 不是自动配置的，需要手动创建 `TypeSafeClient`。

**4\. 多 Agent 场景还在路上**  
跨多个 Agent 等待人工的流程属于 Spring AI Agent 的规划范围，不在 2.1 核心能力里。

## 七、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **企业级 Agent，高危工具需要人工确认** | ✅✅✅ 强烈推荐 | Tool Call Confirmation 是刚需 |
| **需要完整回放模型推理过程** | ✅✅✅ 强烈推荐 | Message Parts 保留顺序和签名 |
| **用 OpenAI 旗舰模型做 Agent** | ✅✅✅ 强烈推荐 | Responses API 是正确端点 |
| **工单分类/风控判断/相关性打分** | ✅✅✅ 强烈推荐 | DecisionModel 比 ChatModel 更合适 |
| **需要流式展示工具调用参数** | ✅✅ 推荐 | 参数增量流式暴露 |
| **已有 ChatMemory 的重度用户** | ⚠️ 需评估 | 需要迁移到 Session API |
| **多 Agent 场景需要人工流转** | ⚠️ 需评估 | 等 Spring AI Agent 的后续版本 |

## 八、写在最后

回到最初的问题： **Spring AI 2.1 到底值不值得升级？**

我的判断是： **如果你的 Agent 要动真格的东西，值得。**

2.1 解决的不是“能不能调模型”的问题，是“**模型调错了怎么办**”的问题。Tool Call Confirmation 把人工确认做成了框架能力，Message Parts 让推理过程不再丢失，Responses API 给了 Agent 正确的端点，DecisionModel 让分类判断有了专门的工具。

这些能力叠加在一起，指向同一个方向： **Spring AI 正在从“AI 接入层”变成“Agent 运行时”。** 2.0 解决了“怎么调”，2.1 开始解决“怎么调得稳、调得对、调得可控”。

当然，2.1 不是没有代价。

ChatMemory 弃用需要迁移，Parts 的完整支持在 M1 到 RC1 之间有版本差异，DecisionModel 需要额外配置，多 Agent 的确认流转还在规划中。

但 **对于正在把 Agent 往生产环境推的团队来说，这些门槛换来的是实打实的安全感。**

参考资源：

Spring AI 2.1.0-M1 发布公告：

[https://spring.io/blog/2026/09/25/spring-ai-2-1-0-M1-available-now](https://spring.io/blog/2026/09/25/spring-ai-2-1-0-M1-available-now)

## 文末送书

为了感谢一路支持苏三的小伙们，今天特地给大家送一点小福利。规则非常简单： **在本文留言，我会挑选3位留言最真诚的粉丝，每人获取1本书。**

后面我会在留言区公布中奖名单，给你免费包邮到家！这些书是由电子工业出版社提供的，感谢赞助。

## 《FDE造局AI落地一线实战指南》

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%8CSpring%20AI%202.1%20%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%EF%BC%81/51c34eee3e0203f5805815ffc18b0946_MD5.webp)

全书结构

**前四章讲的是「进场」。** FDE 的第一性原理「先造局，再交付」，第一次见客户该做什么，怎么用三步速通一个完全陌生的行业，怎么用五步画出客户的业务地图。

**中间四章讲的是「判断」。** 真需求与伪需求怎么分，什么场景才值得下注，ROI 该怎么估，客户那句模糊的话怎么翻译成技术方案。

**接着三章讲的是「推进」。** 面对不同层级的人该怎么沟通，一套 AI 项目的评估体系怎么设计，客户当面说「不」的时候怎么接。

**最后两章讲的是「善后」。** 真正的战场在 PoC 之后，以及项目出现模糊和失败信号时怎么预警。

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%8CSpring%20AI%202.1%20%E6%AD%A3%E5%BC%8F%E5%8F%91%E5%B8%83%EF%BC%81/6f071f3b9aff8cc45be429ce0f241dd5_MD5.webp)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)