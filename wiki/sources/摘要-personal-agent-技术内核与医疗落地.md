---
title: "摘要-personal-agent-技术内核与医疗落地"
type: source
tags: [来源, PersonalAgent, 医疗, MCP, 权限分级]
sources: [raw/01-articles/2026-10-08-关了电脑还在替你干活：Personal Agent的技术内核与医疗落地.md]
last_updated: 2026-10-09
---

## 核心摘要
文章以医疗为试金石拆解 Personal Agent 的三根技术支柱：① 分层记忆（工作记忆/长期记忆/技能记忆，且必须记忆隔离、删除即清除）；② MCP 协议作为 Agent 世界的"USB 接口"统一对接 HIS/LIS/PACS 等异构系统，且要按场景动态加载工具而非堆插件；③ 权限分级（只读默认允许/低风险可自动/高风险必须确认 + Auto-review 二次拦截），医疗场景还要加一条"谁签字谁负责"——AI 只写草稿不诊断不开处方。对比四款产品：OpenAI Dots（云端沙盒全能实习生，但不支持 HIPAA）、Google Gemini Spark（谷歌生态生活调度员）、Claude Cowork（本地虚拟机文档处理专家）、Nuance DAX Copilot（垂直医疗助理，每次接诊省 5 分钟文书）。行业从"比谁更聪明"转向"比谁更靠谱"，演进四阶段：对话式助手→单点执行→后台常驻 Personal Agent→多 Agent 数字共生；本质让渡的不是决策权而是注意力。

## 关联连接
- [[personal-ai-agent]] — 所讨论的品类
- [[Dots]] — 对比产品一
- [[GeminiSpark]] — 对比产品二
- [[ClaudeCowork]] — 对比产品三
- [[DAXCopilot]] — 对比产品四
- [[MCP协议]] — 三根技术支柱之一
- [[多层记忆]] — 分层记忆系统
- [[最小权限原则]] — 权限分级的底层原则
- [[摘要-agent信任与决策权100条]] — 同日同赛道姊妹篇
