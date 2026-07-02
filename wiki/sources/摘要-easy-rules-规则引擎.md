---
title: "摘要-easy-rules-规则引擎"
type: source
tags: [来源, 原始文件, 规则引擎, Java]
sources: [raw/01-articles/干掉if...else，推荐一个小而美的规则引擎.md]
last_updated: 2026-07-02
---

## 核心摘要
苏三（苏三说技术）介绍轻量级 Java 规则引擎 [[EasyRules]]，主张把不断膨胀的 if...else 业务规则从代码中"搬"出来、变成可组合可管理的规则对象。文章先列举 if...else 硬编码的"七宗罪"（可读性/可维护性/可测试性/扩展性差、业务与代码耦合、逻辑重复、改后需重启），再讲解 Easy Rules 的四大核心抽象（Rule / Facts / Rules / RulesEngine）、四种规则定义方式（注解 / 流式 API / 表达式语言 / YAML-JSON）、两种引擎（DefaultRulesEngine 顺序执行、InferenceRulesEngine 前向链推理）与三种复合规则（UnitRuleGroup 与逻辑 / ActivationRuleGroup 排他 / ConditionalRuleGroup 条件）。Easy Rules 极轻量（JAR 仅约 100KB）、学习成本低，但自 2020-12 进入维护模式，不适合超大规模规则集，复杂场景可平滑迁移到 Drools。设计灵感源自 [[MartinFowler]] 提出的规则引擎理念。

## 关联连接
- [[EasyRules]] — 本文主角，j-easy 团队开源的轻量级 Java 规则引擎
- [[MartinFowler]] — 规则引擎概念的提出者，Easy Rules 设计灵感来源
- [[规则引擎]] — 本文所属核心概念，补充了 Easy Rules 的完整实现细节
- [[苏三]] — 本文作者
- [[URule]] — 另一种 Java 规则引擎（可视化路线），可对比
- [[策略模式]] / [[责任链模式]] — 规则引擎本质上是二者的组合应用
