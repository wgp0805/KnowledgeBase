---
title: "claude-code-setup"
type: entity
tags: [Anthropic, ClaudeCode, 插件, 项目配置工具]
sources: [raw/01-articles/Claude 又开源了一款新插件，让你的 Claude Code 满血复活！.md]
last_updated: 2026-06-24
---

## 定义
**claude-code-setup** 是 [[Anthropic]] 官方开源的 [[ClaudeCode]] 项目级一键配置工具型插件，专门帮用户在 Claude Code 上把自动化能力栈（MCP / Skill / Hook / Subagent / Slash Command）针对性地配置起来。

## 关键信息

### 解决的问题
大多数用户只把 Claude Code 当成"聊天框"，不知道也懒得配置其完整自动化能力，导致一身本事被闲置。该插件用扫描+推荐机制，让新手十分钟可上手、老手用来查漏补缺。

### 工作机制
- **背后由 [[claude-automation-recommender]] Skill 驱动**：扫描项目代码 → 根据项目类型有针对性地推荐配置
- **全程只读**：只分析、只建议，绝不修改任何文件，确认后用户自己再让它动手配置
- **按项目类型差异化推荐**：前端项目推荐前端测试/设计，后端项目推荐后端开发/安全相关能力

### 推荐的五大核心能力
- **MCP Servers**：外部能力接入（如 context7、Playwright）
- **Skills**：打包好的专业技能（如 Plan 规划、前端设计）
- **Hooks**：自动触发的动作（如保存时格式化、自动 lint、敏感文件拦截）
- **Subagents**：专职审查子代理（安全、性能、无障碍）
- **Slash Commands**：一键工作流（如 `/test`、`/pr-review`、`/explain`）

### 安装方式
- CLI：`/plugin install claude-code-setup@claude-plugins-official`
- 桌面版：Code 面板 → Customize → Personal plugins → Browse plugins 搜索安装
- 隶属于 [[claude-plugins-official]] 官方插件商店

### 使用方式
完全自然语言交互，无需记复杂指令：
- "帮我 set up claude code"
- "帮我看看这个项目该配哪些自动化"
- "我该用哪些 hooks？"

它输出一份按 项目文档 / MCP / Hooks / Skills / Subagents 分类的推荐清单。

## 关联连接
- [[摘要-claude-code-setup-plugin]] — 来源
- [[ClaudeCode]] — 配置的目标产品
- [[Anthropic]] — 发布方
- [[claude-automation-recommender]] — 底层驱动 Skill
- [[claude-plugins-official]] — 所属插件市场
- [[Skill]] — 推荐的能力之一
- [[MCP]] — 推荐的能力之一
- [[Hooks]] — 推荐的能力之一
- [[Agent]] — 推荐的能力之一（Subagent）
