---
title: "面试官皱眉：\"你懂 Vibe Coding，那你说superpowers和grill-me怎么选？\"，我：\"小孩才做选择，我全都要！\""
source: "https://mp.weixin.qq.com/s/S_aHaKALoOMukPaE3KFRFQ"
---
苏三说技术 *2026年8月4日 16:27*

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

> 面试官：你简历上写了"熟练使用 AI 编程工具"，那我问你，superpowers 和 grill-me 你怎么选？
> 
> 我：这俩又不是竞品，选什么选？grill-me 管"动手前想清楚"，superpowers 管"动手后做到位"，我全都要！
> 
> 面试官：（皱眉）……那你展开说说？

好，今天就来展开聊聊这个话题。

之前我写过一篇 [superpowers使用指南](https://mp.weixin.qq.com/s?__biz=MzU1Nzg4NjgyMw==&mid=2247552761&idx=1&sn=f8578f4ae1bf1aea5d0940f431330849&scene=21#wechat_redirect) ，介绍了它作为 AI 编程全流程方法论的强大之处。但 superpowers 再强，也解决不了一个根本问题—— **你需求都没想清楚，AI 怎么帮你写？**

这就是 grill-me 存在的意义。

简单一句话总结两者的关系：

| 工具 | 定位 | 介入时机 |
| --- | --- | --- |
| grill-me | 需求澄清 / 设计追问 | 编码 **前** |
| superpowers | 全流程开发方法论 | 编码 **中** |

一个帮你想清楚，一个帮你做到位。组合起来，才是完整的 AI 编程工作流。

## 最近建了几个AI技术交流群，扫描加我微信，备注：AI，即可进群交流和学习，获取AI最新咨询。

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/120fc0032d790118e773ec1a67b88378_MD5.webp)

## grill-me 简介

grill-me 出自 TypeScript 圈无人不知的大神 **Matt Pocock** 之手，是他开源的 **mattpocock/skills** 仓库中的一个 skill。这个仓库目前在 GitHub 上已经斩获 **178k+ Star** ，堪称 AI 编程 skill 领域的顶流。

### 核心理念

grill-me 的理念非常朴素： **在 AI 动手写代码之前，先让 AI 像面试官一样追问你，把需求/设计的每个分支都问清楚。**

你有没有遇到过这种情况：

- 跟 AI 说"帮我做个登录功能"，它噼里啪啦写了一堆，结果你根本不需要 OAuth
- 让 AI 设计数据库，它自作主张加了一堆你不需要的字段
- 写到一半发现方向不对，推倒重来

这些问题的根源都是： **需求没对齐就开干了。**

grill-me 就是来解决这个问题的。它会像一个严格的面试官一样，对你的计划进行结构化拆解，逐层追问每个设计分支，直到所有关键决策点都达成共识。

### Skill 本体

你可能会惊讶，这么强大的 skill，本体居然只有几行 prompt：

```
---
name: grill-me
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design, or mentions "grill me".
---

Interview me relentlessly about every aspect of this plan until
we reach a shared understanding. Walk down each branch of the design
tree resolving dependencies between decisions one by one.

If a question can be answered by exploring the codebase, explore
the codebase instead.

For each question, provide your recommended answer.
```

就这么短！但效果出奇地好。关键在于最后那句"provide your recommended answer"——AI 每问一个问题都会附上推荐答案，你只需要说"对"或者纠正它，对话效率极高。

### 适用场景

- 写 PRD 之前，先梳理清楚到底要做什么
- 让 AI 实现功能之前，先对齐设计决策
- 确定数据模型 / API 形状之前，先压力测试一下
- 多个设计决策相互依赖时，逐个解耦

### 与 superpowers 的关系

有人可能会问：superpowers 里不是也有 brainstorming skill 吗？跟 grill-me 有什么区别？

区别在于：

- **grill-me** 是"轻量级压力测试"——专注于一问一答的面试式追问，快速收敛设计决策
- **superpowers brainstorming** 是"全流程头脑风暴"——会生成视觉伴侣、架构图、数据模型等一整套产物

两者不冲突，甚至可以串联使用：先用 grill-me 快速收敛核心决策，再用 superpowers 展开详细设计。

