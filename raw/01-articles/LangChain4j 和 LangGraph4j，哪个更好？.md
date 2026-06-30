---
title: "LangChain4j 和 LangGraph4j，哪个更好？"
source: "https://mp.weixin.qq.com/s/X2OqUtGZag264Gv9ToF55w"
---
苏三 苏三说技术 *2026年6月30日 08:35*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

## 前言

最近这几个月，AI Agent 技术简直火得一塌糊涂。

GitHub Copilot、Cursor、Claude Code 这些工具已经把“AI 辅助编程”这件事推到了一个新的高度。

但当我们回头看 Java 生态，AI 智能体开发这个赛道上，出现了两个绕不开的名字—— **LangChain4j** 和 **LangGraph4j** 。

很多小伙伴跑来问我：“三哥，这两个到底有什么区别？我该选哪个？”

这个问题问得太到位了。

Java 开发者做 AI 智能体，确实面临着和当初做微服务时完全一样的选择困境。

今天这篇文章就专门跟大家一起聊聊这个话题，希望对你会有所帮助。

## 一、先搞清楚它们到底是谁

在开始对比之前，我们需要先明白一件事： **LangChain4j 和 LangGraph4j 不是竞品，而是“能力接入层”和“流程编排层”的关系。**

### LangChain4j

它让 Java 应用“会说话”。

LangChain4j 是 LangChain 的 Java 移植版，本质上是一个 **Java LLM 应用开发框架** ，目的是让 Java 开发者能够方便地接入各种大语言模型和 AI 能力。

它提供了以下核心能力：

- 统一的模型调用接口（支持 OpenAI、Google Vertex AI、Ollama、DeepSeek、通义千问等 20+ 模型）
- Embeddings 和向量检索
- RAG（检索增强生成）
- Tool Calling（让模型能调用你的 Java 方法）
- AiServices 高层 API（让你用声明式的方式定义 AI 服务）

打个比方，LangChain4j 就是你工具箱里的“ **AI 能力接入层** ”，负责解决“能不能用”的问题。

### LangGraph4j

它让多个 AI 智能体“协作干活”。

LangGraph4j 是 LangGraph（Python 端）的 Java 移植版，是一个用于构建 **有状态、多智能体工作流** 的图式编排框架。

它的核心能力包括：

- 有向状态图（StateGraph）编排
- 条件分支和循环控制
- 多智能体协作（Supervisor Pattern、Fan-out 等）
- 检查点和断点恢复（Checkpointing）
- 并行执行节点
- Human-in-the-Loop（人工介入）

如果说 LangChain4j 是工具箱里的“零件”，那么 LangGraph4j 就是那张“ **搭积木的图纸和流水线** ”，负责解决“怎么编排更复杂”的问题。

![图片](assets/LangChain4j%20%E5%92%8C%20LangGraph4j%EF%BC%8C%E5%93%AA%E4%B8%AA%E6%9B%B4%E5%A5%BD%EF%BC%9F/ba4b595dbbae5bdd09f66e8acf1af5f0_MD5.png)

从这张图可以看得很清楚： **它们不是“谁替代谁”的关系，而是不同层级、相互配合的关系。**

## 二、深入对比

### 2.1 LangChain4j—零件箱 + 接口适配层

LangChain4j 关注的核心问题是：“ **如何把大模型的能力接入 Java 应用。** ”

它的设计哲学是 **模块化、低耦合、声明式** 。

你可以把它的功能拆解成几个核心模块：

| 模块 | 能力 | 典型场景 |
| --- | --- | --- |
| **ChatModel** | 统一对话模型接口，支持流式输出 | 聊天机器人、智能助手 |
| **EmbeddingModel** | 文本向量化，对接多种向量数据库 | RAG 检索、相似度匹配 |
| **Tool Calling** | 将 Java 方法暴露给 LLM 调用 | 查询天气、查数据库、发邮件 |
| **AiServices** | 声明式定义 AI 服务，一行代码搞定 | 快速搭建 AI 应用原型 |
| **MCP** | 多链协同协议 | 多步复杂任务编排 |

LangChain4j 对 RAG 的支持尤其强大，内置了 30+ 种向量数据库的适配。

这意味着你不需要关心底层用的是什么向量库——PgVector、Milvus、Elasticsearch，通通都能接。

**代码示例：用 AiServices 声明一个 AI 服务**

