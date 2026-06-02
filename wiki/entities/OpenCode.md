---
title: "OpenCode"
type: entity
tags: [AI, 开源, 编码助手, Agent]
sources: [raw/09-archive/ECC使用教程.md]
last_updated: 2026-06-02
---

## 定义
OpenCode 是开源 AI 编程助手，支持事件驱动 Hook 系统和 SubAgent，是 Claude Code 的开源替代方案。相比 Claude Code 在插件系统和钩子事件上更强大。

## 关键信息

### 与 Claude Code 的对比
| 特性 | Claude Code | OpenCode |
|------|------------|----------|
| 钩子事件类型 | 8 种 | 20+ 种 |
| 自定义工具 | 通过 hooks 模拟 | 6 个原生工具 |
| Skill 格式 | SKILL.md | SKILL.md（兼容） |
| 插件 API | 有限 | 更丰富的插件 API |

### 独有优势
- **file.edited** 事件：文件编辑后自动触发（Claude Code 无此事件）
- **lsp.client.diagnostics** 事件：LSP 诊断后触发
- **原生自定义工具**：run-tests、check-coverage、security-audit
- **精细 Skill 权限控制**：按 agent 设置不同的 skill 访问权限

### 安装 ECC
```bash
npm install -g opencode-ecc
# 或
npm install -g ecc-universal  # 通用包
```

### 配置文件
- 项目级：`opencode.json`
- 全局：`~/.config/opencode/opencode.json`
- Agent 定义：`AGENTS.md`
- Agent 引用：`@planner`、`@code-reviewer`

## 关联连接
- [[ECC]] — 增强框架（同时支持 Claude Code 和 OpenCode）
- [[ClaudeCode]] — 对比平台
- [[Agent]] — Agent 核心概念
- [[Hooks]] — 钩子系统（OpenCode 事件更丰富）
- [[Skill]] — 技能扩展机制
- [[摘要-ECC使用教程]] — 来源
