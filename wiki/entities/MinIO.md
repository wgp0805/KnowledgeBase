---
title: "MinIO"
type: entity
tags: [对象存储, S3兼容, 分布式存储, Go语言]
sources: [raw/01-articles/什么是 MinIO.md, raw/01-articles/MinIO 社区版被故意阉割，Web管理功能全面移除，来试试国产的RustFS？.md]
last_updated: 2026-07-22
---

## 定义
MinIO 是一款基于 Go 语言开发的高性能、分布式开源对象存储系统，完全兼容 Amazon S3 API。支持非结构化数据存储、私有云构建、AI/大数据基础设施和混合云架构。

## 关键信息
- **兼容 S3 API**：现有 S3 生态工具链可无缝迁移
- **主要用途**：海量非结构化数据存储、私有云存储、AI/大数据数据湖、混合云数据桥梁
- **Docker 部署**：通过 Docker 快速部署，映射 9000（API）端口
- **管理方式**：通过命令行客户端 mc 管理
- **配置方式**：通过环境变量驱动，无需传统配置文件
- **许可协议**：AGPL v3（限制较多的开源协议）
- **商业化**：自 2024 年 2 月起通过"精简控制台"PR 删除 11 万行代码，全面移除 Web 管理界面，加速闭源商业化转型；建议社区用户付费迁移至商业产品 AiStor

## 关联连接
- [[摘要-minio-intro]] — 来源
- [[摘要-minio-rustfs]] — 来源
- [[Docker]] — 容器化部署方式
- [[RustFS]] — 国产替代方案
- [[AiStor]] — MinIO 商业化产品
- [[distributed-object-storage]] — 分布式对象存储架构
- [[open-source-commercialization]] — 开源商业化模式
