---
title: "Skill描述预算"
type: concept
tags: [概念, ClaudeCode, Skill, 性能]
sources: [raw/09-archive/2026-09-28-Claude Code 装了一堆 Skill，用了三个月，我删掉了 80% - 码哥字节.md]
last_updated: 2026-09-29
---

## 定义
[[ClaudeCode]] 加载 Skill 机制的隐性成本：客户端会把**所有** Skill 的名称+描述预先加载进上下文，供模型判断何时触发。该预算默认为模型 context window 的 **1%**，每个描述最长 **1536 字符**——10 个 Skill 约占 15K tokens。安装过多 Skill 会挤爆预算，导致描述被截断，**被截断的 Skill 触发失效（等于白装）**。

## 关键信息
- **症状**：会话打开变慢、上下文被描述吃掉、`/skills` 列表冗长难找、`/doctor` 报告描述截断（如装 32 个时 17 个被截断）
- **根因**：预加载机制是触发判断的前提，与 Skill 正文大小无关——正文是按需加载（[[渐进式披露]]），描述是常驻加载
- **解法**（按优先级）：
  1. 删低频 Skill，保留 10-15 个核心（优于调大预算）
  2. 调大 `skillListingBudgetFraction`（治标，挤压其他上下文）
  3. 压缩描述：短句写清"何时用+做什么"，关键词中英文匹配（描述只有英文关键词，中文描述/中文提示词不匹配同样导致触发失效）
- **触发失效的另外两个原因**：描述关键词中英文不匹配（可手动 `/skill-name` 或改 description）、同名冲突（Enterprise > Personal > Project 优先级，覆盖而非叠加）
- **与 CLAUDEmd 分工**：规范/约定放 [[CLAUDEmd]]（每次会话都加载），流程/技能放 Skill（按需加载）——但描述部分永远预加载

## 关联连接
- [[摘要-claude-code-skill删80%精选]] — 来源
- [[Skill]] — 被预算约束的机制
- [[ClaudeCode]] — 机制宿主
- [[antigravity-awesome-skills]] — 触发该问题的典型仓库
- [[渐进式披露]] — Skill 正文的加载原则（对照：描述是预加载的）
- [[CLAUDEmd]] — 与 Skill 的分工对照
