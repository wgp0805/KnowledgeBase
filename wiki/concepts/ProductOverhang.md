---
title: "ProductOverhang"
type: concept
tags: [AI产品, 模型能力, 产品设计, Unhobbling]
sources: [raw/01-articles/2026-08-23-对话 Claude Code 之父：当模型越来越聪明，还在设计复杂工作流的人只是在假装做产品.md]
last_updated: 2026-08-24
---

# Product Overhang

## 核心定义
模型已经具备某种能力，但现有产品没有把这种能力释放出来，形成的能力积压。由 Anthropic 的 Boris Cherny 在 YC 对谈中提出。

## 核心思想
- 模型（不是未来模型，而是当前已存在的模型）能做很多我们尚未意识到的事情
- 产品反而"挡住"了模型（Hobbling），没有让模型展现能力
- Product Overhang 与 Hobbling 是同一件事的两个方面

## 经典案例
**Claude Code 的诞生**：Sonnet 3.5 时代，编程产品只做单行补全和聊天（只读不写）。模型已能一次写完整文件，但没有产品释放这个能力。Claude Code 拿掉所有限制，给模型最简单的 harness，让它直接写完整文件甚至完整功能——这就是 unhobble Sonnet 3.5。

## 创业机会
Boris Cherny 认为，当今现代模型存在大量 Product Overhang，但很少有创业公司真正把这些能力转化出来。真正的机会不是继续堆叠工作流，而是拿掉妨碍模型发挥的设计。

## 如何发现 Product Overhang
1. 给模型布置比你认为它能做到的稍微更难的任务
2. 不要给过于具体的指令，说明目标、约束和完成标准后放手
3. 做实验，随意玩模型，尝试创造性的事情
4. 案例：给 Opus 5 提供 OpenCV 让它绘图，它画得相当不错（未专门训练）

## 关联连接
- [[Unhobbling]]
- [[BorisCherny]]
- [[ClaudeCode]]
- [[AI产品]]
- [[Harness]]
