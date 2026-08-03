---
title: "MCP 第五版 × OpenClaw.NET：从协议升级到生态编排 - 张善友"
source: "博客园"
url: "https://www.cnblogs.com/shanyou/p/22144007"
date: "2026-08-02T04:06:00Z"
score: 0.6
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# MCP 第五版 × OpenClaw.NET：从协议升级到生态编排 - 张善友

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/shanyou/p/22144007  
> **抓取日期**: 2026-08-02  
> **相关性评分**: 0.6

> **副标题** ：当 MCP 从"AI 的 USB"变成"Agent 里的迷你 SaaS"，OpenClaw.NET 如何成为那个 SaaS 的编排操作系统？
> 
> 基于 MCP 2026-07-28 第五版规范与 OpenClaw.NET PR #196（csharp-sdk v2.0 升级）的深度解读

* * *

![image](https://img2024.cnblogs.com/blog/510/202608/510-20260802165550109-1779904638.png)

## 引言：一次协议升级，一次部署范式的迁移

2026 年 7 月 28 日，MCP 协议发布第五版。最醒目的变化是**会话从协议层被彻底删除** ——MCP 从一个有状态的双向协议，变成了无状态的请求-响应协议。

这意味着什么？

  * 远程 MCP Server 可以像普通 HTTP 服务一样部署到 **Serverless、边缘节点或 Kubernetes**
  * 网关可以直接通过 `Mcp-Method` 和 `Mcp-Name` 请求头路由，**无需解析 JSON body**
  * 跨调用的状态不再藏在连接里，而是通过**显式业务句柄** 在工具参数中传递
  * 服务端反向请求客户端的能力，被 **MRTR（多轮往返请求）** 替代



与此同时，OpenClaw.NET 在 PR #196 中完成了向 **csharp-sdk v2.0** 的升级，全面拥抱 Streamable HTTP、协议协商（`server/discover`）、MCP Apps 代理端点、Tasks 扩展以及 JSON Schema 2020-12。

这篇文章要做的，不是重复协议文档，而是回答一个问题：**当 MCP 第五版让单个 Server 变得像迷你 SaaS 时，OpenClaw.NET 如何成为这些 SaaS 的编排操作系统？**

* * *

## 一、第五版核心变革：从"连接即状态"到"请求即自包含"

### 1.1 无状态核心：协议层的彻底解耦

旧协议（有状态） | 第五版（无状态） | 对 OpenClaw.NET 的影响  
---|---|---  
`initialize/initialized` 握手 | 每个请求自包含协议版本与能力 | Gateway 无需维护连接生命周期  
`Mcp-Session-Id` 粘性会话 | 移除协议层会话 | 支持轮询负载均衡，天然适配 K8s  
服务端内存保存客户端状态 | 状态外置到数据库/缓存 | 与 MetaSkill 显式状态管理哲学一致  
HTTP+SSE 长连接 | Streamable HTTP 请求-响应 | 与现有 HTTP 基础设施完全兼容  
  
**关键洞察** ：无状态化不是削弱 MCP，而是把它从"需要特殊照顾的协议"变成"可以标准运维的服务"。这对 OpenClaw.NET 的 Gateway 层是重大利好——网关规则可以大幅简化。

### 1.2 显式业务句柄：状态属于业务，不属于连接

第五版删除了协议会话后，跨调用状态（如浏览器实例、购物车、审批流程）通过**显式句柄** 传递：
    
    
    第一次调用: create_browser → 返回 browser_id
    后续调用: open_page(browser_id) → click(browser_id) → screenshot(browser_id)
    

这与 OpenClaw.NET 的 **MetaSkill DAG** 设计理念高度契合：

  * MetaSkill 的工作流节点之间本就通过**显式参数** 传递状态
  * 工具调用的 `browser_id` 本质上就是 DAG 边上的一个数据令牌（Token）
  * 状态生命周期由业务定义，可以跨实例、跨工具、甚至跨 Agent 传递



### 1.3 MRTR：连接可以断，流程不会丢

旧协议中，服务端可以主动请求客户端（如要求用户确认删除）。这依赖持续连接，在无状态架构下无法工作。

第五版引入 **MRTR（Multi Round-Trip Requests）** ：

  1. 客户端发起工具调用
  2. 服务端返回 `input_required`
  3. 客户端收集用户确认/参数
  4. 客户端携带 `inputResponses` \+ `requestState` **重新发起原始请求**
  5. **任意服务端实例** 继续完成任务



这与 OpenClaw.NET **Harness 引擎** 的"中断-恢复"机制天然互补：

  * Harness 可以将 `input_required` 状态持久化到任务存储
  * 用户响应后，Harness 重新调度任务到任意 Worker 实例
  * 真正实现"连接断、流程在、状态不丢"



* * *

## 二、PR #196 升级路径：OpenClaw.NET 的 MCP 2.0 实践

PR #196 不是简单的 SDK 版本升级，而是一次面向生产环境的架构对齐。以下是关键实现与第五版规范的映射：

### 2.1 Streamable HTTP 与协议协商
    
    
    // OpenClawHttpClient 中的协议协商
    // 1. 优先尝试 server/discover
    // 2. 404 或 -32601 时回退到 initialize
    // 3. 捕获协商版本，后续请求复用
    

**对应第五版** ：

  * 移除了硬编码的 `2025-03-26` 版本回退
  * 支持从 `McpDiscoverRequest` 的 `_meta` 信封中读取协议版本
  * 每个请求携带 `Mcp-Method` 和 `Mcp-Name` 请求头



### 2.2 网关层路由：从 JSON 解析到请求头识别
    
    
    // SendMcpAsync 中注入 Streamable HTTP 请求头
    Mcp-Method: tools/call
    Mcp-Name: search
    Mcp-Protocol-Version: 2026-07-28
    

**生产价值** ：

  * API Gateway、WAF、限流器可以直接根据请求头判断调用方法
  * 无需解析 JSON-RPC body，大幅降低网关 CPU 开销
  * 与 OpenClaw.NET 现有的 Gateway 路由体系无缝集成



### 2.3 MCP Apps 代理端点：从工具到界面

PR #196 实现了 `/apps/mcp/{appId}` 代理端点，对应第五版将 **MCP Apps** 纳入正式扩展框架。

**OpenClaw.NET 的差异化** ：

  * 普通 MCP Server 提供 App HTML，由 Agent Host 在沙箱 iframe 中渲染
  * OpenClaw.NET 的 **OpenSandbox** 可以为 MCP Apps 提供**安全沙箱环境**
  * 结合 TokenHub，App 的每次交互都可以被计量和审计



### 2.4 Tasks 扩展：从实验性 API 到正式扩展
    
    
    // 启用 Tasks 协议扩展
    tasks.EnableProtocol = true;
    

**与 Harness 的融合** ：

  * Tasks 的"任务句柄"模型与 Harness 的"工作流实例 ID"概念同构
  * 客户端可以查询、更新、取消任务——这正是 Harness 引擎的核心能力
  * 长时间异步操作（如批量数据处理、模型训练）可以通过 Tasks 标准接口暴露给 Agent



### 2.5 输入 Schema 的严格化与兼容性

PR #196 处理了第五版对 JSON Schema 2020-12 的升级：

  * 工具缺失 `inputSchema` 时当前被跳过（而非崩溃）
  * `AllowRelaxedInputSchemaValidation` 作为兼容性开关
  * 工具名称清理：LLM 工具名必须符合 `^[a-zA-Z0-9_-]+$`



**与 DDI Registry 的协同** ：

  * JSON Schema 2020-12 支持 `$ref`、`oneOf`、`anyOf`、`allOf`
  * 这与 DDI Registry 的数据契约定义能力深度对齐
  * 工具输入输出可以被注册、版本化、治理



* * *

## 三、融合架构：OpenClaw.NET 的差异化定位

文章中说："现在的 MCP 服务更像一个跑在 Agent 里的迷你 SaaS"。

如果单个 MCP Server 是迷你 SaaS，那么 **OpenClaw.NET 就是这些 SaaS 的编排操作系统** 。

### 3.1 架构定位：从"MCP Client"到"MCP 生态编排层"
    
    
    ┌─────────────────────────────────────────────────────────────┐
    │                      Agent Host / LLM                        │
    │         (Claude, GPT, DeepSeek, OpenClaw Agent)            │
    └──────────────────────┬──────────────────────────────────────┘
                           │
    ┌──────────────────────▼──────────────────────────────────────┐
    │              OpenClaw.NET Gateway (无状态核心)                │
    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
    │  │ Mcp-Method  │  │  缓存语义   │  │   OTel 链路追踪      │ │
    │  │ Mcp-Name    │  │  ttlMs      │  │  traceparent        │ │
    │  │ 路由        │  │  cacheScope │  │  tracestate/baggage │ │
    │  └─────────────┘  └─────────────┘  └─────────────────────┘ │
    │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
    │  │ OAuth/OIDC  │  │  限流/审计  │  │   协议协商           │ │
    │  │ 企业鉴权     │  │  Gateway    │  │  server/discover   │ │
    │  └─────────────┘  └─────────────┘  └─────────────────────┘ │
    └──────────────────────┬──────────────────────────────────────┘
                           │
            ┌──────────────┼──────────────┐
            │              │              │
    ┌───────▼──────┐ ┌────▼─────┐ ┌──────▼───────┐
    │   MCP Tools  │ │ MCP Apps │ │  MCP Tasks   │
    │  (技能服务)   │ │ (UI界面) │ │ (异步任务)   │
    │              │ │          │ │              │
    │ • 文件操作   │ │ OpenSandbox│ │ • 批量处理  │
    │ • 数据库查询 │ │ 沙箱渲染  │ │ • 模型训练  │
    │ • API 调用   │ │          │ │ • 审批流    │
    └───────┬──────┘ └────┬─────┘ └──────┬───────┘
            │             │              │
            └─────────────┼──────────────┘
                          │
    ┌─────────────────────▼───────────────────────────────────────┐
    │              MetaSkill DAG 编排层                        │
    │    (显式句柄传递 + TokenHub 计量 + Harness 状态恢复)       │
    └───────────────────────────────────────────────────────────┘
    

### 3.2 五大融合优势

#### 优势一：无状态 Gateway × 有状态 Harness

  * **Gateway 层** ：完全无状态，支持任意负载均衡策略，可水平扩展到边缘节点
  * **Harness 层** ：通过显式句柄和 Tasks 扩展，将状态持久化到 PostgreSQL/Doris
  * **结果** ：获得 Serverless 的弹性 + 有状态工作流的可靠性



#### 优势二：MCP Apps × OpenSandbox

  * MCP Apps 提供交互式 HTML 界面
  * OpenSandbox 提供**安全沙箱 iframe 渲染环境**
  * TokenHub 对 App 的每次交互进行 Token 计量
  * **结果** ：Agent 不仅能调用工具，还能安全地操作复杂 UI



#### 优势三：Tasks 扩展 × Harness 异步引擎

  * Tasks 定义了标准的"创建-查询-更新-取消"任务接口
  * Harness 引擎提供 DAG 级别的任务编排、重试、超时、熔断
  * **结果** ：长时间任务（如报表生成、数据迁移）可以被 Agent 发起、监控、干预



#### 优势四：显式句柄 × MetaSkill Token 经济

  * 跨调用状态通过显式句柄传递（如 `browser_id`）
  * 每个句柄在 TokenHub 中可以被追踪、计费、审计
  * **结果** ：状态不再是黑盒，而是可治理、可计量的业务资产



#### 优势五：JSON Schema 2020-12 × DDI Registry

  * 工具输入输出使用完整的 JSON Schema 2020-12
  * DDI Registry 可以注册、版本化、治理这些 Schema
  * **结果** ：工具契约从"代码里的注释"变成"注册中心里的治理对象"



## 四、结语：协议变小，生态变大

MCP 第五版做了一件很"Unix 哲学"的事：**把核心协议做得尽可能小，把扩展能力做得尽可能标准** 。

  * 核心协议只关心"如何调用工具"
  * MCP Apps 关心"如何渲染界面"
  * Tasks 关心"如何管理长任务"
  * OAuth/OIDC 关心"如何企业接入"
  * OpenTelemetry 关心"如何观测链路"



当单个 MCP Server 变成"迷你 SaaS"时，OpenClaw.NET 的价值不是再做一个 SaaS，而是成为**SaaS 之间的编排层** ：

  * **Gateway** 负责无状态路由与协议翻译
  * **MetaSkill** 负责工具编排与状态传递
  * **TokenHub** 负责计量与审计
  * **Harness** 负责异步任务与中断恢复
  * **OpenSandbox** 负责安全界面渲染
  * **DDI Registry** 负责契约治理



这大概是 2026 年 Agent 基础设施领域最值得关注的架构方向之一。

* * *

_本文基于 MCP 2026-07-28 第五版规范与 OpenClaw.NET PR #196 技术细节整理。_  
_规范原文请以[MCP 官方文档](<https://modelcontextprotocol.io>) 为准。_


---
> 原文链接: https://www.cnblogs.com/shanyou/p/22144007