---
title: "AgentScope入门指南"
source: "https://mp.weixin.qq.com/s/O_Bi4zOMkieYhPoJttwBoA"
---
苏三 苏三说技术 *2026年7月22日 08:58*

## 大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

## 前言

> Java开发者如何快速构建企业级AI Agent应用

最近这段时间，AI Agent（智能体）这个概念火得一塌糊涂。从OpenClaw到Claude Code，从Manus到各种Agent框架，仿佛一夜之间，“让AI自己干活”成了技术圈最热门的话题。

但很多Java开发者在尝试入局的时候，发现了一个尴尬的问题——市面上主流的Agent框架，绝大多数是Python生态的。

LangChain？Python的。

AutoGen？Python的。

CrewAI？还是Python的。

“三哥，我们团队都是Java技术栈，难道要为了做Agent专门去学Python吗？”

当然不用。

**阿里巴巴开源的AgentScope-Java，就是专为Java开发者打造的智能体开发框架** 。

今天这篇文章就专门跟大家一起聊聊AgentScope-Java，希望对你会有所帮助。

**最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibJZVicC7nz5jN7lz3xCSbNeNj4yNXMvNX12Fgwkvnuibx4wj2uF89ehibUGMOT4DPHibO5dg44kXwBickPvORaQ8JGA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=0)

## 一、AgentScope-Java到底是什么？

### 1.1 一句话说清

**AgentScope-Java是阿里巴巴开源的一个面向智能体（Agent）编程的Java框架，用于构建基于大语言模型（LLM）的智能体应用** 。

它的核心目标很明确—— **让Java开发者用自己熟悉的语言和工具链，快速构建生产级的AI Agent应用** 。

### 1.2 AgentScope-Java解决了什么问题？

在AgentScope出现之前，Java开发者想做Agent应用，基本只有两条路：

**第一条路：用Python框架** 。

学新语言、搭新环境、维护两套技术栈，团队分裂。

**第二条路：自己从零造轮子** 。

写ReAct循环、做工具调用、管理对话记忆、处理多Agent协作……每一项都是大工程。

AgentScope做的事情就是： **把Agent开发需要的所有基础设施——ReAct推理循环、工具调用、记忆管理、多智能体协作、分布式部署——全部封装成一个Java框架，开箱即用** 。

### 1.3 和Spring AI Alibaba有什么区别？

很多小伙伴可能会问：“三哥，阿里巴巴不是有Spring AI Alibaba吗？跟这个有什么区别？”

这是一个非常好的问题。两者定位完全不同：

- **Spring AI Alibaba** ：偏重“AI能力接入”——让Java应用方便地调用各种大模型API，适合做RAG、聊天机器人等场景
- **AgentScope-Java** ：偏重“Agent工程化”——让开发者构建具有自主推理、工具调用、多Agent协作能力的智能体系统

两者不是竞争关系，而是 **可以配合使用** 的关系。AgentScope负责Agent的“大脑”（推理、决策、行动），Spring AI Alibaba负责“感官”（接入各种AI能力）。

## 二、核心概念

AgentScope-Java 2.0的核心设计思路非常清晰—— **提供两种Agent，覆盖从简单到复杂的所有场景** 。

### 2.1 ReActAgent：最轻量的推理核心

**ReActAgent** 是AgentScope最基础的Agent实现，它实现了完整的 **ReAct（Reasoning + Acting）推理循环** 。

所谓ReAct，就是让LLM在“ **思考→行动→观察→再思考** ”的循环中自主完成任务：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3SCLUkuu2IGL7Vaa62rytic7mhNN1SP6ZbAHv3sfWk7q8wPA1GWJMhGyF7eYhdY2pNRzXVE4FsUwjSzZsic4icxX5BDrJfqyeXRPQCMEpVgNGk/640?wx_fmt=webp&from=appmsg#imgIndex=1)

ReActAgent适合 **轻量级、单次对话、不需要持久化状态** 的场景。

### 2.2 HarnessAgent：生产级的工程化封装

**HarnessAgent** 是AgentScope 2.0推荐的 **生产级入口** 。

它在ReActAgent的基础上，额外封装了一套 **工程化能力** ：