```
// 第一步：定义一个接口，声明你要 AI 做什么
public interface Assistant {
    String chat(@UserMessage String message);
}

// 第二步：让 AiServices 帮你实现这个接口
Assistant assistant = 
            AiServices.builder(Assistant
          .class)
        .chatLanguageModel(OpenAiChatModel.withApiKey("sk-xxx"))
        .build();

// 第三步：直接调用
String reply = 
            assistant.chat(
          "Java 中 ConcurrentHashMap 的工作原理是什么？");

            System.out.println(reply);
```

看到没？

你只需要定义一个接口，AiServices 会自动帮你处理模型调用、消息构建、响应解析。

这就是 LangChain4j 的“声明式”力量——把 AI 服务当成普通 Java 接口来用。

### 2.2 LangGraph4j——流程引擎 + 状态机

LangGraph4j 关注的核心问题是：“ **如何把多个 AI 智能体的决策和行动流程化、状态化。** ”

它的设计哲学是 **图即代码、状态即共享内存、节点即智能体行为** 。核心概念有三样：

**① State（状态）——共享笔记本**

LangGraph4j 强制所有智能体围绕一个共享的 `AgentState` 对象工作。这个 State 不是普通的 Map，而是具备类型安全、变更追踪、不可变快照能力的数据对象。

```
// 这就是你的共享笔记本！所有节点都靠它存数据、读数据、传数据
class MyState extends AgentState {
    String userQuestion;      // 用户问什么
    String weatherInfo;       // 查到的天气结果
    String aiAnswer;          // AI 最终回答
    List<String> toolCalls;   // 需要调用的工具列表
}
```

State 的设计极大简化了多节点之间的数据传递——节点之间不直接说话，只读写这个笔记本，下游节点自然就能拿到上游节点的处理结果。

**② StateGraph（状态图）——可执行的流程图**

StateGraph 是 LangGraph4j 的核心抽象：你在纸上画流程图、写节点逻辑、画箭头，它帮你编译成“可运行程序”。

```
// 构建一个思考→行动→回答的三步 Agent 工作流
StateGraph<MyState> graph = new StateGraph<>(MyState.class)
        .addNode("think", this::thinkNode)      // 思考节点：调用 LLM 分析意图
        .addNode("act", this::actNode)          // 行动节点：执行工具调用
        .addNode("answer", this::answerNode)    // 回答节点：生成最终答案
        // 条件边：根据 State 决定下一步走哪条路
        .addConditionalEdges("think", this::routeAfterThink)
        .addEdge("act", "answer")
        .addEdge("answer", END);
```
```
// 条件路由函数 —— 看一眼笔记本，决定下一步怎么走
private String routeAfterThink(MyState state) {
    if (
            state.toolCalls
           != null && !
            state.toolCalls.isEmpty())
           {
        return "act";  // 有工具要调用 → 走行动节点
    }
    return "answer";   // 没有 → 直接回答
}
```

这里的“条件边”是整个框架的灵魂。它不是静态配置，而是可以动态计算的路由逻辑——State 里有什么数据，决定下一步走哪个节点。

**③ Checkpointing（检查点）——不怕系统崩溃**

这是 LangGraph4j 在生产环境中最“救命”的特性。

每次 State 更新后，框架会 **自动序列化全量状态和执行上下文** （包含 token 消耗、耗时、节点 ID、时间戳）到持久化存储。

一旦系统崩溃，你可以精准恢复到最后成功的检查点，重试失败的节点，而不是全链路重跑。

## 三、用一个例子看懂差异

### 3.1 用 LangChain4j做一个简单的智能体

做一个能调用工具的简单 Agent，LangChain4j 的代码非常简洁：

```
// 第一步：定义一个工具（Java 方法 + 注解）
publicclass WeatherTool {
    @Tool("获取某个城市的当前天气")
    String getWeather(@P("城市名称") String city) {
        // 真实场景下这里会调用天气 API
        return city + "今天 25°C，晴朗";
    }
}

// 第二步：构建 Agent
ChatLanguageModel model = 
            OpenAiChatModel.builder()
          
        .apiKey("sk-xxx")
        .build();

Agent agent = 
            Agent.builder(model)
          
        .tools(new WeatherTool())
        .build();

// 第三步：执行
String response = 
            agent.execute(
          "北京今天天气怎么样？");

            System.out.println(response);
          
// 输出：北京今天 25°C，晴朗
```

