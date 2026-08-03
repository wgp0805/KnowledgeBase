---
title: "DiscoveryLoopTax"
type: concept
tags: [概念, Token, Skill, 上下文]
sources:
  - raw/01-articles/12.7K Star，这个开源项目把整本书炼成 Skill.md
last_updated: 2026-08-03
---

## 定义
发现循环税（Discovery Loop Tax）：把「反复翻目录、定位章节、回头补上下文的成本」统称为一种隐性的上下文消耗。这个概念由 book-to-skill 项目作者提出，用于论证「按需加载」比「整本塞进上下文」更划算。

## 关键信息
- **本质**：反复翻找文档产生的 token 浪费 + 结果不稳定
- **book-to-skill 的测算**：针对一个具体问题，运行时加载约 4,000 token 核心 Skill + 约 1,000 token 相关章节；与整本书直接进上下文相比，输入 token 少 24~51 倍
- **限制**：与一次性的发现循环相比优势为 2.4~15.6 倍；发现循环本身是一个「模型」（可被优化）。临时读一次 PDF，直接让 Agent 读可能更省事
- **适用边界**：同一本书/同一套文档被反复查阅时，预编译的收益才显著

## 关联连接
- [[BookToSkill]] — 概念提出项目
- [[Skill]] — 按需加载的载体
- [[ContextManagement]] — 上下文管理
- [[渐进式披露]] — 相关的设计原则
- [[RAG]] — 另一种减少发现成本的方式
- [[摘要-book-to-skill]] — 来源
