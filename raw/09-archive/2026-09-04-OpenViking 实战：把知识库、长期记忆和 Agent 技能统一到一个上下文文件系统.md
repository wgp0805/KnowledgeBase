---
title: "OpenViking 实战：把知识库、长期记忆和 Agent 技能统一到一个上下文文件系统"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6459718.html"
date: "Fri, 04 Sep 2026 09:17:06 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# OpenViking 实战：把知识库、长期记忆和 Agent 技能统一到一个上下文文件系统

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6459718.html  
> **抓取日期**: 2026-09-04  
> **相关性评分**: 1.0

> 火山引擎开源OpenViking，以虚拟文件系统统一知识库、记忆与技能，通过L0/L1/L2分层加载优化Agent上下文检索。本文详解其设计思路、部署流程及Claude Code等工具接入实测，展示如何提升Agent信息利用效率。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/3722e408b19ec5e72e75f58a3340a8e8_MD5.png)

最近在整理 Agent 的知识库和长期记忆时，我发现一个很有意思的开源项目：**OpenViking** 。它来自火山引擎团队，定位是面向 AI Agent 的开源上下文数据库——解决一个越来越明显的问题：资料、记忆、技能和项目文件分散在不同工具里，Agent 虽然“能搜到”，却未必知道应该先看什么、为什么找到这些内容。我用它搭了本地知识库，又接入了 Claude Code、WorkBuddy、Cherry Studio，实际体验下来，它更像一套 Agent 的上下文基础设施，而不只是一个向量数据库。

项目地址：github.com/volcengine/OpenViking

## 01 OpenViking到底是什么？

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/8716460de9baecfd99430e1ac697b862_MD5.png)

OpenViking 把三类内容统一放进一个虚拟文件系统：

  1. Resources · 知识资料：项目文档、网页、代码和其他知识资料，是 Agent 工作时的“参考资料库”。
  2. Memories · 用户记忆：用户偏好、历史事件、实体信息和 Agent 经验，跨会话长期存在。
  3. Skills · 技能工作流：Agent 可以按需调用的技能和工作流，多个 Agent 共享同一套定义。



这些内容使用 viking:// URI 统一表示。对 Agent 来说，它们不再是散落在向量库、Markdown 文件和插件配置里的几套数据，而是可以通过类似文件系统的方式浏览、搜索和读取的上下文资源：

> viking://
> 
> ├── resources/
> 
> │ └── my_project/
> 
> │ ├── docs/
> 
> │ └── src/
> 
> └── user/
> 
> └── default/
> 
> ├── memories/
> 
> ├── resources/
> 
> └── skills/

这个设计有一个重要变化：Agent 检索内容时，可以先浏览目录和结构，再逐步深入具体文件。官方文档把这种方式称为“面向上下文的文件系统范式”。

## 02 传统 RAG 的问题，究竟出在哪里？

传统 RAG 通常会经历这样的流程：

**文档切块 → 向量化 → 相似度检索 → 拼接结果 → 交给模型**

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/79e68f0d8df1dd744452fb5155eff959_MD5.png)

这套流程很成熟，但在知识量增加、任务变复杂之后，几个问题会逐渐暴露出来。

  * 结构丢失：文档被切成片段后，原有的目录结构和上下文关系容易丢失。模型拿到几段相似文本，却未必知道它们属于哪个章节、哪个项目，甚至无法判断内容是否完整。
  * 检索不可观察：结果不准确时，我们看到的通常只有最终召回片段，很难知道是哪个目录、哪个阶段或哪一次筛选导致了偏差。
  * Token 与费用：所有候选内容都直接进入上下文，会增加输入 Token、延迟和费用。对于长文档、代码仓库和多轮 Agent 任务，这个问题尤其明显。
  * 多系统分散：知识库、用户记忆和技能往往由不同系统分别管理。Agent 需要同时适配多个接口，开发者也要维护多套同步和更新机制。



**OpenViking 的思路** 是先建立内容结构，再让 Agent 根据任务逐层读取。

## 03 L0、L1、L2：先看目录，再读正文

像查书一样：摘要 → 概览 → 正文

OpenViking 会为内容生成三层上下文：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/1e91c3c8c70128bfc5c90d4e6620a6ea_MD5.png)

