---
title: "美团二面：Agent、Tools、Workflow 这三个的概念和区别介绍一下？我：没接触过..."
source: "https://mp.weixin.qq.com/s/EdF_pyb_Ci7BFGXQbRsRoA"
---
犬小哈 小哈学Java *2026年7月7日 13:59*

![图片](assets/%E7%BE%8E%E5%9B%A2%E4%BA%8C%E9%9D%A2%EF%BC%9AAgent%E3%80%81Tools%E3%80%81Workflow%20%E8%BF%99%E4%B8%89%E4%B8%AA%E7%9A%84%E6%A6%82%E5%BF%B5%E5%92%8C%E5%8C%BA%E5%88%AB%E4%BB%8B%E7%BB%8D%E4%B8%80%E4%B8%8B%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E6%8E%A5%E8%A7%A6%E8%BF%87/e56337e64fa6bb4ed35f604ae04a2770_MD5.webp)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

## 面试考察点

1. **概念辨析** ：面试官想看你能不能把 Tools、Workflow、Agent 三者的边界说清楚。很多人一上来就混着用这三个词，Anthropic 在 2024 年 12 月那篇《Building Effective Agents》里给了业界公认的定义，先把这个记牢。
2. **架构选型意识** ：知道区别只是入门。给你一个具体业务场景，你能选出合适的形态吗？"什么时候用 Workflow，什么时候必须上 Agent"，这才是面试官真正想听的。
3. **工程实践** ：在 Java 生态里（ `Spring AI` 、 `LangChain4j` ），这三种东西分别怎么落地？有没有动手写过？
4. **前沿认知** ：Anthropic 提的 "简单胜于复杂" 原则你认同吗？2025 年 Spring AI 1.0 把这些概念正式引入了 JVM 生态，你关注过吗？

## 核心答案

这三个东西不是并列关系，而是 **层级递进** 的，一句话概括：

> “
> 
> **Tools 是积木，Workflow 是按图纸拼好的流水线，Agent 是会自己看图纸自己拼的工人。**

| 维度 | Tools（工具） | Workflow（工作流） | Agent（智能体） |
| --- | --- | --- | --- |
| **本质** | LLM 可调用的离散函数 | 人预先编排的固定流程 | LLM 自主驱动的循环系统 |
| **决策方** | 调用者（人或 LLM） | **人**  （开发者写死路径） | **LLM**  （动态决定下一步） |
| **可控性** | 单步可控 | 高（路径固定） | 低（路径不可预测） |
| **灵活性** | 低 | 中 | 高 |
| **典型形态** | 查天气、算数、查 DB | RAG 管线、路由分发 | ReAct 循环、Plan-and-Execute |
| **Java 框架落地** | `@Tool`  注解 | `ChatClient`  链式 API / LangGraph 节点 | Tool Calling + 自主循环 |

Anthropic 给的核心建议很朴素： **先从最简单的方案开始，能用 Workflow 解决的就别上 Agent** 。

## 深度解析

### 一、Tools（工具）—— 最小积木

Tools 是三者里最底层的概念，说白了就是 **一个可以让 LLM 调用的函数** 。它本身没 "智能"，就是一个被动的能力单元，查个数据库、调个 API、读个文件，都是它干的活。

![AI Tool 工具调用流程](assets/%E7%BE%8E%E5%9B%A2%E4%BA%8C%E9%9D%A2%EF%BC%9AAgent%E3%80%81Tools%E3%80%81Workflow%20%E8%BF%99%E4%B8%89%E4%B8%AA%E7%9A%84%E6%A6%82%E5%BF%B5%E5%92%8C%E5%8C%BA%E5%88%AB%E4%BB%8B%E7%BB%8D%E4%B8%80%E4%B8%8B%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E6%8E%A5%E8%A7%A6%E8%BF%87/d4d3cb247b70e71d2f46b12d4489a7a4_MD5.jpg)

AI Tool 工具调用流程

AI Tool 工具调用流程

图上能看出来，Tool 的角色很纯粹，只负责 "执行具体动作"，至于 "什么时候调、调几次、调用结果怎么处理"，那是上层 Workflow 或 Agent 的事。

在 `Spring AI` 里，定义一个 Tool 很简单，用 `@Tool` 注解就够了：

