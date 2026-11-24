---
title: "Docling"
type: entity
tags: [工具, 文档解析, RAG, Python, 开源项目]
sources: ["raw/09-archive/2026-11-22 - 为什么越来越多人用 Docling ？.md"]
last_updated: 2026-11-24
---

## 定义
Docling 是 [[IBM]] 研究院开源、现由 Linux 基金会托管的文档解析工具（Python 包，`pip install docling`），目标是把 PDF/DOCX/PPTX/XLSX/HTML/图片等还原成**带层级、带位置、带表格结构的统一文档模型** `DoclingDocument`，而不是"一堆抠出来的文字"。

## 关键信息
- **定位差异**：PyMuPDF/pdfplumber 解决"把字抠出来"，Docling 解决"把结构留下来"。PDF 本质是"在坐标 (x,y) 画一段文字"的指令集合，不含标题/表格/栏的语义，传统工具取字即丢结构
- **架构三层**：
  1. 解析后端 `docling-parse`（基于 qpdf 构建，规避 PyMuPDF 许可证限制与 pypdfium 质量问题）
  2. AI 管道 `StandardPdfPipeline`：并行跑 OCR、版面分析、表格结构识别
  3. 统一文档模型 `DoclingDocument`：带层级、位置、表格结构，可无损导出 JSON / Markdown / HTML
- **两个关键模型**：版面分析用 **DocLayNet**（识别元素类型 + 坐标，后续处理基于"元素"而非"文本流"）；表格识别用 **TableFormer**（预测行列结构、合并单元格、多级表头，TEDS 0.877–0.911）
- **阅读顺序还原**：解决多栏排版按坐标硬排导致"左栏底部拼右栏顶部"的上下文断裂，推断人类在一页上的实际阅读顺序
- **RAG 接口**：`HybridChunker` 按文档结构切块（标题下的段落不被拆开、表格不被切半），并用 tokenizer 感知切片大小；`contextualize()` 把"员工手册 > 人事制度 > 离职管理"这类章节路径拼回切片文本，提升 Embedding 检索准确率
- **工程用法**：`DocumentConverter().convert(src)` → `export_to_markdown()`；扫描件需 `PdfPipelineOptions(do_ocr=True, do_table_structure=True)` 并通过 `PdfFormatOption` 传入
- **治理**：2025-03 捐 Linux 基金会，2026-08 成为 LF AI & Data Graduated 项目；GitHub 7 万+ Star；68% 以上 PR 来自核心团队之外；贡献者覆盖 109 个组织
- **优点**：结构化输出 RAG 友好、表格能力强、完全本地运行（数据敏感/离线内网可用）、多格式统一、生态成熟（LangChain/LlamaIndex/MCP Server/docling-java）、开源治理可靠
- **缺点**：不是最快（CPU 复杂 PDF 约 9–10 秒，简单 PDF 上 Marker/PyMuPDF4LLM 更快）、极复杂嵌套表格仍逊于商业方案（Reducto 声称高约 20%）、Python 生态导致 Java 需走 `docling-serve` REST 或 `docling-java` 封装、公式转 LaTeX/代码块识别/图片描述默认关闭
- **结论**：一份 PDF 的价值不在字数而在"字与字之间的关系"；结构保留直接决定 RAG 上限

## 关联连接
- [[RAG]] — 主要落地场景（文档预处理）
- [[Chunk分块]] — 字符切片 vs 结构化切片的对照
- [[结构化感知分块]] — 同一思路的既有概念
- [[MinerU]] — 国产开源 PDF 解析对照
- [[LlamaParse]] — 商业文档解析对照
- [[VectorStore]] — 切片落库目标
- [[LangChain4j]] / [[LangChain]] — 生态集成
- [[IBM]] — 出品方
- [[摘要-为什么越来越多人用docling]] — 来源
