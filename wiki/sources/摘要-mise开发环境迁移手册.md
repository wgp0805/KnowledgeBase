---
title: "摘要-mise开发环境迁移手册"
type: source
tags: [来源, 原始文件, mise, 开发环境, 多版本管理]
sources: [raw/01-articles/Mise 开发环境迁移完整手册.md]
last_updated: 2026-10-20
---

## 核心摘要
一份 Windows 下用 mise 统一管理 Java/Node/Maven/PHP 多版本的完整迁移手册，目标是淘汰 nvm 与手动 JDK 切换，实现多项目环境隔离与自动切换。核心机制：`MISE_DATA_DIR=D:\java\mise-software` 统一存放 SDK，PATH 只保留 shims 代理目录（shims 下的 exe 转发到当前激活版本）；项目根目录放 `mise.toml`，进入目录自动切换版本、离开恢复全局，优先级为项目 mise.toml > 全局。配套 PowerShell profile 钩子（`mise activate` + `prompt` 中调 `mise hook-env`）实现 cd 即切换，IDEA 配置提供"固定 installs 目录"与"shim 动态联动"两方案（须统一，防止 IDEA 与终端版本不一致）。手册记录了踩坑：Java 版本须写成 `java@temurin-版本`、Windows PHP 需 vfox 插件与 VC++ 运行库、MISE_DATA_DIR 一旦确定不可改、Node 跨大版本原生包需重装。

## 关联连接
- [[Mise]] — 多语言版本管理工具
- [[IntelliJIDEA]] — 配套 IDE 配置
- [[Maven]] — 由 mise 管理的构建工具
- [[Java]] / [[Node.js]] — 管理的目标运行时
