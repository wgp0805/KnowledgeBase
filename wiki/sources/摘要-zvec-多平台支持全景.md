---
title: "摘要-zvec-多平台支持全景"
type: source
tags: [来源, 原始文件, 向量数据库, Zvec, 多平台]
sources: [raw/01-articles/2026-09-18-让向量检索随处可用：Zvec 多平台支持全景 - DashVector.md]
last_updated: 2026-09-20
---

## 核心摘要
Zvec 是阿里巴巴开源的进程内向量数据库（"向量数据库里的 SQLite"），宿主应用跑在哪里它就要在哪里可用。已支持 Linux/macOS/Windows/Android/iOS，覆盖服务端、桌面端与移动端，提供 Python/Node.js/Go/Rust/Java/Dart-Flutter 六种官方 SDK 与预编译产物。多平台支持的四条标准：CI 持续验证、开箱即用预编译产物、功能一致性明确告知、最大化硬件性能。索引平台适用性：Flat/IVF/HNSW/Vamana/稀疏向量/INVERT/FTS 全平台，RaBitQ 仅 Linux x86_64，DiskANN 除 RISC-V。工程底座靠 C++17 + CMake + 平台抽象层 + SIMD 运行时分派（AVX-512→AVX2→AVX→SSE→scalar）+ I/O 后端抽象（io_uring→libaio→pread）。选型思路：内存放得下用内存索引，放不下用 DiskANN/Vamana 磁盘模式。

## 关联连接
- [[Zvec]] — 进程内向量数据库
- [[ZvecGrep]] — 本地优先搜索层
- [[HNSW]] — 分层可导航小世界图
- [[DiskANN]] — 磁盘级检索
- [[RaBitQ]] — 量化压缩索引
- ISA分派 — 运行时分派
- [[进程内向量数据库]] — 概念
- DashVector — 作者