| 工程能力 | 说明 |
| --- | --- |
| **工作区（Workspace）** | Agent的人格、知识、技能、记忆统一沉淀在结构化工作区中 |
| **长期记忆（Memory）** | 跨会话的记忆持久化和语义检索 |
| **会话持久化（Session）** | 对话状态自动保存，重启后无缝恢复 |
| **子Agent编排** | 主Agent可以委派任务给多个子Agent |
| **沙箱隔离（Sandbox）** | 工具执行在隔离环境中运行，保证安全 |
| **上下文压缩（Compaction）** | 长对话自动压缩，防止上下文溢出 |

**核心区别** ：ReActAgent解决的是“这一次对话怎么跑”，HarnessAgent解决的是“长期运行的Agent怎么稳定、安全、可扩展”。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3SCLUkuu2IHLia8uWeXJjAd09icD2EFNMQCHgicOTvz6T4TUo4zWuuicRGL6DAMMibzusD736bb7AbvIFYspic1VNBtebib2ulw7vuoeicxxM24sicnU/640?wx_fmt=webp&from=appmsg#imgIndex=2)

**我的建议** ： **大部分场景直接用HarnessAgent** 。

虽然看起来多了一些配置，但这些工程能力在生产环境中几乎是必需的。

## 三、5分钟跑通第一个Agent

### 3.1 前置要求

AgentScope-Java 2.0需要 **JDK 17或更高版本** ，推荐使用 `Maven 3.9+` 。

检查你的Java版本：

```
java -version
# 需要输出 17 或更高
```

### 3.2 添加Maven依赖

AgentScope的依赖设计很清晰—— **核心模块和模型扩展分离** 。

**第一步：添加核心依赖**

```
<dependency>
    <groupId>
            io.agentscope
          </groupId>
    <artifactId>agentscope-harness</artifactId>
    <version>2.0.0</version>
</dependency>
```

`agentscope-harness` 会自动引入 `agentscope-core` ，包含了ReActAgent和HarnessAgent的核心实现。

**第二步：添加模型扩展**

根据你要用的模型，添加对应的扩展依赖。以通义千问（DashScope）为例：

```
<dependency>
    <groupId>
            io.agentscope
          </groupId>
    <artifactId>agentscope-extensions-model-dashscope</artifactId>
    <version>2.0.0</version>
</dependency>
```

### 3.3 配置API Key

AgentScope通过环境变量读取API Key。以DashScope为例：

```
export DASHSCOPE_API_KEY="sk-你的API密钥"
```

如果你用的是DeepSeek或OpenAI兼容的服务：

```
export OPENAI_API_KEY="sk-你的API密钥"
```

### 3.4 第一个Agent：最简示例

下面这段代码是AgentScope-Java的“Hello World”——创建一个能对话的Agent。

```
package 
            com.example;
          

import 
            io.agentscope.core.ReActAgent;
          
import 
            io.agentscope.core.agent.RuntimeContext;
          
import 
            io.agentscope.core.formatter.openai.OpenAIChatFormatter;
          
import 
            io.agentscope.core.message.UserMessage;
          
import 
            io.agentscope.core.model.GenerateOptions;
          
import 
            io.agentscope.core.model.OpenAIChatModel;
          
import 
            io.agentscope.core.tool.Toolkit;
          
import 
            io.agentscope.harness.HarnessAgent;
          
import 
            java.nio.file.Path;
          

public class FirstAgent {
    public static void main(String[] args) {
        // 1. 创建Model（以DeepSeek为例）
        String apiKey = 
            System.getenv(
          "DEEPSEEK_API_KEY");
        OpenAIChatModel model = 
            OpenAIChatModel.builder()
          
            .apiKey(apiKey)
            .modelName("deepseek-chat")
            .baseUrl("
            https://api.deepseek.com"
          )
            .stream(true)                    // 启用流式输出
            .enableThinking(true)            // 启用思考模式
            .formatter(new OpenAIChatFormatter())
            .defaultOptions(
            GenerateOptions.builder()
          
                .thinkingBudget(1024)        // 思考token预算
                .build())
            .build();

        // 2. 创建Agent
        HarnessAgent agent = 
            HarnessAgent.builder()
          
            .name("Assistant")
            .sysPrompt("你是一个乐于助人的AI助手，请友好简洁地回答问题。")
            .model(model)
            .workspace(
            Path.of(
          "./workspace"))
            .build();

        // 3. 发送消息并获取回复
        UserMessage userMsg = new UserMessage("你好，请介绍一下自己");
        String reply = 
            agent.call(userMsg,
           
            RuntimeContext.empty())
          
            .block()
            .getTextContent();
        
            System.out.println(reply);
          
    }
}
```

