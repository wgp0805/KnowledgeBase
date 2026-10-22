---
title: "为什么越来越多人用Eino？"
source: "https://mp.weixin.qq.com/s/9NtIiYcERFIzwT_oNs1jyw"
---
苏三 苏三说技术 *2026年10月22日 08:20*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

前阵子技术群里有小伙伴反馈说，他们准备把AI能力接进现有的Go微服务里。

技术负责人跟说了一个很实际的困扰：“我们后端全是Go写的，但大模型生态里全是Python的框架。

LangChain、LlamaIndex，看着都挺好，但我们的服务没法直接跑Python。硬要接，就得在Go服务旁边再起一个Python进程，走HTTP或者gRPC通信，运维复杂度一下就上来了。”

我问他：“你们看过Eino吗？”

他愣了一下：“Eino是什么？Go的AI框架？”

**对，Eino就是字节跳动CloudWeGo团队开源的Go语言大模型应用开发框架。**

它的定位很清晰： **让Go开发者用Go的方式，构建生产级的AI应用和Agent，不需要绕道Python。**

**后面基本程序员都是全栈开发，不光要懂Java，还需要懂Python，还需要懂Go。**

今天这篇文章，我就把Eino到底解决了什么问题、它的核心设计、以及怎么用，从头到尾给你拆解一遍。

希望对你会所有帮助。

## 一、为什么Go有一个自己的AI框架？

> 有些小伙伴可能会说：“我用Go调大模型API不就行了？写个HTTP请求，解析JSON，能有多难？”

调API确实不难。

难的是 **编排** 。

一个正经的AI应用，绝对不是“用户问一句、模型答一句”这么简单。

它需要判断意图、调用工具、把工具结果塞回模型继续推理、处理流式输出、管理多轮对话的上下文、在出错时重试或者切换备用模型。这些逻辑用Go的if-else硬写，代码会迅速膨胀成一团乱麻。

Python有LangChain、LlamaIndex，它们把这些问题封装成了组件和编排抽象。

Go生态里一直没有对等的东西。你要么用Go硬写，要么把AI逻辑拆到Python服务里。

**Eino做的事情，就是把AI应用开发的那套工程抽象，用Go语言重新实现了一遍。**

而且它不是简单的“Go版LangChain”。

Eino在设计上有一个非常明确的目标： **面向生产环境** 。

它借鉴了LangChain和Google ADK的思路，但更强调类型安全、流式处理、并发管理和可观测性。

## 二、一张图看懂Eino的核心架构

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/HUV4yMdu0rfUPey7YnMBQgkBam7fLFrvDBnpD2IqLFkgj2ZEEXuAVKWKn6OWeoqgQTc8JUOngwibwBelcSBjTlYoYnzfzraA2cJQlj4ibO1DQ/640?wx_fmt=png&from=appmsg#imgIndex=0)

Eino的架构可以分成四层：

**组件层** ：定义了ChatModel、Tool、Retriever、ChatTemplate这些基础抽象。每个组件都有自己的输入输出类型和流式范式。官方提供了OpenAI、Claude、Gemini、Ollama、Elasticsearch等大量现成实现。

**编排层** ：用有向图（Graph）把组件连起来。节点是组件实例，边是数据流通道。Eino在编排层承担了类型检查、流式处理、并发管理这些脏活累活。

**Agent开发套件（ADK）** ：在编排之上提供更高层的Agent抽象。核心是ChatModelAgent，它内置了ReAct循环——模型自主决定什么时候调工具、什么时候输出最终答案。还有DeepAgent用于复杂任务的拆解和委派。

**运行时能力** ：流式处理、类型检查、Callback切面、中断恢复。这些是Eino区别于“简单封装库”的关键。

## 三、底层原理

### 3.1 类型安全

编译期就能发现的问题，不要拖到运行时。

AI应用里最常见的bug是什么？

**上下游节点的数据类型对不上。**

