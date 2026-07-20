---
title: "摘要-architecture-diagram-generator"
type: source
tags: [来源, AI画图, Skill, 架构图]
sources:
  - raw/01-articles/又一个神级画图 Skill 开源，再见 draw.io！.md
  - raw/01-articles/推荐一个神级画图Skill.md
last_updated: 2026-07-20
---

## 核心摘要

[[小锋]]（锋哥）介绍 [[CocoonAI]] 团队开源的 Claude AI Skill [[ArchitectureDiagramGenerator]]（架构图生成器）。与传统 [[draw-io]] 手动拖拽不同，它用人话描述系统架构，Claude 生成深色主题、排版整齐的 HTML 架构图，浏览器打开即可查看，支持一键导出 PNG/PDF。属于[[文本绘图|文本绘图]]方法论中"AI 生成 HTML/SVG"路线，核心优势是用对话代替手工，改图只需聊天指令。

## 关键信息

- 输出：自包含 HTML（CSS + SVG 内嵌），发邮件/飞书/挂静态页无需对方装软件
- 导出：页面工具栏 Copy（高清 PNG 到剪贴板）、PNG 下载、PDF 下载（深色主题保留）
- 语义化配色：前端青色、后端绿色、数据库紫色、云服务琥珀色、安全玫瑰色
- 安装：下载 zip -> claude.ai Customize -> Skills 上传；需开启 Code Execution；Claude Code 用户可解压到 ~/.claude/skills/
- 姐妹 Skill：process-flow-diagram-generator（流程图/审批流/流水线），设计语言一致
- 对比 draw.io：描述代替拖拽、聊天改图、单文件分发、免安装
- **GitHub Star**：6.3k+（截至 2026-07，苏三文章补充）
- **安装（Claude Desktop）**：下载 zip → 自定义 → 技能 → 上传技能
- **调用方式**：`/architecture-diagram` 命令触发
- **姐妹 Skill (流程画)**：[[ProcessFlowDiagramGenerator]]（process-flow-diagram-generator），专用于流程图/审批流/流水线，GitHub：https://github.com/Cocoon-AI/process-flow-diagram-generator

## 关联连接

- [[ArchitectureDiagramGenerator]] - 核心实体
- [[CocoonAI]] - 开发团队
- [[小锋]] - 文章作者（第一篇）
- [[苏三]] - 文章作者（第二篇）
- [[draw-io]] - 对比对象
- [[文本绘图]] - 所属方法论
- [[Skill]] - 技能扩展机制
- [[ClaudeCode]] - 兼容工具
- [[ProcessFlowDiagramGenerator]] - 姐妹 Skill
- [[摘要-程序员AI画图技巧]] - 相关画图技巧
