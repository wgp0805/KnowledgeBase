---
title: "摘要-itext9-java-pdf"
type: source
tags: [来源, 原始文件, Java, PDF, iText, 工具库]
sources: [raw/01-articles/iText 9，Java解析PDF神器 ！.md]
last_updated: 2026-09-15
---

## 核心摘要
小锋（公众号 java1234）系统介绍 **iText 9**——一套偏底层但 API 设计克制的 PDF SDK（Java/.NET 通用），社区版 iText Core / Community 走 AGPL，闭源商用需商业授权。iText 9.0 是 2024 年底发布的大版本，现已迭代到 **9.7.1**；大版本与 8.x 不完全兼容，但 7、8 的底子在，迁移成本远小于当年 5 升 7。四大新变化：(1) 加密跟上 PDF 2.0 新标准——**ISO/TS 32003 的 AES-GCM**（比老 AES-CBC 更快更安全）与 **ISO/TS 32004 的 PDF MAC**（完整性保护，文件被改过一眼能看出），从「锁住不让看」到「证明没被人动过手脚」；(2) 数字签名从「能签」到「能验」——签名校验模块收尾，可只验某一个签名、处理加密文档里的签名、顺着修订版本和证书链追；(3) PDF/A、PDF/UA 创建与符合性检查收顺，签 PDF/UA 文档时签名外观缺字体/缺替代文本会直接抛符合性异常，新增「查出某一页真正用到哪些 OCG 图层」API；(4) 后续小版本：9.5.0 Brotli 压缩流 + 后量子签名算法试验，9.7.0 原生 WebP/动态页边距/脚注排版/解压炸弹防护加强，9.7.1 修 Jackson 依赖安全问题（建议从 9.7.0 升上来）。Maven 依赖拉 `itext-core` BOM + `bouncy-castle-adapter`（加密签名靠它），精简场景只引 `kernel` + `layout`。三大日常操作（占 80% 需求）：整本抽文本（`PdfTextExtractor` 默认位置策略，阅读顺序更接近人眼）、定制 Strategy（`LocationTextExtractionStrategy` + `RegexBasedLocationExtractionStrategy`，发票场景先整页抽文本再正则抠「发票号码/价税合计」锚点，**版式稳定后比上大模型便宜得多**）、抠图片（遍历每页 `XObject` 资源字典导出位图，`identifyImageFileExtension()` 判扩展名）。流程习惯：**先 `PdfReader` 打开再包一层 `PdfDocument`，用完一定要关**（`try-with-resources`，否则批量任务句柄会漏）；损坏文件可开非严格模式，9.x 重建 xref 表失败时给更明确原因。写 PDF 中文必须显式指定字体路径（`Identity-H` + `PREFER_EMBEDDED`）。五条踩坑：扫描件不是文本（先确认 Acrobat 里能不能选中）、中文必须显式指定字体、加密文档要密码（空密码/用户密码/所有者密码不是一回事）、**AGPL 不是「随便用」**（内部工具和开源没问题，闭源商用走商业许可）、从 8 升 9 先看 Breaking Changes。与 [[Apache_PDFBox]] 对比：iText 更偏「产品级排版 + 标准合规」。

## 关联连接
- [[iText9]] — 本文主角 PDF SDK
- [[Apache_PDFBox]] — 对比的开源 PDF 库
- [[摘要-apache-pdfbox]] — PDFBox 全解析
- [[PDFBox-双层架构]] — PDFBox 的架构设计
- [[小锋]] — 作者（公众号 java1234）
- [[Java]] — 语言生态
- [[摘要-使用Docker在Windows上部署独立MySQL]] — 同一「运维实操」类文章的同类参考
