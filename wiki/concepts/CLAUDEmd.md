---
title: "CLAUDEmd"
type: concept
tags: [AI, 记忆, 指令系统]
sources: [raw/01-articles/全网最全！60分钟全面掌握Claude Code~【附完整文档】.md, raw/01-articles/6条Claude Code实践中的经验与思考.md]
last_updated: 2026-05-19
---

## 定义
Claude Code 的核心指令与记忆系统，以 CLAUDE.md 文件为载体，三层叠加生效，确保 Agent 在每次对话时都能获取用户/项目的核心规则。

## 关键信息

### 三层体系
1. **全局级** (`~/.claude/CLAUDE.md`)：对所有项目生效，写个人习惯相关规则
2. **项目级** (项目根目录)：团队共享可提交 Git，写技术架构/文件结构/开发规范
3. **文件夹级** (子文件夹)：仅对该文件夹的修改生效

### 设计原则
- 第一优先级，每次对话自动注入上下文
- 不应塞太多内容，理想情况只写最顶层不变化的原则
- 项目级应是动态的：项目加功能、踩了坑就同步更新
- 用 `/init` 自动扫描项目生成项目级 CLAUDE.md

### Codex 的对应物
Codex 使用 `agents.md` 作为手动持久记忆文件，分全局级和项目级，机制类似。

### 实践经验
- CLAUDE.md 本质是"与 AI 签订的契约"
- 积累的错误经验越多，犯错越少
- 可在 CLAUDE.md 中引用自建参考文档实现渐进式披露

## 关联连接
- [[ClaudeCode]] — CLAUDE.md 所属产品
- [[AutoMemory]] — 第二优先级记忆
- [[Codex]] — 对应 agents.md
- [[AICoding]] — AI 编程实践
