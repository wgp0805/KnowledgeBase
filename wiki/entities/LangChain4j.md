---
title: "LangChain4j"
type: entity
tags: [AI框架, Java, LLM]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md, raw/01-articles/如何在Spring Boot中无缝集成LangChain4j，玩转AI大模型！.md, raw/01-articles/用 Java 开发 AI 项目，太爽了！.md, raw/09-archive/JAVA中AI框架选型指南（2026）.md, raw/01-articles/LangChain4j 和 LangGraph4j，哪个更好？.md, raw/01-articles/LangChain4j 入门指南.md]
last_updated: 2026-08-03
---

## 定义
Java 世界首款成熟的 LLM 应用框架，灵感来自 Python LangChain 但非简单翻译，充分尊重 Java 工程习惯（强类型、注解驱动、依赖注入），提供统一的、面向对象的、Java 味十足的 API。

## 关键信息

### 核心抽象七大件
1. **ChatLanguageModel**：所有对话的起点，统一接口抹平模型差异
2. **AI Services**：声明式"魔法"，接口描述需求，框架生成实现
3. **ChatMemory**：让模型拥有上下文，滑动窗口/Token 窗口策略
4. **Tools / Function Calling**：用 @Tool 注解声明方法，框架自动完成 JSON Schema 生成→模型调用→反射执行→结果回传
5. **RAG**：DocumentLoader→DocumentSplitter→EmbeddingModel→EmbeddingStore→ContentRetriever
6. **Streaming**：StreamingChatLanguageModel + StreamingResponseHandler
7. **结构化输出**：根据返回类型自动生成 JSON Schema 并反序列化

### 分层架构
- **应用层**：聊天机器人、RAG 问答、Agent、文档总结、代码助手
- **高级 API 层**：AI Services 声明式描述
- **核心抽象层**：ChatLanguageModel、EmbeddingModel、ChatMemory、ContentRetriever 等
- **集成层**：LLM 适配器、向量库适配器、工具适配器
- **基础设施层**：HTTP Client、JSON、重试熔断、可观测性、Spring/Quarkus Starter

### 适合场景
1. 企业内部智能问答/知识库
2. 客服/营销对话机器人
3. 业务系统 AI 小能手
4. Agent/Copilot 类应用

### Spring Boot Starter 集成

LangChain4j 提供 Spring Boot Starter，自动配置核心组件：

- **依赖命名规范**：`langchain4j-{integration-name}-spring-boot-starter`（如 `langchain4j-open-ai-spring-boot-starter`）
- **属性配置**：在 `application.properties` 中配置 model、api-key、log 等参数后自动创建 `ChatLanguageModel` 实例
- **Streaming 支持**：使用 `streaming-chat-model` 属性前缀自动创建 `StreamingChatLanguageModel`
- **版本要求**：Java 17 + Spring Boot 3.2

自动注入示例：
```java
@RestController
public class ChatController {
    ChatLanguageModel chatLanguageModel;
    public ChatController(ChatLanguageModel chatLanguageModel) {
        this.chatLanguageModel = chatLanguageModel;
    }
    @GetMapping("/chat")
    public String model(@RequestParam(value = "message", defaultValue = "Hello") String message) {
        return chatLanguageModel.generate(message);
    }
}
```

### 护轨（Guardrail）
LangChain4j 支持输入/输出护轨（InputGuardrail/OutputGuardrail），在调用 AI 前/后执行额外操作：
- InputGuardrail：检测用户输入，敏感词拦截等
- OutputGuardrail：检测 AI 响应结果
- 返回 success() 继续调用，fatal() 拒绝请求

### MCP 集成
LangChain4j 支持通过 MCP 协议接入外部服务：
- 支持 SSE 在线调用方式（HttpMcpTransport + DefaultMcpClient）
- 支持本地 Stdio 调用方式（StdioMcpTransport）
- 通过 McpToolProvider 将 MCP 工具注入 AI Service

### SSE 流式接口
推荐使用 Flux 响应式类型实现 SSE 流式输出：
- AI Service 方法返回 Flux\<String\>，配合 StreamingChatModel
- @MemoryId 参数支持多用户会话隔离
- 使用 langchain4j-reactor 依赖实现

#### Skill 支持（原生，双模式）
LangChain4j 通过 `langchain4j-agentic` 模块提供原生 Skill 支持，遵循 Agent Skills 规范。

**两种使用模式：**
- **Tool Mode（推荐）**：Skill 目录通过 `FileSystemSkillLoader` 加载为 Tool，直接注入 AI Service
- **Shell Mode（实验性）**：通过 `ShellSkills` 将 Skill 的执行交给 Shell 命令，适合快速原型和第三方技能生态（如 agentskills.io）

**渐进式披露**：先注入元信息（name + description），模型按需按路径加载完整 SKILL.md 内容。

### Agent 支持（完整）
`langchain4j-agentic` 模块提供两种模式：
- **Workflow 模式**：预定义编排流程（顺序、并行、条件路由、循环）
- **Pure Agent 模式**：模型自主决策，动态选择工具

MCP 集成：`langchain4j-agentic-mcp` 模块支持 MCP 工具作为 Agent 节点。

### 最新版本信息
- 最新版本: 1.15.1 (2026-05) | GitHub Stars: 12,196
- 社区 Stars 居 Java AI 框架之首

