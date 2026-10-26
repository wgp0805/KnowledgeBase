---
title: "ShowMe"
type: entity
tags: [Skill, 开源项目, AI表达, humanlayer]
sources: [raw/09-archive/2026-09-24 - 又一个神级 Skill，让 AI 少写字、多画图！.md]
last_updated: 2026-09-28
---

## 定义

show-me 是 `humanlayer/skills` 仓库（MIT 协议，约 4k Star）中的开源 Skill，用一份一百多行的 Markdown 输出规范约束 AI 编程助手的表达形式：解释问题时少写铺垫文字，能用图说清楚的就不用字。它不教 AI 新能力，只规定「怎么表达」。

## 关键信息

- **仓库**：github.com/humanlayer/skills（共 5 个 Skill，show-me 讨论度最高）
- **安装**：`npx skills add humanlayer/skills --skill show-me`，兼容 Claude Code、Codex、WorkBuddy、Trae、CodeBuddy 等支持技能机制的工具
- **调用**：`/show-me`，或说「内容太多了，给我看」；追加 `as an html explainer` 生成网页讲解
- **七八种表达形式**：逻辑用伪代码、调用关系用缩进调用栈树、前端结构用组件树、多方交互用 Mermaid 时序图、方案对比用 diff、复杂概念生成独立 HTML 讲解页；总约束是「挑最小视图说清关键点，别堆砌」
- **背景**：作者 Dex Horthy 因模型表达冗长（Reddit 前 CEO 亦公开吐槽 Claude 说话风格）而打磨；HTML 讲解功能致谢 [[MattPocock]] 的 /teach
- **边界**：图由 AI 绘制可能出错（小众框架易漏模块、编造调用），需回代码核实；Skill 只管表达形式，方案本身错误时图反而更易取信于人
- HumanLayer 团队内部称 HTML 页面已大幅替代 Figma 做原型

## 关联连接
- [[Skill]] — 所属技能机制
- [[Skills]] — Skills 生态
- [[MattPocock]] — HTML 讲解页灵感来源
- [[程序员追风]] — 介绍文章作者
- [[摘要-show-me-少写字多画图]] — 来源
