---
title: "IoC"
type: concept
tags: [Spring, 设计原则, 依赖注入]
sources: []
last_updated: 2026-05-29
---

## 定义
IoC（Inversion of Control，控制反转）是一种设计原则，将对象的创建和依赖管理从应用代码转移到外部容器，Spring 通过 DI（依赖注入）实现 IoC。

## 关键信息
- 核心思想：对象不自己创建依赖，由容器注入
- 实现方式：构造器注入、Setter 注入、字段注入（@Autowired）
- IoC 容器：BeanFactory（基础）、ApplicationContext（高级）
- 优势：解耦、可测试、可配置
- 与 DI 关系：IoC 是原则，DI 是实现 IoC 的具体手段

## 关联连接
- [[Spring]] — IoC 容器实现
- [[BeanFactory]] — 基础 IoC 容器
- [[ApplicationContext]] — 高级 IoC 容器
- [[工厂模式]] — IoC 的设计模式基础
- [[SpringBoot]] — 自动配置的 IoC 容器
