---
title: "摘要-deepseek-harness桌面客户端"
type: source
tags: [来源, 原始文件, DeepSeekHarness, 桌面Agent, 办公Agent]
sources: [raw/01-articles/2026-09-25-DeepSeek Harness客户端来了，AI办公又多了一个王者？.md]
last_updated: 2026-09-28
---

## 核心摘要

[[欧阳俊杰]] 实测 DeepSeek 尚未官宣但已在社区流传的官方桌面客户端 **DeepSeek Harness**（Windows/macOS，暂无 Linux，走 nightly 通道）：启动第一步就是选择本地文件夹作为工作区，支持读写本地文件、联网搜索、终端操作与多智能体协作，登录可用 DeepSeek 账号（账号模式）或 API Key（API 模式），二者选错会出现"能输入任务但不干活"的典型问题。客户端内置四种模式——标准、PTC、极简、创造——并遵循 **Everything is a Plugin** 的插件化理念，已预装智能体团队、语音输入、终端、Agent Loop、Subagent、网页搜索等插件，其中智能体团队允许多个 Agent 分工（查资料、整理数据、写文档）再由主 Agent 汇总。首次启动的初始化会询问用途（办公与创作/代码与开发）与过程可见度（只看结果/关键步骤/全部过程），把"AI 干活该给用户看多少"的选择权交给用户。文章判断 DeepSeek 正式从"模型、网页、App、API"走向接管本地工作，与 [[WorkBuddy]]、[[豆包工作]]、千问办公在 [[办公Agent]] 赛道正面相撞，而它手握模型品牌与用户基础。

### 关键要点

- **产品形态跃迁**：从"更方便地聊 DeepSeek"变成"进入电脑本地文件夹干活"——工作区概念是与网页版的根本区别。
- **macOS 版带 DeepSeek 主体开发者签名并通过 Apple 公证**，社区核验指向官方体系，但官方尚未正式官宣。
- **仍是 nightly 版本**：更新快、Bug 多，细节仍在打磨。
- **踩坑提示**：账号模式与 API 模式必须和登录方式一致，否则任务不执行。

## 关联连接
- [[DeepSeekHarness]] — 核心实体（增量更新：官方桌面客户端）
- [[DeepSeek]] — 所属公司
- [[办公Agent]] — 所进入的赛道（增量更新）
- [[桌面Agent]] — 产品形态上位概念
- [[欧阳俊杰]] — 作者
- [[WorkBuddy]] — 同赛道产品
- [[豆包工作]] — 同赛道产品
- [[摘要-deepseek-harness内测]] — DSH 工程化内测摘要
- [[摘要-deepseek-harness命令大全]] — DSH 命令行入口速查
