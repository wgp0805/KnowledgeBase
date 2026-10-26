---
title: "BalanceSkillCreators"
type: entity
tags: [工具, 开源项目, Skill, 生成器, WorkBuddy]
sources: ["raw/09-archive/2026-10-23-腾讯司内实践：手把手教你如何用 Skill 与 AI 协作.md"]
last_updated: 2026-10-26
---

## 定义
BalanceSkillCreators 是腾讯产品经理 [[BalanceLi]] 开发的三个 Skill 生成器工具组（Learning/Design/Build，仓库 balancegsr/skill-creators），面向三类高频工作场景按需生成"专属子 Skill"。

## 关键信息
- 三个生成器对应三类场景：**Learning**——理解陌生领域、学会作出有依据的判断；**Design**——想清目标和限制、形成可供评审的方案；**Build**——实现 Skill 或 Demo、检查结果是否满足目标。已上线腾讯司内市场。
- 公开获取地址：https://github.com/balancegsr/skill-creators/tree/main/learning（skill-creator-learning）。
- 两步工作流：① 澄清需求（主题/目标/基础/时间/偏好，一次提供四项信息减少来回补问；只说"精通 AI"会继续追问"具体想用来做什么"），生成 SKILL.md + 配套指南并预览，确认时重点看三件事——**目标是否符合需要、内容有没有超出范围、练习方式是否合适**；② 交付方式二选一：直接安装到当前工作空间（马上用）或打包 ZIP（转移/分享，需在新环境完成安装并确认能调用）。
- 生成的专属子 Skill（示例名 learn_rag_review）包含项目背景、流程与保存规则，会按项目进展引导下一步：设计中发现新信息与原判断矛盾→建议重新检查需求或方案；开发中测试发现问题→回头检查设计或技术选择。
- 三生成器可配合使用，但**需要按任务选择、不会自动依次运行**；Build 生成器先交付一份指导构建工作的 Skill，再按其引导制作、测试业务 Skill 或 Demo。
- 双模式：按预计投入时间推荐**轻量模式**（短期集中学一个主题；学习点较多时才建议复盘；结项通常生成简要总结）或**完整模式**（分模块持续学习；每个模块默认复盘；结项生成认知框架）。换主题时重新用 Learning 生成器生成新项目 Skill（英语示例：先练文字表达，发音口语还需语音工具支持）。

## 关联连接
- [[摘要-腾讯skill协作balance-li]] — 主要来源
- [[BalanceLi]] — 三个生成器的开发者
- [[meta-skill]] — 生成器模式所属的元技能概念
- [[SkillCreator]] — Anthropic 官方元技能（同类工具对照）
- [[WorkBuddy]] — 生成器与子 Skill 的运行平台
- [[学习闭环五步法]] — Learning 生成器落实的核心方法论
