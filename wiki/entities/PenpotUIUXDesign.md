---
title: "PenpotUIUXDesign"
type: entity
tags: [工具, 设计, MCP, Skill]
sources: [raw/01-articles/2026-09-01-Penpot UIUX Design 拆解：把设计判断力塞进 MCP 工具链.md]
last_updated: 2026-09-01
---

## 定义
penpot-uiux-design这个Skill，将设计判断力编码成MCP工具链的工作流，挂在Smithery上，ID是github/penpot-uiux-design。

## 关键信息
- 依赖的penpot/penpot-mcp仓库在2026年2月3日已归档
- 代码迁进了Penpot主仓库的develop/mcp目录
- 工具面：execute_code、export_shape、import_image、penpot_api_info
- 6步工作流：先确认设计系统，再用shapeStructure看层级，用findShapes定位元素，然后创建或修改，套addFlexLayout做响应式，最后export_shape自验
- 5条API gotchas：width/height只读、parentX/parentY只读、z轴排序用insertChild、flex子节点数组顺序反转、text.resize后必须重置growType

## 关联连接
- [[摘要-Penpot-UIUX-Design-MCP工具链]] — 来源文章
- [[Penpot]] — 设计工具
- [[PenpotMCP]] — MCP服务器
- [[Smithery]] — Skill托管平台
- [[先探查再创建]] — 核心架构思想
- [[API gotchas]] — 踩坑记录
