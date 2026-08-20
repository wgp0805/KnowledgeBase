---
title: "AMH"
type: entity
tags: [运维, 面板, Linux, 服务器管理]
sources: [raw/01-articles/2026-08-19-AMH的ams3软件报错s3cmd需要升级？.md]
last_updated: 2026-08-20
---

## 定义
AMH 是国内知名的 Linux 服务器运维管理面板，提供网站、数据库、文件、备份等可视化管理能力。ams3 是 AMH 面板中的 S3 通用备份软件模块，用于将备份上传到 S3 兼容对象存储。

## 关键信息
- **ams3 模块**：AMH 面板的 S3 通用备份软件，底层依赖 s3cmd 与 S3 兼容存储交互
- **已知兼容性问题**：ams3 1.1 + s3cmd 2.2.0 + Python 3.13 环境下报错（详见 [[s3cmd]]）
- **ams3 已知 bug**：存储空间名含 `-` 字符时，保存后再编辑会吞掉 `-` 前的字符（如 `backup-self-private/...` 变成 `self-private/...`），疑似前端解析或后端存储未正确处理 `-` 分隔符

## 关联连接
- [[s3cmd]] — ams3 底层依赖的 S3 命令行工具
- [[MinIO]] — S3 兼容对象存储（同生态参考）
- [[摘要-AMH-ams3-s3cmd报错]] — 来源
