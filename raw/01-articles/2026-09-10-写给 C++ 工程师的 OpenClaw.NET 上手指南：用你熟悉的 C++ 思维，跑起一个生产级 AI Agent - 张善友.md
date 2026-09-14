---
title: "写给 C++ 工程师的 OpenClaw.NET 上手指南：用你熟悉的 C++ 思维，跑起一个生产级 AI Agent - 张善友"
source: "博客园"
url: "https://www.cnblogs.com/shanyou/p/22851086"
date: "2026-09-10T13:38:00Z"
score: 1.0
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 写给 C++ 工程师的 OpenClaw.NET 上手指南：用你熟悉的 C++ 思维，跑起一个生产级 AI Agent - 张善友

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/shanyou/p/22851086  
> **抓取日期**: 2026-09-10  
> **相关性评分**: 1.0

> 编译出单文件原生二进制、没有头文件、async 不用手写状态机、内存安全但不用和借用检查器格斗——一个 C++ 工程师视角下的 .NET AI Agent 运行时。  
>  ![1](https://img2024.cnblogs.com/blog/510/202609/510-20260905070811424-1837144874.jpg)

## 为什么写这篇

如果你是 C++ 工程师，你的世界观大概是：**产物必须是原生机器码、资源生命周期必须确定、抽象不该有隐藏开销** 。Agent 框架的主流世界是 Python / Node——解释执行、运行时依赖一堆、性能随运气——你大概率看不上。

**OpenClaw.NET 值得你多看一眼** ：一个用 .NET 写的自托管 AI Agent 运行时 + 网关，鉴权、策略、记忆、可观测性、多渠道接入全部内置，关键是能用 NativeAOT 编译成**无依赖单文件原生二进制** ——启动即原生码，没有 JIT 预热，没有运行时安装。它已经开源，仓库在 [github.com/clawdotnet/openclaw.net](<https://github.com/clawdotnet/openclaw.net>)。

用一句 C++ 话说：

> **它像一个「基于 boost.asio + REST 端点的常驻服务」——对外是 HTTP / WebSocket / 各 IM 的 webhook，对内跑着一个能调工具、读写记忆、跨渠道对话的 AI Agent——只不过协程不用你手写 promise_type，内存不用你管 new/delete。**

本文全程用 C++ 概念做类比。读完你能：看懂系统组成和消息流转、在本地把它跑起来、并写出你的第一个工具 / 技能 / 插件 / 渠道。

* * *

## 一、30 秒认识 OpenClaw.NET

能力 | 说明  
---|---  
网关 | HTTP / WebSocket / 浏览器 UI（`/chat`）/ 各 IM webhook / OpenAI 兼容端点（`/v1/*`）/ MCP（`/mcp`）  
Agent 运行时 | 推理循环、工具执行、记忆、会话、技能、策略、审批、断路器  
渠道 | WebSocket、TG、Slack、Discord、Teams、WhatsApp，以及**飞书 / 钉钉 / 企业微信**  
扩展点 | 工具（Tool）、技能（Skill）、插件（Plugin）、渠道（Channel）、LLM Provider  
客户端 | 浏览器 UI、CLI、Avalonia 桌面 App、Blazor WASM 运维面板、TUI  
  
> 项目已开源：<https://github.com/clawdotnet/openclaw.net>。仓库里解决方案叫 `OpenClaw.Net.slnx`，命名空间是 `OpenClaw.*`——和名字对得上，找代码不迷路。

* * *

## 二、C++ → C# 心智模型速查

这是全文最该先读的部分。看懂这张表，后面 90% 的代码你都能读：

你在 C++ 里熟悉的 | .NET 里的对应物  
---|---  
编译出原生二进制 | **NativeAOT** ——同款产物；默认还有 JIT 模式  
CMake / Make + vcpkg / conan | `dotnet` CLI + MSBuild（`.csproj`）+ NuGet  
头文件 + 声明/定义分离 | **没有头文件** ——一份代码，编译器自己处理  
模板（编译期展开） | 泛型（运行时具体化）+ `where T : ...` 约束（≈ concepts 青春版）  
`std::async` / C++20 协程 `co_await` | `Task<T>` \+ `async`/`await`——**语言内置，不用手写 promise_type**  
`std::stop_token`（C++20） | `CancellationToken`——**就是同一个东西**  
`std::optional<T>` | `string?` vs `string`——**非空默认，可空显式标注**  
`struct` / `class`（都在栈上或你管堆） | `struct` = 值类型 / `class` = 堆上引用类型——**这个区分 C# 保留了**  
`std::unique_ptr` / `shared_ptr` | **不需要** ——GC 接管，引用语义 ≈ 万物 `shared_ptr`  
**RAII** （析构函数确定性释放） | `IDisposable` \+ `using` 关键差异，见下  
虚函数 / 抽象基类 | interface + `virtual`/`override`（接口必须显式声明实现）  
异常 + RAII 回滚 | 异常 + `try`/`catch`/`finally`——模型几乎一样  
boost.asio 的 io_context | async runtime 内置，无感  
未定义行为（UB） | **内存安全** ——越界、悬垂引用编译期/运行期拦死  
Google Test / Catch2 + gmock | xUnit v3 + NSubstitute  
`#define` / 预处理器 | 基本没有预处理宏（条件编译仅限少数场景）  
`constexpr` | `const` / `static readonly`  
  
### 语法上最容易愣住的三个点
    
    
    // 1) 异步：≈ C++20 协程，但编译器把所有状态机细节都包了
    public async Task<string> RunAsync(Session session, string msg, CancellationToken ct)
    {
        var result = await _llm.CallAsync(msg, ct);   // ≈ co_await llm->Call(msg)
        return result.Text;
    }
    // CancellationToken ≈ std::stop_token：协作式取消，显式传参，务必往下传。
    
    // 2) record + required：≈ 聚合初始化 + 编译期必填，带值相等语义（≈ 默认生成了 operator==）
    public sealed record OutboundMessage
    {
        public required string ChannelId { get; init; }   // 不给就编译不过
        public required string RecipientId { get; init; }
    }
    
    // 3) 可空引用类型：string? 可空，string 不可空——≈ std::optional<std::string> vs std::string
    string? maybe = GetOrNull();
    string sure = maybe;                // ⚠ 编译警告——本项目警告即错误（≈ -Werror）
    string sure2 = maybe ?? "default";  // ?? ≈ maybe.value_or("default")
    

### 最大的思维转换：RAII → GC + using

这是 C++ 工程师最需要重建的习惯。C# 是 GC 语言：**对象内存的回收时机不确定** ，析构函数（终结器）什么时候跑、跑不跑都不保证——RAII 里「离开作用域即释放」的直觉在这里对**内存** 不成立。

但对**非内存资源** （文件句柄、socket、锁），C# 给了显式机制：
    
    
    using var doc = JsonDocument.Parse(json);   // ≈ 栈对象，离开作用域确定性 Dispose
    // 异步版本：await using var stream = ...;  ≈ co_await 风格的确定性清理
    

心智模型这样切换：**内存交给 GC（你不用管），资源交给`using`（你必须管）**。看到实现了 `IDisposable` 的类型，就像看到管理着 fd/handle 的 RAII 类——必须包 `using`。

### 性能纪律还在，只是换了位置

GC 不等于放弃性能意识。本项目的写法你会眼熟：`ValueTask`（避免堆分配的轻量 future）、`Span<T>`（≈ `std::string_view`，零拷贝切片）、`ArrayPool`（≈ 自己维护 freelist）。热路径上的分配纪律依然靠人——只是编译器不逼你。

### NativeAOT 与裁剪：你的主场

「禁运行时反射、序列化走编译期代码生成」——C++ 工程师表示：**RTTI 我都经常关，这算什么约束** 。

本项目开激进裁剪（`TrimMode=link`），裁剪器会删掉"看起来没人引用"的代码，所以 JSON 序列化用**源生成器** ——为类型声明 `JsonSerializerContext`，编译期生成序列化代码：
    
    
    [JsonSerializable(typeof(ProblemDetails))]
    [JsonSerializable(typeof(OperatorAccountService.StoreState))]
    internal partial class GatewayJsonContext : JsonSerializerContext;
    

这就是「编译期生成 vs 运行期内省」的老对立面，你一直站编译期这边。你新增 DTO 时，记得挂到某个 `JsonSerializerContext` 上。

裁剪还引出贯穿全文的**两条运行时车道** ：

  * **`aot` 车道**：裁剪安全、低内存、无动态加载——≈ 静态链接的 release 构建，生产 Docker 镜像走这条。
  * **`jit` 车道**：完整 .NET，JIT 编译 + 支持运行时加载 DLL 插件——开发期默认走这条，≈ 支持 `dlopen` 插件的调试构建。



* * *

## 三、一条消息的一生

这是理解整个系统的主线。中枢是 `OpenClaw.Gateway`——它在启动时把 Agent 运行时、消息管道、渠道适配器、插件宿主组合起来，统一路由所有流量。

一条用户消息从进来到回复，共 11 步（C++ 类比已标注）：

  1. **渠道收消息** ：`IChannelAdapter` 把入站消息写进 `MessagePipeline`——≈ 一个有界的生产者-消费者队列
  2. **Worker 取消息** ：1~4 个 worker（上限 = CPU 核数）从队列读——≈ 你起 `std::thread` 池抢任务
  3. **会话加锁** ：拿该会话的 `SemaphoreSlim`（≈ `std::counting_semaphore<1>`），同一会话不并发跑两轮
  4. **过中间件** ：限流、token 预算，可短路拒绝——≈ 请求处理管线上的拦截器链
  5. **进 Agent 运行时** ：`MafAgentRuntime.RunAsync(...)`
  6. **准备上下文** ：载入/新建会话、裁剪历史、注入记忆召回
  7. **ReAct 循环** ：调 LLM → 要工具就执行 → 结果回灌 → 再调 LLM……直到产出文本
  8. **工具执行** ：一条完整链路——预设过滤 → 治理策略 → Hook → 人工审批 → 执行 → 审计
  9. **韧性** ：LLM 调用自带指数退避重试、超时、断路器、降级模型级联
  10. **落库** ：会话写入 `IMemoryStore`（dev 默认 sqlite）
  11. **回复出站** ：按 `ChannelId` 找到渠道适配器投递



整个系统的「骨架接口」都在 `src/OpenClaw.Core/Abstractions/`：`ITool`、`IChannelAdapter`、`IAgentRuntime`、`IMemoryStore`、`IToolHook`……**看懂它们 = 看懂系统的全部可扩展面** 。扩展方式就是「实现接口（≈ 继承抽象基类、重写纯虚函数）+ 注册进 DI 容器（≈ 一个类型安全的工厂注册表）」。

* * *

## 四、把它跑起来

**前置** ：.NET 10 SDK（必须，≈ 装一次编译器 toolchain）、可选 Node.js 20+（仅跑 TS/JS 插件时需要）、一个 LLM API Key。
    
    
    # 先校验配置（≈ 启动前自检）
    dotnet run --project src/OpenClaw.Gateway -c Release -- --doctor
    
    # 启动（≈ cmake --build --config Release && ./openclaw）
    dotnet run --project src/OpenClaw.Gateway -c Release
    

默认监听 `http://127.0.0.1:18789`，浏览器打开 `/chat` 即可对话。

最快的本地启动（三个环境变量 + 一条命令）：
    
    
    export MODEL_PROVIDER_KEY="sk-..."          # 你的 LLM key
    export OPENCLAW_WORKSPACE="$PWD/workspace"  # 工作区根目录
    mkdir -p "$OPENCLAW_WORKSPACE"
    dotnet run --project src/OpenClaw.Gateway -c Release
    

配置体系是「配置文件 + 环境变量覆盖」的分层套路：环境变量用双下划线映射层级，`OpenClaw__Runtime__Mode` ↔ 配置树 `OpenClaw:Runtime:Mode`。敏感字段支持 `env:VAR_NAME` 引用写法，生产环境推荐——不用自己写 getenv 解析层。

**本地避坑速查** ：

  * 必须 .NET 10，多 SDK 并存时用 `global.json` 钉版本（≈ `toolchain file` 指定编译器版本）
  * 出厂 `appsettings.json` 里的默认 `AuthToken` 和示例 API key **仅供本地回环** ，对外部署务必改成 `env:` 引用，别把真实密钥提交进仓库
  * 公网绑定会被安全硬化拦截（缺鉴权 token、危险工具、`raw:` 密钥都会拒绝启动）——这是有意设计



* * *

## 五、动手扩展：四种方式，从轻到重

### ① 写一个工具（Tool）—— 最常用

一个工具就是一个实现 `ITool` 的类。C++ 视角：**就是继承抽象基类、重写纯虚函数** ——C# 接口同样需要显式声明实现：
    
    
    public interface ITool   // ≈ class ITool { 全是纯虚函数 };
    {
        string Name { get; }              // LLM 用它来调用
        string Description { get; }       // 决定 LLM 何时调用它
        string ParameterSchema { get; }   // 参数的 JSON Schema
        ValueTask<string> ExecuteAsync(string argumentsJson, CancellationToken ct);
    }
    

最小可用示例（字符串反转工具）：
    
    
    public sealed class ReverseTextTool : ITool   // ≈ class ReverseTextTool : public ITool
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
            // 用 JsonDocument 解析入参（AOT 安全）≈ 手写 JSON DOM 解析，不走反射
            using var doc = JsonDocument.Parse(argumentsJson);   // using ≈ RAII，确定性 Dispose
            var text = doc.RootElement.GetProperty("text").GetString() ?? "";
            return new ValueTask<string>(new string(text.Reverse().ToArray()));
        }
    }
    

