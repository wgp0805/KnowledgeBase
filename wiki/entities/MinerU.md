---
title: "MinerU"
type: entity
tags: [PDF, 文档解析, OCR, 开源工具]
sources: [raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md]
last_updated: 2026-08-10
---

## 定义
MinerU 是国人开发的开源文档解析工具，可本地部署，处理速度和精度都非常优秀，推荐用于 RAG 知识库构建中的 PDF 解析环节。

## 关键信息
- **能力**：PDF 解析为主，也支持 HTML、PPT、PPTX、DOC、DOCX、XLS、XLSX、图片等多种格式，单一加载器理论可满足 90% 企业需求
- **使用方式**：
  - SDK：原生 SDK，兼容性最好，可自由处理解析好的 markdown/images/json
  - LangChain：完美适配，但解析 PDF 时只能得到 markdown，其他内容无法获取
- **OCR 支持**：扫描件 PDF 将 `ocr=True` 即可处理
- **服务地址**：mineru.net，注册获取 Token，每日免费 2000 页高优先级额度
- **与 LangChain 集成**：作为 DocumentLoader 使用，输出通常是严谨结构的 Markdown，适合配合结构感知切分

## 关联连接
- [[DocumentLoader]] — LangChain 中的 PDF 加载器
- [[RAG]] — 知识库构建应用场景
- [[TextSplitter]] — 输出 Markdown 适合结构感知切分
- [[LangChain]] — 集成框架
- [[摘要-langchain-rag构建知识库-理论]] — 来源