---
title: "用 ChatModel 构建 LLM 驱动的 Java 应用 - 带刺的坐椅"
source: "博客园"
url: "https://www.cnblogs.com/noear/p/21107092"
date: "2026-07-04T03:26:00Z"
score: 0.75
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 用 ChatModel 构建 LLM 驱动的 Java 应用 - 带刺的坐椅

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/noear/p/21107092  
> **抓取日期**: 2026-07-04  
> **相关性评分**: 0.75

如果你尝试过在 Java 应用中集成大语言模型（LLM），大概率写过不少样板代码：HTTP 客户端、JSON 解析、流式处理、会话管理……Solon 4.0 的 `ChatModel` 用一套简洁的 Builder API 把这些都封装好了。

本文将通过真实的代码示例，带你一步步用 `ChatModel` 构建 AI 功能——从简单的单次调用，到带记忆的流式聊天机器人。

## 1\. 什么是 ChatModel？

`ChatModel` 是 Solon AI 生态中的统一 LLM 客户端。你不再需要为不同的模型提供商写不同的 HTTP 调用，而是通过一套统一的 API 完成：

  * **同步调用** — 一次请求，完整返回
  * **流式调用** — 基于 Project Reactor 的响应式流（`Flux<ChatResponse>`）
  * **工具/函数调用** — 让 LLM 调用你的 Java 方法
  * **聊天会话** — 自动维护对话记忆
  * **多模态消息** — 文本、图片、音频
  * **方言适配** — 支持 OpenAI、Ollama、Anthropic、Gemini、DashScope 等多种服务商



最核心的是它使用了 **方言模式（Dialect Pattern）** ——你只需要指向任意兼容的 LLM 端点，它会自动适配协议。

## 2\. 环境配置

在 `pom.xml` 中添加依赖（Solon 不需要父 POM，独立工作）：
    
    
    <dependency>
        <groupId>org.noear</groupId>
        <artifactId>solon-ai</artifactId>
        <version>${solon.version}</version>
    </dependency>
    

这会引入所有内置的方言适配器（OpenAI、Ollama、Gemini、Anthropic、DashScope）。

## 3\. 配置方式

### 3.1 通过 YAML 配置（推荐）
    
    
    solon.ai.chat:
      demo:
        apiUrl: "http://127.0.0.1:11434/api/chat"   # 完整 URL，非 baseUrl
        standard: "ollama"                           # 接口规范（方言标识）
        model: "llama3.2"                            # 模型名称
        headers:
          x-demo: "demo1"
    

然后通过 `@Bean` 注入一个可以直接使用的 `ChatModel`：
    
    
    import org.noear.solon.ai.chat.ChatConfig;
    import org.noear.solon.ai.chat.ChatModel;
    import org.noear.solon.annotation.Bean;
    import org.noear.solon.annotation.Configuration;
    import org.noear.solon.annotation.Inject;
    
    @Configuration
    public class AiConfig {
        @Bean
        public ChatModel chatModel(@Inject("${solon.ai.chat.demo}") ChatModel model) {
            return model;
        }
    }
    

### 3.2 编程式 Builder
    
    
    @Bean
    public ChatModel chatModel() {
        return ChatModel.of("http://127.0.0.1:11434/api/chat")
                .standard("ollama")          // 或 .provider("ollama")
                .model("llama3.2")
                .timeout(Duration.ofSeconds(60))
                .build();
    }
    

### 3.3 支持的模型提供商

`standard`（或 `provider`）字段选择方言：

方言标识 | apiUrl 示例 | 模型  
---|---|---  
`openai`（默认） | `https://api.openai.com/v1/chat/completions` | GPT、DeepSeek、Qwen、GLM、Kimi 等  
`ollama` | `http://127.0.0.1:11434/api/chat` | 本地 Ollama 模型  
`anthropic` | `https://api.anthropic.com/v1/messages` | Claude  
`gemini` | `https://generativelanguage.googleapis.com/...` | Gemini  
`dashscope` | 阿里云 DashScope 端点 | Qwen（DashScope 原生）  
  
