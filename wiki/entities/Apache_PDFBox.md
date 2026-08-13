---
title: "Apache PDFBox"
type: entity
tags: [开源库, Java, PDF, Apache]
sources: [raw/09-archive/为什么越来越多人使用PDFBox？.md]
last_updated: 2026-07-21
---

## 定义
Apache PDFBox 是 Apache 软件基金会维护的开源 Java 库，专门用于处理 PDF 文档。采用 Apache 2.0 协议，允许自由使用、修改和分发，甚至用于商业闭源产品。

## 关键信息
- **最新版本**：3.0.8（截至 2026 年 7 月）
- **运行环境**：Java 8+
- **协议**：Apache 2.0（商业友好）
- **GitHub**：https://github.com/apache/pdfbox
- **官方文档**：https://pdfbox.apache.org

### 核心功能
- **创建**：全新的 PDF 文件
- **编辑**：现有 PDF 文档
- **提取**：PDF 中的文本、图片和元数据
- **合并/拆分**：多个 PDF 文件
- **加密/解密**：支持用户密码和所有者密码双重加密
- **数字签名**：符合 PDF 安全规范
- **表单填充**：支持 AcroForm 表单字段操作

### 版本迁移要点（2.x → 3.x）
- `PDDocument.load()` 被移除，必须使用 `Loader.loadPDF()`
- IO 模块重构，引入全新的 Loader 类
- 建议升级到 3.x：性能更好、API 更规范

### 与同类库对比
| 库 | 协议 | 商业友好度 |
|---|---|---|
| **Apache PDFBox** | Apache 2.0 | ✅ 高 |
| iText | AGPL（7.0+） | ❌ 商业需付费 |
| OpenPDF | LGPL/MPL | ⚠️ 一般 |

### 优缺点
**优点**：Apache 2.0 协议商业友好、功能全面一站解决、Apache 顶级项目社区活跃、API 设计直观、纯 Java 实现跨平台、附带命令行工具。

**缺点**：大文件性能偏弱、表格提取非原生功能（需结合 Tabula-java）、中文需手动加载字体、3.x 有破坏性变更。

## 关联连接
- [[摘要-apache-pdfbox]] — 来源文章
- [[PDFBox-双层架构]] — COS 层与 PD 层设计
- [[Apache-2.0协议]] — 使用的开源协议