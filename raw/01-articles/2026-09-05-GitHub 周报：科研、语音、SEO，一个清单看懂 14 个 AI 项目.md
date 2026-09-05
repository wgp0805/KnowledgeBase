---
title: "GitHub 周报：科研、语音、SEO，一个清单看懂 14 个 AI 项目"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6460165.html"
date: "Sat, 05 Sep 2026 08:07:54 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# GitHub 周报：科研、语音、SEO，一个清单看懂 14 个 AI 项目

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6460165.html  
> **抓取日期**: 2026-09-05  
> **相关性评分**: 1.0

这是一篇周更式 GitHub 开源盘点：作者从本周 Trending 与社区热点中筛出 14 个项目，每个按 “是什么 → 能做什么 → 注意事项 → 开源地址” 的节奏介绍，可跳读、可收藏。

按用途，本期项目可归为六类：

  * **科研与知识生产（01、05）** ：Scientific Agent Skills 把 160+ 科研技能与 100+ 科学数据库打包成 Agent 可调用的 Skill；中国专利 Skill 则把专利点挖掘、查新、交底书成稿串成一条工作流。
  * **模型与算法（04、08、09）** ：Google TimesFM 让时间序列零样本预测更进一步；MiniMind 用 6400 万参数讲清大模型完整训练链路；Heretic 提供一种调整模型拒答行为的思路。
  * **AI 开发与 Agent 生态（07、10、11、14）** ：OpenClaude 用一个终端切换多模型，Awesome MCP Servers 汇集 9.4 万 + Star 的 MCP 资源，Screenshot to Code 让截图直出前端代码，Archify 把系统描述变成可交互架构图。
  * **语音与多媒体（06、13）** ：VoiceStudio 是本地语音工作室，覆盖克隆、配音、转录；OpenWhispr 让说话直接落到光标处，并支持会议转录与后续 AI 操作。
  * **移动与系统工具（02、12）** ：vphone-cli 在 Mac 里 “养” 一台可编程的虚拟 iPhone；ipatool 用命令行搜索、下载 App Store 应用包。
  * **网站与运营（03）** ：OpenSEO 把关键词研究、排名追踪、竞品与外链分析整合成开源 SEO 方案。



几点提醒：项目热度和上手难度并不总成正比 ——vphone-cli 需要 M 系列芯片、macOS 15 和 Xcode，OpenSEO 的 SEO 数据需另购 API，科研 Skill 也只提供流程与工具，结论仍需研究者自行核验。建议先按你的场景锁定编号，再细看前置条件。

## 01 一大波科研 Skills

Scientific Agent Skills 收录了 **160 多个科研 Skill** ，并整理了 100 多个科学数据库的使用方式。

这些 Skill 包括**生物信息、药物发现、医学研究、材料科学、地理空间分析和科研写作等方向。**

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/48e2308d7a37349e360eea96288ba496_MD5.png)

这些 Skill 的核心价值就是**把科研流程沉淀为可复用的程序性知识，** 让模型少走弯路，也让复杂研究流程更容易复现。

每个 Skill 会告诉 Agent 应该调用什么工具、遵守哪些流程、检查哪些结果。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/a5f239aa9bc6161b3910a8585764cd74_MD5.png)

科研任务对准确性和可追溯性要求很高。

安装这套资源并不等于 AI 自动具备了科学判断力，研究者仍要检查数据来源、统计方法和实验结论。
    
    
    开源地址：https://github.com/K-Dense-AI/scientific-agent-skills

 

## 02 在 Mac 上启动一台虚拟 iPhone

**vphone-cli 可以理解为：在 Mac 里养一台虚拟 iPhone，还能让程序或 AI 操作它。**

比如你开发了一个手机 App，想检查 打开应用 → 点击登录 → 输入内容 → 查看结果 是否正常。

这个项目提供一台虚拟手机，再**通过自动化接口完成点击、滑动、截图等操作，减少反复手动测试。**

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/c66736cddd5e95e0b06b19b6f377c1ed_MD5.jpg)

但是它的**使用门槛很高。**

需要 **M 系列芯片的 Mac、macOS 15 或更新版本，以及 Xcode。**

还涉及调整 Mac 的部分安全保护设置。
    
    
    开源地址：https://github.com/Lakr233/vphone-cli

 

## 03 开源的 SEO 解决方案

OpenSEO 提供**关键词研究、排名追踪、竞品分析、外链分析和站点审计** 等常用功能。

它既有网页界面，也提供 MCP Server 和一组 SEO Skills。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/3d55dd795d23f7d68fa4d58710346d6f_MD5.png)

你可以让 Agetn 读取 SEO 数据，**完成关键词聚类、竞争格局分析和外链机会整** 理。

项目支持 Docker 和 Cloudflare 部署。

