---
title: "Ripgrep"
type: entity
tags: [搜索工具, Rust, CLI, ripgrep]
sources: [raw/01-articles/腾讯面试官："为什么 Claude Code 不用 RAG 检索代码，而是 grep？"我："因为...我也不知道"，他沉默了。.md]
last_updated: 2026-05-20
---

## 定义
用 Rust 编写的现代高性能命令行搜索工具，作者是 Andrew Gallant。Claude Code 的 Grep 工具底层实现。

## 关键信息

### 性能特点
- 基于 Rust 正则表达式引擎，作者花费两年半优化
- 使用 SIMD 指令集加速，搜索速度逼近内存带宽极限
- 中型代码仓库（数万文件）全文搜索约 200ms

### Agent 友好特性
- 默认递归搜索整个目录
- 自动跳过 .gitignore 列出的文件和二进制文件
- 输出结果自带文件名和行号

### Claude Code 封装
- 默认最多返回 250 行（`head_limit` 控制），防止撑爆上下文窗口
- 超时时丢弃最后一行不完整结果，返回已有部分
- 完全无结果才抛超时错误
- 设计哲学："尽力返回结果" vs RAG 的"要么成功要么失败"

## 关联连接
- [[摘要-为什么Claude-Code不用RAG检索代码]] — 来源
- [[ClaudeCode]] — 使用 ripgrep 的产品
- [[AgenticSearch]] — ripgrep 赋能的搜索范式
