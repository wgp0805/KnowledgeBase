---
title: "iText 9，Java解析PDF神器 ！"
source: "https://mp.weixin.qq.com/s/_GTwKXsYY80cLdtLXidXUw"
---
小锋 java1234 *2026年9月15日 09:06*

大家好，我是锋哥。

> 做 Java 的同学，多半都跟 PDF 较过劲。合同要归档、发票要抽数、报表要生成、签完字还得验签——这些活看起来简单，真上手才知道 PDF 有多“拧”。我自己最早用的是 iText 5，后来迁到 7、8。等到 **iText 9** 出来，明显感觉它不再只是“能写 PDF 的库”，而是一套比较完整的 PDF 工具箱：读、写、改、加密、签名、无障碍，一条链路都能走通。锋哥今天来好好聊聊 iText 9 。

---

![图片](assets/iText%209%EF%BC%8CJava%E8%A7%A3%E6%9E%90PDF%E7%A5%9E%E5%99%A8%20%EF%BC%81/cd2690f7478b8fc14920258195d60d0f_MD5.webp)

## 目录

- 一、先认识一下 iText
- 二、iText 9 到底新在哪
- 三、五分钟把依赖加上
- 四、最常用的三件事：抽文本、按页解析、抠图片
- 五、解析流程长什么样
- 六、写 PDF 也顺手带一笔
- 七、几点踩坑提醒

---

## 一、先认识一下 iText

iText 是一套偏底层、但 API 设计得很克制的 PDF SDK，Java 和.NET 都能用。社区版叫 **iText Core / Community** ，走 AGPL；公司内部如果要闭源商用，得买商业授权。

它能干的事大致就这几类：

- **生成** ：从零拼页面，排段落、表格、图片、页眉页脚
- **解析** ：把已有 PDF 里的文字、图片、图层抠出来
- **加工** ：拆页、合并、盖章、填表单
- **合规** ：PDF/A 归档、PDF/UA 无障碍、数字签名

跟 Apache PDFBox 比，iText 更偏“产品级排版 + 标准合规”；跟一堆在线转换工具比，它是能嵌进你自己服务里的。做发票识别、合同归档、电子签这类业务，它基本是 Java 圈里绕不开的选项。

![图片](assets/iText%209%EF%BC%8CJava%E8%A7%A3%E6%9E%90PDF%E7%A5%9E%E5%99%A8%20%EF%BC%81/a717f2059eaf1cca59a515b5bdcc29bf_MD5.jpg)

---

## 二、iText 9 到底新在哪

