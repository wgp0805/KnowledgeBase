---
title: "摘要-magpie替代cc-switch"
type: source
tags: [来源, 原始文件, AI网关, 模型路由, magpie]
sources: [raw/09-archive/替代 CC Switch，这个项目已经斩获 20K Star！.md]
last_updated: 2026-10-27
---

## 核心摘要

程序汪（2026-10-27）的使用复盘：因 CC Switch 切换供应商时整份写回旧快照，导致 `~/.claude/settings.json` 丢失 hooks（13 个）、状态栏配置、`enabledPlugins`/`extraKnownMarketplaces` 清空、`permissions.deny` 拒绝规则被删（3.16.5 起补了保护，但只对开启通用配置的供应商生效），转向本地 AI 网关 magpie（20K Star）。magpie 在本机起一个 `127.0.0.1:3425` 网关，在 OpenAI Chat Completions/Responses、Anthropic Messages、Google Gemini 三类 API 格式间互转；给 Claude Code 的 opus/sonnet/haiku/fable 四档各留下拉框；多家供应商同名模型自动组成路由组（`auto/<模型ID>`），按额度与重置时间智能排序账号（智能/按顺序/轮流/最少使用/重置前用完五种策略），被限流可选保持原位或排到最后，欠费歇半小时、厂商限流按 Retry-After 跳过、报错退避越错越久；配合会话保持四档（自动/整个会话/一轮之内/关闭）避免丢 prompt 缓存优势；还支持按 token 长度/是否带图/是否 reasoning/Agent 来源/时段/星期/文件夹条件分流、图模型代答与搜索代搜、死循环打断（检测到思考或正文反复打转就结束该条回复并交回可重试错误）、意图路由（判断模型分流）。写入极小心：每次写入前先读原文件，只更新接入所需字段，注释/键序/缩进全保留，原子落盘；`applied.json` 记录改了什么、`stash.json` 保留接入前原值，可界面"断开并还原"或 `magpie <agent> default` 一键还原。结论：CC Switch 4.0 已修复写回问题并增加模型聚合；多供应商、多账号、重额度场景 magpie 的自动路由更合习惯。

## 关联连接

- [[Magpie]] — 核心实体
- [[CCSwitch]] — 对比对象（3.16.5 写回缺陷与 4.0 字段级修复）
- [[LLM网关]] — magpie 所属的"统一模型调用中间层"概念（个人/客户端侧网关）
- [[AI网关]] — 团队侧同类基建（1Panel AI 网关）
- [[会话保持]] — 路由选择保持时长的核心机制（本篇提炼概念）
- [[意图路由]] — magpie 用判断模型做的意图分流（增量并入该概念页）
- [[ClaudeCode]] — 被接入的 Agent（settings.json 写回事故主角）
- [[Codex]] — 被接入的 Agent（config.toml 增 model_providers 表）
- [[OpenCode]] — 自动路由组里出现的一个上游来源（OpenCode Go）
- [[DeepSeek]] — 唯一未开通用配置保护而被写回旧快照的供应商
- [[Ollama]] / [[LM_Studio]] — 可充当意图判断的本地模型
- [[程序汪]] — 来源作者
