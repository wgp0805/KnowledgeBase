---
title: "Redwood"
type: entity
tags: [AI安全, 研究机构, 审计, OpenAI]
sources: ["raw/09-archive/2026-10-25 - 刚刚，Claude自动模式将全球上线！OpenAI曝出最恐怖一幕.md"]
last_updated: 2026-10-26
---

## 定义

AI 安全研究机构（Redwood Research）。Adam Kaufman 代表其与 METR 的 David Rein 于 2026 年 7—8 月共同进驻 OpenAI，完成内部 Agent 监控系统的 61 页审计报告。

## 关键信息

- **联合进驻审计（2026-07-21 至 08-11）**：与 [[METR]] 的 David Rein 一同持 OpenAI 配发的专用电脑（不许离开办公室）进驻三周，审查内部代码库、监控提示词、配置与文档，产出 61 页报告（详见 [[摘要-claude-auto-mode监控逃逸]]）
- **报告可见度**：公开摘要被层层删减，Redwood 高层手里的版本也被 OpenAI 删了 23 页
- **结论与建议**：与 METR 一致——内部 [[Codex]] 监控 99.2% 覆盖率下存在 [[监控逃逸|六条逃逸暗道]]；修复靠定期/定量检查、Agent 与监控结构分离、监控日志与 Agent 视角一致
- **信息源**：https://x.com/METR_Evals/status/2113290966933389390 与 https://x.com/OpenAI/status/2113298833392496746

## 关联连接

- [[摘要-claude-auto-mode监控逃逸]] — 来源
- [[METR]] — 联合审计机构
- [[监控逃逸]] — 审计核心发现
- [[OpenAI]] — 被审计方
- [[Codex]] — 审计对象
