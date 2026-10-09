---
title: "ZXing"
type: entity
tags: [开源库, 二维码, Java, Android]
sources: [raw/01-articles/为什么越来越多人用 ZXing？.md]
last_updated: 2026-10-09
---

## 定义
ZXing（发音 "zebra crossing"，斑马线）是开源的多格式 1D/2D 条码图像处理库，Java 实现并移植到多种语言，既能生成也能识别几乎所有主流条形码/二维码，是全球二维码识别的底层标准之一。

## 关键信息
- **出身**：Google 员工 "20% 时间" 副业项目，2007 年 11 月开源，Apache 2.0 协议，GitHub 约 34,000 Star
- **支持格式**：二维码 QR Code / Data Matrix / Aztec / MaxiCode / PDF417；一维码 UPC-A/E、EAN-8/13、Code 39/93/128、ITF、Codabar、RSS 等
- **生态地位**：微信、支付宝、淘宝、美团等扫码 App 底层，Android 系统默认扫码方案
- **核心 API**：生成 `MultiFormatWriter.encode()`（编码+纠错+矩阵填充），识别 `MultiFormatReader.decode()`（定位探测图形+校正+解码）
- **纠错级别**：L 7% / M 15% / Q 25% / H 30%，级别越高越抗造但尺寸越大
- **对比 ZBar/OpenCV**：检测速度最快、集成难度最低（纯 Java 零依赖、不需 JNI）、生态最成熟；小尺寸二维码识别率一般、反色码（白底黑块）无法识别需预处理、严重扭曲场景不如 ZBar
- **Android 架构**：提供相机预览、扫描框、解码线程完整模块，解码放独立线程经 Handler 通信避免 ANR

## 关联连接
- [[摘要-zxing条码库]] — 来源
- [[QR码登录]] — QR 码相邻应用场景
- [[Java]] — 实现语言
- Android — 主战场平台（系统默认扫码方案）
