---
title: "Claude 又开源了一款新插件，让你的 Claude Code 满血复活！"
source: "https://mp.weixin.qq.com/s/luZGXAiaR0djV1oVGoQYiw"
---
Java技术栈 *2026年6月24日 14:31*

大家好，我是R哥。

不知道你有没有这种感觉， **身边人都在吹 Claude Code 多强多神** ，可自己装上之后， **就只会和它普通聊天发任务指令** ，问一句答一句，丝毫感受不到「 **神** 」在哪。

其实问题不在工具， **而是你只用了它三成的功力** 。

Claude Code 真正的杀手锏，是背后那一整套自动化能力，也就是 **hooks、subagents、skills、MCP、斜杠命令** ，这些配好了，它才算真正「 **满血** 」。

可惜大部分人压根不知道怎么配，也懒得配，于是一身本事被硬生生用成了聊天框。

好消息来了，Anthropic 官方最近又开源了一款插件，名字就叫 **claude-code-setup** ，专门来治这个病。

如果你想系统掌握 Claude Code 的核心玩法，也可以看看这篇：

> [夯爆了！Claude Code 最佳实践开源了， 狂斩 57k+ Star，核心玩法、工作流、Agent 等一网打尽！！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487757&idx=1&sn=1ebdb09e42a9620c1c49b437fe393f8a&scene=21#wechat_redirect)

## claude-code-setup

### 基本介绍

一句话概括下，claude-code-setup 它就是项目的 Claude Code 一键配置工具。

![图片](assets/Claude%20%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E6%AC%BE%E6%96%B0%E6%8F%92%E4%BB%B6%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84%20Claude%20Code%20%E6%BB%A1%E8%A1%80%E5%A4%8D%E6%B4%BB%EF%BC%81/485071e4bc063c13e1df4968cdb72c55_MD5.png)

它背后是通过「 **claude-automation-recommender** 」这个 Skill 来完成的。

你把它装上，让它扫一遍你的项目，它就会根据你这个项目的实际情况， **有针对性地告诉你该配哪些自动化** ，每一类只挑最值得上的一两个，不让你对着一堆选项瞎折腾。

另外， **它是只读的** ，全程只分析、只建议，绝不乱动你一个文件，用着踏实。

那它到底推荐些啥？

也就是 Claude Code 最核心的五块能力：

- • **MCP Servers** ：外部能力接入，比如查最新文档的 context7、跑前端测试的 Playwright；
- • **Skills** ：打包好的专业技能，比如 Plan 规划、前端设计；
- • **Hooks** ：自动触发的动作，比如保存时自动格式化、自动 lint、拦截敏感文件；
- • **Subagents** ：专职审查子代理，比如安全审查、性能审查、无障碍审查；
- • **Slash Commands** ：一键工作流，比如 `/test` 跑测试、 `/pr-review` 审代码、 `/explain` 讲逻辑。

看明白了吧？这 5 块内容才是 Claude Code 区别于普通对话工具的关键。

更绝的是，它推荐的还都是跟你项目匹配的配置，前端项目它给你推前端测试和设计相关的，后端项目它就推后端开发和安全相关的。

### 快速安装

进入 Claude Code 后一行命令搞定：

> /plugin install claude-code-setup@claude-plugins-official

或者直接 `/plugin > Discover` 里翻到它点一下，效果一样。

安装好后它就会出现在 **Installed** 下面：

![图片](assets/Claude%20%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E6%AC%BE%E6%96%B0%E6%8F%92%E4%BB%B6%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84%20Claude%20Code%20%E6%BB%A1%E8%A1%80%E5%A4%8D%E6%B4%BB%EF%BC%81/de8de19b4b7460bfa1644b0b7c974200_MD5.png)

Claude 桌面版也能安装，进行「 **Code** 」 面板，点击「 **Customize** 」 菜单，然后在「 **Personal plugins** 」中点击「 **Browse plugins** 」，然后再搜索安装即可：

![图片](assets/Claude%20%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E6%AC%BE%E6%96%B0%E6%8F%92%E4%BB%B6%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84%20Claude%20Code%20%E6%BB%A1%E8%A1%80%E5%A4%8D%E6%B4%BB%EF%BC%81/aec39f2634bcd822c6a00c0dccab0fc3_MD5.png)

Claude Code 官方桌面端的安装和使用看这篇：

> [Claude Code 官方桌面端正式发布，夯爆了！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487743&idx=1&sn=ea660ae13ff3b6058c2aed89e8c82aeb&scene=21#wechat_redirect)

### 使用指南

装好之后更不用费脑子，你都不用记什么复杂指令，直接用自然语言发送指令就行，比如：

- • 帮我 set up claude code
- • 帮我看看这个项目该配哪些自动化
- • 我该用哪些 hooks？

它就会自动扫描项目代码，把推荐清单一条条列给你，剩下的照着配就完事了，新手也能十分钟搞定。

比如我拿一个从未用过 Claude Code 的后端项目让它分析下：

> **帮我 set up claude code**

以下是分析结果：

![图片](assets/Claude%20%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E6%AC%BE%E6%96%B0%E6%8F%92%E4%BB%B6%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84%20Claude%20Code%20%E6%BB%A1%E8%A1%80%E5%A4%8D%E6%B4%BB%EF%BC%81/6078aa8ae77dfa7f765c10fcdc735c96_MD5.png)

![图片](assets/Claude%20%E5%8F%88%E5%BC%80%E6%BA%90%E4%BA%86%E4%B8%80%E6%AC%BE%E6%96%B0%E6%8F%92%E4%BB%B6%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84%20Claude%20Code%20%E6%BB%A1%E8%A1%80%E5%A4%8D%E6%B4%BB%EF%BC%81/6966c48026cf40b287260df82421f6ba_MD5.png)

它只是给出了推荐清单，包括项目文档、MCP、Hooks、Skills、Subagents，全给我一一推荐了，但它并不会帮我直接配好，要实现哪几点你再告诉它，它才会动手配置。

感觉怎么样？这样按它的推荐清单配置好后，项目才会变得有活力，Claude Code 也会满血复活。

## 总结

说实话，Claude Code 这工具最大的门槛从来都不是贵， **而是大多数人根本不知道它能这么玩** 。一身的本事，结果被当成普通聊天机器人，实在太可惜。

说实话， **claude-code-setup** 这配置工具还是挺实用的，至少让新手可以少走弯路，老手也能拿它查漏补缺。

要是你也觉得自己的 Claude Code 一直没发挥出真本事，不妨装上它扫一遍。 **工具买了就得用满，别再让你的 Claude Code 一直半血上阵了。**

所以，Claude Code 本身已经很强，但真正决定上限的，是你怎么使用它。

推荐阅读： [Claude Code 创始人亲授的 10 条核心玩法（建议收藏）](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487178&idx=1&sn=6151407183a6115de139090d19abedb9&scene=21#wechat_redirect)

好了，今天就暂时分享到这里了， **R哥持续分享更多 AI 好玩的东西** ，公众号第一时间推送，关注「 **AI技术宅** 」公众号和我一起学 AI，下期见。

> ⚠️ **版权声明：**
> 
> 本文系公众号 "AI技术宅" 原创，未经授权禁止转载，严禁搬运、抄袭、洗稿、侵权一律投诉，并保留追究其法律责任的权利。

< END >

推荐阅读：

[Claude Code 最佳实践开源，一网打尽！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487757&idx=1&sn=1ebdb09e42a9620c1c49b437fe393f8a&scene=21#wechat_redirect)

[Claude Code 官方桌面端发布，夯爆了！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487743&idx=1&sn=ea660ae13ff3b6058c2aed89e8c82aeb&scene=21#wechat_redirect)

[从夯爆到夯，锐评 7 个主流 AI 编程模型！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487663&idx=1&sn=0b7de8d3f7a2a6ed1673746d31d57713&scene=21#wechat_redirect)

[Claude Code 成本爆降 92% 开源工具！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487651&idx=1&sn=a7e7c1b4bee4061bd84c47d96f8c59b4&scene=21#wechat_redirect)

[OpenClaw 在国内的热度彻底凉了。。](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487555&idx=1&sn=00e47c77348c3d8b403e77456268487a&scene=21#wechat_redirect)

[Claude Code 创始人亲授的 10 条核心玩法](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487178&idx=1&sn=6151407183a6115de139090d19abedb9&scene=21#wechat_redirect)

[Codex 独立 APP 发布，免费用户也能使用！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487162&idx=1&sn=6427120c78781636707035edd75a2c61&scene=21#wechat_redirect)

[玩转 CodeX CLI 的 16 个实用小技巧！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247485761&idx=1&sn=ec9520c75cfee3d81b5e75f289ad8ced&scene=21#wechat_redirect)

[玩转 Claude Code 的 23 个实用小技巧！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247485524&idx=1&sn=dfabb331208e1b3cef651ec766c9f618&scene=21#wechat_redirect)

更多 ↓↓↓ 关注公众号 ✔ 标星⭐ 哦