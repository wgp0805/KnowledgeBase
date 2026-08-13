---
title: "EasyRules"
type: entity
tags: [规则引擎, Java, 开源工具, j-easy]
sources: [raw/09-archive/干掉if...else，推荐一个小而美的规则引擎.md]
last_updated: 2026-07-02
---

## 定义
Easy Rules 是一个简单而强大的**轻量级 Java 规则引擎**，由 **j-easy** 团队开源维护。设计灵感来源于 [[MartinFowler]] 提出的规则引擎理念——"创建一组带有条件（condition）和操作（action）的对象，存入集合并运行它们来评估条件、执行动作"。一句话概括：**把 if...else 从代码里搬出来、用规则对象来管理**。

## 关键信息

### 四大核心抽象
- **Rule（规则）**：最核心的接口，包含 name（唯一名）、description、priority（数字越小优先级越高）、condition（返回 true 触发）、action（条件满足时执行）。核心方法 `evaluate(Facts)` 与 `execute(Facts)`。
- **Facts（事实）**：规则执行时的数据上下文，本质是键值对容器（`facts.put("user", user)`）。
- **Rules（规则集合）**：规则的有序容器，按 priority 自动排序。
- **RulesEngine（规则引擎）**：执行规则的核心引擎。

### 两种引擎实现
| 引擎类型 | 执行策略 | 适用场景 |
| --- | --- | --- |
| **DefaultRulesEngine** | 按优先级顺序执行，条件满足就执行 | 大多数常规场景 |
| **InferenceRulesEngine** | 前向链推理（forward chaining），反复执行直到没有规则可触发 | 规则之间存在依赖和连锁反应 |

前向链推理循环：在当前 Facts 下找出所有条件为 true 的候选规则 → 若无则退出 → 否则执行（可能修改 Facts）→ 回到第一步继续循环。

### 四种规则定义方式
1. **注解方式**（最常用）：`@Rule` / `@Condition` / `@Action` / `@Fact` 标注 POJO。规则固定、逻辑清晰时首选。
2. **流式 API**：`RuleBuilder` 的 `.when(Predicate<Facts>)` / `.then(Consumer<Facts>)`，适合运行时动态生成规则。
3. **表达式语言**（最灵活）：支持 MVEL / SpEL / JEXL，规则可以字符串形式存储在数据库/配置中，**修改无需重新编译部署**。
4. **YAML/JSON 配置**：通过 `MVELRuleFactory` / `SpELRuleFactory` 加载配置文件，规则完全抽离由业务人员维护。

### 三种复合规则
- **UnitRuleGroup**（与逻辑）：所有规则都满足才执行。
- **ActivationRuleGroup**（排他）：多个满足时只执行优先级最高的一个（适合互斥折扣）。
- **ConditionalRuleGroup**（条件）：第一个规则满足才继续执行后续规则链。

### 其他机制
- **RulesEngineParameters**：`skipOnFirstAppliedRule` / `skipOnFirstFailedRule` / `priorityThreshold` 等精细控制。
- **RuleListener 监听器**：`beforeEvaluate` / `afterEvaluate` / `onSuccess` / `onFailure` 生命周期钩子，用于日志、监控、调试。

### Maven 依赖
`org.jeasy:easy-rules-core`（核心）、`easy-rules-support`（YAML/JSON）、`easy-rules-mvel`（MVEL），最新稳定版 **4.1.0**。

## 优缺点
**优点**：极轻量（JAR 约 100KB，毫秒级启动，适合 K8s [[Pod]] 快速启动）、学习成本低（POJO + 注解）、多种定义方式、复合规则、监听器机制、零配置、与 [[SpringBoot]] 无缝集成。

**缺点**：注解/POJO 规则修改仍需重启（除非用表达式语言）、不支持复杂规则链和决策表、**自 2020-12 起进入维护模式**、不适用超大规模规则集（数千条时性能不如 Rete 算法的 Drools）、无可视化管理界面。

**选型建议**：不确定规则复杂度时从 Easy Rules 起步，规则变复杂后再平滑迁移到 Drools。

## 关联连接
- [[规则引擎]] — Easy Rules 所属的核心概念
- [[摘要-easy-rules-规则引擎]] — 来源摘要
- [[MartinFowler]] — 规则引擎理念提出者，设计灵感来源
- [[URule]] — 另一 Java 规则引擎（可视化路线），可对比选型
- [[SpringBoot]] — 可通过 `@Bean` 无缝集成
- [[策略模式]] — 规则即对象，本质是策略模式的应用
- [[苏三]] — 介绍文章作者