可以把它理解成查阅一本书：Agent 第一步只看摘要，判断哪些目录值得关注；第二步读取概览，了解章节结构和关键信息；只有任务确实需要时，才加载完整正文。目录本身也可以拥有摘要和概览，因此 Agent 可以先从较高层级规划路径，再深入到具体文件。

  * L0 摘要层：判断哪些目录值得关注，最轻量
  * L1概览层：章节结构与关键信息，按需加载
  * L2完整正文：原始数据保留在这里，任务确实需要才读



这里有一个容易误解的地方：L0 和 L1 并不会替代原始内容。它们更接近导航和筛选层，原始数据仍然保留在 L2 中，按需读取。

这种分层机制主要带来三点价值：

  1. 减少无关内容进入上下文
  2. 让检索过程更接近人类浏览资料的方式
  3. 保留从目录到文件的检索轨迹，方便排查问题



OpenViking 官方还强调了“可观察检索”。当一次召回结果不理想时，可以查看 Agent 经过了哪些目录和路径，而不是只能猜测向量搜索为什么返回了某段内容。

## 04 部署前需要准备什么？

OpenViking 需要模型参与内容处理和检索，所以部署前要备好三样东西：

  1. Python 3.10+ 或更高版本
  2. 一个用于生成摘要、概览和规划的语言模型或视觉语言模型
  3. 一个嵌入模型



如果资料里包含图片、扫描 PDF 或其他多模态内容，使用视觉语言模型会更合适。纯文本知识库则可以根据成本、速度和效果选择普通语言模型。

## 05 安装 OpenViking

在终端执行：

> pip install openviking –upgrade

然后初始化配置：

> openviking-server init

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/b1f640f7fb0f19202dbcb2af2e29c985_MD5.png)

初始化向导会依次引导你配置模型提供商、嵌入模型、存储位置和服务参数。我的配置方式是调用云端模型，因此在向导中选择了 API 模式。如果你希望完全本地运行，也可以选择本地模型方案——具体能否顺利运行，取决于电脑的显卡、内存和模型要求。

### Step 1 配置嵌入模型

嵌入模型负责把文本或其他内容转换为向量，用于后续的语义检索。我这里使用的是讯飞 MaaS 提供的 Qwen3-Embedding-8B——之前和大家分享过，目前可以免费调用。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/1abdb0d444f6c6f1edc7e442f752b25d_MD5.png)

### Step 2 配置生成模型

生成模型用于内容解析、摘要生成、概览生成和查询规划等环节。如果知识库包含图片、截图或扫描文档，视觉语言模型会更有优势；只处理普通文本时，使用常规 LLM 也可以满足基本需求。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/6e38a1e4db0bc298e1760364983f7ce6_MD5.png)

### Step 3 配置查询规划

查询规划器用于辅助拆解用户问题，并为后续的上下文浏览和检索提供规划。我使用的是云端模型，因此在初始化时没有启用本地查询规划器；使用本地模型时，可以根据设备性能和实际效果决定是否开启。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/a79f45bf1a27e57e0154d045f0ec499e_MD5.png)

然后就是选择本地地址、选择默认端口、保存配置即可。接下来是验证，相当于执行 openviking-server doctor：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/1e6c93254487dd1cc8bfc377fe56d41a_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/8219e330770aa0a7e6124bc9d968ca80_MD5.png)

如果检查结果全部正常，就可以选择 Y 启动服务。如果有问题，调整好之后，执行：

> openviking-server

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/5be24602675ac91fc53c536f6a1aba1a_MD5.png)

启动后，在浏览器打开：

> http://127.0.0.1:1933/

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/44705fcea27439341e81ad645abd5a36_MD5.png)

到这里，OpenViking 服务端已经运行起来了。

## 06 创建第一个知识库

在工作台中点击新增按钮：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/c8b4a3f07b3ec3c0ff6217013cee205c_MD5.png)

OpenViking 支持导入文件、目录和部分远程资源。我的示例是建立一个“统计学”知识库：先指定目标路径，再上传资料，最后点击开始处理。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/6184bd2b39edbfcb4e737f4e6b967dcb_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/b72a240dfc4981de3b01df184b621e0e_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/70529ec3c7035f3f18e1ed22f128f92e_MD5.png)

处理完成后，页面会显示导入状态。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/1ba838040fd39599667026067beb5341_MD5.png)

