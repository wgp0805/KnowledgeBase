---
title: "ArchitectureDiagramGenerator"
type: entity
tags: [AI画图, Skill, 架构图, 开源, HTML]
sources:
  - raw/01-articles/又一个神级画图 Skill 开源，再见 draw.io！.md
  - raw/01-articles/推荐一个神级画图Skill.md
last_updated: 2026-07-20
---

## 定义

Architecture Diagram Generator 是 [[CocoonAI]] 团队开源的 [[Skill|Claude AI Skill]]（MIT 协议），用人话描述系统架构，由 Claude 生成深色主题、排版整齐的自包含 HTML 架构图，支持一键导出 PNG/PDF。属于[[文本绘图|文本绘图]]方法论中"AI 生成 HTML/SVG"路线，主打用对话代替手工拖拽。

## 关键信息

- **GitHub**：https://github.com/Cocoon-AI/architecture-diagram-generator
- **协议**：MIT
- **输出**：自包含 HTML（CSS + SVG 内嵌），无需对方装软件即可查看
- **导出**：Copy（高清 PNG 到剪贴板）、PNG 下载、PDF 下载（深色主题保留）
- **语义化配色**：前端青色、后端绿色、数据库紫色、云服务琥珀色、安全玫瑰色
- **安装**：下载 zip -> claude.ai Customize -> Skills 上传，需开启 Code Execution；Claude Code 用户可解压到 ~/.claude/skills/
- **姐妹 Skill**：process-flow-diagram-generator（流程图/审批流/流水线），设计语言一致
- **对比 [[draw-io]]**：描述代替拖拽、聊天改图、单文件分发、免安装
- **GitHub Star**：6.3k+（截至 2026-07）
- **安装（Claude Desktop）**：下载 zip → 自定义 → 技能 → 上传技能
- **调用方式**：`/architecture-diagram` 命令触发

## 关联连接

- [[CocoonAI]] - 开发团队
- [[文本绘图]] - 所属方法论
- [[draw-io]] - 对比对象
- [[Skill]] - 技能机制
- [[ClaudeCode]] - 兼容工具
- [[SVG]] - 输出格式
- [[ProcessFlowDiagramGenerator]] - 姐妹 Skill（流程图）
- [[苏三]] - 文章作者
- [[摘要-architecture-diagram-generator]] - 来源
