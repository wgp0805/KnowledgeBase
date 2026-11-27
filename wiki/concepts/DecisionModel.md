---
title: "DecisionModel"
type: concept
tags: [概念, SpringAI, 决策, 概率]
sources: ["raw/09-archive/2026-11-22 - 夯爆了，Spring AI 2.1 正式发布 ！.md", "raw/09-archive/夯爆了，Spring AI 2.1 正式发布！.md"]
last_updated: 2026-11-27
---

## 定义
DecisionModel 是 [[SpringAI]] 2.1 引入的模型抽象，专做"是/否、单选、打分"这类**决策题**而不是开放式对话：调用方把候选答案列出来，模型从中挑一个并给出每个答案的概率，由业务代码决定"多有把握才执行"。

## 关键信息
- **要解决的问题**：业务里大量判断只有固定几个答案（评论是否为广告、工单属于哪个分类、用户满意度）。过去让聊天模型输出自由文本再用正则/JSON 硬抠，模型稍微"放飞自我"解析就挂
- **三种题型**：
  - `YesNoQuestion`：是非题，可给 `whenYes` / `whenNo` 语义描述降低歧义
  - `ChoiceQuestion`：单选题，`.option(key, 描述)`
  - `ScoreQuestion`：打分题，`ScoreQuestion.of(text, "unhappy", "neutral", "happy")` 取最近等级
- **概率门控**：`response.getYesNo("defect").isYes(0.9)` —— 模型有九成把握才自动开维修单，把"模型判断"和"业务动作"之间插入一道阈值
- **多题一次调用**：一个 `DecisionPrompt` 里可以并列多个问题，一次拿到缺陷判定 + 分类 + 满意度
- **实现**：`OpenAiDecisionModel`、`OllamaDecisionModel`、`SystemOneDecisionModel`（[[SystemOneModels]] 体系）
- **已被框架自身采用**：RAG 的 `DecisionDocumentReranker`（文档重排序）、`DecisionDocumentFilter`（过滤提示词注入）、工具检索的 `DecisionToolIndex`
- **边界**：它是机器学习模型不是规则引擎，判错代价高的场景必须保留人工确认环节

## 口径差异（两篇来源的 API 命名不同）

2.1 的两篇中文解读对 DecisionModel 的 API 用了**不同命名**，属同一能力的表述差异，不是版本冲突，按实际版本核对：

| | [[摘要-spring-ai-2-1发布]]（[[锋哥]]） | [[摘要-spring-ai-2-1-苏三解读]]（[[苏三]]） |
| --- | --- | --- |
| 答案类型 | `YesNoQuestion` / `ChoiceQuestion` / `ScoreQuestion` | `Choice` / `Noul`（是/否概率）/ `Score` |
| 组装方式 | `DecisionPrompt` 内并列多题 | `DecisionRequest.builder().choice("category","工单分类","billing","technical","other").noul("is_urgent","是否紧急")` |
| 取值方式 | `response.getYesNo("defect").isYes(0.9)` | `response.getNoul("is_urgent").isYes(0.9)` |
| 触发方式 | 未展开 | `decisionModel.evaluate(...)` |

两者共同点（这部分可放心依赖）：**三种题型（是非 / 单选 / 打分）、每题返回概率、用 `isYes(阈值)` 做业务门控、支持一次调用并列多题**。差异集中在 builder/response 的方法名上——`getYesNo` 与 `getNoul` 指向同一个「是非题概率」语义。落地时以项目实际引入的 2.1.0 版本 API 为准，不要照抄任一篇文章的方法名。

关于实现，两篇口径一致：`OpenAiDecisionModel`（配 `spring.ai.openai.decision`）、`OllamaDecisionModel`（默认 `d1-omni:600m`，本地跑无需 Key）、`SystemOneDecisionModel`（TypeSafe Java SDK，兼容 Jev/Laya 的 System One 协议，**不自动配置**，需手建 `TypeSafeClient`）。

## 关联连接
- [[SpringAI]] — 所属框架
- [[SystemOneModels]] — 打分型模型族
- [[判断模型]] — 同类思想（把判断题从生成模型里拆出来）
- [[置信度校准]] — 概率阈值为何要业务侧设定
- [[RAG]] — Reranker/Filter 的落地点
- [[工具路由]] — DecisionToolIndex 的分工
- [[摘要-spring-ai-2-1发布]] — 来源
- [[摘要-spring-ai-2-1-苏三解读]] — 来源（另一套 API 命名口径）
- [[SystemOne]] — System One 决策模型的理论出处
