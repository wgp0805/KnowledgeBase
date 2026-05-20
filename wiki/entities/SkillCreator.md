---
title: "SkillCreator"
type: entity
tags: [Claude Code, Anthropic, 元技能, 工具]
sources: [raw/02-papers/skill-creator使用与优化指南.pdf]
last_updated: 2026-05-20
---

## 定义
skill-creator 是 Anthropic 为 Claude Code 官方提供的 Meta-Skill（元技能工具），专门用于通过自然语言对话自动化创建、优化和测试 AI 技能。

## 关键信息

### 核心价值
- **减少手动编码**：通过对话式交互生成技能文件
- **自动化工作流**：覆盖"需求分析→规则编写→频率控制"全流程
- **测试优化一体化**：自动生成技能后附带测试和优化能力

### 主要功能
1. **创建新技能**：通过自然语言描述技能目标，自动生成 SKILL.md 及配套文件
2. **优化现有技能**：支持边界逻辑优化（异常处理）、触发精准度优化（Description 完善）
3. **基准测试**：支持 A/B 测试对比新旧版本效果

### 安装方式
```bash
# 方式一：通过插件市场安装
/plugin marketplace add anthropics/skills

# 方式二：手动安装
# 从 GitHub https://github.com/anthropic/skills 仓库下载
# 将 /skills/skill-creator/ 目录复制到 ~/.claude/skills/
```

### 使用流程
1. 加载 skill-creator 技能
2. 描述技能目标："使用 skill-creator 帮我创建一个新技能，目的是：..."
3. AI 分析需求后生成技能文件
4. 可进入优化模式进行迭代

### 优化模式
- **边界逻辑优化**：处理异常场景和边缘情况
- **触发精准度优化**：优化 Description 字段，包含 20+ 查询示例
- **A/B 基准测试**：对比新旧版本效果

### 应用场景
- 自动生成 Git 提交规范/代码审查标准
- 团队规范统一和自动化执行
- 标准格式 API 文档生成
- 业务报告自动生成（Excel）
- PDF/Word 结构化信息提取
- 公司 SOP 生成和员工入职文档

## 关联连接
- [[ClaudeCode]] — 所属平台
- [[Meta-Skill]] — 元技能概念
- [[Skill]] — 技能体系
- [[摘要-skill-creator-guide]] — 来源摘要
