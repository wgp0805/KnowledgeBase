---
title: "Nexus"
type: entity
tags: [Maven, 私服, 仓库管理]
sources: [raw/01-articles/Maven依赖管理项目构建工具.md]
last_updated: 2026-05-22
---

## 定义
Nexus（由 Sonatype 开发）是当前最流行的 Maven 私服仓库管理器，作为局域网内的仓库代理，缓存远程仓库构件并支持部署第三方和私有构件。

## 关键信息
- 仓库类型：proxy（远程仓库代理）、hosted（本地上传部署）、group（聚合多个仓库）
- 默认端口：8081
- 默认管理员账号密码：admin / 查看 admin.password 文件
- 支持匿名访问配置
- 可配置中央仓库代理为阿里云镜像加速（Remote Storage URL 设为 http://maven.aliyun.com/nexus/content/groups/public/）

### 使用场景
- 节省外网带宽：消除重复请求
- 加速下载：局域网内下载更快
- 部署第三方构件：Oracle JDBC 驱动等私有构件
- 提高稳定性：外部网络中断时仍可构建

## 关联连接
- [[Maven]] — 构建工具
- [[摘要-maven]] — 来源
