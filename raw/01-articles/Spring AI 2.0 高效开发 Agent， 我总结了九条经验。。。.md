---
title: "Spring AI 2.0 高效开发 Agent， 我总结了九条经验。。。"
source: "https://mp.weixin.qq.com/s/fYuIV9QNDZs2TBgBAxKMVg"
---
小锋 java1234 *2026年7月5日 09:06*

大家好，我是锋哥。

> 最近用 Spring AI 2.0 做了几个 Agent 项目，踩了不少坑，也摸出一点门道。所以把我觉得最实用的九条经验整理出来，配上关键代码，方便大家直接上手。

---

![图片](assets/Spring%20AI%202.0%20%E9%AB%98%E6%95%88%E5%BC%80%E5%8F%91%20Agent%EF%BC%8C%20%E6%88%91%E6%80%BB%E7%BB%93%E4%BA%86%E4%B9%9D%E6%9D%A1%E7%BB%8F%E9%AA%8C%E3%80%82%E3%80%82%E3%80%82/89b17967f806a4225de19c2803aa2875_MD5.webp)

## 目录

- 写在前面：Agent 到底在干什么
- 经验一：ChatClient 是入口，别绕远路
- 经验二：工具调用交给 ToolCallingAdvisor
- 经验三：用 @Tool 定义工具，少写样板代码
- 经验四：System Prompt 比换模型更管用
- 经验五：用 Advisor 链拆分职责
- 经验六：流式输出要尽早接上
- 经验七：会话记忆别自己拼 List
- 经验八：工具宁少勿滥
- 经验九：可观测性要前置

---

## 写在前面：Agent 到底在干什么

很多人第一次接触 Agent，会被各种名词绕晕。其实可以把它想成一件事：

**用户提一个问题 → 大模型决定要不要调工具 → 工具跑完把结果还给模型 → 模型给出最终回答。**

Spring AI 2.0 最大的变化，是把「工具调用循环」从各个 ChatModel 内部抽出来，统一交给 `ChatClient` + `ToolCallingAdvisor` 管理。架构上更清晰，调试也更容易。

![图片](assets/Spring%20AI%202.0%20%E9%AB%98%E6%95%88%E5%BC%80%E5%8F%91%20Agent%EF%BC%8C%20%E6%88%91%E6%80%BB%E7%BB%93%E4%BA%86%E4%B9%9D%E6%9D%A1%E7%BB%8F%E9%AA%8C%E3%80%82%E3%80%82%E3%80%82/da322ed51509c15f02e7a1b3f3e9e178_MD5.jpg)

下面这张图描述了 Agent 一次完整对话的大致流程：

![图片](assets/Spring%20AI%202.0%20%E9%AB%98%E6%95%88%E5%BC%80%E5%8F%91%20Agent%EF%BC%8C%20%E6%88%91%E6%80%BB%E7%BB%93%E4%BA%86%E4%B9%9D%E6%9D%A1%E7%BB%8F%E9%AA%8C%E3%80%82%E3%80%82%E3%80%82/4c40d49c6c333e8d0bb2ba653271b8d2_MD5.png)

## 经验一：ChatClient 是入口，别绕远路

Spring AI 2.0 里， **推荐所有 Agent 场景都从 `ChatClient` 出发** ，而不是直接调 `ChatModel` 。

原因很简单： `ChatClient` 自带 Advisor 链、工具注册、流式封装，你少写很多胶水代码。直接调 `ChatModel` 的话，工具循环、记忆、RAG 都得自己拼。

```kotlin
@RestController@RequestMapping("/agent")public class AgentController {
    private final ChatClient chatClient;
    public AgentController(
            ChatClient.Builder
           builder) {        this.chatClient = builder                .defaultSystem("你是一个 helpful 的助手，回答要简洁。")                .build();    }
    @PostMapping("/chat")    public String chat(@RequestBody ChatRequest request) {        return 
            chatClient.prompt()
                          .user(
            request.message())
                          .call()                .content();    }}
```

`              application.yml            ` 里配好模型就行，Spring Boot 会自动注入 `              ChatClient.Builder            ` ：

```apache
spring:  ai:    openai:      api-key: ${OPENAI_API_KEY}      base-url: 
            https://dashscope.aliyuncs.com/compatible-mode/v1
                chat:        options:          model: qwen3.6-plus          temperature: 0.3
```

---

## 经验二：工具调用交给 ToolCallingAdvisor

2.0 之前，工具调用逻辑散落在各个 Model 实现里，换模型容易出兼容问题。2.0 起， **`ToolCallingAdvisor` 统一负责工具循环** ， `ChatClient` 会自动注册它。

你只需要把工具传进去，框架帮你跑完「模型 → 调工具 → 再喂给模型」这一圈：

