---
title: "KV Cache压缩"
type: concept
tags: [概念, Agent, 压缩, 技术]
sources: [raw/01-articles/2026-09-01-Agent上下文管理概述-1 - Big-Yellow-J.md]
last_updated: 2026-09-01
---

## 定义
处理Transformer每层的Key和Value的压缩技术，目标是在生成过程中只保留一部分历史KV，主要用于降低显存占用和提高推理效率。

## 关键信息
- 严格意义上不太算是上下文压缩策略，更偏向模型运行状态压缩
- StreamingLLM发现attention sink现象：保留起始token的KV能够恢复windows attention的效果
- 起始token有更高的注意力分数，即便在语义上已经不重要
- 操作方式：在计算windows attention时将开始的n个token保留（测试llama-2中n=4）

## 关联连接
- [[摘要-Agent上下文管理概述]] — 来源文章
- [[Agent上下文管理]] — 核心概念
- [[上下文压缩]] — 关键技术
- [[KVCache]] — 相关概念
