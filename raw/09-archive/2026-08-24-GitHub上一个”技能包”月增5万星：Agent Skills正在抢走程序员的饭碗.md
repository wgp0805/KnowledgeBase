---
title: "GitHub上一个”技能包”月增5万星：Agent Skills正在抢走程序员的饭碗"
source: "人人都是产品经理"
url: "https://www.woshipm.com/ai/6453589.html"
date: "Mon, 24 Aug 2026 10:46:02 +0000"
score: 1.0
tags: ["产品经理", "AI产品", "Agent", "中文"]
auto_captured: true
---

# GitHub上一个”技能包”月增5万星：Agent Skills正在抢走程序员的饭碗

> **来源**: 人人都是产品经理  
> **链接**: https://www.woshipm.com/ai/6453589.html  
> **抓取日期**: 2026-08-24  
> **相关性评分**: 1.0

> GitHub 日榜上，Skills 类项目正以惊人速度抢占原本属于大模型新版本的位置。SKILL.md 文件让 Agent 即插即用，一次编写处处复用，成为团队资产。本文拆解 Skills 爆火背后的经济学，揭示三大踩坑点，并给出消费者、创作者、团队负责人的上手路径。

![](https://image.woshipm.com/wp-files/2026/08/Yw3NETnFmF7KwwT7wuKW.png)

上周刷到 GitHub 日榜的时候很震惊，感觉AI的发展太疯狂了。因为三件事同时挤进了同一个榜单的顶部，而它们不是一个东西，是一类东西。

**obra/superpowers，GitHub 总星 27.49 万，单日新增 749。****JuliusBrussee/caveman，GitHub 总星 9.95 万，单日新增 309。****almendili/skills，新建仓库前 25。**

共同点是格式。三家都用同一种结构打包”技能”，一个叫 SKILL.md 的文件，让 Claude Code、Codex、Cursor、Gemini CLI 这些工具即插即用。

而就在 8 月 21 日同一天，稀土掘金一篇拆解文章里提到一个更狠的数字：**mattpocock/skills 单月增星 50,486** 。一个月 5 万。

我不知道你有没有意识到这个数字意味着什么。意味着 GitHub 全站的月榜 TOP 里，有一种东西正在吃掉原本属于”大模型新版本”、”Agent 框架”、”AI 工具新特性”的位置。它，叫**Skills** 。

## 为什么 Skills 突然在 8 月集体爆了

回头看 8 月，Skills 类项目组成了 GitHub 的”技能星光谱”。

![](https://image.woshipm.com/2026/08/24/b17f2eba-9f8f-11f1-a999-00163e09d72f.png)

**“ 给 Agent 的提示词工程”，正在从一段随手粘贴的 system prompt，演化成一个有生产、分发、消费、复用链条的”技能生态”。**

8 月 11 日，Anthropic 官方 skills 仓库（约 17 万星，2025 年 9 月创建）和 Addy Osmani 的 agent-skills 同日登榜。8 月 19 日，Anthropic-Cybersecurity-Skills（817 个安全技能，映射 MITRE ATT&CK 等 6 大安全框架）以日榜第 5 的成绩刷屏，当日新增 726 star。

技能仓库正在从”小众玩法”变成”日榜常客”，从”单个技巧”变成”成体系的工程资产”。

翻译成人话：**当大模型开始按 token 收费的时候，最值钱的不是模型，是那些写一次就能反复套用的 SKILL.md 文件。**

## SKILL.md 到底是什么？

技能（skill）和提示词（prompt）的本质区别在哪儿？在结构化上。

一个完整的技能仓库长这样：

> my-skill/
> 
> ├── SKILL.md # 技能声明：触发条件、适用场景、指令正文
> 
> ├── scripts/ # 可执行脚本（Shell/Python/PowerShell）
> 
> └── references/ # 参考文档，按需加载

乍一看很朴素。但它的真正革命性，是**SKILL.md 就是 Agent 的 ”函数签名”**。

你写代码的时候，函数签名告诉你三件事：函数叫什么、参数是什么、返回什么。

你写一个 SKILL.md，Agent 读到的时候也能立刻知道三件事：**这个技能在什么场景下触发，做什么事，遵守什么边界。**

Karpathy 那个被点 20 万次的 Skills 项目，本质上就是一个精心写的 CLAUDE.md，告诉 Agent：”如果你要帮我写代码，下面这些坑你必须先看一眼—Python 类型注解怎么写、什么时候不要用 async、测试覆盖率怎么定义……”

这是**一份可以挂在你 Claude Code、Cursor、Codex 上的代码标准规范。**

Addy Osmani 把 Chrome 团队资深工程师十几年的代码审查流程，打包成一个 Skills 仓库，结果 8.9 万人点星。为什么？因为他在解决一个具体问题，**Code Review 在 AI 时代怎么做** 。

不是”教 AI 写代码”，而是”给 AI 一份可以照着做的流程清单”。

## Skills 经济学：模型是租的，技能是自己的

为什么 Skills 类项目在 8 月集中爆发？

一个长期被忽略的事实是：**模型能力是租的，技能是自己的。**

模型按 token 付费。你给它一次提示，它回你一次回答。下次再问，又得给一次。这是水电费。

技能不一样。一旦你写好一个 SKILL.md，不管 Claude Code、Codex、Cursor、还是某个新出的 CLI 工具，只要它兼容 Agent Skills 规范，就能即插即用——**一次编写，处处复用。**

这就是 Skills 的真正经济学。

当一个团队的 Claude Code 都装上同一套 code review 技能、部署技能、写提交信息的技能时，”技能库”就成了团队资产——就像当年的 wiki 和内部的脚拉工具一样。**只不过这次消费它们的是 AI。**

mattpocock 是 JavaScript/TypeScript 圈熟脸，著名前端工程师。他那个 5 万星项目，本质是他把自己十几年生产环境踩过的坑，打包成 Claude/Gemini/Codex 通用的”代码自检技能包”。你想用 JavaScript，给 Claude Code 装上；切到 Python，装另一个；做 React，装第三个。

不是 model 在变强。**是你的工具箱在变厚。**

而工具箱的价值，会跟着团队沉淀越来越多。

## 三大踩坑点：Skills 不是越多越好

听到这你可能热血沸腾，”那我马上写 100 个 SKILL.md，让 Claude 装上不就行了？”

现实没那么美好。

**踩坑点一：选择困难症**

每个技能都占上下文窗口（或者至少占用检索时的注意力）。装一堆低质量技能，Agent 会犯选择困难症。

i-have-adhd 这个项目能拿 1.5 万星，反向证明了大家被 Agent 的啰嗦输出折磨得有多惨。”ADHD 友好输出”本质就是个技能——告诉 Agent：”回答直接放第一段，别铺垫八段。”

**装 30 个技能，不如精挑 5 个最常用的。**

**踩坑点二：质量参差**

技能本质是”指令 + 脚本”，也就是说——**它能执行任意代码。**

这就引出第三个最致命的坑。

**踩坑点三：安全边界**

Anthropic 在 8 月上线 claude-plugins-community 仓库时，专门规定：所有插件必须经过官方自动化安全扫描才能分发，直接提交的 PR 会被自动关闭。

但 Skills 生态远不止官方仓库。GitHub 上随便一个 SKILL.md 都可能让你的 Agent 执行恶意脚本。

稀土掘金的拆解文章说得很准：**Skills 不是越多越好，质量参差是当前生态最大的坑。**

## 上手路径：消费者 / 创作者 / 团队负责人

不管你是写代码还是不写代码，推荐下面三条路径上手。

### 消费者

别装了，找对的那几个。

  * **程序员** ：mattpocock/skills（JS/TS）、obra/superpowers（开发方法论）、Karpathy Skills（编码规范）。
  * **产品 / 运营** ：Addy Osmani 的 agent-skills（内容审查流程）、caveman（电报式极简输出）。
  * **安全 / 测试** ：Anthropic-Cybersecurity-Skills（817 个安全技能）。



先去 Claude Code / Cursor 装两三个，先感受一下”工具箱变厚”是种什么体验。

### 创作者

你会写两件事：一份 SKILL.md，一段脚本。

**SKILL.md 写三件事** ：

  1. **触发条件** ：什么时候该用这个技能？（”当用户要求发布文章时”）
  2. **指令正文** ：Agent 该做什么？（”按三段式结构撰写，结尾必须有金句”）
  3. **边界** ：什么不该做？（”严禁编造数据，严禁涉及政治人物”）



**脚本写一件事** ：能跑的、能在你 Claude Code 上立刻工作的。

写完了挂到 GitHub，被点星不是目的，被人用才是。我也把我常用的经验写成了技能，这样我在不同的平台，不管是Claude Code、hermes、workbuddy，都用相同的一套技能也避免了风格不统一，https://github.com/ZOORO-NEW就是我在github上建的一个仓库，放上了我常用的技能，在使用过程中还可以不断更新。

### 团队负责人

别让团队每个人都去网上找 Skills。

**建一个内部 skills 仓** 。

把团队统一的：

  * 代码规范
  * 测试标准
  * 提交信息格式
  * 部署流程
  * 内容审核 checklist



全部打包成 SKILL.md，沉淀在一个 Git 仓库里。所有人的 Claude Code / Codex / Cursor 都从同一份来源拉。

**这就是 2026 年的团队脚手架。**

## 最后

2024 年我们写提示词。2025 年我们调模型。2026 年下半年开始——**我们沉淀技能** 。模型可以换，工具可以换，但一支团队、一个个人多年积累的 SKILL.md 仓库，是带不走的资产。

记住，模型能力是水，技能是池。模型可以升级，可以替换；但你的技能库一旦建好，就是任何模型来了都能立刻调用的杠杆。

工具会拉平执行力的差距。

**但永远拉不平，技能库的厚度。**

本文由@前进ing 原创发布于人人都是产品经理。未经许可，禁止转载。

题图来自作者提供


---
> 原文链接: https://www.woshipm.com/ai/6453589.html