---
title: "DeepSeek"
type: entity
tags: [AI模型, 大语言模型, 中国公司]
sources: [raw/01-articles/2026-09-03-腾讯内测Cheso，一个专做 PPT 的 AI Agent，实测有吓到我.md, raw/01-articles/2026-09-23-开多个 Agent 后 Claude Code 账单翻了 4 倍，一个配置解决了 - 码哥字节.md]
last_updated: 2026-09-28
---

## 定义
中国AI公司开发的大语言模型，是Cheso集成的多个AI模型之一。

## 关键信息
- **开发公司**：DeepSeek
- **产品类型**：大语言模型
- **集成平台**：Cheso演示文稿生成工具
- **技术定位**：为Cheso提供AI能力支持

### Anthropic 兼容端点与 Claude Code 分层接入（2026-09）
来自 [[摘要-claude-code-多agent账单分层路由]]。DeepSeek 提供 Anthropic 兼容 API 端点（`https://api.deepseek.com/anthropic`，**末尾不能加 `/v1`**），Claude Code 改 `ANTHROPIC_BASE_URL` + 模型级别变量即可接入：
- **deepseek-v4-pro[1m]**：主 Agent（Opus/Sonnet 级），`[1m]` 后缀解锁 1M 上下文，不加只有 200K
- **deepseek-v4-flash**：子 Agent（Haiku 级），价格 $0.14/$0.28，比 Claude Haiku 4.5 便宜一个数量级
- **兼容性边界**：端点暂不支持 image/document 内容块（截图类任务拿到空白且无报错）；模型名写错时**静默 fallback 到 v4-flash 不报错**，需去控制台核对实际调用模型

## 关联连接
- [[摘要-腾讯内测cheso一个专做ppt的ai-agent]] — 来源
- [[Cheso]] — 集成平台
- [[DeepSeek-V4]] — 分层路由使用的模型系列
- [[ClaudeCode]] — 兼容端点的主要接入方
- [[模型路由]] — 分层路由概念
- [[摘要-claude-code-多agent账单分层路由]] — 来源（Anthropic 兼容端点实战）