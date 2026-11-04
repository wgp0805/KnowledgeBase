---
title: "ZXing"
type: entity
tags: [开源库, 二维码, Java, Android, 条形码]
sources: [raw/09-archive/为什么越来越多人用 ZXing？.md, raw/09-archive/2026-11-01 - ZXing 3.5 （ Java版 ） 到底有多强 ？.md]
last_updated: 2026-11-02
---

## 定义
ZXing（发音 "zebra crossing"，斑马线）是开源的多格式 1D/2D 条码图像处理库，Java 实现并移植到多种语言，既能生成也能识别几乎所有主流条形码/二维码，是全球二维码识别的底层标准之一。

## 关键信息

### 出身与协议
Google 员工 "20% 时间" 副业项目，2007 年 11 月开源，Apache 2.0 协议，GitHub 约 34,000 Star。

### 包结构（Java 版）
- **`core`**：只管码本身——把文字编成矩阵、把黑白图解成字符串。不认 JPG/PNG，也不依赖 AWT
- **`javase`**：负责与 `BufferedImage` 对接，命令行小工具也放在这里
- 只在内存里摆矩阵、自己负责画图时，第二个包可以不引

### 支持格式
- **二维码**：QR Code、Aztec、Data Matrix、PDF417、MaxiCode
- **一维码**：EAN-8、EAN-13、UPC-A、UPC-E、Code 39、Code 93、Code 128、ITF（交叉二五码）、Codabar、RSS-14、RSS Expanded

### 识别流程（四步）
1. **亮度图**：彩色或灰度收成 0-255 亮度（0 黑、255 白）
2. **二值化**：照片用 `HybridBinarizer` 比较稳；图特别干净时可试 `GlobalHistogramBinarizer`
3. **定位与解码**：用 `POSSIBLE_FORMATS` 收窄码制（面单场景基本是 Code 128 和 QR），速度和误判都会改善
4. **解析**：`TRY_HARDER` 会多花时间找难图，适合模糊、偏转的照片；干净的电子码不必每次开

### 版本演进（3.5.x）
- **3.5.0**（2022-05）：Aztec/PDF417/Data Matrix 解码修过一轮，加更省容量的 minimal 编码模式
- **3.5.1-3.5.3**：继续补边界（极端图不再死盯很久、Code 128 去掉过死的长度限制、GS1 按 2023 规范更新、RSS Expanded 减少误识别）
- **3.5.4**（最新，无新码制，全是「以前会踩、现在少踩」）：
  - 新增 `GrayscaleLuminanceSource`：灰度图可直接送进去（构造方法 `GrayscaleLuminanceSource(width, height, pixels)`）；`RGBLuminanceSource` 改为其子类并补上逆时针 90 度旋转；彩色像素先校验数组长度是否等于宽乘高
  - `QRCodeMultiReader` 保留 `SYMBOLOGY_IDENTIFIER` 符号标识，与单个 `QRCodeReader` 对齐
  - PDF417：`Compaction.TEXT` 只接受码点 0-127，超出抛明确异常；修复「指定行列范围时内容放得下却报 Unable to fit message in columns」
  - RSS Expanded 去掉一处低效容器操作；ITF 放宽 3 倍模块宽度误差上限
  - 二维码模块数估算改为「合法边长必须除以 4 余 1」，差 2 时向下减 2；三个定位角点构成等腰直角三角形时畸变计算修正
  - 邮箱解析格式检查收紧

### 核心 API
- 生成：`MultiFormatWriter.encode()`（编码 + 纠错 + 矩阵填充）
- 识别：`MultiFormatReader.decode()`（定位探测图形 + 校正 + 解码）
- 纠错级别：L 7% / M 15% / Q 25% / H 30%；级别越高越抗造但尺寸越大
- 典型工作两头：给一段文字画二维码/条码；或已有一张图，告诉你里面写了什么、是哪种码、在图的哪个位置

### 依赖坐标
```xml
<dependency>
  <groupId>com.google.zxing</groupId>
  <artifactId>core</artifactId>
  <version>3.5.4</version>
</dependency>
<dependency>
  <groupId>com.google.zxing</groupId>
  <artifactId>javase</artifactId>
  <version>3.5.4</version>
</dependency>
```
按 Java 8 使用即可；版本号三个包保持一致，避免 core 和 javase 各写各的。

### 工程注意
- **静区（margin）不要设成 0**：码四周那圈空白叫静区，裁掉后生成成功但识别经常失败
- 纠错用 M（脏一点、褶一点还有机会读回来）
- 字符集指定 UTF-8，中文才不会在生成阶段就乱码
- 明确指定 `Compaction.TEXT` 时内容出现中文会直接失败，改用自动/字节压缩
- 定位：ZXing Java 版适合「图已经在手里」的服务端场景；手机镜头实时扫，系统扫码和 ML Kit 往往更省事（对焦、旋转、帧率要另写）

### 对比 ZBar/OpenCV
检测速度最快、集成难度最低（纯 Java 零依赖、不需 JNI）、生态最成熟；小尺寸二维码识别率一般、反色码无法识别需预处理、严重扭曲场景不如 ZBar。

### Android 架构
提供相机预览、扫描框、解码线程完整模块，解码放独立线程经 Handler 通信避免 ANR。

### 生态地位
微信、支付宝、淘宝、美团等扫码 App 底层，Android 系统默认扫码方案。

## 关联连接
- [[摘要-zxing-3.5-java版]] — 最新来源
- [[摘要-zxing条码库]] — 早期来源
- [[Java]] — 实现语言
- Android — 主战场平台（系统默认扫码方案）
- [[锋哥]] — 最新来源作者
