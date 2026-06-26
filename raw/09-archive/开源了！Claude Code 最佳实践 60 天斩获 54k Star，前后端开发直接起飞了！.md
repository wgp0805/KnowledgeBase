---
title: "开源了！Claude Code 最佳实践 60 天斩获 54k Star，前后端开发直接起飞了！"
source: "https://mp.weixin.qq.com/s/d3dFVzo3XNkMGXRIhlaSvw"
---
苏三说技术 *2026年6月26日 08:43*

最近想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG + MCP系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247538241&idx=1&sn=73d443e9a5ce6ee3317e97e5ce213d07&scene=21#wechat_redirect)

如果你平时用Claude Code写代码，大概会有同样的感受：这东西不是“会用就行”，而是“用对了”和“用错了”之间，效率能差出一个数量级。

新人装好Claude Code之后，通常就两种状态：

- 一是把它当ChatGPT用——丢一个“帮我写个OAuth登录”的任务过去，等它吐出几百行代码，然后自己一行行看、一点点改。
- 二是靠自己摸索——/compact什么时候该用、 [CLAUDE.md怎么写、Subagents该装哪几个、Hook要不要加——全凭试错。](http://claude.xn--mdsubagentshook-8u9ha5844eja8594mirajut98cb7a92c7jp0ot5tzg0fmj8n00eba787qbpas47x./)

但其实社区已经把这条路趟过一遍了。

最近GitHub上有个项目挺有意思——claude-code-best-practice。它做了一件事：把社区验证过的Claude Code最佳实践，按“概念→功能→工作流→技巧”四个层次系统性地整理了出来。

它的口号很实在：“From vibe coding to agentic engineering—practice makes claude perfect”（从随性写代码到工程化Agent，熟能生巧）。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/73d9a56d35f2d409ddcd403677936e4a_MD5.webp)

有个数据挺能说明问题：开源不到两个月，GitHub Star数突破了54.1k。不到60天拿下5万Star，这在工具类项目里算是相当猛的增长速度。

**最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。**

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/120fc0032d790118e773ec1a67b88378_MD5.webp)

01

它和官方文档有什么不同？

先搞清楚这个项目在生态里的位置。官方其实已经有一些资源了：

| 资源 | 立场 | 特点 | 适合谁 |
| --- | --- | --- | --- |
| Anthropic官方文档 | 官方说明书 | 概念全、案例少 | 想搞清楚“它能做什么” |
| Anthropic Cookbook | 官方示例 | 端到端demo，不踩坑 | 想看官方推荐怎么写 |
| claude-code-best-practice | 社区踩坑总结 | 避坑+多工作流对比 | 想知道“高手是怎么用的” |
| 个人教程 | 单一视角 | 深度参差不齐 | 看某个具体用法 |

这个项目的差异化很清楚——它不是教“会用”，是教“用对”。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/9ac5a524764108b73ee913be03ca6a21_MD5.jpg)

举个例子：官方文档告诉你/compact是干什么的；这个项目告诉你，上下文涨到300k-400k token时理解力会开始下降，最好维持在40%利用率以下，以及什么时候该压缩。后者才是研发真正想要的——踩过坑的人总结出来的真知。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/e3415148a9018e581714e7cf7e6c0289_MD5.png)

02

四大板块：从“能装什么”到“怎么避坑”

按照仓库的结构，整个项目分成四大块。

板块一：核心概念

涵盖了Subagents、Commands、Skills、Workflows、Hooks、MCP Servers、Plugins、Settings、Status Line、Memory这10个Claude Code的关键概念。每个概念都配了一个“最佳实践”按钮，点进去就是实战案例。

比如MCP Servers这块，它不仅讲协议规范，还会列出当前最值得装的MCP：chrome-devtools-mcp（让Claude调浏览器调试）、github-mcp（直接操作PR）、sequential-thinking（强制Claude分步推理）等。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/bb7d37dc81ae448e81e9dcaef5f09f99_MD5.jpg)

板块二：热门功能

紧跟Anthropic的最新beta功能——Ultrareview、Devcontainers、Channels、Ultraplan、Auto Mode、Computer Use、Agent SDK、Code Review、GitHub Actions、Agent Teams、Scheduled Tasks等。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/705192474df2d1d7b5287fa446ae49b8_MD5.jpg)

这块的价值在于“提前一步”。很多beta功能官方文档还没补全的时候，这个项目已经把第一批用户的实践整理出来了。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/5fd5d8ad745828305a165dffade15699_MD5.jpg)

板块三：开发工作流

