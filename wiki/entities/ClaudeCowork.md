---
title: "ClaudeCowork"
type: entity
tags: [AI产品, Anthropic, PersonalAgent, 本地优先]
sources: [raw/09-archive/2026-10-08-关了电脑还在替你干活：Personal Agent的技术内核与医疗落地.md]
last_updated: 2026-10-09
---

## 定义
Claude Cowork 是 Anthropic 的本地路线 Personal Agent：不跑在云端，而是运行在用户电脑本地的虚拟机里，用户可精确控制它能访问哪个文件夹、哪个应用，数据完全不离开设备，长文档处理能力公认领先，定位"文档处理专家"。

## 关键信息
- **运行方式**：本地虚拟机隔离执行，数据不离开用户设备；可精确限定可访问的文件夹与应用
- **权限设计**：默认零权限，每访问一个应用、每做一个操作都要询问；可开 Auto 模式让安全操作自动放行、危险操作拦截
- **长板**：几百页病历、几十篇论文的整理总结与草稿撰写
- **合规边界**：官方明确不支持 HIPAA、FedRAMP 等监管场景，不要用来处理敏感医疗数据；不能联网对接医院系统、不能跨应用执行复杂工作流
- **产品线动态（2026-09-16，见 [[Claude]]）**：Anthropic 已把独立 Chat 和 Cowork 合并成一个 Claude 在做减法——与本页描述的本地隔离形态是不同产品阶段的两说，引用时需注意时间线

## 关联连接
- [[摘要-personal-agent-技术内核与医疗落地]] — 来源
- [[Claude]] — 所属产品线（含合并动态）
- [[Anthropic]] — 开发公司
- [[personal-ai-agent]] — 所属赛道
- [[本地优先]] — 底层产品哲学
- [[GeminiSpark]] — 同文对比的云端路线竞品
- [[DAXCopilot]] — 同文对比的垂直竞品