LangChain4j 的简洁就在于： **一个 `@Tool` 注解 + 几行配置，模型就能自动识别“需要查天气”并调用你的 Java 方法。**

### 3.2 用 LangGraph4j做一个带条件的多智能体

当场景变得复杂——比如需要先分析意图、再决定走哪个子流程、结果不满意还要重试——LangGraph4j 就派上用场了：

```
// 定义共享状态
class CodeReviewState extends AgentState {
    String prDescription;          // PR 描述
    String codeContent;            // 代码内容
    String reviewResult;           // 审查结果
    int reviewAttempts;            // 重试次数
    boolean needsImprovement;      // 是否需要改进
}

// 构建评审图
StateGraph<CodeReviewState> graph = new StateGraph<>(CodeReviewState.class)
        .addNode("analyze", this::analyzePr)        // 分析 PR
        .addNode("review", this::reviewCode)        // 审查代码
        .addNode("improve", this::suggestFix)       // 建议改进
        .addNode("approve", this::approve)          // 批准合并
        .addConditionalEdges("review", state -> {
            if (
            state.reviewResult.contains(
          "严重问题")) {
                return"improve";    // 有问题 → 改进
            }
            return"approve";         // 没问题 → 批准
        })
        .addEdge("improve", "review")                // 改进完重新审查（循环！）
        .build();
```

这个例子展示了 LangGraph4j 的核心优势：

- **循环控制** ： `improve → review` 循环，问题没解决就一直修
- **条件分支** ：根据 reviewResult 的内容动态决定下一步
- **状态共享** ：所有节点共享 `CodeReviewState` ，reviewAttempts 用来控制重试次数

### 3.3 一句话总结差异

| 场景 | 用 LangChain4j | 用 LangGraph4j |
| --- | --- | --- |
| “给模型一个提示词，让它回答” | ✅ 极简 | ❌ 过度设计 |
| “一个智能体+几个工具” | ✅ 刚刚好 | ⚠️ 稍重 |
| “多步决策+条件分支” | ⚠️ 需要手动管理状态 | ✅ 原生支持 |
| “多智能体协作+长流程+断点恢复” | ❌ 难以实现 | ✅ 设计目标 |

你可能也注意到了——LangChain4j 管的是“一次 AI 调用怎么优雅”，而 LangGraph4j 管的是“几十个智能体怎么协同走完整个业务流程”。它们是互补的，不是对立的。

## 四、LangGraph4j 的独特优势

如果说 LangChain4j 是“单兵作战”的利器，那 LangGraph4j 就是“多兵种协同”的总指挥部。

除了上面看到的分支和循环控制，LangGraph4j 还提供了几种极其强大的多智能体协作模式：

**Supervisor Pattern（主控模式）** ：一个主控 Agent 决定把任务分配给哪个专家 Agent 去执行。主控 Agent 分析用户意图，调用合适的 Worker Agent，并行处理子任务。

**Fan-out（扇出模式）** ：把同一个任务分发给多个子 Agent 并行处理，然后汇总所有结果。在做“多方观点分析”或“跨来源验证”时，这个模式非常有价值。

**Human-in-the-Loop（人机协作）** ：节点执行到敏感步骤时自动暂停，把状态推送给人工审批，等待人工响应后再继续后续流程。LangGraph4j 内置了对这种模式的原生支持。

**Checkpointing + Time Travel** ：支持断点恢复和时间旅行式调试——你可以回溯到任何一个历史检查点，分析当时的 State，定位 LLM 幻觉或逻辑错误。

除了这些，LangGraph4j 还有更高级的能力：

- **并行节点执行** ：多个独立任务可以并行运行，提升吞吐量。
- **子图嵌套** ：可以把一个完整的 Graph 当作另一个 Graph 的节点，实现模块化复用。
- **持久化检查点** ：支持 Redis、PostgreSQL 作为检查点存储后端，跨服务重启也能恢复。
- **可视化工具** ：基于 Graphviz 生成可交互的 SVG 流程图。

## 五、优缺点全方位对比

### LangChain4j 的优点

- **功能全面、开箱即用** ：聊天气泡、向量检索、RAG、工具调用，你要的全都有。
- **生态强大** ：天然支持 Spring Boot，可无缝集成现有 Java 中间件系统。
- **声明式 API** ：AiServices 一行注解就能定义整个 AI 服务，把 AI 调用变成 Java 接口调用。
- **低学习成本** ：API 设计直观，文档齐全，Java 开发者几乎零障碍上手。
- **模型选择丰富** ：支持 OpenAI、Azure OpenAI、Google Vertex AI、Anthropic Claude、Ollama、DeepSeek、通义千问等 20+ 种模型。