OpenSEO 的代码可以免费使用，SEO 数据仍然有成本。它主要依赖 DataForSEO，用户需要准备 API 凭证并按调用量付费。

本地 Docker 版本默认采用单用户模式且没有登录验证，也不适合未经配置就暴露到公网。它真正省下的是软件订阅费和工作流锁定，数据采购费用依然存在。
    
    
    开源地址：https://github.com/every-app/open-seo

 

## 04 自动修改语言模型的拒答行为

Heretic 是一个修改 AI 模型的工具，目的是让模型减少抱歉，这个问题我不能回答这类回复。

作者把它称为自动移除模型审查的工具。

更准确地说，它主要削弱模型的拒答行为，同时尽量保留原来的能力。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/991227efb60d3cd7477e31b6da77d8b2_MD5.png)

你可以理解 AI 是一位受过培训的助手：既学了知识，也学了哪些问题应该拒绝。

Heretic 这个开源项目，就像调整后面这部分，让它更愿意回答。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/0b6f6dc17d03587da336ecb320b15d37_MD5.png)
    
    
    开源地址：https://github.com/p-e-w/heretic

 

## 05 中国专利 Skill

这个 Skill 是帮你写专利的。

它把**专利点挖掘、现有技术检索、交底书成稿和后续修订整理成一套工作流。**

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/f8154185baf99ee2d93b2dc35b846fa7_MD5.png)

你发给 Agent 设计文档、代码、Word 或 PPT，Skill 会先扫描材料，再梳理可能的创新点。

它会优先通过国家知识产权局的中国专利公布公告站进行查新，随后**生成包含系统框图和流程图的 Markdown 与 Word 文档。**

交底书修改时会另存新版本，并记录每轮补充和纠正，方便研发人员与专利代理人继续协作。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/5df4e1e95337d0e10384b36dc2a69e03_MD5.jpg)

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/5e47fdec8bb10e6932cc28c6fb692b3a_MD5.jpg)

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/540557471a85130e407fa4afe42337e4_MD5.png)
    
    
    开源地址：https://github.com/handsomestWei/patent-disclosure-skill

 

## 06 VoiceStudio

VoiceStudio 是一套本地的开源语音工作室，**支持语音克隆、声音设计、视频配音、听写、转录和有声书制作。**

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/95ef17a18a5aa0b63cf80e48a160243a_MD5.png)

你可以用短音频建立声音样本，批量生成语音，也能**给视频完成转录、翻译、角色识别和重新配音。**

它同时提供本地 API、OpenAI 兼容音频接口和 MCP Server，方便创作者把语音能力接到自己的脚本或 Agent 工作流中。

项目支持 macOS、Windows 和 Linux，并能利用 CUDA、Apple Silicon 或 CPU 运行不同引擎。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/985b84d6caaf977e6992defca8782127_MD5.gif)
    
    
    开源地址：https://github.com/debpalash/VoiceStudio

 

## 07 OpenClaude：一个终端，接入不同模型

OpenClaude 是一款开源终端 Coding Agent，可以**在同一套工作流里切换云端 API、本地模型和多种模型。**

项目已经有 3.2 万多个 Star。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/f8bd5b3042cf7bc4a91ddcc5527c94a9_MD5.png)

它保留了Coding Agent 常用的文件读写、搜索、Shell、MCP、Skills 和子任务能力。

同时把模型选择权交还给用户。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/011d18f5f43879da70baaa1478f5abd2_MD5.png)
    
    
    开源地址：https://github.com/Gitlawb/openclaude

 

## 08 Google 把多变量预测做成基础模型

TimesFM 是 Google Research 开源的时间序列基础模型，刚更新的版本已经**支持原生多变量预测了。**

库存、销量、能耗、流量和设备指标都属于它的典型应用范围。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/1dd6eb5bedfef14f52c52e15142de468_MD5.png)

传统时间序列项目往往需要针对每类数据重新选模型、训练和调参。

TimesFM 主打零样本预测，**可以在没有见过目标数据训练集的情况下给出预测结果。**

3.0 还能同时处理多条相互关联的序列，并加入历史协变量和未来已知信息，例如节假日、价格或天气预报。

TimesFM 3.0 发布后，这个开源项目就登上本周 GitHub Trending 榜单了。
    
    
    开源地址：https://github.com/google-research/timesfm

 

## 09 用小模型看清 LLM 的完整训练过程

MiniMind 把大模型的结构和训练链路狠狠压缩。

变成一个个人开发者可以**理解、复现和修改的规模。**

主线小模型约有 6400 万参数，项目已经 5.8 万多个 Star。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/ba71e2e044aabb8f8594f08f3a517a40_MD5.png)

这个开源项目包括**数据清洗、预训练、监督微调、LoRA、偏好优化、强化学习、工具调用和模型蒸馏等环节。**