```kotlin
@Servicepublic class WeatherAgent {
    private final ChatClient chatClient;    private final WeatherTools weatherTools;
    public WeatherAgent(
            ChatClient.Builder
           builder, WeatherTools weatherTools) {        this.weatherTools = weatherTools;        this.chatClient = 
            builder.build();
              }
    public String ask(String question) {        return 
            chatClient.prompt()
                          .user(question)                .tools(weatherTools)   // 注册工具，循环由 ToolCallingAdvisor 处理                .call()                .content();    }}
```

![图片](assets/Spring%20AI%202.0%20%E9%AB%98%E6%95%88%E5%BC%80%E5%8F%91%20Agent%EF%BC%8C%20%E6%88%91%E6%80%BB%E7%BB%93%E4%BA%86%E4%B9%9D%E6%9D%A1%E7%BB%8F%E9%AA%8C%E3%80%82%E3%80%82%E3%80%82/1a4c80113b89f1bd095f1b80f74bf517_MD5.jpg)

对应 Mermaid 流程：

![图片](assets/Spring%20AI%202.0%20%E9%AB%98%E6%95%88%E5%BC%80%E5%8F%91%20Agent%EF%BC%8C%20%E6%88%91%E6%80%BB%E7%BB%93%E4%BA%86%E4%B9%9D%E6%9D%A1%E7%BB%8F%E9%AA%8C%E3%80%82%E3%80%82%E3%80%82/b82e4b0eb08c150f4508617cf515e081_MD5.png)

**别自己写 while 循环去解析 tool\_calls** ，除非你有非常特殊的业务需求（比如要和 Prompt Cache 深度结合）。大多数场景，框架托管就够了。

---

## 经验三：用 @Tool 定义工具，少写样板代码

定义工具最省心的方式：写一个普通 Java 类，方法上加 `@Tool` 注解。

```typescript
@Componentpublic class WeatherTools {
    @Tool(description = "根据城市名查询当前天气，例如：北京、上海")    public String getWeather(            @ToolParam(description = "城市名称，不含'市'字") String city) {        // 实际项目里这里调第三方 API        return switch (city) {            case "北京" -> "晴，28°C，东北风 2 级";            case "上海" -> "多云，26°C，东南风 3 级";            default -> "暂无 " + city + " 的天气数据";        };    }
    @Tool(description = "查询指定城市未来三天的天气预报")    public List<String> getForecast(String city) {        return List.of(                city + " 明天：多云，25~31°C",                city + " 后天：小雨，22~27°C",                city + " 大后天：晴，24~30°C"        );    }}
```

几点小建议：

- `description` 一定要写清楚，模型靠它决定什么时候调、传什么参数
- 参数用 `@ToolParam` 补充说明，减少模型传错值的概率
- 返回值尽量是 String 或简单 POJO，复杂对象模型不好消化

---

## 经验四：System Prompt 比换模型更管用

做 Agent 时，遇到问题第一反应往往是「换个更强的模型」。我的经验是： **先把 System Prompt 写好，效果往往比换模型明显，还省钱。**

```python
this.chatClient
= builder        .defaultSystem("""                你是「小助手」，一个面向企业内部员工的问答 Agent。
     规则：                1. 涉及公司制度、流程的问题，必须先调用 searchKnowledge 工具检索，不能凭记忆回答。                2. 不确定的信息，明确说「我不确定」，不要编造。                3. 回答用中文，条理清晰，必要时用编号列表。                4. 单次回答控制在 300 字以内，除非用户要求详细说明。                """)        .build();
```

Prompt 里写清楚「角色、边界、工具使用规则、输出格式」，Agent 的稳定性会好很多。可以把 Prompt 抽到配置文件或数据库，方便运营同学迭代，不用每次改代码发版。

---

## 经验五：用 Advisor 链拆分职责

Agent 很容易写成一个大 Service：记忆在这里、RAG 在那里、日志又塞进来……代码很快变成一团。Spring AI 2.0 的 **Advisor 机制** 就是用来解耦的。

常见组合：

| Advisor | 作用 |
| --- | --- |
| `MessageChatMemoryAdvisor` | 自动读写会话历史 |
| `QuestionAnswerAdvisor` | RAG 检索增强 |
| `ToolCallingAdvisor` | 工具调用循环（框架自动注册） |
| 自定义 Advisor | 审计日志、权限校验、敏感词过滤 |

```typescript
@Configurationpublic class AgentConfig {
    @Bean    ChatClient agentChatClient(            ChatClient.Builder builder,            ChatMemory chatMemory,            VectorStore vectorStore) {
        var memoryAdvisor = MessageChatMemoryAdvisor.builder(chatMemory).build();        var ragAdvisor = QuestionAnswerAdvisor.builder(vectorStore).build();
        return builder                .defaultAdvisors(memoryAdvisor, ragAdvisor)                .defaultSystem("你是企业知识库助手，优先依据检索结果回答。")                .build();    }}
```