然后把它加进内置工具列表（`CreateBuiltInTools(...)`，≈ 你在 main 里集中构造并 `push_back` 进 `std::vector<std::unique_ptr<ITool>>` 的那一段），重启网关，对它说「reverse the text hello」——工具调用会经过完整的审计/治理/审批链路。

### ② 写一个技能（Skill）—— 最轻，纯 Markdown

技能**不是代码** ，而是一份「给 Agent 的操作手册」：教 Agent 遇到某类任务怎么组合调用已有工具。

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
    

重启（或开热加载）即生效。

### ③ 写一个插件（Plugin）—— 打包一组能力

两条路：**原生 .NET 动态插件** （进程内 DLL 加载，仅 jit 车道）和 **JS/TS 桥接插件** （Node.js 子进程 + JSON-RPC，两条车道都行）。

这个取舍你闭着眼都懂：≈ **`dlopen` 加载 .so 进进程 vs 起子进程走 IPC**。前者零调用开销但 ABI/生命周期/崩溃隔离全是坑、且只能在 jit 车道用；后者有 IPC 成本但进程隔离、语言自由、崩了不拖垮宿主。原生契约仅 45 行：
    
    
    public sealed class MyPlugin : INativeDynamicPlugin
    {
        public void Register(INativeDynamicPluginContext context)
        {
            context.RegisterTool(new ReverseTextTool());
            // 还能 RegisterChannel / RegisterHook / RegisterProvider ...
        }
    }
    

