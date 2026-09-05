---
title: "摘要-Apache PDFBox"
type: source
tags: [来源, PDF, Java, 开源库]
sources: [raw/09-archive/为什么越来越多人使用PDFBox？.md]
last_updated: 2026-07-21
---

## 核心摘要
Apache PDFBox 是 Apache 基金会维护的开源 Java PDF 处理库，采用 Apache 2.0 协议（对商业闭源友好）。文章从环境搭建起步，系统介绍了 PDFBox 的核心操作（创建、编辑、提取文本/图片、合并、加密、表单填充），深入解析了其双层架构（COS 底层对象层 + PD 高层语义层）和三层内容处理流水线（PDFStreamEngine → PDFGraphicsStreamEngine → 实现层），并总结了优缺点与适用场景。截至 2026 年 7 月，最新版本为 3.0.8。

## 关联连接
- [[Apache_PDFBox]] — Apache 基金会维护的 Java PDF 处理库
- [[PDFBox-双层架构]] — PDFBox 的 COS 层与 PD 层设计
- [[Apache-2.0协议]] — 对商业友好的开源协议