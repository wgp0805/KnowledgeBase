---
title: "多Agent共享记忆"
type: concept
tags: [Agent, 记忆, 协作]
sources: [raw/01-articles/2026-09-04-OpenViking 实战：把知识库、长期记忆和 Agent 技能统一到一个上下文文件系统.md]
last_updated: 2026-09-05
---

## 定义
多 Agent 共享记忆是指通过统一的上下文数据库（如 OpenViking），让不同 Agent 共享同一套用户偏好、历史事件、实体信息和工作经验，减少重复配置。

## 关键信息
- 记忆内容：用户偏好、重要事件、常用实体、Agent 工作经验、已确认的长期信息
- 共享方式：通过 viking:// URI 统一表示，不同 Agent 连接同一服务即可访问
- 价值：一个 Agent 记下的，其他 Agent 也能用；减少重复配置
- 技能也可共享：多个 Agent 可以共享同一套技能定义，减少重复安装和维护

## 关联连接
- [[OpenViking]] — 火山引擎开源项目
- [[AgentMemory]] — Agent 记忆系统
- [[上下文分层]] — OpenViking 分层机制
- [[摘要-openviking-agent上下文数据库]] — 来源
