---
title: "checkpoint-rebuild"
type: concept
tags: [AI Agent, 上下文管理, 记忆, MiMo Code]
sources: [raw/01-articles/小米版Claude Code正式发布，这次开源能给到夯.md]
last_updated: 2026-06-11
---

## 定义
Checkpoint/Rebuild 是一种上下文窗口管理机制，通过分段持久化和重建上下文实现逻辑会话的无限延伸。在窗口到达上限前的固定位置（checkpoint）派 writer Sub-agent 将结构化状态写入磁盘，窗口接近上限时执行 rebuild 切换新窗口。

## 关键信息
- **Checkpoint**：在窗口上限前的固定位置介入，派出独立的 writer Sub-agent 读取所有对话，将结构化状态并发写入磁盘，不阻塞主 Agent
- **Rebuild**：窗口接近上限时，切断当前窗口，用已持久化的文件作为种子重建新窗口上下文
- **Cycle**：一段被 checkpoint 打过点、最终以 rebuild 收尾的对话轮次序列
- **无数量上限**：每个 cycle 受限于物理窗口大小，但逻辑会话是 cycle 的链，没有最大长度

### 四层记忆体系
Writer 维护一个分层记忆体系，每层不同生命周期：

1. **Session 记忆**（`checkpoint.md`）— 只在当前逻辑会话内存活，记录完整工作状态
2. **Project 记忆**（`MEMORY.md`）— 项目级持久知识库，保存架构决定、用户规则、技术事实
3. **Global 记忆** — 用户级偏好，跨项目生效
4. **History** — 完整 SQLite 轨迹，每条消息和工具调用原文存储，不作为结构化索引

### 便签本机制
主 Agent 可随时追加零散发现，writer 在每次 checkpoint 时读取并将其路由到对应结构化字段后清空。主 Agent 不需要操心信息该放哪个字段，只管随手记下来。

## 关联连接
- [[MiMoCode]] — 所属产品
- [[ContextManagement]] — 上下文管理更广泛的概念
- [[AgentHarness]] — Harness 记忆主题
- [[Agent]] — Agent 上下文管理
- [[摘要-mimo-code发布]] — 来源
