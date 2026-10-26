---
title: "摘要-ai-coding组件库三路接入"
type: source
tags: [来源, 原始文件, AI-Coding, 组件库, MCP, Skills]
sources: [raw/09-archive/2026-10-19-AI Coding中组件库的接入技巧+保姆级指令案例！.md]
last_updated: 2026-10-20
---

## 核心摘要
元尧结合大厂项目经验，给出 AI Coding 接入组件库的三种路径及可复制的项目初始 Prompt：① **npm 包**——让 AI 真正调用组件真实代码（未装包时 AI 只是手写 CSS 模仿样式，没有交互逻辑/无障碍/主题系统），适合可交付前端产品，Prompt 要点：所有组件优先从组件库引用、禁止自己用 HTML/CSS 重实现、禁止装 antd 等其他库、不确定 API 先问；② **MCP**——给 AI 开放动态查询文档的接口，核心价值是**及时更新信息、少用过时 API**（前提：组件库有 MCP Server，如 Ant Design 官方 MCP），规则：写组件前必须 `_get_component` 拿文档不得凭记忆、严格按返回 Props、deprecated 时换替代组件；③ **Skills**——给 AI 的工作指导手册，不提供代码，约束风格与流程（设计原则/命名规则/使用限制），制作门槛最低，适合视觉 Demo 与规范传达。三者本质区别：npm 包=运行时组件代码，Skills=静态上下文了解背景，MCP=动态查询最新文档，不冲突可三层叠加，优先级为 MCP 查询 > Skills 文档 > 训练记忆。维护策略建议：短期先用低门槛 Skills，质量稳定后再让前端发 npm 包。

## 关联连接
- [[AICoding]] — 所属开发范式
- [[MCP]] — 动态文档查询通道
- [[AgentSkills]] — 静态规范约束通道
- 元尧 — 作者（公众号：长弓小子）