### LangChain4j 的局限性

- **Agent 编排能力有限** ：虽然支持基础的多步骤执行，但复杂工作流的编排和状态管理能力远不如 LangGraph4j。
- **无内置状态管理** ：多轮对话和复杂上下文传递需要开发者自己维护状态。
- **复杂文档处理受限** ：内置向量检索模块仅支持单级索引，对表格、图表等多模态文档的处理能力有限。

### LangGraph4j 的优点

- **状态图编排，表达能力极强** ：支持循环、条件分支、并行执行、子图嵌套，图灵完备的控制流。
- **强大的多智能体协作能力** ：Supervisor 模式、Fan-out 扇出、Human-in-the-Loop 三大模式覆盖了 90% 的企业级多智能体场景。
- **生产级可靠性保障** ：检查点机制 + 断点恢复，系统崩溃后不丢进度，对金融、政务等强一致性场景极其重要。
- **框架无关，自由组合** ：LangGraph4j 提供了框架无关的核心抽象，可以与 LangChain4j 或 Spring AI 任意搭配使用。

### LangGraph4j 的局限性

- **不提供 AI 能力接入** ：它只负责“编排”，不负责“调用模型”。模型调用必须依赖 LangChain4j 或 Spring AI 来补充。
- **学习曲线较陡** ：Graph、State、Node、Edge、Checkpoint 等概念很多，上手难度高于 LangChain4j。
- **版本相对较新** ：目前稳定版本 1.7.10 / 1.8-beta，生态不如 LangChain4j 成熟。

## 六、2026 年最新版本状态

截至 2026 年上半年，两个框架都处于积极更新状态：

| 框架 | 最新版本 | 发布时间 | 主要更新 |
| --- | --- | --- | --- |
| **LangChain4j** | 1.11.0 | 2026-02-04 | 多模型支持增强、RAG 优化、MCP 模块完善 |
| **LangGraph4j** | 1.7.10 / 1.8-beta | 2026-01 | Hooks 机制、异步节点、并行执行优化、Checkpointing 增强 |

LangChain4j 的版本更新更偏向功能完善，LangGraph4j 则是逐步迈向稳定生产级别的路线。

## 七、一张表看清所有差异

| 对比维度 | LangChain4j | LangGraph4j |
| --- | --- | --- |
| **核心定位** | AI 能力接入层——“零件箱” | Agent 工作流编排层——“图纸” |
| **核心抽象** | ChatModel、AiServices、Tool | StateGraph、Node、Edge、Checkpoint |
| **状态管理** | 无内置，需自行维护 | 强制 AgentState，类型安全、版本化、可回溯 |
| **条件路由** | 有限的 if-else 逻辑 | 条件边，支持复杂动态路由 |
| **循环支持** | 有限的递归 | 原生循环边，图灵完备 |
| **多智能体协作** | 基础的多实例调用 | Supervisor + Worker + Fan-out + HITL |
| **断点/检查点** | 无 | 内置，支持 Redis/PostgreSQL 持久化 |
| **并发执行** | 需要手动编排 | 原生并行节点、边 |
| **模型支持** | 20+ 种，统一接口 | 框架无关，依赖 LangChain4j 或 Spring AI |
| **学习曲线** | 低 | 中等偏高 |
| **版本成熟度** | 高（1.11.0） | 中（1.7.10） |
| **Gradle/Maven集成** | 成熟 | 成熟 |
| **Spring Boot集成** | 原生支持 | 通过适配模块支持 |
| **可视化支持** | 一般 | 基于 Graphviz 生成可交互图谱 |

## 八、适用场景

### 纯用 LangChain4j 就够了

| 场景 | 典型应用 |
| --- | --- |
| 智能客服 / FAQ 问答系统 | 意图识别 + 知识库问答 |
| RAG 知识库检索 | 文档问答、企业内部知识助手 |
| 单 Agent + 工具调用 | 订阅邮件发送、通知查询、简单 CRUD 任务 |
| 快速原型验证 | 一周内验证 AI 想法，概念验证 |
| 需要精细控制、低耦合的场景 | 已有复杂系统，只需小范围引入 AI 能力 |

对于这些场景，LangChain4j 开箱即用的能力 + 低学习成本是完全的优势。

