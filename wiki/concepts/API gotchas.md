---
title: "API gotchas"
type: concept
tags: [概念, 设计, 踩坑, 经验]
sources: [raw/01-articles/2026-09-01-Penpot UIUX Design 拆解：把设计判断力塞进 MCP 工具链.md]
last_updated: 2026-09-01
---

## 定义
penpot-uiux-design中记录的5条Penpot Plugin API踩坑记录，这些不是API文档能推出来的，全是撞过墙才有的经验。

## 关键信息
1. width/height是只读属性，改尺寸只能用shape.resize(w, h)
2. parentX/parentY只读，移动位置要用penpotUtils.setParentXY
3. z轴排序用insertChild(index, shape)，不是appendChild
4. flex子节点数组在dir为column或row时顺序是反的
5. text.resize之后必须把growType重置回auto-width或auto-height

## 关联连接
- [[摘要-Penpot-UIUX-Design-MCP工具链]] — 来源文章
- [[PenpotUIUXDesign]] — 包含这些踩坑记录的Skill
- [[先探查再创建]] — 核心架构思想
- [[设计系统]] — 工作流的第一步