```
@Component
public class WeatherTools {

    @Tool(description = "查询指定城市的实时天气信息")
    public String getWeather(String city) {
        // 实际调用天气 API
        return 
            WeatherApi.query(city);
          
    }

    @Tool(description = "查询指定城市的未来三天天气预报")
    public String getForecast(String city) {
        return 
            WeatherApi.forecast(city,
           3);
    }
}
```

定义完了，把 Tool 注册给 `ChatClient` ，LLM 就能根据用户的问题自动决定要不要调、调哪个。这里有个细节很多人忽略： **Tool 的 `description` 字段很关键** ，它直接决定 LLM 能不能选对工具，写得模糊或重复，模型就会乱调。

Tools 既不是 Agent 也不是 Workflow，它是构建后两者的最小能力单元。

### 二、Workflow（工作流）—— 固定编排

Workflow 是 **开发者预先设计好代码路径** 的多步流程。LLM 和 Tools 按你写死的步骤一步步走，每一步做什么、结果往哪传，都是确定的。

![Workflow 工作流编排流程](assets/%E7%BE%8E%E5%9B%A2%E4%BA%8C%E9%9D%A2%EF%BC%9AAgent%E3%80%81Tools%E3%80%81Workflow%20%E8%BF%99%E4%B8%89%E4%B8%AA%E7%9A%84%E6%A6%82%E5%BF%B5%E5%92%8C%E5%8C%BA%E5%88%AB%E4%BB%8B%E7%BB%8D%E4%B8%80%E4%B8%8B%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E6%8E%A5%E8%A7%A6%E8%BF%87/a3df72aa043e2946f49e850b9aaaedf2_MD5.jpg)

Workflow 工作流编排流程

Workflow 工作流编排流程

图上是一个典型的 RAG Workflow，每一步的输入输出、调的是 LLM 还是 Tool、调用顺序，都是开发者写死的。LLM 在里面只负责 "执行单步任务"，不决定流程走向。

Spring AI 里用 `ChatClient` 的链式 API 编排 Workflow 很自然：

```
@Service
publicclass RagWorkflow {

    privatefinal ChatClient chatClient;
    privatefinal VectorStore vectorStore;

    public RagWorkflow(
            ChatClient.Builder
           builder, VectorStore vectorStore) {
        this.chatClient = 
            builder.build();
          
        this.vectorStore = vectorStore;
    }

    public String answer(String question) {
        // 这就是一个典型的固定路径 Workflow
        // 每一步都是开发者编排好的，LLM 不决定流程
        return 
            chatClient.prompt()
          
            .user(question)
            .advisors(a -> 
            a.param(RetrievalAugmentationAdvisor.PARAM_RETRIEVE_QUERY,
           question))
            .advisors(
            RagAdvisor.build(vectorStore))
             // 步骤1：检索
            .call()
            .content();                                // 步骤2：生成
    }
}
```

这段代码的关键在于： **流程是开发者写死的** 。LLM 干的活就是 "给你一段上下文，你给我生成一段话"，它没权力决定 "要不要检索"" 检索几次"" 要不要再调一个 Tool"。

Workflow 适合任务路径明确、可预测、对稳定性要求高的场景，比如：

- RAG 问答（检索→重排→生成，固定流水线）
- 文档抽取（解析→分块→抽取字段→校验）
- 意图路由（LLM 分类→分发到对应处理分支）

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E7%BE%8E%E5%9B%A2%E4%BA%8C%E9%9D%A2%EF%BC%9AAgent%E3%80%81Tools%E3%80%81Workflow%20%E8%BF%99%E4%B8%89%E4%B8%AA%E7%9A%84%E6%A6%82%E5%BF%B5%E5%92%8C%E5%8C%BA%E5%88%AB%E4%BB%8B%E7%BB%8D%E4%B8%80%E4%B8%8B%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E6%8E%A5%E8%A7%A6%E8%BF%87/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

### 三、Agent（智能体）—— 自主决策

Agent 是三者里最复杂、最 "智能" 的形态，核心特征就一句话： **LLM 自己决定调什么工具、什么时候调、调几次** ，靠 "感知→思考→行动→观察" 的循环往前推进，直到把任务做完。

