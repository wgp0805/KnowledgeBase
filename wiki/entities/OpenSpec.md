---
title: "OpenSpec"
type: entity
tags: [AI编程, 规范驱动, 开源工具]
sources: [raw/01-articles/同事："Claude Code都能自动写代码了，还要什么Spec Coding？" 我反问："屎山代码你来维护？".md]
last_updated: 2026-06-24
---

## 定义

OpenSpec 是一个面向 AI 编程的规范驱动框架，核心思想是"先对齐需求，再写代码"。它通过生成提案、需求规格、技术设计和任务清单等规划文档，经人工确认后再让 AI 实现，让 AI 编程的结果更加符合预期。

## 关键信息

- **GitHub Star**: 53k+
- **核心理念**: 先对齐需求，再写代码
- **中文版**: https://github.com/studyzy/OpenSpec-cn
- **原版**: https://github.com/Fission-AI/OpenSpec

### 核心工作流

1. **探索模式** (`/opsx:explore`): 通过纯对话方式探讨需求，理清需求再动手
2. **提案模式** (`/opsx:propose`): 生成规划制品，包括：
   - proposal.md：变更提案，为什么要做和做什么
   - specs/spec.md：需求规格，用结构化格式描述具体需求和验收场景
   - design.md：技术设计，描述技术实现方案
   - tasks.md：任务清单，列出实现步骤
3. **应用模式** (`/opsx:apply`): 按清单逐项实现，生成实际代码+tasks进度更新
4. **归档模式** (`/opsx:archive`): 完成后归档存档，将规划文档移入archive目录

### 安装与初始化

```bash
# 安装
npm install -g @studyzy/openspec-cn@latest

# 初始化
cd your-project
openspec-cn init --tools opencode

# 查看仪表盘
openspec-cn view
```

## 关联连接

- [[摘要-OpenSpec规范驱动AI编程框架]] — 来源
- [[摘要-superpowers-openspec-speckit对比]] — 三方对比来源
- [[规范驱动开发]] — 上层方法论
- [[Superpowers]] — 兄弟方案，管"怎么干"
- [[SpecKit]] — 兄弟方案，让规范可执行
- [[AICoding]] — AI 辅助编程范式
- [[OpenCode]] — 支持 OpenSpec 的编程工具
- [[Skill]] — 技能扩展机制
- [[ClaudeCode]] — AI 编程工具
