---
title: "DAP"
type: concept
tags: [IDE, 调试器, 协议, AI编程]
sources: [raw/01-articles/GitHub 38.1k Star 杀疯了！这个能联动 IDE 的终端 AI 编程神器你用了吗？.md]
last_updated: 2026-11-26
---

## 定义
DAP（Debug Adapter Protocol，调试适配器协议）是编辑器/IDE 与调试器之间的标准通信协议，通过一个"调试适配器"把不同语言的真实调试器统一抽象成一套协议接口，使客户端能用同一套方式驱动断点、单步、查看变量等调试操作。

## 关键信息
- **核心价值**：让工具能**直接驱动真实调试器**，而不是靠到处加 print 排查。以 [[OhMyPi]]（提供 28 个 DAP 调试操作）为例——C 程序段错误可以挂 lldb 单步走到出错的指针；Go 服务卡住可以挂 dlv 查看 goroutine；Python 进程可以挂 debugpy 暂停后检查变量
- **对 AI 编程代理的意义**：能驱动真实调试器意味着 AI 代理可以做真正的运行时诊断（断点、单步、检查 goroutine/变量），而非仅靠静态读代码推测，显著提升排查疑难 bug 的能力
- **各语言调试器**：lldb（C/C++）、dlv（Go）、debugpy（Python）等，都可通过 DAP 适配器被统一驱动

## 关联连接
- [[OhMyPi]] — 把 DAP 接进终端的编码代理
- [[LSP]] — 配套的语言服务器协议
- [[AI编程]] — DAP 提升运行时诊断能力的应用领域
- [[摘要-oh-my-pi-ide级终端agent]] — 来源
