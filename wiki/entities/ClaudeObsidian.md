---
title: "ClaudeObsidian"
type: entity
tags: [实体, 知识库, Obsidian, 开源, 工具]
sources: [raw/01-articles/WorkBuddy搭建个人知识库保姆级教程.md]
last_updated: 2026-09-16
---

## 定义
`claude-obsidian` 是一个开源的知识库管理工作流工具，把 Obsidian 知识库的规则、检索脚本和一致性校验器封装成开箱即用的 CLI 工具，专为实现自生长知识库而设计。

## 关键信息

### 定位
- **进阶方案**：与"提示词直建法"相对，是更严密的工程化流程
- **适用场景**：长期维护数万字以上的复杂项目文档或行业知识库
- **优点**：有校验工具兜底，长期维护更省心

### 五大命令
| 命令 | 用途 |
|------|------|
| `init` | 新建知识库时初始化工作流 |
| `adopt` | 接管已有知识库 |
| `wiki-ingest` | 入库操作（读取 raw，写入 wiki） |
| `wiki-query` | 精准问答与溯源 |
| `wiki-lint` | 定期排查孤立页面和失效链接 |

### 与"提示词直建法"的选型
- **日常阅读笔记 / 刚开始尝试 AI 知识管理** → 提示词直建法（轻量易掌控）
- **数万字以上复杂项目文档 / 行业知识库** → `claude-obsidian` 工作流模块

### 底层思想
- 基于 Karpathy LLM Wiki 理念
- 与 [[OpenWiki]] 同属 LLM Wiki 工程实现
- 强调"为 Agent 写文档不是为人写文档"

## 关联连接
- [[LLMWiki]] — 底层理念
- [[Obsidian]] — 承载工具
- [[自生长知识库]] — 相关概念
- [[OpenWiki]] — 同类 LLM Wiki 实现
- [[WorkBuddy]] — 搭配使用的 AI 应用
- [[AGENTS-md]] — 宪法文件
- [[摘要-workbuddy-obsidian-知识库]] — 来源