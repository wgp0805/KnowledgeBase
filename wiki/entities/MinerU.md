---
title: "MinerU"
type: entity
tags: [PDF, 文档解析, OCR, 开源工具, RAG, Agent基础设施]
sources: [raw/01-articles/2026-08-07-LangChain — RAG 构建知识库（理论） - VipSoft.md, raw/01-articles/2026-10-18 - 为什么越来越多人用MinerU？.md]
last_updated: 2026-10-19
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

### 4.0 版本：从"工具"到"Agent 的基础设施"（2026-10-18，详见 [[摘要-为什么越来越多人用MinerU]]）
- **定位**：GitHub 8 万+ Star，AI-Ready 数据生产的基础设施；核心论点"RAG 的上限不在向量库、不在大模型，在文档解析这一层"
- **与"抠字式"解析的区别**：PyMuPDF 按坐标吐文本，会拼乱双栏顺序、拆散表格行列关系、丢公式；MinerU"理解结构再重组"——先判断每页有什么（标题/段落/表格/公式/图片），再按人类阅读逻辑重组为结构化 Markdown/JSON
- **处理链路四步**：判文档类型（原生文本走 PyMuPDF，扫描件才 OCR）→ 视觉模型布局分析 → 分元素处理（公式→LaTeX、表格→HTML/OTSL、图片保位置）→ 结构化重组（剔页眉页脚，保标题层级）
- **定位器（Locator）**：4.0 输出带稳定地址 `doc:{id}/tier:{tier}/page:{page}/block:{block}`，Agent 可先读结构、找到段落再**精确回原文**复查引用——解析从"一次性转换"变成"Agent 可反复查阅的知识库"
- **四档解析**（替代 pipeline/vlm/hybrid）：`flash`（不跑推理直接解析原生文本，预览/索引）、`basic`（小模型 OCR/公式/表格，CPU 可跑）、`standard`（默认，小模型+VLM 平衡）、`advanced`（复杂文档追最高质量）；**默认只读前 10 页并返回 `next_request` 续读命令**，支持渐进式读取
- **代码用法**：`uv pip install -U "mineru"`（基础包 ONNX CPU + llama.cpp VLM，GPU 版 `mineru[full]`）；`mineru parse input.pdf --json` / `--pages all -o output.md`
- **Java 集成**：`mineru server start` 起 HTTP 服务（V1 API），上传→创建 job（带 tier）→**异步轮询**取结果；长文档可能数分钟，不能同步阻塞
- **优缺点**：结构化输出 RAG 友好、原生多格式、默认本地隐私可控、8 万 Star 验证；非学术文档优化不足、**不支持手写中文/古籍竖排**、Java 要走 HTTP、PyMuPDF 等依赖或有 AGPL 需合规确认
- **场景推荐**：RAG 预处理/学术论文/企业文档数字化/Agent 文档读取强烈推荐；合同发票需评估；手写与竖排古籍不推荐

## 关联连接
- [[DocumentLoader]] — LangChain 中的 PDF 加载器
- [[RAG]] — 知识库构建应用场景
- [[TextSplitter]] — 输出 Markdown 适合结构感知切分
- [[LangChain]] — 集成框架
- [[摘要-langchain-rag构建知识库-理论]] — 来源
- [[摘要-为什么越来越多人用MinerU]] — 2026-10-18 来源（4.0 定位器与四档解析）
- [[苏三]] — 4.0 解析文作者
- [[Agent上下文管理]] — 定位器支撑的渐进式读取场景