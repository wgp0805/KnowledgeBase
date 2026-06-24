---
title: "夯爆了！Claude Code 最佳实践开源了， 狂斩 57k+ Star，核心玩法、工作流、Agent 等一网打尽！！"
source: "https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487757&idx=1&sn=1ebdb09e42a9620c1c49b437fe393f8a&scene=21&poc_token=HIx6O2qjJGCxuBd430I1t-zlPd3ZP-bfKWQDdT5k"
---
R哥 AI技术宅 *2026年6月9日 09:41*

大家好，我是R哥。

最近 Claude Code 的热度还是很高啊，这篇《 [Claude Code 官方桌面端正式发布，夯爆了！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487743&idx=1&sn=ea660ae13ff3b6058c2aed89e8c82aeb&scene=21#wechat_redirect) 》都几万阅读了，而且各大社区关于 Claude Code 的讨论也一直很活跃。

可是，很多人拿到 Claude Code 就开始让它写代码了，很多理念、功能都没有真正弄明白，所以没有发挥 Claude Code 的真正功力。

最近 GitHub 上又火起来一个 Claude Code 开源项目： **claude-code-best-practice** ，号称 Claude Code 的最佳实践，目前已经 **57k+** Star 了。

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/d86b6e3469bba4c11c0dfa97d72b3447_MD5.webp)

这个项目把 Claude Code 生态里已经被社区验证过的一批经验做了系统整理，比如： **核心能力、热门功能、工作流、日常开发避开等等** ，全部分类总结出来了。

废话不多说了，直接上干货

## claude-code-best-practice

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/b3f490e2ac63aa55705bbaa035b5d525_MD5.webp)

### 1、核心能力

这个项目把 Claude Code 里最关键的能力进行分类了：

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/bc63c8f52c1c3d5e359d8fbe814ef7de_MD5.webp)

这块适合所有刚开始上手 Claude Code 的人，各个核心能力都提供了最佳实践的使用方法，包括 **Subagents、Commands、Skills、Workflows、Hooks、MCP Servers、Plugins，……** 等。

### 2、热门功能

这个项目还对 Claude Code 热门功能进行了分类总结：

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/de19e8e5d80344630f381578ffb2ca75_MD5.webp)

里面包括 **Ultrareview、Devcontainers、Channels、Ultraplan、No Flicker Mode、Auto Mode、Power-ups、Fast Mode、Computer Use** 、…… 等等。

这些高级功能对前后端团队很实用，因为 Claude Code 真正好用，不是只靠模型聪明，而是要和你现有的工程环境接起来。

### 3、工作流

#### 编排工作流

这个仓库里有一个很值得看的部分： **Orchestration Workflow** 。

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/ce71e3602fdeb5c440c447e407c66bc5_MD5.webp)

它讲的是 **Command → Agent → Skill** 这种组合方式， **Command 负责触发任务，Agent 负责扮演角色，Skill 负责提供专业能力** ，这也是 Claude Code 系统工程化的关键。

它还提供了一个天气系统如何编排的工作流，演示了怎么让 Claude Code 结合 Skills、工具调用、记忆等多种能力，完成一个复杂的工作流任务。

#### 开发工作流

仓库里还整理了一批主流的 Claude Code 开发工作流项目：

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/1659847a65979f2dbd7e440070cde45a_MD5.webp)

比如 **Superpowers、Everything Claude Code、Matt Pocock Skills、Spec Kit、gstack、Get Shit Done、OpenSpec** 等等，所有主要工作流都使用的是同一个套架构模式：

> Research → Plan → Execute → Review → Ship

也就是， **先研究，再计划，再执行，再审查，最后交付** 。

用好这些特别重要，很多人用 Claude Code 不会提效，一上来就让它写代码，结果做出来的东西完全不是自己想要的，因为它不知道你想做成什么样，所以就可能达不到你的预期。

所以比较稳的做法是： **先让 Claude 读项目和需求，输出方案；方案确认后，再开新阶段执行；执行完成后，再进入 Review 和测试阶段** 。

这套流程对前后端都适用，说白了，Claude Code 不是不能干复杂的活，而是必须拆阶段进行，这样才能达到效果。

#### 跨模型工作流

什么是跨模型工作流？

也就是将 Claude Code 与其他模型一起使用，比如： **Codex、Gemini、GPT、Kimi、DeepSeek、本地模型** 等等，它们主要通过这三种机制：

- • 插件 — 另一个模型的 CLI 在 Claude Code 内部运行。
- • MCP — Claude Code 通过 Model Context Protocol 将另一模型作为工具调用。
- • 路由器 — Claude Code 的 API 端点已切换到不同的提供商。

目前仓库收集了以下 4 种跨模型工作流：

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/40f0a1c3b504e5b49456297dc3e9a132_MD5.png)

比如，我前段时间分享的《 [炸裂！OpenAI 把 Codex 装进了 Claude Code！！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487627&idx=1&sn=9a734159f4f6774297cabc5eb42029a3&scene=21#wechat_redirect) 》这篇文章，讲的就是 `codex-plugin-cc` 这个项目。

### 4、SKILL / AGENT 精选集

仓库整理了一批 SKILL / AGENT 精选集，以下按星级从高到低排序。

**Skills 精选集：**

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/97a5d7a8b64de9738a772f95e96c9512_MD5.png)

