---
title: "TreeSitter"
type: entity
tags: [解析库, AST, 增量解析, 开源]
sources: ["raw/09-archive/CodeGraph为什么突然这么火？.md"]
last_updated: 2026-07-20
---

## 定义

Tree-sitter 是一个高性能的增量解析库，支持多种编程语言的语法解析。它能增量更新 AST（抽象语法树），在代码修改时只重新解析变更部分而非全量重建。

## 关键信息

- **用途**：解析源码 AST，提取函数、类、方法、接口、路由、组件等节点
- **特性**：增量更新、多语言支持、高性能
- **应用**：CodeGraph 使用 tree-sitter 作为底层解析引擎，将代码解析为节点和边构建知识图谱
- **优势**：相比传统解析器，tree-sitter 支持增量解析，适合 IDE 和实时代码分析场景

## 关联连接
- [[CodeGraph]] — 使用 tree-sitter 解析代码
- [[摘要-codegraph-deep-dive]] — 来源
