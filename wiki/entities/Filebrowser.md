---
title: "Filebrowser"
type: entity
tags: [工具, Docker, 文件管理, 自托管]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
Filebrowser 是轻量级 Web 文件管理器（镜像 `filebrowser/filebrowser`），用浏览器管理服务器文件，替代复杂 FTP 客户端。

## 关键信息
- 基础操作：上传、下载、删除、重命名、编辑
- **用户与权限管理**：可为不同用户设不同目录与访问权限，适合小团队共享
- 配置驱动：可通过配置文件自定义界面与功能
- 典型用途：远程管理服务器文件、给非技术同事一个"能点开就下载"的入口
- 最小启动：`-v $PWD/filebrowser:/srv -p 80:80 filebrowser/filebrowser`；生产务必把 `/database`（filebrowser.db）也挂出来持久化
- 同类对照：[[Dockge]] 管容器、Filebrowser 管文件，二者常组合成服务器"面板组"
- 安全提醒：默认凭据必须改，且建议只在内网或 VPN 后暴露

## 关联连接
- [[Docker]] — 分发方式
- [[MinIO]] — 对象存储对照（程序化接口 vs 人工操作）
- [[Dockge]] — 常同机部署的容器面板
- [[摘要-8个docker神器]] — 来源
