---
title: "斩获14k+Star，把OpenClaw+Claude Code等多个Agent装进一个UI。"
source: "https://mp.weixin.qq.com/s/Mt7AkhdDheR_tjUH25NtZA"
---
沉默王二 沉默王二 *2026年2月11日 11:25*

大家好，我是二哥呀。

这两天，GitHub 上有一个项目在疯狂刷屏。

AionUi。

一个免费、开源、本地的多 AI Agent 桌面应用，短短一个月就在 GitHub 上斩获了 **14.2k+ Star** ，并且多次登上 GitHub Trending 榜单。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/3abcf432efdcb47fb768a98ff60e4e31_MD5.webp)

说实话，第一眼看到这个项目的时候，我愣了一下。

这不是就是 Claude Cowork 的开源平替吗？

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/7ee4b42f9580f7cc394be8ad1f18a9f9_MD5.webp)

要知道，Anthropic 官方的 Claude Cowork 只支持 macOS 和 Claude 模型。

除了可以作为 Cowork 来用，AionUi 还支持 Gemini CLI、Claude Code、Codex、Qwen Code、Goose CLI、OpenClaw 等主流的命令行 AI 工具，更是横跨 macOS、Windows、Linux 三大平台。

对于需要开多个 AI 工具的小伙伴来说，简直不要太爽。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/c2cc9c7c5b1a0b92dd4ddf17df62e161_MD5.png)

更狠的是，AionUi 还内置了很多专业助手，从文件管理到 PPT 生成，从 PDF 转换到 UI 设计，几乎把 AI 办公+编程自动化这条路给跑通了。

如果你觉得助手的功能不够用，还可以给 AionUi 添加 Skills 扩展能力边界。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/c6e90ae8184421b13bb77ab9cdfc6bc8_MD5.png)

接下来，我就带大家实测一下这个杀疯了的开源项目。

## 01、一键安装，开箱即用

AionUi 的安装非常简单，直接去 GitHub Releases 下载最新版本就可以了。

支持 macOS 10.15+、Windows 10+、Linux Ubuntu 18.04+，内存推荐 4GB 以上。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/7b38986202d6c2efae5be7e8186180ce_MD5.jpg)

> 下载地址： [https://github.com/iOfficeAI/AionUi/releases](https://github.com/iOfficeAI/AionUi/releases)

如果你是 macOS，且安装了 Homebrew，还可以直接用这行命令来安装：

```
brew install aionui
```

很快，就搞定了。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/4948ab6033bce218ce73264ba9721a26_MD5.png)

安装完成后，第一次打开 AionUi，你会发现它已经内置了 Gemini CLI，官方称不需要任何额外配置就可以直接使用。

我没成功，可能是我多个 Google 账号之间登录的 IP 污染了，一直授权不成功。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/0cd6f7551ef2a5347c00c21bfadc123c_MD5.png)

不过不用担心，我们还可以配置自己的 API Key。AionUi 支持绝大多数主流的 AI 模型：

- Gemini（Google 账号登录或 API Key）
- OpenAI（API Key）
- Claude（API Key）
- Qwen（通义千问）
- DeepSeek
- 本地模型（Ollama、LM Studio）
- 等等

实际测试下来，比如说Poe这个代理，我一直拉不出来模型，也不知道为啥。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/e7c74f983c8b07f33498c8be59e82553_MD5.png)

我暂时只配置了 OpenRouter 路由的 Claude Opus 4.6、Gemini 3 Pro-image 和 [GLM-4.7。](http://GLM-4.7。)

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/9bd95bf5a04be9f9e6ab2a9c00a80b27_MD5.png)

配置完成后，我们就可以开始体验了。

## 02、多 Agent 协同，统一管理

AionUi 最大的卖点，就是它的多 Agent 模式。

简单来说，你可以把 Gemini CLI、Claude Code、Codex、Qwen Code 这些命令行 AI 工具，全部整合到一个图形界面里，统一管理。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/7ddb1551141bd4ede088c5dffd99cd83_MD5.gif)

这意味着什么？

意味着你不再需要在终端里敲命令，不再需要记忆复杂的 CLI 参数，不再需要在多个工具之间来回切换。

所有的一切，都在一个界面里完成。

而且，AionUi 还支持多会话并行。你可以同时开启多个对话，每个会话都有独立的上下文记忆，互不干扰。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/aa8748779666eccdfacae9574356c04c_MD5.png)

对于我这种经常需要同时处理多个任务的人来说，这个功能简直太实用了。

一边 Vibe Coding，一边写教程，还能随时切换不同的 AI 模型，效率直接拉满。

## 03、WebUI 远程访问，随时随地

AionUi 另一个让我惊艳的功能，是它的 WebUI 远程访问。

简单来说，你可以在服务器上运行 AionUi，然后通过浏览器从任何设备访问——手机、平板、电脑，统统支持。

AionUi 支持局域网、跨网络和服务器部署。可以通过扫描二维码或账号密码登录，操作简单方便。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/731aeb4893313b4882cc9c4d1da483f1_MD5.png)

这样我们就可以在公司电脑上配置好 AionUi，回家后用平板继续使用；或者把 AionUi 部署在服务器上，随时随地通过手机访问 AI 助手。

