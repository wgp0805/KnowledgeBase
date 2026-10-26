---
title: "LLMWiki分层架构"
type: concept
tags: [概念, LLM Wiki, 知识库, 架构, Schema]
sources:
  - raw/09-archive/2026-10-21-LLM wiki实战：用20篇文章做一个“管理数字分身”.md
last_updated: 2026-10-21
---

## 定义

LLM Wiki 的三层架构：把知识系统的原始素材、维护规则与编译产物分别放在三个互不越权的层里。核心目的是**保证溯源**（所有编译出的知识都能回溯到不可变的原始材料）与**保证一致性**（同一套规则约束所有页面形态）。

## 关键信息

### 三层职责

| 层 | 名称 | 核心原则 | 典型载体 |
|---|---|---|---|
| 第一层 | 原始数据层（Raw Layer） | **不可变**，LLM 只能读取绝不能修改 | `raw/` 目录下的原始文章、PDF、转录 |
| 第二层 | 规则约束层（Schema Layer） | 定义整个知识系统的维护规范 | `AGENTS.md` / `CLAUDE.md`（企业级项目中常直接作为系统提示词） |
| 第三层 | 知识编译层（Wiki Layer） | LLM 负责维护更新 | `wiki/` 下的结构化 Markdown 页面 |

### 第三层的页面分类
摘要、实体、概念、比较、概述、综合理解。每个知识文件都有标准 YAML 元数据头（类别、标签、知识来源、状态、创建及更新时间），以及与其它知识页面的关系链接。

### 人机分工规则
- **人**：定义规则、提供原始数据、负责价值审核与关键裁决
- **LLM**：负责知识编译层的维护更新

### 目录结构（参考实现）
```
knowledge/
├── schema.md
├── raw/papers/
├── templates/          # 与 wiki 子目录一一对应，保证同类型文件结构一致
│   ├── comparison.md / concept.md / entity.md
│   └── overview.md / source.md / topic.md
└── wiki/
    ├── comparisons/ concepts/ entities/ overviews/ sources/ topics/
    ├── index.md       # 全书目录，检索时的第一入口
    └── log.md         # 操作日志，核心原则：内容只增加，不替换
```

### 支撑目录的分工
- `schema.md`：指导 LLM 维护整个知识库的工作原则
- `templates/`：生成 wiki 时的参照模板，与 wiki 目录结构一一对应，便于维护管理
- `index.md`：知识索引，检索时快速定位目标内容
- `log/`：记录每次知识编译更新了哪些知识文件、主题内容是什么

> raw 与 wiki 内部的目录结构**没有固定标准**，可结合实际业务场景调整，不一定要遵循上述分类。

## 关联连接

- [[LLMWiki]] — 所属模式
- [[知识编译]] — 第三层的核心动作
- [[编译器模式vs解释器模式]] — 编译时 vs 运行时的判据
- [[RAG]] — 对照范式
- [[WeKnora]] — 内置了该 Schema 层的落地产品
- [[AndrejKarpathy]] — 理念提出者
- [[渐进式披露]] — 相近的按需加载思想
- [[摘要-llm-wiki-实战管理数字分身]] — 来源
