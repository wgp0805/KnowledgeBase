---
title: "AIService"
type: concept
tags: [AI, 声明式接口, LangChain4j]
sources: [raw/01-articles/LangChain4j 来了，Java AI智能体开发再次起飞。。。.md, raw/01-articles/如何在Spring Boot中无缝集成LangChain4j，玩转AI大模型！.md]
last_updated: 2026-05-19
---

## 定义
LangChain4j 的招牌特性，用 Java 接口+注解声明式描述 AI 能力，框架自动生成动态代理实现，业务代码只需看到干净的 Java 接口。

## 关键信息

### 核心注解
- `@SystemMessage`：设定角色和约束
- `@UserMessage`：用户输入模板
- `@V`：绑定方法参数到 Prompt 模板变量
- `@Tool`：声明可调用工具

### 底层原理
动态代理 + 模板渲染：方法入参通过 @V 绑定到 Prompt 模板，框架拼好最终文本，调用 ChatLanguageModel，根据返回类型把字符串解析成目标对象。

### 价值
业务代码不再关心 Prompt 怎么写、怎么调模型、怎么解析结果——"接口描述需求，框架生成实现"。

### Spring Boot 集成
导入 `langchain4j-spring-boot-starter` 依赖后，`@AiService` 接口在启动时被自动扫描并生成动态代理实现，注册为 Spring Bean，可直接 `@Autowired` 注入：

```java
@AiService
interface Assistant {
    @SystemMessage("You are a polite assistant")
    String chat(String userMessage);
}

@RestController
class AssistantController {
    @Autowired Assistant assistant;
    @GetMapping("/chat")
    public String chat(String message) {
        return assistant.chat(message);
    }
}
```

`@Tool` 注解的方法也可在 Spring 组件中声明，AI 可自动调用。

## 关联连接
- [[LangChain4j]] — AI Service 所属框架
- [[FunctionCalling]] — 工具调用
- [[ChatMemory]] — 记忆集成
