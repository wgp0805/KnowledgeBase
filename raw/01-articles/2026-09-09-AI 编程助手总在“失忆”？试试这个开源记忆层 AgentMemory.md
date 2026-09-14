---
title: "AI 编程助手总在“失忆”？试试这个开源记忆层 AgentMemory"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6462278.html"
date: "Wed, 09 Sep 2026 08:11:39 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# AI 编程助手总在“失忆”？试试这个开源记忆层 AgentMemory

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6462278.html  
> **抓取日期**: 2026-09-09  
> **相关性评分**: 1.0

> 这款开源记忆层 AgentMemory 在 GitHub 拿下 28k Star，把项目交互沉淀为可检索的工作记录，并以四层记忆模型、MCP 与 hooks 自动写入会话事件，让新会话开局即召回历史上下文与长期经验。

![](https://image.woshipm.com/2025/02/16/2f202ffa-ec76-11ef-9075-00163e09d72f.png)

上周，我分享了火山引擎开源的**OpenViking** 。它更像一套面向 Agent 的**上下文数据库** ，适合把记忆、项目资料和技能统一组织起来。OpenViking 实战：把知识库、长期记忆和 Agent 技能统一到一个上下文文件系统

文章发出后，有朋友反馈确实好用，也有人提出了另一个需求：如果我暂时不想搭一套较重的上下文系统，只想先解决 AI 编程助手的**“跨会话失忆”** ，有没有更轻量的方案？

**这次分享的 agentmemory，正好瞄准这个问题。**

## 01 AI 编程助手为什么总要重新认识项目

![](https://image.woshipm.com/wp-files/2026/09/20260909144157324460-02.png)

项目地址：https://github.com/rohitg00/agentmemory

现在的 AI 编程助手，单次会话里的表现已经相当不错。它可以**理解代码、修改文件、运行测试** ，还能根据报错继续修复。

**问题出在会话结束之后。**

> 项目使用 TypeScript 和 PostgreSQL
> 
> JWT 认证放在 src/middleware/auth.ts
> 
> 测试文件是 test/auth.test.ts
> 
> 认证库选择 jose，原因是需要兼容 Edge Runtime

第二天，你只想继续说一句：“给这个接口加上限流。”

一个没有持久化记忆的 Agent，往往还要**重新扫描项目、重新确认认证方案** ，甚至再次询问你为什么选择 jose。这些信息明明已经在昨天的工作中出现过，却**没有被有效保存和调用** 。

CLAUDE.md、.cursorrules、Cursor Notepads 等文件，适合存放稳定的项目规则和人工维护的说明。它们的优点是直观、可控，局限也很明显：需要**手动维护，内容容易过时，检索能力有限** ，而且通常和某个 Agent 的配置绑定在一起。

**agentmemory 的思路，是把 Agent 的工作过程转化为可以保存、检索和管理的记忆。**

![](https://image.woshipm.com/wp-files/2026/09/20260909144157824841-03.png)

## 02 agentmemory 到底保存了什么

![](https://image.woshipm.com/wp-files/2026/09/20260909144159791525-04.png)

agentmemory 会通过 Agent 的**hooks 捕获会话中的提示词、工具调用、文件访问、命令执行结果和错误信息** ，再把这些观察记录整理成更适合检索的内容。

它提供了**MCP 和 REST API** ，因此不同的 Agent 可以**共享同一个本地记忆服务** 。你可以使用 Claude Code 完成一部分工作，再用 Cursor 或 Codex CLI 接着处理，项目背景和过去的决策仍然可以被检索到。

  1. **捕获：** 记录 Agent 做过什么。把每一次工具调用、文件读取、命令执行的原始观察保存下来。
  2. **记忆：** 把值得长期保留的事实、决策和工作方式提炼出来。记忆不是聊天记录的全文搬运。



agentmemory 并不只是把完整聊天记录全部塞进上下文。它会对观察结果进行**压缩、索引和召回** ，在新会话开始时，只注入**与当前项目和问题相关的内容** 。

![](https://image.woshipm.com/wp-files/2026/09/20260909144200368619-05.png)

工作流程

## 03 四层记忆模型：从工作记录到长期经验

![](https://image.woshipm.com/wp-files/2026/09/20260909144201100930-06.png)

项目 README 将记忆整理为**四个层级** ：

![](https://image.woshipm.com/wp-files/2026/09/SVaH2S48AFgK5eHMFyWT.png)

这个设计比较适合软件开发场景。

一次工具调用通常只是一个局部动作，例如读取了某个文件、执行了一条命令。真正有价值的内容，往往要等到多个动作组合起来以后才能看出来：某个 bug 的根因是什么，为什么采用某种实现，测试覆盖了哪些边界。

agentmemory 会尝试把这些零散记录逐步整理成更稳定的项目知识。项目还提供了记忆的**版本关系、来源追踪、过期处理和相似记忆提示** ，方便后续治理。

不过，README 中关于“**像人脑一样按遗忘曲线自动管理记忆** ”的表述，更适合看作**产品设计类比** ，不能理解为它真正复现了人类记忆机制。实际效果仍然取决于**捕获质量、压缩策略、索引方式和召回结果** 。

## 04 它怎样找到正确的记忆

![](https://image.woshipm.com/wp-files/2026/09/20260909144201758179-07.png)

agentmemory 支持**多种检索信号** 。

默认情况下，可以使用 BM25 做关键词检索。配置向量模型后，还可以进行语义检索。项目也支持**知识图谱相关能力** ，用实体和关系补充检索结果，最后将不同来源的结果进行融合。

  * 关键词检索：适合查找文件名、函数名、库名和错误信息。基于 BM25，无任何模型依赖。
  * 向量检索：适合处理表达不同但含义相近的问题。需要 embedding 模型支撑。
  * 图关系检索：适合回答“某个决策和哪些文件、模块或问题有关”。



这也是它和**单纯的聊天记录搜索之间的差别** 。

**注意**

语义检索并非默认一定开启。项目支持无模型的 BM25 模式，也可以通过配置本地 embedding 模型来避免调用远程服务。本地方案是 Xenova/all-MiniLM-L6-v2，首次使用时需要下载模型，后续在本机运行。

## 05 和 OpenViking 的区别

![](https://image.woshipm.com/wp-files/2026/09/20260909144202334562-08.png)

这两个项目都在处理 Agent 的上下文问题，但定位不同。

  * agentmemory：Agent 的持久化记忆层捕获 · 整理 · 检索 · 注入
  * OpenViking：Agent 的上下文管理系统文档 · 资料 · 技能 · 记忆



agentmemory 更像一层专注于“**工作记忆** ”的基础设施。它主要记录 Agent 做过什么，再把相关结果召回给 Agent。重点在于会话捕获、记忆整理、检索和自动注入。

OpenViking 的范围更大。它把记忆、项目资料和技能统一组织成虚拟文件系统，Agent 可以通过目录、文件和搜索操作主动导航上下文。换句话说，OpenViking 更接近 Agent 的**上下文管理系统** ，agentmemory 更接近 Agent 的**持久化记忆层** 。

如果你的主要问题是“**每次开始编码都要重新解释项目** ”，agentmemory 更直接。如果你需要统一管理大量文档、技能、项目资料和记忆，OpenViking 的覆盖面更广。

## 06 安装体验

一条命令可以启动，但 Windows 仍需留意

> npx -y @agentmemory/agentmemory@latest

首次启动会进入交互式向导，主要完成几件事：

  1. 选择需要接入的 Agent
  2. 配置记忆整理所使用的模型提供商
  3. 决定是否安装全局命令
  4. 启用或配置相应的 MCP、hooks 和技能



默认情况下，agentmemory 会启动本地服务。端口分工是：

![](https://image.woshipm.com/wp-files/2026/09/0vFolI09xj7p58zTwhWX.png)

启动后可以在浏览器打开：

> http://localhost:3113

![](https://image.woshipm.com/wp-files/2026/09/20260909144202969461-09.png)

![](https://image.woshipm.com/wp-files/2026/09/20260909144203342072-10.png)

Linux 和 macOS 通常可以由 npm 包自动处理 iii-engine 的安装。Windows 原生环境则需要额外准备 iii-engine，需要**手动下载对应版本的 iii.exe** ，或者使用 WSL2 和 Docker Desktop。

这也是整个安装流程里最需要提前说明的地方：agentmemory 的命令入口很简单，**底层运行时依赖仍然存在** 。对于熟悉 Node.js 和本地服务的开发者，部署难度不高；对于只想执行一条命令、完全不想处理运行时依赖的用户，**Windows 体验还不够轻** 。

## 07 iii-engine 是什么

agentmemory 的后端运行在 **iii-engine** 之上。

**iii 的官方定位，是用 Worker、Function 和 Trigger 三个基本抽象来组合和观察服务。** 它提供状态存储、消息流、任务触发、Worker 管理和可观测能力。agentmemory 把自己的记忆功能注册到这个运行时中。

因此，iii-engine 更准确的理解是 agentmemory 的**运行时和基础设施层** 。它承载了数据状态、服务通信、触发机制和监控能力。把它简单描述成“**一个数据库** ”并不准确，它承担的范围更大。

![](https://image.woshipm.com/wp-files/2026/09/20260909144203670452-11.png)

项目的一项特点，是尽量把记忆服务需要的运行能力放到 iii 中，减少用户手动配置传统基础设施的工作。按照 agentmemory 的官方说明，用户无需单独搭建 PostgreSQL、Redis、Express、pm2 或 Prometheus 这一整套组件。

但这并不代表没有依赖，而是把多项依赖集中到了一个新的运行时中。它降低了组件数量，也增加了**对 iii 生态的依赖** ，这是评估项目时需要考虑的取舍。

项目地址：https://github.com/iii-hq/iii

![](https://image.woshipm.com/wp-files/2026/09/20260909144204084372-12.png)

Windows 还需要配置环境变量：

![](https://image.woshipm.com/wp-files/2026/09/20260909144204513984-13.png)

## 08 模型配置：OpenAI 只是协议入口

在向导中，如果没有看到你正在使用的模型厂商，可以选择 **OpenAI 兼容接口** ，再填写对应的 Base URL、API Key 和模型名。

agentmemory 当前支持多种模型提供商，也支持 Ollama、LM Studio、vLLM 等提供 OpenAI 兼容接口的本地服务。这里的“OpenAI”更准确地说是**协议兼容选项** ，并不意味着只能使用 OpenAI 的模型。

配置文件位于：

> ~/.agentmemory/.env

**提示**

模型提供商和功能开关是两回事。配置了模型之后，是否启用自动压缩、总结或知识图谱处理，还要看相应的环境变量设置。建议先使用默认配置观察效果，再逐步开启自动压缩，避免每次工具调用都产生额外模型费用。

![](https://image.woshipm.com/wp-files/2026/09/20260909144205106041-14.png)

## 09 MCP 接通之后，还需要 hooks 才能自动采集

这里有一个**容易混淆的概念** 。

**MCP 负责让 Agent 调用记忆服务，例如保存一条记忆、搜索过去的记录、查看会话历史。** 它解决的是“Agent 能不能使用记忆工具”。hooks 负责在会话生命周期和工具调用过程中自动采集信息。它解决的是“Agent 的工作过程能不能被记录下来”。

所以，只接通 MCP，通常只能**手动保存和查询** ；想要自动记录会话，还需要安装对应的**插件或 hooks** 。

以 Claude Code 为例，官方仓库提供了插件安装方式：

> /plugin marketplace add rohitg00/agentmemory
> 
> /plugin install agentmemory

安装后，Claude Code 的会话、提示词和工具调用可以按照插件支持的 hook 事件写入 agentmemory。项目也提供了针对 Codex CLI、Cursor、OpenCode、Gemini CLI 等工具的不同接入方式，具体能力取决于对应 Agent 的插件和 hooks 支持情况。

![](https://image.woshipm.com/wp-files/2026/09/20260909144205437469-15.png)

![](https://image.woshipm.com/wp-files/2026/09/20260909144205952467-16.png)

## 10 我认为它最值得关注的地方

![](https://image.woshipm.com/wp-files/2026/09/20260909144206373056-17.png)

agentmemory 最有价值的地方，不在于它宣称“**让 Agent 记住一切** ”，而在于它把记忆变成了一条**相对完整的工程管线** ：

![](https://image.woshipm.com/wp-files/2026/09/20260909144207055303-18.gif)

**图示** 捕获 → 压缩 → 索引 → 召回，光点沿线流动

这条链路里，最重要的是“**召回质量** ”和“**记忆治理** ”。

**记忆保存得越多，未必越好。** 如果旧方案、临时判断和错误总结也被长期注入，Agent 可能会被自己的历史误导。agentmemory 提供了记忆版本、来源、相似项和删除能力，这些功能比单纯增加向量库容量更重要。

从这个角度看，Agent 的长期记忆最终需要解决三个问题：

  1. 什么内容值得记住
  2. 什么内容应该在什么时候被召回
  3. 错误、过时或敏感内容如何被删除



agentmemory 已经开始覆盖这些问题，但项目仍然处于快速迭代阶段，实际使用时需要查看记忆内容，**定期清理错误信息** ，并**谨慎开启自动采集** 。

## 最后的判断

![](https://image.woshipm.com/wp-files/2026/09/20260909144207730205-19.png)

如果你只想给 AI 编程助手增加跨 Agent、跨会话记忆，agentmemory 是一个值得试用的开源项目。它的定位清晰，支持本地运行，也能通过 MCP 和 hooks 接入多个 Agent。相比面向完整上下文管理的 OpenViking，它更聚焦在会话记忆和工作经验的沉淀。

agentmemory 的优势，是定位明确、接入方式开放、支持本地运行，并且把捕获、整理、检索和注入串成了一条完整链路。它的代价也很明显：依赖 iii-engine，Windows 部署仍有门槛，自动采集还需要认真处理隐私和错误记忆。它更适合愿意折腾本地工具、长期使用 AI 编程助手的开发者。

我更愿意把 agentmemory 看成 AI 编程助手的“**工作记忆层** ”。

它保存的是长期信息，服务的却是每天的开发过程：项目为什么采用某种方案，某个 bug 曾经如何解决，一条命令为什么不能直接执行，某个文件里已经有哪些约定。

这些内容单独看都很琐碎，积累起来却决定了 Agent 能不能真正连续地工作。agentmemory 目前还不算开箱即用，尤其是 Windows 环境仍有一定部署门槛，自动采集也需要用户主动关注隐私和记忆质量。但对于已经长期使用 Claude Code、Cursor、Codex CLI 或 OpenCode 的开发者来说，它提供了一种值得尝试的思路。

**让 Agent 不只记住当前对话，也逐渐记住项目的工作方式。**

作者：AI李子 公众号：AI李子

本文由 @AI李子 原创发布于人人都是产品经理。未经作者许可，禁止转载

题图来自Unsplash，基于CC0协议


---
> 原文链接: https://www.woshipm.com/ai/6462278.html