---
title: "如何在Spring Boot中无缝集成LangChain4j，玩转AI大模型！"
source: "https://javaedge.blog.csdn.net/article/details/142392834"
---
### 0 前言

LangChain4j 提供了用于以下功能的 [Spring Boot 启动器](https://github.com/langchain4j/langchain4j-spring)：

- 常用集成
- 声明式 [AI 服务](https://docs.langchain4j.dev/tutorials/ai-services)

### 1 常用集成的 Spring Boot starters

Spring Boot 启动器帮助通过属性创建和配置 [语言模型](https://docs.langchain4j.dev/category/language-models)、[嵌入模型](https://docs.langchain4j.dev/category/embedding-models)、[嵌入存储](https://docs.langchain4j.dev/category/embedding-stores) 和其他核心 LangChain4j 组件。

要使用 Spring Boot 启动器，请导入相应依赖包。

Spring Boot 启动器依赖包的命名规范：`langchain4j-{integration-name}-spring-boot-starter`。

如对于 OpenAI （`langchain4j-open-ai`），依赖包名称为 `langchain4j-open-ai-spring-boot-starter`：

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-open-ai-spring-boot-starter</artifactId>
    <version>0.34.0</version>
</dependency>
```

然后，可在 `application.properties` 文件中配置 模型 参数：

```text
langchain4j.open-ai.chat-model.api-key=${OPENAI_API_KEY}
langchain4j.open-ai.chat-model.model-name=gpt-4o
langchain4j.open-ai.chat-model.log-requests=true
langchain4j.open-ai.chat-model.log-responses=true
...
```

此时，将自动创建一个 `OpenAiChatModel` 实例（`ChatLanguageModel` 的实现）

![](https://img-blog.csdnimg.cn/8d280742d5134a49b7e2c68d46d4bf87.png)

并且可通过自动注入在需要的地方使用它：

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

如需一个 `StreamingChatLanguageModel` 实例，使用 `streaming-chat-model` 代替 `chat-model` 属性：

```text
langchain4j.open-ai.streaming-chat-model.api-key=${OPENAI_API_KEY}
...
```

### 2 声明式 AI 服务的 Spring Boot starter

LangChain4j 提供一个 Spring Boot starter，用于自动配置 [AI 服务](https://docs.langchain4j.dev/tutorials/ai-services)、[RAG](https://docs.langchain4j.dev/tutorials/rag)、[工具](https://docs.langchain4j.dev/tutorials/tools) 等功能。

假设已导入某已集成的starters（见上文），然后导入 `langchain4j-spring-boot-starter`：

```xml
<dependency>
    <groupId>dev.langchain4j</groupId>
    <artifactId>langchain4j-spring-boot-starter</artifactId>
    <version>0.34.0</version>
</dependency>
```

定义 AI 服务接口，并用 `@AiService` ：

```java
@AiService
interface Assistant {

    @SystemMessage("You are a polite assistant")
    String chat(String userMessage);
}
```

可把它看作标准 Spring Boot的 `@Service`，但带有 AI 功能。

当应用程序启动时，LangChain4j 启动器将扫描类路径并找到所有带有 `@AiService` 注解的接口。对于每个找到的 AI 服务，它将使用应用程序上下文中的所有 LangChain4j 组件创建此接口的实现，并将其注册为一个 bean，因此您可以在需要的地方进行自动注入：

```java
@RestController
class AssistantController {

    @Autowired
    Assistant assistant;

    @GetMapping("/chat")
    public String chat(String message) {
        return assistant.chat(message);
    }
}
```

更多细节请见 [这里](https://github.com/langchain4j/langchain4j-spring/blob/main/langchain4j-spring-boot-starter/src/main/java/dev/langchain4j/service/spring/AiService.java)。

### 3 支持的版本

LangChain4j 的 Spring Boot 集成需要 Java 17 和 Spring Boot 3.2。

### 4 示例

- [低级 Spring Boot 示例](https://github.com/langchain4j/langchain4j-examples/blob/main/spring-boot-example/src/main/java/dev/langchain4j/example/lowlevel/ChatLanguageModelController.java) 使用 [ChatLanguageModel API](https://docs.langchain4j.dev/tutorials/chat-and-language-models)
- [高级 Spring Boot 示例](https://github.com/langchain4j/langchain4j-examples/blob/main/spring-boot-example/src/main/java/dev/langchain4j/example/aiservice/AssistantController.java) 使用 [AI 服务](https://docs.langchain4j.dev/tutorials/ai-services)

#### 4.1 使用 Spring Boot 的客户支持代理示例

从官网拉下代码后，直接修改配置文件中的 api-key 如下（仅做本地演示用）：

![](https://img-blog.csdnimg.cn/ec62dcfd6f3040569bba26a18bcd5e31.png)

启动CustomerSupportAgentApplication应用后，直接在控制台交互：

我开始提问：How can I cancel my booking？

![](https://img-blog.csdnimg.cn/17a28620674644a592f887908740c665.png)

为啥 AI 会要求提供信息呢？因为注册了一个工具：

```java
@Component
public class BookingTools {

    @Autowired
    private BookingService bookingService;

    @Tool
    public void cancelBooking(String bookingNumber, String customerName, String customerSurname) {
        System.out.printf("[Tool]: Cancelling booking %s for %s %s...%n", bookingNumber, customerName, customerSurname);
        bookingService.cancelBooking(bookingNumber, customerName, customerSurname);
    }
}
```

那我就按他的要求提供信息：

![](https://img-blog.csdnimg.cn/78e1575cee724f87a8e88976ad4d57ea.png)

AI 还是会问我要名字。那我就随便回答，然后就报错了：

![](https://img-blog.csdnimg.cn/414a60f329ba4c9e9327b6dd0c77150c.png)

注意这是个后端自定义的业务异常，即没有找到对应名字的预订。但请注意最后 AI 还是会提醒你输入正确信息：

![](https://img-blog.csdnimg.cn/4f446148354c4b729a51813ee231193b.png)

那就放过他吧，我输入后端存储的真实信息：

![](https://img-blog.csdnimg.cn/e4cc68958bdf44dfb4f9c6eff6191c68.png)

#### 4.2 HelloWorld

```java
import dev.langchain4j.model.chat.ChatLanguageModel;
import dev.langchain4j.model.openai.OpenAiChatModel;

import static dev.langchain4j.model.openai.OpenAiChatModelName.GPT_4_O_MINI;

public class _00_HelloWorld {

    public static void main(String[] args) {

        ChatLanguageModel model = OpenAiChatModel.builder()
                .apiKey(ApiKeys.OPENAI_API_KEY)
                .modelName(GPT_4_O_MINI)
                .build();

        String answer = model.generate("Say Hello World");

        System.out.println(answer);
    }
}
```

响应：

```bash
Hello, World!
```