**代码拆解** ：

- **第1步** ：创建 `OpenAIChatModel` ，配置API地址、模型名称、是否流式输出、是否启用思考模式
- **第2步** ：用 `              HarnessAgent.builder()            ` 创建Agent，指定名称、系统提示词、模型和工作区目录
- **第3步** ：构造 `UserMessage` ，调用 `              agent.call()            ` 获取回复

**运行后** ，你会看到Agent的回复。整个过程不到10行核心代码，一个能对话的AI Agent就跑起来了。

## 四、工具系统：让Agent“长出手脚”

> 有些小伙伴可能会说：“Agent光会聊天有什么用？我要的是它能调用工具、执行操作！”

别急。AgentScope的 **工具系统** 就是干这个的。

没有工具的Agent只能“纸上谈兵”。AgentScope通过 `@Tool` 注解，让开发者可以 **把任意Java方法注册为Agent可调用的工具** 。

### 4.1 定义工具

用 `@Tool` 和 `@ToolParam` 注解定义工具：

```
import 
            io.agentscope.core.tool.Tool;
          
import 
            io.agentscope.core.tool.ToolParam;
          

public class WeatherTools {
    
    @Tool(name = "get_weather", description = "获取指定城市的当前天气")
    public String getWeather(
        @ToolParam(name = "city", description = "城市名称，例如'北京'") 
        String city
    ) {
        // 这里可以调用真实的天气API
        return city + "今天晴，温度25°C";
    }
    
    @Tool(name = "calculate", description = "执行数学计算")
    public double calculate(
        @ToolParam(name = "expression", description = "数学表达式") 
        String expression
    ) {
        // 这里可以集成表达式计算引擎
        return 42.0;
    }
}
```

**关键点** ：

- `@Tool` 的 `name` 是工具的唯一标识，Agent调用时使用此名称
- `@Tool` 的 `description` 描述工具功能，Agent根据此描述决定何时调用
- `@ToolParam` 标注在方法参数上，描述参数的含义

### 4.2 注册工具

创建 `Toolkit` 实例，将工具注册进去：

```
// 创建工具集
Toolkit toolkit = new Toolkit();

            toolkit.registerTool(
          new WeatherTools());

// 将工具集传给Agent
HarnessAgent agent = 
            HarnessAgent.builder()
          
    .name("Assistant")
    .sysPrompt("你是一个可以使用工具的助手。")
    .model(model)
    .toolkit(toolkit)              // 注册工具
    .workspace(
            Path.of(
          "./workspace"))
    .build();
```

### 4.3 带工具的Agent

```
public class ToolCallingExample {
    public static void main(String[] args) {
        // 创建Model
        OpenAIChatModel model = ...;
        
        // 创建工具集
        Toolkit toolkit = new Toolkit();
        
            toolkit.registerTool(
          new WeatherTools());
        
        // 创建Agent并注册工具
        HarnessAgent agent = 
            HarnessAgent.builder()
          
            .name("Assistant")
            .sysPrompt("你是一个可以使用工具的助手。当用户问天气时，调用get_weather工具。")
            .model(model)
            .toolkit(toolkit)
            .build();
        
        // 用户提问，Agent会自动决定是否调用工具
        UserMessage userMsg = new UserMessage("北京今天天气怎么样？");
        String reply = 
            agent.call(userMsg,
           
            RuntimeContext.empty())
          
            .block()
            .getTextContent();
        
            System.out.println(reply);
          
        // 输出：北京今天晴，温度25°C
    }
}
```

**关键理解** ：Agent在ReAct循环中会 **自主决定** 是否调用工具、调用哪个工具、何时调用。开发者只需要定义工具，Agent自己会判断“什么时候该用”。

## 五、多Agent协作

> 有些小伙伴可能会问：“一个Agent不够用怎么办？复杂任务需要多个Agent协作怎么搞？”

AgentScope 2.0提供了 **orchestrator + workers** 模式来实现多Agent协作。

### 5.1 核心模式

2.0版本的核心理念是： **主Agent扮演“主持人”，子Agent扮演“参与者”** 。

