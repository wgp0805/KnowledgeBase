---
title: "写给 TypeScript 工程师的 OpenClaw.NET 上手指南：用你熟悉的 TS 思维，跑起一个生产级 AI Agent - 张善友"
source: "博客园"
url: "https://www.cnblogs.com/shanyou/p/22850478"
date: "2026-09-05T13:17:00Z"
score: 1.0
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 写给 TypeScript 工程师的 OpenClaw.NET 上手指南：用你熟悉的 TS 思维，跑起一个生产级 AI Agent - 张善友

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/shanyou/p/22850478  
> **抓取日期**: 2026-09-05  
> **相关性评分**: 1.0

> 一个自带 Node.js 插件桥的 .NET AI Agent 运行时——内核是编译型语言的性能与部署形态，扩展层你可以继续写 TypeScript。

![1](assets/2026-09-05-%E5%86%99%E7%BB%99%20TypeScript%20%E5%B7%A5%E7%A8%8B%E5%B8%88%E7%9A%84%20OpenClaw.NET%20%E4%B8%8A%E6%89%8B%E6%8C%87%E5%8D%97%EF%BC%9A%E7%94%A8%E4%BD%A0%E7%86%9F%E6%82%89%E7%9A%84%20TS%20%E6%80%9D%E7%BB%B4%EF%BC%8C%E8%B7%91%E8%B5%B7%E4%B8%80%E4%B8%AA%E7%94%9F%E4%BA%A7%E7%BA%A7%20AI%20Agent%20-%20%E5%BC%A0%E5%96%84%E5%8F%8B/1e9a10fabe52a96a7f99dbb8975c4073_MD5.jpg)

## 为什么写这篇

如果你是 TypeScript 工程师，你的日常大概率是 Node.js 后端 + 各种 Agent SDK。Agent 生态确实是 Python / Node 优先，但你应该也体会过 Node 在**生产化** 上的隐痛：部署要带运行时、进程模型单线程、长期驻留服务的内存与可观测性要靠自己攒。

