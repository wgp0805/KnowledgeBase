---
title: "Flame"
type: entity
tags: [工具, Docker, 导航页, 极简]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
Flame（镜像 `pawelmalak/flame`）是极简风格的自托管个人导航页/应用仪表盘，可聚合常用网站与自建服务入口。

## 关键信息
- 定位：个人导航 + 书签管理，界面比 [[Homer]] 更克制
- 配置：`/app/data` 持久化，支持 `PASSWORD` 环境变量做访问保护
- 最小启动：`-p 5005:5005 -v flame:/app/data pawelmalak/flame`
- 适合：想快速得到一个"打开就是我的服务列表"的首页，不想折腾主题
- 边界：只解决"入口聚合"，不提供服务健康状态（状态监控用 [[UptimeKuma]]）

## 关联连接
- [[Docker]] — 分发方式
- [[Homer]] — 经典分组图标墙对照
- [[UptimeKuma]] — 状态监控分工
- [[摘要-8个docker神器]] — 来源
