---
title: "AgentSkills"
type: concept
tags: [AI编程, Agent, 扩展机制, 协议]
sources:
  - raw/01-articles/Pi 大道至简，超越Codex和Claude Code的极简Agent，保姆级全攻略， 一文精通.md
  - raw/01-articles/GitHub狂揽8.6万Star！为什么越来越多人用 Pi ？.md
  - raw/01-articles/2026-08-24-GitHub上一个”技能包”月增5万星：Agent Skills正在抢走程序员的饭碗.md
  - raw/01-articles/2026-08-24-Huashu-Excel正式发布！可能、也许、大概是最好用的Excel数据处理和分析skill.md
  - raw/01-articles/2026-08-24-普通人也能用Agent Skills：龙叔的保姆级教程.md
last_updated: 2026-08-25
---

## 定义
Agent Skills 是 AI Agent 的可复用行为模块标准协议，通过将特定领域知识、工作流程、工具使用方法封装为"技能"，让 Agent 按需加载。遵循标准 Skills 协议的技能可在不同 Agent 框架间复用。[[Pi]]、[[ClaudeCode]]、[[DeepSeekHarness]] 均支持该协议。

## 关键信息

### 存放位置
- **项目级**：`项目目录/.agents/skills/`
- **全局级**：`~/.agents/skills/`
- Agent 自动扫描这两个目录加载技能

### 兼容性
- [[Pi]] 自动读取 `~/.agents/skills`，[[ClaudeCode]] 积累无缝迁移
- [[ClaudeCode]] 原生支持 Skills 协议
- [[DeepSeekHarness]] 通过插件支持 Skills
- 可从 SkillHub 检索社区技能

### 典型 Skills
- Playwright CLI 浏览器自动化
- Markdown Converter 文档转换
- TTS 技能（Edge TTS 零成本）
- 各领域定制工作流

### 与插件的区别
- **Skills**：声明式行为模块，描述"怎么做"，Agent 按需调用
- **插件**：命令式扩展，提供新工具和功能
- 两者互补，Skills 偏知识/流程，插件偏工具/能力

### 经济学（2026-08，详见 [[摘要-agent-skills-经济学-月增5万星]]）
- **模型能力是租的**（按 token 付费），**技能是自己的**（一次编写处处复用）
- **mattpocock/skills** 单月增星 50,486，本质是十几年生产环境踩坑打包成通用代码自检技能包
- **不是 model 在变强，是工具箱在变厚**
- 把 skill 当纪律，不当框架

### 普通人构建路径（2026-08，龙叔教程，详见 [[摘要-agent-skills-普通人教程-龙叔]]）
- 三步法：写 SKILL.md → 放对目录 → 用自然语言调用
- 存放位置：项目级 `.claude/skills/`、全局级 `~/.claude/skills/`
- SKILL.md 三要素：name（触发名）、description（触发条件）、内容（指令）
- 普通人也能写：会说话就会写 Skill，自然语言即指令

### 数据分析领域实践（2026-08，花叔 huashu-excel，详见 [[摘要-huashu-excel-skill]]）
- 一套体系化策略激发大模型能力同时避开其数据处理缺陷
- test-time scaling：八步流程强制 agent 多想
- 抗差统计：默认中位数和五数概括
- 压测方法：十份真实公开业务数据独立 agent 实跑 + 复核 agent 重算

## 关联连接
- [[Pi]] — 支持 Skills 协议的 Agent
- [[ClaudeCode]] — 原生支持 Skills
- [[DeepSeekHarness]] — 通过插件支持 Skills
- [[AGENTS-md]] — 配套的项目上下文机制
- [[摘要-pi-agent-保姆级全攻略]] — 来源
- [[摘要-GitHub狂揽8.6万Star-Pi]] — 来源
- [[摘要-agent-skills-经济学-月增5万星]] — 来源（经济学视角）
- [[摘要-agent-skills-普通人教程-龙叔]] — 来源（普通人构建教程）
- [[摘要-huashu-excel-skill]] — 来源（数据分析 Skill 实践）
- [[mattpocock-skills]] — 月增 5 万星的技能包仓库
- [[花叔]] — huashu-excel skill 作者
