---
title: "Java AI框架选型指南"
source: "https://mp.weixin.qq.com/s/5M9lMNu0o1IV5ZpzxUfVFg"
---
苏三 苏三说技术 *2026年9月18日 08:40*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

前阵子帮有位球友说，他们公司做技术评审时，遇到了一个特别典型的问题。

他们要做一个智能客服系统，团队里三个人吵得不可开交。

一个说用Spring AI，理由是“Spring官方出品，肯定稳”；

一个说用LangChain4j，理由是“生态最全，什么都能干”；

还有一个说用AgentScope，理由是“阿里内部验证过的，生产级”。

三个人说的都对，但三个人说的不是一回事。

**因为这三个框架解决的根本不是同一个问题。**

这就是Java AI框架选型最大的坑——你以为你在选“哪个更好”，实际上你在选“哪个更适合你的场景”。

而选型这件事，最怕的就是拿着功能列表比参数，比到最后发现选错了层。

今天这篇文章，我就把Java生态里主流的AI框架从头到尾给你拆解一遍。

不讲虚的，只讲一件事： **每个框架站在哪一层，解决什么问题，什么时候该用它。**

希望对你会有所帮助。

## 一、Java AI框架分几层？

很多人选型的时候，把Spring AI、LangChain4j、AgentScope、Embabel放在一起比，这本身就是错的。

它们不在同一层。

Rod Johnson在发布Embabel的时候，给了一个非常锋利的类比：

| 层级 | 类比 | 代表框架 |
| --- | --- | --- |
| **底层基础设施** | Servlet API | Spring AI / LangChain4j |
| **高级应用框架** | Spring MVC | Embabel |

什么意思？

Spring AI和LangChain4j解决的是“怎么连上LLM、怎么管Embedding、怎么接向量库”这类管道问题。

Embabel解决的是“怎么让智能体在复杂业务流程里可靠、可解释、确定性地完成多步骤任务”这类编排问题。

两者是互补关系，不是竞争关系。

再往上，AgentScope解决的是“怎么让Agent在企业级分布式环境里长期稳定运行”的问题。

Solon AI解决的是“怎么在Java 8到Java 26的全版本范围内、在任意框架里嵌入AI能力”的问题。

**一句话说清：选型的第一步不是“选哪个框架”，而是“搞清楚你需要哪一层的框架”。**

## 二、一张图看懂Java AI框架的层级定位

![图片](assets/Java%20AI%E6%A1%86%E6%9E%B6%E9%80%89%E5%9E%8B%E6%8C%87%E5%8D%97/62b0a47a3fa05aabf3fb221e5902a5f7_MD5.jpg)

这张图是整篇文章的骨架。

下面我逐层拆解。

## 三、第一层：底层基础设施

这一层解决的核心问题是： **怎么把大模型、向量数据库、Embedding、工具调用这些基础能力，用Java的方式接进你的项目。**

### 3.1 Spring AI 2.0：Spring官方答案

Spring AI 2.0.0 GA于2026年6月12日正式发布，基于Spring Boot 4.1和Spring Framework 7.0构建。

**它最大的变化是什么？**

