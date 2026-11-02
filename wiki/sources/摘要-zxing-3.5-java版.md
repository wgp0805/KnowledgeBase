---
title: "摘要-zxing-3.5-java版"
type: source
tags: [来源, ZXing, 二维码, Java, 条形码]
sources: [raw/01-articles/2026-11-01 - ZXing 3.5 （ Java版 ） 到底有多强 ？.md]
last_updated: 2026-11-02
---

## 核心摘要

「java1234 / 锋哥」拆解 ZXing 3.5.4（Java 版）的能力与版本变更。ZXing 使用时只需引两个包：`core`（只管码本身——文字编成矩阵、黑白图解成字符串，不依赖 AWT）与 `javase`（对接 `BufferedImage` + 命令行小工具）；只在内存里摆矩阵、自己负责画图时可只引 `core`。

业务代码识别二维码的四步：

1. **亮度图**：彩色或灰度收成 0-255 亮度值（0 黑，255 白）
2. **二值化**：决定每个点算黑还是白；照片用 `HybridBinarizer` 比较稳，图特别干净时可试 `GlobalHistogramBinarizer`
3. **定位与解码**：用 `POSSIBLE_FORMATS` 收窄码制（如面单场景基本是 Code 128 和 QR），速度和误判都会改善
4. **解析**：`TRY_HARDER` 会多花时间找难图，适合模糊、偏转的照片

覆盖码制：QR Code、Aztec、Data Matrix、PDF417、MaxiCode、EAN-8/13、UPC-A/E、Code 39/93/128、ITF、Codabar、RSS-14、RSS Expanded。

版本演进：3.5.0（2022-05）修了 Aztec/PDF417/Data Matrix 解码并加入 minimal 编码模式；3.5.1-3.5.3 继续补边界；3.5.4 无新码制，重点修复：

- 新增 `GrayscaleLuminanceSource`，灰度图可直接送进去（构造方法 `GrayscaleLuminanceSource(width, height, pixels)`）；`RGBLuminanceSource` 改为其子类并补上逆时针 90 度旋转；彩色像素先校验数组长度是否等于宽乘高
- `QRCodeMultiReader` 保留 `SYMBOLOGY_IDENTIFIER` 符号标识，与单个 `QRCodeReader` 对齐
- PDF417：`Compaction.TEXT` 只接受码点 0-127，超出抛明确异常；修复「指定行列范围时内容放得下却报 Unable to fit message in columns」
- RSS Expanded 去掉一处低效容器操作；ITF 放宽 3 倍模块宽度误差上限；二维码模块数估算改为合法边长必须「除以 4 余 1」，差 2 时向下减 2
- 邮箱解析格式检查收紧

工程注意：静区（margin）不要为了图小设成 0，裁掉后识别经常失败；纠错用 M（脏一点、褶一点还有机会读回来）；字符集指定 UTF-8，中文才不会在生成阶段乱码。

## 关联连接
- [[ZXing]] — 被介绍的库
- [[摘要-zxing条码库]] — 更早的同主题来源
- [[Java]] — 实现语言
