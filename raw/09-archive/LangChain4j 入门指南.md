---
title: "LangChain4j 入门指南"
source: "https://mp.weixin.qq.com/s/_UL_18bqiM0D56Ju7StopQ"
---
苏三 苏三说技术 *2026年8月3日 16:33*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

## 前言

最近经常有小伙伴问我—— **“老的Java项目做AI应用开发，到底该用什么框架？”**

我的回答是： **LangChain4j** 。

今天这篇文章，我就从零开始，把LangChain4j的核心概念、底层原理、实战代码从头到尾给你拆解一遍。

希望对你会有所帮助。

## 最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。

![图片](assets/LangChain4j%20%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97/120fc0032d790118e773ec1a67b88378_MD5.webp)

## 一、LangChain4j到底是什么？

> 有些小伙伴可能会说：“LangChain4j不就是Python LangChain的Java版吗？”

**还真不是。**

LangChain4j从名字上看确实跟Python的LangChain有关系，但它 **不是LangChain的简单移植** 。

它完全从头开始设计，遵循Java的编程习惯——类型安全、POJO、注解、接口、依赖注入、流式API。

截至2026年，LangChain4j在GitHub上已经积累了 **超过12,200颗Star** 和 **2,300次Fork** ，最新版本为 **1.15.1** ，保持着活跃的开发节奏。

它原生支持 **20+个LLM提供商** 和 **30+个向量存储** ，并且与Spring Boot、Quarkus、Helidon、Micronaut等主流Java框架有一流集成。

**一句话说清** ：LangChain4j是专为Java/Kotlin开发者打造的大语言模型应用开发框架，提供统一、标准化的API，屏蔽各类大模型、向量数据库、文档解析的底层差异，让Java开发者无需重复造轮子，快速构建稳定、可扩展的AI业务应用。

### 1.1 不用LangChain4j，你得面对什么？

直接对接大模型API，你要处理的麻烦事可不少：

- 每个厂商的API格式不一样、参数名不一样、返回结构不一样；
- 每次调用都要手动处理HTTP请求、JSON解析、认证和重试；
- 多轮对话要手动管理消息历史；
- 想让AI基于你的文档回答要做RAG；
- 想让AI查天气、查订单要做工具调用。

**LangChain4j的解决方案：这些复杂功能都已封装成现成组件，拿来就用。**

## 二、一张图看懂LangChain4j的架构

在写代码之前，我们先建立一个整体认知。

![图片](assets/LangChain4j%20%E5%85%A5%E9%97%A8%E6%8C%87%E5%8D%97/9a93ac2fbc45da174180abd7fceab7bf_MD5.webp)

LangChain4j的整体架构分层清晰，五大核心模块支撑所有AI业务能力：

- **Model模型层** 统一封装各类大模型、嵌入模型调用逻辑，屏蔽API差异；
- **Memory记忆层** 管理多轮对话记忆，支持内存、持久化、分段记忆；
- **Document文档层** 支持PDF、Word、TXT等多格式文档加载、解析、文本切片、清洗；
- **Embedding & Store向量存储层** 统一封装向量化与向量检索逻辑。

LangChain4j采用清晰的分层架构设计，核心抽象层（langchain4j-core）是整个框架的基石，定义了所有核心接口和数据模型。

## 三、LangChain4j的“七件套”

LangChain4j的组件体系非常清晰，下面我逐个给你拆解。

### 3.1 Model（模型层）

它是AI的“大脑”。

Model是与大模型交互的入口。LangChain4j提供了统一的接口来对接不同的模型提供商。

目前主要有两类API：

- **LanguageModel** ：输入输出都是String，现在用得越来越少了
- **ChatModel** ：应用最广泛的API，接收多个 `ChatMessage` 作为输入，输出一个 `AiMessage` ，支持文本、图片等多模态输入

**示例：创建一个ChatModel**

