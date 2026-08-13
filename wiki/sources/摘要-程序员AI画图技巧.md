---
title: "摘要-程序员AI画图技巧"
type: source
tags: [AI画图, 文本绘图, 架构图, 流程图]
sources: [raw/09-archive/程序员必备的4种AI画图技巧.md]
last_updated: 2026-06-26
---

## 核心摘要

苏三介绍了 4 类基于"文本绘图"的 AI 画图技巧，所有图均由 AI 生成可编辑文本，保证可二次精修：

1. **文本作图语言**（PlantUML / Mermaid / Flowchart / Graphviz）：语雀原生支持，用 `/文本` 唤起，PlantUML 强于线性流程与时序图，Graphviz 强于非线性复杂图，Mermaid 上手最快、Markdown 原生集成。
2. **Obsidian Canvas**：本地多文档关系展示与思维导图，可把笔记直接作为子节点。
3. **SVG**：作者认为**最适合架构图**的方式，文章给出了完整的"SVG 海报设计专家 Prompt"并演示在 Cursor 中配置 Project Rule（Always）。
4. **draw.io**：自由度最高，可导入 AI 生成的 XML，使用代码块右上角复制粘贴到 draw.io 才能正确渲染。

作者推荐栈：Cursor + claude-3.7-sonnet Thinking 模式。原则：所有图必须能手动调整，避免不可编辑的"AI 黑盒图"。

## 关联连接

- [[文本绘图]] — 核心方法论
- [[Mermaid]] — Markdown 原生集成方案
- [[PlantUML]] — 时序图首选
- [[Graphviz]] — 复杂非线性图首选
- [[draw-io]] — XML 编辑流程图
- [[SVG]] — 架构图首选
- [[ObsidianCanvas]] — 多文档关系图
- [[Cursor]] — 主要使用环境
