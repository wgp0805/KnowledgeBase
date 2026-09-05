---
title: "Resource"
type: entity
tags: [Spring, 资源加载, 策略模式]
sources: [raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义
Resource 是 Spring 框架中用于抽象资源访问的接口，通过策略模式支持从不同来源（类路径、文件系统、网络等）加载资源。

## 关键信息
- 策略模式：同一接口，不同实现策略
- 常见实现：ClassPathResource（类路径）、FileSystemResource（文件系统）、UrlResource（网络）
- 统一接口：调用方只面向 Resource 接口编程，不关心底层资源来源
- ResourceLoader：定义资源加载策略的接口，ApplicationContext 实现了此接口
- 方法：getInputStream()、exists()、getDescription() 等

## 关联连接
- [[Spring]] — 所属框架
- [[策略模式]] — Resource 体现的设计模式
- [[ApplicationContext]] — ResourceLoader 的实现
- [[摘要-spring-design-patterns]] — 来源文章