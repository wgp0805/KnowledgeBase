---
title: "预签名URL"
type: concept
tags: [对象存储, S3, 安全, 临时授权]
sources: [raw/09-archive/SpringBoot+Minio实现高效文件存储解决方案.md]
last_updated: 2026-10-27
---

## 定义
预签名 URL（Presigned URL）是对象存储用 AccessKey/SecretKey 对请求预签名后生成的**限时访问链接**：客户端在有效期内无需持有任何永久凭证，即可按链接执行下载（或上传）操作，过期自动失效。

## 关键信息
- **解决的问题**：对象默认私有，把 AccessKey/SecretKey 暴露给前端不安全；由服务端签发临时链接，前端直连存储完成下载/上传，文件流量不经手业务服务器
- **MinIO 用法**：`minioClient.getPresignedObjectUrl(GetPresignedObjectUrlArgs.builder().method(Method.GET).bucket(bucket).object(objectKey).expiry(minutes, TimeUnit.MINUTES).build())`
- **典型参数**：HTTP 方法（GET 下载 / PUT 上传）、bucket、object、有效期（分钟级）
- **安全价值**：敏感文件不设公开读，靠短期签名链接按需授权；即使链接泄露，损失窗口也被限制在有效期内，是对象存储权限控制的常用手段
- **实践注意**（[[RustFS]] 场景记录）：S3Presigner 的 endpoint 要用对外可访问的 `publicUrl`，否则签出的链接内网可达、外网打不开

## 关联连接
- [[MinIO]] — 本知识库来源实践中的预签名实现
- [[RustFS]] — S3 兼容存储同样适用，注意 publicUrl 配置
- [[distributed-object-storage]] — 所属存储架构
- [[摘要-springboot-minio文件存储]] — 来源
