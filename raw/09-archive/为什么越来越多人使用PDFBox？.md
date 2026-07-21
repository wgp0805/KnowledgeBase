---
title: "为什么越来越多人使用PDFBox？"
source: "https://mp.weixin.qq.com/s/PkajVxZcdDXlWZW7UhjuTg"
---
苏三 苏三说技术 *2026年7月21日 08:59*

## 大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

## 前言

最近有球友问：三哥，解析PDF用哪个工具比较好？

市面上主流的Java PDF处理库，大概分成三类：iText（商业授权，AGPL对商业不友好）、OpenPDF（iText 4的分支，LGPL/MPL协议）、以及今天要聊的 **Apache PDFBox（Apache 2.0协议，对商业最友好）** 。

PDFBox是目前 **唯一一个由Apache基金会维护** 的Java PDF处理库，功能覆盖从文本提取到数字签名的全场景。

截至2026年7月，PDFBox的最新版本已经更新到 **3.0.8** 。

今天这篇文章，我就把PDFBox从安装到实战、从底层原理到性能调优，从头到尾给你拆解一遍。

希望对你会有所帮助。

## 一、先搞清楚：PDFBox到底是什么？

### 1.1 一句话说清

**Apache PDFBox是一个开源的Java库，专门用于处理PDF文档** 。

它允许你：

- **创建** 全新的PDF文件
- **编辑** 现有的PDF文档
- **提取** PDF中的文本、图片和元数据
- **合并、拆分、加密、解密、签名** PDF文件

简单说，只要是跟PDF相关的事，PDFBox基本都能干。

### 1.2 为什么选PDFBox？

在Java生态里，PDF处理库其实不少。但PDFBox有几个独特的优势：

**第一，Apache 2.0协议，对商业最友好。** iText从7.0开始采用AGPL协议，如果你的项目是商业闭源软件，要么花钱买授权，要么开源全部代码。而PDFBox采用Apache 2.0协议， **允许自由使用、修改和分发，甚至用于商业闭源产品** 。

**第二，Apache顶级项目，社区活跃。** PDFBox是Apache软件基金会的顶级项目，有持续的版本迭代和社区支持。2026年3月至今，PDFBox已经连续发布了3.0.6、3.0.7和3.0.8等多个版本。

**第三，“一站式”解决方案。** 从最简单的文本提取到复杂的数字签名，从基本的文档合并到高级操作，PDFBox几乎涵盖了PDF处理的所有场景。

## 二、环境搭建：5分钟跑起来

### 2.1 添加依赖

