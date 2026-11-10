---
title: "LiteLLM"
type: entity
tags: [开源项目, AI网关, LLM网关, Python, 基础设施]
sources: [raw/09-archive/为什么越来越多人用 AI Gateway？.md]
last_updated: 2026-11-10
---

## 定义

LiteLLM 是目前最广泛使用的开源 AI Gateway（Python 生态），核心工作是 **Translation and parameter mapping**：把统一的 OpenAI Chat Completions 协议翻译成各家供应商（OpenAI/Anthropic/Gemini/DeepSeek/Ollama 等）的调用格式，并在中间层完成路由、回退、重试、虚拟 Key 与用量计量。Thoughtworks 技术雷达已将其从"语言与框架"移入"平台"类别——"我们更多把它看作基础设施，而不是一个库"。

## 关键信息

### 快速启动

```bash
pip install 'litellm[proxy]'
litellm --config /path/to/config.yaml
```

### 配置文件（model_list 路由）

```yaml
model_list:
  - model_name: "gpt-4o"
    litellm_params:
      model: "openai/gpt-4o"
      api_key: os.environ/OPENAI_API_KEY
  - model_name: "deepseek-chat"
    litellm_params:
      model: "deepseek/deepseek-chat"
      api_key: os.environ/DEEPSEEK_API_KEY
  - model_name: "qwen-max"
    litellm_params:
      model: "dashscope/qwen-max"
      api_key: os.environ/DASHSCOPE_API_KEY
```

### 客户端零改动调用

```python
from openai import OpenAI

client = OpenAI(api_key="sk-litellm-virtual-key", base_url="http://localhost:4000")
resp = client.chat.completions.create(
    model="gpt-4o",   # 或 "deepseek-chat" / "qwen-max"
    messages=[{"role": "user", "content": "解释一下什么是 AI Gateway"}],
)
```

业务代码只认 `base_url` 与 `model` 两个东西，背后是哪家供应商完全透明。

### 核心能力（对应 AI Gateway 四能力）

| 能力 | LiteLLM 对应实现 |
|------|-----------------|
| 协议归一化 | `litellm.completion()` 统一翻译请求/响应/流式事件 |
| 模型路由 | Router：Load balancing + Fallbacks + Retries 收在一层 |
| 虚拟 Key | 请求第一步校验 `Bearer` token 对应 Virtual Key 是否有效、是否在预算内 |
| 可观测 | Token 消耗、成本归因、预算控制 |

### 已知风险

- **CVE 数量多**：2026 年已报告 25+ CVE，自托管需及时打安全补丁
- **功能抹平**：`drop_params` 模式会静默丢弃供应商不支持的参数，依赖特有能力时需评估
- **多一个故障点**：网关本身的高可用必须保证，不能单点

## 关联连接
- [[摘要-为什么越来越多人用ai-gateway]] — 来源
- [[LLM网关]] — 上位概念
- [[AI网关]] — 同类概念
- [[模型路由]] — Router 能力所属
- [[苏三]] — 介绍作者
- [[DeepSeek]] — 配置示例中的供应商
- [[OpenAI]] — 协议基准
