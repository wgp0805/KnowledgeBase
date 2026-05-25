---
title: "摘要-singleton-pattern"
type: source
tags: [设计模式, 单例模式, 面试, Java]
sources: [raw/01-articles/美团面试：单例模式的 5 种写法，你会几种？ 我只答上来 3 种.md]
last_updated: 2026-05-25
---

## 核心摘要

本文讲解单例模式的5种经典写法及其线程安全、防破坏机制。五种写法：饿汉式（类加载时创建，简单但不延迟加载）、懒汉式同步方法（性能差，每次调用都加锁）、双重检查锁DCL（volatile防止指令重排序）、静态内部类（推荐，利用JVM类加载机制保证线程安全）、枚举单例（Effective Java推荐，天然防反射和序列化破坏）。单例可被反射和序列化/反序列化破坏，枚举单例天然免疫。Spring Bean默认scope=singleton，但由容器管理，与传统单例模式不同。

## 关联连接
- [[Java]] — 面向对象编程语言
- [[JVM]] — Java 虚拟机（类加载机制）
- [[Spring]] — Spring 容器单例管理
