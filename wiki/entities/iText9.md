---
title: "iText9"
type: entity
tags: [实体, 工具库, Java, PDF, SDK, 加密, 数字签名]
sources: [raw/01-articles/iText 9，Java解析PDF神器 ！.md]
last_updated: 2026-09-15
---

## 定义
iText 是一套偏底层、但 API 设计得很克制的 PDF SDK，Java 和 .NET 都能用。社区版叫 **iText Core / Community**，走 **AGPL** 协议；公司内部要闭源商用，必须买商业授权。**iText 9** 是 2024 年底发布的大版本，现已迭代到 9.7.1。

## 关键信息

### 能力范围（四类）
- **生成**：从零拼页面，排段落、表格、图片、页眉页脚
- **解析**：把已有 PDF 里的文字、图片、图层抠出来
- **加工**：拆页、合并、盖章、填表单
- **合规**：PDF/A 归档、PDF/UA 无障碍、数字签名

跟 [[Apache_PDFBox]] 比，iText 更偏「产品级排版 + 标准合规」；跟在线转换工具比，它能嵌进你自己的服务里。做发票识别、合同归档、电子签这类业务，它基本是 Java 圈里绕不开的选项。

### 9.0 的四大新变化
1. **加密跟上 PDF 2.0 新标准**：支持 **ISO/TS 32003** 的 AES-GCM 加密（速度和安全性都比老 AES-CBC 好）与 **ISO/TS 32004** 的 **PDF MAC**（给加密文档加一层完整性保护，文件被悄悄改过一眼就能看出来）——从「锁住不让看」到「证明没被人动过手脚」
2. **数字签名从「能签」到「能验」**：iText 8 把签名能力做厚，9.0 把签名校验模块收尾——可以只验某一个签名、能处理加密文档里的签名、能顺着修订版本和证书链往下追，签和验不用两套工具来回倒
3. **PDF/A、PDF/UA 创建更省心**：创建与符合性检查收顺，签 PDF/UA 文档时签名外观缺字体、缺替代文本会**直接抛符合性异常**而不是让你在一堆属性错误里自己猜；新增实用 API——查出某一页真正用到了哪些图层（**OCG**），图纸、设计稿这类带图层的 PDF 排查方便很多
4. **后续小版本**：
   | 版本 | 值得关注的点 |
   | --- | --- |
   | 9.5.0 | Brotli 压缩流（面向未来 PDF 规范）、后量子签名算法试验 |
   | 9.7.0 | 原生 WebP 图片、动态页边距、脚注排版、解压炸弹防护加强 |
   | 9.7.1 | 修了 Jackson 依赖的安全问题，建议从 9.7.0 升上来 |

### 依赖引入
最省事写法：拉 `itext-core` BOM + 官方 Bouncy Castle 适配器（加密、签名都靠它）：
```xml
<properties>
    <itext.version>9.7.1</itext.version>
</properties>
<dependencies>
    <dependency>
        <groupId>com.itextpdf</groupId>
        <artifactId>itext-core</artifactId>
        <version>${itext.version}</version>
        <type>pom</type>
    </dependency>
    <dependency>
        <groupId>com.itextpdf</groupId>
        <artifactId>bouncy-castle-adapter</artifactId>
        <version>${itext.version}</version>
    </dependency>
</dependencies>
```
项目很瘦、只想读文本不碰签名时，只引 `kernel` 和 `layout` 即可。中文 PDF 还得额外准备字体文件（思源黑体、宋体等），**iText 不会凭空变出中文字形来**。

### 三大日常解析操作（占 80% 需求）
1. **整本抽文本**：`PdfTextExtractor.getTextFromPage()`，默认基于位置的策略，阅读顺序一般比「按内容流原始顺序」更接近人眼看到的样子。这是排查「这文件到底有没有可选中文字」的首选。
2. **定制 Strategy**：默认抽取不够用时用 `LocationTextExtractionStrategy`，9.x 里分隔符可定制，多页正则定位（`RegexBasedLocationExtractionStrategy`）也修过一波。发票场景的实用组合是：先整页抽文本，再用正则抠「发票号码」「价税合计」这些锚点——**版式一旦稳定，比上大模型便宜得多**。
3. **抠图片**：遍历每一页的资源字典，从 `XObject` 中取 `PdfStream`，判断 `Subtype` 为 `Image` 后用 `PdfImageXObject` 导出，`identifyImageFileExtension()` 判扩展名。JPEG、PNG 最常见；9.7 起 WebP 也能进 PDF。

### 核心流程习惯
**先 `PdfReader` 打开，再包一层 `PdfDocument`，用完一定要关**。生产代码保持 `try-with-resources`，否则大文件跑批量任务时句柄会漏。文件可能损坏时，创建 `PdfReader` 可打开非严格模式，9.x 重建 xref 表失败时会给出更明确的原因，排障比以前少猜很多。

### 写 PDF 与中文
生成回执 PDF 用 `PdfWriter` + `PdfDocument` + `Document`（layout 模块）。写中文必须把 `StandardFonts.HELVETICA` 换成磁盘上的中文字体路径：
```java
PdfFont font = PdfFontFactory.createFont(
    "C:/Windows/Fonts/simsun.ttc,0",
    "Identity-H",
    PdfFontFactory.EmbeddingStrategy.PREFER_EMBEDDED
);
```
`Identity-H` 是 Unicode 水平书写；嵌入策略选 `PREFER_EMBEDDED`，别人电脑没装这个字体也能打开。

### 踩坑提醒（五条）
1. **扫描件不是文本**——`PdfTextExtractor` 抽出来是空的，先确认 Acrobat 里能不能选中文字；那是 OCR 的活，得接 `pdfOCR` 或别的识别服务
2. **中文必须显式指定字体**——漏了就会缺字、方块、或者直接异常
3. **加密文档要密码**——`new PdfReader(path, new ReaderProperties().setPassword(...))`，空密码和用户密码、所有者密码不是一回事
4. **AGPL 不是「随便用」**——内部工具、开源项目没问题；要闭源商用，走商业许可
5. **从 8 升 9 先看 Breaking Changes**——符合性、签名、图层相关 API 有整理，照着官方迁移说明改，比对着编译错误一个个猜快

### 迁移成本
iText 9.0 是大版本，与 8.x 不完全兼容，但 7、8 打下的底子还在，**迁移成本没有当年从 5 升 7 那么疼**。

## 关联连接
- [[摘要-itext9-java-pdf]] — 来源
- [[Apache_PDFBox]] — 对比的开源 PDF 库（AGPL vs Apache 2.0）
- [[摘要-apache-pdfbox]] — PDFBox 全解析
- [[PDFBox-双层架构]] — PDFBox 的架构设计
- [[小锋]] — 文章作者
- [[Java]] — 语言生态
- [[Jackson]] — 9.7.1 修复的依赖安全问题