**OpenClaw.NET 给了一个有趣的组合** ：内核用 .NET 写成——自托管 AI Agent 运行时 + 网关，鉴权、策略、记忆、可观测性、多渠道接入全部内置，还能用 NativeAOT 编译成**一个无依赖的单文件原生二进制** ；而扩展层它**内置了一个 Node.js 插件桥（JSON-RPC over stdio/socket）** ——意味着你可以**直接用 TypeScript 写插件** ，复用上游 OpenClaw 的整个 TS/JS 插件生态。它已经开源，仓库在 [github.com/clawdotnet/openclaw.net](<https://github.com/clawdotnet/openclaw.net>)。

用一句 TS 话说：

> **它像一个「Hono/Fastify 应用」——对外是 HTTP / WebSocket / 各 IM 的 webhook，对内跑着一个能调工具、读写记忆、跨渠道对话的 AI Agent——只不过网关本体编译成了一个二进制，而你的插件还是一个普通的 Node 进程。**

本文全程用 TypeScript 概念做类比。读完你能：看懂系统组成和消息流转、在本地把它跑起来、并写出你的第一个工具 / 技能 / 插件 / 渠道。

* * *

## 一、30 秒认识 OpenClaw.NET

能力 | 说明  
---|---  
网关 | HTTP / WebSocket / 浏览器 UI（`/chat`）/ 各 IM webhook / OpenAI 兼容端点（`/v1/*`）/ MCP（`/mcp`）  
Agent 运行时 | 推理循环、工具执行、记忆、会话、技能、策略、审批、断路器  
渠道 | WebSocket、TG、Slack、Discord、Teams、WhatsApp，以及**飞书 / 钉钉 / 企业微信**  
扩展点 | 工具（Tool）、技能（Skill）、插件（Plugin，**含 TS 桥** ）、渠道（Channel）、LLM Provider  
客户端 | 浏览器 UI、CLI、Avalonia 桌面 App、Blazor WASM 运维面板、TUI  
  
> 项目已开源：<https://github.com/clawdotnet/openclaw.net>。仓库里解决方案叫 `OpenClaw.Net.slnx`，命名空间是 `OpenClaw.*`——和名字对得上，找代码不迷路。

* * *

## 二、TypeScript → C# 心智模型速查

这是全文最该先读的部分。好消息：TS 和 C# 是「远房亲戚」（背后都有 Anders Hejlsberg），语法亲缘度极高。看懂这张表，后面 90% 的代码你都能读：

你在 TS 里熟悉的 | .NET 里的对应物  
---|---  
`Promise<T>` \+ `async`/`await` | `Task<T>` \+ `async`/`await`——**几乎逐字对应**  
`AbortController` / `AbortSignal` | `CancellationToken`（方法最后一个参数）——**就是同一个模式**  
npm / pnpm + `package.json` | `dotnet` CLI + `.csproj` \+ NuGet  
`tsconfig.json`（公共配置继承） | `Directory.Build.props`（解决方案级公共配置）  
Hono / Fastify / NestJS | ASP.NET Core（Minimal API 风格，路由写法神似 Hono）  
NestJS DI / tsyringe / InversifyJS | `Microsoft.Extensions.DependencyInjection`（内置 DI 容器）  
`interface`（**结构化类型** ，形状对就行） | C# interface（**具名类型** ，必须显式声明）关键差异  
`string | null` \+ `strictNullChecks` | `string?` \+ 可空引用类型——**严格程度一个级别**  
`JSON.parse` / `JSON.stringify`（任何对象直接转） | `System.Text.Json` \+ **源生成器（编译期）** 关键差异  
zod / io-ts（运行时校验） | JSON Schema（工具参数声明）  
`AsyncIterable<T>` / `ReadableStream` | `IAsyncEnumerable<T>` \+ `await foreach`（流式 token 就靠它）  
`EventEmitter` | `event Func<...>`（事件订阅）  
`using` 声明（TS 5.2+）/ `Disposable` | `using` / `await using`——C# 是这特性的原产地  
vitest / jest + sinon | xUnit v3 + NSubstitute  
`bun build --compile` / `deno compile` | **NativeAOT** ——同样的单文件二进制产物  
  
### 语法上最容易愣住的三个点
    
    
    // 1) 异步：和 TS 几乎逐字对应
    public async Task<string> RunAsync(Session session, string msg, CancellationToken ct)
    {
        var result = await _llm.CallAsync(msg, ct);   // ≈ await llm.call(msg)
        return result.Text;
    }
    // CancellationToken ≈ AbortSignal：你把 signal 一路传进 fetch 的习惯，原样搬过来——
    // 这里每个异步方法尾参都挂着 ct，务必往下传。
    
    // 2) record + required：≈ TS 的 interface + 必填字段，但校验发生在编译期且有值相等语义
    public sealed record OutboundMessage
    {
        public required string ChannelId { get; init; }   // 不给就编译不过
        public required string RecipientId { get; init; }
    }
    
    // 3) 可空引用类型：string? 可空，string 不可空
    // ≈ strictNullChecks 永远开着、且没有 any 逃生舱的世界
    string? maybe = GetOrNull();
    string sure = maybe;                // ⚠ 编译警告——本项目警告即错误！
    string sure2 = maybe ?? "default";  // ?? 和 TS 的空值合并运算符一模一样
    

### 最大的思维差异：结构化类型 → 具名类型

TS 里「形状对就是同一类型」——对象字面量只要有 `name` 和 `execute` 方法，就能当 `Tool` 用。**C# 不是这样** ：接口必须显式声明 `class MyTool : ITool`，类型关系靠「声明」而非「形状」。

所以要扩展，就是「声明实现某个接口 + 注册进 DI」——比 TS 多一句声明，换来的是编译器全程盯着你，重构时安全感极强。

### 依赖注入：≈ 内置版的 NestJS DI，但没有装饰器魔法
    
    
    // 注册（≈ @Injectable() + providers 数组）
    services.AddSingleton<IMemoryStore, FileMemoryStore>();
    
    // 解析（≈ 构造器注入后直接用）
    var store = sp.GetRequiredService<IMemoryStore>();
    

本项目几乎全是单例（Singleton），注册按职责拆成一堆扩展方法，在 `Program.cs` 里顺序调用——结构上和 NestJS 的 module providers 一样，只是没有装饰器，全是显式函数调用。

### 一个绕不开的硬约束：NativeAOT 与裁剪

先说好消息：**单文件二进制对 TS 工程师不陌生** ——`bun build --compile`、`deno compile` 干的就是这事。NativeAOT 是 .NET 版的同款：无运行时依赖、毫秒级冷启动。

但代价要清楚。本项目开了激进裁剪（`TrimMode=link`），后果是：

  * **不能用运行时反射** 。TS 里 `JSON.parse(JSON.stringify(obj))` 随便转、`Object.keys()` 动态遍历、装饰器元数据运行时读取——这些「运行时内省」玩法在 aot 车道都不行，裁剪器会把"看起来没人引用"的代码删掉。
  * **JSON 序列化用源生成器** ：为类型声明 `JsonSerializerContext`，编译期生成序列化代码：


    
    
    [JsonSerializable(typeof(ProblemDetails))]
    [JsonSerializable(typeof(OperatorAccountService.StoreState))]
    internal partial class GatewayJsonContext : JsonSerializerContext;
    

TS 视角：相当于强制你所有序列化都走「编译期生成 schema」的路线（类似 typia 的 transform 模式），而不是 `JSON.stringify` 那种运行时反射——更快，且裁剪安全。你新增 DTO 时，记得挂到某个 `JsonSerializerContext` 上。

裁剪还引出贯穿全文的**两条运行时车道** ：

  * **`aot` 车道**：裁剪安全、低内存、无动态加载。生产 Docker 镜像走这条。
  * **`jit` 车道**：完整 .NET，支持反射和进程内动态加载 .NET 插件——开发期默认走这条。
  * **注意：TS 插件走独立的 Node.js 子进程，两条车道都支持** ——这是给 TS 工程师的后门，见第五节。



* * *

## 三、一条消息的一生

这是理解整个系统的主线。中枢是 `OpenClaw.Gateway`——它在启动时把 Agent 运行时、消息管道、渠道适配器、插件宿主组合起来，统一路由所有流量。

一条用户消息从进来到回复，共 11 步（TS 类比已标注）：

  1. **渠道收消息** ：`IChannelAdapter` 把入站消息写进 `MessagePipeline`——≈ 一个有界的异步队列
  2. **Worker 取消息** ：1~4 个 worker（上限 = CPU 核数）从队列读——注意，**这是真·多线程并行，不是 Node 的单线程事件循环**
  3. **会话加锁** ：拿该会话的 `SemaphoreSlim`（≈ 容量为 1 的 async mutex），同一会话不并发跑两轮
  4. **过中间件** ：限流、token 预算，可短路拒绝——≈ Hono/Express 的 middleware 链
  5. **进 Agent 运行时** ：`MafAgentRuntime.RunAsync(...)`
  6. **准备上下文** ：载入/新建会话、裁剪历史、注入记忆召回
  7. **ReAct 循环** ：调 LLM → 要工具就执行 → 结果回灌 → 再调 LLM……直到产出文本
  8. **工具执行** ：一条完整链路——预设过滤 → 治理策略 → Hook → 人工审批 → 执行 → 审计
  9. **韧性** ：LLM 调用自带指数退避重试、超时、断路器、降级模型级联
  10. **落库** ：会话写入 `IMemoryStore`（dev 默认 sqlite）
  11. **回复出站** ：按 `ChannelId` 找到渠道适配器投递



整个系统的「骨架接口」都在 `src/OpenClaw.Core/Abstractions/`：`ITool`、`IChannelAdapter`、`IAgentRuntime`、`IMemoryStore`、`IToolHook`……**看懂它们 = 看懂系统的全部可扩展面** 。

* * *

## 四、把它跑起来

**前置** ：.NET 10 SDK（必须，≈ 装一次 Node 运行时）、**Node.js 20+** （跑 TS 桥接插件时需要——对你来说应该早就装好了）、一个 LLM API Key。
    
    
    # 先校验配置（≈ 启动前自检）
    dotnet run --project src/OpenClaw.Gateway -c Release -- --doctor
    
    # 启动（≈ tsx watch src/index.ts，但自带编译）
    dotnet run --project src/OpenClaw.Gateway -c Release
    

默认监听 `http://127.0.0.1:18789`，浏览器打开 `/chat` 即可对话。

最快的本地启动（三个环境变量 + 一条命令）：
    
    
    export MODEL_PROVIDER_KEY="sk-..."          # 你的 LLM key
    export OPENCLAW_WORKSPACE="$PWD/workspace"  # 工作区根目录
    mkdir -p "$OPENCLAW_WORKSPACE"
    dotnet run --project src/OpenClaw.Gateway -c Release
    

配置体系和 Node 服务常见的「配置文件 + 环境变量覆盖」一个套路：环境变量用双下划线映射层级，`OpenClaw__Runtime__Mode` ↔ 配置树 `OpenClaw:Runtime:Mode`——≈ `config` 库或 dotenv 的分层覆盖思路。敏感字段支持 `env:VAR_NAME` 引用写法，生产环境推荐。

**本地避坑速查** ：

  * 必须 .NET 10，多 SDK 并存时用 `global.json` 钉版本（≈ `.nvmrc` / `package.json` 的 `engines` 字段）
  * 出厂 `appsettings.json` 里的默认 `AuthToken` 和示例 API key **仅供本地回环** ，对外部署务必改成 `env:` 引用，别把真实密钥提交进仓库
  * 公网绑定会被安全硬化拦截（缺鉴权 token、危险工具、`raw:` 密钥都会拒绝启动）——这是有意设计



* * *

## 五、动手扩展：四种方式，从轻到重

### ① 写一个工具（Tool）—— 最常用

一个工具就是一个实现 `ITool` 的类。TS 视角：**就是你定义一个`Tool` interface 然后实现它**，只不过 C# 要显式声明：
    
    
    public interface ITool
    {
        string Name { get; }              // LLM 用它来调用
        string Description { get; }       // 决定 LLM 何时调用它
        string ParameterSchema { get; }   // 参数的 JSON Schema
        ValueTask<string> ExecuteAsync(string argumentsJson, CancellationToken ct);
    }
    

最小可用示例（字符串反转工具）：
    
    
    public sealed class ReverseTextTool : ITool   // ← 显式声明实现（具名类型，不是形状匹配）
    {
        public string Name => "reverse_text";
        public string Description =>
            "Reverse the characters of the given text.";
    
        public string ParameterSchema => """
        {
          "type": "object",
          "properties": {
            "text": { "type": "string", "description": "Text to reverse" }
          },
          "required": ["text"]
        }
        """;
    
        public ValueTask<string> ExecuteAsync(string argumentsJson, CancellationToken ct)
        {
            // 用 JsonDocument 解析入参（AOT 安全）≈ JSON.parse 后手动取字段
            using var doc = JsonDocument.Parse(argumentsJson);
            var text = doc.RootElement.GetProperty("text").GetString() ?? "";
            return new ValueTask<string>(new string(text.Reverse().ToArray()));
        }
    }
    

然后把它加进内置工具列表（`CreateBuiltInTools(...)`，就是个集中组装的工厂函数），重启网关，对它说「reverse the text hello」——工具调用会经过完整的审计/治理/审批链路。

### ② 写一个技能（Skill）—— 最轻，纯 Markdown

技能**不是代码** ，而是一份「给 Agent 的操作手册」。TS 视角：**工具 = 你写的 tool 函数，技能 = 一段精心设计的 system prompt** ，教 Agent 遇到某类任务怎么组合调用已有工具。

机制是**渐进式披露** ：系统提示里只放技能索引（省 token）→ Agent 判断相关时拉取完整正文 → 需要时再读附属文件。

创建只需一个文件夹 + 一个 `SKILL.md`，零编译：
    
    
    ---
    name: pr-reviewer
    description: 当用户要求审查一个 Pull Request 或 diff 时使用。
    ---
    
    ## 步骤
    1. 用 `read_file` 或 `shell`（git diff）拿到改动
    2. 按正确性、边界、安全、可读性审查
    3. 输出分级意见：🔴 必须改 / 🟡 建议 / 🟢 可选
    

重启（或开热加载）即生效——体验接近 nodemon，连编译都省了。

### ③ 写一个插件（Plugin）—— TS 工程师的主场 ⭐

两条路：**原生 .NET 动态插件** （进程内 DLL 加载，仅 jit 车道）和 **JS/TS 桥接插件** （Node.js 子进程 + JSON-RPC，**两条车道都行** ）。

对 TS 工程师，重点是后者——**这是你的主场** ：

  * 网关在运行时拉起一个 **Node.js 子进程** （`plugin-bridge.mjs`），通过 stdio/socket 上的 **JSON-RPC** 通信
  * 你的插件就是一个普通 Node 包，**用 TypeScript 写，完全不用碰 C#**
  * **不受 aot/jit 车道限制** （进程隔离天然免疫裁剪问题），生产镜像也能跑
  * 可直接复用上游 OpenClaw 的整个 TS/JS 插件生态



开启方式：
    
    
    "OpenClaw": {
      "Plugins": {
        "Enabled": true,
        "Load": { "Paths": ["./my-ts-plugins"] }   // 指向你的插件目录
      }
    }
    

架构取舍你一眼就能看懂：≈ VS Code 的 Extension Host 模型——内核进程保证稳定，扩展跑在独立 Node 进程里，崩了不拖垮主进程。**如果要在生产环境（aot 车道）跑自定义逻辑，TS 桥接插件是唯一推荐路径。**

当然，如果你想写原生 .NET 插件（契约仅 45 行）也完全欢迎：
    
    
    public sealed class MyPlugin : INativeDynamicPlugin
    {
        public void Register(INativeDynamicPluginContext context)
        {
            context.RegisterTool(new ReverseTextTool());
            // 还能 RegisterChannel / RegisterHook / RegisterProvider ...
        }
    }
    

### ④ 接一个渠道（Channel）—— 接你自己的 IM

契约是 `IChannelAdapter`（收 + 发），入站走「webhook → handler 校验解析 → 管道入队」，出站按 `ChannelId` 路由投递。照抄 Twilio SMS 的实现（最简单的参照）即可，6 步：配置类 → 适配器 → webhook handler → DI 注册 → 挂适配器 → 映射端点。

webhook handler 的核心形态，写 Hono/Fastify 的你一眼熟：
    
    
    // ≈ app.post('/webhook', async (c) => {...})：验签 → 解析 → 白名单 → 入队
    public async ValueTask<WebhookResult> HandleAsync(
        string bodyText, string? signature,
        Func<InboundMessage, CancellationToken, ValueTask> enqueue, CancellationToken ct)
    {
        if (_config.ValidateSignature && !IsValidSignature(bodyText, _secret, signature))
            return WebhookResult.Unauthorized();
        // ... 解析、白名单校验 ...
        await enqueue(new InboundMessage { ChannelId = "myim", SenderId = senderId, Text = text }, ct);
        return WebhookResult.Ok();
    }
    

> 每个渠道都该有的安全面：签名校验（恒定时间比较，≈ Node 的 `crypto.timingSafeEqual`）、发送者白名单、体积上限、去重窗口。

### 选型一图流

你的需求 | 用 | 要编译吗  
---|---|---  
加一个 Agent 能调用的动作 | **工具** | 要  
教 Agent 某类任务的处理流程 | **技能** | 不要（纯 md）  
打包一组能力，**想用 TS 写** | **TS 桥接插件** | 不要（Node 进程）  
打包一组能力，写原生 .NET | **原生插件** | 要（仅 jit）  
接一个新的消息入口 | **渠道** | 要  
  
* * *

## 六、开发约定：三个必须知道的红线

  1. **警告即错误** （`TreatWarningsAsErrors=true`）+ 可空性强制——≈ `strict: true` \+ `noUncheckedIndexedAccess` 全开、CI 上 `tsc --noEmit` 一个 warning 都不许过。第一次写会被编译器频繁拦，但它挡掉的就是你在生产里怕的那类 `Cannot read properties of undefined`。
  2. **JSON 必须走源生成器** ，别指望 `JSON.stringify` 式的运行时反射，否则 AOT 下运行时炸。
  3. **数据安全铁律** ：记忆/会话默认落 `./memory/`，严禁用「清空整库 / DROP / 删目录」做测试隔离——只删自己创建的数据，或用独立的 throwaway 路径（≈ 每个测试用临时目录的 fixture 思路）。



测试栈是 xUnit v3 + NSubstitute（≈ vitest + sinon）：
    
    
    dotnet test                                                # 全部（≈ vitest run）
    dotnet test --filter "FullyQualifiedName~ProcessToolTests" # 单类（≈ vitest -t）
    

* * *

## 写在最后

对 TypeScript 工程师来说，这套系统的亲和力来自两层：

**读代码层** ：TS 和 C# 本来就是「远房亲戚」——`async`/`await`、`??`、接口、泛型、严格空检查，你的心智模型几乎无缝平移。真正要适应的只有两件事：类型是具名而非结构化的（多一句显式声明），以及 NativeAOT 下的「禁反射」约束。

**写扩展层** ：你甚至可以不怎么碰 C#——Node.js 插件桥意味着**你的 TypeScript 插件就是一等公民** ，而且能在生产 aot 车道跑。内核给你 .NET 的性能与单二进制部署，扩展层让你留在最舒服的生态里。

想继续深挖，最可靠的三个源码入口：

  1. `src/OpenClaw.Gateway/Program.cs` —— 启动主线（≈ 你的 `src/index.ts`）
  2. `src/OpenClaw.Agent/MafAgentRuntime.cs` —— Agent 循环本体
  3. `src/OpenClaw.Core/Abstractions/` —— 所有可扩展接口（≈ 项目里的 `types.ts`）



> 本文所有代码与结论均对照开源仓库 [clawdotnet/openclaw.net](<https://github.com/clawdotnet/openclaw.net>) 当前源码（运行时 = MAF + jit）。如果你发现与代码不符——以代码为准，也欢迎提 PR。

**觉得有用，欢迎去 GitHub 点个 Star ⭐，也欢迎点赞 / 在看 / 转发给你的 TS 朋友 👋**


---
> 原文链接: https://www.cnblogs.com/shanyou/p/22850478