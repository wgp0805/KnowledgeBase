---
title: "PDFBox 双层架构"
type: concept
tags: [架构, PDF, PDFBox, 软件设计]
sources: [raw/01-articles/为什么越来越多人使用PDFBox？.md]
last_updated: 2026-07-21
---

## 定义
PDFBox 采用双层架构来分离底层 PDF 结构和高层业务语义，实现"常规操作快速完成，复杂需求下沉到 COS 层获取完全控制权"的设计目标。

## 关键信息

### COS 层（底层对象层）
直接映射 PDF 文件中的基本对象：
- **COSDictionary** — 字典
- **COSArray** — 数组
- **COSStream** — 流
- 通过 COS 层可以访问 PDF 文件的任何底层细节

### PD 层（高层语义层）
在 COS 层之上封装面向开发者的友好 API：
- **PDDocument** — 代表整个文档
- **PDPage** — 代表一页
- **PDPageContentStream** — 代表内容流

### 三层内容处理流水线
1. **基础处理层（PDFStreamEngine）**：解析内容流为 Token 序列，将操作分发给注册的处理器，维护图形状态栈，管理资源。把 PDF 的"二进制指令流"翻译成"可执行的操作序列"。
2. **图形抽象层（PDFGraphicsStreamEngine）**：定义图形操作的抽象方法（路径构建、填充、描边、绘制图像），只定义"画什么"不关心"怎么画"。
3. **实现层（PageDrawer、PDFTextStripper 等）**：提供具体实现。`PageDrawer` 负责渲染到 Graphics2D，`PDFTextStripper` 通过重写 `showGlyph()` 方法收集字符位置信息实现文本提取。

这种分层设计使 PDFBox 具有极高的可扩展性——开发者可以继承 `PDFStreamEngine` 实现自定义行为，如内容分析或自定义渲染后端。

## 关联连接
- [[Apache_PDFBox]] — 使用该架构的 PDF 处理库
- [[摘要-apache-pdfbox]] — 来源文章