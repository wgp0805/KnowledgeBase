---
title: "为什么越来越多人用 ZXing？"
source: "https://mp.weixin.qq.com/s/bDGSLq3lBubQFE1UKzw1rw"
---
苏三 苏三说技术 *2026年10月9日 08:39*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

不知道你有没有做过支付系统，收银台一般有“主扫”和“被扫”两种模式：主扫是用户扫商家的静态码，被扫是商家用扫码枪扫用户的付款码。

你手机里几乎所有的扫码App——微信、支付宝、淘宝、美团——底层的二维码识别能力，都源自一个叫ZXing的开源库。

Android系统的扫码功能，默认用的也是它。

ZXing在GitHub上有 **34,000颗Star** ，Apache 2.0协议开源，从2007年发布至今，已经快19年了。

它最初只是Google员工的一个“20%时间”副业项目，后来却成了全球二维码识别的底层标准。

今天这篇文章，我就把ZXing为什么越来越多人用的原因，从头到尾给你拆解一遍。

希望对你会有所帮助。

## 一、ZXing到底是什么？

ZXing的发音是“zebra crossing”（斑马线），是一个开源的、多格式的1D/2D条码图像处理库，用Java实现，并且被移植到了其他多种语言。

**一句话说清：ZXing是一个能生成和识别几乎所有主流条形码/二维码的Java库。**

它支持的格式包括：

| 类型 | 格式 |
| --- | --- |
| **二维码** | QR Code、Data Matrix、Aztec、MaxiCode、PDF417 |
| **一维条码** | UPC-A、UPC-E、EAN-8、EAN-13、Code 39、Code 93、Code 128、ITF、Codabar、RSS-14、RSS Expanded |

**这意味着什么？**

不管你面对的是微信支付码、商品条形码、还是机票上的PDF417码，ZXing都能处理。

## 二、ZXing的“出身”

> 有些小伙伴可能会说：“ZXing这么好用，肯定是哪个大公司的重点产品吧？”

**恰恰相反。**

ZXing最初是Google员工的“20%时间”项目。

2007年11月，Google开发者博客上有一篇很简短的公告：“今天我想宣布‘ZXing’项目，一个开源的、Java的、多格式的1D/2D条码阅读器。

这个项目始于一个20%时间的尝试，目前还不完整，所以把它开源出来有点实验性质。

它还不是‘史上最好的条码阅读器’，但看起来还不错。”

**一个副业项目，却成了行业标准。**

这背后的逻辑很值得琢磨。

## 三、一张图看懂ZXing的编解码流程

ZXing的核心能力分两块： **生成二维码** 和 **识别二维码** 。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20ZXing%EF%BC%9F/e136843408a270b5c20ffa2a3fcad9ee_MD5.jpg)

**生成的核心是“编码+纠错”** ：把文本转成二进制，加入纠错码，按二维码标准填进矩阵，最后渲染成图片。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20ZXing%EF%BC%9F/cdcd867761853bbc2866a7209625c8a4_MD5.jpg)**识别的核心是“定位+解码”** ：先找到二维码的探测图形（那三个角落的方块），校正图像，然后逐位解码。

## 四、代码实战

> 有些小伙伴可能会说：“说了这么多，到底怎么用？”

ZXing的API设计极其简洁。 **生成二维码，核心就两行** ：

### 4.1 生成二维码

