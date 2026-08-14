---
title: "Qwen"
type: entity
tags: [AI模型, 阿里云, 通义千问, 多模态, 本地微调]
sources: [raw/01-articles/DeepSeek、Gemini、Qwen、Step 3.7 Flash实测，谁才是国产黑马？.md, raw/09-archive/测评国内多模态大模型，到底哪个更省事？.md, raw/01-articles/2026-07-09-开源诗词数据集poetry_dataset｜Mac本地微调诗词大模型全方案，配套诗词检索站shi-ci.cn - Java码界探秘.md, raw/01-articles/2026-07-19-【RAG扫盲系列·3】从零开始构建你的RAG项目第二弹：API 调用大模型问答 - Alkaid2077.md, raw/01-articles/阿里又开源了一个神级Skill项目！.md]
last_updated: 2026-08-14
---

## 定义
Qwen 是阿里通义千问大模型系列，本知识库主要收录 Qwen3.6 Flash 在 Coding Agent、源码解读和多模态视觉理解任务中的表现。

## 关键信息
- 面向 API 调用场景提供三层模型选型（详见 [[摘要-rag-api-call]]）：qwen-turbo（快速成本低，适合测试）、qwen-plus（平衡性能与成本，适合通用应用）、qwen-max（精度最高，适合复杂推理）
- 通过 DashScope OpenAI 兼容模式，可直接复用 LangChain、OpenAI SDK 等生态工具
- Qwen3.6 Flash 被用于"源码解读并生成 HTML 架构分析报告"的多轮工具调用任务。
- 文章认为 Qwen3.6 Flash 能一次对话完成任务，源码总结质量可用，但执行过程中出现多次工具调用失败，需要模型自修复。
- 与 Step 3.7 Flash 对比时，Qwen3.6 Flash 的输出 token 更多、API 时间更长、估算成本略高。
- 在横向表中，Qwen3.6 Flash 的工具调用稳定性低于 Step 3.7 Flash、DeepSeek V4 Flash 和 Gemini 3.5 Flash，但错误自修复能力仍被评价为高。

### 多模态实测（苏三 2026-07 横评，详见 [[摘要-多模态大模型横评-苏三]]）
| 场景 | 表现 |
|------|------|
| **流程图→业务逻辑还原** | 输出 9 步（**比参照少 1 步**：将步骤 3、4 合并），整体逻辑仍正确；19s；换算 ¥0.0483 |
| **电子发票→结构化 JSON** | 12 字段完全正确；7.38s（三者最慢）；换算 ¥0.0075 |

**综合评价**：稳定性达标（结构化任务无错误），但在两个场景下**速度和 Token 消耗都居中偏后**，属于"可用但不最优"档位。

### 多模态生成模型（通过 [[QianWen-AI]] Skill 调用）
- **wan2.6-t2i**：文本生成图片模型，qianwen-ai 自动选择用于图片生成
- **wan2.6-t2v**：文本生成视频模型，qianwen-ai 自动选择用于视频生成
- **qwen3-tts-instruct-flash**：语音合成模型，qianwen-ai 自动选择用于 TTS
- 详见 [[摘要-阿里开源qianwen-ai-skill项目]]

### Embedding 模型
- **Qwen3-Embedding-0.6B**：0.6B 参数，1024 维，32K 长度，MTEB 多语言榜 64.34 分，支持 MRL 维度压缩，多语言能力强
- 可通过 Ollama（OllamaEmbeddings）本地部署或阿里云 API 使用（见 [[Embeddings]]）
- 文本向量化服务还有 text-embedding-v3/v4 系列（见 [[DashScope]]）

## 关联连接
- [[摘要-step-3-7-flash-agent横评]] — Coding Agent 横评来源
- [[摘要-多模态大模型横评-苏三]] — 多模态横评来源
- [[多模态大模型]] — 归属类别
- [[Step3Flash]] — 横评对比模型（综合胜出方）
- [[MiniMax]] — 多模态横评对手
- [[DeepSeek]] — 横评对比模型
- [[Gemini]] — 横评对比模型
- [[AICoding]] — Coding Agent 应用场景
- [[Embeddings]] — Qwen3-Embedding 向量化模型
- [[LoRA]] — 微调方法
- [[摘要-开源诗词数据集poetry_dataset]] — 来源
- [[poetry_dataset]] — 支持 Qwen2.5 本地微调
- [[摘要-rag-api-call]] — API 调用与 RAG 实践
- [[摘要-langchain-rag构建知识库-理论]] — Embedding 模型来源
- [[DashScope]] — API 平台
- [[QianWen-AI]] — 通义千问多模态能力打包的 Agent Skill 项目
- [[摘要-阿里开源qianwen-ai-skill项目]] — 来源
