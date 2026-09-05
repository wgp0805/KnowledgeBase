---
title: "PushbackReader"
type: entity
tags: [Java, IO, 字符流, 装饰器模式]
sources: [raw/01-articles/2026-06-29-14、Reader的源码、FilterReader源码、PushbackReader源码（windows操作系统，JDK8） - Carey_ccl.md]
last_updated: 2026-06-30
---

## 定义
PushbackReader 是 Java I/O 中支持“字符回退”的字符输入流装饰器，允许把已读取或预读的字符重新压回缓冲区，供后续读取再次消费。

## 关键信息
- 继承自 [[FilterReader]]，内部维护 `char[] buf` 作为有限长度的回退缓冲区。
- `pos` 是可读指针，`pos < buf.length` 表示回退缓冲区中还有字符可读。
- `read()` 优先读取回退缓冲区中的字符；缓冲区为空时再读取被装饰的 Reader。
- `unread(int c)` 和 `unread(char[] cbuf, int off, int len)` 会把字符写回缓冲区；空间不足时抛出 `IOException: Pushback buffer overflow`。
- 不支持 `mark()` 与 `reset()`，`markSupported()` 固定返回 false。
- 适合词法分析、协议解析、文本解析等需要“看一眼下一个字符，不合适再退回”的场景。

## 关联连接
- [[摘要-reader-filterreader-pushbackreader源码]] — 来源
- [[Reader]] — 字符输入流抽象基类
- [[FilterReader]] — 直接父类
- [[装饰器模式]] — 通过包装 Reader 增加回退能力
- [[Java]] — 标准库所属语言
