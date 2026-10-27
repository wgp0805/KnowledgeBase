---
title: "MinIO"
type: entity
tags: [对象存储, S3兼容, 分布式存储, Go语言]
sources: [raw/09-archive/什么是 MinIO.md, raw/09-archive/MinIO 社区版被故意阉割，Web管理功能全面移除，来试试国产的RustFS？.md, raw/09-archive/SpringBoot+Minio实现高效文件存储解决方案.md]
last_updated: 2026-10-27
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
- **仓库归档**：2026-04-25 归档主仓库；2026-07-15 归档 mc（MinIO Client）仓库并删除 Dockerhub 上的 mc 镜像，社区用户无法获取最新版本和安全补丁

## Spring Boot 集成（minio-java SDK）
2026-10 实战教程给出的「配置-工具-业务」三层集成模式：
- **配置层**：yml 配置 `url / username / password / bucketName`，`MinioProperties` 用 @ConfigurationProperties + @Component 绑定为 Bean（见 [[ConfigurationProperties]]）
- **工具层**：`MinioUtil` 封装 MinioClient——@PostConstruct 初始化客户端并自动建桶（bucketExists 不存在则 makeBucket）；核心 API：putObject / getObject / removeObject / statObject / getPresignedObjectUrl
- **业务层**：FileService + FileController 暴露图片上传/下载/删除接口；上传支持三种形态——表单文件（MultipartFile）、字节数组（如压缩后的图片）、本地临时文件（如生成的 Excel）
- **工程要点**：
  - 唯一文件名：`yyyy-MM-dd/uuid.扩展名`（日期分目录 + UUID 去横线防重名，见 [[UUID]]）
  - 大文件流式传输：putObject 直传 InputStream（partSize -1），避免整文件读入内存
  - 下载响应头用 URLEncoder 编码中文文件名（`+` 替换回 `%20`）防乱码；IOUtils.copy 内置 8KB 缓冲
  - 受检异常统一包装为 RuntimeException；fileExists 捕获 NoSuchKey 判定对象不存在
  - 敏感文件不设公开读，用 [[预签名URL]]（expiry 分钟级有效期）按需授权
- **生产提醒**（教程原文）：集群部署保证高可用、定期备份桶数据；选型时注意社区版闭源归档风险（对照 [[RustFS]]）

## 关联连接
- [[摘要-minio-intro]] — 来源
- [[摘要-minio-rustfs]] — 来源
- [[摘要-springboot-minio文件存储]] — Spring Boot 集成实战来源
- [[SpringBoot]] — 集成框架
- [[预签名URL]] — 限时访问直链机制
- [[Docker]] — 容器化部署方式
- [[RustFS]] — 国产替代方案
- [[AiStor]] — MinIO 商业化产品
- [[distributed-object-storage]] — 分布式对象存储架构
- [[open-source-commercialization]] — 开源商业化模式
