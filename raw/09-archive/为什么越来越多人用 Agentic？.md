---
title: "为什么越来越多人用 Agentic？"
source: "https://mp.weixin.qq.com/s/qLVHvKXF1jNu91Ef8f4I8Q"
author:
  - "[[苏三]]"
published:
created: 2026-11-03
description:
tags:
  - "clippings"
---
苏三 苏三说技术 *2026年11月3日 08:20*

## 大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

做 AI Agent 的同学，大概率都经历过这样一个阶段。

在笔记本上跑 Demo 的时候，感觉很丝滑：给大模型丢几个工具，它自己就能思考、调用、总结，几行代码就搞定一个智能体。

但是一旦把这套东西搬到生产环境，面对真实的并发、复杂的网络环境、以及业务方对“稳定交付”的要求时，问题就全暴露出来了。

最常见的几个坑：

- 用户问了个问题，Agent 没去查数据库，直接瞎编了一个答案；
- 某一步工具调用超时了，整个 Agent 卡死，也没个重试机制；
- 想看看到底是哪一步耗时太长，结果框架只返回了一段最终文本，中间的调用链路完全是黑盒。

这几年，Agent 框架出了不少，但很多是第一代的设计思路——它们是为了让开发者快速体验“哇，AI 能自己干活”而生的，而不是为了让架构师把它安稳地放进生产环境而设计的。

`Agentic` 就是在这个背景下越来越受关注的一个框架。

它不是教你如何让模型更聪明，而是教你如何把 AI 约束在一个可控、可观测的工程轨道里。

今天这篇文章，就专门跟大家一起聊聊Agentic，希望对你会有所帮助。

## 一、第一代框架为什么在“裸奔”？

有些小伙伴可能会说：“LangChain、AutoGen 不都能做 Agent 吗？为什么还要搞个新东西？”

能。

但很多框架的设计初衷，是让你在笔记本上跑通一个 Demo，而不是让你把几万个 Agent 放在生产环境里扛并发。

传统的 Agent 开发，通常是把一堆工具塞给大模型，然后大模型自己在那边“想”：“我要调这个，我要查那个。”

这种模式在 Demo 里很酷，但在生产环境里，就像让一个没有监控、没有日志、没有权限控制的实习生去操作核心数据库，你心里能踏实吗？

**Agentic 解决的核心痛点有三个：**

- **黑盒问题**
	：Agent 跑完了只给你一段文本，中间调了什么、哪一步耗时、为什么失败，你完全不知道。
- **配置问题**
	：工具的参数、API Key 全写在代码里，换一个环境就得改代码重发版。
- **协作问题**
	：多个 Agent 之间怎么通信？如果跑一半需要人工审批怎么办？传统的框架让你自己造轮子。

Agentic 的定位，就是把这些“生产环境才暴露的问题”，在架构底层直接焊死。

## 二、Agentic 的核心架构

Agentic 的团队说，他们的 Agent 循环代码只有几百行，直接调用 LLM API。

这意味着它没有藏着一堆你读不懂的复杂抽象。

出问题时，你可以直接扒开底裤看。

下面这张图，是 Agentic 的整体架构设计：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/HUV4yMdu0rf1eSzbyFNL6JFibl9ukKW5fPk44qZUffJ5jTcXFXJtjIWFQdOxMUNwHxbYMTNKFXtJc2XlZb1ibVuu592po74hhXuKz6NPT159U/640?wx_fmt=png&from=appmsg#imgIndex=0)

Agentic 有几个非常明确的选择：

1. **极简抽象**
	：你只需要懂 Agent、Tool、Run、Thread。不需要去拼装复杂的 DAG 图。
2. **事件驱动**
	：Agent 不是返回一段死板的文本，而是往外吐 **类型化的事件** 。你可以订阅这些事件，做流式输出、做后台通知。
3. **基于 Ray**
	：底层用 Ray 的 Actor 模型来托管 Agent。每个 Agent 就是一个独立的 Actor，有自己的状态和消息队列，天然支持高并发。

## 三、深入原理

> 有些小伙伴可能会问：“Agent 到底是怎么决定下一步做什么的？它为什么会调用工具？它又是怎么知道自己该停下来的？”

我们来看下面这张图，这是 Agentic 最核心的 **ReAct 循环（推理与行动）** ：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/HUV4yMdu0rd07qrQBzzApenCy4RKbFiczOPBF8Rpw0XvnTHlSlOXoicicZDtY6eKibJHxL2g3Yd9ZIBEasgLMFI1via9OCjqYZjK2RD9zWY3CLOo/640?wx_fmt=png&from=appmsg#imgIndex=1)

在这个循环里，Agentic 做了哪些工程增强呢？

**第一，工具执行是异步、有配置的。**

工具不只是一个简单的函数。它在 Agentic 里是可以配置超时、重试、认证的独立组件。

**第二，事件是类型化的。**

不是只给你最终结果，而是告诉你每一步： `ToolCallEvent` 、 `ToolResultEvent` 、 `LLMResponseEvent` 。这为后续的可观测性打下了基础。

**第三，Human-in-the-loop 原生支持。**

如果工具执行需要人工审批，Agent 可以无限期暂停，等待你批准后再继续，而不是傻等或者直接报错。

## 四、用 Agentic 搭一个“不瞎编”的助手

假设我们就要解决开头那个“数据瞎编”的问题。

我们需要一个 Agent，强制它在回答问题前，必须调用工具查库。

### 4.1 定义工具

```
from 
            agentic.common
           import Agent, Tool

# 定义工具时，加上严格的描述，告诉大模型必须用它
def query_db(sql_query: str) -> str:
    """
    查询销售数据库。
    当你需要回答关于销售、订单、金额的问题时，必须调用此工具。
    """
    # 模拟查库操作
    return "昨天销售额为 12000 元。"

sales_tool = Tool(
    name="query_sales_db",
    description="查询销售数据的唯一工具",
    function=query_db
)
```

