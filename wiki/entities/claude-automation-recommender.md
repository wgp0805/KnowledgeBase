---
title: "claude-automation-recommender"
type: entity
tags: [Skill, Anthropic, ClaudeCode, 自动化推荐]
sources: [raw/01-articles/Claude 又开源了一款新插件，让你的 Claude Code 满血复活！.md]
last_updated: 2026-06-24
---

## 定义
**claude-automation-recommender** 是 [[Anthropic]] 在 [[claude-code-setup]] 插件背后实际驱动配置推荐工作的 [[Skill]]，负责扫描项目代码并产出针对性的自动化能力配置清单。

## 关键信息

### 角色定位
- 属于 [[Skill]] 而非独立插件，被 [[claude-code-setup]] 这个插件外壳调用
- 是 [[ClaudeCode]] 用 Skill 来打包"项目分析+推荐能力"的官方范例

### 核心行为
- **扫描分析**：识别项目类型（前端/后端等）、技术栈、目录结构
- **差异化建议**：每类能力（MCP/Skill/Hook/Subagent/Slash Command）只挑最值得上的一两个，避免选项过载
- **只读约束**：绝不修改用户的任何文件，仅产出推荐清单

### 设计意义
体现了 [[渐进式披露]] 与"约束式建议"原则——不直接配置而是先呈现清单等待用户确认，符合 [[ClaudeCode]] 高级能力配置的安全实践。

## 关联连接
- [[摘要-claude-code-setup-plugin]] — 来源
- [[claude-code-setup]] — 调用它的插件
- [[Skill]] — 所属概念
- [[ClaudeCode]] — 运行环境
- [[Anthropic]] — 发布方
- [[渐进式披露]] — 设计哲学呼应
