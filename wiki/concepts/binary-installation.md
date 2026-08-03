---
title: "binary-installation"
type: concept
tags: [概念, 运维, 安装]
sources:
  - raw/01-articles/一个运维狗的 Elasticsearch 到 SkyWalking 的部署之路.md
last_updated: 2026-08-03
---

## 定义
二进制安装（Binary Installation）指直接下载编译好的二进制包进行部署的方式，区别于源码编译、包管理器或容器化部署，常用于 SkyWalking、Elasticsearch 等服务端软件的快速部署。

## 关键信息
- **流程**：下载官方二进制包 → 解压 → 配置 → 启动，配合 systemd 管理服务
- **优点**：无需编译环境、部署路径清晰、便于精确控制版本
- **缺点**：升级/回滚需手动管理，依赖人工配置
- **实例**：[[SkyWalking]] 9.3.0 与 [[Elasticsearch]] 8.5.1 的 Linux 二进制安装

## 关联连接
- [[SkyWalking]] — 安装对象
- [[Elasticsearch]] — 安装对象
- [[Linux]] — 部署平台
- [[摘要-skywalking-install]] — 安装实战来源