```
<dependency>
    <groupId>
            com.google.zxing
          </groupId>
    <artifactId>core</artifactId>
    <version>3.5.3</version>
</dependency>
<dependency>
    <groupId>
            com.google.zxing
          </groupId>
    <artifactId>javase</artifactId>
    <version>3.5.3</version>
</dependency>
```
```
import 
            com.google.zxing.BarcodeFormat;
          
import 
            com.google.zxing.MultiFormatWriter;
          
import 
            com.google.zxing.client.j2se.MatrixToImageWriter;
          
import 
            com.google.zxing.common.BitMatrix;
          
import 
            java.nio.file.Path;
          
import 
            java.nio.file.Paths;
          

publicclass QRCodeGenerator {
    public static void main(String[] args) throws Exception {
        String data = "
            https://www.example.com"
          ;
        String path = "
            QRCode.png"
          ;
        
        // 核心两行：编码 + 写文件
        BitMatrix bitMatrix = new MultiFormatWriter()
            .encode(data, 
            BarcodeFormat.QR_CODE,
           200, 200);
        
            MatrixToImageWriter.writeToPath(bitMatrix,
           "PNG", 
            Paths.get(path));
          
        
        
            System.out.println(
          "二维码生成成功");
    }
}
```

            **`              MultiFormatWriter.encode()            `** 做了所有脏活累活：数据编码、纠错码计算、矩阵填充、探测图形添加。你只需要告诉它“编码什么内容、用什么格式、多大尺寸”。

### 4.2 识别二维码

```
import 
            com.google.zxing.BinaryBitmap;
          
import 
            com.google.zxing.MultiFormatReader;
          
import 
            com.google.zxing.Result;
          
import 
            com.google.zxing.client.j2se.BufferedImageLuminanceSource;
          
import 
            com.google.zxing.common.HybridBinarizer;
          
import 
            javax.imageio.ImageIO;
          
import 
            java.io.File;
          

publicclass QRCodeReader {
    public static void main(String[] args) throws Exception {
        // 读取图片
        var image = 
            ImageIO.read(
          new File("
            QRCode.png"
          ));
        
        // 构建二进制位图
        var source = new BufferedImageLuminanceSource(image);
        var bitmap = new BinaryBitmap(new HybridBinarizer(source));
        
        // 解码
        Result result = new MultiFormatReader().decode(bitmap);
        
            System.out.println(
          "识别结果：" + 
            result.getText());
          
    }
}
```

            **`              MultiFormatReader.decode()            `** 是识别的核心入口。它会自动定位二维码、校正图像、解码并纠错，返回识别结果。

### 4.3 带纠错级别的生成（生产环境推荐）

```
import 
            com.google.zxing.EncodeHintType;
          
import 
            com.google.zxing.qrcode.decoder.ErrorCorrectionLevel;
          
import 
            java.util.HashMap;
          
import 
            java.util.Map;
          

Map<EncodeHintType, Object> hints = new HashMap<>();
// H级别：可纠正30%的错误，适合打印在易磨损的表面上

            hints.put(EncodeHintType.ERROR_CORRECTION,
           
            ErrorCorrectionLevel.H);
          
// 设置字符集，避免中文乱码

            hints.put(EncodeHintType.CHARACTER_SET,
           "UTF-8");

BitMatrix bitMatrix = new MultiFormatWriter()
    .encode(data, 
            BarcodeFormat.QR_CODE,
           300, 300, hints);
```

**纠错级别说明** ：L（7%）、M（15%）、Q（25%）、H（30%）。级别越高，二维码越“抗造”，但尺寸也越大。

## 五、ZXing在Android中的架构

> 有些小伙伴可能会说：“ZXing是Java SE的库，Android能用吗？”

**Android才是ZXing的主战场之一。**

微信、支付宝的扫码功能，底层都是ZXing。

ZXing提供了专门的Android客户端模块，包含完整的相机预览、扫描框、解码线程。

Android端的核心流程是：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20ZXing%EF%BC%9F/f0622c97fca3f87f17024263478cf9af_MD5.jpg)

**关键设计** ：解码放在 **独立的线程** 中执行，通过Handler传递消息。

因为解码是耗时操作，放在主线程会触发ANR。

## 六、ZXing vs 其他方案

