---
title: "AgentScope"
type: entity
tags: [框架, 多智能体, 阿里, Java/Python]
sources: ["raw/09-archive/太酷了，RuoYi Office：一套系统把 OA、CRM、ERP 全装进去.md"]
last_updated: 2026-11-24
---

## 定义
AgentScope 是面向多智能体应用的开发框架（阿里系开源，有 Python 与 Java 两套实现），提供消息传递、Agent 编排、工具调用与状态管理等能力，走"显式编排多 Agent 协作"的路线。

## 关键信息
- **定位**：多 Agent 编排框架，与 [[SpringAI]]（模型接入与工具调用基础设施）不是同一层——Spring AI 偏"零件箱"，AgentScope 偏"多 Agent 协作运行时"
- **在 RuoYi Office 中的用法**：[[AgentOS]] 把模型运行时做成可配置项，可在 Spring AI 与 AgentScope 之间切换，而**不影响上层已审核上架的业务能力**（业务接口与模型运行时解耦）
- **Java 版**：与 Spring 生态集成的 AgentScope Java 2.0 曾在库中作为独立来源记录（见 [[摘要-AgentScopeJava2.0发布]]）
- **选型提示**：单 Agent + 工具调用用 Spring AI 就够；需要多角色协作、显式消息路由与共享状态时再引入编排框架，避免为简单场景引入复杂度

## 关联连接
- [[SpringAI]] — 模型接入层（同场景可替换）
- [[AgentOS]] — 可切换运行时的实际案例
- [[RuoYiOffice]] — 宿主平台
- [[多智能体编排]] — 所属概念
- [[摘要-ruoyi-office-agentos实测]] — 来源
