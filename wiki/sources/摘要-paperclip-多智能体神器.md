---
title: "摘要-paperclip-多智能体神器"
type: source
tags: [来源, 多智能体, Agent编排, AI一人公司]
sources: [raw/09-archive/2026-10-30 - 10万+Star！GitHub爆火的多智能体神器！.md]
last_updated: 2026-11-02
---

## 核心摘要

「程序员追风」介绍开源项目 Paperclip（GitHub `paperclipai/paperclip`，10万+ Star，Node.js 服务端 + React 前端，MIT 协议，2026 年 3 月开源）。Paperclip 不做代理，而是给 Claude Code、Codex、Cursor、Gemini CLI、bash 脚本、OpenClaw、自写 HTTP 机器人等 Agent 安排岗位、划定汇报线、分配预算、跟踪进度——「OpenClaw 是员工，Paperclip 是公司」。

关键机制：

- **心跳机制**：按时间表定时唤醒代理、检查状态、结果向上汇报；一个目标拆到哪一层、谁负责哪一段，面板上都能追溯
- **预算刹车**：每个代理有月度预算，花到上限自动停止，防止代理陷入循环烧光额度
- **审批与审计**：雇佣、暂停、终止代理都需要审批；所有操作留审计日志，配置变更带版本控制可回滚
- **任务绑定**：任务跟公司目标、项目目标、具体工单绑定，代理清楚自己为什么做这件事
- **依赖关系**：任务之间有依赖，阻塞项没解决下游不启动
- **多租户**：一个实例可跑多个公司，数据互相隔离，手机上也能监控

部署：`npx paperclipai onboard --yes`（默认本地回环），API 服务跑在 3100 端口，嵌入式 PostgreSQL 自动创建。前置要求 Node.js 20+、pnpm 9.15+。

评价：方向对但仍需打磨——开源才半年多，issue 区堆着六千多个未关闭问题，更适合爱折腾、能接受边用边修的人。

## 关联连接
- [[Paperclip]] — 被介绍的实体
- [[摘要-paperclip-多智能体公司]] — 更早的同主题来源
- [[OpenClaw]] — 文中提到的「员工」Agent
- [[ClaudeCode]] / [[Codex]] / [[Cursor]] — 可接入的代理
- [[多智能体编排]] — 上位概念
- [[程序员追风]] — 文章作者
