# JAVA中AI框架选型指南（2026）


  

## 一、整体对比

| 维度  | Spring AI | LangChain4j | Spring AI Alibaba | Solon AI | JBoltAI | AgentScope-Java |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **GitHub Stars** | 8,854 | 12,196 | 9,871 | 2,745 | ~1,200 | 3,458 |
| **最新版本** | 2.0.0-M8 (2026-05) | 1.15.1 (2026-05) | 1.1.2.0 | 3.10.7 | 1. [0.x](http://0.x) | v2  |
| **框架依赖** | Spring Boot | 框架中立 | Spring Boot | 无（纯JDK） | Spring Boot | 框架中立 |
| **Java 版本** | Java 17+ | Java 17+ | Java 17+ | **Java 8~26** | Java 17+ | Java 17+ |
| **模型支持** | 10+ | 20+ | 通义为主（多模型） | 5+  | 多模型（含本地） | 多模型 |
| **RAG** | ✅ 内置 | ✅ 内置 | ✅ 内置 | ✅ 独立模块 | ✅ 核心特色 | ⚠️ 基础 |
| **Agent** | ⚠️ 基础 | ✅ 完整 | ✅ 完整 | ✅ ReActAgent+TeamAgent | ✅ AgentRAG | ✅ 完整 |
| **Skill** | ❌ 无抽象 | ✅ 原生 | ✅ 原生 | ✅ **原生（最丰富）** | ⚠️ 平台级 | ✅ 原生 |
| **可观测性** | ✅ Micrometer | ⚠️ 基础 | ⚠️ 基础 | ⚠️ 基础 | ✅ 完整日志 | ⚠️ 基础 |

## 二、各框架详解

### 1\. Spring AI ⭐⭐⭐⭐⭐

**定位**：Spring 官方推出的 AI 框架，把 Spring 的设计哲学（依赖注入、自动配置、POJO 编程）带到 AI 开发中。

**GitHub**： https://github.com/spring-projects/spring-ai | **Stars**：8,854 | **最新版本**：2.0.0-M8

#### 核心能力

* **ChatClient**
    
     — 流式 API，风格类似 WebClient/RestClient
    
* **Tool/Function Calling**
    
     — 让模型调用业务方法
    
* **RAG**
    
     — 基于向量数据库的检索增强生成
    
* **Advisors**
    
     — 拦截器模式封装对话记忆、安全审核等通用逻辑
    
* **ETL Pipeline**
    
     — 文档注入框架，数据预处理
    
* **Structured Output**
    
     — AI 输出转 POJO
    
* **可观测性**
    
     — 与 Micrometer 深度集成
    
* **模型评估**
    
     — 评估生成内容质量
    

**支持模型**：OpenAI、Anthropic、DeepSeek、Google Gemini、Ollama、Amazon Bedrock、Azure OpenAI、阿里通义 等 10+。

**支持向量库**：PGVector、Chroma、Pinecone、Redis、Milvus、Weaviate、Elasticsearch、MongoDB Atlas、Cassandra、Qdrant、Oracle 等 15+。

#### 快速上手

**Maven 依赖（Spring Boot 3. [5.x](http://5.x) \+ Spring AI 1. [1.x）：](http://1.x）：)**

```
|     |     |
| :--- | ---: |
|     | xml |



<dependency>
        <groupId>
            [org.springframework.ai](http://org.springframework.ai)
          </groupId>
        <artifactId>spring-ai-openai-spring-boot-starter</artifactId>
        <version>1.1.7</version>
</dependency>
```

**[application.yml：](http://application.yml：)**

```
|     |     |
| :--- | ---: |
|     | yaml |



spring:
    ai:
        openai:
            api-key:  ${OPENAI_API_KEY}
            chat:
                options:
                    model:  gpt-4o
```

**ChatClient 使用：**

```
|     |     |
| :--- | ---: |
|     | java |



@RestController
classChatController  {
        privatefinal  ChatClient chatClient;

        publicChatController(
            [ChatClient.Builder](http://ChatClient.Builder) builder)  {
                this.chatClient = [builder.build();](http://builder.build%28%29;)
          
        }

        @GetMapping("/chat")
        String  chat(@RequestParam  String message)  {
                return 
            [chatClient.prompt()](http://chatClient.prompt%28%29)
          
                        .user(message)
                        .call()
                        .content();
        }
}
```

**带 RAG 的 ChatClient：**

```
|     |     |
| :--- | ---: |
|     | java |



@RestController
classRagController  {
        privatefinal  ChatClient chatClient;

        publicRagController(
            [ChatClient.Builder](http://ChatClient.Builder) builder, VectorStore vectorStore)  {
                this.chatClient = builder
                        .defaultAdvisors(
                                newVectorStoreChatMemoryAdvisor(vectorStore),
                                newQuestionAnswerAdvisor(vectorStore, [SearchRequest.defaults())](http://SearchRequest.defaults%28%29%29)
          
                        )
                        .build();
        }

        @GetMapping("/rag")
        String  chat(@RequestParam  String message)  {
                return 
            [chatClient.prompt()](http://chatClient.prompt%28%29)
          
                        .user(message)
                        .call()
                        .content();
        }
}
```

#### Skill 支持

**无原生 Skill 抽象。** Spring AI 不支持通用的 Skill/ [SKILL.md](http://SKILL.md) 机制。其等价能力仅通过 Tool Calling 实现：

* **`@Tool` 注解**
    
     — 将方法注册为 AI 可调用的工具
    
* **`FunctionToolCallback`**
    
     — 编程式注册工具
    
* **`ToolContext`**
    
     — 工具执行上下文
    

```
|     |     |
| :--- | ---: |
|     |     |



// 注册一个工具
@Tool(description = "查询天气")
String getWeather(String city) { ... }

// 通过 ChatClient 调用

            [chatClient.prompt()](http://chatClient.prompt%28%29)
          
        .tools(getWeather)
        .user("北京天气？")
        .call();
```

但 Tool 不具备**渐进式披露**能力（元信息列表→按需加载），也没有标准化的 [SKILL.md](http://SKILL.md) 目录结构。需要 Skill 机制时需配合 LangChain4j 或 Spring AI Alibaba 使用。

#### Agent 支持

Agent 能力相对基础。Spring AI 的 Agent 模式基于 **Advisors 链**：

* **ChatClient Advisors**
    
     — 在 ChatClient 调用前后插入处理逻辑
    
* **工具调用**
    
     — 模型可请求执行注册的 Tool 函数
    
* **对话记忆**
    
     — MessageChatMemoryAdvisor 维护多轮上下文
    

缺乏 LangChain4j 或 Spring AI Alibaba 那样的声明式 Agent 接口和自循环推理机制。

#### 优缺点

| 优点  | 缺点  |
| :---: | :---: |
| Spring 生态无缝集成，学习成本最低 | 必须依赖 Spring Boot |
| 官方维护，迭代稳定 | 无原生 Skill/Agent 抽象 |
| 开箱即用的自动配置 | Agent 能力相对基础 |
| 可观测性原生支持 |     |

### 2\. LangChain4j ⭐⭐⭐⭐⭐

**定位**：社区最活跃的 Java AI 框架，没有之一。框架中立，不绑 Spring，Quarkus、Micronaut、Helidon、纯 Java 都能用。

**GitHub**： https://github.com/langchain4j/langchain4j | **Stars**：12,196 | **最新版本**：1.15.1

#### 核心能力

* **AI Service**
    
     — 声明式编程，通过接口+注解定义 AI 服务，无需实现类
    
* **Tool/Function Calling**
    
     — 强大的工具调用机制
    
* **RAG**
    
     — 完整的数据摄取→检索管道
    
* **Agent**
    
     — `langchain4j-agentic` 模块，支持 Workflow 和 Pure Agent
    
* **Skill**
    
     — 原生 Skill 模块，遵循 Agent Skills 规范
    
* **MCP 支持**
    
     — Model Context Protocol
    
* **Chat Memory**
    
     — 多种记忆模式
    
* **30+ 向量数据库**
    
     — 业界最广覆盖
    

#### 快速上手

**Maven 依赖：**

```
|     |     |
| :--- | ---: |
|     | xml |



<dependency>
        <groupId>
            [dev.langchain4j](http://dev.langchain4j)
          </groupId>
        <artifactId>langchain4j</artifactId>
        <version>1.15.1</version>
</dependency>
<dependency>
        <groupId>
            [dev.langchain4j](http://dev.langchain4j)
          </groupId>
        <artifactId>langchain4j-open-ai</artifactId>
        <version>1.15.1</version>
</dependency>
```

**基础对话：**

```
|     |     |
| :--- | ---: |
|     | java |



ChatLanguageModel  model  = 
            [OpenAiChatModel.builder()](http://OpenAiChatModel.builder%28%29)
          
    .apiKey(
            [System.getenv(](http://System.getenv%28)
          "OPENAI_API_KEY"))
        .modelName("gpt-4o")
        .build();

String  answer  = 
            [model.generate(](http://model.generate%28)
          "Java 8 和 Java 17 有什么区别？");
```

**AI Service 声明式编程（核心特色）：**

```
|     |     |
| :--- | ---: |
|     | java |



interface  CustomerSupportAgent  {
        @SystemMessage("你是一个客服助手")
        String  chat(@UserMessage  String userMessage);
}

CustomerSupportAgent  agent  = 
            [AiServices.create(CustomerSupportAgent.class,](http://AiServices.create%28CustomerSupportAgent.class,) model);
String  response  = 
            [agent.chat(](http://agent.chat%28)
          "这款产品的退款政策是什么？");
```

#### Skill 支持 ✅ （原生支持，遵循 Agent Skills 规范）

LangChain4j 通过 `langchain4j-agentic` 模块提供**原生 Skill 支持**，遵循 **Agent Skills 规范**（ [SKILL.md](http://SKILL.md) 格式）。

**Skill 目录结构：**

```
|     |     |
| :--- | ---: |
|     |     |



skill-name/
├── [SKILL.md](http://SKILL.md)          # 必需：YAML frontmatter（name + description）+ 指令正文
├── references/       # 可选：参考文档
├── examples/         # 可选：示例
└── scripts/          # 可选：脚本
```

**[SKILL.md](http://SKILL.md) 格式：**

```
|     |     |
| :--- | ---: |
|     | markdown |



---
name: docx
description: Edit and review Word documents using tracked changes
---

# Word Document Editor

Instructions for editing Word documents...
```

**两种使用模式：**

**模式一：Tool Mode（推荐）**

Skill 目录通过 `FileSystemSkillLoader` 加载为 Tool，直接注入 AI Service。

```
|     |     |
| :--- | ---: |
|     | java |



Skills  skills  = 
            [FileSystemSkillLoader.loadSkills(Path.of(](http://FileSystemSkillLoader.loadSkills%28Path.of%28)
          "skills/"));

MyAiService  service  = 
            [AiServices.builder(MyAiService.class)](http://AiServices.builder%28MyAiService.class%29)
          
        .chatModel(chatModel)
        .tools(skills)                                        // 所有 Skill 自动注册为 Tool
        .build();
```

**模式二：Shell Mode（实验性）**

通过 `ShellSkills` 将 Skill 的执行交给 Shell 命令。适合快速原型和第三方技能（如  `[agentskills.io](http://agentskills.io)`  生态）。

```
|     |     |
| :--- | ---: |
|     | java |



ShellSkills  skills  = 
            [ShellSkills.from(](http://ShellSkills.from%28)
          
    
            [FileSystemSkillLoader.loadSkills(Path.of(](http://FileSystemSkillLoader.loadSkills%28Path.of%28)
          "skills/"))
);

MyAiService  service  = 
            [AiServices.builder(MyAiService.class)](http://AiServices.builder%28MyAiService.class%29)
          
        .chatModel(chatModel)
    .toolProvider(
            [skills.toolProvider())](http://skills.toolProvider%28%29%29)
          
        .systemMessage("You have access to the following skills:\n"
        + [skills.formatAvailableSkills()](http://skills.formatAvailableSkills%28%29)
          
                +  "\nWhen the user's request relates to one of these skills, read its [SKILL.md](http://SKILL.md) before proceeding.")
        .build();
```

`formatAvailableSkills()` 的输出包含 `<location>` 字段，LLM 可据此定位 [SKILL.md](http://SKILL.md) 文件路径。

**工作方式：**

* **渐进式披露**
    
     — 先注入元信息（name + description），模型按需按路径加载完整内容
    
* **保持上下文精简**
    
     — 只在需要时加载大段指令
    

#### Agent 支持 ✅ （完整）

`langchain4j-agentic` 模块提供两种模式：

**Workflow 模式：** 预定义编排流程（顺序、并行、条件路由、循环）**Pure Agent 模式：** 模型自主决策，动态选择工具

```
|     |     |
| :--- | ---: |
|     | java |



@Agent
interface  CustomerSupportAgent  {
        String  chat(@UserMessage  String userMessage);
}
```

**MCP 集成：**`langchain4j-agentic-mcp` 模块支持 MCP 工具作为 Agent 节点。

#### 优缺点

| 优点  | 缺点  |
| :---: | :---: |
| 功能最全面，Skill+Agent 能力最强 | API 相对复杂 |
| 框架中立，生态最广 | Agent 模块标注 experimental |
| 社区最活跃（12k+ Stars） | 文档在某些领域不够完善 |
| 原生 Skill 支持 |     |

### 3\. Spring AI Alibaba ⭐⭐⭐⭐

> ⚠️ **说明**：Spring AI Alibaba 是阿里推出的 **独立项目**（`alibaba/spring-ai-alibaba`），与 Spring Cloud Alibaba 无关。后者是微服务中间件。

**定位**：阿里出的独立项目，专攻多智能体系统和工作流编排。深度集成 Spring AI 生态，核心跑在 Graph Runtime 上。

**GitHub**： https://github.com/alibaba/spring-ai-alibaba | **Stars**：9,871 | **版本**：1.1.2.0

**官方文档**： https://java2ai.com/docs/overview

#### 快速上手

**Maven 依赖：**

```
|     |     |
| :--- | ---: |
|     | xml |



<dependency>
        <groupId>
            [com.alibaba.cloud.ai](http://com.alibaba.cloud.ai)
          </groupId>
        <artifactId>spring-ai-alibaba-agent-framework</artifactId>
        <version>1.1.2.0</version>
</dependency>
<dependency>
        <groupId>
            [com.alibaba.cloud.ai](http://com.alibaba.cloud.ai)
          </groupId>
        <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
        <version>1.1.2.1</version>
</dependency>
```

**构建 ReactAgent：**

```
|     |     |
| :--- | ---: |
|     | java |



DashScopeApi  dashScopeApi= 
            [DashScopeApi.builder()](http://DashScopeApi.builder%28%29)
          
    .apiKey(
            [System.getenv(](http://System.getenv%28)
          "AI_DASHSCOPE_API_KEY"))
        .build();
ChatModelchatModel= 
            [DashScopeChatModel.builder()](http://DashScopeChatModel.builder%28%29)
          
        .dashScopeApi(dashScopeApi)
        .build();

// 定义工具
ToolCallbackweatherTool= 
            [FunctionToolCallback.builder(](http://FunctionToolCallback.builder%28)
          "get_weather",  newWeatherTool())
        .description("Get weather for a given city")
    .inputType(
            [String.class)](http://String.class%29)
          
        .build();

// 创建 ReactAgent
ReactAgentagent= 
            [ReactAgent.builder()](http://ReactAgent.builder%28%29)
          
        .name("weather_agent")
        .model(chatModel)
        .tools(weatherTool)
        .build();

Stringresult= 
            [agent.run(](http://agent.run%28)
          "北京的天气怎么样？");
```

#### Skill 支持 ✅ （原生支持，遵循 Agent Skills 规范）

Spring AI Alibaba 通过 **`SkillRegistry` + `SkillsAgentHook`** 提供**原生 Skill 支持**，同样遵循 **Agent Skills 规范**。

**核心组件：**

* **`SkillRegistry`**
    
     — 技能注册中心，管理所有 Skill 的元信息
    
* **`SkillsAgentHook`**
    
     — Agent 钩子，自动注入 `read_skill` 工具和技能列表到 System Prompt
    
* **`FileSystemSkillRegistry`**
    
     — 从本地文件系统加载 Skill 目录
    

**Skill 目录结构（与 LangChain4j 完全一致）：**

```
|     |     |
| :--- | ---: |
|     |     |



skills/
├── pdf-extractor/
│   ├── [SKILL.md](http://SKILL.md)          # YAML frontmatter（name + description）+ 指令
│   ├── references/       # 可选
│   └── scripts/          # 可选
├── code-reviewer/
│   └── [SKILL.md](http://SKILL.md)
```

**[SKILL.md](http://SKILL.md) 格式（完全一致）：**

```
|     |     |
| :--- | ---: |
|     | markdown |



---
name: pdf-extractor
description: Extract structured data from PDF documents
---

# PDF Extractor

Instructions for extracting data from PDF files...
```

**在 Agent 中使用：**

```
|     |     |
| :--- | ---: |
|     | java |



SkillRegistry  registry= 
            [FileSystemSkillRegistry.builder()](http://FileSystemSkillRegistry.builder%28%29)
          
    .projectSkillsDirectory(
            [System.getProperty(](http://System.getProperty%28)
          "
            [user.dir"](http://user.dir)
          ) +  "/skills")
        .build();

SkillsAgentHookhook= 
            [SkillsAgentHook.builder()](http://SkillsAgentHook.builder%28%29)
          
        .skillRegistry(registry)
        .build();

ReactAgentagent= 
            [ReactAgent.builder()](http://ReactAgent.builder%28%29)
          
        .name("skills-agent")
        .model(chatModel)
        .saver(newMemorySaver())
    .hooks(
            [List.of(hook))](http://List.of%28hook%29%29)
          
        .build();


            [agent.call(](http://agent.call%28)
          "请介绍你有哪些技能");
```

**工作方式：**

* **渐进式披露**
    
     — System Prompt 先注入技能列表（name, description, skillPath）
    
* 模型判断需要某技能时调用 `read_skill(skill_name)` 加载完整 [SKILL.md](http://SKILL.md)
    
* 按需访问技能目录下的 resources 或使用绑定的工具
    

#### Agent 支持 ✅ （完善）

**单 Agent（ReactAgent）：** ReAct 范式，思考→行动→观察循环**多 Agent 工作流：**

* `SequentialAgent`
    
     — 链式顺序执行
    
* `ParallelAgent`
    
     — 并行执行
    
* `LlmRoutingAgent`
    
     — LLM 路由分发
    
* `LoopAgent`
    
     — 循环迭代执行
    

**高级编排（Graph Core）：** DAG 工作流 + 条件路由 + 状态管理 + PlantUML/Mermaid 可视化

**A2A（Agent-to-Agent）：** 通过 Nacos 实现分布式 Agent 间通信

#### 优缺点

| 优点  | 缺点  |
| :---: | :---: |
| Agent/Multi-Agent 能力最完善 | 强依赖阿里云 DashScope |
| Graph 工作流编排强大 | 国际化和社区规模较小 |
| 原生 Skill 支持 | 部分文档以中文为主 |
| 与 Spring AI 生态兼容 | 模型锁定风险 |

### 4\. Solon AI ⭐⭐⭐⭐

**定位**：全场景轻量级 Java AI 框架。无需框架容器，纯 JDK 即可运行，支持 Java 8 到 Java 26。

**GitHub**： https://github.com/opensolon/solon | **Stars**：2,745 | **AI 版本**： [v3.9.0+（v3.10.7）](http://v3.9.0+（v3.10.7）)

**AI 模块体系：**

* `solon-ai`
    
     — LLM 基础（模型、Prompt、Tool、Skill、方言）
    
* `solon-ai-skills`
    
     — 技能开发（独立模块， [v3.9.0+）](http://v3.9.0+）)
    
* `solon-ai-rag`
    
     — RAG 知识库
    
* `solon-ai-flow`
    
     — AI 工作流编排
    
* `solon-ai-agent`
    
     — Agent（SimpleAgent、ReActAgent、TeamAgent）
    
* `solon-ai-harness`
    
     — Harness 智能体马具框架
    
* `solon-ai-mcp`
    
     — MCP 协议
    

#### 快速上手

```
|     |     |
| :--- | ---: |
|     | xml |



<dependency>
        <groupId>
            [org.noear](http://org.noear)
          </groupId>
        <artifactId>solon-ai</artifactId>
        <version>3.10.7</version>
</dependency>
```

```
|     |     |
| :--- | ---: |
|     | java |



@Controller
public  class  AIController  {
        @Inject
        private  ChatClient chatClient;

        @Mapping("/chat")
        public  String  chat(String msg)  {
                return 
            [chatClient.prompt(msg).call().content();](http://chatClient.prompt%28msg%29.call%28%29.content%28%29;)
          
        }
}
```

#### Skill 支持 ✅ （原生支持，功能最丰富）

Solon AI Skills 是其独立模块 `solon-ai-skills`（ [v3.9.0+），概念原型参考了](http://v3.9.0+），概念原型参考了) Claude Code Agent Skills 的设计思想。

**核心特色：**

| 特性  | 说明  |
| :---: | :---: |
| 构建方式 | 两种构建方式（声明式/编程式） |
| 多态性 | 技能多态，同一接口不同实现 |
| 动态 Prompt | 提示语动态赋能 |
| 注册与优先级 | SkillRegistry + 优先级排序 |
| 加载策略 | 按需动态加载（与渐进式加载区分） |
| 分布式 | Remote Skills 支持 |
| 预置技能 | 内置 20 个预置技能 |
| 生态兼容 | CliSkill 对接海量 Claude Agent Skills |

**Skill 类型体系：**

| Skill 类型 | 用途  |
| :---: | :---: |
| **CliSkill** | 对接海量 Claude Agent Skills 生态（兼容 [agentskills.io）](http://agentskills.io）) |
| **RestApiSkill** | 对接海量 WebAPI |
| **ToolGatewaySkill** | 对接 Tool（或 MCP 服务） |
| **Text2SqlSkill** | 数据库自然语言查询 |
| **Remote Skill** | 分布式技能，跨服务调用 |

**Tool 与 Skill 的区别**：Tool 是功能型（执行原子操作），Skill 是知识型（包含指令/SOP/上下文）。Skill 可以包含多个 Tool 调用和决策逻辑。

#### Agent 支持 ✅

Solon AI Agent 模块 `solon-ai-agent` 提供三种 Agent 类型：

* **SimpleAgent**
    
     — 简单对话代理
    
* **ReActAgent**
    
     — 推理+行动循环
    
* **TeamAgent**
    
     — 多智能体团队协作
    

另有 `solon-ai-harness` Harness 马具框架，提供智能体脚手架能力。`solon-ai-flow` 提供 AI 工作流编排（类似 Spring AI Alibaba 的 Graph Core）。

#### 优缺点

| 优点  | 缺点  |
| :---: | :---: |
| 极致轻量（内存~1MB核心） | 社区和生态较小 |
| 支持 Java 8~26 | 国际化程度有限 |
| Skill 系统最完善（16+ 子主题文档） | 文档以中文为主 |
| 预置 20 个技能，开箱即用 | 企业级特性较少 |
| 兼容 Claude Skills 生态 |     |

### 5\. JBoltAI ⭐⭐⭐⭐

**定位**：面向企业的 Java AI 应用开发框架，强调私有化部署、全链路可追溯、AgentRAG。

**网站**： https://jboltai.com

#### 核心特色

* **AgentRAG**
    
     — "理解→规划→检索→评估→再检索→生成"完整链路
    
* **私有化部署**
    
     — Docker/K8s 全量本地运行
    
* **知识库管理**
    
     — 自动分块、向量化、混合检索
    
* **可视化工作流**
    
     — 拖拽式 Agent 编排
    
* **审计日志**
    
     — 全链路追踪
    

#### Skill 与 Agent 支持

**无原生 Skill 抽象。** 但提供平台级替代方案：

* **Agent 模板**
    
     — 预设的 Agent 配置模板（类似 Skill 的可复用套餐）
    
* **插件系统**
    
     — 对接企业系统的扩展点
    
* **可视化编排**
    
     — 拖拽式构建工作流
    

Agent 方面，**AgentRAG 框架**实现完整的推理链路，过程透明可追溯。

#### 优缺点

| 优点  | 缺点  |
| :---: | :---: |
| 企业级私有化部署 | 社区规模较小 |
| 全链路可追溯 | 无原生 Skill 抽象 |
| 可视化编排 | 部分功能需企业版 |

### 6\. AgentScope-Java ⭐⭐⭐⭐

**定位**：面向生产环境的智能体运行平台，阿里通义实验室出品。提供 ReAct 推理、Harness 工程化基础设施、多智能体编排与 MCP/A2A 协议支持。

**GitHub**： https://github.com/agentscope-ai/agentscope-java | **Stars**：3,457

#### 核心能力

* **Harness 工程化**
    
     — 长期运行、复杂任务的工程底座
    
* **多智能体**
    
     — 子 Agent 声明 + agent_spawn/agent_send
    
* **Middleware**
    
     — onAgent/onReasoning/onActing/onModelCall 五层钩子
    
* **沙箱执行**
    
     — 本地/Docker/E2B 一行切换，快照恢复
    
* **工具与 MCP**
    
     — 注解驱动工具注册，统一 MCP 接入
    
* **Workspace 抽象**
    
     — 工作区即 Agent 人格+记忆+领域知识
    
* **自学习闭环**
    
     — Agent 自起草 Skill → 审核 → 后台整理
    

#### Skill 支持 ✅ （原生支持，Agent Skills 规范）

AgentScope-Java 通过 **`SkillRepository`** 提供**原生 Skill 支持**，同样遵循 **Agent Skills 规范**。

**两大来源：**

1.  **技能市场（Skill Repository）**
    
     — Git 仓库 / Nacos / MySQL / classpath / 自定义后端
    
2.  **工作区**
    
     — `workspace/skills/` 共享 / `<userId>/skills/` 按用户隔离
    

**Skill 目录结构（完全一致）：**

```
|     |     |
| :--- | ---: |
|     |     |



code-reviewer/
├── [SKILL.md](http://SKILL.md)           # YAML frontmatter（name + description）+ 指令正文
├── references/        # 参考文档，agent 按需读取
│   └── [style-guide.md](http://style-guide.md)
          
└── scripts/           # agent 可通过 shell 调用的脚本
    └── [run-checks.sh](http://run-checks.sh)
```

**[SKILL.md](http://SKILL.md) 格式（完全一致）：**

```
|     |     |
| :--- | ---: |
|     | markdown |



---
name: code-reviewer
description: 当用户需要代码评审、风格反馈或 PR 审核时使用。
---

# Code Reviewer

步骤：
1.  读  `references/
            [style-guide.md`](http://style-guide.md`)
            获取项目规范
2.  跑  `scripts/
            [run-checks.sh](http://run-checks.sh) <目标路径>`
```

**多后端支持：**

```
|     |     |
| :--- | ---: |
|     | java |



// Git 技能仓库
HarnessAgentagent= 
            [HarnessAgent.builder()](http://HarnessAgent.builder%28%29)
          
        .name("assistant")
        .model(model)
        .workspace(workspace)
        .skillRepository(newGitSkillRepository("
            [https://github.com/your-org/team-skills.git"](https://github.com/your-org/team-skills.git)
          ))
        .build();

// Nacos 技能市场
NacosSkillRepositorymarket=newNacosSkillRepository(aiService,  "namespace");

            [HarnessAgent.builder()](http://HarnessAgent.builder%28%29)
          
        .skillRepository(market)
        .build();

// MySQL 技能注册表
MysqlSkillRepositoryregistry= 
            [MysqlSkillRepository.builder(dataSource)](http://MysqlSkillRepository.builder%28dataSource%29)
          
        .databaseName("agentscope")
        .skillsTableName("skills")
        .createIfNotExist(true)
        .writeable(true)
        .build();
```

**自学习闭环：**

* Agent 可以从执行中总结经验，自动起草 Skill → 审核 → 周期性后台整理
    
* 成功模式以 Markdown 技能形式自动沉淀到 `workspace/skills/`
    
* 每轮按需加载、跨会话共享——Agent 在每次运行之间累积 know-how
    

#### Agent 支持 ✅ （完善）

**HarnessAgent：** Middleware + Toolkit 两个扩展通道，把工作区、记忆、沙箱、子 Agent、技能与计划模式打包。

**子智能体：** 在 Markdown 里声明子 agent 规格，运行时按需 `agent_spawn` / `agent_send`，支持同步阻塞与后台委派。后台任务终态通过 system-reminder 反向推送。

**多 Agent 协作：** 支持 Pipeline、Broadcast、Sequential 等协作模式。

**A2A + MCP：** 跨进程 Agent 编排与工具集成。

#### 优缺点

| 优点  | 缺点  |
| :---: | :---: |
| 多 Agent 协作最强 | 文档以中文为主 |
| 原生 Skill 支持（多后端） | 社区生产验证案例较少 |
| 自学习闭环 | 学习曲线较陡 |
| Harness 工程化完善 | 偏向研究型场景 |
| 沙箱执行 + 快照恢复 |     |

### 7\. 官方 SDK

当只需要简单调用某个模型 API 时使用。**无 Skill/Agent 抽象。**

| SDK | GitHub Stars | 说明  |
| :---: | :---: | :---: |
| openai-java (TheoKanning) | 4,745 | 非官方但最成熟的 OpenAI Java 客户端 |
| openai-java (官方) | 1,466 | OpenAI 官方 Java 库 |
| deepseek4j | 752 | DeepSeek Java SDK |
| chatgpt-java | 3,449 | 支持流式输出、GPT 插件 |

## 三、Skill 支持对比

> Skill（技能）定义为：**遵循 Agent Skills 规范的可复用能力包**——一个包含  `[SKILL.md](http://SKILL.md)` （YAML frontmatter + 指令）的目录，支持渐进式披露（先列元信息，按需加载详情）。

### 对比总表

| 框架  | 原生 Skill | 遵循规范 | [SKILL.md](http://SKILL.md) | 支持后端 | 特色能力 |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Solon AI** | ✅   | ✅ Claude Skills 规范 | ✅   | 本地/Remote | **20个预置技能、CliSkill/RestApiSkill/ToolGatewaySkill/Text2SqlSkill、分布式、多态、优先级** |
| **LangChain4j** | ✅   | ✅ Agent Skills 规范 | ✅   | 文件系统 | Tool Mode / Shell Mode 双模式 |
| **Spring AI Alibaba** | ✅   | ✅ Agent Skills 规范 | ✅   | 文件系统 | SkillRegistry + SkillsAgentHook |
| **AgentScope-Java** | ✅   | ✅ Agent Skills 规范 | ✅   | Git/Nacos/MySQL/文件 | 自学习闭环 |
| **Spring AI** | ❌   | —   | —   | 仅 Tool Callback | —   |
| **JBoltAI** | ⚠️ 平台级 | —   | —   | Agent 模板 + 插件 | —   |
| **官方 SDK** | ❌   | —   | —   | —   | —   |

### 四者对比

四个框架（LangChain4j、Spring AI Alibaba、AgentScope-Java、Solon AI）均实现了原生 Skill 支持，差异在于规范遵循和接入方式：

| 维度  | LangChain4j | Spring AI Alibaba | AgentScope-Java | Solon AI |
| :---: | :---: | :---: | :---: | :---: |
| **遵循规范** | Agent Skills 规范 | Agent Skills 规范 | Agent Skills 规范 | Claude Skills 规范 |
| **注册方式** | Skills API / ShellSkills | SkillRegistry + SkillsAgentHook | SkillRepository | SkillRegistry |
| **加载方式** | 文件系统 | FileSystemSkillRegistry | Git / Nacos / MySQL / 文件 | 本地 / Remote |
| **与 Agent 结合** | [AiServices.tools()](http://AiServices.tools%28%29) / .toolProvider() | [ReactAgent.hooks()](http://ReactAgent.hooks%28%29) | HarnessAgent 内建 | ChatModel/Agent 内建 |
| **Skill 类型** | [SKILL.md](http://SKILL.md) 目录 | [SKILL.md](http://SKILL.md) 目录 | [SKILL.md](http://SKILL.md) 目录 | CliSkill / RestApiSkill / ToolGatewaySkill / Text2SqlSkill |
| **预置技能** | ❌   | ❌   | ❌   | ✅ 20 个 |
| **生态兼容** | ❌   | ❌   | ❌   | ✅ Claude Skills 生态 |
| **同一切换不同后端** | ❌   | ❌   | ✅   | ❌   |

## 四、Agent 支持对比

| 框架  | 单 Agent | 多 Agent | 工作流编排 | 核心实现 | 评价  |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Spring AI** | ⚠️ 基础 | ❌   | ⚠️ 简单链 | ChatClient + Advisor | 适合对话类 |
| **LangChain4j** | ✅   | ✅   | ✅ Workflow+Pure Agent | @Agent + agentic 模块 + MCP | 最灵活 |
| **Spring AI Alibaba** | ✅   | ✅   | ✅ Graph/DAG | ReactAgent + Multi-Agent + Graph Core + A2A | 多 Agent 编排最强 |
| **Solon AI** | ✅   | ✅   | ✅   | SimpleAgent + ReActAgent + TeamAgent + Harness + Flow | 模块最完整 |
| **JBoltAI** | ✅   | ⚠️  | ✅ 可视化编排 | AgentRAG + 拖拽式 | 企业级 |
| **AgentScope-Java** | ✅   | ✅   | ✅ 多种协作 | HarnessAgent + SubAgent + Middleware | 生产级，工程化最强 |
| **官方 SDK** | ❌   | ❌   | ❌   | —   | —   |

## 五、选型建议

### 按技术栈

**Spring Boot 重度用户 → Spring AI**

只做基础对话/RAG 的话，Spring AI 上手最快。需要 Skill 和 Agent 就在它上面叠 Spring AI Alibaba 或 LangChain4j。

**需要 Skill + Agent 全栈 → LangChain4j 或 Solon AI**

两个都是功能很全的选择。LangChain4j 框架中立，社区大（12k+ Stars）。Solon AI 轻量，Java 8~26 都兼容。看技术栈偏好：Spring 生态选前者，纯 Java 或非 Spring 选后者。

**需要多 Agent 编排 + Skill + Spring 生态 → Spring AI Alibaba**

团队在用 Spring Boot 的话，这是最自然的选择。兼容 Spring AI，自带 Graph 工作流，不用额外搭编排层。

**需要企业级生产部署 + Skill 系统 → AgentScope-Java**

沙箱执行、快照恢复、多后端 Skill 市场、自学习闭环、多租户隔离——Harness 的工程化能力确实是其他框架没做的。Skill 支持 Git/Nacos/MySQL 三种后端。

**非 Spring 技术栈 / 极致轻量 → Solon AI**

纯 JDK 就能跑，Java 8~26 兼容，IoT 和边缘计算场景下比 Spring 系实在太多。

**企业私有化部署 → JBoltAI / AgentScope-Java**

JBoltAI 有可视化编排和审计日志，AgentScope-Java 有沙箱执行和 Harness 工程化。看你是要"好用"还是要"可靠"。

### 一个通用组合方案

**Spring Boot 项目想要全套能力：**

```
|     |     |
| :--- | ---: |
|     |     |



Spring AI（基础 Chat/RAG + 可观测性）
    + Spring AI Alibaba（Agent 编排 + Skill 支持）
```

**非 Spring 项目想要轻量全栈：**

```
|     |     |
| :--- | ---: |
|     |     |



Solon AI（全模块：Chat + Agent + Skill + Flow + Harness）
```

LangChain4j 和 Spring AI Alibaba 有功能重叠，选一个就行。AgentScope-Java 的 Skill Repository 和沙箱执行可以当补充层加进来。

