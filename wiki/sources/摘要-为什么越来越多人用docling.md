---
title: "摘要-为什么越来越多人用docling"
type: source
tags: [来源, Docling, RAG, 文档解析]
sources: ["raw/09-archive/2026-11-22 - 为什么越来越多人用 Docling ？.md"]
last_updated: 2026-11-24
---

## 核心摘要
苏三 2026-11-22 解析 [[Docling]] 为什么被 RAG 项目大量采用。核心论点：RAG 效果差多数不是 Embedding/切片/检索的问题，而是**PDF 变文本时结构就已经丢了**——传统工具（PyMuPDF、pdfplumber）解决"把字抠出来"，Docling 解决"把结构留下来"。它用 AI 模型把 PDF 的视觉信息还原成逻辑结构，识别标题/段落/表格/图片/公式/代码块并按人类阅读顺序重组，输出带层级、带位置、带表格结构的 `DoclingDocument`。

架构分三层：解析后端 `docling-parse`（基于 qpdf 构建，规避 PyMuPDF 许可证限制与 pypdfium 质量问题）；AI 管道 `StandardPdfPipeline` 并行跑 OCR、版面分析与表格识别（版面用 **DocLayNet**，表格用 **TableFormer**）；统一文档模型支持无损导出 JSON/Markdown/HTML。三个关键原理：①版面分析先识别"元素类型+坐标"，后续处理都基于元素而非文本流；②阅读顺序还原解决双栏论文"左栏底部拼右栏顶部"的上下文断裂；③TableFormer 预测行列结构，能还原合并单元格与多级表头（TEDS 0.877–0.911），让大模型知道"这个数字属于哪个指标"。

工程侧：`pip install docling`（Python 3.10+，三平台），`DocumentConverter` + `PdfPipelineOptions(do_ocr, do_table_structure)`，`HybridChunker` 按结构切块并用 `contextualize()` 把"员工手册 > 人事制度 > 离职管理"这类章节路径拼回切片，Embedding 拿到的是带上下文的文本。

治理与局限：IBM 研究院出品，2025-03 捐 Linux 基金会，2026-08 成为 LF AI & Data Graduated 项目，GitHub 7 万+ Star，68% 以上 PR 来自核心团队外。缺点：不是最快（CPU 复杂 PDF 9–10 秒）、极复杂嵌套表格仍不如商业方案（Reducto 声称高约 20%）、Python 生态导致 Java 需走 `docling-serve` REST 或 `docling-java` 封装、公式转 LaTeX/代码块/图片描述等高级功能默认关闭。结论：结构保留直接决定 RAG 上限，Docling 是开源里结构保留最完整、生态集成最成熟的选择之一。

## 关联连接
- [[Docling]] — 本篇主角
- [[RAG]] — 主要应用场景
- [[Chunk分块]] — HybridChunker 的结构化切分对照
- [[结构化感知分块]] — 同一思路的既有概念
- [[MinerU]] — 同类开源 PDF 解析工具（选型对照）
- [[LlamaParse]] — 商业文档解析对照
- [[VectorStore]] — 切片后的落库目标
- [[LangChain4j]] — 生态集成对象