iText 9.0 是 2024 年底发布的大版本，到现在已经迭代到 **9.7.1** 。大版本意味着跟 [8.x](http://8.x/) 不完全兼容，但好消息是：7、8 打下的底子还在，迁移成本没有当年从 5 升 7 那么疼。

我把 [9.x](http://9.x/) 系列里，开发时真正能感知到的变化，收成下面几条。

### 1\. 加密终于跟上 PDF 2.0 的新标准

9.0 直接支持了两个新 ISO 技术规范：

- **ISO/TS 32003** ：PDF 2.0 里的 **AES-GCM** 加密，速度和安全性都比老的 AES-CBC 更舒服
- **ISO/TS 32004** ： **PDF MAC** ，给加密文档加一层完整性保护，文件被悄悄改过一眼就能看出来

简单说：以前更多是“锁住不让看”，现在还能证明“没被人动过手脚”。

### 2\. 数字签名，从“能签”变成“能验”

iText 8 把签名能力做厚了，9.0 把 **签名校验模块** 收了个尾：可以只验某一个签名、能处理加密文档里的签名、还能顺着修订版本和证书链往下追。签和验终于不用两套工具来回倒了。

### 3\. PDF/A、PDF/UA 创建更省心

无障碍和归档一直是 iText 的强项。9.0 把 PDF/A、PDF/UA 的创建和符合性检查收顺了，签 PDF/UA 文档时，签名外观缺字体、缺替代文本，会直接抛符合性异常，而不是让你在一堆属性错误里自己猜。

另外还多了个小而实用的 API： **查出某一页真正用到了哪些图层（OCG）** 。图纸、设计稿这类带图层的 PDF，排查起来方便很多。

### 4\. 后面几个小版本也没闲着

如果你直接上最新的 9. [7.x，还能顺手拿到这些：](http://7.x，还能顺手拿到这些：)

| 版本 | 值得关注的点 |
| --- | --- |
| 9.5.0 | Brotli 压缩流（面向未来 PDF 规范）、后量子签名算法试验 |
| 9.7.0 | 原生 WebP 图片、动态页边距、脚注排版、解压炸弹防护加强 |
| 9.7.1 | 修了 Jackson 依赖的安全问题，建议从 9.7.0 升上来 |

![图片](assets/iText%209%EF%BC%8CJava%E8%A7%A3%E6%9E%90PDF%E7%A5%9E%E5%99%A8%20%EF%BC%81/13ed7d8c4aa16873171dffabf9a9acde_MD5.jpg)

---

## 三、五分钟把依赖加上

Maven 里最省事的写法，是直接拉 `itext-core` 这个 BOM，再配上官方的 Bouncy Castle 适配器（加密、签名都靠它）：

```xml
<properties>    <
            itext.version
          >9.7.1</
            itext.version
          ></properties>
<dependencies>    <dependency>        <groupId>
            com.itextpdf
          </groupId>        <artifactId>itext-core</artifactId>        <version>${
            itext.version}
          </version>        <type>pom</type>    </dependency>    <dependency>        <groupId>
            com.itextpdf
          </groupId>        <artifactId>bouncy-castle-adapter</artifactId>        <version>${
            itext.version}
          </version>    </dependency></dependencies>
```

如果项目很瘦，只想读文本、不想碰签名，也可以只引 `kernel` 和 `layout` ：

```xml
<dependency>    <groupId>
            com.itextpdf
          </groupId>    <artifactId>kernel</artifactId>    <version>9.7.1</version></dependency><dependency>    <groupId>
            com.itextpdf
          </groupId>    <artifactId>layout</artifactId>    <version>9.7.1</version></dependency>
```

中文 PDF 还得额外准备字体文件（比如思源黑体、宋体），iText 不会凭空变出中文字形来，这一点后面会再提一句。

---

## 四、最常用的三件事：抽文本、按页解析、抠图片

日常解析，80% 的需求就卡在这三件事上。

![图片](assets/iText%209%EF%BC%8CJava%E8%A7%A3%E6%9E%90PDF%E7%A5%9E%E5%99%A8%20%EF%BC%81/d8ed39bff213b555681fd142a9a21808_MD5.jpg)

### 1\. 一页都不想管，整本抽文本

这是入门第一行代码，也是我排查“这文件到底有没有可选中文字”时的首选：

```java
import 
            com.itextpdf.kernel.pdf.PdfDocument;
          import 
            com.itextpdf.kernel.pdf.PdfReader;
          import 
            com.itextpdf.kernel.pdf.canvas.parser.PdfTextExtractor;
          
import 
            java.io.IOException;
          
/** * 把整本 PDF 的可见文本抽出来。 */public class ExtractAllText {
    public static String extract(String pdfPath) throws IOException {        try (PdfDocument pdf = new PdfDocument(new PdfReader(pdfPath))) {            StringBuilder all = new StringBuilder();            int pages = 
            pdf.getNumberOfPages();
                      for (int i = 1; i <= pages; i++) {                String pageText = 
            PdfTextExtractor.getTextFromPage(pdf.getPage(i));
                          
            all.append(
          "----- 第 ").append(i).append(" 页 -----\n");                
            all.append(pageText).append(
          '\n');            }            return 
            all.toString();
                  }    }
    public static void main(String[] args) throws IOException {        String text = extract("
            invoice.pdf"
          );        
            System.out.println(text);
              }}
```

`PdfTextExtractor` 默认用的是基于位置的策略，阅读顺序一般比“按内容流原始顺序”更接近人眼看到的样子。扫描件、纯图片 PDF 抽出来会是空的，那是 OCR 的活，得接 `pdfOCR` 或者别的识别服务。

### 2\. 想控制换行和阅读顺序时，自己上 Strategy

默认抽取不够用时，把 `LocationTextExtractionStrategy` 拿出来更稳。 [9.x](http://9.x/) 里它的分隔符可以定制，多页正则定位（ `RegexBasedLocationExtractionStrategy` ）也修过一波，结果更干净：

```java
import 
            com.itextpdf.kernel.pdf.PdfDocument;
          import 
            com.itextpdf.kernel.pdf.PdfReader;
          import 
            com.itextpdf.kernel.pdf.canvas.parser.PdfCanvasProcessor;
          import 
            com.itextpdf.kernel.pdf.canvas.parser.listener.LocationTextExtractionStrategy;
          
import 
            java.io.IOException;
          
/** * 用位置策略抽取首页文本，适合发票、合同这类版式固定的文件。 */public class ExtractWithStrategy {
    public static String extractFirstPage(String pdfPath) throws IOException {        try (PdfDocument pdf = new PdfDocument(new PdfReader(pdfPath))) {            LocationTextExtractionStrategy strategy = new LocationTextExtractionStrategy();            PdfCanvasProcessor processor = new PdfCanvasProcessor(strategy);            
            processor.processPageContent(pdf.getFirstPage());
                      return 
            strategy.getResultantText();
                  }    }}
```

发票场景里，我通常是：先整页抽文本，再用正则抠 `发票号码` 、 `价税合计` 这些锚点。版式一旦稳定，比上大模型便宜得多。

### 3\. 把页面里的图片另存出来

做回单识别、证件归档时，经常要先把图抠出来再送 OCR：

```java
import 
            com.itextpdf.kernel.pdf.PdfDocument;
          import 
            com.itextpdf.kernel.pdf.PdfPage;
          import 
            com.itextpdf.kernel.pdf.PdfReader;
          import 
            com.itextpdf.kernel.pdf.xobject.PdfImageXObject;
          import 
            com.itextpdf.kernel.pdf.PdfName;
          import 
            com.itextpdf.kernel.pdf.PdfDictionary;
          import 
            com.itextpdf.kernel.pdf.PdfStream;
          
import 
            java.io.IOException;
          import 
            java.nio.file.Files;
          import 
            java.nio.file.Path;
          import 
            java.nio.file.Paths;
          
/** * 遍历每一页资源字典，把嵌入的位图导出成文件。 */public class ExtractImages {
    public static void dump(String pdfPath, String outputDir) throws IOException {        Path dir = 
            Paths.get(outputDir);
                  
            Files.createDirectories(dir);
          
        try (PdfDocument pdf = new PdfDocument(new PdfReader(pdfPath))) {            int seq = 1;            for (int i = 1; i <= 
            pdf.getNumberOfPages();
           i++) {                PdfPage page = 
            pdf.getPage(i);
                          PdfDictionary resources = 
            page.getResources().getPdfObject();
                          PdfDictionary xobjects = 
            resources.getAsDictionary(PdfName.XObject);
                          if (xobjects == null) {                    continue;                }                for (PdfName name : 
            xobjects.keySet())
           {                    PdfStream stream = 
            xobjects.getAsStream(name);
                              if (stream == null || !
            PdfName.Image.equals(stream.getAsName(PdfName.Subtype)))
           {                        continue;                    }                    PdfImageXObject image = new PdfImageXObject(stream);                    String ext = 
            image.identifyImageFileExtension();
                              Path dest = 
            dir.resolve(
          "page-" + i + "-img-" + seq + "." + ext);                    
            Files.write(dest,
           
            image.getImageBytes());
                              seq++;                }            }        }    }}
```

导出后记得看扩展名，JPEG、PNG 最常见；9.7 起 WebP 也能进 PDF，遇到新格式别惊讶。

---

## 五、解析流程长什么样

把上面几段代码串起来，其实就一张很短的流水线。读 PDF 时，iText 不会“理解”业务含义，它只负责把页面内容还原成你能继续处理的原材料。

![图片](assets/iText%209%EF%BC%8CJava%E8%A7%A3%E6%9E%90PDF%E7%A5%9E%E5%99%A8%20%EF%BC%81/63c023d73b5f9cbca72206a4127f87a3_MD5.png)

记住一个习惯就行： **先 `PdfReader` 打开，再包一层 `PdfDocument` ，用完一定要关** 。上面例子里我都写成了 `try-with-resources` ，生产代码请保持这个写法，不然大文件跑批量任务时句柄会漏。

如果文件可能损坏，创建 `PdfReader` 时可以打开非严格模式， [9.x](http://9.x/) 重建 xref 表失败时会给出更明确的原因，排障比以前少猜很多。

---

## 六、写 PDF 也顺手带一笔

解析是入口，很多项目紧接着就要“再生成一份回执 PDF”。最小例子如下：

```java
import 
            com.itextpdf.kernel.pdf.PdfDocument;
          import 
            com.itextpdf.kernel.pdf.PdfWriter;
          import 
            com.itextpdf.layout.Document;
          import 
            com.itextpdf.layout.element.Paragraph;
          import 
            com.itextpdf.kernel.font.PdfFont;
          import 
            com.itextpdf.kernel.font.PdfFontFactory;
          import 
            com.itextpdf.io.font.constants.StandardFonts;
          
import 
            java.io.IOException;
          
/** * 生成一份最简单的 PDF，演示 layout 模块的基本用法。 */public class CreateSimplePdf {
    public static void create(String dest) throws IOException {        PdfFont font = 
            PdfFontFactory.createFont(StandardFonts.HELVETICA);
                  try (PdfWriter writer = new PdfWriter(dest);             PdfDocument pdf = new PdfDocument(writer);             Document doc = new Document(pdf)) {            
            doc.setFont(font);
                      
            doc.add(
          new Paragraph("Hello, iText 9"));            
            doc.add(
          new Paragraph("This PDF was created by Java."));        }    }}
```

要写中文，把 `              StandardFonts.HELVETICA            ` 换成磁盘上的中文字体路径，例如：

```java
PdfFont font = 
            PdfFontFactory.createFont(
                  "C:/Windows/Fonts/
            simsun.ttc,0"
          ,        "Identity-H",        
            PdfFontFactory.EmbeddingStrategy.PREFER_EMBEDDED
          );
```

`Identity-H` 是 Unicode 水平书写，嵌入策略选 `PREFER_EMBEDDED` ，别人电脑没装这个字体也能打开。

---

## 七、几点踩坑提醒

1. **扫描件不是文本。** `PdfTextExtractor` 抽出来是空的，先确认 Acrobat 里能不能选中文字。
2. **中文必须显式指定字体。** 漏了就会缺字、方块、或者直接异常。
3. **加密文档要密码。** `new PdfReader(path, new ReaderProperties().setPassword(...))` ，空密码和用户密码、所有者密码不是一回事。
4. **AGPL 不是“随便用”。** 内部工具、开源项目没问题；要闭源商用，走商业许可。
5. **从 8 升 9 先看 Breaking Changes。** 符合性、签名、图层相关 API 有整理，照着官方迁移说明改，比对着编译错误一个个猜快。

[2026年，锋哥又开始收Java+AI大模型编程学员了！目前活动，送AI编程+Python+AI大模型VIP。。](https://mp.weixin.qq.com/s?__biz=MzIxNTAwNjA4OQ==&mid=2247571915&idx=1&sn=6deb7659b60dc4dc3647a22babe9aad3&scene=21#wechat_redirect)