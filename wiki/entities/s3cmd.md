---
title: "s3cmd"
type: entity
tags: [S3, 命令行工具, Python, 对象存储]
sources: [raw/01-articles/2026-08-19-AMH的ams3软件报错s3cmd需要升级？.md]
last_updated: 2026-08-20
---

## 定义
s3cmd 是基于 Python 的 S3 兼容对象存储命令行工具，用于上传、下载、同步、管理 S3 存储桶中的对象。常作为面板/脚本底层依赖与 S3 兼容存储（如 MinIO、AWS S3、Ceph）交互。

## 关键信息
- **版本兼容性问题**：s3cmd 2.2.0 在 Python 3.13 环境下报错
  - `SyntaxWarning: invalid escape sequence`（源码正则未用 r-string，Python 3.12+ 升级为 SyntaxWarning）
  - `DeprecationWarning: pkg_resources is deprecated`（setuptools 弃用 pkg_resources API）
  - `'SortedDictIterator' object is not iterable`（核心阻塞错误，导致请求重试失败）
- **解决方向**：升级 s3cmd 到兼容 Python 3.13 的版本
- **使用场景**：AMH 面板 ams3 模块底层依赖、脚本化 S3 备份、对象存储运维

## 关联连接
- [[AMH]] — ams3 模块依赖 s3cmd
- [[MinIO]] — S3 兼容对象存储（s3cmd 常用对接目标）
- [[摘要-AMH-ams3-s3cmd报错]] — 来源
