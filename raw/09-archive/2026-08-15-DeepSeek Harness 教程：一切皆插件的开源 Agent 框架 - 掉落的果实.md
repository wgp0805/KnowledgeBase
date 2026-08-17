---
title: "DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实"
source: "博客园"
url: "https://www.cnblogs.com/hong2018/p/22494668"
date: "2026-08-15T08:02:00Z"
score: 0.8
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/hong2018/p/22494668  
> **抓取日期**: 2026-08-15  
> **相关性评分**: 0.8

# DeepSeek Harness 教程：一切皆插件的开源 Agent 框架

> **更新时间** ：2026-08-15  
>  **适用版本** ：v0.1 开发者预览版  
>  **说明** ：本文基于官方 README、官方文档（deepseek-harness.github.io）以及 2026 年 8 月 13 日发布以来的公开报道整理。框架仍处于快速迭代的预览阶段，具体细节请以官方最新文档为准。

* * *

## 目录

  * 谁适合阅读本教程？
  * 阅读前需要具备的基础能力
  * 核心特性概览
  * 相关资源
  * 一、DeepSeek Harness 简介
  * 二、快速上手：三分钟跑起来
  * 三、安装详解
  * 四、配置模型
  * 五、Web UI 使用指南
  * 六、四种运行模式详解
  * 七、开发者进阶：从第一个插件开始
  * 八、社区与生态
  * 九、媒体实测与社区反馈
  * 十、常见问题 FAQ
  * 十一、注意事项与风险提示
  * 十二、总结
  * 附录 A：参考链接
  * 附录 B：术语表



* * *

## 谁适合阅读本教程？

以下人群都适合阅读本文：

  * **想了解 DeepSeek Harness 是什么、能做什么** 的开发者与 AI 从业者；
  * **想在自己电脑上把 Harness 跑起来体验** 的"动手派"；
  * 想做 **Agent 二次开发或插件开发** 的人；
  * 想用开源 Agent 框架做**模型基准测试、内部工具链** 的人；
  * 关注 **AI Agent 生态与开源框架** 的科技爱好者、产品经理和技术决策者。



需要说明的是：**现阶段 Harness 更适合开发者，而不是只想用 AI 聊天的普通用户。** 如果你只是想体验 DeepSeek 的对话能力，官方网页版 / App 会更直接；如果你想搭建一个"能自己干活"的 Agent 底座，Harness 才真正对味。

## 阅读前需要具备的基础能力

本教程尽量做到"跟着做就能跑"，但建议你先具备以下基础：

  * 会安装软件（尤其是 Node.js）；
  * 会打开命令行 / 终端，并执行简单命令（Windows 的 PowerShell 或 CMD 均可）；
  * 知道什么是 **API Key（密钥）** 、什么是**环境变量** ；
  * 了解 Git、pnpm 的概念更佳（仅源码安装时需要，用 npx 方式可跳过）；
  * 想做插件开发的话，需要一点 TypeScript / JavaScript 基础（不会也能先跑起来）。



## 核心特性概览

  * **特性一** ：一切皆插件，模型、工具、会话、UI 都可自由替换；
  * **特性二** ：模型无关，DeepSeek、Anthropic、OpenAI 及任意 OpenAI 兼容端点都能接入；
  * **特性三** ：四种运行模式，覆盖日常开发、批量任务、基准测试与实验创造；
  * **特性四** ：每次运行都有迹可循，事件流 + 轨迹回放；
  * **特性五** ：本地可控，工作区隔离 + 权限审批；
  * **特性六** ：MIT 协议开源，免费使用，可二次开发。



详细解读见下文 一、DeepSeek Harness 简介。

## 相关资源