### 4.2 构建 Agent 并注入系统提示词

```
# 构建 Agent
sales_agent = Agent(
    name="销售助手",
    instructions="""
    你是一个数据分析助手。
    规则：
    1. 凡是涉及具体销售数据的问题，必须先调用 query_sales_db 工具。
    2. 严禁在未调用工具的情况下，凭空捏造数据。
    3. 如果工具调用失败，直接回答“数据获取失败”，不要编造。
    """,
    tools=[sales_tool],
    model="gpt-4o" # 这里底层是 Litellm，随便切模型
)
```

### 4.3 运行并捕获事件流

```
# 运行 Agent
run = 
            sales_agent.run(
          "昨天销售额多少？")

# 消费事件流
for event in 
            run.stream_events():
          
    if 
            event.event_type
           == "ToolCallEvent":
        print(f"[系统日志] Agent决定调用工具: {
            event.tool_name}
          ")
    elif 
            event.event_type
           == "ToolResultEvent":
        print(f"[系统日志] 工具返回结果: {
            event.result}
          ")
    elif 
            event.event_type
           == "TextEvent":
        # 流式输出给用户
        print(
            event.content,
           end="", flush=True)
```

通过上面这段代码，如果模型产生幻觉想去捏造数据，事件流里就不会出现 `ToolCallEvent` ，你在后台一眼就能看出来它没查库。

这就是 **工程化可控** 的价值。

## 五、怎么帮你定位“Agent 跑歪了”？

这是 Agentic 最厉害的地方之一：由于它输出的日志是结构化的事件流，你可以直接把日志喂给 AI，让它充当“排障专家”。

**场景** ：你的助手回答了一个错误的数据，用户投诉了。

**第一步：将 Trace 日志喂给 AI**

你把上面运行产生的结构化事件流复制下来，发给 AI：

> “这是一次失败的 Agent 执行记录。帮我分析一下，为什么它没有调用 `query_sales_db` 工具就给出了答案。”

**第二步：AI 分析并定位根因**

AI 看了日志，告诉你：

> “我在日志中发现，在第一步 LLM 返回时，没有触发 `ToolCallEvent` 。随后 Agent 直接输出了 `TextEvent` 。  
> 这说明大模型忽略了系统提示词中的强制要求。  
> 建议排查：
> 
> 1. 你的工具 `description` 可能不够有吸引力。
> 2. 可以尝试在系统提示词里加重语气，比如‘不调用工具将导致系统崩溃’。”

**第三步：让 AI 帮你写测试用例防回归**

你继续说：

> “帮我写一个基于 pytest 的测试用例，模拟大模型不调用工具的情况，确保我的 Agent 会抛出异常。”

AI 会为你生成一份测试代码，确保下次发版前，这种“不查库瞎编”的回归问题能被自动化测试拦截。

## 六、优缺点

### 优点

**1\. 极简抽象，透明可控**  
只有四个核心概念，没有过度封装。出问题你可以直接读循环代码。

**2\. 事件驱动，流式响应**  
不是返回一段死文本，而是产生类型化的事件流。支持多通道、后台运行、流式 UI。

**3\. Human-in-the-loop 原生支持**  
Agent 可以无限期等待人工输入，通知可通过邮件或 Webhook 推送，不需要你写复杂的死循环。

**4\. 工程化内置**  
日志、Trace、上下文管理、工具认证——生产环境需要的东西，框架天生自带。

**5\. 基于 Ray 的运行时**  
Actor 模型天然支持异步和并发，处理复杂 Agent 团队更从容。

### 缺点

**1\. 生态相对较新**  
它不是 LangChain 那种“什么都有”的巨无霸，组件和第三方集成的数量还在成长中。

**2\. 基于 Ray，有学习成本**  
如果你不熟悉 Ray 框架，理解底层的 Actor 模型和分布式运行需要花点时间。

**3\. Python 版本要求严格**  
目前在 Python 3.12 下运行最稳定，不支持 3.13+（因为底层 Ray 的兼容性）。

**4\. 需要转变思维**  
习惯了写 `if/else` 或者简单的 Chain 调用的人，需要适应“基于事件订阅”的异步编程思维。

## 七、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **生产级 Agent 服务** | ✅✅✅ 强烈推荐 | 事件流、Trace、Human-in-the-loop 是刚需 |
| **需要强制 Agent 行为** | ✅✅✅ 强烈推荐 | 工具配置可控，结合提示词可防止瞎编 |
| **多 Agent 协作团队** | ✅✅✅ 强烈推荐 | Ray Actor 天然支持并发和状态隔离 |
| **需要流式/后台通知** | ✅✅✅ 强烈推荐 | 多通道事件流原生支持 |
| **快速 Demo/原型** | ⚠️ 需评估 | LangChain 可能更快出效果 |
| **需要大量第三方插件** | ⚠️ 需评估 | 生态还在追赶中 |

## 八、写在最后

回到最初的问题： **为什么越来越多人用 Agentic？**

因为它把 Agent 从“Demo 玩具”变成了“生产系统”。

第一代 Agent 框架解决了“能不能跑起来”的问题。

Agentic 解决的是“ **跑起来之后，我能不能知道它在干什么、能不能控制它、能不能让它稳定地跑完** ”的问题。

事件流让你看清每一步，Trace 让你回溯每一次失败，Human-in-the-loop 让你在关键节点介入。

参考资源：

- GitHub： [https://github.com/supercog-ai/agentic](https://github.com/supercog-ai/agentic)
- 官方文档： [https://supercog-ai.github.io/agentic/](https://supercog-ai.github.io/agentic/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)