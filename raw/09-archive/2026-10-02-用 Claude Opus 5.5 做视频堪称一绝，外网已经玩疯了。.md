---
title: "用 Claude Opus 5.5 做视频堪称一绝，外网已经玩疯了。"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6473114.html"
date: "Fri, 02 Oct 2026 07:57:26 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# 用 Claude Opus 5.5 做视频堪称一绝，外网已经玩疯了。

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6473114.html  
> **抓取日期**: 2026-10-02  
> **相关性评分**: 1.0

> 火起来的不是视频生成模型，而是让 Claude Code、Codex 这类工具写 HTML、Canvas 或 Remotion 动画，再逐帧导出 MP4，字幕、镜头和转场都在代码里调。文章整理了外网 10 支成品，又挑了五个能上手的开源项目。

![](https://image.woshipm.com/2024/03/05/8fa330e4-dae2-11ee-840e-00163e142b65.png)

好好好，Jev 模型和 GPT-6 做 3D 的爆火浪潮还没过去。

大家就研究出来**用Claude Opus 5.5 做视频。**

![](https://image.woshipm.com/wp-files/sha256/73/dc/73dc0a44a7101bb2b9e075f85b9ad25187adc6233d54b4f66c5de9ea176eb165.png)

![](https://image.woshipm.com/wp-files/sha256/d3/20/d320be7a6d658e1f4f783a4daf36e285ac57f574e7a2097628c2505f399c5a78.png)

这里提到的做视频不是 Seedance 这类模型的视频生成。

而是让 Claude Code、Codex 等 Agent 工具**编写 HTML、Canvas、WebGL 或 Remotion 动画，然后逐帧导出 MP4。**

字幕、镜头路径和转场都可以在代码里调整。

所以现在你应该能刷到很多用 Claude Opus 5.5 做的**产品发布片、动态图解，甚至五分钟的历史电影。**

模型的代码能力到了一个门槛，真的很多场景的可用性就很高了。

## 01 先看 10 支成品

### ① 小女孩问 Claude：你喜欢什么？

让 Opus 5.5 用 JavaScript 逐帧画出一支约 28 秒的手绘短片。

镇上的人不断向 Claude 提需求，一个女孩却问它喜欢什么。

画面随着回答切到大海、动物和星星，最后又回到女孩的窗前。

https://x.com/kevin_t_ngo/status/2102437977435893771

### 2\. 一个按钮，连续变成整支视频

给 Opus 5.5 的任务是用一个 HTML 文件拍完这支界面短片。

按钮先伸展成播放器，画面继续变为图表和命令面板，光标每次点击都推动下一次转场。

这个帖子的提示词还写明了逐帧计算和导出方法。

https://x.com/twoclipping/status/2103273003555402193

单个 HTML 页面用时间参数计算每一帧的元素位置和形状，因此任何时刻的画面都能准确重现。Playwright 截取浏览器画面，再由 FFmpeg 合成为视频。

### 3\. 镜头一路钻进 Blackwell 芯片

Lucian 做了一段约 49 秒的镜头，带观众从数据中心钻进服务器，再穿过芯片，直到原子尺度。

整个三维场景装在一个 HTML 文件里，由 Opus 5.5 编写的 Three.js 代码在浏览器中实时绘制。

https://x.com/lucian__03/status/2103494418477260830

原理就是 Three.js 实时渲染机房、服务器和芯片等三维场景，连续推进的镜头把不同尺度串成一次穿梭。

### 4\. 一张鸡尾酒图，变成 30 秒的调制动画

给模型一张参考图，让它用 HTML 把静态画面扩展成完整的调制过程。

配料逐步出现，画面同时标出步骤和用量。

提示词就在原帖。

https://x.com/Ror_Fly/status/2102853258582880547

核心原理就是参考图提供杯子、配料和文字的视觉样式，HTML 动画再按时间顺序展开调制步骤。

### 5\. 两分钟沙画，讲美国 250 年历史

这个是让 Opus 5.5 用两分钟沙画讲 250 年美国历史，再配上音乐和音效。

用代码把不同历史节点组织成一段连续的沙画叙事，并生成配乐与音效。

https://x.com/Michaelzsguo/status/2102592355165782312

### 6\. 一句需求，做出推理产品介绍片

让 Opus 5.5 给一家提供推理服务的创业公司做利落的介绍视频，得到约 26 秒的成片。

JavaScript 控制文字、图形和转场随时间变化，**再用 Playwright 和 FFmpeg 导出。**

https://x.com/deedydas/status/2102787937482252537

### 7\. 一支产品歌短片

这个是用 Opus 5.5 和 JavaScript 制作了约 28 秒的 Replit Animation 宣传片。

橙色图形和产品画面随着音乐切换。

Opus 5.5 **编写 JavaScript 来安排图形运动和剪辑节奏，Replit Animation 提供工程搭建与导出能力。**

https://x.com/samuel_spitz/status/2103293794594816100

### 8\. 五分钟的奥斯特里茨战役电影

五分钟的历史影片，WebGL 程序按照叙事时间线渲染战场和镜头运动，再把生成的声音、离线旁白与画面合成。

**镜头从地图推进到士兵行动，最后形成一支有叙事节奏的影片。**

https://github.com/WinterArc21/Battle-of-Austerlitz-Film

### 9\. 用剪纸动画解释相对论

日本创作者让 Opus 5.5 用 JavaScript 在 Canvas 上逐帧画出约 46 秒的相对论科普片，音乐和音效也由代码生成。

**剪纸般的纸片、星球和人物解释了双生子佯谬。**

https://x.com/masahirochaen/status/2102722719502704941

### 10\. 40 秒讲清浏览器怎样工作

Addy Osmani 让 Opus 5.5 用 JavaScript 逐帧**画出一支《浏览器如何工作》的解释动画。**

页面、网络请求和渲染过程被画成会动的图解。

https://x.com/addyosmani/status/2103009037164110327

## 02 相关开源项目

下面是我找到的几个 GitHub 上用 Opus 5.5 做视频的一些开源项目，有的是搞了一些风格，有的是有一些提示词开源的，你可以看一看了解一下。

### ① 30 种影片画面风格

![](https://image.woshipm.com/wp-files/sha256/67/6f/676fe77097ee7ff3713ab66c19e668678dc336413715c8dd310e2ee73beffe56.png)

Lemo-Opuscar 这个开源项目**收集了 39 种用 Opus 5.5 做成的影片风格** ，每一种都配有样片和说明。

先在样片库里挑一种喜欢的视觉效果，再把自己的主题交给它的 Skill。

![](https://image.woshipm.com/wp-files/sha256/02/0b/020b3613d9d3aa7c005cbc5b79b5ed7e6133764e2c92312a72418fbaf22e8255.png)

> 开源地址：https://github.com/lemomo-ai/lemo-opuscar

### ② Awesome-Opus5-5-Videos

还有一个很火的开源项目。

一共301 个 Opus 5.5 视频，开发者花了整整 $3000。

用 Claude Opus 5.5 把全网最难、最火的特效重新做了一遍。

所有测试视频、全套 Prompt 和工作流，全部整理开源。

![](https://image.woshipm.com/wp-files/sha256/c7/0f/c70f221c321a70c36f002e1b7a022ce59e028a7d52792779079bde54eec409b0.png)

> 地址：https://github.com/yihui-dev/awesome-opus5-5-videos

### ③ 提示词大合集

这个开源项目是 Opus 5.5 视频**提示词合集。**

它把不同作者的成片和提示词放在一起，方便顺着喜欢的视频找写法。

![](https://image.woshipm.com/wp-files/sha256/60/df/60df6b855ec155d2c6f56cbcba87fe2714db512ea7114ddf78e7a762b7263de7.png)

![](https://image.woshipm.com/wp-files/sha256/fd/99/fd998b0e12782c36b62bf70e19218fcd7adfdf272a9220830f8c713acea69d78.png)

> 开源地址：https://github.com/joeseesun/opus-video-prompts

### ④ 想把镜头和转场做得更顺

OneTake 收集了一镜到底产品视频的动作和制作拆解，还提供可复用的 Skill。

![](https://image.woshipm.com/wp-files/sha256/b1/17/b117d0ff384597e23043ea57d699a9269450a43652016d49cb64882d675fd938.png)

如果你想用 Claude Code 生成下面这种视频的话，可以研究研究这个开源项目。

![](https://image.woshipm.com/wp-files/sha256/64/d6/64d6a3a41ba8d5083b2189ead89644a1125dc31903bc59b07e1d4d43ffe9b55e.gif)

> 地址：https://github.com/feitangyuan/onetake

### ⑤两个老牌的项目

**HyperFrames** 可以把 HTML 动画渲染成视频。**Remotion** 官方 Agent Skills则教 Agent 用 React 代码制作、预览和导出视频。

这两个 skill 是 GitHub 上比较火的让 AI 通过 Coding 方式做视频的高赞项目。

地址：https://github.com/heygen-com/hyperframes

地址：https://github.com/remotion-dev/skills

另外还有其它 AI Coding 的方式生成视频的 Case 或项目。

作者：逛逛GitHub 公众号：逛逛GitHub

本文由 @逛逛GitHub 原创发布于人人都是产品经理。未经作者许可，禁止转载

题图来自 Unsplash，基于CC0协议


---
> 原文链接: https://www.woshipm.com/ai/6473114.html