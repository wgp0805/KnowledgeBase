---
title: "当 AI Agent 遇到 Nacos：OpenClaw.NET 集成入门 - 张善友"
source: "博客园"
url: "https://www.cnblogs.com/shanyou/p/23130581"
date: "2026-09-26T23:28:00Z"
score: 1.0
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 当 AI Agent 遇到 Nacos：OpenClaw.NET 集成入门 - 张善友

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/shanyou/p/23130581  
> **抓取日期**: 2026-09-27  
> **相关性评分**: 1.0

——不写一行 LLM 调用，让 Agent 确定性地发现并调用注册中心里的 MCP 工具

![image](https://img2024.cnblogs.com/blog/510/202609/510-20260927072614239-907794835.png)

* * *

## 从一个场景说起

假设你在写一个 AI Agent，它要"查一下杭州的天气"。天气服务不是你写的，它注册在公司的 Nacos 集群里，是一个标准的 MCP Server。

要完成这个任务，Agent 得做一串动作：发现服务、确认版本、拿到工具列表和参数 schema、发起调用、处理失败、留审计记录。

常见的做法是让大模型自己去摸索。实测下来，这种方式每轮要消耗上万个 input token，而且结果不稳定——如果注册表里的描述写着"天气"、后端实际只有时间工具，模型还可能直接编一个气温出来。

OpenClaw.NET 的做法是把这串动作做成一条确定性管线，全程不调用 LLM。本文介绍这套基于 Nacos 3.2.4 AI 注册中心和 MCP 协议的集成怎么用、背后是什么结构。

* * *

## 一、Nacos AI 管理中心管什么

Nacos 3.x 把 AI 资源提升为与配置管理、服务发现并列的核心能力，叫 AI Registry。它管的是：Skill、Agent、MCP Server、Prompt、AgentSpec 这些东西怎么注册进平台、怎么治理、怎么按版本发布、怎么被运行时发现。

先建立一个认知，很多集成问题都出在这里：

> AI 资源不是配置，也不是普通服务。

配置管理关心内容的发布和监听，服务发现关心实例健康。MCP Server 的治理重点是另外一些东西：协议类型、端点、版本，以及"工具开关"（toolSpec.ToolsMeta）——管理员可以在 Nacos 控制台直接关掉某个 MCP Server 的某个工具，运行时必须遵守。

OpenClaw.NET 走的是 Nacos MCP Router 模式：由 Router 统一发现注册表中的 MCP Server，对外提供 search / add / use 三个工具。

* * *

## 二、架构：三层各管一摊

职责划分是这样的：

> Registry 决定"存在什么、谁可见"，Router 决定"如何被发现和连接"，OpenClaw Runtime 决定"何时、以何身份、经何审批执行"。
    
    
    ┌──────────────────────────────────────────────┐
    │  Nacos 3.2.4 · AI 管理中心                     │
    │  MCP 元数据 / 工具开关 / 端点 / 版本              │
    └────────────────┬─────────────────────────────┘
                     │ RedNb.Nacos.Ai（分页 blur 检索）
    ┌────────────────▼─────────────────────────────┐
    │  NacosMcpRouter（.NET global tool）            │
    │  search → add → use 三工具 · ONNX 本地向量检索  │
    └────────────────┬─────────────────────────────┘
                     │ MCP 协议
    ┌────────────────▼─────────────────────────────┐
    │  OpenClaw.Adapters.Nacos      OpenClaw.Adapters│
    │  （provider：发现/绑定/        .Nacos.Events    │
    │   失败规范化）                 （失效事件）      │
    ├──────────────────────────────────────────────┤
    │  OpenClaw.Core 契约 + OpenClaw.Agent 策略引擎   │
    │  确定性排序 / 有界缓存 / 熔断 / 审计回放          │
    ├──────────────────────────────────────────────┤
    │  meta-skill DAG：tool_call 步骤 capability_ref  │
    └──────────────────────────────────────────────┘
    

层 | 组件 | 职责  
---|---|---  
注册中心 | Nacos 3.2.4 AI 管理中心 | 托管 MCP Server 元数据、版本、端点、工具开关  
发现路由 | NacosMcpRouter | search（搜索 Server）→ add（安装连接）→ use（调用工具）  
运行时 | OpenClaw.NET | 能力解析、策略审批、缓存熔断、审计，全程零 LLM 调用  
  
* * *

## 三、上手：Agent 侧只需要几行声明

接入的复杂工作都在 adapter 和运行时里。对 Agent 开发者来说，只需要在 skill 文件里声明一个能力引用：
    
    
    - id: weather
      kind: tool_call
      capability_ref:
        provider: nacos
        binding: dynamic
        intent:
          task_description: "查询杭州今天天气"
          keywords: ["天气", "杭州"]
      tool_args:
        city: 杭州
    

几个字段的含义：

  * `provider: nacos`：这个能力从 Nacos 注册中心解析，不是本地静态绑定；
  * `binding: dynamic`：动态绑定，运行时按需搜索、选择最合适的 MCP Server 和工具；
  * `intent`：给 Router 的检索意图。Router 内部用 ONNX 做本地向量检索，不依赖外部 LLM。



解析和调用由 `AgentRuntime` / `MafAgentRuntime` 的同一条 capability 路径完成，没有 LLM 发现调用。你写的是意图，"找哪个 Server、调哪个工具、参数怎么填"由管线完成。

* * *

## 四、使用时会碰到的四个机制

使用侧很轻，但了解这几个机制对配置和排障有帮助。

### 4.1 协议防腐层

Router 的工具返回不是结构化 JSON，而是自然语言包裹 JSON 的"散文信封"，比如 search 的返回：
    
    
    ## 获取查询天气的步骤如下:
    ### 1. 当前可用的mcp server列表为:{"weather-mcp":{...}}
    ### 2. 从当前可用的mcp server列表中选择你需要的mcp server调add_mcp_server工具安装mcp server
    

OpenClaw.NET 把对这些中文字面量 marker 的解析收敛到一个独立的契约文件，并有测试钉住。上游协议变化的影响被限制在这一个点，业务代码不用动。同一套 adapter 同时兼容 Python 版和 .NET 版 Router。

实际影响：升级 Router 或 Nacos 版本时，只需要看 adapter 的兼容性说明。

### 4.2 缓存与世代

动态解析结果会缓存（TTL 300 秒、容量 1024、FIFO 驱逐），缓存键里编入了世代（generation）：
    
    
    key = "{provider.Id}:{generation}:{binding}:{intentKey}"
    

Nacos 侧配置一变，世代 +1，旧键直接失效，旧世代的在途解析晚到了也写不进新缓存。如果填充完成后发现世代变了，返回 `capability_stale_binding` 让调用方重试，不会静默使用旧绑定。

### 4.3 熔断

同一目标（安全域 + provider + 世代 + Server + 工具）连续失败 3 次，熔断 30 秒；成功一次立即复位；被策略阻止（Blocked）的失败不计入。熔断器容量满时，冷却中的熔断器不会被驱逐，只淘汰尚未熔断的条目。

### 4.4 失效事件

Nacos 配置变更的监听链路：
    
    
    Nacos 长轮询 → 内容 SHA-256 → 与上次哈希比对 → 不同则发布 CapabilityChange → 缓存全量清空
    

几点说明：

  * SHA-256 去重，防止 SDK 把初始快照当变更重复投递；
  * 只保留 digest，失效通道不传输、不落地配置正文；
  * 用保守的全量失效，正确性优先于缓存命中率。



* * *

## 五、安全模型：句柄不等于授权

这套集成里有一条原则贯穿始终：

> "A tool handle, never permission to execute." 能力句柄只是句柄，授权在每次执行时重新检查。

具体体现：

  1. 整个能力解析与执行被包装成名为 `resolve_capability` 的工具，先经过 OpenClawToolExecutor 的治理链（审批、hooks、审计、工具策略），再执行目标工具；
  2. userId / sessionId 随 MCP 请求的 `Meta` 字段传给 Router，审计链路完整；
  3. 缓存命中后会复检：如果当前 skill 策略已不允许某工具，动态绑定丢弃缓存重新解析，静态绑定保持 pin、在执行阶段拒绝；
  4. 注册表元数据不等于真实能力。即使注册中心的描述和后端实际能力不符，Gateway 的本地策略与授权依然生效。



* * *

## 六、上手 Checklist

按这个顺序把环境跑起来：

  1. 准备 Nacos 3.2.4，在 AI 管理中心注册你的 MCP Server（元数据、端点、版本、工具开关）；

  2. 安装 Router（.NET global tool，不需要 Python 环境）：
         
         dotnet tool install --global NacosMcpRouter
         

注意：Router 的 Console API client 默认连 `127.0.0.1:8080` 且不可覆盖，本地验证时把 Nacos Console 端口固定为 8080；

  3. 在 skill 文件中声明 `capability_ref`（见第三节），按需选择 `binding: dynamic`（动态发现）或静态绑定（固定目标）；

  4. 运行 Agent，观察治理链日志：能力解析、策略审批、工具调用、审计记录应一一对应，全程无 LLM 发现调用；

  5. 验证治理行为：在 Nacos 控制台关闭某个工具，确认运行时在数秒内完成失效并拒绝后续调用。




* * *

## 结语

Nacos 3.2.4 的 AI Registry 解决"有什么、谁可见"，OpenClaw.NET 运行时解决"能不能安全地用"。对使用者来说，这套集成的收益很直接：几行 YAML 声明意图，换来确定性的发现、调用和治理——成本可预测，行为可审计，失败有明确的降级路径。

* * *

_本文基于`https://github.com/clawdotnet/openclaw.net` @ `main`（2026-09-27）整理，涉及组件：OpenClaw.Adapters.Nacos(.Events)、CapabilitySlotExecutor、CapabilityBindingCache、NacosMcpRouter。_


---
> 原文链接: https://www.cnblogs.com/shanyou/p/23130581