---
title: "Claude Code 最新版更新 Mods 能力，致敬 DeepSeek Harness？"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6473496.html"
date: "Sun, 04 Oct 2026 00:26:50 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# Claude Code 最新版更新 Mods 能力，致敬 DeepSeek Harness？

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6473496.html  
> **抓取日期**: 2026-10-04  
> **相关性评分**: 1.0

> Anthropic 在 Claude Code 的 v2.1.287 里加了 Claude Mods：写一段 TypeScript 或 JavaScript 函数，就能挂到事件流上观察、改写或接管工具调用。DeepSeek Harness 走的则是服务接口拼装的路子。

![](https://image.woshipm.com/2024/03/05/8fa330e4-dae2-11ee-840e-00163e142b65.png)

DeepSeek-V4.1-Flash 的最佳 Harness 搭档，我觉得可能是 Claude Code

下载即用的 DeepSeek Harness 桌面客户端，开源！支持 Windows

Anthropic 刚刚发布了 Claude Code 的 v2.1.287 版本，值得关注的新能力 Claude Mods，它允许开发者通过编写小型的 TypeScript 或 JavaScript 函数，改变 Claude Code 的事件逻辑并绘制自定义界面

换言之，开发者可以按自己的流程改造工作台了，哪些地方值得动手、哪些需求用现成 Skills 或 Hooks 就够了

## 01 什么是 Mod：运行在进程内的事件函数

按官方给出的产品定义，Mod 是运行在 Claude Code 进程内部的扩展逻辑，当 Claude Code 运行时，内部会派发各种生命周期事件，挂载在上面的 Mod 可以在事件流中执行三类操作：

  1. **观察（Observe）：** 只读取事件数据并放行，在每次工具调用后记录消耗或者统计轮次
  2. **改写（Rewrite）：** 在数据发给模型或者执行之前动态修改，对敏感路径脱敏，或者把高风险命令参数改写为安全选项
  3. **接管（Answer）：** 直接处理事件并返回结果，跳过 Claude Code 原有的默认逻辑



这种类似中间件管道（Middleware Chain）的处理方式，让开发者可以深入介入 Claude Code 的事件生命周期，并在终端或桌面端绘制界面组件

## 02 四种扩展怎么选：Skills、MCP、Hooks、Mods 各司其职

面对 Skills、MCP、Settings Hooks 和 Mods，很多同学容易混淆它们的使用场景

需要说明的是，这四种机制属于互补协同关系，一个标准的插件包完全可以同时包含指令、外部工具、拦截脚本与模组，我整理了一张清晰的选型对照图：

![Claude Code 四种扩展机制怎么选](https://image.woshipm.com/wp-files/sha256/1e/3e/1e3e4f5a50bd01c0fbbb3299f16933991555062870b57791319d5725c4f39bcd.png)

Claude Code 四种扩展机制怎么选

结合官方文档的对比说明，四者的选择维度大致如下：

  * **Skills（技能）** ：载体为 Markdown（SKILL.md），作用于模型上下文，适合沉淀特定业务排查 SOP、编码规范与多步骤指导，教模型如何理解任务
  * **MCP Servers（模型上下文协议）** ：载体为外部独立进程或网络服务，通过标准协议为 Agent 提供外部工具，适合读写数据库、调用私有云平台接口或连接企业协作系统
  * **Settings Hooks（生命周期钩子）** ：载体为配置在 settings.json中的 Shell 脚本、HTTP 请求或 Prompt，由生命周期事件触发外部运行，适合在工具调用前后进行放行审核或记录外部审计
  * **Mods（模组）** ：载体为进程内事件处理函数，常驻在 Claude Code 运行时内部，适合需要自定义界面组件、重写事件流、跨钩子共享状态或动态调整推理参数的场景



在官方博客和上手教程中，Anthropic 给出了几个具代表性的演示设想与示例

### 场景 1：Token Weather（上下文天气预报）

在处理多文件重构任务时，开发者往往需要关注上下文窗口的消耗，官方教程给出了一个约 80 行代码的轻量 Mod 示例 Token Weather，通过挂载 AbovePrompt组件，在输入框上方实时绘制天气指示条

官方演示截图展示了指示条的变化：

![Token Weather 上下文天气预报界面展示](https://image.woshipm.com/wp-files/sha256/9d/67/9d674fc482d90fb2be7d8a9b066b3384f8c91b9408a8d0d7fca88ffb24ac1a26.png)

Token Weather 上下文天气预报界面展示

官方设定的区间阈值如下：

  * 25% 以下：显示晴天（![☀](https://s.w.org/images/core/emoji/16.0.1/72x72/2600.png) Clear）
  * 25% 至 49%：显示多云（![☁](https://s.w.org/images/core/emoji/16.0.1/72x72/2601.png) Cloudy）
  * 50% 至 74%：显示阵雨（![☂](https://s.w.org/images/core/emoji/16.0.1/72x72/2602.png) Showers）
  * 75% 至 89%：显示暴风雨（☇ Storm）
  * 90% 及以上：提示即将压缩上下文（↯ Compact soon）



在 Claude Code 给出的演示记录中，展示了会话随着多轮读取，读数从 18% 晴天、67% 阵雨逐步上升到 81% 暴风雨的过程

### 场景 2：Blast Radius（危险操作拦截确认）

针对高危变更，Claude Code 设计了名为 Blast Radius 的防护示例，当检测到可能丢失本地修改的命令时，Mod 会在终端上方直接绘制一个带黄色边框的确认框

![Blast Radius 高危指令交互拦截框](https://image.woshipm.com/wp-files/sha256/f1/8e/f18ee895f6415b259c3863c5173bf7b1a7cc641b8b24e45e4edea7b69a2f836e.png)

Blast Radius 高危指令交互拦截框

该组件会列出受影响的文件，并提供带编号的 Proceed 与 Cancel 选项供用户直接选择

### 场景 3：Replay Theater（步骤复盘与差异审查）

在Claude Code 教程展示的另一个进阶示例 Replay Theater 中，Mod 在输入框上方绘制了一个洋红色边框的交互面板

![Replay Theater 步骤审查界面展示](https://image.woshipm.com/wp-files/sha256/49/c9/49c9509dab32bbe50f3958338ab61c3bcd10adbf1f6fddd2002438f33b6188a7.png)

Replay Theater 步骤审查界面展示

该面板包含了步骤编号指示条、单行文件变更对比，以及上一页、下一页和关闭按钮，这是一个独立的教程展示案例，用来演示如何用 Mod 构建分步审查流程，与内置的 /diff属于不同实现

### 场景 4：副代理机制（You should know）

最新版提供了一个内置实验 Mod：cc-plugin-you-should-know

该 Mod 默认处于关闭状态，在支持该特性的组织环境下，且仅限开启了遥测的第一方会话中，用户可通过以下命令尝试启用：

shell

> /plugin enable cc-plugin-you-should-know@builtin

官方设计目标是让一个副代理（Side Agent）在后台观察长任务过程，当发现可能存在的疏漏时，在输入框上方弹出便签提醒

## 03 架构演进信号：部分内置能力向 Mods 迁移

Claude Code 的部分内置能力目前已经以 Mod 形式交付，例如交互式终端里的 /diff面板对应内置的 cc-plugin-diff，加载 AGENTS.md项目指令对应内置的 cc-plugin-agents-md

官方表示，未来计划将更多内置功能逐步迁移为 Mods，使用户可以把 Claude Code 缩减为一个较小的 Core，再按需添加所需要的功能，这意味着官方正在探索将宿主本身解耦的架构路径，但目前仍处于早期演进阶段

## 04 DeepSeek Harness 的一切皆插件

看到 Claude Code 计划把内置能力逐步拆成 Mods，很多关注底层设计的同学很容易联想到 DeepSeek Harness 的一切皆插件设计，把这两套思路放在一起观察，能帮我们看清当前 AI 编程运行时的演变

我扒了 DeepSeek Harness 219 个包，真有价值的是插件内核，附插件推荐

两者的共同特征，是把定制单元从外部提示词或单纯的外部工具挂载，推进到了 Agent 的运行时内部，官方内置功能和扩展共享同一套底层机制，在调用链路上都引入了类似中间件的流水线模式：前一个扩展处理完后调用 next 把控制权交给后续逻辑，或者提前返回直接接管，生命周期与状态管理也成为开发者干预的接缝，这些相似的演化方向反映出大家对运行时灵活性的共同诉求，但两边在技术实现上各自独立，并没有协议兼容或继承关系

两者的核心定位与架构层级存在明显区别，我整理了一张简明对比表：

维度 | DeepSeek Harness（一切皆插件） | Claude Code Mods  
---|---|---  
产品能力怎样装配 | 启动时依据配置与 Profile 组装整棵 Cordis 插件树，由依赖注入驱动服务挂载与卸载 | 随插件包安装至客户端，在会话启动或重载时加载并介入中间件事件链  
默认 Loop 与服务替换范围 | AgentLoop、模型适配与工具注册均以服务契约提供，允许通过配置提供新的 Provider | 宿主引擎保持完整运行，官方正逐步将特定内置能力迁移为 Mod，用户可干预单轮模型路由与工具执行  
扩展之间协作方式 | 插件向上下文注册服务或监听 Typed 事件，通过服务依赖与生命周期 Effects 实现自动协同 | 扩展按来源、托管配置优先级及依赖关系组成事件处理链，支持扩展 API 命名空间与多模组策略约束  
宿主运行与权限边界 | 运行于 Node.js/Cordis 插件体系，沙箱和审批是另行配置的能力 | 运行于宿主内部受控 JS 环境，经宿主 API 行使当前用户操作系统权限  
  
据 dsh 官方架构文档介绍，DeepSeek Harness 是以 Cordis 框架为底座，把“一切皆插件”作为整套 Harness 的核心装配原则，它的模型适配、工具注册表、会话日志乃至默认的 Agent Loop，都作为插件向共享上下文提供服务，由依赖注入机制管理生命周期，Cordis 底座、Node 环境与引导入口依然承担基础支撑，但应用自身各模块之间没有特权核心，开发者既能用它跑完整的桌面端、Web 端或命令行，也可以通过配置替换其中的服务实现

Claude Code 的 Mods 则是在终端与桌面端运行的产品中开放出来的内部事件扩展能力，官方是在已有运行闭环基础上，逐步把差异对比面板、项目指令加载等内置能力做成 Mods 交付，并允许用户介入提示词、工具校验与模型路由，更深的一层在于，Mod 具备超越界面的深层介入能力：排在事件链前面的 Mod 可以处理后续 Mod 发起的 API 调用，或者挂载新的 API 命名空间，官方开源的遥测模块就是在底层为其他 Mod 注入新方法，而安全模组也在利用事件链约束后续行为，两者的差异主要在于架构范围：一套是用插件装配整套 Harness 的组件服务，另一套是在已有宿主上把关键生命周期开放给事件中间件

举一个常见场景：如果要在 Agent 执行高危命令前做安全审计，或者把执行交给自己定制的环境，两边在设计上都能支持，在 dsh 里，通常是通过提供新的工具服务或执行 provider 替换默认实现，在启动时挂载；而在 Claude Code 里，则是编写 Mod 监听 tool.call 事件，直接在中间件管道里改写执行参数、弹窗让用户确认，或者调用自己的后端执行后返回结果，前者偏向服务契约层面的组件插拔，后者偏向会话流水线上的事件拦截与改写，两者适用的改造粒度各有所长，并不存在功能维度的单向独占

需要说明的是，两套机制的 API 与上下文模型完全不同，基于 Cordis Context 编写的服务提供者无法直接塞进 Claude Code，而 Mods 的 register 与事件钩子也无法直接在 dsh 中运行，业务层面的审计逻辑或规则可以参考，具体的代码实现必须针对各自宿主单独编写

## 05 运行环境与安全边界

使用和编写 Mod 时，有几项关键事实需要明确：

### 1\. Mods 运行在当前用户权限范围内（无沙箱）

官方明确强调：Mods aren’t sandboxed

对于这套机制的安全特征，需要区分三个不同维度的表现：

首先在代码层面，Mod 的 hook 模块本身运行在受控的 JavaScript 环境中，并没有直接暴露原生的 Node.js 全局 API（无法直接使用 require 引入外部底层库，也没有原生的全局定时器或直接网络调用），所有涉及底层资源的操作都必须经由宿主提供的 $ API 进行

其次在权限层面，虽然代码运行受到宿主接口约束，但当 Mod 调用 $.fs 操作文件或通过 $.process 启动外部程序时，在操作系统层面行使的是当前登录用户的实际系统权限，它依然能够读写用户可访问的文件，读取配置文件中的 API Key，或者发起网络请求

最后在系统隔离层面，这种受控的 JS 环境并不等同于操作系统级别的进程沙箱，特别需要注意，Claude Code 的 Bash 沙箱隔离针对的是模型自主调用的 Bash 命令，由 Mod 自身启动的外部进程运行在 Bash 沙箱之外，因此不要随意安装来源不可信的第三方 Mod

### 2\. 界面与权限的硬性边界

Mod 能够重绘大部分交互界面，但官方明确规定：**Mod 不能改绘系统的权限提示框（permission prompt）**

同时，Mod 可以在提示出现前批准或拒绝某些工具调用，具体受托管策略与拒绝规则约束，权限框的显示保护和执行授权是两项需要分别理解的边界

### 3\. 企业管控与sec-default

官方列出的加载条件有两种：机器配置了 Managed Settings，或者用户以 Team / Enterprise 方案登录 Claude Code，满足其中一项，内置的 cc-plugin-sec-default就会先于用户安装的 Mods 加载

它保护托管指令、托管 Hooks、设置和托管 MCP 信息等内容；管理员还可以在托管配置的 cc-plugin-sec-default@builtin选项中设定 allowManagedModsOnly: true，阻止用户自行带入的 Mods 加载

这些保护有明确范围：拒绝规则和托管 Hooks 约束的是 Claude 的工具调用，Mod 自己通过 $.fs或 $.process操作文件、启动程序时，仍有当前用户的访问能力，sec-default提供的治理也需要结合可信来源和组织策略使用

### 4\. UI 绘制的实际环境差异

Mod 的事件钩子支持范围较广，但界面渲染受到宿主环境限制：

  * **终端环境：** 完整支持事件运行与界面绘制
  * **Desktop 桌面客户端：** 在 Code 标签页下支持界面绘制，个别标注为终端专用的元素除外；WSL 会话下暂不支持插件与 Mods
  * **VS Code 扩展聊天面板、claude -p命令行、Agent SDK：** 事件钩子正常运行，但 Mod 绘制的自定义 UI 不会显示
  * **远程控制（Remote Control）：** 事件运行在本地机器会话中，界面也仅绘制于本地终端，远端不显示
  * **云端会话（Cloud Session）：** 当插件满足同步条件时钩子可运行，但界面不会直接渲染



编写带有界面的 Mod 时，需要做好环境兼容处理

## 06 从哪一步开始：动手体验指引

如果你想了解本地环境是否支持，可以按照官方文档推荐的步骤进行查看：

第一步，检查本地 Claude Code 版本是否达到要求：

> claude –version

要求版本在 v2.1.287 或更高

第二步，在会话中运行命令，查看当前环境已加载的内置模组：

> /plugin

在 Installed 标签页下的 Built-in 区域，可以查阅到当前平台支持的内置插件列表

第三步，若想探索编写自己的模组，建议先从简单且低风险的案例入手，例如在终端输出工具调用次数或上下文读数，也可以在 Claude Code 中描述需求，让 Claude 借助官方文档生成本地模组模板，并在对应目录下执行校验：

> claude plugin validate ./your-mod-dir

通过校验工具审查 Mod 声明的事件钩子与系统调用，确认无误后再进行加载

## 07 总结

把 DeepSeek Harness 的架构装配思路与 Claude Code 刚推出的 Mods 放在一起看，能清晰看到 AI 编程运行时的演进脉络：两边都在把 Agent 的执行过程进一步拆解为可以观察、改写与协同的环节，dsh 展现了用服务接口拼装整套 Harness 的可能性，Claude Code 则为日常客户端提供了直接改写事件与界面的抓手，对于开发者来说，理解这些扩展接缝的位置，远比盲目追逐新名词更有价值

作者：Ai学习的老章 公众号：Ai学习的老章

本文由 @Ai学习的老章 原创发布于人人都是产品经理。未经作者许可，禁止转载

题图来自 Unsplash，基于CC0协议


---
> 原文链接: https://www.woshipm.com/ai/6473496.html