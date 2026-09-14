---
title: "给 React Native 的鸿蒙化画一张全景地图：rn-ohos-adaptation-overview 诞生记"
source: "人人都是产品经理"
url: "https://www.woshipm.com/share/6462774.html"
date: "Sat, 12 Sep 2026 03:54:30 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# 给 React Native 的鸿蒙化画一张全景地图：rn-ohos-adaptation-overview 诞生记

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/share/6462774.html  
> **抓取日期**: 2026-09-12  
> **相关性评分**: 1.0

> 从 reactnative.directory 收录的 2694 个三方库出发，用六步自动化核验流程把 React Native 的鸿蒙适配现状整理成可更新的数据清单，并给出键名归一化等工程细节与社区可以认领的适配方向。

![](https://image.woshipm.com/2023/09/26/14fe7516-5c65-11ee-bd4e-00163e142b65.jpg)

从 reactnative.directory 全量 2694 个三方库出发，通过自动化核验，把”鸿蒙适配现状”变成一份可随时更新的数据清单——这就是 **rn-ohos-adaptation-overview**[1] 做的事。这篇文章记录我是如何实现的，以及关于助力开源鸿蒙跨平台框架生态繁荣的一些思考。

## 一、背景：RN 鸿蒙化的机遇与最痛的短板

HarmonyOS / OpenHarmony 生态发展至今，跨平台框架的鸿蒙化已经走过了从“能不能跑”到“跑得好不好”的阶段。React Native 作为最主流的跨平台框架之一，通过 React Native OpenHarmony（RNOH）项目可以在鸿蒙设备上运行。对开发者来说，这意味着一个巨大的机会：**一套代码，多端发布** 。

但横亘在“能跑”和“能用”之间的，是一个非常现实的问题——**三方库生态** 。React Native 的应用几乎离不开三方库：相机、地图、推送、支付、图表、动画……每一个都在你项目的 package.json 里。而在鸿蒙平台上，这些库的适配情况是碎片化的：

  * 有些库官方已经完成了鸿蒙适配（如 @react-native-oh-tpl 系列）；
  * 有些库是纯 JS 实现，没有原生代码，其实**直接就能用** ；
  * 有些库没有适配，但同分类下已有成熟替代，**换个库就行** ；
  * 还有一些库完全没有替代，**需要社区认领去适配** 。



问题在于：这些信息散落在 npm、GitHub、各组织仓库里，**没有一份权威、完整、可检索的清单** 。开发者只能靠试错——装一个库，跑不起来，再去搜有没有鸿蒙版本，效率极低；社区贡献者也看不到“哪些库最值得适配”，无从下手。

## 二、想法：把”适配现状”变成一份会自己更新的数据清单

我决定做一件事：**把 reactnative.directory 上全部 React Native 三方库的鸿蒙适配现状，系统性地盘点一遍，产出一份可自动更新的清单** 。

这不是一份手工整理的 Excel，而是一条数据流水线。我给自己定了三个要回答的问题：

  1. **哪些库已经完成鸿蒙适配？** （开发者可以直接用）
  2. **哪些库无需适配？** （纯 JS，开箱即用）
  3. **哪些库待适配？其中哪些有替代、哪些必须重点投入？** （社区认领的方向）



想清楚之后，方案就变得清晰：数据源用 reactnative.directory（它聚合了 GitHub react-native-community/directory 的库信息），适配来源用鸿蒙社区现有的几个已知渠道，匹配逻辑用脚本自动完成，最后生成多份清单文件。

## 三、实现：一条六步的数据流水线

整个生成过程在 **scripts/regenerate.py**[2] 中实现，分六个步骤：

### 1\. 拉取全量库数据

数据源是 reactnative.directory 的 API，共 **2694** 个库。每个库带有 npm 包名、GitHub 地址、热度评分（score）、平台信息（iOS / Android）、是否包含原生代码（hasNativeCode）以及 topic 标签。

脚本支持两种模式：**在线模式** （–live，实时抓取刷新快照）和**快照模式** （默认，读取 data/ 目录下的离线快照）。快照机制让清单可复现、可审计，不依赖网络环境。

### 2\. 核验适配来源，打上”已适配”标记

我汇总了鸿蒙社区目前最主要的 **5 个适配来源** ：

来源 | 说明  
---|---  
CPF-RN/usage-docs | HarmonyOS 平台 RN 第三方库使用文档（含适配库清单与各库使用文档）  
hxa-RN 组织 | 鸿蒙系统 RN 开源库社区，已建仓库即已适配  
CPF-RN 组织 | RN 鸿蒙化适配仓库（rntpc_* 前缀等）  
@react-native-oh-tpl（121 个） | RNOH 官方适配包  
@react-native-ohos（295 个） | 社区另一套鸿蒙适配包  
  
把 2694 个库逐一与这 5 个来源做匹配。**匹配的关键** 是键的归一化：同一个库在不同来源里写法可能不同（react-native-view-shot 在适配包里可能叫 @react-native-oh-tpl/react-native-view-shot，@react-native-community/slider 也可能被写成 slider）。我设计了一套**固定优先级的有序 key 候选链** （name → npmPkg → fullName → 去连字符变体），按顺序取第一个命中项。

这里有一个值得分享的工程细节：早期实现用 set 做匹配，结果发现 **Python set 的迭代顺序受哈希随机化影响** ，导致同一个输入在不同进程里生成的清单归属不稳定（同一个库有时算已适配、有时算待适配）。后来改为固定优先级的 key 列表匹配，彻底消除了随机性——这是“数据流水线”类工具最容易踩、也最容易被忽视的坑：**结果必须可复现** 。你永远不会希望同一份数据在 CI 里和本地生成出两份不同的清单。

### 3\. 拆分纯 JS 库，做依赖链核验

hasNativeCode == false 的库原则上不需要原生适配，但还有一个隐藏陷阱：**一个纯 JS 库可能依赖了某个未适配的原生库** ，那它照样跑不起来。比如某个表单库依赖了未适配的相机库。

所以这一步会对候选纯 JS 库逐个检查 npm 依赖链：只有”自身无原生代码 **且** 依赖链不含未适配原生库“的库才真正归入”无需适配”清单；依赖了未适配原生库的，会被打上 ![⚠](https://s.w.org/images/core/emoji/16.0.1/72x72/26a0.png) 标记并移回待适配列表。

### 4\. topic 分类匹配，给出”优先替换”建议

对剩下的待适配库，我会拿它的 topic 标签与所有已适配库的 topic 做重叠匹配。如果同分类下已经有成熟鸿蒙化适配库，就在清单里标记 **![🔁](https://s.w.org/images/core/emoji/16.0.1/72x72/1f501.png)优先替换** ，并给出候选替代库的链接——**与其重复造轮子，不如换一个已经能用的** 。这一条规则对开发者的指导价值非常大：很多时候你不需要等某个库的鸿蒙适配，换一个同类库就能立刻跑起来。

### 5\. 分类归组

没有替代、需要重点适配的库，按功能分类归组（未分类、Expo 模块、广告统计监控、系统能力设备、支付 IAP、音视频、图像图形、相机扫码 OCR、地图定位导航、网络通信、安全认证、数据存储、云服务 BaaS、AI 大模型、开发者工具、推送通知、社交分享 IM、游戏 3D AR、动画交互……），组内按热度降序。

### 6\. 写回五份清单文件

最后把结果渲染为五份 Markdown 文件，作为仓库的“产品”：

文件 | 内容 | 数量  
---|---|---  
README.md[3] | 剩余待适配主清单（按热度，含 ![🔁](https://s.w.org/images/core/emoji/16.0.1/72x72/1f501.png)/![⬜](https://s.w.org/images/core/emoji/16.0.1/72x72/2b1c.png) 标记） | 1263  
priority-by-category.md[4] | 重点待适配清单（按分类细化） | 466  
priority-adaptation.md[5] | 重点待适配清单（按热度平铺版） | 466  
adapted-libraries.md[6] | 已适配清单（含适配来源与链接） | 406  
pure-js-libs.md[7] | 无需适配清单（纯 JS 可直接使用） | 1025  
  
一次盘点，全貌尽收眼底：**406 个已适配 + 1025 个纯 JS 可直接用 + 1263 个待适配（其中 797 个有替代可优先替换，466 个需重点投入）** 。对开发者而言，“某个库在鸿蒙上能不能用”不再靠猜；对贡献者而言，“该适配谁”有了明确答案。

四、工程化：可复现、可自检、可持续

一个清单类工具，最怕的就是“生成一次就再也跑不起来”。所以我在工程上有三个坚持：

  1. **数据快照** ：data/ 目录固化抓取时间与数据源版本，离线可复现，在线可刷新；
  2. **确定性** ：固定优先级 key 匹配，同一输入必然得到同一输出；
  3. **自动审计** ：scripts/audit.py[8] 对五份文件做 7 项完整性自检——统计守恒（五文件并集必须等于 2694）、集合关系（priority 两文件必须是 README 的子集）、无重复包名、Markdown 链接括号平衡、状态列分布（![🔁](https://s.w.org/images/core/emoji/16.0.1/72x72/1f501.png) 797 / ![⬜](https://s.w.org/images/core/emoji/16.0.1/72x72/2b1c.png) 466）、统计段与行数一致性。任何一处数字对不上，审计直接报错。



这保证了清单不是一份“死文档”，而是一个**可持续演化的数据产品** ：适配来源新增一个库，重新生成，清单自动更新；误判被发现，改逻辑，审计兜底。

## 五、社区协作：把清单交给官方确认

盘点做完只是第一步。这份清单的**正确性** 需要鸿蒙 RN 社区、尤其是适配工作一线的组织来把关。我做了两件事：

  1. **提交 Issue 给 CPF-RN/usage-docs** （Issue #708[9]）：把 466 个重点待适配库的完整明细（按 19 个分类、含热度与 GitHub 链接，共 8 条评论全量贴出）提交给官方，请求确认——哪些库确实未适配？哪些值得优先适配？适配完成后如何回流到适配来源？
  2. **开放协作入口** ：欢迎官方与社区在 rn-ohos-adaptation-overview 仓库提交 Issue / PR——提交适配成果、修正数据误判、分享适配经验。



清单的价值不在于“我列出来了”，而在于**它成为社区协作的公共底座** ：官方确认结论 → 修正清单 → 适配成果回流 → 清单再更新，形成正向循环。

## 六、关于助力开源鸿蒙跨平台框架生态繁荣的一些思考

做完这件事，我最大的体会是：**一个生态的繁荣，往往不取决于某个“杀手级框架”，而取决于那些看不见的基础设施——文档、工具链、数据，以及清晰的协作机制。** 具体到鸿蒙跨平台生态，有几点思考想分享：

### 1\. 数据透明化，是生态繁荣的第一块基石

开发者做技术选型时，最怕的不是“没有库”，而是“不知道哪个库能用”。三方库的鸿蒙适配状态，本质上是一份**数据** ——它理应被系统性地采集、整理、公开，而不是靠每个人在群里问“xx 库有人适配过吗”。

当“能不能用”变成一张可检索的表格，开发者的迁移成本就大幅降低：纯 JS 库直接用，已适配库放心装，有替代的换一个，没替代的知道要等。**生态的繁荣，从消灭“信息差”开始。**

### 2\. 避免重复造轮子，把力量集中在刀刃上

盘点结果里有一个非常有意思的发现：1263 个待适配库中，**797 个（63%）其实同分类下已有成熟鸿蒙化替代** 。这意味着社区真正需要集中力量攻坚的，只有 466 个。

如果每个团队都闷头适配自己遇到的库，很可能出现“十个团队适配了十个类似的图表库，而最核心的地图库无人问津”的局面。**一份带替代建议的清单，就是最好的“力量调度器”**——它告诉社区：这里已经有替代，别重复造轮子；那里是空白，欢迎来补。

### 3\. 清单即任务池：降低贡献门槛

开源贡献最大的门槛往往不是技术难度，而是”**不知道从哪里下手** “。一份按分类、按热度排好序的待适配清单，天然就是一个任务池：

  * 新贡献者进来，选一个热度高、分类清晰的库认领；
  * 适配思路可以参考同分类已适配库的经验（清单里直接给了链接）；
  * 完成适配后按规则回流，清单自动更新，贡献被”看见”。



**把“该做什么”摆到明面上，贡献就从偶然变成可持续。**

### 4\. 自动化与可复现，让生态数据”活”起来

手工维护的清单注定会过时。我在这件事上投入了大量精力做工程化：数据快照、固定优先级匹配保证确定性、审计脚本兜底完整性。因为我相信，**生态基础设施必须能自我演化** ——适配来源更新了，清单要能跟着更新；数据错了，要能快速发现并修正。

### 5\. 与官方社区协同，形成反馈闭环

我把 466 个重点待适配库全量提交给了 CPF-RN/usage-docs 官方确认，并邀请官方在清单仓库提交 Issue / PR。这一步的价值在于：**民间盘点与官方实践互相校验** 。官方的确认结论让清单更权威，清单又反向帮助官方了解社区需求分布。这个闭环一旦转起来，生态数据就会越来越准。

### 6\. 展望：下一步还能做什么

这份清单只是起点。沿着这个方向，还有不少值得做的事：

  * **AI 辅助适配评估** ：结合每个库的代码结构、依赖关系，自动评估鸿蒙化适配难度与工作量，给每个库打上”难度星级”；
  * **适配进度追踪** ：把清单做成可交互的看板，记录每个库的适配状态（认领中 / 适配中 / 已提 PR / 已发布），让社区协作可视化；
  * **CI 自动化** ：定时重新生成清单 + 跑审计，数据变更自动提交，让清单永远是最新的；
  * **质量分级** ：区分”官方适配 / 社区适配 / 实验性适配”，让开发者对每个库的成熟度心里有数。



## 七、相关组织与 AtomGit 共建

开源鸿蒙跨平台框架 RN 生态的繁荣，离不开一个个组织与项目的持续投入。这里把与本文相关的组织和项目集中列出，供大家参考与关注：

组织 / 项目 | 说明 | 链接  
---|---|---  
oh-react-native | 本清单仓库（rn-ohos-adaptation-overview）所在组织 | atomgit.com/oh-react-native[10]  
CPF-RN | RN 鸿蒙化适配组织（含 usage-docs 使用文档、rntpc_* 等适配仓库） | atomgit.com/CPF-RN[11]  
CPF-RN/usage-docs | HarmonyOS 平台 RN 三方库使用文档（本清单主要适配来源之一） | atomgit.com/CPF-RN/usage-docs[12]  
hxa-RN | 鸿蒙系统 RN 开源库社区（已建仓库即已适配） | atomgit.com/hxa-rn[13]  
react-native-oh-library | RNOH 官方适配组织（@react-native-oh-tpl 适配包来源） | github.com/react-native-oh-library[14]  
@react-native-oh-tpl | RNOH 官方鸿蒙适配包（npm 组织，121 个） | npmjs.com/org/react-native-oh-tpl[15]  
@react-native-ohos | 社区鸿蒙适配包（npm 组织，295 个） | npmjs.com/org/react-native-ohos[16]  
  
**欢迎在 AtomGit 平台上共建** ![🤝](https://s.w.org/images/core/emoji/16.0.1/72x72/1f91d.png)：无论你来自哪个组织，都可以通过 AtomGit 参与这份生态基础设施的建设——

  * 在 rn-ohos-adaptation-overview[17] 提交 Issue / PR：补充适配来源、修正清单数据、认领待适配库；
  * 把适配成果回流到 usage-docs[18] 等适配来源，清单重新生成后自动更新；
  * 在你的组织仓库中直接复用 regenerate.py / audit.py，一起把鸿蒙跨平台生态的数据底座越做越厚。



## 结语

React Native 的鸿蒙化，是开源鸿蒙生态里一块潜力巨大的拼图。而拼图的每一块，最终要靠社区一块一块拼起来。这份清单，是我能提供的、让拼图过程更快一点点的基础设施——**它不直接写一行鸿蒙代码，但它让每一行鸿蒙代码都能被更快、更准地写出来。**

如果你也在做鸿蒙跨平台相关的工作，欢迎到 **rn-ohos-adaptation-overview**[19] 提交 Issue / PR：修正一个误判、补充一个适配来源、认领一个库，或者只是告诉我你的使用体验。**生态繁荣，始于每一个“我觉得可以更好”的行动。**

## 参考资料

[1]rn-ohos-adaptation-overview: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview_

[2]scripts/regenerate.py: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview/blob/main/scripts/regenerate.py_

[3]README.md: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview/blob/main/README.md_

[4]priority-by-category.md: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview/blob/main/priority-by-category.md_

[5]priority-adaptation.md: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview/blob/main/priority-adaptation.md_

[6]adapted-libraries.md: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview/blob/main/adapted-libraries.md_

[7]pure-js-libs.md: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview/blob/main/pure-js-libs.md_

[8]

scripts/audit.py: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview/blob/main/scripts/audit.py_

[9]Issue #708: _https://atomgit.com/CPF-RN/usage-docs/issues/708_

[10]atomgit.com/oh-react-native: _https://atomgit.com/oh-react-native_

[11]atomgit.com/CPF-RN: _https://atomgit.com/CPF-RN_

[12]atomgit.com/CPF-RN/usage-docs: _https://atomgit.com/CPF-RN/usage-docs_

[13]atomgit.com/hxa-rn: _https://atomgit.com/hxa-rn_

[14]github.com/react-native-oh-library: _https://github.com/react-native-oh-library_

[15]npmjs.com/org/react-native-oh-tpl: _https://www.npmjs.com/org/react-native-oh-tpl_

[16]npmjs.com/org/react-native-ohos: _https://www.npmjs.com/org/react-native-ohos_

[17]rn-ohos-adaptation-overview: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview_

[18]usage-docs: _https://atomgit.com/CPF-RN/usage-docs_

[19]rn-ohos-adaptation-overview: _https://atomgit.com/oh-react-native/rn-ohos-adaptation-overview_

本文由人人都是产品经理作者【nutpi】，微信公众号：【nutpi】，原创/授权 发布于人人都是产品经理，未经许可，禁止转载

题图来自Unsplash，基于 CC0 协议。


---
> 原文链接: https://www.woshipm.com/share/6462774.html