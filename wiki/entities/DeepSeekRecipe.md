---
title: "deepseek-recipe"
type: entity
tags: [实体, 编解码, 开源, DeepSeek, 工具调用]
sources: [raw/01-articles/2026-10-21 - 真正的 OpenAI！DeepSeek 开源内部推理框架 DeepInfer。.md]
last_updated: 2026-10-22
---

## 定义
deepseek-recipe 是 [[DeepSeek]] 与 [[DeepInfer]] 同批开源的**生产级 Token 编解码组件**，用 Rust 编写。它解决的是私有化部署中最常见的落差："明明权重一模一样，自己搭建的服务在深度思考或工具调用时就是不如官方的 API 稳定"——病根在于协议转换与分词处理。

## 关键信息
- **多协议统一**：把 Chat Completions API、Responses API、Messages API 统一转换成标准对话格式
- **两大难题的解法**：
  1. **提示词注入** —— 用户输入或工具结果里夹带的 `<｜User｜>` 或 `</think>` 会被直接编码成普通 Token，防止恶意文本篡改思考边界
  2. **分段并行分词** —— 沿特殊 Token 划定的边界多线程并行编码各段文本，大幅降低长上下文的分词耗时
- **输出端**：用基于 **KMP 算法**的状态机做跨数据块（Chunk）的流式解析，工具名解析完就立刻返回，参数生成时再逐段输出 JSON 片段，省去反复构造完整对象的开销
- **落地价值**：自建模型网关时可直接安装 deepseek-recipe，一步到位接管多协议转换、特殊字符注入与流式工具调用解析

## 关联连接
- [[DeepInfer]] — 同批开源的推理引擎
- [[DeepSeek]] — 开源方
- [[ToolCalling]] — 流式工具调用解析
- [[提示词注入防御]] — 特殊 Token 边界匹配
- [[FunctionCalling]] — 协议统一与工具协议
- [[ResponsesApi]] / [[ChatCompletionsAPI]] — 被统一的目标协议
- [[Rust]] — 实现语言
- [[摘要-deepinfer-deepseek开源推理框架]] — 来源
