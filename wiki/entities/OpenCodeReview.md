---
title: "OpenCodeReview"
type: entity
tags: [阿里, 代码审查, Agent, 开源项目]
sources: [raw/01-articles/2026-09-05 - 阿里开源了一个神级Agent项目.md, raw/01-articles/2026-10-08-阿里开源了个神器，给WorkBuddy、豆包挑毛病.md]
last_updated: 2026-10-09
---

## 定义
Open Code Review 是阿里巴巴开源的 AI 代码审查 Agent，源自内部官方 AI 代码审查助手，采用"确定性工程 + LLM Agent"混合架构。

## 关键信息
- 来源：阿里巴巴集团内部，服务数万开发者，识别数百万代码缺陷
- 架构：确定性工程（文件选择/分束/规则匹配/位置定位）+ LLM Agent（动态决策/上下文检索/深度审查）
- 性能：相同模型下精度反超 Claude Code，token 消耗约1/9
- 速度：中等规模 PR 1-3 分钟
- 内置规则：NPE、SQL注入、XSS、线程安全、参数校验、Mapper SQL
- 协议：Apache-2.0
- 安装：`npm install -g @alibaba-group/open-code-review`
- **Vibe Coding 验收闭环（2026-10-08，详见 [[摘要-opencodereview-workbuddy代码体检]]）**：WorkBuddy 开发 → Open Code Review 检查 → WorkBuddy 修复 → 再次检查；扫描命令 `ocr scan`，先用 `ocr scan --preview` 预览范围再真扫，避免把敏感内容交给模型；可让开发 Agent 用普通人语言解读报告并修复
- **Delegation Mode（委托模式）**：把部分审查工作交给 AI 编程工具自身的模型执行，官方明确提到 Qoder、Cursor、Claude Code、Codex——不一定需单独配审查模型，但不等同于完整独立审查能力
- **产品判断**：AI Coding 下一个机会在"验收"（代码审查、自动测试、安全检测、业务逻辑验收）；多 AI 互相检查可能有共同盲区，支付/隐私/真实资金场景仍需专业测试

## 关联连接
- [[摘要-阿里开源open-code-review]] — 来源
- [[摘要-opencodereview-workbuddy代码体检]] — 来源（验收闭环与委托模式）
- [[阿里巴巴]] — 开源公司
- [[代码审查]] — Code Review
- [[确定性工程]] — 工程保证确定性
- [[ClaudeCode]] — 对比基准
- [[Apache-2.0协议]] — 开源协议
