---
title: "Obsidian"
type: entity
tags: [笔记软件, Markdown, 知识管理]
sources:
  - raw/09-archive/Codex联动Obsidian搭建卡帕西同款知识库教程.md
  - raw/01-articles/WorkBuddy最值得推荐的15个技能（9月最新版）.md
  - raw/01-articles/WorkBuddy搭建个人知识库保姆级教程.md
last_updated: 2026-09-16
---

## 定义
基于本地 Markdown 文件的笔记软件，以双向链接（wikilink 语法）和知识图谱为核心特性，广泛用于个人知识管理（PKM）。

## 关键信息
- 本地存储，隐私安全，无需云端依赖
- 核心特性：双向链接、知识图谱视图、丰富的插件生态
- 可通过 [[Codex]]、[[WorkBuddy]] 等 AI Agent 实现知识自动采集、整理、输出
- 支持 Canvas 画布（[[ObsidianCanvas]]）可视化笔记关系
- 知识库操作技能包括 ingest（摄入）、query（查询）、lint（健康检查）

### 与 AI Agent 联动的知识库模式
- **Codex 版本**：早期教程，见 [[摘要-codex-obsidian-自生长知识库]]
- **WorkBuddy 版本**：苏三 2026-09-16 分享的保姆级教程，用 WorkBuddy + Obsidian 搭建自生长知识库，三层极简目录 + AGENTS.md 宪法 + 每次入库更新 index.md 和 log.md（见 [[摘要-workbuddy-obsidian-知识库]]）
- **开源工作流**：进阶可接入 `claude-obsidian`（见 [[ClaudeObsidian]]），命令包括 `init` / `adopt` / `wiki-ingest` / `wiki-query` / `wiki-lint`

### 相关 Skills
- **Obsidian Skills**（kepano）：让 AI 按 Obsidian 的规则管理知识库，支持创建修改笔记、建立双链、生成数据视图、绘制 Canvas 画布，还可以把网页内容整理后保存进知识库（见 [[摘要-workbuddy-15技能推荐]]）

## 关联连接
- [[摘要-codex-obsidian-自生长知识库]] — 来源（Codex 版本）
- [[摘要-workbuddy-obsidian-知识库]] — 来源（WorkBuddy 版本）
- [[摘要-Obsidian保姆级入门教程]] — 来源（入门教程）
- [[自生长知识库]] — 关联概念
- [[LLMWiki]] — 底层理念
- [[ObsidianCanvas]] — 相关功能
- [[ClaudeObsidian]] — 进阶工作流工具
- [[Codex]] — 联动 AI Agent
- [[WorkBuddy]] — 平民实现载体
- [[marka]] — 同类本地优先 Markdown 编辑器
