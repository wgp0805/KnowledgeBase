---
title: "Graphify"
type: entity
tags: [开源项目, 知识图谱, AI编程, 代码分析, MCP]
sources: [raw/09-archive/2026-11-04 - 这个GitHub 142K+ Star的开源神器用一条命令把整个项目变成AI能查的知识图谱！！.md]
last_updated: 2026-11-04
---

## 定义

Graphify 是 Graphify Labs 开源的项目知识图谱工具（GitHub `Graphify-Labs/graphify`，142K+ Star，2026-04 开源）：给 AI 编程助手挂载"项目地图"能力——执行 `/graphify .` 扫描当前项目，把代码、文档、PDF 等整理成一张可查询、可遍历的知识图谱，让助手回答问题时先查图而不是每次翻文件重拼上下文。

## 关键信息

### 核心特性

| 维度 | 说明 |
|------|------|
| **本地代码解析** | 基于 **tree-sitter** 语法树解析，覆盖约 40 种语言，全程本机完成、不调模型、不传代码 |
| **非代码材料** | 文档/PDF/图片/音视频需模型参与（当前会话模型或自配 API key），Word/Excel/视频需扩展包 |
| **关系溯源标签** | 边分三类：`EXTRACTED`（源码直接存在）/`INFERRED`（推断）/`AMBIGUOUS`（拿不准），便于判断是否需复核 |
| **三个查询命令** | `query`（自然语言→相关子图）、`path`（两对象连通路径）、`explain`（概念及周边关系） |
| **核心节点识别** | 自动找出连接数最多的 **god nodes**（项目绕不开的核心概念） |
| **子系统切分** | 用 **Leiden 算法**聚类并自动命名，`graph.html` 按子系统分块浏览 |
| **注释与决策记录** | 以 NOTE/WHY 开头的注释、架构决策记录被抽成独立节点挂到对应代码旁 |
| **增量与团队协作** | 改过的文件增量更新；git hook 后每次 commit/切分支自动重建；图文件可提交仓库；可做 MCP/HTTP 服务共用；PR 看板显示改动了图中哪些区域、哪些 PR 撞同一子系统 |

### 基准数据（LOCOMO 数据集）

- recall@10：**0.497**（mem0 0.048、supermemory 0.149）
- QA 准确率：**45.3%**（高于 mem0，低于 supermemory 的 49.7%）

### 安装与踩坑

```bash
# 前置：Python 3.10+
uv tool install graphifyy      # 注意 PyPI 包名两个 y
graphify install               # 注册给 AI 助手
/graphify .                    # 在助手里建图
```

- 安装后命令仍叫 `graphify`；PyPI 上其他相似包与官方无关
- Windows PowerShell 执行 `graphify .`（不带斜杠，否则当路径）
- `command not found` → 多因工具目录没进 PATH（`uv tool update-shell` + 开新终端）
- 中文提问多可装 `graphifyy[chinese]`（含 jieba 分词）

### 适用边界

- **收益明显**：500~5000 个文件的仓库——新人摸架构、团队共享项目结构
- **不如直接读文件**：几十个文件的小项目
- **成本提醒**：非代码内容建图会消耗 API 额度；纯代码部分零费用

## 关联连接
- [[摘要-graphify代码知识图谱]] — 来源
- [[知识图谱]] — 上位概念（代码知识图谱场景）
- [[冰河]] — 介绍作者
- [[MCP]] — 图可做成 MCP 服务接入其他工具
- tree-sitter — 本地语法树解析引擎（无独立页，见本页说明）
- [[Cursor]] — 同类 AI 编程助手生态
- [[Neo4j]] — 知识图谱存储对照（Graphify 输出为文件/服务而非图数据库）