### ChatMessage 五种消息类型
| 消息类型 | 描述 | 主要用途 |
| --- | --- | --- |
| `UserMessage` | 用户输入的消息 | 用户提问 |
| `AiMessage` | AI 生成的回复 | 模型输出 |
| `SystemMessage` | 系统消息 | 设置 AI 的角色和行为 |
| `ToolExecutionResultMessage` | 工具执行结果 | 函数调用后回传结果 |
| `CustomMessage` | 自定义消息 | 扩展场景 |

### 优缺点总结
**优点**：统一 API 多模型无缝切换；极致多模型适配（15+主流大模型）；声明式开发效率极高；模块化可插拔架构；全场景能力覆盖（RAG/流式/记忆/工具/Agent）；与 Spring 生态完美融合；社区活跃迭代快速。

**缺点**：学习曲线较陡（需理解 Prompt 模板/记忆管理/工具调用/RAG/Agent 等新概念）；版本迭代快存在破坏性变更；官方文档不够完善；部分高级功能仍在开发中。

### 与 Spring AI 对比
| 对比维度 | Spring AI | LangChain4j |
| --- | --- | --- |
| 核心定位 | Spring 生态的 AI 基础设施 | JVM 上的 LLM 应用开发工具箱 |
| 框架依赖 | 强依赖 Spring Boot | 不依赖 Spring，是通用 Java 库 |
| 功能丰富度 | 基础功能 | 功能更丰富、更灵活 |
| 学习曲线 | 较低 | 较高 |
| 适用场景 | 简单功能、快速接入 | 复杂工作流、Agent、高级定制 |

选型建议：Spring 生态深度用户刚开始学 AI 推荐先从 Spring AI 入门；需要构建复杂 Agent/RAG/工作流推荐 LangChain4j；两者可混用。本质区别：Spring AI 像熟练的装配工，LangChain4j 更像逻辑缜密的架构师。

### 与 LangGraph4j 的关系
[[摘要-langchain4j-langgraph4j-comparison]] 强调，LangChain4j 与 [[LangGraph4j]] 不是竞品，而是不同层级的互补关系：
- LangChain4j 是 AI 能力接入层，解决模型调用、Embedding、RAG、Tool Calling、AiServices 等“能不能用”的问题。
- LangGraph4j 是 Agent 工作流编排层，解决状态图、条件分支、循环、多智能体协作、检查点等“怎么编排复杂流程”的问题。
- 轻量场景（单次调用、RAG 问答、单 Agent + 工具）优先用 LangChain4j；复杂场景（多步分支、循环、Human-in-the-Loop、断点恢复）引入 LangGraph4j。
- 企业项目常见组合：LangChain4j 负责模型/RAG/Tool，LangGraph4j 负责状态图编排、流程路由和恢复能力。

## 版本信息（已统一）

截至 2026-07-07，LangChain4j GitHub 最新 Release 为 **1.17.2**。
- [[摘要-java-ai框架选型指南-2026]] 记录的 1.15.1（2026-05）为当时快照，已过时。
- [[摘要-langchain4j-langgraph4j-comparison]] 记录的 1.11.0（2026-02-04）为更早快照，已过时。
- 两者均为不同时间点的真实版本，非事实冲突，现已以官方 GitHub Release 为准统一为 1.17.2。

## 生产避坑指南
1. **工具描述要写清楚**：AI 能否正确调用工具全看 `@Tool` 的描述，描述太模糊 AI 不知何时调用
2. **多模型切换注意配置冲突**：同时配置多个模型提供商时，需为每个命名模型明确指定 provider
3. **对话记忆不是历史记录**：记忆会根据算法对历史进行改造（淘汰/总结/去除不重要细节/注入额外信息）
4. **模型能力不一致**：同一品牌不同型号能力差别很大，先跑最小可用 Demo 验证
5. **AiMessage.text() 为 null**：多 Agent 设置中 LLM 返回纯工具调用响应时，处理 text 字段可能抛 NPE
6. **依赖版本要匹配**：LangChain4j 版本要与后端模型 SDK 版本对齐，避免兼容性问题

## 工程化建议
- Prompt 与代码分离
- 对 LLM 调用做幂等与重试
- 可观测性（Micrometer + OpenTelemetry）
- 内容审查与越狱防御
- 模型选型做成配置
- RAG 关键在切分策略

## 关联连接
- [[摘要-LangChain4j-Java-AI智能体开发]] — 来源
- [[SpringBoot]] — 集成框架
- [[RAG]] — 检索增强生成
- [[FunctionCalling]] — 工具调用
- [[ChatMemory]] — 对话记忆
- [[AIService]] — 声明式 AI 接口
- [[MCP]] — 模型上下文协议
- [[Skill]] — 技能扩展机制
- [[Skill_Registry]] — 技能注册中心
- [[摘要-java-ai-langchain4j]] — 来源
- [[摘要-java-ai框架选型指南-2026]] — 来源
- [[摘要-langchain4j-langgraph4j-comparison]] — 来源（与 LangGraph4j 的互补选型）
- [[LangGraph4j]] — Agent 工作流编排层
- [[Agent工作流编排]] — 复杂多 Agent 流程编排方法论
- [[摘要-LangChain4j入门指南-苏三]] — 来源（入门指南，优缺点与 Spring AI 对比）
- [[spring-ai-vs-langchain4j]] — 概述
