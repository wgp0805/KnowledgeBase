---
title: "Embabel"
type: entity
tags: [实体, AI框架, Agent, Java, 开源]
sources:
  - raw/09-archive/2026-08-01-Spring之父再次出山，开发了新的AI框架！ - 苏三说技术.md
last_updated: 2026-08-03
---

## 定义
Embabel 是 Rod Johnson（Spring 之父）面向企业 AI Agent 打造的 JVM 开源框架，通过确定性规划（GOAP）让非确定性的 AI 在确定性的企业系统里稳定工作。定位为「企业级 Agent 编程模型」，是 Spring AI 之上的一层（类似 Spring MVC 之于 Servlet API）。

## 关键信息
- **发布节点**：2026 年 4 月 Microsoft JDConf 发布；2026-07-20 1.0.0 GA；Apache 2.0 协议
- **核心抽象**：
  - **Agent**：自包含组件，封装领域逻辑、AI 能力和工具使用，代表用户完成特定目标
  - **Action**：Agent 可执行的离散步骤，`@Action`/`@ActionMethod` 注解标记，输入输出为强类型领域对象
  - **Goal**：Agent 要达成的目标，`@Goal` 注解标记；GOAP 引擎根据当前状态动态规划最优行动序列，无需手写 if-else/流程控制
- **两种规划模式**：GOAP（默认，确定性，不用 LLM）；Utility AI（每个 Action 由效用函数打分，每步执行得分最高者，如 Stashbot RAG 文档助手）
- **技术选型**：核心 Kotlin（空安全、简洁语法、reified 泛型），但 Java 互操作性好，用 Java 构建应用看不到 Kotlin 导入；基于 Spring Boot 集成
- **成本优势**：GOAP 规划器不用 LLM → 省 40-60% LLM 调用；强类型 Domain Model 精确契约 → 省 20-40% Token；整体降本 50-70%
- **与 Spring AI 对比**：Spring AI 是命令式（开发者手动编排 ReAct 循环，每次决策都调 LLM），Embabel 是声明式（定义 Action/Goal，GOAP 运行时动态计算最优路径，规划 0 Token）
- **优点**：GOAP 确定性可审计；成本显著；编译时类型安全；与 Spring 生态无缝集成；避免 LLM 过度设计；可扩展性强
- **缺点**：项目年轻（生态早期）；核心 Kotlin（读源码需懂 Kotlin）；GOAP/Utility AI 概念新；文档尚完善中；与 Python AI 生态成熟度有差距
- **开源地址**：github.com/embabel/embabel-agent；示例 embabel-agent-examples；文档 docs.embabel.com

## 关联连接
- [[RodJohnson]] — 创始人
- [[GOAP]] — 核心算法
- [[UtilityAI]] — 备选规划模式
- [[SpringAI]] — 对比/互补框架
- [[Agent]] — 编程模型
- [[SpringBoot]] — 集成基础
- [[ReAct_Agent]] — 对比的 Agent 模式（Embabel 不用 LLM 规划）
- [[摘要-embabel]] — 来源