Spring AI [1.x里，ChatClient和ChatModel的边界很模糊，很多人直接@Autowired](http://1.x%E9%87%8C%EF%BC%8CChatClient%E5%92%8CChatModel%E7%9A%84%E8%BE%B9%E7%95%8C%E5%BE%88%E6%A8%A1%E7%B3%8A%EF%BC%8C%E5%BE%88%E5%A4%9A%E4%BA%BA%E7%9B%B4%E6%8E%A5@autowired/) ChatModel来用，工具调用、重试、内存管理全往里塞。

2.0把这个边界明确了：ChatClient是面向用户的高层API，内置Advisor链，日常业务开发用它；ChatModel是底层模型抽象，直接对接各厂商SDK，框架开发者才需要碰。

更关键的是 **工具调用的重构** 。

在 [1.x里，每个ChatModel实现都内嵌了自己的私有工具执行循环——OpenAI有一套、Ollama有一套、Anthropic有一套，代码重复、行为不一致、bug各不相同。](http://1.xn--x,chatmodelopenaiollamaanthropic,bug-jg8va3210ngaka19214ahakc42dfa98k8xr0j97fu66btvar31i3maq74v9qdial3466a00vpti6va190g4j5bj42dmajm4287f1r7f2ba2164adfhd9unx5ao96kbyau940bgba6113mq9nake./)

2.0把这些全干掉了，工具执行循环被提升到Advisor链里，统一处理。

```
// Spring AI 2.0的工具调用写法
String response = 
            ChatClient.create(chatModel)
          
    .prompt("明天是星期几？")
    .tools(new DateTimeTools())
    .call()
    .content();
```

**干净、简洁，工具调用、执行循环全部自动处理。**

这个设计最优雅的地方在于： **循环是可组合的** 。

Advisor链支持循环重入——工具调用Advisor可以重新进入下游链。同一套机制还可以用来做结构化输出的重试循环、评估循环等等。

**什么时候用Spring AI？** 如果你的项目是Spring Boot [4.x，团队熟悉Spring生态，需要快速把AI能力接进现有系统——Spring](http://4.xn--x,spring,aispring-212ja2189wz0sado9booa78hy0rl4gvtztx1e0smlokmn5dswm44quj2ehq4b08bnz8gv8g/) AI是最顺滑的选择。

它的自动配置、依赖注入、可观测性，全是Spring那一套。

唯一的代价是Java版本要升到17+（2.0需要21+）。

### 3.2 LangChain4j：JVM上的AI工具箱

LangChain4j从2023年初开始发展，是目前Java生态里模型支持和向量存储支持最丰富的框架。

截至2026年9月，最新版本是1.19.0。

**它和Spring AI的核心区别是什么？**

一句话： **Spring AI追求的是“集成效率”，LangChain4j追求的是“场景能力”** 。

Spring AI胜在Spring生态原生集成，声明式@AiService、自动配置、Spring Boot Starter，全都有。

LangChain4j胜在功能丰富度和灵活度——支持30+模型开箱即用，向量库覆盖最广。

它的Agent机制更成熟，处理多步逻辑更稳。

```
// LangChain4j的声明式AI服务
interface Assistant {
    @SystemMessage("你是一个Java技术顾问，请用中文回答")
    String chat(@UserMessage String question);
}

Assistant assistant = 
            AiServices.create(Assistant
          .class, model);
String answer = 
            assistant.chat(
          "什么是虚拟线程？");
```

**什么时候用LangChain4j？**

如果你需要最丰富的模型和向量存储支持，或者你的项目不是纯Spring（可能用Quarkus、Micronaut或纯Java），LangChain4j是最灵活的选择。

但你要忍受它不够简洁的写法，以及相对较高的学习和使用成本。

**LangChain4j 1.19的一个重要变化是MCP协议进入稳定期** 。

2026年7月28日MCP发布新规范，Streamable HTTP变成无状态的，协议级session被删了，服务器不再靠session id记着谁是谁。

这意味着MCP的集成方式会更标准化。

### 3.3 Solon AI：全场景、全版本兼容

Solon AI是Solon项目的核心子项目之一，定位是 **全场景Java AI开发框架** 。

它最大的特点有两个：

**第一，兼容Java 8到Java 26。**

这在Java AI框架里非常罕见——Spring AI 2.0需要Java 21+，LangChain4j需要Java 17+。

**第二，可以嵌入任意框架。**

它不绑定Solon，可以无缝嵌入Spring Boot、 [Vert.x、Quarkus、JFinal。](http://vert.xn--xquarkusjfinal-552mha./)

```
// Solon AI的构建式API
ChatModel chatModel = 
            ChatModel.of(
          "http://127.0.0.1:11434/api/chat")
    .provider("ollama")
    .model("
            qwen2.5:1.5b"
          )
    .build();

AssistantMessage result = 
            chatModel.prompt(
          "杭州今天天气怎么样？")
    .options(op -> 
            op.toolAdd(
          new WeatherTools()))
    .call()
    .getMessage();
```

**什么时候用Solon AI？**

如果你的项目还在Java 8上运行，或者你需要一个“框架无关”的AI能力层——Solon AI是目前唯一的选择。

在Agent体系上，它提供了三级递进式的智能体架构：SimpleAgent、ReActAgent、TeamAgent。

## Java AI框架选型指南

大家好，我是老张，一名在Java开发这条路上摸爬滚打了10年的架构师。

前阵子帮一个团队做技术评审，遇到了一个特别典型的问题。他们要做一个智能客服系统，团队里三个人吵得不可开交——一个说用Spring AI，理由是“Spring官方出品，肯定稳”；一个说用LangChain4j，理由是“生态最全，什么都能干”；还有一个说用Spring AI Alibaba，理由是“阿里内部验证过的，生产级”。

三个人说的都对，但三个人说的不是一回事。

**因为这三个框架解决的根本不是同一个问题。**

这就是Java AI框架选型最大的坑——你以为你在选“哪个更好”，实际上你在选“哪个更适合你的场景”。而选型这件事，最怕的就是拿着功能列表比参数，比到最后发现选错了层。

今天这篇文章，我就把Java生态里主流的AI框架从头到尾给你拆解一遍。不讲虚的，只讲一件事： **每个框架站在哪一层，解决什么问题，什么时候该用它。**

## 一、先搞清楚：Java AI框架分几层？

很多人选型的时候，把Spring AI、LangChain4j、Spring AI Alibaba、Embabel放在一起比，这本身就是错的。它们不在同一层。

Rod Johnson在发布Embabel的时候，给了一个非常锋利的类比：

| 层级 | 类比 | 代表框架 |
| --- | --- | --- |
| **底层基础设施** | Servlet API | Spring AI / LangChain4j |
| **高级应用框架** | Spring MVC | Embabel |

什么意思？ **Spring AI和LangChain4j解决的是“怎么连上LLM、怎么管Embedding、怎么接向量库”这类管道问题。Embabel解决的是“怎么让智能体在复杂业务流程里可靠、可解释、确定性地完成多步骤任务”这类编排问题。**

两者是互补关系，不是竞争关系。

再往上，Spring AI Alibaba解决的是“怎么在Spring生态里构建企业级多智能体和工作流编排”的问题。AgentScope解决的是“怎么让Agent在企业级分布式环境里长期稳定运行”的问题。Solon AI解决的是“怎么在Java 8到Java 26的全版本范围内、在任意框架里嵌入AI能力”的问题。

**一句话说清：选型的第一步不是“选哪个框架”，而是“搞清楚你需要哪一层的框架”。**

## 二、一张图看懂Java AI框架的层级定位

```
flowchart TB
    subgraph L1[底层基础设施层<br>怎么接入AI]
        A1[Spring AI<br>Spring生态的AI抽象层]
        A2[LangChain4j<br>JVM上的AI工具箱]
        A3[Solon AI<br>全场景AI开发框架]
    end

    subgraph L2[Agent编排层<br>怎么组织AI干活]
        B1[Spring AI Alibaba<br>企业级多智能体与工作流]
        B2[AgentScope<br>企业级分布式Agent]
        B3[Embabel<br>确定性GOAP编排]
    end

    L1 --> L2
```

这张图是整篇文章的骨架。下面我逐层拆解。

## 三、第一层：底层基础设施——怎么接入AI

这一层解决的核心问题是： **怎么把大模型、向量数据库、Embedding、工具调用这些基础能力，用Java的方式接进你的项目。**

### 3.1 Spring AI 2.0：Spring生态的官方答案

Spring AI 2.0.0 GA于2026年6月12日正式发布，基于Spring Boot 4.1和Spring Framework 7.0构建。

**它最大的变化是什么？**

Spring AI [1.x里，ChatClient和ChatModel的边界很模糊，很多人直接@Autowired](http://1.x%E9%87%8C%EF%BC%8CChatClient%E5%92%8CChatModel%E7%9A%84%E8%BE%B9%E7%95%8C%E5%BE%88%E6%A8%A1%E7%B3%8A%EF%BC%8C%E5%BE%88%E5%A4%9A%E4%BA%BA%E7%9B%B4%E6%8E%A5@autowired/) ChatModel来用，工具调用、重试、内存管理全往里塞。2.0把这个边界明确了：ChatClient是面向用户的高层API，内置Advisor链，日常业务开发用它；ChatModel是底层模型抽象，直接对接各厂商SDK，框架开发者才需要碰。

更关键的是 **工具调用的重构** 。在 [1.x里，每个ChatModel实现都内嵌了自己的私有工具执行循环——OpenAI有一套、Ollama有一套、Anthropic有一套，代码重复、行为不一致、bug各不相同。2.0把这些全干掉了，工具执行循环被提升到Advisor链里，统一处理。](http://1.xn--x,chatmodelopenaiollamaanthropic,bug-jg8va3210ngaka19214ahakc42dfa98k8xr0j97fu66btvar31i3maq74v9qdial3466a00vpti6va190g4j5bj42dmajm4287f1r7f2ba2164adfhd9unx5ao96kbyau940bgba6113mq9nake.2.xn--0,advisor,-zf2p43c1ho27argr3irvg1t6axfvrqclzjvpr1wal5q5zbhw8sr6bs23k7dzcrlcuz3g5bnivz./)

```
// Spring AI 2.0的工具调用写法
String response = 
            ChatClient.create(chatModel)
          
    .prompt("明天是星期几？")
    .tools(new DateTimeTools())
    .call()
    .content();
```

**干净、简洁，工具调用、执行循环全部自动处理。**

这个设计最优雅的地方在于： **循环是可组合的** 。Advisor链支持循环重入——工具调用Advisor可以重新进入下游链。同一套机制还可以用来做结构化输出的重试循环、评估循环等等。

**什么时候用Spring AI？** 如果你的项目是Spring Boot [4.x，团队熟悉Spring生态，需要快速把AI能力接进现有系统——Spring](http://4.xn--x,spring,aispring-212ja2189wz0sado9booa78hy0rl4gvtztx1e0smlokmn5dswm44quj2ehq4b08bnz8gv8g/) AI是最顺滑的选择。它的自动配置、依赖注入、可观测性，全是Spring那一套。唯一的代价是Java版本要升到17+（2.0需要21+）。

### 3.2 LangChain4j：JVM上的AI工具箱

LangChain4j从2023年初开始发展，是目前Java生态里模型支持和向量存储支持最丰富的框架。截至2026年9月，最新版本是1.19.0。

**它和Spring AI的核心区别是什么？**

一句话： **Spring AI追求的是“集成效率”，LangChain4j追求的是“场景能力”** 。

Spring AI胜在Spring生态原生集成，声明式@AiService、自动配置、Spring Boot Starter，全都有。LangChain4j胜在功能丰富度和灵活度——支持30+模型开箱即用，向量库覆盖最广。它的Agent机制更成熟，处理多步逻辑更稳。

```
// LangChain4j的声明式AI服务
interface Assistant {
    @SystemMessage("你是一个Java技术顾问，请用中文回答")
    String chat(@UserMessage String question);
}

Assistant assistant = 
            AiServices.create(Assistant
          .class, model);
String answer = 
            assistant.chat(
          "什么是虚拟线程？");
```

**什么时候用LangChain4j？** 如果你需要最丰富的模型和向量存储支持，或者你的项目不是纯Spring（可能用Quarkus、Micronaut或纯Java），LangChain4j是最灵活的选择。但你要忍受它不够简洁的写法，以及相对较高的学习和使用成本。

### 3.3 Solon AI：全场景、全版本兼容

Solon AI是Solon项目的核心子项目之一，定位是 **全场景Java AI开发框架** 。它最大的特点有两个：

**第一，兼容Java 8到Java 26。** 这在Java AI框架里非常罕见——Spring AI 2.0需要Java 21+，LangChain4j需要Java 17+。

**第二，可以嵌入任意框架。** 它不绑定Solon，可以无缝嵌入Spring Boot、 [Vert.x、Quarkus、JFinal。](http://vert.xn--xquarkusjfinal-552mha./)

```
// Solon AI的构建式API
ChatModel chatModel = 
            ChatModel.of(
          "http://127.0.0.1:11434/api/chat")
    .provider("ollama")
    .model("
            qwen2.5:1.5b"
          )
    .build();

AssistantMessage result = 
            chatModel.prompt(
          "杭州今天天气怎么样？")
    .options(op -> 
            op.toolAdd(
          new WeatherTools()))
    .call()
    .getMessage();
```

**什么时候用Solon AI？** 如果你的项目还在Java 8上运行，或者你需要一个“框架无关”的AI能力层——Solon AI是目前唯一的选择。在Agent体系上，它提供了三级递进式的智能体架构：SimpleAgent、ReActAgent、TeamAgent。

## 四、第二层：Agent编排

这一层解决的核心问题是： **当AI需要多步骤推理、工具调用、多Agent协作时，怎么让流程可控、可解释、可恢复。**

### 4.1 Spring AI Alibaba：企业级多智能体与工作流编排

Spring AI Alibaba由Spring开源社区和Alibaba开源社区共同维护，2024年9月开源，目前GitHub Star数已超过 **10,000** 。

项目基于Spring AI构建，是阿里云通义系列模型及服务在Java AI应用开发领域的最佳实践。

**它的核心定位是什么？**

Spring AI Alibaba在Spring AI的基础上做了 **向上抽象和功能增强** 。

Spring AI提供AI应用的基础抽象——模型接入、函数调用、MCP、对话记忆、RAG、可观测。

Spring AI Alibaba在此基础上补充了 **Agent编排、Graph工作流引擎、MCP双端支持和企业级治理** 。

用一句话说清区别： **Spring AI解决“怎么调用模型”，Spring AI Alibaba解决“怎么让多个Agent协同完成复杂业务流程”。**

它的架构分为三层：

- **Agent Framework** 以ReactAgent为核心，提供Agent开发框架；
- **Graph** 是低级别的工作流和多代理协调框架，是Agent Framework的底层运行时基座；
- **Augmented LLM** 以Spring AI的原子抽象为基础，提供模型、工具、MCP、向量存储等基础能力。
```
// Spring AI Alibaba创建Agent
DashScopeApi dashScopeApi = 
            DashScopeApi.builder()
          
    .apiKey(
            System.getenv(
          "AI_DASHSCOPE_API_KEY"))
    .build();
ChatModel chatModel = 
            DashScopeChatModel.builder()
          
    .dashScopeApi(dashScopeApi)
    .build();

ReactAgent agent = 
            ReactAgent.builder()
          
    .name("weather_agent")
    .model(chatModel)
    .instruction("You are a helpful weather forecast assistant.")
    .build();

            agent.call(
          "what is the weather in Hangzhou?");
```

**Spring AI Alibaba 1.1.2.0版本带来了两个关键能力升级** ：

**Agent Skills** ——ReactAgent集成了Agent Skills能力，支持以“技能”为单位做可复用指令与上下文的渐进式披露。系统提示中先只注入技能列表，模型在需要某技能时才加载完整内容，从而 **降低Token消耗、扩展能力规模** 。

**多智能体并行执行** ——LlmRouting、Supervisor等模式既可路由到单一子智能体，也可一次选择多个子智能体并 **并行执行** ，便于做多领域并行查询与结果汇总。

**什么时候用Spring AI Alibaba？**

如果你的项目是Spring Boot，需要构建 **企业级多智能体系统** 或 **工作流编排** ——比如智能客服、审批流、数据管道——Spring AI Alibaba是目前最完整的选择。

它同时具备Spring生态的集成优势和阿里云基础设施的深度适配（通义千问、百炼、Higress AI网关、Nacos等）。

### 4.2 AgentScope Java 2.0：企业级分布式Agent底座

AgentScope Java 2.0于2026年6月正式发布，是阿里巴巴集团内部使用最广泛的智能体框架（Java & Python），在十余条核心业务线生产环境深度使用。

**它的核心思路是什么？**

基于ReActAgent推理内核，增加一个 **Harness工程化层** 。

开发者既可以继续使用轻量的ReAct循环，也可以按需启用Workspace、持久记忆、Session、Sandbox、Skill和Subagent等能力，将同一套Agent逻辑落地部署到企业级分布式服务中。

```
// AgentScope HarnessAgent
var agent = 
            HarnessAgent.builder()
          
    .name("coder")
    .model("dashscope:qwen-max")
    .workspace(
            Paths.get(
          ".agentscope/workspace"))
    .filesystem(new DockerFilesystemSpec())
    .isolationScope(
            IsolationScope.USER)
          
    .build();

            agent.call(msg,
           
            RuntimeContext.builder()
          
    .sessionId("demo")
    .userId("alice")
    .build()).block();
```

**AgentScope最核心的差异化能力是什么？**

三个词： **身份持续、上下文可控、状态可恢复** 。

工作区即Agent的人格和长期记忆，每轮自动注入；

上下文自动压缩，大工具结果自动落盘，ContextOverflow兜底重试；

同sessionId可跨进程恢复完整对话，沙箱状态可快照。

**什么时候用AgentScope？**

如果你要构建的是企业级多Agent系统，需要长期稳定运行、需要多租户隔离、需要工具调用权限管控——AgentScope是目前Java生态里最完整的选择。

### 4.3 Embabel：把“规划”从LLM手里抢回来

Embabel是Spring之父Rod Johnson打造的JVM原生智能体框架，2026年8月发布1.0.0 GA版本。

**它解决的核心问题是什么？**

用Rod Johnson自己的话说： **“自从我创立Spring以来，从没这么确信一个新项目是必要的。”**

Embabel的核心设计是引入 **GOAP（Goal-Oriented Action Planning）目标导向规划算法** ——一种传统上用于游戏AI的规划算法。

它不是按照脚本或预先连线的图来执行，而是为智能体提供一组可用的Action，每个Action带有前置条件与效果，规划器搜索满足目标的动作序列。

**这跟其他框架最大的区别是什么？**

**规划不依赖LLM。**

大部分AI Agent框架的规划步骤是让LLM来决定“下一步该做什么”。

但LLM是有幻觉的、是不确定的。Embabel把规划这件事交给确定性的GOAP算法——它根据Action的前置条件和效果计算最优路径，并说明为什么选择这条路径。

Embabel构建在Spring AI之上，直接吃Spring AI的模型连接能力，所以Spring AI生态里的@Tool、ChatClient那套你都能继续用。

**什么时候用Embabel？**

如果你的场景需要 **可解释、可审计、确定性的多步骤任务编排** ——比如金融合规、医疗决策、供应链调度——Embabel的GOAP规划比其他框架的LLM驱动规划更可靠。

## 五、一张表看懂所有框架的定位

| 框架 | 层级 | 核心定位 | Java版本 | 框架依赖 | 最适合 |
| --- | --- | --- | --- | --- | --- |
| **Spring AI** | 基础设施 | Spring生态AI抽象层 | 21+ | 强依赖Spring Boot | Spring Boot项目快速接入AI |
| **LangChain4j** | 基础设施 | JVM上的AI工具箱 | 17+ | 框架中立 | 需要丰富模型/向量库支持 |
| **Solon AI** | 基础设施 | 全场景AI开发框架 | **8-26** | 可嵌入任意框架 | Java 8项目、框架无关场景 |
| **Spring AI Alibaba** | Agent编排 | 企业级多智能体与工作流 | 17+ | 基于Spring AI | 多Agent协作、工作流编排 |
| **AgentScope** | Agent编排 | 企业级分布式Agent | 17+ | 框架中立 | 多Agent协作、生产级部署 |
| **Embabel** | Agent编排 | 确定性GOAP编排 | 17+ | 基于Spring AI | 可审计、确定性的流程编排 |

## 六、选型的决策逻辑

看到这里，你应该已经发现了： **没有“最好的框架”，只有“最匹配你场景的框架”。**

我按常见的决策路径，给你梳理一下。

### 6.1 第一个问题：你的项目是什么技术栈？

![图片](assets/Java%20AI%E6%A1%86%E6%9E%B6%E9%80%89%E5%9E%8B%E6%8C%87%E5%8D%97/610a20cf964980e71bc559a6521d39e0_MD5.jpg)

### 6.2 第二个问题：你的场景需要什么？

![图片](assets/Java%20AI%E6%A1%86%E6%9E%B6%E9%80%89%E5%9E%8B%E6%8C%87%E5%8D%97/24b1f5087a26ba0d043bd1f4281cc9c0_MD5.jpg)

### 6.3 三个关键判断

**判断一：你的Java版本是多少？**

如果还在Java 8或11上，Spring AI 2.0和LangChain4j都用不了。

Solon AI是唯一的选择。

**判断二：你的项目是单体还是分布式？**

如果是单体应用或简单微服务，Spring AI或LangChain4j足够了。

如果要做企业级多Agent分布式系统，Spring AI Alibaba或AgentScope的工程化层是刚需。

**判断三：你的场景需要“确定性”吗？**

如果你在金融、医疗、政务等需要审计和合规的场景，Embabel的GOAP规划比LLM驱动的规划更可靠—— **因为它的每一步决策都是可追溯、可解释的** 。

## 七、优缺点

### Spring AI 2.0

**优点** ：Spring官方出品，与Spring Boot [4.x深度集成；Advisor链设计优雅，工具调用可组合；自动配置、可观测性完善。](http://4.xn--x;advisor,;-2e3jy265a36g0wep8fda06by4vjy7ankk97ds7k1kmdy4ezrdir8dbi6c79ddqxwl1dsrml1ag1eh22fu01ad0nya./)

**缺点** ：强依赖Spring Boot [4.x和Java](http://4.xn--xjava-rn9h/) 21+；不支持Java 8/11/17；非Spring项目使用不便。

**适用场景** ：Spring Boot [4.x项目快速接入AI。](http://4.xn--xai-1v1ez77dt9emm3bde6byyp./)

### LangChain4j

**优点** ：30+模型开箱即用，向量库覆盖最广；框架中立，可搭配任意Java框架；MCP协议支持成熟。

**缺点** ：写法不够简洁，学习成本较高；版本迭代快，API稳定性不如Spring AI。

**适用场景** ：需要丰富模型/向量库支持，或非Spring项目。

### Solon AI

**优点** ： **唯一支持Java 8到Java 26的框架** ；可嵌入Spring Boot、 [Vert.x、Quarkus；三级Agent架构。](http://vert.xn--xquarkus;agent-552mi280bqs4dyzab203a./)

**缺点** ：生态和社区规模不如Spring AI和LangChain4j；中文文档为主。

**适用场景** ：Java 8/11项目，或需要框架无关的AI能力层。

### Spring AI Alibaba

**优点** ： **Spring AI + 阿里云基础设施的完整组合** ；Agent Framework + Graph工作流引擎；Agent Skills支持，渐进式披露降低Token消耗；多智能体并行执行；深度适配通义千问、百炼、Higress AI网关、Nacos等。

**缺点** ：相对较新（2024年9月开源），生态还在建设；主要面向Spring生态，非Spring项目使用不便。

**适用场景** ：Spring Boot项目构建企业级多智能体系统、工作流编排。

### AgentScope

**优点** ：阿里十余条业务线生产验证；Harness工程化层提供Workspace、持久记忆、沙箱隔离、权限管控；分布式部署支持。

**缺点** ：概念较多，学习曲线较陡；主要面向企业级场景，简单场景可能过度设计。

**适用场景** ：企业级多Agent分布式系统。

### Embabel

**优点** ：GOAP确定性规划，不依赖LLM；可解释、可审计；构建在Spring AI之上，可直接复用。

**缺点** ：核心用Kotlin编写（但Java完全兼容）；相对较新，生态还在建设。

**适用场景** ：金融合规、医疗决策等需要确定性编排的场景。

## 八、写在最后

回到最初的问题： **Java AI框架到底怎么选？**

我的建议是 **三步走** ：

**第一步：搞清楚你站在哪一层。**

你是要“接入AI”（基础设施层），还是要“组织AI干活”（Agent编排层）？两个问题的答案完全不同。

**第二步：搞清楚你的约束条件。**

Java版本是什么？框架是什么？团队熟悉什么？数据合规要求是什么？把这些约束列出来，可选范围立刻缩小一半。

**第三步：搞清楚你的核心场景。**

RAG、多Agent协作、工作流编排、确定性编排、简单接入——每个场景匹配的框架不一样。

**最忌讳的选型方式，是拿功能列表比参数。**

“Spring AI有15个向量库，LangChain4j有30个，所以LangChain4j更好”——这种比较没有意义。

**30个向量库你可能只用得上一个，多出来的15个只是负担。**

**真正该问的问题是：我的项目最需要什么能力，哪个框架在这个能力上最强？**

选框架跟选工具一样， **合适的才是最好的** 。

## 九、参考资源

- **Spring AI官方文档** ： [https://docs.spring.io/spring-ai](https://docs.spring.io/spring-ai)
- **LangChain4j官方文档** ： [https://docs.langchain4j.dev](https://docs.langchain4j.dev/)
- **Solon AI官方文档** ： [https://solon.noear.org](https://solon.noear.org/)
- **Spring AI Alibaba官方文档** ： [https://java2ai.com](https://java2ai.com/)
- **Spring AI Alibaba GitHub** ： [https://github.com/alibaba/spring-ai-alibaba](https://github.com/alibaba/spring-ai-alibaba)
- **AgentScope Java官方文档** ： [https://java.agentscope.io](https://java.agentscope.io/)
- **Embabel官方文档** ： [https://docs.embabel.com](https://docs.embabel.com/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)