### 需要 LangGraph4j 强力入场

| 场景 | 典型应用 |
| --- | --- |
| 复杂多轮决策 + 多智能体协作 | 代码 Review 多智能体系统、供应链智能调度 |
| 长流程审批 + 人机协作 | 项目审核系统、高危 SQL 审批、金融订单审核 |
| 需要断点恢复的长周期任务 | 舆情监测智能体（可能运行数小时甚至数天） |
| 多个 Agent 并行执行 + 分阶段汇总 | 多方观点分析、跨来源信息验证 |
| 从 Python LangGraph 迁移 | 保持相同的图编排逻辑，技术栈换 Java |

在这些场景中，LangGraph4j 提供的能力是 LangChain4j 单独使用时很难实现的。

### 最佳实践组合

最优雅的方案永远不是“二选一”。在实际项目里， **LangChain4j + LangGraph4j** 是非常常见的组合方式：

- **LangChain4j 负责** ：模型调用、RAG 检索、Tool 定义、向量化存储
- **LangGraph4j 负责** ：状态图编排、多 Agent 协调、断点恢复、流程路由
![图片](assets/LangChain4j%20%E5%92%8C%20LangGraph4j%EF%BC%8C%E5%93%AA%E4%B8%AA%E6%9B%B4%E5%A5%BD%EF%BC%9F/9dc2224318ebda7fb4574d99a9916cb1_MD5.png)

LangGraph4j 官方路线也是这个思路：提供框架无关的核心抽象，通过适配模块分别适配 LangChain4j 和 Spring AI 的接口规范。

也就是说，不管你底层用 LangChain4j 还是 Spring AI，图编排的逻辑都是一样的，切换底层不需要改图。

## 九、快速上手

### LangChain4j

- **GitHub** ： [https://github.com/langchain4j/langchain4j](https://github.com/langchain4j/langchain4j)
- **官方文档** ： [https://docs.langchain4j.dev](https://docs.langchain4j.dev/)
- **最新版本** ：1.11.0（2026-02-04）
- **Maven 依赖** ：
```
<dependency>
    <groupId>
            dev.langchain4j
          </groupId>
    <artifactId>langchain4j</artifactId>
    <version>1.11.0</version>
</dependency>
```

### LangGraph4j

- **GitHub** ： [https://github.com/langgraph4j/langgraph4j](https://github.com/langgraph4j/langgraph4j)
- **最新版本** ：1.7.10 / 1.8-beta（2026-01）
- **Maven 依赖** ：
```
<dependency>
    <groupId>
            org.bsc.langgraph4j
          </groupId>
    <artifactId>langgraph4j-core</artifactId>
    <version>1.7.10</version>
</dependency>
<!-- 与 LangChain4j 集成 -->
<dependency>
    <groupId>
            org.bsc.langgraph4j
          </groupId>
    <artifactId>langgraph4j-langchain4j</artifactId>
    <version>1.7.10</version>
</dependency>
```

## 十、写在最后

写到这里，我想用一句话做总结： **LangChain4j 让你“能把大模型接入 Java”，LangGraph4j 让你“能优雅地把多个 AI 智能体编排起来”。**

它们从来不是“二选一”的关系，而是不同层级的协作关系。

LangChain4j 是 AI 能力的接入层——给你模型 API、向量检索、Tool Calling；LangGraph4j 是流程编排层——给你状态图、条件路由、检查点恢复。

一个是“怎么接”，一个是“怎么排”。

技术选型的正确姿势不是问“哪个更好”，而是问自己三个问题：

1. **我的业务需要几步决策？** 1-3 步，LangChain4j 足够；多步 + 分支 + 循环，LangGraph4j 入场。
2. **我的 Agent 之间需要协作吗？** 单 Agent 用 LangChain4j；多 Agent 用 LangGraph4j 的 Supervisor 模式。
3. **我的任务流程中，失败后能全部重跑吗？** 轻量任务没必要；长周期任务 + 断点恢复，LangGraph4j 的检查点机制几乎无可替代。

从轻到重的演进路径非常清晰： `ChatModel 单次调用` → `AiServices 声明式服务` → `工具调用单 Agent` → `多步骤条件链` → `LangGraph4j 图编排` 。

什么时候该升级工具，什么时候该保持简单，这个判断本身也是架构能力的一部分。

希望这篇文章能让你不再对着这两个框架感到迷茫。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)