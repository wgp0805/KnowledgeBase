---
title: "Docker"
type: entity
tags: [容器, DevOps]
sources: [raw/01-articles/Docker-window环境下部署RocketMq.md, raw/01-articles/docker安装及使用-windows环境.md, raw/01-articles/docker部署nacos.md, raw/01-articles/Docker部署Redis全攻略：持久化、自定义网络与配置详解.md, raw/01-articles/使用Docker在Windows上部署独立MySQL.md, raw/01-articles/使用n8n搭建Agent项目笔记.md]
last_updated: 2026-05-19
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

## 关联连接
- [[DockerDesktop]] — 桌面版
- [[MySQL]] — 数据库容器化
- [[Redis]] — 缓存容器化
- [[RocketMQ]] — 消息队列容器化
- [[Nacos]] — 注册中心容器化
- [[kubernetes-detailed-guide]] — Kubernetes 详细教程与 Docker 对比
- [[kubernetes-introduction]] — Kubernetes 入门介绍
