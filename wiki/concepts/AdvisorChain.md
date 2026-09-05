---
title: "AdvisorChain"
type: concept
tags: [Spring AI, Agent, 职责链, 模式]
sources: [raw/01-articles/Spring AI 2.0 高效开发 Agent， 我总结了九条经验。。。.md]
last_updated: 2026-07-06
---

## 定义
Advisor 链（Advisor Chain）是 Spring AI 2.0 的职责链模式实现，将 Agent 的横切关注点（记忆、RAG、工具调用、审计日志）拆分为独立 Advisor，通过链式组合实现职责分离。

## 关键信息

### 内置 Advisor
| Advisor | 作用 |
|---------|------|
| `MessageChatMemoryAdvisor` | 自动读写会话历史 |
| `QuestionAnswerAdvisor` | RAG 检索增强 |
| `ToolCallingAdvisor` | 工具调用循环（框架自动注册） |
| 自定义 Advisor | 审计日志、权限校验、敏感词过滤 |

### 执行顺序
- 通过 order 值控制执行优先级
- 自定义 Advisor 的 order 设得比 ToolCallingAdvisor 更高（数值更大），则会在工具循环"内部"被触发

### 典型组合
记忆 + RAG 作为默认 Advisor 注册到 ChatClient.Builder，所有对话自动获得多轮记忆与知识检索能力，无需在每次调用时手动配置。

## 关联连接
- [[SpringAI]] — 所属框架
- [[ChatClient]] — 聊天客户端入口
- [[ChatMemory]] — 对话记忆管理
- [[RAG]] — 检索增强生成
- [[FunctionCalling]] — 工具调用
- [[摘要-spring-ai-2-agent-tips]] — 来源