**AGENT 精选集：**

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/8e20a6915c6face2dd956bff89263906_MD5.png)

### 5、实战技巧

这个项目最适合收藏反复看的，其实是 83 条实战技巧。

仓库整理了大量日常开发建议，覆盖 **Prompting、Planning、Context、Session Management、Memory、Agents、Commands、Skills、Hooks、Workflows、Git/PR、Debugging、Utilities、Daily practices** 等方向。

拿 **CLAUDE.md +.claude/rules** 为例：

![图片](assets/%E5%A4%AF%E7%88%86%E4%BA%86%EF%BC%81Claude%20Code%20%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5%E5%BC%80%E6%BA%90%E4%BA%86%EF%BC%8C%20%E7%8B%82%E6%96%A9%2057k+%20Star%EF%BC%8C%E6%A0%B8%E5%BF%83%E7%8E%A9%E6%B3%95%E3%80%81%E5%B7%A5%E4%BD%9C%E6%B5%81%E3%80%81Agent%20%E7%AD%89%E4%B8%80%E7%BD%91%E6%89%93%E5%B0%BD%EF%BC%81%EF%BC%81/9852627f41c7ff1434cde28315a0e6b3_MD5.png)

比如，第 1 条 Tip 就告诉我们 CLAUDE.md 的每个文件应目标在 200 行以下，第 2 条 Tip 告诉我们 claude/rules/\*.md 会在每个会话中自动加载。

掌握这 83 条最佳实战技巧，能让你在使用 Claude Code 的时候少走很多弯路。

> 这篇就不一一解读了，下篇我再单独拿出来分享，关注我第一时间分享。

## 总结

如果你只是偶尔让 Claude Code 写个小功能，那这个项目可能没那么大的必要。

但如果你已经开始用 Claude Code 做前端页面、后端接口、Bug 修复、代码重构等复杂任务，那这个仓库非常值得抽时间好好看一遍。

不用一口气全学完，可以分步骤慢慢来：

- • 先看 Concepts，搞清楚 Claude Code 到底有哪些能力。
- • 再看 Workflows，看看高手是怎么做工作流系统的。
- • 最后看 Tips，把最佳实践规则进行项目的落地。

至少不要把 Claude Code 当成聊天机器人来使用，最基本的比如： **agents、commands、skills、hooks** 等这些都是必须要掌握的，要学会如何将它们组装成你自己的工作流程当中。

所以，Claude Code 本身已经很强，但真正决定上限的，是你怎么使用它。

好了，今天就暂时分享到这里了， **R哥持续分享更多 AI 好玩的东西** ，公众号第一时间推送，关注「 **AI技术宅** 」公众号和我一起学 AI，下期见。

> ⚠️ **版权声明：**
> 
> 本文系公众号 "AI技术宅" 原创，未经授权禁止转载，严禁搬运、抄袭、洗稿、侵权一律投诉，并保留追究其法律责任的权利。

< END >

推荐阅读：

[Claude Code 官方桌面端发布，夯爆了！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487743&idx=1&sn=ea660ae13ff3b6058c2aed89e8c82aeb&scene=21#wechat_redirect)

[Codex 手机端发布，远程操控电脑夯爆了！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487676&idx=1&sn=18a22835bc1fd0ba75a047d0a4b3e870&scene=21#wechat_redirect)

[从夯爆到夯，锐评 7 个主流 AI 编程模型！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487663&idx=1&sn=0b7de8d3f7a2a6ed1673746d31d57713&scene=21#wechat_redirect)

[Claude Code 成本爆降 92% 开源工具！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487651&idx=1&sn=a7e7c1b4bee4061bd84c47d96f8c59b4&scene=21#wechat_redirect)

[OpenAI 把 Codex 装进了 Claude Code！！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487627&idx=1&sn=9a734159f4f6774297cabc5eb42029a3&scene=21#wechat_redirect)

[OpenClaw 在国内的热度彻底凉了。。](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487555&idx=1&sn=00e47c77348c3d8b403e77456268487a&scene=21#wechat_redirect)

[Claude Code 创始人亲授的 10 条核心玩法](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487178&idx=1&sn=6151407183a6115de139090d19abedb9&scene=21#wechat_redirect)

[Codex 独立 APP 发布，免费用户也能使用！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487162&idx=1&sn=6427120c78781636707035edd75a2c61&scene=21#wechat_redirect)

[玩转 CodeX CLI 的 16 个实用小技巧！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247485761&idx=1&sn=ec9520c75cfee3d81b5e75f289ad8ced&scene=21#wechat_redirect)

[玩转 Claude Code 的 23 个实用小技巧！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247485524&idx=1&sn=dfabb331208e1b3cef651ec766c9f618&scene=21#wechat_redirect)

更多 ↓↓↓ 关注公众号 ✔ 标星⭐ 哦