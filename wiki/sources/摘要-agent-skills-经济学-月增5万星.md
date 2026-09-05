---
title: "摘要-agent-skills-经济学-月增5万星"
type: source
tags: [来源, Agent Skills, GitHub, 经济学, 团队资产]
sources: [raw/01-articles/2026-08-24-GitHub上一个”技能包”月增5万星：Agent Skills正在抢走程序员的饭碗.md]
last_updated: 2026-08-25
---

## 核心摘要
前进ing 拆解 Agent Skills 在 2026 年 8 月 GitHub 集体爆发的现象。mattpocock/skills 单月增星 50,486，obra/superpowers 总星 27.49 万，Skills 类项目正在吃掉原本属于「大模型新版本」「Agent 框架」的榜单位置。核心经济学判断：**模型能力是租的（按 token 付费），技能是自己的（一次编写处处复用）**。SKILL.md 本质是 Agent 的「函数签名」，告诉 Agent 触发条件、做什么、遵守什么边界。文章给出三大踩坑点（选择困难症、质量参差、安全边界）和消费者/创作者/团队负责人三条上手路径，强调「2026 年下半年开始我们沉淀技能，技能库是带不走的资产」。

## 关键信息
- **爆发数据**：
  - obra/superpowers：总星 27.49 万，单日新增 749
  - JuliusBrussee/caveman：总星 9.95 万，单日新增 309
  - mattpocock/skills：单月增星 50,486
  - Anthropic 官方 skills 仓库：约 17 万星
  - Anthropic-Cybersecurity-Skills：817 个安全技能，映射 MITRE ATT&CK 等 6 大安全框架
- **Skills 经济学**：模型按 token 付费是水电费；技能一次编写处处复用是资产
- **SKILL.md 结构**：SKILL.md（技能声明）+ scripts/（可执行脚本）+ references/（参考文档按需加载）
- **SKILL.md 三件事**：触发条件、指令正文、边界
- **三大踩坑**：
  1. 选择困难症：装 30 个不如精挑 5 个（i-have-adhd 项目 1.5 万星反向证明）
  2. 质量参差：技能本质是「指令+脚本」能执行任意代码
  3. 安全边界：Anthropic 官方仓库要求自动化安全扫描，但 GitHub 随便一个 SKILL.md 都可能执行恶意脚本
- **消费者路径**：程序员（mattpocock/skills、obra/superpowers、Karpathy Skills）；产品运营（Addy Osmani agent-skills、caveman）；安全测试（Anthropic-Cybersecurity-Skills）
- **团队负责人路径**：建内部 skills 仓，统一代码规范/测试标准/提交格式/部署流程/内容审核，所有人从同一份来源拉
- **时代判断**：2024 写提示词 → 2025 调模型 → 2026 下半年沉淀技能

## 关联连接
- [[AgentSkills]] — Agent 技能生态
- [[Superpowers]] — Jesse Vincent 的 AI 编程 Skill 框架
- [[SkillCreator]] — Claude Code 元技能创建工具
- [[Anthropic]] — 官方 skills 仓库与安全扫描规则制定者
- [[mattpocock-skills]] — JS/TS 圈 5 万星技能包
