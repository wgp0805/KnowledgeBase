---
title: "DaoCloud加速器"
type: concept
tags: [Docker, 镜像加速, 国内网络, DaoCloud]
sources: [raw/09-archive/2026-09-16-Ubuntu 22.04 Docker 从零部署全栈项目实录：Next.js + FastAPI + PostgreSQL 一次跑通 - 码农刚子.md]
last_updated: 2026-09-17
---

## 定义
DaoCloud 加速器是 DaoCloud 提供的 Docker 镜像公共加速服务，地址 `https://docker.m.daocloud.io`，用于解决国内直接拉 `docker.io` 镜像容易超时的问题。是 [[国内源三件套]] 中最稳的 Docker 镜像加速方案。

## 关键信息

### 配置方法
- 配置文件：`/etc/docker/daemon.json`
- 内容：
  ```json
  {
    "registry-mirrors": ["https://docker.m.daocloud.io"]
  }
  ```
- 重启生效：`systemctl daemon-reload && systemctl restart docker`

### 关键坑
- **地址末尾不要加斜杠**，否则可能报 403
- 错误：`https://docker.m.daocloud.io/`
- 正确：`https://docker.m.daocloud.io`

### 与其他加速器对比
[[码农刚子]] 踩过几个坑后结论：
- 腾讯加速器：不稳
- 163 加速器：不稳
- 阿里云专属加速器：不稳
- **DaoCloud 公共加速器**：最稳

## 关联连接
- [[国内源三件套]] — 所属组合
- [[Docker]] — 加速对象
- [[码农刚子]] — 推荐者
- [[摘要-ubuntu-docker-全栈部署实录]] — 来源