核心算法主要用原生 PyTorch 实现。

你可以看到每一步具体做了什么，不会被高层训练框架遮住关键细节。
    
    
    开源地址：https://github.com/jingyaogong/minimind

 

## 10 Awesome MCP Servers

Awesome MCP Servers 整理了大量可供 Codex、Claude Code 等调用的 MCP Server，**目前已经拥有 9.4 万多个 Star。**

这份列表按**浏览器自动化、数据库、开发工具、文件系统、搜索、金融和多媒体等场景分类。**

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/58c5c21175a0bffc4937200741d53c0b_MD5.png)

每个项目还会标注主要语言、本地或云端运行方式、支持的系统以及是否是官方的。

刚开始给 Agent 接工具时，从分类目录寻找候选项目会比全网搜索省事很多。

合集里的项目既有生产级工具，也有实验性实现。
    
    
    开源地址：https://github.com/punkpeye/awesome-mcp-servers

 

## 11 截图、设计稿和录屏都能生成前端代码

Screenshot to Code 可以把**页面截图、设计稿和屏幕录制转换成可运行的前端代码。**

项目已经获得 7.7 万多个 Star，是视觉生成代码领域最有代表性的开源项目之一。

它支持 HTML、CSS、React、Vue 和多种样式方案。

生成后可以在浏览器里预览，再**继续修改布局和素材。**

视频模式还会读取页面操作过程，用来恢复部分交互效果，比只看一张静态截图多了时间维度的信息。
    
    
    开源地址：https://github.com/abi/screenshot-to-code

 

## 12 用命令行搜索和下载 App Store 应用包

ipatool 可以在 Windows、Linux 和 macOS 上登录 App Store，**搜索应用并下载加密的 IPA 安装包。**

它也支持列出可用历史版本，并通过外部版本 ID 下载指定版本。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/247f8e3cf58305128dd3a173316bdb2d_MD5.gif)

这套能力对应用归档、兼容性测试和安全研究很实用。

命令支持文本和 JSON 输出，也能使用非交互模式接入自动化脚本。

macOS 用户可以通过 Homebrew 安装：brew install ipatool

项目需要使用已经能够访问 App Store 的 Apple ID。
    
    
    开源地址：https://github.com/majd/ipatool

 

## 13 把语音输入变成桌面工作流

OpenWhispr 是一款跨平台语音输入应用，可以把说话内容写入当前光标位置。

也能完成**会议转录、笔记整理和语音 Agent 操作。**

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/998d8e883644517a34ff3c51afaf5655_MD5.png)

你可以选择 Whisper 等本地语音模型，让音频保存在你的电脑上。

也可以使用自带 API Key 的云端服务换取更快的处理速度。

会议模式能够识别 Zoom、Teams 和 FaceTime 等通话，并提供说话人区分、笔记搜索和后续 AI 操作。

项目还开放了 MCP Server，方便其他 Agent 读取转录与笔记。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/849f3de719683013404d39ae92fb8abf_MD5.png)

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/65db7e06bfb78635598e28b435f6ccb5_MD5.png)

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/cf0fccbc61f650cf90b4cd7d48e4d91f_MD5.png)
    
    
    开源地址：https://github.com/OpenWhispr/openwhispr

 

## AI 画架构图

Archify 这个开源项目，可以把一段系统描述或**一个代码仓库变成可交互的系统图。**

目前项目已经拿到 4.8 万多个 Star，本周的增长很快。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/520e66fbad18d2499c6b687249260745_MD5.png)

Archify 有一层约束：**Agent 先生成带类型的结构化数据，工具完成校验后再渲染 HTML 和 SVG。**

节点、连接和路径都来自已经写入的数据，渲染器不会在数据之外额外添加依赖关系。

但校验主要检查结构、布局和组合规则，不能自动证明图与真实系统完全一致。

它支持**架构图、工作流图、时序图、数据流图和生命周期图。**

生成结果是一个自包含的 HTML 文件，可以搜索节点、追踪上下游路径，也能导出 PNG、SVG 和视频。

![](assets/2026-09-05-GitHub%20%E5%91%A8%E6%8A%A5%EF%BC%9A%E7%A7%91%E7%A0%94%E3%80%81%E8%AF%AD%E9%9F%B3%E3%80%81SEO%EF%BC%8C%E4%B8%80%E4%B8%AA%E6%B8%85%E5%8D%95%E7%9C%8B%E6%87%82%2014%20%E4%B8%AA%20AI%20%E9%A1%B9%E7%9B%AE/55f8ad02bfe6cd92d7855b65500e46de_MD5.gif)
    
    
    开源地址：https://github.com/tt-a1i/archify

本文由作者@逛逛GitHub，授权发布于平台，未经许可禁止转载。


---
> 原文链接: https://www.woshipm.com/ai/6460165.html