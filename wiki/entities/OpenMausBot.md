---
title: "OpenMausBot"
type: entity
tags: [开源项目, PersonalAgent, 桌面应用, Agent客户端, GrokBot平替]
sources: [raw/09-archive/2026-11-09 - 单日暴涨 1500 Star，又一神级开源 Agent 彻底火了！.md]
last_updated: 2026-11-10
---

## 定义

OpenMausBot 是开源桌面 Agent 客户端（GitHub `milind-soni/OpenMausBot`，2026-11-09 单日涨约 1500 Star），定位为 [[GrokBot]] 的开源替代：把"通讯录式多 Agent"从厂商云端搬回用户本机——代码开源、数据尽量留在本地、不自带模型。

## 关键信息

### 基本形态

- 打开像聊天软件：左侧联系人列表，每个"联系人"是一个会真干活的 AI agent
- 发一句话它就去执行，关键处停下来先征求同意
- **不自带模型**：调用本机已登录的 CLI（Claude Code / Codex / Grok CLI），不额外要 API key、不用注册新账号，复用现有订阅；也支持 OpenAI 兼容接口（DeepSeek / OpenRouter）
- 前提：本机需已安装并登录至少一个 agent CLI

### 功能矩阵

| 功能 | 说明 |
|------|------|
| 每 bot 独立选模型 | Claude/Codex 模型并排可选，默认标注、不可用灰掉并说明原因；会话中可换模型 |
| 每 bot 一台电脑 | 云端 Linux 桌面 / 隔离本地 VM / 本机三选一；**本机默认关闭**（macOS、Ubuntu Xorg 需明确同意；Wayland 禁用）；Computer 面板可看实时画面、浏览器可接管；云端用 Boat 服务（试用后收费） |
| 执行前审批 | 跑命令/改文件先弹审批卡片，允许或拒绝，不点不动；云端与本机一致 |
| 应用市场 | 走 [[Composio]]，500+ 应用（Gmail/Slack/GitHub/Notion/Linear），一次授权全 bot 可用（Gmail 15 分钟轮询，Slack/GitHub 实时） |
| 定时任务与 webhook | 自然语言建任务并出管理卡片；Triggers 页带日历与执行记录；**webhook 默认只监听 127.0.0.1**，公网需自配反代 |
| 语音 | 回复可朗读；可打电话边干活边汇报并口头审批；ElevenLabs / Fish Audio / Grok 语音 / Mac 自带 / 本地 Chatterbox |
| 团队打包 | 整套 bot 团队存为 Markdown 文件导入导出——不带密钥/聊天记录/权限，导入后定时任务暂停、应用连接关闭 |

### 安装

- 安装包：Mac dmg（已签名公证）、Windows exe（无需管理员、未签名，SmartScreen 需手动放行）、Ubuntu 24.04 deb/AppImage（beta，仅 GNOME）
- 源码：Node 24+ + pnpm（`pnpm dev:server` 8799 / `pnpm dev` 5199 / `pnpm dev:desktop`）
- 一键：`npm install -g openmausbot` 或 `npx openmausbot`

### 与同类工具的关系

- **[[GrokBot]]**：闭源原型（云端多 Bot、共用一台云电脑、含付费 Cursor 计划）——OpenMausBot 是它的开源平替
- **[[OpenBot]]**：同为"多 CLI 桌面应用"，但 OpenBot 强调"一个窗口调度多 agent + 频道协作"，OpenMausBot 强调"通讯录式联系人 + 每 bot 独立电脑 + 审批卡"
- **[[Rakazo]]**：同批开源平替（对 Grok Bot 的另一实现）
- 同赛道还有 Meta Muse、OpenAI Dots、Manus Cue（均闭源）

## 关联连接
- [[摘要-openmausbot开源agent]] — 来源
- [[GrokBot]] — 开源替代对象
- [[OpenBot]] — 同类多 CLI 桌面应用
- [[Rakazo]] — 同批开源平替
- [[Composio]] — 应用市场底座
- [[ClaudeCode]] — 可调用 CLI
- [[Codex]] — 可调用 CLI
- [[DeepSeek]] — OpenAI 兼容接口
- [[OpenRouter]] — OpenAI 兼容接口
- [[personal-ai-agent]] — 所属赛道
- [[HITL]] — 执行前审批机制