回到根目录，就能看到刚刚建立的资源目录。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/97725169560e30b3797ada8e896e715e_MD5.png)

## 07 启动 VikingBot，对话式使用知识库

加个 –with-bot 参数就行

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/5b0a14d97306dd69c2c5fb760bf0380e_MD5.png)

第一次启动服务时，如果没有加 Bot 参数，工作台里可能还没有对话入口。先在终端按下 Ctrl + C 停止当前服务，然后执行：

> openviking-server –with-bot

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/2b3256a1f627835cc59cedfb3305d892_MD5.png)

启动成功后，就可以直接在工作台中对话。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/cadbfceea90bd11c11e3dd3ca470a6c2_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/4bbfaff870b309107f0b224ea112f820_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/6bc493262599f93d0c7706caaea68827_MD5.png)

和 Bot 的对话全部都会显示在会话中，你也可以在会话中新建。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/adaa63f28589cdc0bb126a4a627184e8_MD5.png)

## 08 用户记忆：多 Agent 共享同一套上下文

一个 Agent 记下的，其他 Agent 也能用

OpenViking 把用户记忆放在用户上下文空间中，并通过 OpenViking 的API、MCP 和 Agent 集成能力提供访问：

> viking://user/default/

用户记忆可以包含：

  * 用户偏好
  * 重要事件
  * 常用实体
  * Agent 工作经验
  * 已确认的长期信息



这些内容可以被不同 Agent 共享，从而减少重复配置。一个 Agent 中记录的偏好，在其他接入同一 OpenViking 服务的 Agent 中也有机会被检索到。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/f092d614778ae62484989a294bcc5b79_MD5.png)

## 09 用 Helper 管理记忆和技能

OpenViking 官方提供了 **OpenViking Helper** ，支持 macOS 和 Windows x64。它主要解决三类问题：

  1. 配置 OpenViking 服务连接
  2. 安装和检查 Agent 集成
  3. 查看会话、记忆和技能的同步状态



Helper 可以检测本机安装的 Claude Code、Codex、Cursor、TRAE 和 OpenCode，并根据对应集成方式配置插件、MCP、Hook 或 CLI。在项目首页下载即可：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/216c4d8a1638d33d4233c419cca24e62_MD5.png)

装完成后，在配置页面填写本地服务地址：

> http://127.0.0.1:1933

本地 dev 无鉴权模式下，服务端不校验密钥，随便填写一个非空字符串即可。AgentID 字段是用来标识不同调用方、方便排障的，普通使用直接留空即可，不用填写。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/06bd3ca4f5300d2a89bf251561f228c7_MD5.png)

进入 Agent 插件页面后，Helper 会列出本机检测到的 Agent。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/6e0b4256b29d391ca1900d7df0cce41b_MD5.png)

Helper 不只是“帮你写配置文件”。它还能查看部分 Agent 会话中的 OpenViking 活动，例如记忆召回、上下文注入、MCP 调用、对话捕获和会话提交。这对于排查“插件装上了但似乎没有生效”的问题很有帮助。

### Step 1 查看资源、记忆和技能

连接本地服务后，可以在 Helper 中看到相应目录：

  * **User** ：通常对应用户上下文和个性化记忆
  * **Resources** ：对应知识库和项目资料
  * **Skills** ：对应可复用的 Agent 技能



![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/a9d6ec9f7970d7e7c5bf0616ade450db_MD5.png)

Helper 会把本地 Agent 的相关记录列出来，你可以选择哪些内容同步到 OpenViking。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/a2f421ef497ce3c985bdf4bce42a0424_MD5.png)

记忆功能中也一样，会查询到你所有的记忆，你可以根据实际情况进行同步。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/8655f7202203cbbb52177b4f552ca2df_MD5.png)

完成同步后，记忆可以被连接到同一服务的其他 Agent 使用。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/290eb56a982eb7febbe4a9bbe2f0fc4d_MD5.png)

### Step 2 技能也可以统一管理

除了记忆，OpenViking 还可以管理 Agent 技能。将本地 Agent 的 SKILL.md 或相关技能目录同步到 OpenViking 后，技能会进入用户上下文空间的 Skills 目录。这样，多个 Agent 可以共享同一套技能定义，减少重复安装和维护。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/24214164e5aefc516e924f34b7098431_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/ff2cfd3652962c81ce13274d827be6ab_MD5.png)