PDFBox [3.x需要](http://3.xn--x-hj1d638a/) `Java 8+` 环境。

如果你的项目用的是Maven：

```
<dependency>
    <groupId>
            org.apache.pdfbox
          </groupId>
    <artifactId>pdfbox</artifactId>
    <version>3.0.8</version>
</dependency>
```

如果用的是Gradle：

```
implementation '
            org.apache.pdfbox:pdfbox:3.0.8'
```

**版本选择建议** ：PDFBox [3.x是目前最常用的Java](http://3.xn--xjava-6t6h152e9ro1wbq41enedhpb/) PDF处理起点。

截至2026年7月，最新版本是 **3.0.8** 。

如果你的项目还在用 [2.x，建议升级到3.x——性能更好、API更规范。](http://2.xn--x,3-9j2ew3co61b3j6ci1v.xn--xapi-586aa356zom3exsmp6pfa7801fvrfup0a./)

### 2.2 第一个程序：提取PDF文本

```
import 
            org.apache.pdfbox.Loader;
          
import 
            org.apache.pdfbox.pdmodel.PDDocument;
          
import 
            org.apache.pdfbox.text.PDFTextStripper;
          
import 
            java.io.File;
          
import 
            java.io.IOException;
          

public class ExtractText {
    public static void main(String[] args) throws IOException {
        File file = new File("
            sample.pdf"
          );
        // PDFBox 
            3.x
           使用 
            Loader.loadPDF()，不再是
           
            PDDocument.load()
          
        try (PDDocument document = 
            Loader.loadPDF(file))
           {
            PDFTextStripper stripper = new PDFTextStripper();
            String text = 
            stripper.getText(document);
          
            
            System.out.println(text);
          
        }
    }
}
```

**关键注意** ：PDFBox 3.0移除了 `              PDDocument.load()            ` 方法，必须使用 `              Loader.loadPDF()            ` 。

**提取指定页面范围的文本** ：

```
try (PDDocument document = 
            Loader.loadPDF(
          new File("
            sample.pdf"
          ))) {
    PDFTextStripper stripper = new PDFTextStripper();
    
            stripper.setStartPage(
          2);  // 从第2页开始
    
            stripper.setEndPage(
          4);    // 到第4页结束
    String text = 
            stripper.getText(document);
          
    
            System.out.println(text);
          
}
```

## 三、核心操作：从入门到进阶

### 3.1 创建PDF文档

```
import 
            org.apache.pdfbox.pdmodel.PDDocument;
          
import 
            org.apache.pdfbox.pdmodel.PDPage;
          
import 
            org.apache.pdfbox.pdmodel.PDPageContentStream;
          
import 
            org.apache.pdfbox.pdmodel.font.PDType1Font;
          

public class CreatePDF {
    public static void main(String[] args) {
        try (PDDocument document = new PDDocument()) {
            // 添加一个空白页
            PDPage page = new PDPage();
            
            document.addPage(page);
          
            
            // 创建内容流
            PDPageContentStream contentStream = new PDPageContentStream(document, page);
            
            // 设置字体和大小
            
            contentStream.setFont(PDType1Font.HELVETICA_BOLD,
           12);
            
            contentStream.beginText();
          
            
            contentStream.newLineAtOffset(
          100, 700);  // 坐标：距离左侧100，距离底部700
            
            contentStream.showText(
          "Hello, PDFBox!");
            
            contentStream.endText();
          
            
            contentStream.close();
          
            
            
            document.save(
          "
            HelloPDFBox.pdf"
          );
        } catch (Exception e) {
            
            e.printStackTrace();
          
        }
    }
}
```

**坐标系统说明** ：PDF的坐标原点在 **页面左下角** ，X轴向右为正，Y轴向上为正。这与Swing等GUI库的坐标系统（左上角为原点）正好相反，新手容易踩坑。

**处理多行文本** ：

```
contentStream.setLeading(
14.5f);  // 设置行间距

  contentStream.showText(
"第一行文本");

  contentStream.newLine();

  contentStream.showText(
"第二行文本");
```

### 3.2 提取图片

```
import 
            org.apache.pdfbox.pdmodel.PDDocument;
          
import 
            org.apache.pdfbox.pdmodel.PDPage;
          
import 
            org.apache.pdfbox.pdmodel.PDResources;
          
import 
            org.apache.pdfbox.pdmodel.common.PDRectangle;
          
import 
            org.apache.pdfbox.pdmodel.graphics.image.PDImageXObject;
          

public class ExtractImages {
    public static void main(String[] args) throws IOException {
        try (PDDocument document = 
            Loader.loadPDF(
          new File("
            sample.pdf"
          ))) {
            for (int pageIndex = 0; pageIndex < 
            document.getNumberOfPages();
           pageIndex++) {
                PDPage page = 
            document.getPage(pageIndex);
          
                PDResources resources = 
            page.getResources();
          
                
                // 遍历页面中的所有资源
                for (COSName name : 
            resources.getXObjectNames())
           {
                    if (
            resources.isImageXObject(name))
           {
                        PDImageXObject image = (PDImageXObject) 
            resources.getXObject(name);
          
                        // 
            image.getImage()
           可以获取 BufferedImage 对象
                        
            System.out.println(
          "找到图片：" + 
            name.getName());
          
                    }
                }
            }
        }
    }
}
```

### 3.3 合并PDF文件

PDFBox提供了 `PDFMergerUtility` 工具类来合并多个PDF：

```
import 
            org.apache.pdfbox.io.MemoryUsageSetting;
          
import 
            org.apache.pdfbox.multipdf.PDFMergerUtility;
          

public class MergePDFs {
    public static void main(String[] args) throws IOException {
        PDFMergerUtility merger = new PDFMergerUtility();
        
        // 添加源文件
        
            merger.addSource(
          new File("
            file1.pdf"
          ));
        
            merger.addSource(
          new File("
            file2.pdf"
          ));
        
            merger.addSource(
          new File("
            file3.pdf"
          ));
        
        // 设置目标文件
        
            merger.setDestinationFileName(
          "
            merged.pdf"
          );
        
        // 执行合并
        
            merger.mergeDocuments(MemoryUsageSetting.setupMainMemoryOnly());
          
    }
}
```

### 3.4 加密PDF

PDF加密需要 **两个密码** ：用户密码（打开查看，权限受限）和所有者密码（完全访问权限）：

```
import 
            org.apache.pdfbox.pdmodel.PDDocument;
          
import 
            org.apache.pdfbox.pdmodel.encryption.AccessPermission;
          
import 
            org.apache.pdfbox.pdmodel.encryption.StandardProtectionPolicy;
          

public class EncryptPDF {
    public static void main(String[] args) throws IOException {
        try (PDDocument document = 
            Loader.loadPDF(
          new File("
            sample.pdf"
          ))) {
            AccessPermission ap = new AccessPermission();
            // 允许打印，但不允许修改
            
            ap.setCanPrint(
          true);
            
            ap.setCanModify(
          false);
            
            StandardProtectionPolicy spp = new StandardProtectionPolicy(
                "user_password",  // 用户密码
                "owner_password", // 所有者密码
                ap
            );
            
            spp.setEncryptionKeyLength(
          128);
            
            
            document.protect(spp);
          
            
            document.save(
          "
            encrypted.pdf"
          );
        }
    }
}
```

### 3.5 填充PDF表单

PDFBox支持操作AcroForm表单字段：

```
import 
            org.apache.pdfbox.pdmodel.PDDocument;
          
import 
            org.apache.pdfbox.pdmodel.interactive.form.PDAcroForm;
          
import 
            org.apache.pdfbox.pdmodel.interactive.form.PDTextField;
          

public class FillForm {
    public static void main(String[] args) throws IOException {
        try (PDDocument document = 
            Loader.loadPDF(
          new File("
            form.pdf"
          ))) {
            PDAcroForm acroForm = 
            document.getDocumentCatalog().getAcroForm();
          
            
            // 获取表单字段并填充
            PDTextField nameField = (PDTextField) 
            acroForm.getField(
          "name");
            if (nameField != null) {
                
            nameField.setValue(
          "张三");
            }
            
            PDTextField emailField = (PDTextField) 
            acroForm.getField(
          "email");
            if (emailField != null) {
                
            emailField.setValue(
          "zhangsan@
            example.com"
          );
            }
            
            
            document.save(
          "
            filled_form.pdf"
          );
        }
    }
}
```

## 四、底层原理

> 有些小伙伴可能会好奇：“PDFBox到底是怎么把一团乱码的PDF文件变成可读的文本和图片的？”

理解底层原理，能帮你更好地理解PDFBox的能力边界和性能瓶颈。

### 4.1 PDF文档的物理结构

PDF文件本质上是一个 **字节序列** 。

它的物理结构分为四个部分：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8PDFBox%EF%BC%9F/27feaa027d21c5f1638bd72a3ae9c9bd_MD5.jpg)

- **文件头** ：位于文档开头，包含PDF版本信息（如 `%             PDF-1.7           ` ）
- **文件体** ：存储所有PDF对象——页面、图像、字体、注释等
- **交叉引用表** ：提供快速定位文件体内对象位置的方法
- **文件尾** ：包含指向交叉引用表和文档根对象的指针

### 4.2 PDFBox的双层架构

PDFBox采用 **双层架构** 来分离底层PDF结构和高层业务语义：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8PDFBox%EF%BC%9F/90071c4ea30cf836e5126a603a92d3a5_MD5.jpg)

**COS层（底层对象层）** ：直接映射PDF文件中的基本对象——字典（COSDictionary）、数组（COSArray）、流（COSStream）等。你可以通过COS层访问PDF文件的任何底层细节。

**PD层（高层语义层）** ：在COS层之上封装了面向开发者的友好API—— `PDDocument` 代表整个文档， `PDPage` 代表一页， `PDPageContentStream` 代表内容流。

这种分层设计的核心价值在于： **你可以通过PD层快速完成常规操作，遇到复杂需求时又能随时下沉到COS层获取完全控制权** 。

### 4.3 内容处理的三层流水线

PDFBox的内容处理架构分为三个层次：

**第一层：基础处理层（PDFStreamEngine）**

这是最底层。它负责解析内容流为Token序列，将操作分发给注册的处理器，维护图形状态栈，管理资源。

简单说，它把PDF的“二进制指令流”翻译成“可执行的操作序列”。

**第二层：图形抽象层（PDFGraphicsStreamEngine）**

这层定义了图形操作的抽象方法——路径构建、填充、描边、绘制图像。它不关心“怎么画”，只定义“画什么”。

**第三层：实现层（PageDrawer、PDFTextStripper等）**

这层提供了具体的实现。 `PageDrawer` 负责渲染到Graphics2D， `PDFTextStripper` 负责提取文本。

以提取文本为例， `PDFTextStripper` 就是通过重写 `showGlyph()` 方法来收集字符的位置信息，从而实现文本提取。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E4%BD%BF%E7%94%A8PDFBox%EF%BC%9F/dd358a3f3c57cb9c361d1e18a2ae9c48_MD5.jpg)

