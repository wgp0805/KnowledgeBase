---
title: "SkillCreator"
type: entity
tags: [Claude Code, Anthropic, 元技能, 工具]
sources: [raw/09-archive/skill-creator使用与优化指南.pdf, raw/09-archive/2026-08-24-GitHub上一个”技能包”月增5万星：Agent Skills正在抢走程序员的饭碗.md, raw/09-archive/2026-11-24 - 像高手一样做自己的 Skill！【小白教程】.md]
last_updated: 2026-11-25
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

### 定制个人专属 Skill（2026-11 补充）
来自 [[摘要-做自己的skill小白教程]]：把"在底子上叠加个人标准"的做法用 skill-creator 固化成自己的 Skill——提示词为"在 [[Humanizer]] 基础上，把我们的风格清单和刚才这套做法改进去，存成一个新的 Skill，并且起一个自己的名字，把原作者署名和 MIT 协议留在文件里"。生成后还需两步人工收敛：**砍掉多余内容**（AI 只增不删，但 Skill 越短越有效——删掉 AI 本来就会的、与自己目标无关的英文习惯）与**拆分文件**（SKILL.md 只留主流程和目录，习惯清单/样文/统计进 reference/，脚本进 scripts/）。完整流程见 [[个人Skill定制七步法]]。

## 关联连接
- [[ClaudeCode]] — 所属平台
- [[meta-skill]] — 元技能概念
- [[Skill]] — 技能体系
- [[摘要-skill-creator-guide]] — 来源摘要
- [[AgentSkills]] — 技能生态
- [[mattpocock-skills]] — 通用代码自检技能包
- [[摘要-agent-skills-经济学-月增5万星]] — 来源（Skills 经济学）
- [[个人Skill定制七步法]] — 用 skill-creator 固化个人 Skill 的完整流程
- [[摘要-做自己的skill小白教程]] — 来源
- [[Humanizer]] — 被改造的底子