```
// 以OpenAI为例
ChatModel model = 
            OpenAiChatModel.builder()
          
    .apiKey(
            System.getenv(
          "OPENAI_API_KEY"))
    .modelName("gpt-4")
    .build();

// 发送消息
ChatResponse response = 
            model.chat(
          
    
            UserMessage.from(
          "你好，请介绍一下自己")
);

            System.out.println(response.aiMessage().text());
```

### 3.2 ChatMessage（消息类型）

它是对话的基本单元。

LangChain4j支持五种消息类型：

| 消息类型 | 描述 | 主要用途 |
| --- | --- | --- |
| `UserMessage` | 用户输入的消息 | 用户提问 |
| `AiMessage` | AI生成的回复 | 模型输出 |
| `SystemMessage` | 系统消息 | 设置AI的角色和行为 |
| `ToolExecutionResultMessage` | 工具执行结果 | 函数调用后回传结果 |
| `CustomMessage` | 自定义消息 | 扩展场景 |

### 3.3 ChatMemory（记忆层）

它让AI“记住”对话。

大模型本身是无状态的，不会记录对话历史。LangChain4j提供了 `ChatMemory` 来管理对话上下文。

**两种内置的记忆淘汰策略** ：

- **MessageWindowChatMemory** ：基于消息滑动窗口，仅保留最近的N条消息
- **TokenWindowChatMemory** ：基于Token滑动窗口，只保留最近的N个Token
```
// 创建记忆，保留最近10条消息
ChatMemory memory = 
            MessageWindowChatMemory.builder()
          
    .maxMessages(10)
    .build();

// 添加用户消息

            memory.add(UserMessage.from(
          "我叫张三"));
// 获取AI回复
AiMessage response = 
            model.chat(memory.messages()).aiMessage();
          

            memory.add(response);
          

// 下一轮对话会自动带上历史

            memory.add(UserMessage.from(
          "我叫什么名字？"));
AiMessage response2 = 
            model.chat(memory.messages()).aiMessage();
          
// 模型会记得你叫张三
```

**💡 一个关键概念** ：LangChain4j提供的是“记忆”而非“历史记录”。

记忆会根据算法对历史进行改造——淘汰某些消息、总结多条消息、去除不重要的细节、注入额外信息等。

### 3.4 Tools（工具层）

它让AI“长出手脚”。

Tools（函数调用）是LangChain4j最强大的功能之一。它让LLM可以调用外部工具——网络搜索、调用外部API、执行特定代码等。

**示例：定义一个数学工具**

```
import 
            dev.langchain4j.agent.tool.Tool;
          

public class CalculatorTools {
    
    @Tool("对给定的2个数字求和")
    double sum(double a, double b) {
        return a + b;
    }
    
    @Tool("返回给定数字的平方根")
    double squareRoot(double x) {
        return 
            Math.sqrt(x);
          
    }
}
```

**⚠️ 重点** ：工具描述一定要写清楚，AI能否正确调用工具全看这个描述！

**让AI使用工具**

```
ChatModel model = 
            OpenAiChatModel.builder()
          
    .apiKey(
            System.getenv(
          "OPENAI_API_KEY"))
    .modelName("gpt-4")
    .build();

// 把工具传给模型
ChatRequest request = 
            ChatRequest.builder()
          
    .messages(
            UserMessage.from(
          "475695037565的平方根是多少？"))
    .toolSpecifications(
            ToolSpecifications.from(CalculatorTools
          .class))
    .build();

ChatResponse response = 
            model.chat(request);
          
// AI会返回一个toolExecutionRequest，表示它想调用squareRoot工具
```

**工具调用的完整流程** ：AiServices发送消息和工具架构给LLM，LLM回复函数调用（如 `add(42, 58)` ），LangChain4j执行Calculator方法，将结果反馈回去。

### 3.5 AiServices（高层API）

它能做声明式AI开发。

`AiServices` 是LangChain4j的高层API，也是 **最让Java开发者感到亲切的部分** 。

