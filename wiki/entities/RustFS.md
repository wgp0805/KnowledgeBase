---
title: "RustFS"
type: entity
tags: [对象存储, 分布式存储, Rust, 开源, AI存储]
sources: [raw/01-articles/MinIO 社区版被故意阉割，Web管理功能全面移除，来试试国产的RustFS？.md, raw/01-articles/给 MinIO 说再见，最强 AI 存储 RustFS 发布正式版了！.md]
last_updated: 2026-09-18
---

## 定义
RustFS 是一款基于 Rust 编写的高性能分布式对象存储系统，采用 Apache 2.0 开源协议，完全兼容 S3 API，自带 Web 控制台，可作为 MinIO 的国产平替方案。2026 年 9 月正式发布 GA（1.0.0）版本。

## 关键信息
- **语言**：Rust（Tokio 异步 + io_uring，无 GC）
- **开源协议**：Apache 2.0
- **兼容性**：完全兼容 S3 API
- **管理方式**：自带 Web 控制台（Vue.js 3，开源可用）
- **部署方式**：支持 Docker Compose 一键部署
- **HTTPS 配置**：可通过 Nginx 反向代理 + Let's Encrypt 配置 HTTPS
- **GitHub Stars**：32k+（截至 2026-09）
- **DockerHub 下载量**：1000 万+（截至 2026-09）

### 性能优势
- 无 GC 暂停，内存安全在编译期保证
- 4KB 小对象吞吐量是 MinIO 的 2.3 倍（官方压测）
- 底层使用 Tokio 异步处理并发请求，Linux 支持 io_uring 异步 I/O
- 数据保护采用纠删码（Erasure Coding），RS(4,2) 配置存储开销 50%
- 分布式模式无中心元数据服务器，read-after-write 一致性

### NVIDIA 合作
- 2026 年 4 月加入 NVIDIA Inception 全球加速计划
- NVIDIA OSMO 平台集成 RustFS 作为集群内存储后端替代方案
- 正在开发 GPUCache 项目：基于 Rust + NVIDIA DOCA + RDMA + BF-4 DPU 的 PB 级 GPU 缓存系统
- 为 NVIDIA BlueField DPU 做原生 RDMA 支持，纠删码计算卸载到 DPU 硬件加速

### S3 Tables 与数据湖
- 实现了 Iceberg REST Catalog，支持 PyIceberg 和 DuckDB 直接连接（Preview 状态）
- 原始文档和结构化元数据可放在同一存储层，RustFS 同时承担对象存储和数据湖角色

### 生产功能
- 纠删码、版本控制、对象锁（WORM）、服务端加密
- IAM / OIDC / SSO 认证
- Prometheus + Grafana 可观测性
- Kubernetes Helm Charts 和 Operator
- S3、MCP / FTPS / WebDAV / SFTP 多协议支持

### Spring Boot 对接
- 使用 AWS SDK for Java v2，需设置 `forcePathStyle(true)` 使用 path style
- S3Presigner 的 endpoint 用 `publicUrl`，保证预签名链接正确访问

### 从 MinIO 迁移
1. **二进制替换**：RustFS 可直接读取 MinIO 数据目录，停机 2-5 分钟
2. **mc mirror 跨服务器复制**：只复制当前版本，不迁移版本历史
3. **Godwit Sync**：处理版本历史、对象锁、断点续传，生产推荐

## 关联连接
- [[MinIO]] — 对标的对象存储系统
- [[NVIDIA]] — 采用 RustFS 的公司
- [[RAG]] — RustFS S3 Tables 对 RAG 场景的意义
- [[摘要-minio-rustfs]] — 来源
- [[摘要-rustfs-ga正式版]] — 来源
