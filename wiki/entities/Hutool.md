---
title: "Hutool"
type: entity
tags: [Java, 工具库, 效率]
sources: []
last_updated: 2026-05-29
---

## 定义
Hutool 是一个小而全的 Java 工具类库，通过静态方法封装，降低学习成本，提高开发效率，涵盖 HTTP、JSON、加密、日期、文件等常用工具。

## 关键信息
- 核心模块：hutool-core（核心工具）、hutool-http（HTTP 客户端）、hutool-json（JSON 处理）、hutool-crypto（加密解密）
- 设计理念：方法优先于对象，减少 new 操作
- StrUtil / DateUtil / FileUtil / HttpUtil 等常用工具类
- 与 Apache Commons 对比：Hutool 更现代、API 更简洁
- cn.hutool.core 包名

## 踩坑记录

### Sftp.upload 不会自动创建目录
> **现象**：`cn.hutool.extra.ssh.Sftp.upload()` 底层调用 JSch 的 `put` 方法，如果目标目录不存在，直接报错 `SftpException: Failure`。
>
> **对比**：`Ftp.upload()` 底层会在上传前调用 `mkDir` 自动创建目录，所以不会出现此问题。
>
> **解决**：调用 `Sftp.upload()` 前，先手动调用 `Sftp.mkDirs()` 确保目标路径存在。

## 关联连接
- [[Java]] — 所属语言生态
- [[SpringBoot]] — 常配合使用