它的核心思想是 **面向接口编程** ：你只需要定义一个Java接口，用注解标明它需要哪些能力（系统提示词、用户消息模板、记忆、工具等）， `AiServices` 会为你生成一个 **动态代理对象** ，内部自动编排所有组件。

**最简单的AiService示例** ：

```
interface Assistant {
    String chat(String userMessage);
}

// 创建AI服务
Assistant assistant = 
            AiServices.builder(Assistant
          .class)
    .chatLanguageModel(model)
    .build();

// 直接调用
String reply = 
            assistant.chat(
          "你好，请介绍一下自己");

            System.out.println(reply);
```

**带系统提示词和记忆的AiService** ：

```
interface ChatAssistant {
    
    @SystemMessage("你是一个专业的Java技术顾问，请用中文回答问题")
    String chat(@UserMessage String userMessage);
}

// 创建带记忆的AI服务
ChatMemory chatMemory = 
            MessageWindowChatMemory.builder()
          
    .maxMessages(10)
    .build();

ChatAssistant assistant = 
            AiServices.builder(ChatAssistant
          .class)
    .chatLanguageModel(model)
    .chatMemory(chatMemory)
    .build();

// 多轮对话自动带记忆
String reply1 = 
            assistant.chat(
          "我叫张三");
String reply2 = 
            assistant.chat(
          "我叫什么名字？"); // AI记得你叫张三
```

`AiServices` 支持的能力包括：

- **静态/动态系统消息** ：通过 `@SystemMessage` 注解或 `systemMessageProvider()` 配置
- **静态/动态用户消息** ：通过 `@UserMessage` 注解或 `@UserMessage` 标注参数
- **共享记忆** ：通过 `chatMemory(ChatMemory)` 配置
- **多用户记忆** ：通过 `chatMemoryProvider()` 和 `@MemoryId` 标注参数
- **RAG检索增强** ：通过 `contentRetriever()` 或 `retrievalAugmentor()` 配置

### 3.6 RAG（检索增强生成）

它让AI“有据可查”。

RAG是LangChain4j的核心能力之一。

它的流程是：用户提问 → 从知识库检索相关文档 → 把问题和检索到的文档一起发给AI → AI生成基于文档的回复。

在LangChain4j中，RAG的核心组件是 **RetrievalAugmentor** 。

它就像RAG系统的“中央处理器”，专门负责给用户的问题“加料”——通过调用各种检索渠道，把找到的相关知识片段“贴”到原始问题里，让大模型回答时能参考这些资料。

```
// 1. 加载文档
Document document = 
            FileSystemDocumentLoader.loadDocument(
          "
            knowledge.txt"
          );

// 2. 切片
DocumentSplitter splitter = 
            DocumentSplitters.recursive(
          300, 0);
List segments = 
            splitter.split(document);
          

// 3. 向量化存储
EmbeddingModel embeddingModel = new BgeSmallEnV15EmbeddingModel();
EmbeddingStore<TextSegment> embeddingStore = new InMemoryEmbeddingStore<>();
for (TextSegment segment : segments) {
    Embedding embedding = 
            embeddingModel.embed(segment).content();
          
    
            embeddingStore.add(embedding,
           segment);
}

// 4. 创建ContentRetriever
ContentRetriever retriever = 
            EmbeddingStoreContentRetriever.builder()
          
    .embeddingStore(embeddingStore)
    .embeddingModel(embeddingModel)
    .maxResults(3)
    .build();

// 5. 创建带RAG的AiService
Assistant assistant = 
            AiServices.builder(Assistant
          .class)
    .chatLanguageModel(model)
    .contentRetriever(retriever)
    .build();

// 6. 提问，AI会基于知识库回答
String answer = 
            assistant.chat(
          "公司的请假流程是什么？");
```

**标准版RAG还可以做更多定制** ：加载Markdown文档并按需切割、补充文件名信息、自定义Embedding模型、自定义内容检索器。

**进阶版RAG** 支持查询转换器、查询路由、内容聚合器、内容注入器等特性，将整个RAG流程流水线化（RAG Pipeline）。

### 3.7 MCP协议