这块特别实用。它把GitHub上最有名的13个Claude Code工作流（Superpowers、Everything Claude Code、Spec Kit、gstack、Get Shit Done等）放在一起做了对比。

每个工作流都标注了Star数、独特性、是否有Plan阶段、用了几个Subagents/Commands/Skills。一张表就能选出适合自己团队的工作流。

更重要的是，项目识别出了一个共同模式：Research → Plan → Execute → Review → Ship。所有真正跑得通的工作流，最后都收敛到了这五步——这是踩坑总结出来的规律。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/1ce1b8649a1db35e4c8b352bb854d01e_MD5.jpg)

里面还提到了一个跨模型组合：Claude Code写代码，Codex来评审。两个不同模型互相挑刺，比单一模型自审客观得多。这个组合我自己也在用，确实能挑出Claude自己看不出的边界问题。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/4f5a302b09317e8ff400481ae7d22bbb_MD5.jpg)

板块四：83条实战技巧

这是整个项目最值钱的部分。83条tips按15个分类整理：Prompting、Planning、Context、Session Management、Memory、Agents、Commands、Skills、Hooks、Workflows、Advanced Workflows、Git/PR、Debugging、Utilities、Daily practices。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/9eea27790a68669ac4870848014e6dbd_MD5.jpg)

调试板块里有几条特别有用：遇到问题先截图发给Claude、用chrome-devtools-mcp让Claude自己看控制台日志——很多时候Claude答不出来不是它笨，是你给的信息量不够。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/0af085a3a82e0cbabb95d11e506c17d8_MD5.jpg)

03

三条最值得抄走的技巧

83条全看一遍挺累的，挑三条研发同学立刻能用上的：

技巧一：上下文保持在40%以下，超过300k就压缩

项目里明确写了：“Context rot at ~300-400k tokens”——上下文超过300k之后，Claude的理解力开始打折，老指令会被新内容稀释。最佳实践是维持在总context的40%以下。

操作很简单：看到status line显示context利用率超过40%，就执行一次/compact。别等到爆了再压。

技巧二：Plan和Execute分阶段跑，中间稿别带过去

Research → Plan → Execute → Review → Ship这五步要分阶段跑。尤其是Plan阶段产出的中间稿，不要带到Execute阶段，否则会污染Claude的判断。

正确做法：Plan阶段结束后，把方案commit到一个markdown文件里。开一个新session，让Claude读这个markdown直接执行。新session = 干净的context。

技巧三：Hook用来强制纪律，不是用来“加功能”

很多新人把Hook当成“扩展功能”来用——这是错的。Hook真正的价值是强制工程纪律。

举个例子：设一个PostToolUse hook，只要Claude改了src/下的文件，就自动跑mvn test。这是Claude自己不会想起来做的事。

在多模块Spring Boot项目里特别有用——Claude改了一个模块的代码，自动触发该模块的单测，省掉“忘了跑测试就commit”这个最常见的坑。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/e3415148a9018e581714e7cf7e6c0289_MD5.png)

04

中文版怎么看？

claude-code-best-practice默认是英文的。如果想看中文版，不用去找翻译稿——直接去这个仓库的Pull Requests里找，社区已经有人提过中文PR。

作者一直没合并是因为更新太频繁，怕翻译跟不上。但英文每次更新后，社区的中文PR也会跟着更新，可以直接checkout那个PR的分支来用。

![图片](assets/%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%2060%20%E5%A4%A9%E6%96%A9%E8%8E%B7%2054k%20Star%EF%BC%8C%E5%89%8D%E5%90%8E%E7%AB%AF%E5%BC%80%E5%8F%91%E7%9B%B4%E6%8E%A5%E8%B5%B7%E9%A3%9E%E4%BA%86%EF%BC%81/02eb1de90fd203e3bb2a0586feaa4ac0_MD5.jpg)

05

最后

用Claude Code用得不顺手的同学，80%的问题不是工具本身的问题，而是不知道“高手是怎么用的”。而高手的经验过去散落在上百个公众号、几十个YouTube视频、一堆Twitter thread里。

这个项目把它们收敛到了一个仓库里。51k Star不是因为它做了什么新东西，而是因为它把“该怎么用对”这件事系统化了。

值得抽一个小时把“83条tips”扫一遍，挑三五条最适合自己工作流的，落到 [CLAUDE.md里。剩下的，等需要的时候再来翻。](http://claude.xn--md-kd5g.xn--,-mo6at9ds1bl5ac79eqdcxu2cba323j6rmzz1aj32b./)

开源地址： [https://github.com/shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)

```
—END—最近想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:推荐一个牛逼的RAG + MCP系统
```