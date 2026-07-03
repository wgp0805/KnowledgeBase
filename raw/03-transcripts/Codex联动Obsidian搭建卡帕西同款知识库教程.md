---
title: "Codex联动Obsidian搭建卡帕西同款知识库教程"
type: source
tags: [Codex, Obsidian, 知识库, Karpathy, 教程, B站视频]
sources: [https://www.bilibili.com/video/BV1MJVb6cETR/]
last_updated: 2026-07-02
---

# Codex 联动 Obsidian，搭建卡帕西同款知识库——手把手教程

> **来源**: B站视频 [Codex联动Obsidian，搭建卡帕西同款知识库，手把手教程](https://www.bilibili.com/video/BV1MJVb6cETR/)
> **UP主**: [Xuan_酱](https://space.bilibili.com/14848367)
> **时长**: 13分23秒 | **播放**: 16.3万 | **收藏**: 1.45万
> **发布日期**: 2025年（pubdate: 1780034906）

## 视频概述

十分钟，用 Codex + Obsidian 搭建 AI 大神 [Karpathy](https://github.com/karpathy) 同款可以"自生长"的知识库，帮你把信息的利用效率直接拉到 next level。

它能：
- 定时抓取热点
- 自动整理信息、定期复盘
- 让知识体系自动迭代生长
- 直接输出文档、PPT、视频等成果

## 视频章节

1. [视频内容简介](#1-视频内容简介)（0:00 - 0:45）
2. [自生长理论](#2-自生长理论)（0:45 - 1:36）
3. [软件安装与配置](#3-软件安装与配置)（1:36 - 2:52）
4. [阶段一：信息收集](#4-阶段一信息收集)（2:52 - 6:29）
5. [阶段二：知识处理迭代](#5-阶段二知识处理迭代)（6:29 - 8:34）
6. [阶段三：Skill管理](#6-阶段三skill管理)（8:34 - 10:13）
7. [阶段四：知识高效输出](#7-阶段四知识高效输出)（10:13 - 12:53）
8. [总结](#8-总结)（12:53 - 13:23）

---

## 1. 视频内容简介

UP主 Xuan_酱 介绍了如何使用 Codex（OpenAI 的 AI Agent 工具）配合 Obsidian 笔记软件，搭建一个类似 [Karpathy](https://github.com/karpathy) 个人知识库的"自生长"知识系统。

核心理念是：**让 AI 帮你自动完成知识的采集、整理、沉淀和输出**，而不是手动一条条地记笔记。

### 什么是"自生长"知识库？

传统知识库是人手动记录知识，而这个系统的核心在于：
- 知识来源自动抓取（RSS、网页、热点）
- 内容自动整理分类（Codex Agent 处理）
- 知识自动关联链接（Obsidian 双链）
- 成果自动输出（文档、PPT、视频等）

---

## 2. 自生长理论

### 核心理念

"自生长"（Self-Growing）知识库的本质是让知识体系具备**自我迭代**的能力：

1. **输入层**：自动从互联网获取信息（热点抓取、RSS订阅、网页剪藏）
2. **处理层**：AI 自动整理、分类、摘要、建立关联
3. **存储层**：Obsidian 作为本地 Markdown 知识库，持久化存储
4. **输出层**：自动生成报告、文档、PPT、视频等内容

### 为什么选择 Karpathy 的知识库作为范本？

[Andrej Karpathy](https://karpathy.github.io/) 是 AI 领域顶级科学家（前 Tesla AI 总监、OpenAI 创始成员），他的个人网站就是一个典型的自生长知识库：
- 用 Markdown 写作
- 所有文章互相链接
- 持续更新迭代
- 内容结构清晰

这正是我们想要搭建的系统形态。

---

## 3. 软件安装与配置

### 所需工具

#### 3.1 Codex（OpenAI）

[Codex](entities/Codex.md) 是 OpenAI 推出的桌面端 AI Agent 程序，正从编程 Agent 进化为"电脑工作系统"。

**安装方式**：
`ash
# Mac/Linux 一键安装
curl -fsSL https://chatgpt.com/codex/install.sh | sh

# npm 全局安装
npm install -g @openai/codex

# Homebrew (macOS)
brew install openai-codex
`

**前置条件**：
- Node.js >= 18
- ChatGPT Plus/Pro 订阅（/月起）

**核心能力**：
- 本地文件读写操作
- 命令行工具执行
- 持久记忆（agents.md）
- 插件系统（Browser Use、Computer Use 等）
- Skill 流程沉淀
- MCP 外部服务连接
- 自动化定时任务

#### 3.2 Obsidian

[Obsidian](entities/Obsidian.md) 是一款基于本地 Markdown 文件的笔记软件，核心特性：
- 双向链接（[[wikilink]]）
- 知识图谱视图
- 丰富的插件生态
- 本地存储，隐私安全

**安装**：从 [obsidian.md](https://obsidian.md) 下载对应平台的客户端。

---

## 4. 阶段一：信息收集

### 4.1 自动抓取热点

使用 Codex 的 Automation（自动化）功能，设置定时任务来抓取互联网热点信息：

**配置思路**：
1. 创建 Codex 的 Automation 定时任务
2. 设置抓取源（RSS、API、网页）
3. 定时执行抓取并保存到本地

**示例配置**（在项目的 gents.md 中）：
`markdown
## 自动化任务
- 每天上午 9 点抓取 Hacker News 热门技术文章
- 每周日 20 点整理本周知识并生成周报
`

### 4.2 RSS 订阅

Codex 可以通过读取 RSS 订阅源来自动获取内容：
- 技术博客 RSS
- 新闻网站 RSS
- YouTube/B站频道更新

### 4.3 网页剪藏

使用剪藏工具（如 [MarkDownload](https://github.com/marvinahlmark/mark-download)、[SingleFile](https://github.com/gildas-lormeau/SingleFile)）将网页保存为 Markdown 格式，存入知识库的 aw/ 目录。

---

## 5. 阶段二：知识处理迭代

### 5.1 摄入（Ingest）流程

将原始素材（raw 目录）转化为结构化知识（wiki 目录）：

`
raw/           →  原始素材（网页剪藏、RSS内容）
    ↓ ingest
wiki/          →  结构化知识（概念、实体、综合）
    ↓ lint     →  健康检查（修复死链、孤岛页面）
`

### 5.2 知识分类

将摄入的内容按类型分类存储：

| 目录 | 内容类型 | 命名规则 | 示例 |
|------|---------|---------|------|
| wiki/concepts/ | 概念、框架、方法论 | TitleCase | [[Agent]], [[Skill]] |
| wiki/entities/ | 人物、公司、工具、产品 | TitleCase | [[Codex]], [[Obsidian]] |
| wiki/sources/ | 原始素材摘要 | kebab-case | [[摘要-video-title]] |
| wiki/syntheses/ | 综合分析、对比报告 | kebab-case | [[codex-vs-claude-code]] |

### 5.3 双向链接

每个 wiki 页面必须包含 ## 关联连接 区域，使用 Obsidian 双链 [[页面名称]] 链接到其他相关页面，避免产生孤岛页面。

### 5.4 矛盾处理

如果新摄入的知识与旧知识冲突，不要静默覆盖：
1. 在新页面中新建 ## 知识冲突 区块
2. 将两种说法都保留并做对比
3. 标注各自的来源和时间

---

## 6. 阶段三：Skill 管理

### 6.1 什么是 Skill？

[Skill](entities/Skill.md) 是可复用的方法、流程和工具组合。在 Codex 中，Skill 是一组指令文件（SKILL.md），告诉 AI Agent 如何完成特定任务。

### 6.2 知识库必备 Skills

针对自生长知识库，需要配置以下 Skill：

#### ingest Skill（知识摄入）
- 扫描 aw/ 目录下未处理文件
- 提炼核心价值到 wiki/ 目录
- 更新 index.md（总目录）和 log.md（操作日志）
- 将源文件归档到 aw/09-archive/

#### query Skill（知识查询）
- 通过 index.md 定位相关文件
- 深度阅读后进行综合回答
- 使用 [[wikilink]] 标注引用来源

#### lint Skill（健康检查）
- 扫描 wiki/ 目录
- 找出孤岛页面（没有双链）
- 检测死链（链接不存在的页面）
- 发现未同步索引的文件

### 6.3 Skill 配置示例

在项目中创建 .codex/skills/ 目录，为每个 Skill 创建 SKILL.md 文件：

`markdown
---
name: ingest
description: 将 raw/ 目录下的原始资料编译到 wiki/ 中
---

# Ingest Skill

## 工作流程
1. 扫描 raw/ 目录下所有 .md 文件
2. 读取每个文件内容
3. 提炼核心知识点
4. 写入 wiki/ 对应分类目录
5. 更新 wiki/index.md
6. 更新 wiki/log.md
7. 将处理过的文件移至 raw/09-archive/
`

---

## 7. 阶段四：知识高效输出

### 7.1 自动生成文档

利用 Codex 的能力，从知识库中提取内容生成各种格式的文档：

- **技术报告**：从 wiki 中提取相关概念，自动生成报告
- **学习笔记**：按主题整理知识，生成学习路径
- **API 文档**：从代码注释和 wiki 中提取，生成文档

### 7.2 生成 PPT

使用 Codex 的 PPT 生成 Skill，可以将知识库内容转化为演示文稿：
1. 从 wiki 中提取核心知识点
2. 按照 PPT 结构组织内容
3. 自动生成幻灯片

### 7.3 生成视频

通过 Remotion 框架（React 视频），可以用代码生成视频内容：
- 将知识库内容转化为视频脚本
- 自动生成视频画面和字幕
- 批量生成系列教学内容

### 7.4 周报/月报生成

配置自动化任务，定期从知识库中提取本周/本月新增知识，自动生成总结报告。

---

## 8. 总结

### 完整架构图

`
┌─────────────────────────────────────────────────┐
│                  自生长知识库                      │
├──────────┬──────────┬──────────┬────────────────┤
│  输入层   │  处理层   │  存储层   │    输出层      │
│          │          │          │                │
│ RSS/API  │ Codex    │ Obsidian │ 文档/PPT/视频  │
│ 网页剪藏  │ Agent    │ Markdown │  周报/月报     │
│ 手动录入  │ 处理     │ 双链网络 │  知识图谱      │
└──────────┴──────────┴──────────┴────────────────┘
`

### 关键要点

1. **工具组合**：Codex（AI Agent）+ Obsidian（本地知识库）
2. **核心理念**：让知识体系"自生长"——自动采集、自动整理、自动关联、自动输出
3. **工作流**：raw → ingest → wiki → lint → output
4. **Skill 驱动**：用可复用的 Skill 封装工作流
5. **双向链接**：确保知识之间的关联性，避免孤岛

### 与传统笔记的区别

| 维度 | 传统笔记 | 自生长知识库 |
|------|---------|-------------|
| 信息采集 | 手动搜索记录 | 自动抓取热点/RSS |
| 知识整理 | 手动分类标签 | AI 自动分类关联 |
| 知识关联 | 手动添加链接 | 双向链接自动发现 |
| 内容输出 | 手动编写 | AI 自动生成文档/PPT/视频 |
| 维护成本 | 高（全靠人力） | 低（自动化为主） |

---

## 关联连接

- [[Codex]] — 核心 AI Agent 工具
- [[ClaudeCode]] — 对标产品
- [[Skill]] — 可复用流程封装
- [[automations]] — 定时自动化任务
- [[goals]] — 带验证器的长跑型任务
- [[AICoding]] — AI 辅助编程范式
- [[multi-agent-collaboration]] — 多 Agent 协作模式
- [[ReActAgent]] — 核心推理循环 Agent
- [[AgenticRAG]] — 智能体化 RAG
- [[ContextEngineering]] — 上下文工程
- [[规范驱动开发]] — Spec-Driven Development
- [[文本绘图]] — 可视化方法论
- [[摘要-40分钟学会Codex零基础教程]] — Codex 系统教程
- [[摘要-cherry-studio-knowledge-base]] — Cherry Studio 搭建个人知识库
- [[ai-programmer-survival-guide]] — AI 时代程序员生存指南