另外补充一点：OpenViking Helper 这个官方客户端管理配置很方便，许多原本需要通过命令或配置文件完成的操作，也可以在这里进行。比如我在这里建立另外一个知识库，也很方便——在 Resources 下添加文件、文件夹，它会自动给你建立目录。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/7892f59d7ac90001aeb746ea8e384c30_MD5.png)

添加文件夹：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/6e243e8ef2abee171ab783b669a01a14_MD5.png)

下面是添加完成后的效果：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/1804318918a6791808ee85ff9f5d6955_MD5.png)

基本核心功能就说完了。

## 10 用 Claude Code 调用知识库和记忆

还有 Cherry Studio 和 WorkBuddy

在 Helper 中完成 Claude Code 集成后，重启 Claude Code。刚才在配置向导过程中我已经安装了 Claude Code 插件：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/e451e196494742ec76325730f3d3c1b8_MD5.png)

在 Claude Code 中验证一下：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/c572021f9af6b9e21580bc9438371c9e_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/af51d7977e117f996981bbebf0bcbe8f_MD5.png)

测试召回记忆——这里我用的是卡神之前分享的 claude.md 文档来测试召回：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/1d7b25f21add1403dcd4ec87ca317fc1_MD5.png)

知识库的使用也很流畅：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/8875862ff8f7ead22fb6e5dd35afdd50_MD5.png)

### Cherry Studio 通过 MCP 接入

OpenViking Helper 当前主要面向本地 Agent 的配置和管理。Cherry Studio、WorkBuddy 等工具，可以通过MCP 接入 OpenViking。在 Cherry Studio 的 MCP 设置中添加 OpenViking 服务，然后启用对应工具。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/df0adafe2c45e72d4bc2fe3927fdcca9_MD5.png)

启用后，可以先测试普通对话，再测试知识库检索。

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/3ac1fd7090d99d64d197c3f9ee9692e3_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/8676765e4cfbdda982515ee438fc694a_MD5.png)

### WorkBuddy 同样走 MCP

WorkBuddy 同样可以通过 MCP 调用 OpenViking。将服务配置添加到 MCP 中并启用：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/fddc3f434808bc582b0711fe2282ace8_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/982dd27ba3658e5d53eb201b2b14f558_MD5.png)

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/759b938baa01d72c0f69a35313fe2582_MD5.png)

然后测试它能否检索“统计学”知识库中的内容：

![](assets/2026-09-04-OpenViking%20%E5%AE%9E%E6%88%98%EF%BC%9A%E6%8A%8A%E7%9F%A5%E8%AF%86%E5%BA%93%E3%80%81%E9%95%BF%E6%9C%9F%E8%AE%B0%E5%BF%86%E5%92%8C%20Agent%20%E6%8A%80%E8%83%BD%E7%BB%9F%E4%B8%80%E5%88%B0%E4%B8%80%E4%B8%AA%E4%B8%8A%E4%B8%8B%E6%96%87%E6%96%87%E4%BB%B6%E7%B3%BB%E7%BB%9F/efde72c17fedd56fa9a09996c265ab1e_MD5.png)

> 提示：
> 
> MCP 连接成功并不代表模型一定会主动调用知识库。测试时，问题最好明确指定资料范围，例如“请根据统计学知识库回答……”，并检查客户端是否实际调用了对应工具。

## 我的实际感受

OpenViking 最值得关注的地方，在于它重新组织了 Agent 使用上下文的方式。它把知识资料、用户记忆和技能放进统一的上下文空间，再通过目录结构、分层加载和可观察检索，让 Agent 逐步判断哪些内容值得读取。

这套设计对三类场景尤其有价值：需要长期维护的个人知识库、同时使用多个 Agent 工具的开发者，以及希望把用户偏好、项目资料和工作技能统一管理的团队。当然，它仍然处于快速迭代阶段，不同版本的命令、配置项和 Agent 集成方式可能发生变化，部署时最好以官方仓库和文档为准；知识库质量也不会因为换了工具就自动提升，资料结构、命名方式、更新机制和记忆筛选仍然需要认真设计。

作者：AI李子 公众号：AI李子

本文由 @AI李子 原创发布于人人都是产品经理。未经作者许可，禁止转载

题图来自Unsplash，基于CC0协议


---
> 原文链接: https://www.woshipm.com/ai/6459718.html