## 4\. 同步调用（最简单的方式）

最基本的用法——发送提示词，获取完整响应：
    
    
    import org.noear.solon.ai.chat.ChatModel;
    import org.noear.solon.ai.chat.ChatResponse;
    import org.noear.solon.annotation.Inject;
    import org.noear.solon.annotation.Component;
    
    @Component
    public class ChatService {
        @Inject
        ChatModel chatModel;
    
        public String ask(String question) throws IOException {
            ChatResponse resp = chatModel.prompt(question).call();
            return resp.getMessage().getContent();
        }
    }
    

仅三行业务代码，搞定。

## 5\. 流式调用（实时响应）

对于聊天机器人和助手类应用，流式响应是刚需。`ChatModel` 返回 Reactor 的 `Flux<ChatResponse>`：
    
    
    import reactor.core.publisher.Flux;
    
    public Flux<String> askStream(String question) throws IOException {
        return chatModel.prompt(question)
                .stream()
                .filter(resp -> resp.hasContent())       // 跳过空块
                .map(resp -> resp.getContent());
    }
    

如果你使用 Solon Web Reactive，可以直接把 `Flux` 返回给 SSE 端点：
    
    
    import org.noear.solon.web.sse.SseEvent;
    import org.noear.solon.annotation.Mapping;
    import reactor.core.publisher.Flux;
    
    @Mapping("/chat/stream")
    public Flux<SseEvent> chatStream(String prompt) throws IOException {
        return chatModel.prompt(prompt)
                .stream()
                .filter(resp -> resp.hasContent()) 
                .map(resp -> new SseEvent().data(resp.getContent()));
    }
    

流式协议根据提供商不同，使用标准 SSE 或 `x-ndjson`。

## 6\. 对话记忆：ChatSession

LLM 本身是无状态的，每次请求都需要传入历史上下文。`ChatSession` 自动帮你完成这件事。

### 6.1 基本用法
    
    
    import org.noear.solon.ai.chat.ChatSession;
    import org.noear.solon.ai.chat.session.InMemoryChatSession;
    
    ChatSession session = InMemoryChatSession.builder()
            .sessionId("user-123")
            .maxMessages(10)     // 保留最近 10 轮
            .build();
    
    // 第一轮
    ChatResponse resp1 = chatModel.prompt("你好！")
            .session(session)
            .call();
    
    // 第二轮——模型记得刚才的对话
    ChatResponse resp2 = chatModel.prompt("我刚才说了什么？")
            .session(session)
            .call();
    

### 6.2 Web 应用中的用户级会话

在实际的 Web 应用中，每个用户需要一个独立的会话：
    
    
    import org.noear.solon.annotation.Controller;
    import org.noear.solon.web.sse.SseEvent;
    import reactor.core.publisher.Flux;
    import java.util.Map;
    import java.util.concurrent.ConcurrentHashMap;
    
    @Controller
    public class ChatController {
        @Inject
        ChatModel chatModel;
    
        final Map<String, ChatSession> sessionMap = new ConcurrentHashMap<>();
    
        @Mapping("/chat")
        public Flux<SseEvent> chat(String sessionId, String prompt) throws IOException {
            ChatSession session = sessionMap.computeIfAbsent(sessionId,
                    k -> InMemoryChatSession.builder().sessionId(k).build());
    
            return chatModel.prompt(prompt)
                    .session(session)
                    .options(o -> o.systemPrompt("你是一个友好、乐于助人的助手。"))
                    .stream()
                    .filter(ChatResponse::hasContent)
                    .map(resp -> new SseEvent().data(resp.getContent()));
        }
    }
    

### 6.3 内置会话实现

实现类 | 存储方式 | 适用场景  
---|---|---  
`InMemoryChatSession` | 本地 Map | 开发、单节点  
`FileChatSession` | 文件系统 | CLI 工具、桌面应用  
`RedisChatSession` | Redis | 生产环境、分布式部署  
  
