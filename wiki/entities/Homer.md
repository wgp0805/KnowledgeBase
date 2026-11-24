---
title: "Homer"
type: entity
tags: [工具, Docker, 导航页, 自托管]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
Homer（镜像 `b4bz/homer`）是由静态 YAML 驱动的个人导航主页生成器，用来把自托管服务、常用链接聚成一个漂亮入口页。

## 关键信息
- 纯静态：一个 `config.yml` 定义分组、服务卡片、图标、链接，改文件即改页面
- 适合：个人主页、家庭/内网服务器入口页（把所有自托管服务的入口集中）
- 最小启动：`-p 8080:8080 -v ${PWD}/assets:/www/assets b4bz/homer:latest`
- 端口注意：默认 8080，与 [[CodeServer]] 冲突
- 与 [[Flame]] 的区别：Homer 偏"多分组 + 图标墙"的经典风格，Flame 更极简；两者都靠 YAML 配置
- 边界：纯展示层，没有权限与状态，别把内网地址与凭据写进公开可访问的 config

## 关联连接
- [[Docker]] — 分发方式
- [[Flame]] — 极简风同类
- [[CodeServer]] — 同为 8080 端口
- [[UptimeKuma]] / [[Dockge]] — 常同机部署的面板组
- [[摘要-8个docker神器]] — 来源
