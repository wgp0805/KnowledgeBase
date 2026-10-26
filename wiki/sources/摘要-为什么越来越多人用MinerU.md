---
title: "摘要-为什么越来越多人用MinerU"
type: source
tags: [来源, MinerU, 文档解析, RAG, Agent基础设施]
sources: [raw/09-archive/2026-10-18 - 为什么越来越多人用MinerU？.md]
last_updated: 2026-10-19
---

## 核心摘要

苏三说技术的 MinerU 深度解析：**RAG 的上限不在向量库、不在大模型，在文档解析这一层**——传统"抠字式"解析（PyMuPDF 按坐标吐文本）会拼乱双栏顺序、拆散表格行列、丢失公式，喂给 RAG 的原料是碎的，检索与生成必然碎。MinerU（GitHub 8 万+ Star，定位 AI-Ready 数据生产的基础设施）做的是"理解结构再重组"，2026 年 9 月发布的 **4.0 版本面向 Agent 时代引入定位器（Locator）与四档解析**。

## 关键信息

### 传统解析"碎"在三处
1. **多栏排版**：按坐标排序会把左栏底部和右栏顶部拼在一起，上下文断裂
2. **表格**：单元格是独立文本块，抠出来行列关系全丢，数字对不上指标名
3. **公式**：图片或特殊字体渲染，提取出乱码或占位符——技术文档丢了公式等于丢了半篇文章

### MinerU 处理链路（四步）
1. 判断文档类型：原生文本 PDF 直接走 PyMuPDF 解析原生对象，扫描件/纯图片页才启用 OCR
2. 布局分析：视觉模型识别文本块、表格、插图、公式位置，决定切分与阅读顺序
3. 分元素处理：公式→自研模型转 LaTeX，表格→HTML/OTSL，图片提取并保留位置
4. 结构化重组：按人类阅读顺序重组，剔除页眉页脚页码，保留标题层级

### 4.0 版本两大核心变化
- **定位器（Locator）**：输出带稳定地址 `doc:{id}/tier:{tier}/page:{page}/block:{block}`，Agent 可先读整体结构、找到相关段落，再**精确回到原文位置**复查引用——文档解析从"一次性转换"变成"Agent 可反复查阅的知识库"
- **四档解析**（替代原 pipeline/vlm/hybrid）：`flash`（不跑推理，直接解析原生文本，快速预览/索引）、`basic`（小模型 OCR/公式/表格，CPU 可跑）、`standard`（默认，小模型+VLM 平衡质量速度）、`advanced`（复杂文档，投入更多推理算力）
- 默认行为改为**只读前 10 页**并返回 `next_request` 续读命令，支持 Agent 渐进式读取

### 代码用法
- 安装：`uv pip install -U "mineru"`（基础包：ONNX CPU 小模型 + llama.cpp VLM）；GPU 完整版 `mineru[full]`
- CLI：`mineru parse input.pdf --json`（前 10 页续读）/ `mineru parse input.pdf --pages all -o output.md`
- **Java 集成走 HTTP**：`mineru server start` 启动 V1 API 服务，流程为上传拿 file_id → 创建 job（带 tier 参数）→ 轮询状态取结果；解析是**异步的**，长文档可能几分钟，必须轮询/回调不能同步阻塞

### 优缺点与适用场景
- 优点：结构化输出 RAG 友好、原生多格式（PDF/图片/DOCX/PPTX/XLSX/EPUB/OFD/HTML）、四档按需控成本、定位器可溯源、**默认全程本地隐私可控**（`--remote` 才上传）、8 万+ Star 社区验证
- 缺点：非学术文档优化不足（基因是科学文献符号转换）、**不支持手写中文/古籍竖排**、Python 工具 Java 集成要走 HTTP 加异步复杂度、PyMuPDF 等依赖可能有 AGPL 许可证需合规确认
- 强推荐：RAG 文档预处理、学术论文、企业文档数字化、Agent 工作流文档读取；需评估：合同发票；不推荐：手写/竖排古籍

## 关联连接
- [[MinerU]] — 实体页（本次增量合并 4.0 信息）
- [[苏三]] — 本文作者
- [[RAG]] — 文档解析质量决定其上限
- [[DocumentLoader]] — 上游解析环节
- [[TextSplitter]] — 结构化 Markdown 的下游切分
- [[摘要-langchain-rag构建知识库-理论]] — 既有 MinerU 相关来源
- [[摘要-apache-pdfbox]] — 同作者此前解析工具对比文
