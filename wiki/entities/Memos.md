---
title: "Memos"
type: entity
tags: [工具, Docker, 笔记, 自托管]
sources: ["raw/09-archive/2026-11-20 - 8 个让你直呼卧槽的 Docker 神器，让你的服务器瞬间开挂！.md"]
last_updated: 2026-11-24
---

## 定义
Memos（镜像 `neosmemo/memos`）是轻量级开源自托管笔记工具，主打"随手记想法/灵感"，产品形态接近单机版 flomo。

## 关键信息
- 极轻：单容器、占用资源少、启动快，数据落在 `/var/opt/memos`
- 交互简单：纯时间流式记录，适合碎片化灵感与日常笔记
- 与重型知识库的分工：Memos 负责"输入端随手记"，结构化沉淀仍要靠 [[Obsidian]] / 本 Wiki 这类体系
- 最小启动：`-p 5230:5230 -v ~/.memos/:/var/opt/memos neosmemo/memos:latest`
- 适合创作者、开发者做"第二大脑"的收件箱层

## 关联连接
- [[Docker]] — 分发方式
- [[Obsidian]] — 结构化知识库对照
- [[LLMWiki]] — 从随手记到知识编译的流程
- [[摘要-8个docker神器]] — 来源
