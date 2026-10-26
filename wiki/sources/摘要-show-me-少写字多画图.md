---
title: "摘要-show-me-少写字多画图"
type: source
tags: [来源, 原始文件]
sources: [raw/09-archive/2026-09-24 - 又一个神级 Skill，让 AI 少写字、多画图！.md]
last_updated: 2026-09-28
---

# 摘要-show-me-少写字多画图

## 核心摘要

show-me 是 humanlayer/skills 仓库（MIT，约 4k Star）中的一个开源 Skill，作用是让 AI 编程助手解释问题时少写字、多画图。它不教 AI 任何新本事，整个技能就是一份一百多行的 Markdown 输出规范，规定七八种表达形式并按问题类型选用：讲逻辑用伪代码、调用关系画成缩进调用栈树、前端结构用组件树、多方交互用 Mermaid 时序图、方案对比用 diff、复杂概念直接生成可双击打开的 HTML 讲解页，并要求「挑最小视图说清关键点，不要堆砌」。安装方式为 `npx skills add humanlayer/skills --skill show-me`，对话里 `/show-me` 或说「内容太多了，给我看」即可触发，加 "as an html explainer" 出网页版。作者 Dex Horthy 因模型表达冗长而打磨此 Skill，网页讲解功能致谢 Matt Pocock 的 /teach；使用注意两点：AI 画图可能画错（需回代码核实）、图只解决表达形式，方案本身靠不住时图更可信反而容易带偏。

## 关联连接
- [[ShowMe]] — 该文介绍的开源 Skill 实体
- [[Skill]] — 所属技能机制
- [[Skills]] — Skills 生态
- [[MattPocock]] — HTML 讲解页功能的启发来源（/teach）
- [[程序员追风]] — 文章作者
