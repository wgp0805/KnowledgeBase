---
title: "摘要-一文搞懂agent-memory"
type: source
tags: [来源, Agent, Memory, 记忆系统, 认知科学]
sources: [raw/09-archive/2026-10-12-一文搞懂 Agent Memory：AI 是如何记住你说过的话的？ - Tomorrowland_D.md]
last_updated: 2026-10-13
---

## 核心摘要
Tomorrowland_D 系统讲解 Agent Memory 的科普长文，回答三个主线问题：**记什么、存在哪里、如何运转**。核心论点：Memory 不是让上下文窗口变大，而是让 Agent 在有限 Context Window 中**有选择地利用历史信息**；Memory 也不修改模型权重，而是外部信息的提取、持久化与重新注入。

## 关键信息

### 三类记忆（借鉴认知科学）
| 类型 | 回答的问题 | 典型内容 |
|------|------|------|
| 情景记忆 Episodic | 发生过什么？ | 历史任务、对话记录、工具调用轨迹、成功经验与失败教训 |
| 语义记忆 Semantic | 什么是事实？ | 用户偏好、项目配置、领域知识（跨会话仍有效） |
| 程序记忆 Procedural | 应该怎么做？ | 工作流、操作规范、调试策略 |

三类不互斥："上次测试失败是因为 Redis 没启动，今后测试前先检查 Redis"同时含情景与程序记忆。

### 三种存储形态（引自综述《Memory in the Age of AI Agents》）
- **Token-level Memory（外部文本记忆）**：记忆表示为可读取内容存外部存储，需要时塞回 Prompt。商业 LLM API 开发者的首选；数据结构可分扁平 / 图 / 层级
- **Latent Memory（模型内部状态）**：KV Cache 复用、历史状态压缩等，需访问底层推理机制，商业 API 开发者用不到
- **Parametric Memory（模型参数）**：Fine-tuning / LoRA / 知识编辑，适合领域适配，不适合频繁更新的项目配置

### 记忆生命周期三环节
- **Write 写入**：摘要式（压缩长对话，可能丢细节）、提取式（抽取独立事实，便于精确更新）、结构化（实体/属性/时间戳/来源，成本高）。工程上常把摘要与事实提取结合
- **Maintain 维护**：合并（相似记忆去重）、更新（PostgreSQL 迁到 MySQL 就替换旧值，可保留历史版本与生效时间）、遗忘（临时任务、过期配置、用户要求删除的信息；不能简单按访问频率判断价值）
- **Retrieve 检索**：BM25（文件名、函数名、专有术语）、Embedding（语义）、Hybrid Search、Reranking、查询改写。**不是检索越多越好，越相关越准确才好**——无关记忆进上下文反而干扰判断

### 三个主流方案
| 方案 | 理念 | 特点 |
|------|------|------|
| MemGPT / [[Letta]] | Agent 自主管理记忆（Context Window=RAM，外部存储=磁盘） | Core / Recall / Archival 三层，灵活但质量受 Agent 决策能力影响 |
| Mem0 | 把记忆封装为独立服务 | 自动提取、查找、保存/维护、检索；能力随版本变化 |
| [[ClaudeCode]] | 文件系统记忆 | `CLAUDE.md` 持久化指令 + Auto Memory + `MEMORY.md` 索引，透明、简单、易维护；量大后遇到检索与维护成本问题 |

### 边界辨析
- **Memory ≠ RAG**：RAG 从外部知识源检索增强回答；Memory 关注信息如何产生、保存、更新与复用。RAG 可作为 Memory 的检索基础，但 Memory 还包括写入与维护
- **Memory ≠ 持续学习**：大多数系统实现的是"系统层面经验积累"，模型参数并未更新
- **Memory 不是越多越好**：过时信息干扰、记忆冲突、检索噪声、成本上升

### 最小可用实现四步
Markdown 文件目录（`MEMORY.md` 索引 + project / preferences / experiences）→ 提供 `save_memory`/`search_memory`/`update_memory`/`delete_memory` 工具 → 新会话先加载索引、按需 search → 定期合并/更新/删除。遇到检索瓶颈再上 Embedding、BM25、向量库或图结构。

## 关联连接
- [[AgentMemory]] — 核心概念
- [[Agent记忆三型]] — 三类记忆分类
- [[Token级记忆]] — 最实用的存储形态
- [[Mem0]] — 自动化记忆服务
- [[Letta]] — Agent 自主管理路线
- [[ClaudeCode]] — 文件系统记忆路线
- [[长期记忆]] — 相关概念
- [[RAG]] — 技术重叠但不等同
