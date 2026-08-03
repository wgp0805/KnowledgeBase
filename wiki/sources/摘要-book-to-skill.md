---
title: "摘要-book-to-skill"
type: source
tags: [来源, Skill, 知识库]
sources:
  - raw/01-articles/12.7K Star，这个开源项目把整本书炼成 Skill.md
  - raw/01-articles/就一个skill，凭啥6wstar？.md
  - raw/01-articles/为什么越来越多人用MapStruct.md
  - raw/01-articles/面试官：SpringBoot 在打包部署的时候打包成 jar 和 war 有什么不同.md
last_updated: 2026-08-03
---

## 核心摘要
- book-to-skill 是一个 GitHub 开源项目（截至 2026-07-30 达 12,739 Star / 1,416 Fork），理念是把整本书「预编译」成结构化、可安装的 Agent Skill，替代「整本 PDF 塞进上下文」的一次性问答方式。
- 生成结果是一个 Skill 目录：主 `SKILL.md`（核心心智模型 + 章节索引）+ `chapters/` 逐章 Markdown + `glossary.md`（术语表）+ `patterns.md`（方法与模式清单）+ `cheatsheet.md`（决策规则速查表）。按需加载相关章节，不必每轮对话背着整本书跑。
- 与 RAG 的本质区别：RAG 擅长「广而浅」地在大批文档中找相似片段；book-to-skill 是「深而专」的知识编辑，适合反复查阅的少量高价值材料。
- 效率测算：作者引入「Discovery Loop Tax」（发现循环税）概念，针对具体问题运行时约加载 4,000 token 核心 Skill + 1,000 token 相关章节，相比整本书入上下文，输入 token 少 24~51 倍（与一次性发现循环相比优势为 2.4~15.6 倍）。
- 安装分两条路线：克隆仓库到 `~/.claude/skills/`（注册 `/book-to-skill` Agent Skill）；或 `pip install book-to-skill`（仅文本提取 CLI，不注册 Skill）。文本提取优先 pdftotext，回退 pypdf/pdfminer.six，复杂技术书可选 Docling。
- 注意事项：章节标题规范才切分稳；生成 Skill 是对原书的结构化整理，涉及版权边界；任何外部文档转 Agent 指令的流程都要防提示注入。

## 关联连接
- [[BookToSkill]] — 本项目
- [[DiscoveryLoopTax]] — 核心概念
- [[Skill]] — 生成产物类型
- [[RAG]] — 对比方案
- [[ClaudeCode]] — 支持的宿主
- [[渐进式披露]] — 按需加载的设计原则
- [[程序员追风]] — 文章作者
