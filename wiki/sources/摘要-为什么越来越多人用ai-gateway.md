---
title: "摘要-为什么越来越多人用ai-gateway"
type: source
tags: [来源, 原始文件, AI Gateway, LLM网关, LiteLLM, 基础设施]
sources: [raw/09-archive/为什么越来越多人用 AI Gateway？.md]
last_updated: 2026-11-10
---

## 核心摘要

苏三（2026-11-10）从"AI 客服系统在业务层写了三套供应商适配器（OpenAI/Anthropic/通义千问），老板说切 DeepSeek 要改三个适配器 + 一堆 `if provider == 'openai'`"的真实痛点切入，拆解 **AI Gateway**：把"调模型"从业务代码里抽出来，变成一层统一基础设施——业务只对一个地址说一种语言，路由/翻译/兜底/记账交给网关。

**直接调模型的四大灾难**：
1. **协议不统一**：OpenAI 用 `tool_calls`、Anthropic 用 `tool_use` content block、Gemini 用 `functionCall` part；系统提示位置不同、流式增量结构各异 → 每接一家写一套入参/出参/流式转换
2. **故障处理零散**：每个业务方法都写 try-catch + fallback，重试/降级/429 处理逻辑各处不一致
3. **成本不可见**：多供应商账单格式不同，对不上"哪个业务线花了多少钱"
4. **安全管控分散**：部门 Token 限额、PII 脱敏、调用审计无法统一

**AI Gateway 四大能力**：
1. **协议归一化**：业务发标准 OpenAI Chat Completions 格式，Gateway 翻译成目标供应商格式再翻回来（LiteLLM 的 `litellm.completion()` 就是 Translation and parameter mapping）
2. **模型路由**（四层次）：固定模型 → 规则路由（按场景/租户/风险映射）→ 成本路由（小模型先试、置信度低再升级强模型）→ Fallback 与熔断（**不是所有错误都该 Fallback**：网络瞬断/5xx 适合切换；429 要读 `Retry-After`；认证错误切了也没用）
3. **Key 管理（虚拟 Key）**：给应用/用户发虚拟 Key，Gateway 映射到真实供应商 Key；可随时吊销单个虚拟 Key、追踪哪个应用调了多少花了多少、给部门设预算上限
4. **可观测性**：**Token 消耗、成本归因、首 Token 延迟是新的 QPS**——两个请求 QPS 一样但一个 100 Token、一个 10 万 Token，成本差千倍，传统按 QPS 限流无效，要按 Token 限流/预算控制

**LiteLLM 落地**：`pip install 'litellm[proxy]'` + `config.yaml` 定义 model_list（model_name / litellm_params / api_key: os.environ/XXX），客户端用 OpenAI SDK 指向 `base_url=http://localhost:4000`、传虚拟 Key，业务代码只认 `base_url` 和 `model`。Thoughtworks 技术雷达已把它从"语言与框架"移到"平台"类别（"我们更多把它看作基础设施，而不是一个库"）。

**AI 辅助排障**：网关日志集中且结构化，把网关请求/错误日志喂给 AI 可快速区分"网关配置问题 vs 供应商问题"（如 `gpt-4o` 报 500 但 deepseek 正常 → 日志显示 `AuthenticationError: Incorrect API key` → 网关到 OpenAI 的 Key 配置问题）；但"Key 为什么失效"需人工查供应商控制台——**AI 缩小范围，人做最终判断**。

**优缺点**：优点——业务与供应商解耦、故障处理集中、成本可观测可控、Key 管理更安全、协议翻译自动化；缺点——**多一层多一个故障点**（网关必须高可用）、供应商特有功能可能被"抹平"（LiteLLM `drop_params` 静默丢弃不支持的参数）、自托管有运维成本（LiteLLM 2026 年已报告 25+ CVE 需及时打补丁）、单模型简单应用属过度设计。

**适用场景**：多模型/多供应商切换、成本管控与归因、企业级 Key 管理与审计、供应商故障自动兜底——强烈推荐；单模型简单应用不推荐；依赖供应商特有功能需评估。

**结论**："调模型"正从"写一行代码"变成"管一套基础设施"——多模型、多供应商、需成本管控和审计的团队，AI Gateway 已从可选项变成基础设施。

## 关联连接
- [[LLM网关]] — 同义/上位概念（本文为工程化全景版）
- [[AI网关]] — 团队侧集中管理的同类概念
- [[LiteLLM]] — 最广泛使用的开源 AI Gateway
- [[模型路由]] — 路由四层次与错误分类
- [[苏三]] — 作者
- [[OpenAI]] — 协议基准与供应商
- [[Anthropic]] — 供应商之一
- [[DeepSeek]] — 成本路由候选
- [[Ollama]] — 自建模型接入示例
- [[Token估算]] — Token 计量相关
- 语义缓存 — 阿里云 AI 网关并列的核心能力（无独立页）