![图片](assets/Spring%20AI%202.0%20%E9%AB%98%E6%95%88%E5%BC%80%E5%8F%91%20Agent%EF%BC%8C%20%E6%88%91%E6%80%BB%E7%BB%93%E4%BA%86%E4%B9%9D%E6%9D%A1%E7%BB%8F%E9%AA%8C%E3%80%82%E3%80%82%E3%80%82/507f587264fc69eff8bcd07f969f137d_MD5.jpg)

Advisor 的执行顺序很重要。想观察每一次工具调用的中间过程，就把自定义 Advisor 的 order 设得比 `ToolCallingAdvisor` 更高（数值更大），这样它会在工具循环「内部」被触发。

---

## 经验六：流式输出要尽早接上

Agent 调工具时，用户可能要等好几秒。如果一直白屏，体验很差。 **流式输出（SSE）应该尽早接上** ，至少让用户看到「正在思考」或逐字输出的效果。

```typescript
@GetMapping(value = "/chat/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)public Flux<String> chatStream(@RequestParam String message) {    return chatClient.prompt()            .user(message)            .tools(weatherTools)            .stream()            .content();}
```

前端用 EventSource 或 fetch 读 SSE 就行。注意：流式场景下如果有多轮工具调用，中间会有几次「停顿」，可以在 UI 上加一个 loading 状态，别让用户以为卡死了。

---

## 经验七：会话记忆别自己拼 List

多轮对话是 Agent 的基本能力。2.0 里直接用 `ChatMemory` + `MessageChatMemoryAdvisor` ，别自己维护 `List<Message>` 再手动塞给模型。

```typescript
@BeanChatMemory chatMemory() {    return MessageWindowChatMemory.builder()            .maxMessages(20)          // 保留最近 20 条，防止 token 爆炸            .build();}
// 调用时带上 conversationIdpublic String chat(String conversationId, String message) {    return chatClient.prompt()            .user(message)            .advisors(a -> a.param(ChatMemory.CONVERSATION_ID, conversationId))            .call()            .content();}
```

记忆窗口别设太大。对话一长，token 费用和响应延迟都会上去。重要信息可以落库，需要时再检索，而不是全部堆在上下文里。

---

## 经验八：工具宁少勿滥

新手容易犯一个错： **给 Agent 塞几十个工具** ，觉得功能越多越好。实际效果是模型经常选错工具，或者犹豫半天。

我的做法是：

- 单 Agent 控制在 **5~8 个工具** 以内
- 功能相近的工具合并，比如 `searchOrderById` 和 `searchOrderByPhone` 合成一个带参数的 `searchOrder`
- 复杂流程拆成多个专用 Agent，而不是一个「万能 Agent」

```javascript
// 不推荐：工具太多，模型容易懵.tools(tool1, tool2, tool3, tool4, tool5, tool6, tool7, tool8, tool9, tool10)
// 推荐：按场景分组，每次只注册相关工具.tools(orderTools)          // 订单 Agent.tools(inventoryTools)      // 库存 Agent
```

---

## 经验九：可观测性要前置

Agent 出问题时，最难排查的是「模型为什么没调工具」或「为什么调错了工具」。所以 **日志和监控要在一开始就接上** ，别等线上出事故再补。

```typescript
@Slf4j@Componentpublic class AgentAuditAdvisor implements CallAdvisor {
    @Override    public ChatClientResponse adviseCall(            ChatClientRequest request, CallAdvisorChain chain) {
        log.info("Agent 请求 | user={}", request.prompt().getUserMessage());        long start = System.currentTimeMillis();
        ChatClientResponse response = chain.nextCall(request);
        log.info("Agent 响应 | 耗时={}ms | tokens={}",                System.currentTimeMillis() - start,                response.chatResponse().getMetadata().getUsage());
        return response;    }
    @Override    public String getName() {        return "AgentAuditAdvisor";    }
    @Override    public int getOrder() {        return Ordered.HIGHEST_PRECEDENCE + 100;    }}
```

Spring AI 也集成了 Micrometer，配合 Prometheus + Grafana 可以看 token 用量、调用延迟。Agent 是按 token 计费的，这个监控直接关系到成本。

---

[最近，锋哥又开始收Java+AI大模型编程学员了！](https://mp.weixin.qq.com/s?__biz=MzIxNTAwNjA4OQ==&mid=2247571719&idx=1&sn=8a19d877e40d49d46ce3637575bb7403&scene=21#wechat_redirect)