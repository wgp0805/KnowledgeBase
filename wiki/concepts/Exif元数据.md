---
title: "Exif元数据"
type: concept
tags: [图像, 元数据, HarmonyOS]
sources: [raw/09-archive/2026-09-08-一文读懂 HarmonyOS 7.0 带来的十大重要升级（一）.md]
last_updated: 2026-09-09
---

## 定义
嵌入图像文件中的附加信息，记录图像的版本、创作者、镜头参数、拍照参数、拍照时的地理位置等。是图像文件之外最丰富的语义来源之一。

## 关键信息

### HarmonyOS 7.0 的 Image Kit 支持
- 新增 readImageMetadata 接口读取指定图像源的元数据，使用 propertyKeys 指定待获取的字段
- 限制：仅支持 JPEG、PNG、HEIF、WEBP 和 DNG 文件（不同硬件设备支持情况不同），且需要包含 Exif 信息
- 引入动机：image 模块原本只能调用 getImageInfo 获取图像的宽高大小、像素密度、像素格式等常见属性，无法获取更多的 Exif 元数据

### 与既有能力的分工
- getImageInfo：尺寸、像素密度、像素格式等基础属性
- readImageMetadata：版本、创作者、镜头参数、拍照参数、地理位置等扩展属性

### 隐私提示
Exif 中的地理位置与设备信息属于敏感数据，在用户上传图片到网络时应默认剥离。

## 关联连接
- [[HarmonyOS]] — 提供该接口的系统
- [[摘要-harmonyos-7十大升级一]] — 来源
- [[数据隐私]] — Exif 携带的敏感信息
