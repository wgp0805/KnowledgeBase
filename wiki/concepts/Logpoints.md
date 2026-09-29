---
title: "Logpoints"
type: concept
tags: [概念, 调试, IDEA]
sources: [raw/01-articles/IDEA 2026.2 必装插件 Top 100.md]
last_updated: 2026-09-29
---

## 定义
日志断点（Logpoints）：在代码行上设置不暂停程序、只向控制台输出自定义消息或表达式值的断点。[[IntelliJIDEA]] 2026.2 将其作为内置能力推出，是"非侵入式调试"的代表——**无需改代码、无需暂停程序**，替代了手动加 `println` 再删掉的传统调试方式。

## 关键信息
- **工作方式**：右键行号 → Toggle Logpoint → 输入要打印的内容（可含变量表达式），命中时输出到控制台，程序继续运行
- **对比传统方式**：
  - 手动 println/debug 日志：侵入代码、需重新编译、调试完要清理
  - 普通断点：暂停程序，改变执行时序，不适合并发/时序敏感场景
  - Logpoints：零侵入、不暂停、可随时开关
- **2026.2 语境**：与终端拖拽路径、Resolve All Simple Conflicts 一键解冲突等同属"内置功能替代旧插件"趋势——过去需装插件（如 Scientist 等调试辅助类）的能力被 IDE 原生吸收

## 关联连接
- [[摘要-idea-2026-2-必装插件-top100]] — 来源
- [[IntelliJIDEA]] — 载体 IDE
- [[Java]] — 主要适用语言
- [[日志分析]] — 输出去向的下游概念
