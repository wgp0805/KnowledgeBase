---
title: "摘要-8个docker神器"
type: source
tags: [来源, Docker, 自托管, 运维工具]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 核心摘要
小哈学Java 2026-11-20 的 Docker 自托管工具清单（转载自掘金，原文 juejin.cn/post/7438638095946055716），盘点了 Docker Hub 上一批"小而美"的镜像，每个都给出 `docker run` 与 `docker-compose.yml` 两套最简启动配置。目录列了 10 项、正文实际覆盖 11 个：[[CodeServer]]（浏览器里的完整 VS Code，可把宿主机工作目录映射进去当文件资源管理器用）、[[CloudBeaver]]（Web 版多数据库管理，替代操作别扭的 PhpMyAdmin，带 SQL 面板与智能提示）、[[QingLong]]（定时脚本任务面板，签到/爬虫/备份）、[[PocketBase]]（轻量 Serverless：数据+文件存储、用户授权、日志，单容器起步）、[[Homer]]（个人导航主页）、[[UptimeKuma]]（服务监控 + 多渠道通知）、[[Memos]]（轻量笔记/灵感速记）、[[Umami]]（开源、隐私友好、不采集个人数据的站点统计）、[[Flame]]（极简风导航页）、[[Filebrowser]]（在线文件管理器，含用户与权限管理）、[[Dockge]]（以 compose.yaml 为中心的管理器，1.4.0 起支持多服务器）。文末统一提示：这些只是最基础启动配置，定制要回官方仓库查参数；需要映射宿主机目录的务必手动创建目录。

> 原文标题称"8 个"，实际清单为 11 个；目录漏掉青龙面板但正文有完整配置，属清单口径不一致。

## 关联连接
- [[Docker]] — 运行载体
- [[CodeServer]] — 远程开发
- [[CloudBeaver]] — 数据库管理
- [[QingLong]] — 定时任务面板
- [[PocketBase]] — 轻量 Serverless 后端
- [[Homer]] / [[Flame]] — 导航页两种风格
- [[UptimeKuma]] — 服务监控
- [[Memos]] — 个人笔记
- [[Umami]] — 隐私友好统计
- [[Filebrowser]] — 文件管理
- [[Dockge]] — compose 管理
- [[DockerCompose生产配置]] — 从单容器到 compose 落地的下一步
- [[自托管]] — 该清单的共性场景（待沉淀概念）