它让AI拥有“USB接口”。

> 有些小伙伴可能会问：“除了自定义工具，LangChain4j还能接入外部服务吗？”

**MCP（Model Context Protocol）** 就是干这个的。

你可以把MCP想象成AI应用的“USB接口”，它为AI提供了与外部工具、资源和服务交互的标准化方式。

在LangChain4j中集成MCP非常方便：

```
<!-- 引入MCP依赖 -->
<dependency>
    <groupId>
            dev.langchain4j
          </groupId>
    <artifactId>langchain4j-mcp</artifactId>
    <version>1.1.0-beta7</version>
</dependency>
```
```
@Configuration
public class McpConfig {
    @Bean
    public McpToolProvider mcpToolProvider() {
        // 1. 配置与MCP服务的通讯方式（SSE）
        McpTransport transport = new 
            HttpMcpTransport.Builder()
          
            .sseUrl("
            https://open.bigmodel.cn/api/mcp/web_search/sse?Authorization="
           + apiKey)
            .build();
        // 2. 创建MCP客户端
        McpClient mcpClient = new 
            DefaultMcpClient.Builder()
          
            .transport(transport)
            .build();
        // 3. 从MCP客户端获取工具提供者
        return 
            McpToolProvider.builder()
          
            .mcpClients(mcpClient)
            .build();
    }
}
```

## 四、实战

光说不练假把式。

下面我用 **Spring Boot + LangChain4j** 快速搭建一个AI对话应用。

### 4.1 第一步：创建项目并添加依赖

```
<properties>
    <
            java.version
          >21</
            java.version
          >
    <
            spring-boot.version
          >3.4.5</
            spring-boot.version
          >
    <
            langchain4j.version
          >1.15.1</
            langchain4j.version
          >
</properties>

<dependencies>
    <!-- Spring Boot Web -->
    <dependency>
        <groupId>
            org.springframework.boot
          </groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    
    <!-- LangChain4j核心 -->
    <dependency>
        <groupId>
            dev.langchain4j
          </groupId>
        <artifactId>langchain4j</artifactId>
        <version>${
            langchain4j.version}
          </version>
    </dependency>
    
    <!-- OpenAI兼容适配器（兼容DeepSeek/Ollama/DashScope等） -->
    <dependency>
        <groupId>
            dev.langchain4j
          </groupId>
        <artifactId>langchain4j-open-ai</artifactId>
        <version>${
            langchain4j.version}
          </version>
    </dependency>
    
    <!-- Spring Boot集成 -->
    <dependency>
        <groupId>
            dev.langchain4j
          </groupId>
        <artifactId>langchain4j-spring-boot-starter</artifactId>
        <version>${
            langchain4j.version}
          </version>
    </dependency>
</dependencies>
```

**关键理解** ： `langchain4j-open-ai` 不只是对接OpenAI，它是一个OpenAI兼容协议适配器。任何提供 `/v1/chat/completions` 端点的服务（DeepSeek、Ollama、SiliconFlow、通义千问DashScope）都能用。

### 4.2 第二步：配置 application.yml

```
langchain4j:
  open-ai:
    chat-model:
      api-key: ${OPENAI_API_KEY}
      model-name: gpt-4
      temperature: 0.7
      log-requests: true
      log-responses: true
    embedding-model:
      api-key: ${OPENAI_API_KEY}
      model-name: text-embedding-ada-002
```

### 4.3 第三步：定义AiService接口

```
package 
            com.example.service;
          

import 
            dev.langchain4j.service.SystemMessage;
          
import 
            dev.langchain4j.service.UserMessage;
          
import 
            dev.langchain4j.service.MemoryId;
          
import 
            dev.langchain4j.service.spring.AiService;
          

@AiService
public interface ChatAssistant {
    
    @SystemMessage("你是一个专业的AI助手，请用中文回答问题，简洁友好。")
    String chat(@UserMessage String userMessage);
    
    // 带会话ID的多用户记忆
    @SystemMessage("你是一个专业的AI助手，请用中文回答问题。")
    String chat(@MemoryId String sessionId, @UserMessage String userMessage);
}
```

