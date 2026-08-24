---
title: "Unhobbling"
type: concept
tags: [AI产品, 模型能力, 产品设计, ProductOverhang]
sources: [raw/01-articles/2026-08-23-对话 Claude Code 之父：当模型越来越聪明，还在设计复杂工作流的人只是在假装做产品.md]
last_updated: 2026-08-24
---

# Unhobbling

## 核心定义
Hobbling 指模型本身正在做某件事，而产品却从中阻碍它。Unhobbling 就是拿掉这些阻碍，让模型的潜在能力变成可用、可收费的产品。与 [[ProductOverhang]] 是同一件事的两个方面。

## 实践方法
1. **每次新模型发布后做 Ablation**：删除 system prompt、skills、hooks 和工具，观察模型表现
2. **逐行加回**：只有当模型反复在同一处失败时，才把相应约束加回来
3. **不要过早添加指令**：模型每次使用都会读到指令，确保模型确实需要它
4. **Claude Code 的实践**：为 Opus 5 删除了超过 80% 的 system prompt，消融实验显示去掉 prompt 后模型反而更聪明

## 与传统工程的区别
传统工程：一开始就认真思考系统设计，搭建庞大精巧的系统，重新架构需数月甚至数年。
模型工程：模型像有生命的有机体，每代行为不同，需以经验性、科学性的方式对待——尝试、观察、迭代。

## 关联连接
- [[ProductOverhang]]
- [[AblationStudy]]
- [[BorisCherny]]
- [[ClaudeCode]]
- [[ContextEngineering]]