## 安装

- 安装非常简单，一条命令搞定：
```
npx skills@latest add mattpocock/skills
```
- 由于 `mattpocock/skills` 是一个技能合集，运行命令后可以选择你需要的技能进行安装，我这里只选择了 grill-me 相关的 skill；
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/90e6abf3aae0ce91cc3c2ae25ab190f2_MD5.png)

- 选择完成后，还需要选择安装到哪个 AI 代理编程工具中，我这里选择的是 Claude Code；
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/d8b587aac4ab12363b184b7ca041d8dd_MD5.png)

- 之后选择技能的安装范围，是项目范围还是全局范围；
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/990c0603e5fe21e61346fbdf42dbe836_MD5.png)

- 安装完成后，输入 `/grill-me` 就可以找到对应的命令了。
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/b5f9dc1572c7a2b2488add12b743d25e_MD5.png)

## 使用

> 这里以开发一个 Markdown 编辑器为例，演示 grill-me 的追问过程。

- 在 Claude Code 中输入 `/grill-me 我想开发一个 Markdown 编辑器。` ，接下来，AI 就会化身"面试官"，开始对你的计划进行灵魂拷问；
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/81c9ea4315e7118ad088f77a5b04b67f_MD5.png)

- 例如第 5 个问题：你喜欢哪种编辑形态？不仅提供了 4 种不同的编辑形态，还对每个形态的优缺点做了介绍；
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/769d5303d4a6f58036706404053a62e1_MD5.png)

- 还有第 10 个问题：用什么前端框架和构建工具？同样提供了 4 种解决方案，还对最适合的方案添加了推荐；
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/8f5d8be1cb82b33c66788e7a47971b81_MD5.png)

- 使用 grill-me 之后，Claude Code 将反复追问你的需求，我这里它提出了一共 14 个问题，涵盖了项目开发的方方面面，整个过程大概花了 10 分钟；
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/fa12790fb73a5765cc5af5de0a122fd3_MD5.png)

- 最终 Claude Code 和我达成了完整的共识，就可以进入项目的实施阶段了；
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/be32af8f1f5a0564ab4740205f6b7a2a_MD5.png)

- 最终生成的编辑器支持实时预览、代码高亮、双栏滚动同步，完全覆盖了追问阶段确定的需求。
![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%E7%9A%B1%E7%9C%89%EF%BC%9A%E4%BD%A0%E6%87%82%20Vibe%20Coding%EF%BC%8C%E9%82%A3%E4%BD%A0%E8%AF%B4superpowers%E5%92%8Cgrill-me%E6%80%8E%E4%B9%88%E9%80%89%EF%BC%9F%EF%BC%8C%E6%88%91%EF%BC%9A%E5%B0%8F%E5%AD%A9%E6%89%8D%E5%81%9A%E9%80%89%E6%8B%A9%EF%BC%8C%E6%88%91%E5%85%A8%E9%83%BD%E8%A6%81%EF%BC%81/6231b01a38071ae54335c9fc7d2aadc1_MD5.png)

## 效果对比

**不用 grill-me：** 你说"帮我做个 Markdown 编辑器"，AI 可能直接给你搞一个带用户系统、云端同步、协作编辑的"全家桶"，写了两小时发现 80% 的功能你根本不需要。

**用了 grill-me：** 14 轮追问，10 分钟对齐所有设计决策，AI 拿着明确的共识去写代码，一次到位，不返工。

这就是"想清楚再动手"的力量。

## 总结

回到开头那个面试问题：superpowers 和 grill-me 怎么选？

答案是 **不需要选** 。它们解决的是不同阶段的问题：

- **grill-me** ：编码前的"需求压力测试"，用一轮深度追问换来零返工
- **superpowers** ：编码中的"全流程方法论"，从计划到执行到测试一条龙

完整的组合工作流是这样的：

```
grill-me（想清楚）→ superpowers brainstorming（补充细节）→ writing-plans（拆任务）→ tdd / subagent（执行）
```

小孩才做选择，我全都要！

## 项目地址

[https://github.com/mattpocock/skills](https://github.com/mattpocock/skills)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)