资源 | 链接  
---|---  
官网 | [deepseek.com/harness](<https://www.deepseek.com/harness/>)  
GitHub 仓库 | [github.com/deepseek-ai/deepseek-harness](<https://github.com/deepseek-ai/deepseek-harness>)  
官方文档 · 快速入门 | [deepseek-harness.github.io/deepseek-harness/guide/quickstart](<https://deepseek-harness.github.io/deepseek-harness/guide/quickstart>)  
npm 包 | `@deepseek-ai/dsh`（`npx @deepseek-ai/dsh web` 一键启动）  
Node.js 下载 | [nodejs.org/zh-cn/download](<https://nodejs.org/zh-cn/download>)  
插件社区 | [GitHub Topics: dsh-plugin](<https://github.com/topics/dsh-plugin>)  
社区支持 | [GitHub Discussions](<https://github.com/deepseek-ai/deepseek-harness/discussions>)  
设计论文 | [A Programming Paradigm for Spatiotemporal Composability](<https://github.com/cordiverse/paper>)  
  
* * *

## 一、DeepSeek Harness 简介

### 1.1 什么是 DeepSeek Harness？

**DeepSeek Harness（简称`dsh` / DSH）是 DeepSeek AI 于 2026 年 8 月 13 日发布的开源 Agent（智能体）运行框架**，当前版本为 v0.1 开发者预览版，采用 MIT 协议开放完整源码。

一句话概括它的定位：

> **让大模型不仅会"想"，还会"做"——读写文件、执行命令、调用工具、派出子任务，并在授权范围内把长任务持续做完的运行时底座。**

如果把大模型比作"大脑"，Agent 比作"会思考、会执行、会调试的工作单元"，那么 **Harness 就是连接大脑与工具、手脚的中枢调度系统** 。

### 1.2 为什么需要 Harness？

大模型本身只负责"生成下一步内容"。一个能完成真实工作的 Agent，还需要处理大量"模型之外"的事情：

  * **执行能力** ：读写文件、执行命令、调用外部服务；
  * **上下文管理** ：长任务中会积累大量中间信息，需要压缩、筛选、注入；
  * **权限控制** ：哪些目录能碰、哪些命令要批准；
  * **状态保存与错误恢复** ：任务中断后能恢复、重试；
  * **循环与停止条件** ：什么情况下继续、什么情况下收尾；
  * **可观测性** ：记录每一步的输入输出，方便排查"哪一步出了问题"。



当模型评测从"单次问答"走向"真实工程任务"之后，**Harness 本身已经成为影响评测结果的重要变量** ——同一个模型，在不同运行框架里的表现可能差异很大。

### 1.3 AI 工程范式的三次跃迁

> 说明：以下"三次跃迁"是笔者为了帮助理解而做的梳理，并非官方术语。

阶段 | 形态 | 特点  
---|---|---  
第一次跃迁 | 对话式 AI | 模型即产品，一次提问一次回答，能力边界在"模型本身"  
第二次跃迁 | Agent + 工具调用 | Function Calling、MCP 等把外部工具接入模型，模型开始"动手"  
第三次跃迁 | Agent 运行时（Harness） | 在模型与工具之上，增加循环、权限、状态、可观测、可组合的底座，Agent 可以连续完成数十分钟甚至数小时的任务  
  
DeepSeek Harness 正是第三次跃迁的代表作之一：它不再只拼模型能力，而是把"模型如何利用工具、如何持续运行"变成一套可编程、可组合的底层运行时。

### 1.4 核心架构：一切皆插件

DeepSeek Harness 采用**"一切皆插件"** 的插件式开放架构：

  * **模型、工具、技能、会话、沙箱、存储、Agent 循环、任务调度、UI** ——所有 Agent 能力都由插件组合而成，可自由替换、灵活重组；
  * 底层由 **Cordis 插件元框架** 驱动。Cordis 本身"几乎什么都不干"，只负责三件事：**插件的加载、卸载、依赖关系管理** ；
  * Cordis 的理念来自北京大学与 DeepSeek 联合署名的论文《A Programming Paradigm for Spatiotemporal Composability》，强调"时空可组合性"： 
    * **时间可组合性** ：插件卸载后，它注册过的服务、事件和副作用能随之撤销；
    * **空间可组合性** ：插件可以声明依赖，并在其他组件变化时重新建立协作关系。



对开发者的直接价值：

  1. **模型与运行环境分离** ：可以保留同一套会话、工具、权限体系，只替换模型适配器，方便对比不同模型；
  2. **企业可保留自己的基础设施** ：沙箱、存储、审批、凭证、遥测都可以做成插件，接入内部权限与审计体系；
  3. **能力可以形成独立生态** ：开发者不需要维护 Harness 主代码，只要按插件接口开发，就能扩展或替换任意能力。



### 1.5 四种运行模式

针对不同使用场景，DeepSeek Harness 内置**四种运行模式** ，每种模式默认加载不同的插件集合：

模式 | 默认插件集合 | 适用场景  
---|---|---  
**标准模式** （standard） | 完整的工具组合（文件操作、Shell、搜索、子任务委派、计划维护等） | 日常写代码、修 Bug、分析项目，默认推荐  
**PTC / 代码模式** （Programmatic Tool Calling） | 模型先生成一段代码，由代码编排多轮工具调用 | 连续查询、批量处理、需要根据中间结果分支的任务  
**极简模式** （minimal） | 只保留一个 Shell 工具和一个文件编辑工具 | 最小环境下做模型基准测试  
**创造模式** （creative） | 可检查当前运行时、在内存中试验 Cordis 插件 | 实验新插件，组合并创作新的模式  
  
### 1.6 核心特性

#### 特性一：一切皆插件，像玩乐高一样拼装

模型、工具、会话、存储、UI 全是插件。开发者无需修改 Harness 主体源码，就能替换或扩展任意能力。不少内测开发者评价："完全模块化，可以重写、替换任何不喜欢的部分。"

#### 特性二：模型无关（Model-agnostic）

官方内置 DeepSeek 模型接入，同时支持 Anthropic、OpenAI 等提供方，以及任意 OpenAI 兼容的自定义端点（公司网关、自建服务器都行）。模型配置变更**下次请求即生效，无需重启服务** 。

#### 特性三：四种运行模式自由选择

从"最完整的标准模式"到"只留两个工具的极简模式"，再到"让 Agent 自己造插件"的创造模式，覆盖了从基础任务到高级实验的全部场景。

#### 特性四：每次运行都有迹可循

模型看到的一切都会写入**仅追加（append-only）的会话日志** ，包括系统提示词、思维链、工具调用与结果、子 Agent 调度、每一次上下文注入。可以在**轨迹视图（Trajectory）** 中按来源查看；会话的恢复、分叉、检索与回放都共享同一套事件流。

#### 特性五：本地可控，权限审批

Agent 只能操作你明确选择的**工作区** 目录；危险操作会先弹出确认。工作区隔离 + 权限确认机制，对重视数据隐私和本地执行的场景更友好。

#### 特性六：MIT 协议开源

完整源码开放，免费使用，可自由二次开发。发布当天 GitHub 仓库半小时星数破万（据媒体报道），社区热度极高。

### 1.7 Harness 与相关工具的关系

工具 / 框架 | 与 Harness 的关系  
---|---  
**MCP** | 两者不在同一层。MCP 是连接 AI 应用与外部数据、工具、工作流的**开放标准** ；Harness 是更上层的**运行逻辑** （什么时候给模型工具、调用前是否审批、失败是否重试、何时派出子任务、何时停止）。MCP Server 可以成为 Harness 里的一个插件  
**OpenAI Agents SDK** | 同类参照物，提供工具、Agent 交接、护栏、会话与追踪  
**Claude Agent SDK / Claude Code** | Claude Code 更像"精致、即插即用的商业化成品"；Harness 是开放可定制的"工坊"  
**LangGraph** | 侧重持久化执行、人类介入与状态恢复，与 Harness 同属运行时赛道  
**OpenAI Codex** | 社区常拿来做对比：Codex 偏封闭黑盒，Harness 主打开放可重写  
**Pi-Agent** | 社区讨论中常提到的另一个 MIT 协议开源轻量 Agent 框架  
  
* * *

## 二、快速上手：三分钟跑起来

最快路径只需要三步：

**第 1 步：安装 Node.js**

从 [nodejs.org/zh-cn/download](<https://nodejs.org/zh-cn/download>) 下载并安装 **22.19 及以上（22.x 系列）或 24 及以上** 的 LTS 版本。安装后在终端验证：
    
    
    node -v
    

能输出版本号即安装成功。

**第 2 步：一键启动**
    
    
    npx @deepseek-ai/dsh web
    

首次运行会自动下载依赖包，稍等片刻。终端会打印访问地址，默认是：
    
    
    http://127.0.0.1:3080
    

**第 3 步：在浏览器中完成配置**

  1. 打开 `http://127.0.0.1:3080`；
  2. 进入 **设置 → 模型** ，填入 DeepSeek API Key 并保存（密钥申请见下文）；
  3. 点击**选择工作区** ，添加你想让 Agent 操作的项目目录并选中；
  4. 在对话框中发送第一个任务，例如：


    
    
    Summarize this repository and identify its main packages.
    

到此，你已经成功跑起了一个开源 Agent 框架。

* * *

## 三、安装详解

### 3.1 环境要求

项目 | 要求  
---|---  
操作系统 | Windows 10+、macOS 10.15+ 或主流 Linux（x64 / arm64）  
Node.js | v22.19 及以上（22.x 系列），或 v24 及以上  
包管理器 | npx 方式无需额外安装；源码安装需要 pnpm（`npm install -g pnpm`）  
网络 | 首次启动需要从 npm 拉取依赖  
API Key | DeepSeek 或其他兼容提供方的密钥（启动后可在界面中配置）  
硬件 | 普通笔记本即可，无特殊要求  
可选 | Git；Python 3.10+（仅使用官方 Python SDK 时需要）  
  
建议**单独准备一个练习目录作为工作区** ，避免 Agent 误操作重要文件。

### 3.2 方式一：npx 快速体验（推荐）
    
    
    npx @deepseek-ai/dsh web
    

要点：

  * 首次运行会从 npm 下载 `@deepseek-ai/dsh` 包，需保持网络通畅；
  * 启动成功后终端会打印地址（默认 `http://127.0.0.1:3080`）；
  * **关闭终端，服务一般会随之停止** ；
  * 国内网络较慢时，可先配置 npm 镜像：


    
    
    npm config set registry https://registry.npmmirror.com
    

### 3.3 方式二：从源码运行

需要改配置、做二次开发或开发插件时，从源码运行：
    
    
    git clone https://github.com/deepseek-ai/deepseek-harness.git
    cd deepseek-harness
    pnpm install
    pnpm run build
    pnpm dsh web
    

若未安装 pnpm，先执行：
    
    
    npm install -g pnpm
    

### 3.4 方式三：Python SDK（程序化调用，可选）

适合把 Harness 的能力嵌入自己的脚本或自动化流程，而不是通过 Web 界面交互。

> ⚠️ **注意** ：官方 Python SDK 文档目前列出的前置环境为 **Linux x64 / Linux arm64 / macOS 14+（arm64）** ，示例组合不支持 Windows。Windows 用户建议用 Web UI 方式体验，或借助 WSL。
    
    
    git clone https://github.com/deepseek-ai/deepseek-harness.git
    cd deepseek-harness
    python -m venv .venv
    source .venv/bin/activate        # Windows WSL/Linux 下的激活方式
    python -m pip install deepseek-harness-sdk
    

设置环境变量：
    
    
    export DEEPSEEK_API_KEY=你的密钥
    # export DEEPSEEK_BASE_URL=http://127.0.0.1:8000/v1   # 使用 OpenAI 兼容代理时
    # export DSH_MODEL=deepseek-v4-flash
    # export DSH_SYSTEM_PROMPT='You are a helpful software engineer assistant.'
    

运行仓库内置示例：
    
    
    python examples/jsonrpc-agent/minimal.py \
      --workspace /绝对路径/workspace \
      --session-root /绝对路径/sessions \
      --session-id example-001 \
      "Inspect the repository and fix the failing tests."
    

SDK 的完整用法见官方文档 [Python SDK 快速上手](<https://deepseek-harness.github.io/deepseek-harness/guide/python-sdk>)。

### 3.5 安装常见问题

问题 | 解决方法  
---|---  
`node -v` 无输出或版本过低 | 重新安装 Node.js，确保 ≥ v22.19（22.x）或 ≥ v24  
下载依赖超时 / 安装慢 | 配置 npmmirror 镜像后重试  
端口 3080 被占用 | 先关掉占用程序，或换端口启动（以官方 CLI 帮助为准）  
服务停不掉 | 关闭运行它的终端窗口；必要时在任务管理器中结束 `node` 进程  
浏览器打不开地址 | 确认服务进程还在运行，且地址完全一致（注意是 `127.0.0.1` 不是 `localhost` 也能通）  
  
* * *

## 四、配置模型

### 4.1 配置 DeepSeek

  1. 打开 Web UI 的 **设置 → 模型** ；
  2. 在 DeepSeek 卡片中填写 **API 密钥** 并保存；
  3. 模型路由会**立即生效，不需要重启服务器** 。



DeepSeek API 密钥在官方开放平台申请（`platform.deepseek.com`，登录后在"API Keys"处创建）。API 调用按官方计费规则收费，请留意自己的用量。

### 4.2 添加其他模型提供方

**已内置目录的提供方** ：选择"添加提供方"，可以选 Anthropic、OpenAI 等，输入 API Key 保存即可。已安装目录会提供端点、协议和模型列表。

需要各自**原生凭据** 的提供方：

  * Bedrock：AWS 凭据与区域；
  * Vertex：ADC（应用默认凭据）项目；
  * Azure：`api-version` 等参数；
  * Codex：OAuth 登录。



**自定义提供方** （公司网关、自建服务器等）：

  1. 选择"添加自定义提供方"；
  2. 填写：小写 **Provider ID** 、**基础 URL** 、**API 协议** 、**凭据** 、至少**一个模型** ；
  3. 选择"获取可用模型"可以查询当前 URL 下可用的模型列表（模型发现会调用 OpenAI 兼容的 `GET /models` 端点；不提供该端点的服务需手动输入模型）。



> Provider ID 是**永久** 的——请求、已保存会话、模型默认值和凭据引用都会使用它。想重命名时，应新建提供方并删除旧的。

### 4.3 凭据存储与安全

  * API 密钥是**只写** 的：保存后页面只会显示脱敏描述符，永远不会回显明文；
  * 密钥存储在 `$DSH_HOME/.credentials.yaml` 中，设置页只保留凭据引用；
  * 请妥善保管该文件，不要提交到 Git 仓库。



### 4.4 选择模型与常见排错

配置好的提供方会出现在**模型选择器** 中；选择某个模型会将其设为新会话的默认值。已发送过请求的会话会保留自身日志中记录的模型。

报错 / 现象 | 处理方法  
---|---  
`MISSING_CREDENTIAL` | 到模型页存储提供方密钥，或配置所引用的环境变量  
`UNKNOWN_MODEL` | 选择已配置的模型，或给自定义提供方补上缺失的模型  
"获取可用模型"返回 401 | 检查 API Key 是否正确  
图片在发送前被拒绝 | 该模型未声明图片模态；自定义提供方的视觉模型需加 `input: [text, image]`（DeepSeek 自身的 chat-completions 路由为纯文本，无法配置改变）  
提供方拒绝带图片的请求 | 该模型声明了端点实际并不支持的图片能力，需去掉 `image` 模态并开启新会话  
  
* * *

## 五、Web UI 使用指南

### 5.1 选择工作区

`dsh` 进程会把启动时的调用目录作为默认文件系统位置，但 Web UI 在**添加工作区之前不会选中任何工作区** ：

  1. 点击"选择工作区"；
  2. 添加启动 `dsh` 时所在的项目目录；
  3. 选中它。



> 选中工作区之前，会话输入框是不可用的——这是刻意的安全设计：Agent 只能操作你明确授予的目录。

### 5.2 运行第一个任务

官方快速上手示例（英文）：
    
    
    Summarize this repository and identify its main packages.
    

中文任务示例：
    
    
    分析当前目录的结构，并生成一份简要说明。
    
    
    
    定位并修复当前测试失败的问题。
    

Agent 会读取工作区文件、运行命令、必要时委派子任务并维护计划。任务描述越明确，效果越好。

### 5.3 权限与审批

当操作超出当前权限策略、需要审批时，Web UI 会**先询问你** 再执行。实际使用建议：

  * 先在**独立练习目录** 里试，熟悉权限确认和文件修改行为；
  * 涉及写操作、删除、执行命令时多看几眼再放行；
  * 不要把生产环境关键目录直接设为工作区。



### 5.4 轨迹视图与事件流

这是 Harness 最有特色的功能之一：

  * 所有会话记录以**仅追加的事件流** 保存，是 Agent 全部交互历史的唯一事实来源；
  * 系统提示词、思维链、工具调用与结果、子 Agent 调度、上下文注入都会被记录；
  * 在 **Trajectory（轨迹）视图** 中可以按来源查看每一步；彩色进度条对应每个运行节点，鼠标选中即可查看详细过程；
  * **恢复、分叉、检索与回放** 都基于同一套事件流。



价值很直接：当 Agent 在第几十步做错了决定，你可以回到"模型当时真正看到的内容"，判断问题到底出在模型判断、工具返回、提示词还是上下文注入。

* * *

## 六、四种运行模式详解

### 6.1 标准模式（standard）

  * **插件集合** ：完整工具组合，包括文件操作、Shell、搜索、子任务委派、计划维护等；
  * **适用场景** ：日常写代码、修 Bug、分析项目、文档整理；
  * **特点** ：能力最全、最"省心"，是默认选择。



### 6.2 PTC / 代码模式（Programmatic Tool Calling）

  * **工作方式** ：模型先生成一段代码，再由代码组织多轮工具调用；
  * **适用场景** ：需要连续查询、批量处理、根据中间结果分支的任务；
  * **优势** ：减少模型与工具之间反复往返，降低上下文中堆积的中间信息；
  * **注意** ：模型生成的代码获得了更强的调度能力，对沙箱隔离、超时、资源配额和权限控制要求更高。



### 6.3 极简模式（minimal）

  * **插件集合** ：只保留一个 Shell 工具 + 一个文件编辑工具；
  * **适用场景** ：最小环境下做**模型基准测试** ，尽量减少外围工具差异；
  * **特点** ：让评测更接近对模型自主规划、代码修改和终端操作能力的直接观察；Agent 不会做多余动作。



### 6.4 创造模式（creative）

  * **工作方式** ：Agent 可以检查当前运行时、在内存中试验 Cordis 插件，再组合出新的运行模式；
  * **适用场景** ：插件实验、模式创作、"让 Agent 自己改进自己"的探索；
  * **注意** ：官方已有"自指式"演示，允许 Agent 检查和修改正在运行的插件环境，但距离稳定的"自我进化"还有很长的工程路径。



### 6.5 模式对比速查

模式 | 插件多少 | 可控性 | 上手难度 | 典型用途  
---|---|---|---|---  
标准 | 多（完整工具组合） | 中 | 低 | 日常开发  
PTC/代码 | 中（代码编排工具） | 高 | 中 | 批量、复杂流程  
极简 | 少（Shell + 编辑） | 高 | 低 | 模型基准测试  
创造 | 动态（内存试验） | 最高 | 高 | 插件实验、新模式  
  
* * *

## 七、开发者进阶：从第一个插件开始

> 本节为开发者准备。官方教程位于仓库 `docs/user/develop/basic/`，从源码运行后即可跟着做。

### 7.1 插件是什么

在 Harness 中，**插件是一个导出`apply` 函数的 TypeScript 模块**。框架加载插件时会调用 `apply`，并传入一个 `ctx`（上下文对象），你通过 `ctx` 注册能力：
    
    
    import type { Context } from '@deepseek-ai/cordis'
    
    export const name = 'my-plugin'
    
    export function apply(ctx: Context) {
      // 在这里注册工具、服务、事件等能力
    }
    

### 7.2 注册一个工具

工具通过 `ctx.tools.register(defineTool(...))` 注册。官方教程强调，工具描述要写清楚：

  * **何时调用** 、必要前置条件、失败语义与副作用；
  * `parameters` 与 `output.schema` 的规范。


    
    
    ctx.tools.register(
      defineTool({
        name: 'my_tool',
        description: '描述该工具的作用、前置条件与副作用',
        parameters: { /* JSON Schema */ },
        async execute(args) {
          // 工具实现
        },
      }),
    )
    

### 7.3 插件配置

Harness 要求"两个部署环境可能需要不同的值"都做成配置字段。插件的默认配置写在 `cordis.yml` 中，Cordis 加载插件时会用导出的 schema 校验配置并填充默认值。

### 7.4 发布与发现

  * 为你的插件仓库添加 **`dsh-plugin`** 话题（GitHub Topics），便于被社区发现；
  * 欢迎到 [GitHub Discussions](<https://github.com/deepseek-ai/deepseek-harness/discussions>) 分享插件和反馈；
  * 社区内测期间已出现数百个插件（据社区统计），涵盖工具、UI、权限钩子等类型。



* * *

## 八、社区与生态

  * **GitHub Discussions** ：提交反馈、Bug 报告、讨论功能与插件；
  * **GitHub Topics:`dsh-plugin`**：插件聚合与发现入口；
  * **企微群** ：官方提供入群问卷，扫码添加企微小助手后可加入官方交流群；
  * **生态现状** ：发布当天星数迅速破万（媒体报道），社区热度高；插件生态处于早期、快速生长阶段。



* * *

## 九、媒体实测与社区反馈

> 以下均为**媒体 / 社区的一手实测反馈，不是官方承诺** ，请以你自己的实测结果为准。

**媒体实测案例（智东西 2026-08-14）：**

  * 88 页论文 PDF 翻译任务：耗时约 22 分钟，过程中派出 10 个子代理，完成复制、修正与补齐，最终得到格式完整、内容严谨的翻译文件；
  * 任务期间首 Token 启动速度平均约 1.4 秒，缓存命中率 98%；
  * 贪吃蛇小游戏：极简模式约 50 秒完成，PTC 模式约 1 分 05 秒完成。



**社区口碑较好的点：**

  * 长任务稳定性：V4 Flash / V4 Pro 在 DSH 中完成多步工具调用时，返工频率和交付质量口碑不错；
  * 成本友好：搭配 DeepSeek 自家模型时，复杂编程任务的费用往往只有几毛到一两块（社区反馈，随模型价格调整会变化）；
  * 可观测性好：事件流、轨迹回放、会话日志对排查问题很有价值。



**被吐槽的点：**

  * 上手门槛偏高：需要 Node.js、终端命令，缺少面向普通用户的引导；
  * 产品细节粗糙：Thinking 过程文字闪烁、多面板与 Diff 展示等还不够完善；
  * 稳定性：作为开发者预览版，接口可能随时变化，插件生态仍在早期。



* * *

## 十、常见问题 FAQ

**Q1：DeepSeek Harness 是免费的吗？**

框架本身以 MIT 协议开源，**使用框架免费** ；但调用模型 API 需要按 DeepSeek 官方计费规则付费（模型调用费用以官方为准）。

**Q2：一定要用 DeepSeek 的模型吗？**

不是。官方支持 Anthropic、OpenAI、Bedrock、Vertex、Azure、Codex 以及任意 OpenAI 兼容的自定义端点。

**Q3：Windows 能不能用？**

Web UI / CLI 方式支持 Windows（Node.js 环境即可）。官方 **Python SDK 示例目前面向 Linux 与 macOS** ，Windows 用户建议用 Web UI，或通过 WSL 使用 Python SDK。

**Q4：Harness 和 MCP 有什么区别？**

MCP 是"连接标准"（AI 应用如何接入外部工具和数据），Harness 是"运行逻辑"（何时调用、是否审批、如何重试、何时停止）。MCP Server 可以作为插件接入 Harness。

**Q5：它能替代 Claude Code / Codex 吗？**

目前更像一个开放的"底座/工坊"，而不是开箱即用的成品。如果你追求开箱即用，商业产品更省心；如果你想高度定制、可控，Harness 的开放性是优势。

**Q6：可以直接上生产环境吗？**

官方明确这是**开发者预览版** ，未来将出现破坏兼容性的变更。建议先在实验环境评估，生产关键流程等版本稳定后再考虑。

**Q7：怎么保护我的数据？**

使用独立工作区目录；不要把密钥、敏感文件放进工作区或会话日志；注意会话日志会记录工具调用与文件内容，妥善管理 `$DSH_HOME` 下的配置文件。

* * *

## 十一、注意事项与风险提示

  1. **预览版警告** ：官方声明"未来将出现破坏兼容性的变更"，配置与插件接口可能随时调整；
  2. **不构成生产承诺** ：功能、稳定性、性能均以官方最新版本为准，不要基于本教程做关键决策；
  3. **成本控制** ：模型 API 按量计费，长任务可能产生较多 token，请关注官方计费与缓存命中率；
  4. **数据安全** ：会话事件流可能包含代码、凭据线索和内部文件内容，注意权限与脱敏；
  5. **插件供应链风险** ：插件可以访问文件与外部服务，安装第三方插件前请检查来源；
  6. **网络环境** ：首次启动与 API 调用都需要网络；内网环境可能需要配置代理或镜像；
  7. **以官方文档为准** ：本文信息截至 2026-08-15，后续请以 [官方文档](<https://deepseek-harness.github.io/deepseek-harness/guide/quickstart>) 和 [GitHub 仓库](<https://github.com/deepseek-ai/deepseek-harness>) 的最新内容为准。



* * *

## 十二、总结

DeepSeek Harness 是一套**把大模型接到本地文件与工具上的开源 Agent 运行时** ，核心卖点不是"又一个聊天产品"，而是：

  * **一切皆插件** 的可组合架构（基于 Cordis）；
  * **模型无关** 的开放接入；
  * **四种运行模式** 覆盖日常开发、批量任务、基准测试与实验创造；
  * **事件流 + 轨迹回放** 的强可观测性；
  * **MIT 开源** 带来的二次开发空间。



如果你想搭建属于自己的、可控、可定制的 Agent 环境，或者想对比不同模型在相同工具环境下的真实表现，DeepSeek Harness 值得一试。安装只需要一条命令：
    
    
    npx @deepseek-ai/dsh web
    

然后打开 `http://127.0.0.1:3080`，配置 API Key、选择工作区，就能看到它"自己干活"的全过程了。

* * *

## 附录 A：参考链接

**官方资源**

  * 官网：<https://www.deepseek.com/harness/>
  * GitHub 仓库：<https://github.com/deepseek-ai/deepseek-harness>
  * 官方文档 · 快速入门：<https://deepseek-harness.github.io/deepseek-harness/guide/quickstart>
  * 配置模型：<https://deepseek-harness.github.io/deepseek-harness/guide/providers>
  * Python SDK 快速上手：<https://deepseek-harness.github.io/deepseek-harness/guide/python-sdk>
  * 设计论文：<https://github.com/cordiverse/paper>



**相关报道（背景参考）**

  * 腾讯科技 / 36氪：《DeepSeek 的 Harness，为何是一头黑色鲸鱼？》
  * 界面新闻：《像玩乐高一样拼插件，DeepSeek Harness 能带来哪些改变？》
  * 智东西：《实测 DeepSeek Harness！》
  * 阿里云开发者社区：《DeepSeek Harness 本地安装与使用指南》



## 附录 B：术语表

术语 | 含义  
---|---  
Agent | 智能体，能理解任务、调用工具、执行并反馈的完整工作单元  
Harness | 智能体运行框架 / 运行时，负责"模型之外"的执行逻辑  
Cordis | Harness 底层的插件元框架，只负责插件的加载、卸载与依赖管理  
插件（Plugin） | 导出 `apply` 函数的 TypeScript 模块，可注册工具、服务等能力  
模式（Mode） | 预设的插件集合，如标准、PTC、极简、创造四种  
PTC | Programmatic Tool Calling，程序化工具调用，由模型生成的代码编排多轮工具调用  
MCP | Model Context Protocol，连接 AI 应用与外部工具/数据的开放标准  
Trajectory | 轨迹视图，按来源查看 Agent 每一步运行过程  
工作区（Workspace） | 授予 Agent 操作权限的项目目录  
API Key | 调用模型服务的密钥  
  
* * *

_本文基于公开资料整理，仅供学习交流。DeepSeek Harness 为 DeepSeek AI 开源项目，一切以官方最新文档为准。_


---
> 原文链接: https://www.cnblogs.com/hong2018/p/22494668