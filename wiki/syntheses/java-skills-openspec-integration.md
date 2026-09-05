---
title: "Java 开发 Skills 与 OpenSpec 配合使用指南"
type: synthesis
tags: [Java, OpenSpec, Skills, AI编程, 规范驱动]
sources: []
last_updated: 2026-08-12
---

# Java 开发 Skills 与 OpenSpec 配合使用指南

## 核心观点

OpenSpec 是规范驱动的 AI 编程框架，负责"做什么"和"按什么规矩做"；Java 开发 Skills 负责具体编码实现质量。两者是互补关系，在 OpenSpec 工作流中协同工作。

## Java 开发相关的 Skills 列表

| Skill 名称 | 核心用途 |
|------------|----------|
| `java-dev` | Java 开发规范，包含命名约定、异常处理、Spring Boot 最佳实践等 |
| `java-spring-framework` | Java & Spring Boot 4 / Spring Framework 7 架构师技能，适用于最新规范 |
| `dr-jskill` | 创建 Java + Spring Boot 项目，JHipster 作者出品 |
| `spring-boot-skill` | 构建 Spring Boot 4.x 应用，遵循最佳实践 |
| `jspecify-skill` | 添加 jspecify 支持，用于空安全检查 |
| `spring-jpa-testing` | Spring JPA 测试规范 |
| `spring-mvc-testing` | Spring MVC 测试规范 |
| `spring-security-testing` | Spring Security 测试规范 |
| `spring-testing-fundamentals` | Spring 测试基础，Boot 4 迁移指南 |
| `spring-webflux-testing` | Spring WebFlux 测试规范 |
| `spring-websocket-testing` | Spring WebSocket 测试规范 |

## OpenSpec 核心工作流

1.  **探索模式** (`/opsx:explore`)：通过对话探讨需求
2.  **提案模式** (`/opsx:propose`)：生成规划文档（proposal、specs、design、tasks）
3.  **应用模式** (`/opsx:apply`)：按清单逐项实现，生成代码
4.  **归档模式** (`/opsx:archive`)：完成归档

## 配合使用方式

### 规划阶段 (OpenSpec)

OpenSpec 负责定义功能需求和技术方案，生成的文档包括：
- `proposal.md`：变更提案，为什么做什么
- `specs/spec.md`：需求规格，用 SHALL/MUST 确定性词汇描述
- `design.md`：技术设计，描述实现方案
- `tasks.md`：任务清单，列出实现步骤

### 实现阶段 (Skills)

当执行 `/opsx:apply` 生成代码时，AI 会参考项目中已安装的 Skills。此时 `java-dev` 等 Skills 会作为编码规范约束，确保生成的代码符合 Java 最佳实践。

### 集成建议

在 OpenSpec 的提案阶段，可以在 `design.md` 中引用 `java-dev` 的规范作为技术约束，例如：

```markdown
## 技术约束

- 遵循 `java-dev` Skill 中的命名约定
- 使用 Lombok 处理 DTO/VO 类
- 遵循 N+1 查询防范规范
- 遵循并发安全规范
```

这样 AI 在实现时会严格遵守这些规范。

## 实际应用场景

### 场景一：新功能开发

1. 使用 `/opsx:explore` 探讨需求
2. 使用 `/opsx:propose` 生成规划文档
3. 在 `design.md` 中引用 Java 开发规范
4. 使用 `/opsx:apply` 生成符合规范的代码

### 场景二：现有代码重构

1. 使用 Delta Spec 描述增量变更
2. 在技术设计中明确要遵循的 Java 规范
3. 通过 `/opsx:apply` 实现重构，确保代码质量

## 总结

OpenSpec 与 Java 开发 Skills 的配合，实现了 **"规划先行，规范约束"** 的 AI 编程模式。OpenSpec 确保需求对齐，Java Skills 确保代码质量，两者结合可以显著提升 AI 生成代码的可靠性和可维护性。

## 关联连接

- [[OpenSpec]] — 规范驱动 AI 编程框架
- java-dev — Java 开发规范 Skill（skill 名，非 wiki 页）
- java-spring-framework — Spring 框架架构师技能（skill 名）
- spring-boot-skill — Spring Boot 应用构建技能（skill 名）
- [[规范驱动开发]] — 上层方法论
- [[Superpowers]] — 兄弟方案，管"怎么干"
- [[SpecKit]] — 兄弟方案，让规范可执行