这种分层设计让PDFBox具有极高的 **可扩展性** ——你可以继承 `PDFStreamEngine` 来实现自定义的行为，比如内容分析或自定义渲染后端。

## 五、常见问题与避坑指南

### 5.1 PDFBox 2.x → 3.x迁移要点

如果你从PDFBox [2.x升级到3.x，这几个变化必须注意：](http://2.x升级到3.x，这几个变化必须注意：)

**变化一： [PDDocument.load()被移除](http://pddocument.xn--load\(\)-8y1p535gn2z/)**

```
// PDFBox 
            2.x
          
PDDocument document = 
            PDDocument.load(
          new File("
            sample.pdf"
          ));

// PDFBox 
            3.x
          
PDDocument document = 
            Loader.loadPDF(
          new File("
            sample.pdf"
          ));
```

**变化二：IO模块重构**

PDFBox 3.0引入了全新的IO模块和Loader类，这是3.0版本中变化最大的部分。

### 5.2 中文显示问题

PDFBox默认的 `PDType1Font` 不支持中文。要用中文，你需要自己加载中文字体：

```
// 加载中文字体
PDType0Font font = 
            PDType0Font.load(document,
           new File("
            simsun.ttf"
          ));

            contentStream.setFont(font,
           12);
```

### 5.3 大文件性能问题

PDFBox在处理大型或复杂的PDF文件时，性能可能比其他PDF库慢一些。优化建议：

- 使用 `              Loader.loadPDF()            ` 时指定 `MemoryUsageSetting` 来控制内存使用
- 对于超大文件，考虑分页处理
- 使用 `try-with-resources` 确保资源及时释放

## 六、优缺点

### 优点

**1\. Apache 2.0协议，商业友好** 可以自由使用、修改和分发，甚至用于商业闭源产品。

**2\. 功能全面，“一站式”解决方案** 从文本提取到数字签名，从文档合并到OCR集成，覆盖几乎所有PDF处理场景。

**3\. Apache顶级项目，社区活跃** 持续的版本迭代，2026年已连续发布多个版本。

**4\. API设计直观** 即使没有PDF处理经验的开发者也能快速上手。

**5\. 命令行工具** PDFBox还包含一套命令行工具，可以执行常见的PDF处理任务。

**6\. 纯Java实现** 可以在任何支持Java的平台上运行，无需依赖特定操作系统。

### 缺点

**1\. 大文件性能偏弱** 处理非常大的或结构复杂的PDF文件时，速度可能不如商业库。

**2\. 表格提取不是原生功能** PDFBox提取表格需要结合Tabula-java等工具。

**3\. 中文支持需要额外配置** 默认字体不支持中文，需要手动加载中文字体。

**4\. 3.0版本有破坏性变更** 从 [2.x升级到3.x需要注意API变化。](http://2.xn--x3-rh5c94bk04k.xn--xapi-ok0g63br28civvs02deh2a./)

## 七、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **文档管理系统** | ✅✅✅ 强烈推荐 | 创建、编辑、提取PDF内容 |
| **报表自动生成** | ✅✅✅ 强烈推荐 | 动态生成包含图表和表格的复杂PDF报表 |
| **合同/发票解析** | ✅✅✅ 强烈推荐 | 提取结构化数据，Apache 2.0协议商业友好 |
| **电子书阅读器** | ✅✅ 推荐 | 支持文本搜索和内容提取 |
| **数字签名** | ✅✅ 推荐 | PDFBox提供符合PDF安全规范的数字签名 |
| **PDF加密/解密** | ✅✅ 推荐 | 支持用户密码和所有者密码双重加密 |
| **PDF合并/拆分** | ✅✅ 推荐 | `PDFMergerUtility`  工具类 |

## 八、写在最后

Apache PDFBox作为一个Apache基金会的顶级项目，用 **Apache 2.0协议** 给了商业开发者最大的自由度——你可以免费使用、自由修改，甚至用于商业闭源产品。

它的功能覆盖从 **创建、编辑、提取到加密、签名、合并** 的几乎所有PDF操作。而且它的API设计直观，即使没有PDF处理经验的开发者也能快速上手。

当然，PDFBox也不是银弹。

处理超大文件时性能可能不如商业库，表格提取需要借助额外工具。

但对于绝大多数PDF处理需求，PDFBox已经足够强大。

**我的建议是** ：如果你的项目需要PDF处理能力， **先花一个下午把PDFBox跑一遍**

。感受一下“免费、开源、功能全面”的PDF处理体验——你会发现，很多事情根本不需要花钱。

开源地址

- **GitHub** ： [https://github.com/apache/pdfbox](https://github.com/apache/pdfbox)
- **官方文档** ： [https://pdfbox.apache.org](https://pdfbox.apache.org/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)