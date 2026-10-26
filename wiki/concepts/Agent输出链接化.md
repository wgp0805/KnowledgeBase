---
title: "Agent输出链接化"
type: concept
tags: [Agent, 终端, 链接, IDE集成]
sources: ["raw/09-archive/2026-10-23-Agent YOLO 三端全开：一个 YOLO 面板，在 IntelliJ、Visual Studio、VS Code 里都能跑起来 - Cn#工作室.md"]
last_updated: 2026-10-26
---

## 定义
把 Agent CLI 在终端里打印的纯文本输出实时扫描成可点击超链接（文件路径、堆栈帧、类型名、成员引用、URL），并且只在能解析时才成链、防止误链的技术。

## 关键信息
- **可识别形态**：Windows 路径、无扩展名文件、`file://` URI、Python / JS 回溯帧（堆栈帧）、类型名、成员引用、URL。
- **交互示例**：点 `ClassLibrary1\OrderService.cs:128` 直接跳到那一行；点 `ClassLibrary1.OrderService.Save` 直接定位成员——Agent 说"异常在 `OrderService.cs` 第 128 行"时，不必再手动翻文件找行号。
- **链接过滤器（防误链）**：只有当链接能解析成项目里真实存在的文件 / 类时才渲染为链接，随机单词不会误链；Agent YOLO 的 IntelliJ main 分支含这套过滤器，`exp` 实验分支不含。
- **三端实现差异**：VS Code 端路径链接走文件系统解析、开箱即用，但类型 / 成员链接须经 LSP `workspace/symbol`，需装对应语言的 language server（Java 用 Red Hat、TS 内置、Python 用 Pylance……），否则 "no symbol found"；IntelliJ / VS 端内置解析。
- **工程一致性**：链接正则在各端的处理要大体一致（个别语言差异除外），统一在 `Meta/` 下维护一份 RegExp（见 [[多端共享元数据]]）。

## 关联连接
- [[摘要-agent-yolo-三端ide面板]] — 来源文章
- [[AgentYOLO]] — 落地该机制的三端产品
- [[多端共享元数据]] — 链接正则的统一维护处
