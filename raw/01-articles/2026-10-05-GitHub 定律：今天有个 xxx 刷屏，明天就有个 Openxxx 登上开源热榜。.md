---
title: "GitHub 定律：今天有个 xxx 刷屏，明天就有个 Openxxx 登上开源热榜。"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6473633.html"
date: "Mon, 05 Oct 2026 05:07:41 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# GitHub 定律：今天有个 xxx 刷屏，明天就有个 Openxxx 登上开源热榜。

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6473633.html  
> **抓取日期**: 2026-10-05  
> **相关性评分**: 1.0

> 一个产品刚刷屏，第二天开源社区里就可能冒出一个复刻版——过去三年这几乎成了固定节目。文章沿着时间轴，从 2023 年的对话产品讲到今天的 Agent 热潮，盘点那些爆火产品后来都带出了哪些开源方案。

![](https://image.woshipm.com/2023/04/14/91d2911a-da9e-11ed-95a1-00163e0b5ff3.png)

现在，做一个产品 Demo 确实简单很多了。

现在什么产品火了，稍微拆解一下它的技术路线，找找有哪些开源的组件能攒一攒。

然后把能找到围绕这个爆火产品相关的重要 Context 一同丢给 Codex。

打开 GPT 6 Astra Ultra，多聊几轮，**一个开源复刻就出来了。**

![](https://image.woshipm.com/wp-files/sha256/0b/cb/0bcb2f77af39f303a0c864360bcc5818de97ff87fce4506ea31782b2aa34817e.png)

于是，有一个很好玩的现象。

我叫他 **AI 时代的 GitHub 定律** ：**今天，一个叫 xxx 的产品刚刚刷屏。明天，GitHub 上很可能就会冒出一个 Openxxx。**

![](https://image.woshipm.com/wp-files/sha256/4b/b6/4bb693416bd094d537b78e43bbe74939d29b1c84f6017b039d7adc7f54c5eb0b.png)

开源版本紧跟着出现，冲上 GitHub 热榜。

然后轮到公众号、X、科技媒体和小红书接力，标题大概是：大厂刚发布，开源平替已经来了。

过去 3 年，仿佛一直在上演这出固定节目。

原本只有少数团队能做的产品，**现在有更多人可以动手验证。**

**开源版本也给大家多了一种选择，很多新想法正是在互相跟进和不断改进里，慢慢变成了一个真正的产品方向。**

下面就沿着时间轴捋一遍：**从 2023 年到今天，那些曾经刷屏的 AI 产品，后来都带出了哪些开源复刻。**

## 01 2023：ChatGPT 把门打开了

**ChatGPT** 发布于 2022 年底，到了 2023 年，它的影响已经从科技圈扩散到大量普通用户。

![](https://image.woshipm.com/wp-files/sha256/ce/52/ce52e22e5be02c5429dd87cf57af8dad82157e2116e044f223ea60177c8f6d1b.png)

大家第一次直观感受到，聊天框背后的 AI 已经能写文章、整理资料、回答问题。

还能帮人做出一个像模像样的产品。

不知道大家还记不记得， **ChatGPT** 没多久。

GitHub 很快出现了第一轮开放版本，就是清华团队的 **ChatGLM-6B** ， 主打中英双语和本地运行。

![](https://image.woshipm.com/wp-files/sha256/24/32/2432f5bc9f42b42f2fc142aca0e89be724c9a6ff8fe02e578ac20a0f11a7dd13.png)

与此同时，**Chatbot UI** 等项目把 ChatGPT 那套熟悉的聊天界面也做了出来。

一个纯 UI 的开源项目现在都还有 3 万 Star，虽然 3 年已经没有更新。

![](https://image.woshipm.com/wp-files/sha256/e1/54/e154b9eca1343c8de889ee5da21cbb785cb17c5f1355e0d239b2b22259f20c5c.png)

因为在当时 AI Coding 的能力并没有那么强，不像现在，你想复刻什么 UI，一句话的事，Codex 跑个半小时就能复刻完了。

当时可能**还需要老艺术家手搓实现。**

所以在 AI 大模型前时代，确实有很多前端 UI 类的开源项目很火。现在就不会了。

模型、界面和本地部署凑齐之后，民间版 ChatGPT 开始批量出现。

这一年的另一个代表是 **Code Interpreter** 。

OpenAI 让 ChatGPT 可以读取文件、分析数据和运行代码后，**Open Interpreter** 很快给出了一个可以在个人电脑上运行的开放版本。

接着，**AutoGPT、BabyAGI** 和 **MetaGPT** 等项目接连走红。

![](https://image.woshipm.com/wp-files/sha256/94/5c/945c62ec23922397baad85d49626eff7d9e2c894ba37382f36285958719de649.png)  
![](https://image.woshipm.com/wp-files/sha256/8b/bf/8bbfcc4acb5a23d45f05bfaf9ff22484167578d07cf3d099f2c094641fbcbaed.png)  
![](https://image.woshipm.com/wp-files/sha256/bf/ce/bfce3fd7c69310409badeafd3b6ece8a4b877d88f7e0b6586a74f9c971fb2719.png)

它们尝试让 AI 自己拆解目标，一步步完成任务，也提前准备好了后来复刻 Devin、Manus 所需的许多零件。

## 02 2024：开始出现牛逼的 AI 应用

2024 年 2 月，OpenAI 公布 **Sora** 。

那时候感觉这玩意像黑科技一样。普通用户还用不上，网上已经被它生成的视频刷屏。

5 天后，**Open-Sora** 开源了，它想做一个任何人都能研究和使用的视频生成方案。

![](https://image.woshipm.com/wp-files/sha256/51/cf/51cfd9947ef56d0aeab7b3d5de106a41005635f003041f42b91f91e2323609d2.png)

3 月，发布 **Devin** 了，把它称作 AI 软件工程师。

第二天，**OpenDevin** 就开源了，不过后来更名为 **OpenHands** 。

我截屏一下这个项目的主页，你就知道是哪个开源项目了。

![](https://image.woshipm.com/wp-files/sha256/f3/36/f336c84016a07fe8523c9e1f00aeba269ea22295e6631bbb664490e6ff198ab4.png)

OpenHands 可以读取项目、修改文件和运行任务，让更多人尝试 Devin 展示的工作方式。

同一时期，**Perplexity** 也很火。

毕竟 AI 前期很好落地的场景就是信息获取。

**Perplexity** 带火了会搜索、会总结、还能附上来源的 AI 搜索产品。

**Perplexica** 随后成为热门开源替代，后来好像更名为 **Vane** 了。

![](https://image.woshipm.com/wp-files/sha256/f0/07/f00720e293d85f2e63319d0e95aa7044b0bf47c257f5a172bc9c8c833561353d.png)

**Cursor** 在这一年成为热门 AI 编辑器。

**Void** 随后以开源替代品的定位出现。

用这个编辑器可以自由选择不同的 AI，也可以把更多内容留在自己的电脑上。

不过到目前，今年 3 月份 **Void** 已经停止维护了。

![](https://image.woshipm.com/wp-files/sha256/b5/3a/b53aa45cfd9b7d16a302ebc964707abb3d5c84b665c01d858fe87a3432c50920.png)

2024 年，还有一个产品很火，叫 **NotebookLM** 。

它的双人播客功能在 2024 年秋天突然刷屏。

上传一堆资料，两位 AI 主播就能把内容聊成一期节目。

**Open Notebook** 在当年 10 月出现了，把资料问答和播客生成做成了可以自行搭建的版本。

我之前还专门写过一篇文章，盘点 **NotebookLM** 的开源平替呢：Google 神级生产力工具，所有 GitHub 开源平替都找到了。

![](https://image.woshipm.com/wp-files/sha256/4a/36/4a36cd48cbae7f512b07593409d33a10131f9027f95f23be6f169d1ce8b823af.png)

## 03 2025： 所谓的 Agent 元年

时间来到了 2025 年。

Gemini 和 OpenAI 相继推出 **Deep Research** 后，能自动搜索大量网页、整理资料并写出报告的产品成了新热点。

不过这一次，开源社区甚至抢跑了：LangChain 的 **Open Deep Research** 在 2024 年 11 月就开源了。

早于 Gemini 和 OpenAI 的同名产品发布。

不过现在这个开源项目已经不维护了。

![](https://image.woshipm.com/wp-files/sha256/14/b6/14b65ae712aeb030c6e014dd2f127ba3b12ad562b7152bb12d20a91a1d1f32b3.png)

后来商业产品走红，这类开源方案也跟着被更多人看到。

**Deep Research** 很快从一个功能名，变成了一整类产品的名字。

真正把 GitHub 定律推到极致的，还是 **Manus** 。

![](https://image.woshipm.com/wp-files/sha256/ed/be/edbef143a263caa1a3bbc570903498487c57c3865b3c5678835e75cc5ac1200e.png)

2025 年 3 月，**Manus** 刷屏，邀请码一度被炒成稀缺品。

很多人还在排队等资格，**OpenManus** 已经出现在 GitHub。

![](https://image.woshipm.com/wp-files/sha256/2a/f3/2af38d2d7e13605a7259f36df5ba8fc725a80c2a174bd287e06ea7ac28175fae.png)

开源时间和 Manus 发布是同一天，我记得当时团队说最早的版本只用了大约 3 个小时。

3 个小时做出来的 **OpenManus** 只是一个可运行的早期版本，和 Manus 的完整能力仍有距离。

把已经成熟的 AI、网页操作和任务执行能力组合起来，先让大家看到大致思路。

**Manus** 走红还带火了 OWL 等原有项目。

OWL 背后的团队此前已经积累了相关能力，项目也有自己的发展路线。

热点到来后，老项目找到了新的介绍方式，也被更多人看到。

随后，**Lovable、v0** 和 **Bolt** 让说一句话生成应用成为热门赛道。

**Open Lovable** 可以参考一个现有网站，快速做出可编辑的网页版本。

![](https://image.woshipm.com/wp-files/sha256/b1/db/b1dbc8d4a4faef002a42420e56c9466c229bf5ba9256d51b223696fa24c77466.png)

## 04 2026：产品发布和开源复刻开始按天计算了

**Claude Design** 在 2026 年 4 月发布后，大约十来天，**OpenDesign** 出现。

它可以连接不同的 Agent ，根据文字要求生成网页、PPT 和设计素材，并把文件留在用户自己的电脑上。

![](https://image.woshipm.com/wp-files/sha256/62/72/6272c8bcf399cfffdd11657bc039dbc596ccd67f087b4b22f1efddfdf45c40b8.png)

9 月 8 日，Meta 推出个人 AI 助手 **Muse** 。

![Chatting with Muse via mobile or Mac](https://image.woshipm.com/wp-files/sha256/03/67/0367a371902f5a7fae34a288221cc36e94de4a6078fc0ddce20924796c7921d4.jpg)

它能打开网页、填写表单，还可以在用户离开后继续完成任务。7 天后，**OpenMuse** 就出来了，提供了相似的个人 Agent 工作方式。

![](https://image.woshipm.com/wp-files/sha256/57/7e/577e3a5cb6f82054d8f0d17158c17c4f8f940ad5063eaa4df3bf58b4b897de38.png)

9 月 15 日，TypeSafe AI 发布 **Jev** 。

它不负责陪人聊天，主要任务是读取现有信息，然后快速给出选择、评分和概率，方便其他软件继续处理。

![](https://image.woshipm.com/wp-files/sha256/57/7e/577ef4ab54aa9890b683271523e5e8b91eceeb0d23bb55fbcc02c1dccb8a0e91.png)

第二天，**Open JEV** 出现了。

几天后，Laya 也开源了，我之前还单独有一个文章介绍过这个 **Laya** 。

说是在精度、速度、校准、多语言覆盖和成本五个维度全面优于 **Jev** 。

![图片](https://image.woshipm.com/wp-files/sha256/68/c5/68c5b3dad0d1e3101420f8411fa968f046b9626eeeb0de063d0f3e151004f2c2.png)

当复刻变得越来越容易，产品的物理实体（代码）已经不再是最稀缺的了。

至少在现阶段，真正拉开产品差距的，**可能是实现之前的判断，以及产品上线之后的运营/渠道。**

首先是判断力。

它不仅体现在解决问题的能力上，更体现在能否发现并定义一个新问题，以及能否真正理解这个问题。

比如 OpenClaw 刚发布时，主打的是 **Personal AI** 。半年之后，最初的热度逐渐退去，Muse 又带着一款体验更流畅、打磨更完善的 **Personal Agent** 来到市场。

看起来是在做相似的事情，但对需求、时机和产品形态的不同判断，最终会导向完全不同的产品。

判断力之外，还有所谓的**品味与取舍。**

在 AI 的加持下，同一个品类可以不断叠加各种功能，做加法变得前所未有地容易。

但什么该做、什么不该做，如何保持克制，让产品始终围绕核心价值展开，**反而更加考验创造者的判断与品味。**

再往后，真正决定产品能否长期生存的，就是渠道、信任，以及持续运营的能力。

这也解释了为什么越来越多独立开发者会同步经营自己的自媒体账号：**他们不仅是在为产品寻找流量，也是在长期建立个人信用、用户关系和稳定的分发渠道。**

当产品越来越容易被复制，真正难以复刻的，或许正是这些代码之外的东西。

作者：逛逛GitHub 公众号：逛逛GitHub

本文由 @逛逛GitHub 原创发布于人人都是产品经理。未经作者许可，禁止转载

题图来自 Unsplash，基于CC0协议


---
> 原文链接: https://www.woshipm.com/ai/6473633.html