| 对比维度 | ZXing | ZBar | OpenCV |
| --- | --- | --- | --- |
| **语言** | Java | C | C++ |
| **识别速度** | **最快** | 中等 | 最慢 |
| **小尺寸二维码** | 一般 | 较好 | **最好** |
| **模糊/扭曲容错** | **较好** | 较好 | 一般 |
| **集成难度** | **极低** | 低 | 高 |
| **生态成熟度** | **最成熟** | 一般 | 好 |

**实测数据** ：在检测速度上， **ZXing是最快的** ，OpenCV最慢。

在识别准确率上，对于标准的、清晰的二维码，ZXing和ZBar表现接近；对于小尺寸或低分辨率的二维码，OpenCV反而更好。

**ZXing的核心优势不是“识别率最高”，而是“综合体验最好”** ：纯Java实现、零依赖、API简洁、Android原生支持、Apache 2.0协议。

## 七、优缺点

### ZXing的优点

**1\. 零依赖，纯Java实现** 不需要任何本地库，不需要JNI，直接引入 `core` 和 `javase` 两个jar包就能用。

**2\. API极简** 生成二维码两行代码，识别二维码核心一行代码。

**3\. 多格式支持** 支持几乎所有主流的一维码和二维码格式，不仅仅是QR Code。

**4\. Android原生支持** 提供了完整的Android客户端模块，相机预览、扫描框、解码线程全部封装好了。

**5\. 生态成熟** 从2007年至今，近19年的迭代，GitHub 34,000 Star，Apache 2.0协议。

**6\. 识别速度最快** 在主流开源库中，ZXing的检测速度是最快的。

### ZXing的缺点

**1\. 小尺寸二维码识别率一般** 对于模块尺寸小于3像素的二维码，识别率会明显下降，不如OpenCV。

**2\. 反色二维码无法识别** ZXing的识别逻辑默认是“黑底白块”，如果二维码是反色的（白底黑块），它识别不了。这是社区反馈最多的坑之一。

**3\. 复杂扭曲场景不如ZBar** 对于严重扭曲、遮挡的二维码，ZBar的纠错能力更强。

## 八、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **支付系统二维码生成** | ✅✅✅ 强烈推荐 | 几行代码搞定，稳定可靠 |
| **Android扫码功能** | ✅✅✅ 强烈推荐 | 原生支持，微信/支付宝同款方案 |
| **商品条形码生成** | ✅✅✅ 强烈推荐 | 支持EAN、UPC、Code 128等 |
| **电子票务/优惠券** | ✅✅✅ 强烈推荐 | 生成二维码作为凭证 |
| **需要识别反色二维码** | ⚠️ 需处理 | 需要手动做图像反色预处理 |
| **极小尺寸二维码识别** | ⚠️ 需评估 | OpenCV可能更合适 |
| **严重扭曲/遮挡的二维码** | ⚠️ 需评估 | ZBar纠错能力更强 |

## 九、写在最后

回到最初的问题： **为什么越来越多人用ZXing？**

答案不复杂—— **因为它把一个复杂的问题，变成了两行代码。**

二维码的生成和识别，涉及数据编码、纠错算法、图像处理、定位算法——每一个都是硬核的计算机视觉问题。

ZXing把所有这些复杂性封装在一个 `encode()` 和一个 `decode()` 后面。

**它快不是因为它比OpenCV更“聪明”，它快是因为它的定位算法和浮点运算优化做得更早、更成熟。**

在标准清晰二维码的场景下，ZXing就是最快的。

**它稳不是因为它从不出错，它稳是因为它被验证了19年。**

你的微信扫码、支付宝付款、淘宝商品查询——这些每天几十亿次的调用，都在用ZXing。

一个经过如此大规模验证的库，稳定性是刻在骨子里的。

当然，ZXing也有短板——反色二维码不识别、小尺寸识别率一般。

但这些都可以通过预处理解决，而ZXing的简洁性和生态成熟度，是其他方案很难替代的。

开源地址：

- **GitHub** ： [https://github.com/zxing/zxing](https://github.com/zxing/zxing)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)