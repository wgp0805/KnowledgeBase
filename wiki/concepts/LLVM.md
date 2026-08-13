---
title: "LLVM"
type: concept
tags: [编译器, 基础设施, 开源, 性能优化]
sources: [raw/09-archive/蚂蚁又开源了一个顶级Java项目！.md]
last_updated: 2026-07-23
---

## 定义
LLVM（Low Level Virtual Machine）是目前最受欢迎的开源编译器基础设施，拥有模块化的设计、优秀的编译优化能力与完备的后端支持。它提供了一套现成的"超级零件箱"，可以快速拼出新的编译器。

## 关键信息
- **编译流程**：
  1. 编写语言前端：将编程语言代码转换成 LLVM IR（Intermediate Representation）
  2. 利用 LLVM 的优化器对 LLVM IR 进行分析与优化
  3. 通过 LLVM 的代码生成器从 LLVM IR 生成真正的 CPU 指令
- **核心优势**：
  - 极致的性能优化：业界顶尖的代码分析和优化能力
  - 高度模块化：按需取用，灵活扩展，是现代编程语言（Rust、Swift）的首选
  - 繁荣的开源生态：全球顶尖公司、研究机构和开发者共同维护
- **应用领域**：Rust 编译器、Swift 编译器、[[Jeandle]]（JVM JIT 编译器）、AI 领域

## 关联连接
- [[Jeandle]] — 基于 LLVM 的 JVM JIT 编译器
- [[JIT编译]] — 即时编译
- [[摘要-jeandle-llvm-jit编译器]] — 来源