---
title: "MartinFowler"
type: entity
tags: [人物, 软件架构, 规则引擎]
sources: [raw/01-articles/干掉if...else，推荐一个小而美的规则引擎.md]
last_updated: 2026-07-02
---

## 定义
Martin Fowler，知名软件架构师与作者，以对企业应用架构、重构、领域建模等领域的开创性著述著称。在规则引擎领域，他提出了一个被广泛引用的朴素定义。

## 关键信息
Martin Fowler 在经典文章中指出：
> "你可以自己构建一个简单的规则引擎。你只需要创建一组具有条件（condition）和操作（action）的对象，将它们存储在一个集合中，并运行它们来评估条件并执行操作。"

这一理念直接启发了 [[EasyRules]] 的设计——Easy Rules 提供 `Rule` 抽象来创建带条件和操作的规则，并用 `RulesEngine` API 运行一系列规则，正是对该定义的工程化落地。

## 关联连接
- [[EasyRules]] — 以其规则引擎理念为设计灵感的轻量级 Java 规则引擎
- [[规则引擎]] — 其定义所属的核心概念
- [[摘要-easy-rules-规则引擎]] — 引用其观点的来源摘要
