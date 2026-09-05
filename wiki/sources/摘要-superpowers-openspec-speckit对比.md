---
title: "摘要-superpowers-openspec-speckit对比"
type: source
tags: [AI编程, 规范驱动, 工程纪律, 对比]
sources: [raw/01-articles/Superpowers、OpenSpec、Spec-Kit 傻傻分不清楚.md]
last_updated: 2026-06-26
---

## 核心摘要

苏三系统对比了三个总 Star 接近 40 万的 AI 编程治理工具：**Superpowers**（238K Star，14 Skill + 五阶段流程，强制工程纪律，解决"怎么干"）、**OpenSpec**（46K+ Star，Delta-Based 增量规格 + DAG 工件依赖图，轻量规范管理，解决"改了什么"，对棕地项目最友好）、**Spec-Kit**（115K+ Star，GitHub 官方出品，七阶段流水线 + `constitution`/`spec`/`plan`/`tasks`，让规范可执行，解决"按什么规矩干"，更适合绿地项目）。三者并非"三选一"，理想组合是：用 Spec-Kit 定项目宪法 → 用 OpenSpec 管每次变更生命周期 → 用 Superpowers 强制执行纪律。文中还介绍了将 OpenSpec 与 Superpowers 组合的 Comet 工具。

## 关联连接

- [[Superpowers]] — 技能驱动工作流
- [[SpecKit]] — GitHub 官方规范驱动工具
- [[OpenSpec]] — 增量规格管理框架
- [[VibeCoding]] — 三者共同要解决的"乱写代码"现象
- [[规范驱动开发]] — 共同的方法论根基
- [[Skill]] — 三者均围绕 Skill/规范 文档展开
- [[ClaudeCode]] — 主要承载平台
