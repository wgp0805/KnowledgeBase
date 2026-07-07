---
title: "Java"
type: entity
tags: [编程语言, JVM]
sources: [raw/01-articles/CompletableFuture的使用.md, raw/01-articles/java8新特性详解.md, raw/01-articles/Java接口中的Default方法及其意义.md, raw/01-articles/java时间的比较.md, raw/01-articles/lambda表达式简单解析.md, raw/01-articles/jvm参数解释.md, raw/01-articles/Steam的简单操作.md, raw/01-articles/MessageDigest简介及应用.md, raw/01-articles/图文详解Java泛型，写得太好了！.md, raw/01-articles/2026-06-29-14、Reader的源码、FilterReader源码、PushbackReader源码（windows操作系统，JDK8） - Carey_ccl.md]
last_updated: 2026-06-30
---

## 定义
Java 是一种广泛使用的面向对象编程语言，基于 JVM（Java 虚拟机）实现跨平台运行，是企业级应用开发的主流语言。

## 关键信息
- Java 8 重要特性：Lambda 表达式、Stream API、Optional、CompletableFuture、接口 Default 方法、新日期时间 API
- 函数式编程支持：函数式接口（@FunctionalInterface）、方法引用（::）
- Stream API 提供声明式数据处理：map/filter/reduce/collect
- CompletableFuture 实现异步任务编排
- MessageDigest 支持 MD5/SHA 等消息摘要算法
- Lambda 表达式精简匿名内部类编写

### 泛型特性
- 泛型是 Java 5 引入的类型参数机制，提升代码类型安全和复用
- 支持泛型类、泛型接口、泛型方法
- 编译时类型检查，避免 ClassCastException
- 类型擦除机制：运行时泛型信息被擦除

## 关联连接
- [[JVM]] — Java 虚拟机
- [[Spring]] — 应用框架
- [[SpringBoot]] — 自动配置框架
- [[IntelliJIDEA]] — Java IDE
- [[generics]] — 泛型概念
- [[摘要-java-generics-explained]] — 泛型详解
- [[摘要-reader-filterreader-pushbackreader源码]] — Reader/FilterReader/PushbackReader 源码解读
- [[Reader]] — 字符输入流抽象基类
- [[FilterReader]] — 字符流装饰器基类
- [[PushbackReader]] — 支持字符回退的字符流装饰器
- [[摘要-HttpClient的简单使用]] — 基于 JDK 原生 HttpURLConnection 封装…
- [[摘要-httpUtils]] — 基于 JDK 原生 HttpURLConnection 和 …
- [[摘要-MessageDigest简介及应用]] — 介绍 Java MessageDigest 类实现 MD5、…
- [[摘要-mybatis-plus-12-optimization-tips]] — 本文介绍了 12 个 MyBatis Plus 性能优化技巧…
- [[摘要-Java接口中的Default方法及其意义]] — 讲解 Java 8 接口 Default 方法的意义：向后兼…
