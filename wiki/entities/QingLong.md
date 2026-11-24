---
title: "QingLong"
type: entity
tags: [工具, Docker, 定时任务, 脚本]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
青龙面板（QingLong，镜像 `whyour/qinglong`）是带 Web 界面的定时脚本任务管理器，支持用 Cron 跑各种语言脚本。

## 关键信息
- 能力：任务调度（定时/Cron）、脚本管理、依赖安装、环境变量管理、日志查看
- 常见个人用途：每日签到、自动回复、数据备份、爬虫定时抓取
- 最小启动：`-p 5700:5700 -v $PWD/ql:/ql/data whyour/qinglong:latest`
- 数据卷 `/ql/data` 必须持久化，脚本与环境变量都在里面
- 边界与风险：本质是"服务器上的定时执行器"，脚本来源不可信时等于给人留后门；公开面板必须改默认凭据并限制来源 IP（[[最小权限原则]]）
- 定位对比：轻量个人自动化用它；企业级调度看 [[XXL-JOB]] / [[PowerJob]]

## 关联连接
- [[Docker]] — 分发方式
- [[XXL-JOB]] — 企业级分布式任务调度对照
- [[PowerJob]] — 同类调度平台
- [[任务调度]] — 所属概念
- [[摘要-8个docker神器]] — 来源
