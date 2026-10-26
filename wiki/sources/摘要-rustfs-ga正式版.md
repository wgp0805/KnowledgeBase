---
title: "摘要-rustfs-ga正式版"
type: source
tags: [来源, 原始文件]
sources: [raw/09-archive/给 MinIO 说再见，最强 AI 存储 RustFS 发布正式版了！.md]
last_updated: 2026-09-18
---

## 核心摘要
RustFS 是用 Rust 语言从零构建的高性能分布式对象存储系统，于 2026 年 9 月正式发布 GA（1.0.0）版本，Apache 2.0 许可证，S3 API 完全兼容。RustFS 采用 Tokio 异步处理和 io_uring，无 GC 暂停，4KB 小对象吞吐量是 MinIO 的 2.3 倍。NVIDIA OSMO 已集成 RustFS 作为集群内存储后端替代方案，并正在开发基于 BlueField DPU 的 GPUCache 项目。文章还提供了 Docker 部署、Spring Boot 对接、MinIO 迁移三条路径的完整实战指南。

## 关联连接
- [[RustFS]] — 主体实体
- [[MinIO]] — 对标对象存储
- [[NVIDIA]] — 采用 RustFS 的公司
- [[RAG]] — RustFS S3 Tables 对 RAG 场景的意义