比如你把一个 `ChatModel` 节点的输出（ `*             schema.Message           ` ）直接连到一个期望 `[]*             schema.Document           ` 的 `Retriever` 节点上。

在Python里，这个问题可能要等到运行时才报错。

在Eino里， `              graph.AddEdge            ` 的时候就会检查类型是否匹配，不匹配直接编译失败。

**这不是“多一点代码”的问题，这是“少一次线上事故”的问题。**

### 3.2 流式处理

让组件只关心自己该关心的事。

大模型的输出是流式的——一个字一个字往外蹦。但有些下游节点（比如工具调用节点）只接受完整的输入，不处理流。

如果每个组件都要自己处理“流怎么拼接、怎么分发、怎么合并”，代码会变得极其复杂。

Eino的做法是： **组件只实现自己真正需要的流式范式，剩下的框架帮你补全。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/HUV4yMdu0rcl42q83SuJYt8UXdPSbkHCj5HiaJErtcBVqhqcce6GFJx1GwUEFtibHUJcshT5tj3keibkqSCd0icJvPeMf6QyKDzM93VshEnR8Tg/640?wx_fmt=png&from=appmsg#imgIndex=1)

具体来说：

**自动拼接** ：下游节点只接受非流输入时，Eino把流拼成完整内容再传过去。 **自动装箱** ：下游需要流但上游给的是非流数据时，Eino自动包成流。 **自动合并** ：多个流汇聚到一个节点时，Eino负责合并。 **自动复制** ：一个流要分发给多个下游节点时，Eino负责复制，避免竞争。

**对开发者来说，这意味着你写组件的时候不需要考虑“我上游给的是流还是非流”，只需要声明自己需要什么，Eino负责适配。**

### 3.3 Agent运行时：ReAct循环 + 中间件

Eino ADK的核心是 `ChatModelAgent` 。

你给它一个模型和一组工具，它自己跑ReAct循环——推理、行动、观察、再推理，直到任务完成。

```
agent, err := 
            adk.NewChatModelAgent(ctx,
           &
            adk.ChatModelAgentConfig{
          
    Model: myChatModel,
    ToolsConfig: 
            adk.ToolsConfig{
          
        ToolsNodeConfig: 
            compose.ToolsNodeConfig{
          
            Tools: []
            componenttool.BaseTool{myTool},
          
        },
    },
    MaxIterations: 10, // 防止无限循环
})
```

**但生产环境的Agent远不止ReAct循环。**