生产环境（aot 车道）要跑自定义逻辑，走 TS 桥接插件。

### ④ 接一个渠道（Channel）—— 接你自己的 IM

契约是 `IChannelAdapter`（收 + 发），入站走「webhook → handler 校验解析 → 管道入队」，出站按 `ChannelId` 路由投递。照抄 Twilio SMS 的实现（最简单的参照）即可，6 步：配置类 → 适配器 → webhook handler → DI 注册 → 挂适配器 → 映射端点。

webhook handler 的核心形态：
    
    
    // 验签 → 解析 → 白名单 → 入队，和你写的任何 webhook endpoint 一个结构
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
    

> 每个渠道都该有的安全面：签名校验（恒定时间比较，防时序侧信道）、发送者白名单、体积上限、去重窗口。

### 选型一图流

你的需求 | 用 | 要编译吗  
---|---|---  
加一个 Agent 能调用的动作 | **工具** | 要  
教 Agent 某类任务的处理流程 | **技能** | 不要（纯 md）  
打包一组能力 / 复用 TS 生态 | **插件** | 原生要 / 桥不要  
接一个新的消息入口 | **渠道** | 要  
  
* * *

## 六、开发约定：三个必须知道的红线

  1. **警告即错误** （`TreatWarningsAsErrors=true`）+ 可空性强制——≈ `-Wall -Wextra -Werror` 全开。第一次写会被编译器频繁拦，但它挡掉的就是你在 code review 里最不想看到的那类空指针路径。
  2. **JSON 必须走源生成器** ——对你而言这叫「编译期代码生成」，老朋友了。
  3. **数据安全铁律** ：记忆/会话默认落 `./memory/`，严禁用「清空整库 / DROP / 删目录」做测试隔离——只删自己创建的数据，或用独立的 throwaway 路径。



