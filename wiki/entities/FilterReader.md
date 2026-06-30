---
title: "FilterReader"
type: entity
tags: [Java, IO, 装饰器模式]
sources: [raw/01-articles/2026-06-29-14、Reader的源码、FilterReader源码、PushbackReader源码（windows操作系统，JDK8） - Carey_ccl.md]
last_updated: 2026-06-30
---

## 定义
FilterReader 是 Java 字符输入流体系中的抽象装饰器基类，用于包装另一个 `Reader` 并将默认读取行为委托给被包装对象。

## 关键信息
- 内部持有 `protected Reader in`，表示实际被装饰的字符输入流。
- 构造时调用 `super(in)`，使同步锁复用被装饰 Reader，降低并发访问中的锁不一致风险。
- 默认实现会把 `read()`、`read(char[], int, int)`、`skip()`、`ready()`、`mark()`、`reset()`、`close()` 等方法转发给内部 Reader。
- 子类可以只重写需要增强的方法，从而在不改变原 Reader 接口的前提下增加过滤、转换、回退等能力。

## 关联连接
- [[摘要-reader-filterreader-pushbackreader源码]] — 来源
- [[Reader]] — 父类与被装饰对象类型
- [[PushbackReader]] — FilterReader 的具体子类
- [[装饰器模式]] — FilterReader 的核心设计模式
- [[Java]] — 标准库所属语言
