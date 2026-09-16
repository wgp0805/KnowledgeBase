---
title: "WorkBuddy搭建个人知识库保姆级教程"
source: "https://mp.weixin.qq.com/s/g0S1C4iEogdaVAWrRbjnzA"
---
苏三说技术 *2026年9月16日 09:00*

大家好，我是苏三。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

很多人用 Obsidian、Notion 这类笔记软件，都有一个逃不掉的魔咒，叫“收藏即吃灰”。

平时看到好文章、技术资料或者讨论记录，随手点个剪藏存进笔记库。存的时候觉得掌握了全世界，过几个月想找某一个具体方案，搜关键词搜出一堆碎片，根本找不到当时最核心的那段结论。

说白了，传统的笔记库只是一个杂乱的文件仓库。东西放进去是死的，存得越多，信息冗余越大，更谈不上建立自己的知识体系。

今天分享一套我一直在用的方法，用 WorkBuddy 配合 Obsidian，搭建一套真正会自生长的个人知识库。平时习惯用 Codex 等支持本地读写工具的朋友，逻辑也是完全相通的。

每次把新文章丢进去，AI 会先去翻看旧知识，已有页面直接增量补充，缺失概念单独新建，所有结论必须附带原文路径。更关键的是，它会自动记录每一次知识的生长过程。

照着做，几分钟就能跑通。

## 核心区别

在动手之前，先厘清普通知识库和自生长知识库的区别。

普通知识库本质上是资料中转站。你把几十篇讲同一个技术的文章存进去，知识库里就多了几十个独立的 Markdown 文件。它们彼此之间没有连接，新旧观点没有对照，过时的信息也不会被覆盖。

自生长知识库的核心在于知识融合。

新资料进入知识库后，AI 不会直接把它变成孤立笔记，而是带着这篇资料先遍历已有体系。如果旧页面已经讨论过这个话题，它会把新观点合并进去；如果发现了新概念，它才单独建页；如果两篇文章对同一个问题说法不一致，它会同时保留两方观点并标明来源。

知识库不是文件越堆越多，而是体系随着每次输入不断生长。