Eino [v0.9版本围绕“Agentic](http://v0.xn--9agentic-3p3d0313c5jpbc41aqd8a/) Runtime”做了大量增强：

**Cancel** ：从外部主动终止正在运行的Agent，支持安全点取消和checkpoint持久化。

**Model Retry** ：重试决策可以读取模型输出、拒绝不满足条件的输出、修改下一次输入。

**Model Failover** ：主模型调用失败后切换到备用模型，支持优先复用上一次成功的模型。

**Middleware** ：在ReAct循环的生命周期点位注入行为，比如上下文压缩、工具搜索、文件系统操作。

**这些能力的共同点是：它们解决的是“Agent在生产环境跑不稳”的问题，而不是“Agent能不能跑起来”的问题。**

### 3.4 中断与恢复：Human-in-the-Loop的原生支持

AI Agent经常需要人工介入——比如执行高危操作前需要审批，或者遇到不确定的情况需要用户补充信息。

Eino的ADK支持 **任意节点中断、精确恢复** 。Agent执行到某个节点时暂停，等待人工输入，然后从断点继续，不需要从头重跑。

这个能力在生产环境中极其重要。

没有它，一个跑了十分钟的Agent因为需要一次人工确认就要全部重来，成本和时间都不可接受。

## 四、代码实战

### 4.1 安装

```
go get 
            github.com/cloudwego/eino@latest
```

### 4.2 定义一个最简单的Agent

```
package main

import (
    "context"
    "
            github.com/cloudwego/eino/adk"
          
    "
            github.com/cloudwego/eino/components/model"
          
    "
            github.com/cloudwego/eino/components/tool"
          
    "
            github.com/cloudwego/eino/compose"
          
)

func main() {
    ctx := 
            context.Background()
          

    // 1. 创建ChatModel（以OpenAI为例）
    chatModel := 
            model.NewOpenAIChatModel(...)
          

    // 2. 定义工具
    myTool := 
            tool.NewMyTool(...)
          

    // 3. 创建ChatModelAgent
    agent, err := 
            adk.NewChatModelAgent(ctx,
           &
            adk.ChatModelAgentConfig{
          
        Model: chatModel,
        ToolsConfig: 
            adk.ToolsConfig{
          
            ToolsNodeConfig: 
            compose.ToolsNodeConfig{
          
                Tools: []
            componenttool.BaseTool{myTool},
          
            },
        },
        MaxIterations: 10,
    })
    if err != nil {
        panic(err)
    }

    // 4. 运行
    events, err := 
            agent.Run(ctx,
           "帮我查一下北京明天的天气")
    if err != nil {
        panic(err)
    }

    // 5. 消费事件流
    for event := range events {
        // 处理Agent的每一步输出
        
            fmt.Println(event)
          
    }
}
```

**关键理解** ： `ChatModelAgent` 内部处理了完整的ReAct循环。你不需要自己写“模型决定调工具→执行工具→把结果喂回模型”这个循环，ADK帮你做了。

### 4.3 用Graph做确定性编排

当你的流程是确定的（比如“先检索、再生成、最后校验”），用Graph比Agent更合适：

```
graph := 
            compose.NewGraph[*schema.Message,
           *
            schema.Message]()
          

// 添加节点

            graph.AddChatModelNode(
          "chat", chatModel)

            graph.AddRetrieverNode(
          "retrieve", retriever)

            graph.AddLambdaNode(
          "format", 
            compose.InvokableLambda(formatFunc))
          

// 连接节点

            graph.AddEdge(compose.START,
           "retrieve")

            graph.AddEdge(
          "retrieve", "chat")

            graph.AddEdge(
          "chat", "format")

            graph.AddEdge(
          "format", 
            compose.END)
          

// 编译并运行
runnable, err := 
            graph.Compile(ctx)
          
result, err := 
            runnable.Invoke(ctx,
           input)
```

**Graph和Agent的区别** ：Graph是 **确定性编排** ，你明确知道每一步该做什么；Agent是 **自主决策** ，模型自己决定下一步。

Eino同时支持两者，而且Graph可以被包装成Tool给Agent用，实现“确定性流程”和“自主决策”的混合。

## 五、Eino vs LangChain：Go开发者的视角

| 对比维度 | Eino | LangChain（Python） |
| --- | --- | --- |
| **语言** | Go | Python |
| **类型安全** | 编译期检查 | 运行时检查 |
| **并发模型** | Goroutine，单机2000+连接 | Thread/Async，200+连接时延迟显著 |
| **内存占用** | 启动约30MB | 启动约200MB |
| **编排方式** | 显式Graph，逻辑清晰 | Chain模式，容易写成面条代码 |
| **微服务生态** | 无缝对接Hertz/Kitex/Gorm | 需要额外集成 |
| **流式处理** | 框架自动处理拼接/分发/合并 | 部分自动，部分需要手动 |

**核心差异** ：Eino不是“把LangChain翻译成Go”，而是 **用Go的工程哲学重新设计AI应用框架** 。

显式优于隐式，类型安全优于运行时灵活，并发原生优于异步模拟。

## 六、优缺点

### 优点

**1\. Go原生，不绕道Python**  
用Go写AI应用，不需要在Go服务旁边起Python进程。部署简单，运维成本低。

**2\. 类型安全，编译期发现问题**  
Graph构建时就检查上下游类型是否匹配，不需要等到运行时才发现“这个节点输出类型不对”。

**3\. 流式处理框架自动适配**  
组件只需要声明自己需要什么流式范式，拼接、装箱、合并、复制全部由框架处理。

**4\. Agent运行时能力完善**  
Cancel、Retry、Failover、Middleware、中断恢复——生产环境需要的运行时能力，ADK基本都覆盖了。

**5\. 高并发低资源**  
Go的Goroutine模型天然适合高并发场景，内存占用远低于Python服务。

**6\. 字节跳动内部验证**  
CloudWeGo是字节跳动的开源项目，Eino在设计上考虑了大规模生产环境的需求。

### 缺点

**1\. 生态还在成长**  
组件实现的数量和第三方集成丰富度，跟LangChain的Python生态还有差距。虽然官方提供了主流模型和检索器的实现，但遇到小众工具可能需要自己封装。

**2\. API仍在演进**  
[v0.9版本对Agent运行时做了大量调整，部分API被标记为“不推荐使用”。版本升级需要关注迁移文档。](http://v0.xn--9agent,api-rx6ema3993m7rap9ab0ieseg5jxs0bm1lxk3b5iil3cnwk50fr34fpiqfq7g2g4azlcys1bwlci93ci1h58h.xn--d6q67br25abrbs3bk4md6jw4pq2jzk1a6hp5pu./)

**3\. Go开发者AI经验相对少**  
如果你是从Java或Python转过来的，Go本身的语法和并发模型也需要适应。Eino的文档虽然完善，但社区讨论的丰富度不如Python生态。

**4\. 不适合完全不懂Go的团队**  
Eino的价值建立在“你已经用Go”的前提下。如果团队技术栈是Java，Spring AI Alibaba或LangChain4j是更自然的选择。

## 七、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **Go微服务接入AI能力** | ✅✅✅ 强烈推荐 | 原生Go，不引入Python进程 |
| **高并发AI网关/Agent服务** | ✅✅✅ 强烈推荐 | Goroutine模型天然适合 |
| **需要类型安全的生产级应用** | ✅✅✅ 强烈推荐 | 编译期类型检查，减少运行时事故 |
| **复杂Agent工作流** | ✅✅✅ 强烈推荐 | ADK + Middleware + 中断恢复 |
| **确定性流程编排** | ✅✅✅ 强烈推荐 | Graph编排清晰可控 |
| **Java/Python技术栈团队** | ⚠️ 需评估 | Spring AI / LangChain更自然 |
| **需要大量第三方集成的场景** | ⚠️ 需评估 | 生态还在成长中 |

## 八、写在最后

回到最初的问题： **为什么越来越多人用Eino？**

**因为它让Go开发者用Go的方式做AI，而不是被逼着去写Python。**

AI应用落地的难点从来不是“调不通API”，而是 **编排、流式处理、类型安全、并发管理、运行时稳定性** 。

这些东西在Python生态里有LangChain和LlamaIndex，在Go生态里，Eino是目前最完整、最面向生产环境的选择。

它不是“Go版LangChain”的简单翻译。

它用Go的工程哲学——显式编排、类型安全、并发原生——重新设计了AI应用开发的抽象。

对于已经在Go技术栈上的团队来说，这意味着 **不需要为了接AI而引入第二套语言和运行时** 。

当然，Eino的生态还在成长，API仍在演进。

但对于 **Go微服务、高并发Agent服务、需要类型安全的生产级应用** 这些场景来说，它已经是一个值得认真评估的选择。

参考资源：

- GitHub： [https://github.com/cloudwego/eino](https://github.com/cloudwego/eino)
- 官方文档： [https://www.cloudwego.io/docs/eino/](https://www.cloudwego.io/docs/eino/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

我的企业智能知识库项目Go后端就是Eino对接的大模型，这个项目有：Java、python、Go 三种不同的后端版本，想学习其他语言项目的小伙伴一定不要错过。