主Agent负责接收用户任务、拆解任务、委派给子Agent、汇总结果。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3SCLUkuu2IFbLMezp7icuRXrZVx8yibxWCFAvZmrTT81KxGHKFGaAibrrgayREsYbM5RRPWtygjgvL2FUfaJ43WYwQ2dCgnROPaN4t1tfAjpZs/640?wx_fmt=webp&from=appmsg#imgIndex=3)

### 5.2 定义子Agent

子Agent可以通过 **文件驱动** 的方式定义——在 `workspace/subagents/` 目录下创建`.md` 文件：

**workspace/subagents/ [weather.md](http://weather.md/)** ：

```
id: weather
description: 查城市天气。输入：城市名 + 日期。输出：温度区间、是否下雨。
sysPrompt: |
  你是一个气象助理。用户给你一个城市和日期，你返回：
  - 温度（高/低）
  - 是否下雨
  - 是否需要带伞
  严格三行，不超过60字。
```

**workspace/subagents/ [flight.md](http://flight.md/)** ：

```
id: flight
description: 查航班信息。输入：出发城市 + 到达城市 + 日期。
sysPrompt: |
  你是一个航班查询助理。根据用户输入给出一个mock航班号和起降时间。
```

### 5.3 Java端补强

如果子Agent需要调用Java端的工具（比如真实的天气API），可以在Java端再注册一份：

```
import 
            io.agentscope.harness.agent.subagent.SubagentDeclaration;
          

// Java端补强weather子Agent
SubagentDeclaration weather = 
            SubagentDeclaration.builder()
          
    .name("weather")
    .description("查城市天气；输入城市+日期，返回温度区间和是否带伞")
    .inlineAgentsBody("你是一个气象助理，会调用工具查询真实天气")
    .build();

// 在HarnessAgent中注册子Agent
HarnessAgent agent = 
            HarnessAgent.builder()
          
    .name("TravelAssistant")
    .model(model)
    .subagent(weather)          // 注册子Agent
    .workspace(
            Path.of(
          "./workspace"))
    .build();
```

**主Agent会自己决定** ：是否需要调用子Agent、调用哪些子Agent、调用顺序是什么。

## 六、底层原理

### 6.1 分层架构

AgentScope-Java采用 **经典的分层架构设计** ：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3SCLUkuu2IEicjeNOs5CWYFweNqA5h4TE0IYdEFKLzGAB4MvT6TljQ1iauy4u3pVXowVkiaiaIpnCu0lDdqw1B3MRMQia5pAf4c0UCEia2qsoVVTo/640?wx_fmt=webp&from=appmsg#imgIndex=4)

AgentScope的整体架构可以清晰分为四层：

- **模型适配层** ：负责与不同LLM提供商通信，支持OpenAI协议、DashScope（通义千问）、Anthropic Claude、Google Gemini等
- **ReAct推理层** ：实现ReAct推理循环（思考→行动→观察→再思考），是整个Agent的“大脑”
- **Harness工程化层** ：在ReAct之上封装了工作区、记忆、会话、子Agent、沙箱等工程能力
- **应用层** ：你的业务代码

### 6.2 ReAct推理循环的执行流程

当一个用户消息进入Agent时，ReAct循环的执行流程如下：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3SCLUkuu2IG5KhbEagHGRKQZQjWpTSiaYfAD86tDuFia0Qm0wKlDXicJQ8HrY4ibicpNnzZEXmumdQaZNxcxx7dZtBFslB3ZCTiceyVGNqcVwWu4w/640?wx_fmt=webp&from=appmsg#imgIndex=5)

HarnessAgent在ReAct循环的 **关键时机插入了Hook** ，实现了工作区加载、记忆读写、会话持久化等功能。

### 6.3 分布式部署架构

AgentScope 2.0最核心的升级之一，就是 **原生支持分布式部署** 。

在单机开发阶段，状态默认落到本地 `workspace` 目录。

进入生产部署后，只需把状态后端切换为分布式存储：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3SCLUkuu2IHTWlRQ6Ga1Mic0KdofPIbf65zJOblXfCPFhB8foMN84bq69D5dRqccRZZorYIupkqfqWJMLHBicjAgx1rJV1KQx9SEZlWRNIdJY/640?wx_fmt=webp&from=appmsg#imgIndex=6)

同一份业务代码，只需切换存储后端，就能从单机模式切换到分布式模式。

任意副本都能恢复任意用户的完整上下文。

## 七、实战案例：多Agent天气助手

> 有些小伙伴可能会说：“单个Agent我跑通了，但真实业务需要多个Agent协作，怎么办？”

AgentScope 2.0提供了 **文件驱动的Subagent机制** 。你只需要在 `workspace/subagents/` 目录下放几个`.md` 文件，主Agent就会自己决定“什么时候该叫谁”。

我们来看一个完整的实战—— **旅行助手** 。用户问：“我明天从北京飞杭州，落地后去西湖，要带伞吗？”

[1.x时代，你需要写代码串三个Agent（天气→航班→景点）。](http://1.xn--x,agent\(\)-de3ea2077kjmaud29jba83swurjp1bfr7cddch03cplwhsrm6xsm4dco0b874e./)

2.0时代，主Agent自己决定先查天气还是航班，三个Subagent **并行启动** 。

### 7.1 工程结构

```
travel-assistant/
├── 
            pom.xml
          
└── workspace/
    ├── 
            MEMORY.md
          
    ├── subagents/
    │   ├── 
            weather.md
          
    │   ├── 
            flight.md
          
    │   └── 
            attraction.md
          
    └── state/
        └── session-*.json    # JsonFileAgentStateStore自动生成
```

### 7.2 三个Subagent文件

**workspace/subagents/ [weather.md](http://weather.md/)** ：

```
id: weather
description: |
  查城市天气。
  输入：城市名 + 日期（YYYY-MM-DD）。
  输出：温度区间、是否下雨、是否需要带伞。
sysPrompt: |
  你是一个气象助理。
  用户给你一个城市和日期，你返回：
  - 温度（高/低，摄氏度）
  - 是否下雨
  - 是否需要带伞
  严格三行，不超过60字。
```

**workspace/subagents/ [flight.md](http://flight.md/)** ：

```
id: flight
description: |
  查航班信息（mock）。
  输入：出发城市 + 到达城市 + 日期。
  输出：航班号、起飞时间、到达时间。
sysPrompt: |
  你是一个航班查询助理。
  根据用户输入给出一个mock航班号和起降时间。
  注意：测试环境，无需真查询，给出合理mock即可。
```

**workspace/subagents/ [attraction.md](http://attraction.md/)** ：

```
id: attraction
description: |
  景点信息助理（mock）。
  输入：城市 + 景点名。
  输出：开放时间、是否需要预约、周边交通。
sysPrompt: |
  你是一个导游助理。
  根据用户输入给出景点的实用信息。
```

这三份描述对主Agent来说是 **路由表** ——主Agent全靠 `description` 决定要不要 `spawn` 它们。

### 7.3 Java端补强Subagent

如果某个Subagent需要调用Java端的真实工具（比如 [weather.md背后要接真的天气API），可以在Java端再注册一份——](http://weather.xn--mdapi\),java-8g3fa6965n91cel748ara896itraj53cimk0x4drk2b2le809etodi78af12bvu6c/) **HarnessAgent会把文件+Java声明合并** ：

```
import 
            io.agentscope.core.model.DashScopeChatModel;
          
import 
            io.agentscope.core.tool.Toolkit;
          
import 
            io.agentscope.harness.HarnessAgent;
          
import 
            io.agentscope.harness.agent.subagent.SubagentDeclaration;
          
import 
            java.nio.file.Path;
          

public class TravelAssistant {
    public static void main(String[] args) {
        // 1. 创建Model
        DashScopeChatModel model = 
            DashScopeChatModel.builder()
          
            .apiKey(
            System.getenv(
          "DASHSCOPE_API_KEY"))
            .modelName("qwen-plus")
            .build();
        
        // 2. 创建Toolkit并注册天气查询工具
        Toolkit toolkit = new Toolkit();
        
            toolkit.registerTool(
          new WeatherLookupTool());  // 真实的天气API工具
        
        // 3. Java端补强weather subagent——tools白名单过滤继承自父agent的工具
        SubagentDeclaration weather = 
            SubagentDeclaration.builder()
          
            .name("weather")
            .description("查城市天气；输入城市+日期，返回温度区间和是否带伞")
            .inlineAgentsBody("你是一个气象助理，会调用工具查询真实天气")
            .build();
        
        // 4. 创建HarnessAgent，注册subagent
        HarnessAgent agent = 
            HarnessAgent.builder()
          
            .name("TravelAssistant")
            .model(model)
            .toolkit(toolkit)
            .workspace(
            Path.of(
          "./workspace"))
            .subagent(weather)  // Java端补强的subagent
            .build();
        
        // 5. 运行
        UserMessage userMsg = new UserMessage(
            "我明天从北京飞杭州，落地后去西湖，要带伞吗？"
        );
        String reply = 
            agent.call(userMsg,
           
            RuntimeContext.empty())
          
            .block()
            .getTextContent();
        
            System.out.println(reply);
          
    }
}
```

**关键理解** ：主Agent在推理过程中会 **自主决定** 是否需要调用Subagent、调用哪些Subagent、调用的顺序是什么。

整个“编排”过程由LLM完成，不需要你写死Pipeline。

## 八、实战案例：MCP协议工具

> 有些小伙伴可能会说：“工具调用要自己写Java类，如果要接入GitHub、数据库、Slack这些外部服务，难道每个都要自己封装？”

不用。

AgentScope 2.0支持 **MCP（Model Context Protocol）协议** ，你只需要在 `workspace/             tools.json           ` 里 **一行声明** 一个MCP server，Agent启动时 **自动发现并注册工具** 。

### 8.1 什么是MCP？

MCP是Anthropic在2024年推出的开放协议，让LLM应用以统一方式发现并调用外部工具。

AgentScope 2.0把MCP server作为Agent工具的一种“来源”——你在 `              tools.json            ` 里声明一个MCP server，Agent启动时通过stdio或sse协议连上它， **自动把server暴露的工具当作Agent自己的tool** 。

### 8.2 第一个MCP集成

**workspace/ [tools.json](http://tools.json/)** ：

```
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    }
  }
}
```

**[HarnessAgent.builder().workspace(path)](http://harnessagent.builder\(\).workspace\(path\)/)** 启动时会自动扫描 `workspace/             tools.json           ` 的 `mcpServers` 段、连接每个server、把工具注册到Agent—— **不需要额外开关** ：

```
HarnessAgent agent = 
            HarnessAgent.builder()
          
    .name("GitHubAssistant")
    .model(model)
    .workspace(
            Path.of(
          "./workspace"))  // 自动加载
            tools.json
          
    .build();
```

跑起来后，Agent就能调用GitHub MCP server暴露的 `create_issue` 、 `list_repos` 、 `search_code` 等工具了。

### 8.3 三种连接方式

MCP支持三种传输协议：

| 协议 | 适用场景 | 声明方式 |
| --- | --- | --- |
| **stdio** | 本地进程，最常见 | `command`  \+ `args` |
| **sse** | 远程HTTP SSE server | `url`  \+ `headers` |
| **ws** | 双向WebSocket | `url`  \+ `headers` |

**stdio示例** （接入本地文件系统）：

```
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "./data"]
    }
  }
}
```

**sse示例** （接入远程知识库）：

```
{
  "mcpServers": {
    "remote-knowledge": {
      "url": "
            https://mcp.example.com/sse"
          ,
      "headers": {
        "Authorization": "Bearer ${env:MCP_TOKEN}"
      }
    }
  }
}
```

### 8.4 不想写JSON？Java代码直接配

有时候你想在代码里动态拼参数——比如token从环境变量读、超时按环境切换。

这时候可以直接在Java代码里配：

```
import 
            io.agentscope.harness.agent.tools.McpServerConfig;
          
import 
            io.agentscope.harness.agent.tools.ToolsConfig;
          

ToolsConfig cfg = new ToolsConfig();
Map<String, McpServerConfig> servers = new LinkedHashMap<>();

McpServerConfig github = new McpServerConfig();

            github.setTransport(
          "stdio");

            github.setCommand(
          "npx");

            github.setArgs(List.of(
          "-y", "@modelcontextprotocol/server-github"));

            github.setEnv(Map.of(
          "GITHUB_PERSONAL_ACCESS_TOKEN", 
            System.getenv(
          "GITHUB_TOKEN")));

            servers.put(
          "github", github);

            cfg.setMcpServers(servers);
          
// 然后通过HarnessAgent的toolsConfig()方法传入
```

效果和 `              tools.json            ` 完全一样。

### 8.5 常见的MCP Server

| MCP Server | 用途 | 安装命令 |
| --- | --- | --- |
| **server-github** | GitHub操作（创建Issue、搜索代码等） | `npx -y @modelcontextprotocol/server-github` |
| **server-filesystem** | 本地文件系统读写 | `npx -y @modelcontextprotocol/server-filesystem` |
| **server-postgres** | PostgreSQL数据库查询 | `npx -y @modelcontextprotocol/server-postgres` |
| **server-slack** | Slack消息发送 | `npx -y @modelcontextprotocol/server-slack` |
| **server-puppeteer** | 浏览器自动化（网页抓取、截图） | `npx -y @modelcontextprotocol/server-puppeteer` |

接入MCP生态后，AgentScope的Agent能力边界被极大地扩展了—— **只要能通过MCP暴露的工具，Agent都能调用** 。

## 九、优缺点

### 优点

**1\. Java生态无缝集成** AgentScope完美兼容Spring Boot、Spring Cloud、Maven等Java主流技术栈。对于Java团队来说，学习曲线非常平缓。

**2\. 双Agent架构，覆盖全场景** ReActAgent满足轻量级需求，HarnessAgent覆盖生产级工程需求。从原型到生产，一套框架全搞定。

**3\. 完善的工具系统** 通过 `@Tool` 注解即可将任意Java方法注册为Agent工具，Agent在ReAct循环中自主决定调用时机。

**4\. 原生多Agent协作** 内置orchestrator + workers模式，主Agent可以委派任务给多个子Agent，支持同步和异步两种模式。

**5\. 生产级工程能力** 工作区、长期记忆、会话持久化、上下文压缩、沙箱隔离——HarnessAgent把企业级Agent需要的工程能力全部打包。

**6\. 分布式部署原生支持** 支持Redis、MySQL、PostgreSQL等多种状态存储后端，支持Kubernetes水平扩展。

**7\. 多模型支持** 内置OpenAI协议（DeepSeek、GLM、Ollama等）、DashScope（通义千问）、Anthropic Claude、Google Gemini。

**8\. MCP/A2A协议支持** 支持Model Context Protocol和Agent-to-Agent协议，可以接入MCP生态的工具和服务。

### 缺点

**1\. 相对较新** AgentScope-Java 1.0于2025年12月发布，2.0于2026年7月GA。相比Spring AI等成熟框架，社区积累较少。

**2\. 学习曲线** HarnessAgent的工程化概念（工作区、记忆、子Agent等）需要一定的学习成本。

**3\. 生态不如Spring AI丰富** 目前第三方集成和扩展的数量不如Spring AI Alibaba。

**4\. 文档偏英文** 虽然官方提供了中文文档，但部分深度内容仍以英文为主。

## 十、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **智能客服系统** | 强烈推荐 | 多Agent协作+知识库RAG |
| **运维诊断Agent** | 强烈推荐 | 自主推理+工具调用+日志分析 |
| **金融分析Agent** | 强烈推荐 | 结构化输出+多步推理 |
| **代码辅助Agent** | 推荐 | 工具调用+代码执行沙箱 |
| **企业内部知识助手** | 推荐 | RAG+长期记忆 |
| **简单聊天机器人** | 可能过度设计 | 用Spring AI Alibaba即可 |
| **已有Spring AI生态** | 需评估 | 两者可以配合使用 |

## 总结

回到最初的问题： **Java开发者怎么做AI Agent？**

AgentScope-Java给出了一个非常完整的答案。

它不是“把Python框架翻译成Java”的简单移植，而是 **从Java生态的实际情况出发，专门为Java开发者设计的Agent框架** 。

**ReActAgent** 让你快速跑通Agent原型， **HarnessAgent** 让你把原型变成生产级应用。

`@Tool注解` 让工具定义像写普通Java方法一样自然， **子Agent系统** 让多Agent协作变得清晰可控。

最关键的是—— **它让Java开发者不需要为了做Agent去学Python** 。

开源地址

- **GitHub** ： [https://github.com/agentscope-ai/agentscope-java](https://github.com/agentscope-ai/agentscope-java)
- **官方文档** ： [https://java.agentscope.io/](https://java.agentscope.io/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)