![Agent ReAct 推理行动循环](assets/%E7%BE%8E%E5%9B%A2%E4%BA%8C%E9%9D%A2%EF%BC%9AAgent%E3%80%81Tools%E3%80%81Workflow%20%E8%BF%99%E4%B8%89%E4%B8%AA%E7%9A%84%E6%A6%82%E5%BF%B5%E5%92%8C%E5%8C%BA%E5%88%AB%E4%BB%8B%E7%BB%8D%E4%B8%80%E4%B8%8B%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E6%8E%A5%E8%A7%A6%E8%BF%87/01295df02c40b497fcc23ce70b38eaa6_MD5.jpg)

Agent ReAct 推理行动循环

Agent ReAct 推理行动循环

图上就是经典的 **ReAct（Reasoning + Acting）循环** 。看那条从 `Observe` 回到 `Think` 的边，这就是 Agent 跟 Workflow 最本质的区别： **它有循环，会在中间结果的基础上重新决策** 。

Workflow 是 "直线"，Agent 是 "圆环"。

在 Spring AI 里实现一个 Agent，关键是给 LLM 配备一组 Tool，并开启自主循环：

```
@Service
publicclass ResearchAgent {

    privatefinal ChatClient chatClient;

    public ResearchAgent(
            ChatClient.Builder
           builder,
                         WeatherTools weatherTools,
                         SearchTools searchTools,
                         DatabaseTools dbTools) {
        this.chatClient = builder
            .defaultTools(weatherTools, searchTools, dbTools)  // 配备一组工具
            .build();
    }

    public String research(String task) {
        // Agent 的核心：LLM 自主决定调用哪个工具、调用几次
        // 开发者不写死任何路径，全部交给 LLM 决策
        return 
            chatClient.prompt()
          
            .system("""
                你是一个研究助手，可以根据任务自主选择合适的工具。
                你可以反复调用工具、观察结果、调整策略，直到完成任务。
                """)
            .user(task)
            .call()
            .content();
    }
}
```

这段代码看着跟 Workflow 没差多少，但本质完全不同。开发者 **不知道** LLM 会先调 `searchTools` 还是 `dbTools` ，也不知道它会循环几次，运行时根据任务和中间反馈自己决定路径。

Agent 适合任务路径不明确、需要自适应推理的场景，比如：

- 复杂研究任务（"帮我调研一下 2025 年新能源车市场，输出一份报告"）
- 多步骤问题求解（不知道要走几步的问题）
- 开放式探索（用户给的目标本身就是模糊的）

### 四、三者关系：从积木到编排到自主

把三者放到一起看，它们是 **层级递进** 关系：

![Tools、Workflow、Agent 三者关系对比](assets/%E7%BE%8E%E5%9B%A2%E4%BA%8C%E9%9D%A2%EF%BC%9AAgent%E3%80%81Tools%E3%80%81Workflow%20%E8%BF%99%E4%B8%89%E4%B8%AA%E7%9A%84%E6%A6%82%E5%BF%B5%E5%92%8C%E5%8C%BA%E5%88%AB%E4%BB%8B%E7%BB%8D%E4%B8%80%E4%B8%8B%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E6%8E%A5%E8%A7%A6%E8%BF%87/12e34ee552d99eec3c9ee55f184c673d_MD5.jpg)

Tools、Workflow、Agent 三者关系对比

Tools、Workflow、Agent 三者关系对比

如上图所示：

- **第一层 Tools** ：是构建一切的基础，但它单独存在没有任何 "智能"，就是个能力插件
- **第二层 Workflow** ：把多个 Tools 按 **固定路径** 串起来，开发者是司机，LLM 是执行单元
- **第三层 Agent** ：把 Tools 全部交给 LLM， **LLM 自己当司机** ，在循环里决定下一步往哪走

这里有个容易混淆的认知点： **Tools 本身不是 Agent，调用 Tools 的 LLM 也不一定是 Agent** 。只有 "LLM 自主决策 + 循环执行" 同时成立时，才叫 Agent。一个简单的 Function Calling，只要路径是开发者写死的，就仍然只是 Workflow 的一部分。

### 五、选型决策：什么时候用哪个

Anthropic 给的建议，也是 2025 年业界的主流共识：

