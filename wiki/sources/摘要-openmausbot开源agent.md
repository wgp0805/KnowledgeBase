---
title: "摘要-openmausbot开源agent"
type: source
tags: [来源, 原始文件, OpenMausBot, PersonalAgent, 开源, 桌面应用]
sources: [raw/09-archive/2026-11-09 - 单日暴涨 1500 Star，又一神级开源 Agent 彻底火了！.md]
last_updated: 2026-11-10
---

## 核心摘要

程序员追风（2026-11-09）介绍单日暴涨约 1500 Star 的开源桌面 Agent **OpenMausBot**（milind-soni/OpenMausBot）：定位是 [[GrokBot]] 的开源替代——Grok Bot（xAI）之外还有 Meta Muse、OpenAI Dots、Manus Cue，共同点是闭源、模型/电脑/数据全在厂商侧；OpenMausBot 把这套东西搬回用户自己的电脑，代码开源、数据尽量留在本地。

**核心形态**：桌面软件长得像聊天软件，左边联系人列表里每个"联系人"都是一个真干活的 AI agent，发一句话就去做事，关键处停下来先问同不同意。**不自带模型**，靠本机已装好的命令行工具跑（Claude Code / Codex / Grok CLI 均可），不找你要 API key、不用注册新账号，用的就是现有登录和订阅；也支持 OpenAI 兼容接口（DeepSeek、OpenRouter 等）。

**关键功能**：
1. **每个 bot 单独选模型**：选择器里 Claude/Codex 模型并排，默认有标注、不可用灰掉并说明原因；聊到一半可换模型不用重开会话（写代码用 Codex、整理资料用 Claude）
2. **每个 bot 配一台电脑**：云端 Linux 桌面 / 隔离本地虚拟机 / 本机三选一；**用本机默认关闭**，macOS 与 Ubuntu Xorg 需明确同意才开，Wayland 直接禁用；Computer 面板可看实时画面、浏览器可接管；云端电脑用 Boat 服务（试用期后收费）
3. **干活之前先问**：跑命令/改文件先在聊天里弹审批卡片（允许/拒绝，不点不动），云端与本机都走这一步
4. **连外部应用**：内置应用市场走 [[Composio]]，Gmail/Slack/GitHub/Notion/Linear 等 500+ 应用，授权一次所有 bot 可用（Gmail 每 15 分钟轮询，Slack/GitHub 实时推送）
5. **定时任务与 webhook**：一句话建定时任务（如"每个工作日九点汇总收件箱"）并出管理卡片；Triggers 页面统一列出、带日历与执行记录；**webhook 默认只监听 127.0.0.1**，暴露公网需自己配反代
6. **语音**：每条回复可朗读；可直接打电话，边干活边口头汇报进度并口头请求审批；语音可选 ElevenLabs / Fish Audio / Grok 语音 / Mac 自带（无需云端 key）/ 本地 Chatterbox
7. **打包团队**：调好的整套 bot 团队可存成一个 **Markdown 文件**发给别人导入——不带密钥、不带聊天记录、不带权限，导入后定时任务暂停、应用连接关闭，需自行逐个开启

**安装**：GitHub Releases 安装包（Mac dmg 已签名公证；Windows exe 无需管理员但未签名，SmartScreen 提示"未知发布者"；Ubuntu 24.04 deb/AppImage 仍是 beta、官方仅支持 GNOME）；源码需 Node 24+ 与 pnpm（`pnpm dev:server` 8799 + `pnpm dev` 5199 + `pnpm dev:desktop`）；或 `npm install -g openmausbot` / `npx openmausbot` 一键跑。**前提：本机需先安装并登录至少一个 agent CLI**。

**作者评价**：最认可这个形态——把每个 bot 做成通讯录联系人，各管各的会话与记忆，派任务像回消息；安装后自动并入本地已配置的 AI，省二次配置；Codex 已有 Skill 可直接用，集成邮箱/看板/数据库，订阅的模型基本都能用且可互相协作，还有账单与 App。

## 关联连接
- [[OpenMausBot]] — 本文主角实体
- [[GrokBot]] — 开源替代的对象
- [[Composio]] — 内置应用市场（500+ 应用授权）
- [[ClaudeCode]] — 可调用的本机 CLI 之一
- [[Codex]] — 可调用的本机 CLI 之一
- [[DeepSeek]] — OpenAI 兼容接口接入
- [[OpenRouter]] — OpenAI 兼容接口接入
- [[personal-ai-agent]] — 所属赛道（开源平替序列）
- [[OpenBot]] — 同类多 CLI 桌面应用（调度视角 vs 通讯录视角）
- [[HITL]] — 干活前审批卡的机制归属
- [[Skill]] — 复用本机 Codex 的 Skill