测试栈是 xUnit v3 + NSubstitute（≈ Google Test + gmock）：
    
    
    dotnet test                                                # 全部（≈ ctest）
    dotnet test --filter "FullyQualifiedName~ProcessToolTests" # 单类（≈ gtest_filter）
    

* * *

## 写在最后

对 C++ 工程师来说，这套系统的读感大概是「熟悉中带着一丝轻松」：**单文件原生二进制、非空默认、显式接口实现、编译期代码生成、确定性的`using` 资源管理、警告即错误**——你在乎的工程纪律都在。

真正要适应的只有两件事：**内存从 RAII 换成 GC** （确定性析构变成了 `using` 显式管理非内存资源），以及**模板换成带约束的泛型** （编译期元编程的火力弱了，但编译速度快得不像话）。你失去一部分对内存的绝对控制，换来的是没有 UB、没有头文件、async 不用手写状态机——值不值，写两个工具你自有判断。

想继续深挖，最可靠的三个源码入口：

  1. `src/OpenClaw.Gateway/Program.cs` —— 启动主线（≈ 你的 `main.cpp`）
  2. `src/OpenClaw.Agent/MafAgentRuntime.cs` —— Agent 循环本体
  3. `src/OpenClaw.Core/Abstractions/` —— 所有可扩展接口（≈ 项目里那堆抽象基类的头文件）



> 本文所有代码与结论均对照开源仓库 [clawdotnet/openclaw.net](<https://github.com/clawdotnet/openclaw.net>) 当前源码（运行时 = MAF + jit）。如果你发现与代码不符——以代码为准，也欢迎提 PR。

**觉得有用，欢迎去 GitHub 点个 Star ⭐，也欢迎点赞 / 在看 / 转发给你的 C++ 朋友 👋**


---
> 原文链接: https://www.cnblogs.com/shanyou/p/22851086