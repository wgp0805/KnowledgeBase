---
title: "Docker"
type: entity
tags: [容器, DevOps]
sources: [raw/09-archive/Docker-window环境下部署RocketMq.md, raw/09-archive/docker安装及使用-windows环境.md, raw/09-archive/docker部署nacos.md, raw/09-archive/Docker部署Redis全攻略：持久化、自定义网络与配置详解.md, raw/09-archive/使用Docker在Windows上部署独立MySQL.md, raw/09-archive/使用n8n搭建Agent项目笔记.md, raw/09-archive/同事一个比喻，让我搞懂了Docker和k8s的核心概念.md, raw/01-articles/2026-08-24 - 拒绝再买服务器！我用 Docker + FRP 实现内网穿透，舒服~.md]
last_updated: 2026-08-25
---

## 定义
Docker 是一个开源的应用容器引擎，让开发者可以打包应用及依赖到一个可移植的容器中，发布到任何 Linux/Windows 机器上。

## 关键信息
- 容器化部署提高环境一致性
- Docker Desktop 提供 Windows/Mac 上的容器运行环境
- 支持卷挂载（Volume Mounting）实现数据持久化
- 支持自定义网络配置（bridge/host/overlay）
- docker-compose 可编排多容器服务

## 常用命令参数

### `docker logs -f`
- `-f` / `--follow`：持续跟踪日志输出（类似 `tail -f`），实时查看容器日志流
- 其他常用参数：`--tail n`（只显示最后 n 行）、`--since`（指定起始时间）、`--until`（指定结束时间）、`-t` / `--timestamps`（显示时间戳）、`--details`（显示额外详情）

### `docker rm -f`
- `-f` / `--force`：强制删除正在运行的容器（先发 SIGKILL 停止，再删除），不加 `-f` 时只能删除已停止的容器
- 场景：常用于快速重建容器，如 `docker rm -f nacos && docker run ...`（见 [[摘要-docker部署nacos]]）

## 核心概念关系

```
Dockerfile (配方) ──docker build──→ Image (镜像/静态快照) ──docker run──→ Container (容器/运行态)
```

- **镜像（Image）**：静态的、只读的系统快照，包含 OS + 运行时 + 依赖 + 代码，类似一张光盘
- **容器（Container）**：镜像的运行态，动态、可写，销毁后改动消失（除非挂载外部存储）
- **Dockerfile**：定义如何构建镜像的配方文件（基于哪个镜像、安装什么依赖、执行什么命令）
- **docker-compose**：定义如何运行一组容器的编排工具（多服务启动、网络、卷挂载）

一个镜像可以同时跑多个容器，互不影响。

## Docker + FRP 内网穿透（2026-08，详见 [[摘要-docker-frp-内网穿透]]）
- 使用 `fatedier/frps:v0.61.2` 和 `fatedier/frpc:v0.61.2` 镜像
- `--network host` 复用主机端口，避免端口映射复杂性
- 配置文件通过卷挂载（`-v`）注入容器
- frps（服务端）部署在公网云服务器，frpc（客户端）部署在内网本地电脑
- token 密钥验证，客户端与服务端必须一致

## 关联连接
- [[DockerDesktop]] — 桌面版
- [[MySQL]] — 数据库容器化
- [[Redis]] — 缓存容器化
- [[RocketMQ]] — 消息队列容器化
- [[Nacos]] — 注册中心容器化
- [[FRP]] — 内网穿透工具（Docker 部署）
- [[kubernetes-detailed-guide]] — Kubernetes 详细教程与 Docker 对比
- [[kubernetes-introduction]] — Kubernetes 入门介绍
- [[摘要-使用Docker在Windows上部署独立MySQL]] — 在 Windows 上使用 Docker 部署 MySQL …
- [[摘要-idea的特殊用法及远程DEBUG的方法]] — 介绍 IntelliJ IDEA 远程调试 Java 应用的…
- [[摘要-docker-frp-内网穿透]] — 来源（Docker + FRP 内网穿透）
- [[kafka-complete-tutorial]] — Apache Kafka 完整教程
