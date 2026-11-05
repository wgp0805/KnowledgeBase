---
title: "摘要-graphify代码知识图谱"
type: source
tags: [来源, 原始文件, Graphify, 知识图谱, AI编程, 开源]
sources: [raw/09-archive/2026-11-04 - 这个GitHub 142K+ Star的开源神器用一条命令把整个项目变成AI能查的知识图谱！！.md]
last_updated: 2026-11-04
---

## 核心摘要

冰河技术（2026-11-04）介绍开源工具 **Graphify**（GitHub 142K+ Star，2026-04 开源）：给 AI 编程助手挂载"项目地图"能力——安装后在助手里执行 `/graphify .`，扫描当前项目把代码/文档/PDF 等整理成**可查询、可遍历的知识图谱**，此后助手回答问题时先查图，不必每次翻十几个文件重拼上下文。

**一条命令建图，代码解析不花模型额度**：用 **tree-sitter** 做语法树解析，覆盖约 40 种语言，代码解析全程本机完成、不调大模型、不传代码出去 → 仅建代码图谱零 API 费用；需要模型的只有文档/PDF/图片/音视频等非代码内容（用当前会话模型或自配 key）。

**每条关系标来源**：边带标签——`EXTRACTED`（源码中直接存在）、`INFERRED`（工具推断）、`AMBIGUOUS`（拿不准），排查时一眼判断哪些关系需要复核。三个常用命令：`query`（自然语言问题→相关子图）、`path`（两对象如何连通）、`explain`（解释某概念及周边关系）。官方示例查 FastAPI 的 APIRouter：来自 `routing.py` 第 2210 行、连接 47 个节点。

**基准数据**（LOCOMO 数据集）：recall@10 = 0.497（mem0 0.048、supermemory 0.149）；QA 准确率 45.3%（高于 mem0，低于 supermemory 的 49.7%）。

**自动找核心节点与切分子系统**：① 找出连接数最多的 **god nodes**（项目绕不开的核心概念，新人先看能快速抓重点）；② 用 **Leiden 算法**把图切成子系统并自动命名，`graph.html` 按子系统分块浏览。除代码外，Markdown/PDF/图片/音视频/SQL 表结构/Terraform 配置也能进同一张图（Word/Excel/视频需装扩展包）；以 NOTE/WHY 开头的注释和架构决策记录会被抽成独立节点挂在被解释代码旁——"当时为什么这么写"与代码同图可查。

**图随代码更新、可团队共用**：改过的文件增量更新（不必全量重跑）；装 git hook 后每次 commit/切分支自动重建；图文件可直接提交进仓库供他人 clone 使用；可做成 MCP 服务或起 HTTP 服务供团队共用；还有 PR 看板显示每个 PR 改了图中哪些区域、哪些 PR 撞同一子系统，辅助安排 review 顺序。

**上手与坑**：Python 3.10+，`uv tool install graphifyy` + `graphify install`，然后 `/graphify .`。注意 PyPI 包名是 `graphifyy`（两个 y，安装后命令仍叫 `graphify`）；Windows PowerShell 执行 `graphify .` 不带斜杠；command not found 多半是 PATH 问题（`uv tool update-shell` + 新终端）；中文提问多可装 `graphifyy[chinese]`（含 jieba 分词）。

**适用**：500~5000 文件仓库收益最明显（新人摸架构、团队共享结构）；几十个文件的小项目直接让助手读文件更快。注意非代码内容建图会消耗 API 额度。

## 关联连接
- [[Graphify]] — 本文主角实体
- [[知识图谱]] — 上位概念（代码知识图谱场景）
- [[冰河]] — 作者
- [[MCP]] — 图可做成 MCP 服务接入其他工具
- [[Cursor]] — 同类 AI 编程助手生态（Graphify 是给助手挂载的能力）
- tree-sitter — 本地语法树解析引擎（无独立页，见实体页说明）
- 代码知识图谱 — 本文提炼的场景概念（并入 [[知识图谱]]）