## 7\. 调优：ChatOptions

通过 `ChatOptions` 可以在每次请求中控制模型行为：
    
    
    chatModel.prompt("写一首关于 Java 的诗")
            .options(o -> o
                .temperature(0.8)
                .max_tokens(500)
                .top_p(0.9)
                .systemPrompt("你是一位富有创造力的诗人。"))
            .call();
    

部分常用参数：

方法 | 说明  
---|---  
`temperature(val)` | 采样温度（0.0–2.0）  
`max_tokens(val)` | 最大输出 Token 数  
`top_p(val)` | 核采样参数  
`top_k(val)` | Top-K 采样  
`frequency_penalty(val)` | 降低重复  
`presence_penalty(val)` | 鼓励新话题  
`tool_choice(val)` | 强制工具调用：`none`、`auto`、`required` 或工具名  
`role(val)` | Agent 角色（role + instruction 可自动生成 systemPrompt）  
`instruction(val)` | Agent 指令（role + instruction 可自动生成 systemPrompt）  
`systemPrompt(val)` | 本次请求的系统提示词（完全定制）  
  
## 8\. 多消息 Prompt

有时候你需要的不只是一条消息。可以用 `Prompt` 和 `ChatMessage` 构建更复杂的上下文：
    
    
    import org.noear.solon.ai.chat.Prompt;
    import org.noear.solon.ai.chat.message.ChatMessage;
    
    Prompt prompt = Prompt.of(
        ChatMessage.ofUser("Hello, how are you?"),
        ChatMessage.ofAssistant("Bonjour, comment allez-vous?"),
        ChatMessage.ofUser("What is your name?")
    );
    
    ChatResponse resp = chatModel.prompt(prompt).options(o -> o.systemPrompt("你是一名中英翻译专家。")).call();
    

## 9\. 完整实战：知识感知聊天机器人

下面是一个轻量级的 RAG 模式示例——用 `ChatMessage.ofUserAugment()` 把上下文注入到 Prompt 中：
    
    
    import org.noear.solon.ai.chat.ChatModel;
    import org.noear.solon.ai.chat.ChatResponse;
    import org.noear.solon.ai.chat.message.ChatMessage;
    import org.noear.solon.annotation.Component;
    import org.noear.solon.annotation.Inject;
    
    @Component
    public class KnowledgeChatbot {
        @Inject
        ChatModel chatModel;
    
        public String answer(String question, String referenceContext) throws Exception {
            // 将参考上下文与用户问题合并
            ChatMessage augmented = ChatMessage.ofUserAugment(question, referenceContext);
    
            ChatResponse resp = chatModel.prompt(augmented)
                    .options(o -> o
                        .temperature(0.3)
                        .systemPrompt("你是一个知识渊博的助手。请基于提供的参考资料回答。"))
                    .call();
    
            return resp.getMessage().getContent();
        }
    }
    

这种模式——用上下文增强用户输入，再调用模型——正是 Solon AI 中 RAG（检索增强生成）的基础。

## 10\. 下一步

`ChatModel` 只是入口点。Solon AI 还提供：

  * **工具调用** — 用 `@ToolMapping` 定义 LLM 可调用的 Java 方法
  * **Talent 系统** — 可复用的能力模块
  * **Agent** — `ReActAgent` 和 `TeamAgent` 实现多步推理
  * **RAG 流水线** — 完整的文档加载、切分、嵌入、检索流程
  * **MCP 协议** — 连接 MCP 服务器使用外部工具



完整文档参见官方指南：

  * 👉 <https://solon.noear.org/article/918>（模型构建）
  * 👉 <https://solon.noear.org/article/920>（API 参考）



* * *

_你有没有在 Java 中集成过 LLM？最大的痛点是什么？欢迎在评论区分享，可能会在后续文章中专门讨论。_


---
> 原文链接: https://www.cnblogs.com/noear/p/21107092