### 4.4 第四步：写Controller

```
package 
            com.example.controller;
          

import 
            com.example.service.ChatAssistant;
          
import 
            org.springframework.web.bind.annotation.*;
          

@RestController
@RequestMapping("/api/chat")
public class ChatController {
    
    private final ChatAssistant chatAssistant;
    
    public ChatController(ChatAssistant chatAssistant) {
        this.chatAssistant = chatAssistant;
    }
    
    @PostMapping
    public String chat(@RequestBody ChatRequest request) {
        return 
            chatAssistant.chat(request.getMessage());
          
    }
    
    @PostMapping("/session")
    public String chatWithSession(@RequestBody SessionChatRequest request) {
        return 
            chatAssistant.chat(request.getSessionId(),
           
            request.getMessage());
          
    }
}

record ChatRequest(String message) {}
record SessionChatRequest(String sessionId, String message) {}
```

### 4.5 第五步：启动应用

```
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        runApplication(Application.class, args);
    }
}
```

启动后，访问 `POST /api/chat` 就能跟AI对话了。

**前后不到50行代码，一个完整的AI对话服务就跑起来了。**

## 五、进阶用法

### 5.1 结构化输出

它让AI返回Java对象。

许多LLM支持生成结构化格式（通常是JSON）的输出，这些输出可以轻松映射到Java对象并在应用程序中使用。

```
// 1. 定义要提取的数据结构
public class PersonInfo {
    public String name;
    public int age;
    public String city;
}

// 2. 在AiService中指定返回类型
interface PersonExtractor {
    @UserMessage("从以下文本中提取人物信息：{{text}}")
    PersonInfo extractPerson(@V("text") String text);
}

// 3. 调用
PersonExtractor extractor = 
            AiServices.builder(PersonExtractor
          .class)
    .chatLanguageModel(model)
    .build();

PersonInfo info = 
            extractor.extractPerson(
          "张三，今年28岁，住在北京");

            System.out.println(info.name);
           // 张三

            System.out.println(info.age);
           // 28
```

### 5.2 流式响应

它能像ChatGPT一样逐字输出。

通过 `StreamingChatLanguageModel` 实现流式传输，无需等待完整答案加载，实时响应用户。

```
StreamingChatLanguageModel model = 
            OpenAiStreamingChatModel.builder()
          
    .apiKey(
            System.getenv(
          "OPENAI_API_KEY"))
    .modelName("gpt-4")
    .build();

            model.chat(UserMessage.from(
          "写一首关于Java的诗"), 
    new StreamingResponseHandler<AiMessage>() {
        @Override
        public void onNext(String token) {
            
            System.out.print(token);
           // 实时打印每个token
        }
        @Override
        public void onComplete(Response<AiMessage> response) {
            
            System.out.println(
          "\n--- 生成完成 ---");
        }
        @Override
        public void onError(Throwable error) {
            
            error.printStackTrace();
          
        }
    }
);
```

## 六、优缺点

### 优点

**1\. 统一API，多模型无缝切换** LangChain4j提供统一的API屏蔽了不同LLM提供商和向量存储的差异。从OpenAI切换到通义千问，只需改配置，业务代码几乎不用动。

**2\. 极致多模型适配** 原生支持OpenAI、通义千问、文心一言、Llama3、Claude等15+主流大模型，一套代码无缝切换。

**3\. 声明式开发，效率极高** `AiServices` 让开发者只需定义接口加注解，框架自动生成实现。告别冗余的模板代码。

**4\. 模块化可插拔架构** 对话、记忆、文档加载、切片、向量存储、工具调用组件完全解耦，按需组合。

**5\. 全场景能力覆盖** 原生支持RAG、流式对话、多轮记忆、函数调用、Agent智能编排、文档解析。

**6\. 与Spring生态完美融合** 提供Spring Boot Starter，完美融入Java主流技术栈。

