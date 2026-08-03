---
title: "BookToSkill"
type: entity
tags: [开源项目, Skill, 知识库, 工具]
sources:
  - raw/01-articles/12.7K Star，这个开源项目把整本书炼成 Skill.md
last_updated: 2026-08-03
---

## 定义
book-to-skill 是一个开源工具（作者 virgiliojr94），把 PDF、EPUB、DOCX、Markdown、HTML、RTF 等书籍/文档先本地提取正文，再由 Agent 整理成一套结构化、可安装的 Skill，让「Agent 读一次书」变成「一本书以后都能在工作里被调用」。

## 关键信息
- **数据**：截至 2026-07-30，GitHub 12,739 Star / 1,416 Fork；仓库 2026 年 5 月初创建，更新活跃
- **产物结构**：
  ```
  your-book-skill/
  ├── SKILL.md          # 核心心智模型 + 章节索引
  ├── chapters/         # 逐章 Markdown，按需加载
  ├── glossary.md       # 术语表
  ├── patterns.md       # 方法与模式清单
  └── cheatsheet.md     # 决策规则速查表
  ```
- **两段式流程**：① 本地文本提取（pdftotext → pypdf/pdfminer.six 回退，复杂技术书可选 Docling）；② Agent 整理（识别书名/作者/目录/章节，提炼框架、方法、反模式、例子，生成索引与清单）
- **更新模式**：支持 fold-in，新论文/章节/内部文档可增量并入已有 Skill，无需推倒重做
- **安装方式**：
  - Claude Code：`git clone https://github.com/virgiliojr94/book-to-skill.git ~/.claude/skills/book-to-skill`，然后 `/book-to-skill ~/path/your-book.pdf`
  - 其他宿主：`~/.copilot/skills/`、`~/.agents/skills/`；明确支持的宿主为 GitHub Copilot CLI、Amp、Claude Code
  - `pip install "book-to-skill[pdf,epub,docx]"` 仅安装提取 CLI，不注册 Agent Skill
- **测试**：163 项测试全部通过；README 识别约 4,424 token，检出 14 个章节级标题
- **适用场景**：同一本书/同一套内部文档被反复查阅时收益最大；临时读一次 PDF 直接让 Agent 读更省事
- **安全与版权**：生成 Skill 是对原书的结构化整理，受版权保护的书公开分发有风险；master 分支已加入生成 Skill 的安全扫描（提示性检查）

## 关联连接
- [[DiscoveryLoopTax]] — 核心设计概念
- [[Skill]] — 生成产物
- [[RAG]] — 对比方案（深 vs 广）
- [[ClaudeCode]] — 宿主
- [[渐进式披露]] — 按需加载原则
- [[摘要-book-to-skill]] — 来源
