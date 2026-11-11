---
title: "Paperclip"
type: entity
tags: [开源项目, 多智能体, Agent编排, AI一人公司]
sources: [raw/09-archive/2026-10-29 - 开源项目｜100k+ Star！GitHub爆火的多智能体神器，一条命令搭起AI一人公司.md, raw/09-archive/2026-10-30 - 10万+Star！GitHub爆火的多智能体神器！.md, raw/09-archive/开源项目｜100k+Star！GitHub爆火的多智能体神器，一条命令搭起AI一人公司.md]
last_updated: 2026-11-11
---

## 定义

Paperclip 是一个开源多智能体编排项目（GitHub `paperclipai/paperclip`，10万+ Star，Node.js 服务端 + React 前端，MIT 协议，2026-03 开源）。定位：「**OpenClaw 是员工，Paperclip 是公司**」——它不做代理，做编排层，为多个 AI Agent 安排岗位、划定汇报线、分配预算、跟踪进度。

## 关键信息

### 公司组织架构模式

- 可接入类型：Claude Code、Codex、Cursor、Gemini CLI、bash 脚本、OpenClaw、自写 HTTP 机器人
- 每个代理配置：角色、职称、汇报关系、预算；官方适配器写好后「填空入职」
- 比喻：Claude Code 当 CTO、Codex 当工程师、Cursor 当设计师
- **「只要能接收心跳，就能入职」**

### 核心机制

| 机制 | 说明 |
|------|------|
| 任务绑定 | 任务与公司目标、项目目标、具体工单绑定，代理清楚「为什么做」 |
| 心跳唤醒 | 按时间表定时唤醒代理、检查状态、结果向上汇报；面板可追溯拆解层级 |
| 预算刹车 | 每月预算花到上限自动停止，防代理陷入循环烧光额度 |
| 审批控制 | 雇佣/暂停/终止代理需审批；操作留审计日志，配置变更带版本控制可回滚 |
| 依赖关系 | 任务间有依赖，阻塞项没解决下游不启动 |
| 上下文上流 | 上下文从任务流到项目和公司目标 |
| 多租户 | 一个实例跑多个公司，数据互相隔离，手机可监控 |

### 安装

```bash
npx paperclipai onboard --yes                # 本地回环，最快
npx paperclipai onboard --yes --bind lan     # 局域网
npx paperclipai onboard --yes --bind tailnet # Tailscale
npx --registry https://registry.npmjs.org paperclipai onboard --yes  # 私有 registry 报错时强制公共源
```

- API 服务跑在 3100 端口，嵌入式 PostgreSQL 自动创建
- 前置要求：Node.js 20+、pnpm 9.15+
- 开源、自托管、无需注册账号，链路全在本机

### 首次使用

1. 新手引导页 → 新建公司（公司名即隔离单位，代理/工单/预算挂其下）
2. 添加员工：第一个自动成为 CEO（建议用最强的模型）
3. 选适配器 → 配置心跳间隔 → 创建代理
4. 代理详情页「测试环境」确认配置通了再派活

### 现状评价

- 生态仍在生长、社区推插件、Star 还在涨
- 开源才半年多，issue 区堆着六千多个未关闭问题
- 更适合爱折腾、能接受边用边修的人；装上就零维护的团队工具还需等待

## 关联连接
- [[摘要-paperclip-多智能体公司]] — 早期来源
- [[摘要-paperclip-多智能体神器]] — 最新来源
- [[多智能体编排]] — 上位概念（公司组织架构 vs AgentScope 主控模式对照）
- [[OpenClaw]] — 被编排的「员工」之一
- [[ClaudeCode]] — 可接入代理（CTO 位）
- [[Codex]] — 可接入代理（工程师位）
- [[Cursor]] — 可接入代理（设计师位）
- [[超级个体]] — "AI 一人公司"关联概念
