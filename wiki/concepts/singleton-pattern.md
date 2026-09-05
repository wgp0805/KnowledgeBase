---
title: "singleton-pattern"
type: concept
tags: [设计模式, 单例模式, Java, 线程安全, Spring]
sources: [raw/01-articles/美团面试：单例模式的 5 种写法，你会几种？ 我只答上来 3 种.md, raw/01-articles/Spring 用到了哪些设计模式？你能答上来几个？.md]
last_updated: 2026-05-25
---

## 定义

单例模式是一种创建型设计模式，确保一个类只有一个实例，并提供一个全局访问点。在 JVM 进程内保证唯一性，分布式环境下需要分布式锁或集中式存储保证。

## 关键信息

### 五种经典写法

| 写法 | 线程安全 | 延迟加载 | 推荐指数 |
|------|----------|----------|----------|
| 饿汉式 | ✅ | ❌ | ⭐⭐⭐ |
| 懒汉式（同步方法） | ✅ | ✅ | ⭐ |
| 双重检查锁（DCL） | ✅ | ✅ | ⭐⭐⭐⭐ |
| 静态内部类 | ✅ | ✅ | ⭐⭐⭐⭐⭐ |
| 枚举单例 | ✅ | ❌ | ⭐⭐⭐⭐⭐ |

### DCL 的 volatile 问题
`new Singleton()` 在 JVM 层面分三步：①分配内存 → ②初始化对象 → ③指向引用。不加 volatile 可能发生指令重排序（①→③→②），导致其他线程获取到未初始化的对象。volatile 利用内存屏障禁止指令重排序。

### 单例的破坏与防御
1. **反射破坏**：构造器中加判断，或直接用枚举
2. **序列化/反序列化破坏**：实现 readResolve() 方法，或直接用枚举

### 枚举单例优势
- 线程安全（JVM 保证）
- 防反射（JVM 直接抛异常）
- 防序列化（JVM 保证不会创建新对象）

### Spring 单例 vs 设计模式单例
Spring Bean 默认 scope=singleton，由 Spring 容器管理，与传统单例模式不同。Spring 单例是每个容器内唯一，且处理了线程安全问题。

### Spring 单例实现
- 容器级别单例：由 Spring 容器保证同一个 id 的 Bean 只创建一次
- 三级缓存机制：DefaultSingletonBeanRegistry 通过三级缓存解决循环依赖
- 线程安全：Spring 单例是非线程安全的，Bean 应设计为无状态（不包含可变成员变量）
- 非传统实现：不是 private 构造器 + static 实例，而是容器管理

## 关联连接
- [[摘要-singleton-pattern]] — 来源
- [[摘要-spring-design-patterns]] — Spring 设计模式来源
- [[Java]] — 面向对象编程语言
- [[JVM]] — Java 虚拟机（类加载机制、指令重排序）
- [[Spring]] — Spring 容器单例管理
- [[DefaultSingletonBeanRegistry]] — Spring 单例实现核心类
- [[BeanFactory]] — 单例 Bean 的管理容器
