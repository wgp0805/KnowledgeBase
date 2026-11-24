---
title: "Dockge"
type: entity
tags: [工具, Docker, Compose, 运维]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
Dockge 是围绕 `docker-compose.yaml` 的 Docker 管理面板，1.4.0 起支持多服务器，定位是"compose 文件的可视化编辑器 + 容器控制台"。

## 关键信息
- **一站式管理**：新建/修改/启动/停止/重启/删除 compose 栈
- **一键更新镜像**、**网页版终端**（浏览器里敲命令）
- **可视化编辑 compose.yaml**，所见即所得，不用手敲 YAML
- **一键转换**：把复杂 `docker run` 命令自动转成 `compose.yaml`
- **多服务器支持**（1.4.0 新增）：一个界面管多台机器的 Docker
- **文件原生存储**：配置文件就在硬盘上，不锁死在自己的数据库里，命令行照常可用
- **实时反馈**：拉镜像/启停的进度与终端输出实时显示
- 界面风格与 [[UptimeKuma]] 同源，操作直观
- 最小启动需挂载 `/var/run/docker.sock`（等价于宿主机 root 权限，必须做好访问控制）

## 关联连接
- [[Docker]] — 被管理的容器引擎
- [[DockerCompose生产配置]] — compose 写法规范
- [[UptimeKuma]] — 同风格界面的姊妹工具
- [[Portainer]] — 同类 Docker 面板对照
- [[摘要-8个docker神器]] — 来源
