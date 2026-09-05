---
title: "Reader"
type: entity
tags: [Java, IO, 字符流]
sources: [raw/01-articles/2026-06-29-14、Reader的源码、FilterReader源码、PushbackReader源码（windows操作系统，JDK8） - Carey_ccl.md]
last_updated: 2026-06-30
---

## 定义
Reader 是 Java I/O 中用于读取字符流的抽象基类，面向 `char` 字符数据而非字节数据，适合处理文本、中文等字符内容。

## 关键信息
- Reader 实现 `Readable` 与 `Closeable`，核心抽象方法是 `read(char[] cbuf, int off, int len)` 与 `close()`。
- `read()` 默认通过长度为 1 的 `char[]` 调用子类的批量读取方法，读到流末尾时返回 `-1`。
- `skip(long n)` 通过内部 `skipBuffer` 循环读取并丢弃字符，每次最多跳过 8192 个字符。
- `lock` 字段用于在读取、跳过等操作中做同步；构造函数既可默认使用 `this`，也可传入外部锁对象。
- `mark()`、`reset()`、`ready()`、`markSupported()` 默认能力较弱，具体是否支持由子类重写决定。

## 关联连接
- [[摘要-reader-filterreader-pushbackreader源码]] — 来源
- [[Java]] — 标准库所属语言
- [[FilterReader]] — Reader 的装饰器基类子类
- [[PushbackReader]] — 支持字符回退的 Reader 子类
- [[装饰器模式]] — Java I/O 字符流常用结构模式