和最近疯狂刷屏的 OpenClaw 是一个道理。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/8c1b822e8379a393744db97c77fbacc0_MD5.png)

我试了一下局域网，从手机访问 AionUi 的 WebUI，首次访问有点慢，但后续的交互速度是没问题的，很快。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/dc14755ce905689801abb165c7d0d123_MD5.jpg)

只需要在AionUi设置中，启用 WebUI 功能即可，然后拿起微信扫二维码就可以了。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/093e74d73c44e1bff811b147ab20a4a1_MD5.png)

而且，AionUi 还支持 Telegram、飞书、Slack 等聊天平台的集成。你可以直接在这些平台上和 AI 助手对话，真正的 7×24 小时 AI 陪伴。

## 04、实时预览，9+ 格式支持

AionUi 内置了强大的预览面板，支持 9+ 种格式的实时预览：PDF、Word、Excel、PPT、代码、Markdown、图片、HTML、Diff 等。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/d889e36f43ec56cbed09768440da2b13_MD5.png)

当 AI 生成文件，或者我们需要实时查看任何输入来源的文件时，可以立即查看预览，不需要切换到其他应用。而且预览面板支持实时跟踪文件变化，编辑器和预览会智能同步。

对于 Markdown、代码、HTML 等格式，还支持实时编辑，所见即所得。

这个功能在调试 AI 生成的代码时特别有用，改完立马看效果，效率直接翻倍。

## 05、定时任务，自动化工作流

AionUi 还支持定时任务功能。

设置好定时任务后，AI 助手会按照你设定的时间自动执行，真正实现 7×24 小时无人值守运行。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/6199dc5f04ffd6dccf04664d70f7eedf_MD5.png)

使用场景包括：

- 定时数据汇总
- 定期报告生成
- 自动文件整理
- 定时提醒

你可以用自然语言告诉 AI 你想做什么，就像正常聊天一样。然后设置执行时间（每天、每周、每月都可以），AionUi 就会自动执行。

对于经常忘记事情的小伙伴来说，这个功能会很贴心。

## 06、10+ 专业助手，开箱即用

AionUi 内置了 10+ 专业助手，每个助手都有预定义的能力。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/e4fba70c50b400ce19f5f783eb4cb110_MD5.png)

- **Cowork** - 自主任务执行（文件操作、文档处理、工作流规划）
- **PPTX Generator** - 生成 PPTX 演示文稿
- **PDF to PPT** - PDF 转 PPT
- **UI/UX Pro Max** - 专业 UI/UX 设计（57 种风格，95 种配色）
- **Planning with Files** - 基于文件的复杂任务规划
- **moltbook** - 零部署集成，自动心跳调度、活动报告、无缝 AI Agent 社交
- **Beautiful Mermaid** - 流程图、序列图等

比如说我们让 AionUi 生成一张 PaiFlow 工作流 Agent 项目的学习路线图。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/5a0f53105e8dbfd9e6427dbe6b117886_MD5.png)

他就会调用 Mermaid 这个助手，生成 Mermaid 格式的代码。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/fa998f9f9a0d8db346fc7b348d273fb0_MD5.png)

复制出来，放到 `              https://mermaid.live            ` 来看一下效果，个人觉得水平还是非常高的。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/f036a047f007fa732defb1337863f102_MD5.png)

步骤清晰，并且内容提取的也很棒，没有任何错误。

## 07、ending

接下来，我还会继续挖掘，给大家带来更多的体验，希望能给大家提供一些帮助和参考。

如果只用一句话来总结我的真实体验：

**AionUi 已经坐实了 AI 办公+编程自动化的最佳实践。**

从多 Agent 协同到 WebUI 远程访问，从智能文件管理到定时任务自动化，从 10+ 专业助手到 AI 绘图，AionUi 几乎覆盖了打工人的所有场景。

最重要的是，它完全免费、开源。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/b6329c73f10c8293183934e50445e40b_MD5.png)

> GitHub： [https://github.com/iOfficeAI/AionUi](https://github.com/iOfficeAI/AionUi)

目前已经斩获 **14.2k+ Star** ，而且还在快速增长中。

![图片](assets/%E6%96%A9%E8%8E%B714k+Star%EF%BC%8C%E6%8A%8AOpenClaw+Claude%20Code%E7%AD%89%E5%A4%9A%E4%B8%AAAgent%E8%A3%85%E8%BF%9B%E4%B8%80%E4%B8%AAUI%E3%80%82/62892e71deb87e4c0acbe17127d04857_MD5.png)

要我说，以后是码转文科的时代。

为什么？

因为各种AI工具的出现，让每个人都能Vibe Coding出自己想要的工具。

剩下的只是你的创意，你脑子里的想法。

换句话说：

「 **工具的价值，是让我们专注于创造，而不是重复劳动** 。」

如果你也在用 Claude Code、Gemini CLI 这些命令行 AI 工具，或者你正在寻找一款强大的 AI 办公自动化平台，AionUi 绝对值得一试。

他能让你从重复的劳动中解脱出来，把注意力集中在你想要创造的事情上。

我们下期见～

派聪明AI · 目录

作者提示: 个人观点，仅供参考

阅读原文