**7\. 社区活跃，迭代快速** 自2023年初启动以来，社区持续活跃。2026年已发布1.14.0、1.15.1等多个版本。

### 缺点

**1\. 学习曲线较陡** 需要理解LLM应用开发的新概念：Prompt模板、记忆管理、工具调用、RAG、Agent等。相比Spring AI，LangChain4j配置更多、学习曲线更陡，但胜在能拿捏细节、掌控力拉满。

**2\. 版本迭代快，存在破坏性变更** 版本更新频繁可能导致API变化，升级时需要关注Release Notes。

**3\. 官方文档不够完善** 有开发者反映“根本找不到关键内容的官方文档，该有的重要内容是一点都不介绍”。

**4\. 部分高级功能仍在开发中** 虽然核心功能已经就位，但部分功能还在开发中。

## 七、LangChain4j vs Spring AI

很多开发者会纠结：到底选Spring AI还是LangChain4j？

| 对比维度 | Spring AI | LangChain4j |
| --- | --- | --- |
| **核心定位** | Spring生态的AI基础设施 | JVM上的LLM应用开发工具箱 |
| **框架依赖** | 强依赖Spring Boot | 不依赖Spring，是通用Java库 |
| **功能丰富度** | 基础功能 | 功能更丰富、更灵活 |
| **学习曲线** | 较低 | 较高 |
| **适用场景** | 简单功能、快速接入 | 复杂工作流、Agent、高级定制 |

**选型建议** ：

- 如果你是Spring生态的深度用户，刚开始学习AI，推荐先从 **Spring AI** 入门，快速完成模型接入
- 当需要构建 **复杂的Agent、RAG或工作流** 时，推荐 **LangChain4j**
- 两者也可以混用——在Spring Boot项目中按需使用LangChain4j的特定能力

**本质区别** ：如果说Spring AI是个熟练的装配工，那LangChain4j就更像是个逻辑缜密的架构师。

## 八、生产避坑指南

> 有些小伙伴可能会在实践过程中踩坑，这里我整理了几个常见问题：

**坑1：工具调用的描述要写清楚** AI能否正确调用工具全看 `@Tool` 的描述。描述太模糊，AI可能不知道该在什么时候调用。

**坑2：多模型切换时注意配置冲突** 当同时配置多个模型提供商时，需要为每个命名模型明确指定provider。

**坑3：对话记忆不是历史记录** LangChain4j提供的是“记忆”而非完整“历史记录”，记忆会根据算法对历史进行改造。

**坑4：模型能力不一致** 同一品牌不同型号的能力差别很大，先跑最小可用Demo验证。

**坑5： [AiMessage.text()为null的情况](http://aimessage.xn--text\(\)null-3x2pi84ahl3c1vyd/)** 在多Agent设置中，当LLM返回纯工具调用响应（无文本内容）时，处理AiMessage的text字段可能抛出NPE。

**坑6：依赖版本要匹配** LangChain4j的版本要与后端模型SDK的版本对齐，避免兼容性问题。

## 九、写在最后

回到最初的问题： **Java做AI应用开发，到底该用什么框架？**

如果你是一个Java后端开发者，想在Spring Boot项目里快速集成AI能力—— **LangChain4j是目前最好的选择之一** 。

它不是Python LangChain的简单移植，而是 **为Java从头设计的、遵循Java编程习惯的AI应用开发框架** 。

它提供 **统一的API、声明式的AiServices、丰富的组件库、与Spring生态的无缝集成** 。

## 十、开源地址

- **GitHub** ： [https://github.com/langchain4j/langchain4j](https://github.com/langchain4j/langchain4j)
- **官方文档** ： [https://docs.langchain4j.dev](https://docs.langchain4j.dev/)
- **示例代码** ： [https://github.com/langchain4j/langchain4j-examples](https://github.com/langchain4j/langchain4j-examples)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

我的企业智能知识库系统就是用LangChain4j开发的，感兴趣的小伙伴，可以加入星球学习。