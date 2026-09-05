---
title: "JBoltAI"
type: entity
tags: [AI框架, 企业, Java, 私有化]
sources: [raw/09-archive/JAVA中AI框架选型指南（2026）.md]
last_updated: 2026-06-08
---

## 定义
面向企业的 Java AI 应用开发框架，强调私有化部署、全链路可追溯、AgentRAG。网站: jboltai.com

## 关键信息
- 框架依赖: Spring Boot | Java 17+
- 核心特色：
  - **AgentRAG** — "理解→规划→检索→评估→再检索→生成"完整链路
  - **私有化部署** — Docker/K8s 全量本地运行
  - **知识库管理** — 自动分块、向量化、混合检索
  - **可视化工作流** — 拖拽式 Agent 编排
  - **审计日志** — 全链路追踪

### Skill 与 Agent 支持
- 无原生 Skill 抽象，提供平台级替代方案（Agent 模板 + 插件系统）
- AgentRAG 框架实现完整的推理链路，过程透明可追溯

## 关联连接
- [[RAG]] — 检索增强生成
- [[SpringAI]] — 底层框架生态
- [[摘要-java-ai框架选型指南-2026]] — 来源