![自生长对比](https://mmbiz.qpic.cn/mmbiz_png/YHZARf33mbEibJufNZUW0mt8e900jI39P8CJdhibpPnkASROFtvJOGia0SQ8hhWRLooZA8t5P0DlyU3vI2gptYMxPUfJyZFVz5yE4cb0dohK2c/640?wx_fmt=png&from=appmsg#imgIndex=0)

## 工具准备

搭建整套体系只需要两个工具。

一个是 Obsidian。它负责在本地保存和可视化浏览所有 Markdown 文件，双链和图谱功能成熟，而且数据都在本地，不用担心服务商关停。

另一个是 WorkBuddy。它负责扮演知识库的维护者，读取新资料、提炼重点、和旧知识做交叉对比，然后增量写入。

先打开 Obsidian，点击新建一个空的本地仓库，名字随意，比如叫 MyKnowledge。

![图片](https://mmbiz.qpic.cn/mmbiz_png/YHZARf33mbF1hFNhdmQNQmhQ7yF7mOtjW6Vw5zoYRPkPMwKvbicb9e6rkZUkABh39n7DP7xgzjHRThLC32FjuSxo5JFJKiciaKcpFQMY0wf1u4/640?wx_fmt=png&from=appmsg#imgIndex=1)

建好之后，先不用在 Obsidian 里手动建任何文件夹，我们把剩下的事情交给 WorkBuddy。

## 极简分层

打开 WorkBuddy，点击“打开本地文件夹”，选中刚才新建的那个空知识库目录。

让它列出当前目录确认一下，确保操作的是一个干净的目录。

![WorkBuddy 打开知识库目录](https://mmbiz.qpic.cn/mmbiz_png/YHZARf33mbFOQEEpFyv1s7lib6U1Vwqz7zQ7AqldeAR9S0zhCx6NCBv6UPicaNsB6lpb8GxafmdklaRcWk1f5me9yd6CIgUEAdhibraibGmbCZI/640?wx_fmt=png&from=appmsg#imgIndex=3)

一套能长期维护的知识库，目录分层必须极简。层次越深，AI 维护起来越容易迷路。

我们只分三层。

`raw/` 专门存原始文章、剪藏网页和会议记录，这一层的原则是只读，任何情况下都不改动原文。

`wiki/` 是 AI 提炼整理后的结构化知识，也就是长期留存的核心资产。

`output/` 用来存放临时报告、文章大纲或者阶段性分析结果。

不用自己手动新建文件夹，直接把下面这段初始化提示词复制发给 WorkBuddy。

```
请把当前 Obsidian 知识库配置成一套可以长期增量维护的 LLM Wiki。创建 raw、wiki、output 三个目录，并把维护规则写入 
            AGENTS.md。
          

raw 只保存原始资料，不修改原文。
wiki 由你维护，每次处理新资料前，先读取 wiki/
            index.md
           并搜索相关页面，已有主题直接补充，没有合适页面再新建。写入 wiki 的重要结论必须标注对应的 raw 文件路径，不同来源说法不一致时同时保留。
output 用来保存临时报告和分析结果。
每次处理完成后更新 wiki/
            index.md
           和 wiki/
            log.md。
          

请先创建目录和规则，不要处理现有文件。
```
![执行初始化提示词](https://mmbiz.qpic.cn/sz_mmbiz_png/YHZARf33mbEb0iaj9hzVB7jibo326ln1y7ibz7KOruJGwOZNia2d2qSwstZo2m3HlsicjYGxsTQOCRMnniavQ75Gm47gxmD6XGKNNOVs9cLGj7icE8/640?wx_fmt=png&from=appmsg#imgIndex=4)

等待 WorkBuddy 执行完毕，花十秒钟快速检查一下。

看三个目录有没有建好，重点打开根目录新生成的 `              AGENTS.md            ` 。

这个规则文件就是整个知识库的宪法。它明确规定了原文只读、优先增量更新旧页面、结论必须溯源等原则。有了这份规则，AI 后续的操作才不会随意发挥。

![检查 AGENTS.md 规则](https://mmbiz.qpic.cn/mmbiz_png/YHZARf33mbHMbtZ5RIrbnia4WHoDmnEqB19ACW3SibY3rJ5CiakHCRhuY3IK4mpMgaMgkFWH8zTM8gTr61MYfPUXibGrhQPfKAVpzKn5clRCo1g/640?wx_fmt=png&from=appmsg#imgIndex=5)

## 首次入库

规则就位后，开始放入第一篇资料。

挑一篇你最近想消化的长文或者技术资料，用浏览器剪藏插件转成 Markdown，直接扔进 `raw/` 文件夹。

这里有个关键技巧，第一次测试只放一篇资料。先不要一口气扔几十篇，放一篇能让我们直观观察到 AI 究竟修改了哪些文件。

![资料存入 raw](https://mmbiz.qpic.cn/sz_mmbiz_png/YHZARf33mbGeBqRVpetQxHicyZGmx7SCQZfCAP1KOTeKZRCcbsv9iaP64sLtKicsgFNRrR0sWwwQVDfgH0Jg79ro8kVYaVwkHM10yzxDlq1nbI/640?wx_fmt=png&from=appmsg#imgIndex=6)

文件放好后，把入库指令发给 WorkBuddy。

```
请读取 raw 中刚加入的资料，并按照 
            AGENTS.md
           增量维护 wiki。先查找已有相关页面，再决定更新还是新建。完成后更新 
            index.md
           和 
            log.md，并告诉我本次新增了什么、修改了什么、哪些内容存在冲突或还不能确认。
```

WorkBuddy 会按步骤读取原文，在 `wiki/` 下生成结构化的概念页面，最后刷新全局索引 `              index.md            ` ，并在 `              log.md            ` 里记录这次操作的详细变动。

此时再去查看， `raw/` 中的原文完好无损，而提炼出来的要点已经整整齐齐沉淀到了 `wiki/` 目录中。

![完成首次入库](https://mmbiz.qpic.cn/mmbiz_png/YHZARf33mbEQTjC4ns4462ibcdic99rns9XUkoMNibo7VCtjCA5mrztZKHerjR2xkVicpGJB2uniaC0S2fCU9TJtObBL1sfKRNyXlLPoSuEM2kibQ/640?wx_fmt=png&from=appmsg#imgIndex=7)

## 增量演进

知识库搭没搭成功，关键就在这一步。

如果第二篇文章放进去，AI 只是重新建了一个新文件，那它依然只是个静态网盘。

为了验证它是否真的会自生长，找一篇同主题、但有新观点或不同视角的文章，存入 `raw/` 文件夹，然后再次发送上面的入库指令。

这时候要观察两件事。

第一，对于已经存在的概念，它有没有在原页面上做内容融合，而不是无脑新建重名文件。

第二，页面里沉淀的核心结论后面，有没有同时附带指向两篇不同原文的文件路径。如果遇到观点冲突，有没有客观保留两方的说法。

如果两项都符合，说明知识融合机制已经完整跑通了。

![验证知识增量演进](https://mmbiz.qpic.cn/sz_mmbiz_png/YHZARf33mbEd9wLQWrI8Em5sKlSLka14W4LzQ0t5Jfpzq0WhKKmjuIdBre2LGCgZNCsQVRESpokibEfAg1HTajFLP2xibVv2mzzrtS3icaTdM8/640?wx_fmt=png&from=appmsg#imgIndex=8)

## 进阶方案

上面这套提示词直建法，目录干净，改动灵活，最适合新手理解整套知识库生长的底层机制。

如果你的资料量非常大，想要更严密的工程化流程，也可以直接接入开源的 `claude-obsidian` 。

![claude-obsidian 开源工具体系](https://mmbiz.qpic.cn/mmbiz_png/YHZARf33mbEeic4H9XMVQzxMCz9Y0ibOKJTDrujQDxx8udU2VuFfWUJINVZcNNulN634FicIctcsaExZicDpN6r966kicSt4xxOg6ubrzqHFpAoI/640?wx_fmt=png&from=appmsg#imgIndex=9)

它把整套规则、检索脚本和一致性校验器封装成了开箱即用的工作流。

新建知识库运行 `init` ，已有知识库运行 `adopt` 直接接管。入库用 `wiki-ingest` ，精准问答与溯源用 `wiki-query` ，定期排查孤立页面和失效链接用 `wiki-lint` 。

![知识循环流图](https://mmbiz.qpic.cn/mmbiz_svg/Q3auHgzwzM5oXeefX2vku3iciapiamm5ialvEvz5bBto8WMDFay9FoU5hC2jwgFQTj8jF0UrRiaUiaYtO34fZliaBvDlH2p6spU2mejb2Nu419OIWnDpCLepxOQbg/640?wx_fmt=svg&from=appmsg#imgIndex=10)

两种方案怎么选，其实很简单。

如果是日常阅读笔记、刚开始尝试 AI 知识管理，直接用提示词直建法，轻量且容易掌控。

如果要长期维护数万字以上的复杂项目文档或者行业知识库，可以进阶使用现成的工作流模块，有校验工具兜底，长期维护更加省心。

## 自检清单

知识库跑通之后，平时维护建议记住这 5 条自检标准。

1. 原文和提炼页面是否彻底隔离。 `raw/` 负责真实存档， `wiki/` 负责知识沉淀，绝对不改动原始文件。
2. 关键事实能否溯源。 `wiki/` 里的核心论断必须带上来源文件的相对路径。
3. 相同主题是否合并。新资料优先补充旧主题，避免重复建页造成信息孤岛。
4. 变更日记是否清晰。每次入库后， `              log.md            ` 都有清晰的变动记录，方便回溯。
5. 索引是否保持同步。 `              index.md            ` 随时反映最新的知识全貌。

资料存得再多，不产生连接就只是占空间的数字垃圾。

让知识在每一次输入中自我对照、增量迭代，才能把碎片化的信息真正变成自己的第二大脑。

## 最后

说个现实的问题，AI 工具更新太快了。Codex 配置、Plus 充值，每个环节都可能卡你半天，网上教程下个月可能就过时了。

这些坑我基本都踩过，配置教程和踩坑记录一直在更新。AI 提效技巧、副业实操、新模型怎么选，也会持续分享。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)