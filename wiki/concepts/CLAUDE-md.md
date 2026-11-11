---
title: "CLAUDE.md"
type: concept
tags: ["Claude-Code", "长期记忆"]
last_updated: 2026-09-01
---

# CLAUDE.md（长期记忆文件）

CLAUDE.md 是 Claude Code 的长期记忆文件，存储在项目根目录，每次启动自动加载。注入项目规范、编码约定、常用命令。最佳实践：分层组织、简洁明确、避免冲突。

## 补充要点（2026-11-10，详见 [[摘要-claude桌面app全攻略]]）

- **生成方式**：`/init` 让 Claude 通读项目自动生成，之后每个新 Session 开工前先读它快速掌握项目
- **长度控制**：建议 **≤200 行**；太长时按模块拆分（如前端/后端各一个文件）+ 主文件留指针
- **更推荐 `AGENTS.md`**：所有 Agent 通用（Codex、WorkBuddy 也能读），CLAUDE.md 通常只有 Claude 自己用
- **全局记忆**：`~/.claude/CLAUDE.md`（Windows 为 `C:\Users\<用户名>\.claude\CLAUDE.md`），对所有项目生效，适合写个人偏好（如"前端技术讲详细点"）
- **隐藏的第二套记忆**：Claude Code 还有按项目隔离、每条一个 Markdown 文件的记忆目录，但很少主动写，多数场景 CLAUDE.md 足够
- **与 Chat/Cowork 隔离**：CLAUDE.md 只对 Code 模式生效；Chat/Cowork 用设置里 Your Claude 的记忆 + Memory 开关，两套完全独立

## 关联连接
[[Claude-Code]], [[长期记忆]], [[沉默王二]], [[摘要-claude桌面app全攻略]], [[NestedSession]]
