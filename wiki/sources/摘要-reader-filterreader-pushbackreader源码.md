---
title: "摘要-reader-filterreader-pushbackreader源码"
type: source
tags: [来源, Java, IO, 源码]
sources: [raw/01-articles/2026-06-29-14、Reader的源码、FilterReader源码、PushbackReader源码（windows操作系统，JDK8） - Carey_ccl.md]
last_updated: 2026-06-30
---

## 核心摘要
这篇资料围绕 JDK8 中 `Reader`、`FilterReader`、`PushbackReader` 三个字符输入流类展开源码解读。`Reader` 是字符输入流抽象基类，通过 `lock` 对象协调多线程下的读取、跳过、标记和关闭操作；`FilterReader` 是字符流装饰器基类，将读取、跳过、标记、关闭等操作委托给内部 `Reader`。`PushbackReader` 在装饰器基础上增加有限长度的字符回退缓冲区，支持把已读字符重新压回输入流，用于解析器、词法分析等需要“预读后回退”的场景。

## 关联连接
- [[Reader]] — JDK 字符输入流抽象基类
- [[FilterReader]] — 字符流装饰器基类
- [[PushbackReader]] — 支持字符回退的装饰器实现
- [[Java]] — 所属语言与标准库生态
- [[装饰器模式]] — FilterReader/PushbackReader 的结构型设计模式基础
