---
title: "Token级记忆"
type: concept
tags: [Agent, Memory, 上下文工程, 实现方案]
sources: [raw/09-archive/2026-10-12-一文搞懂 Agent Memory：AI 是如何记住你说过的话的？ - Tomorrowland_D.md]
last_updated: 2026-10-13
---

## 定义
Token-level Memory（外部文本记忆）是目前普通 Agent 应用开发最值得关注的记忆方案：**把记忆表示为可读取的内容，保存在外部存储中，需要时重新放进 Prompt**。整个过程不修改模型参数。综述论文《Memory in the Age of AI Agents》将其与 Latent Memory、Parametric Memory 并列为三大实现方向。

## 关键信息

### 三种记忆形态对比
| 形态 | 机制 | 适用 |
|------|------|------|
| **Token-level** | 外部文本 + 检索后注入 Prompt | 商业 LLM API 开发者的首选，最实用起点 |
| Latent Memory | KV Cache 复用、历史状态压缩、隐式记忆表示 | 需访问模型底层推理机制，API 开发者不可控 |
| Parametric Memory | Fine-tuning / LoRA / 知识编辑 | 领域适配与行为调整，不适合频繁更新的配置 |

用户把数据库从 PostgreSQL 换成 MySQL 时，没必要为它微调一次模型——这正是 Token-level 的适用边界。

### 数据结构三选
- **扁平结构**：每条记忆独立存储，关键词或向量检索（初学者与小型 Agent 的推荐起点）
- **图结构**：实体与关系连接，适合多跳查询
- **层级结构**：按主题和粒度组织（项目摘要 → 模块信息 → 具体事件）

### 生命周期三环节
- **Write**：摘要式 / 提取式 / 结构化写入，工程上常把摘要与事实提取结合
- **Maintain**：合并相似记忆、更新过期值（可保留历史版本与生效时间）、删除临时与过期内容
- **Retrieve**：BM25（术语、文件名）、Embedding（语义）、Hybrid、Reranking、查询改写；**原则是越相关越准确越好，不是越多越好**

### 落地建议
最小实现只需 Markdown 文件目录 + 四个 Function Calling 工具（`save_memory` / `search_memory` / `update_memory` / `delete_memory`）；遇到检索瓶颈再上向量库与图结构。

## 关联连接
- [[AgentMemory]] — 上位概念
- [[Agent记忆三型]] — 功能分类
- [[上下文工程]] — 相关工程域
- [[RAG]] — 检索技术基础（Memory 不止检索）
- [[摘要-一文搞懂agent-memory]] — 来源
