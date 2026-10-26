---
title: "摘要-claude-code-skill删80%精选"
type: source
tags: [来源, ClaudeCode, Skill, 码哥字节, 选型]
sources: [raw/09-archive/2026-09-28-Claude Code 装了一堆 Skill，用了三个月，我删掉了 80% - 码哥字节.md]
last_updated: 2026-09-29
---

## 核心摘要

[[码哥字节]]（博客园，2026-09-28）复盘：曾被 [[antigravity-awesome-skills]]（37K star、1400+ Skills）"装完满级"的宣传吸引，一口气装 30 多个 Skill，两周后 Claude Code 打开巨慢、上下文预算被描述撑爆、`/skills` 列表找不到东西——删掉 80%，留下 10 个高频 Skill。

**最大坑：Skill 描述预算被打爆**（详见 [[Skill描述预算]]）：Claude Code 把所有 Skill 名称+描述加载进上下文，预算默认为模型 context window 的 1%（每个描述最长 1536 字符，10 个约 15K tokens）。装 32 个时 `/doctor` 显示 17 个描述被截断——**这些 Skill 等于白装（触发失效）**。解法：删低频 Skill 保留 10-15 个核心（优于调大 `skillListingBudgetFraction`）。

**留下的 10 个精选（三组）**：
- 每天用：superpowers（brainstorming + systematic-debugging 减少 40% 返工）、simplify（官方自带，直接改而非只指出问题）、go-coverage-improvement（覆盖率 52%→78%）
- 按需用：tech-hv-research（选型调研 15 分钟出简报）、claude-api（prompt caching 省 60% API 成本）、web-design-guidelines（Vercel，22K star）
- 后台跑：security-review（抓到越权漏洞）、fewer-permission-prompts（高频只读命令进白名单）、init（自动生成 CLAUDE.md，自带）、update-config（管理 settings.json）

**三大仓库选型**：antigravity（数量最多但 AI 批量生成质量参差，探索用）> VoltAgent/awesome-agent-skills（官方团队维护、真实验证，前后端都做的人）；alirezarezvani/claude-skills（分类细、后端专项弱）。后端工程师建议：**Anthropic 官方 skills + Superpowers + 按需从 antigravity 精选 2-3 个，不要无脑全装**。

**触发失效排查三因**：描述预算挤占（`/doctor`）、描述关键词中英文不匹配（手动 `/brainstorming` 或改 description）、同名冲突（Enterprise > Personal > Project 优先级，覆盖而非叠加）。**Skill vs CLAUDE.md**：规范放 CLAUDE.md（每次加载），流程放 Skill（按需加载）。SKILL.md 格式已成跨平台开放标准（Claude Code/Cursor/Gemini CLI/Codex CLI 通用），`npx skills` CLI 一键安装。

## 关联连接
- [[码哥字节]] — 文章作者
- [[ClaudeCode]] — Skill 机制宿主
- [[Skill]] — 核心机制
- [[Skill描述预算]] — 该文提炼的核心概念
- [[antigravity-awesome-skills]] — 该文提炼的核心实体（37K star 生态仓库）
- [[Superpowers]] — 精选清单第一位
- [[摘要-claude-code-skill-7大反模式]] — 同作者前作（Skill 反模式）
- [[CLAUDEmd]] — 与 Skill 的分工对照
- [[渐进式披露]] — Skill 内容组织原则