| 场景特征 | 推荐形态 | 原因 |
| --- | --- | --- |
| 单步任务（查个天气、翻译一句话） | **单次 Tool Calling** | 杀鸡焉用牛刀 |
| 任务路径明确、步骤固定 | **Workflow** | 可控、可调试、可监控 |
| 任务路径不明确、需要自适应 | **Agent** | 灵活、能处理开放性问题 |
| 对稳定性、成本、延迟极度敏感 | **Workflow** | Agent 的循环会带来不可控的 Token 消耗 |

我自己踩过这个坑，之前做一个客服系统，一开始图酷炫上了纯 Agent 架构，结果线上 Token 消耗爆炸、偶尔还会陷入死循环，后来老老实实改回 Workflow + 几个分支路由，稳定性和成本都好太多。

Anthropic 反复强调： **简单胜于复杂** 。能不调 LLM 就不调 LLM，能用 Workflow 就别上 Agent，能用单个 Tool 就别编排一长串流程。懂得克制，比会堆复杂架构更难。

## 面试高频追问

1. **Agent 会不会陷入死循环或者一直调错工具？怎么处理？**
	会。生产环境必须加护栏：限制最大循环次数（max\_iterations）、限制单次任务的 Token 预算、对 Tool 调用结果做校验、加上 "失败 N 次就降级到人工" 的兜底逻辑。这块是 Agent 工程化的核心难点。
2. **Workflow 和 Agent 能混合用吗？**
	能，而且这是 2025 年生产环境的主流形态。典型做法： **外层 Workflow 编排，关键决策点交给 Agent** 。比如 RAG 主流程是 Workflow，但 "查询改写" 这一步用一个小 Agent 来动态决定改写策略。这种 "Workflow 里嵌 Agent" 的形态叫 "Agent with Guardrails"。
3. **Spring AI 和 LangChain4j 在这三个概念上有什么差异？**
	抽象基本一致，都遵循 Anthropic 的定义。 `Spring AI` 用 `@Tool` 注解 + `ChatClient` 链式 API，跟 Spring Boot 生态深度集成； `LangChain4j` 更接近 Python 版 LangChain 的设计，API 风格更 "LangChain 味"。企业级 Spring Boot 项目优先选 Spring AI。

## 常见面试变体

- "Tool Calling 和 Agent 是一回事吗？"（考察对边界的理解）
- "你做过的 RAG 系统是 Workflow 还是 Agent？为什么这么选？"
- "Anthropic 那篇《Building Effective Agents》里讲了哪几种 Workflow 模式？"（提示：Prompt Chaining、Routing、Parallelization、Orchestrator-Workers、Evaluator-Optimizer）
- "为什么 Anthropic 建议优先用 Workflow 而不是 Agent？"

## 记忆口诀

\*\*"积木、流水线、当家人"\*\*：

- Tools 是 **积木** ——被动能力单元
- Workflow 是 **流水线** ——人写死路径
- Agent 是 **当家人** ——LLM 自己决定路径

一句话记区别： **Workflow 是人开车，Agent 是 LLM 开车，Tools 是车上的各种零件。**

## 总结

Tools、Workflow、Agent 是 AI 应用的三个抽象层级，不是并列关系而是递进关系。面试回答时记住三件事： **讲清三者边界、给出 Java 落地代码、强调 "简单胜于复杂" 的选型原则** 。最后一条特别加分，能体现你不只是会用，还懂得克制，这恰恰是工程师跟 "工具人" 的区别。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E7%BE%8E%E5%9B%A2%E4%BA%8C%E9%9D%A2%EF%BC%9AAgent%E3%80%81Tools%E3%80%81Workflow%20%E8%BF%99%E4%B8%89%E4%B8%AA%E7%9A%84%E6%A6%82%E5%BF%B5%E5%92%8C%E5%8C%BA%E5%88%AB%E4%BB%8B%E7%BB%8D%E4%B8%80%E4%B8%8B%EF%BC%9F%E6%88%91%EF%BC%9A%E6%B2%A1%E6%8E%A5%E8%A7%A6%E8%BF%87/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 面试官：满足什么条件时，一个 Java 类会被卸载？3. logback VS log4j2：一倍左右的性能差异，是时候注意了！4. 面试官：为什么需要 Gateway 网关，它有什么作用？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

Java 面试题 | 八股文汇总 · 目录

阅读原文