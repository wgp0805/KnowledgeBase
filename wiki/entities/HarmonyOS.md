---
title: "HarmonyOS"
type: entity
tags: [操作系统, 鸿蒙, 移动开发, 华为]
sources: [raw/09-archive/2026-09-08-一文读懂 HarmonyOS 7.0 带来的十大重要升级（一）.md]
last_updated: 2026-09-09
---

## 定义
华为推出的操作系统。HarmonyOS 7.0 于 2026 年 9 月 7 日正式发布，在 HarmonyOS 6.1 基础上增强了若干特性。

## 关键信息

### 7.0 十大 Kit 升级（系列文章第一篇覆盖）
| Kit | 新特性 | 关键约束 |
|---|---|---|
| [[ArkUI]] | TextController 新增 setTextSelection，可设置文本选择区域并高亮 | copyOption 为 CopyOptions.None、textOverflow 为 TextOverflow.MARQUEE 时不生效 |
| [[ArkWeb]] | window.detectSimulatedClickRiskEnhanced 模拟点击检测 | 每 30 秒最多 10 次；每应用每设备每天最多 20 次 |
| AVCodec Kit | AV1/VP9/VP8/RV30/RV40/WVC1/DVVIDEO/RAWVIDEO/MPEG1 视频软解码 | 原先仅支持 H.26x 家族与 MPEG2/MPEG4 |
| Call Service Kit | 跳转系统"电话 > 更多 > 设置 > 陌生号码和信息识别"页面 | — |
| Camera Kit | onCapturePhotoAvailable 注册全质量图与未压缩图上报事件 | 原先只能拿到压缩后照片，无法跑自研算法 |
| Image Kit | readImageMetadata 读取元数据（用 propertyKeys 指定字段） | 仅 JPEG/PNG/HEIF/WEBP/DNG，且需含 Exif |
| Map Kit | 3D 地球与城市灯光效果，sphereEnabled / setSphereEnabled / isSphereEnabled | 层级缩小到小于 4 时才能清晰看到 3D 地球 |
| Media Kit | fetchFramesByTimes 传入时间戳数组批量取缩略图 | 原先 fetchFrameByTime 一次只返回一张 |
| Network Kit | network_config.json 配置 HTTP 明文传输策略 | 位置 src/main/resources/base/profile/ |
| Telephony Kit | 新增 VCard 模块，importVCard 导入 .vcf、exportVCard 导出 | — |

### 编码格式与容器对应关系（AVCodec）
- AV1：基于 VP9 迭代升级，完全开源、免专利授权费
- VP9/VP8：原 On2 Technologies 格式，被谷歌收购后开源免费，用于 WebM
- RV30/RV40：RealNetworks 专有编码，用于 RM/RMVB
- WVC1：微软专有编码，高清 DVD/蓝光备选，用于 WMV/ASF
- DVVIDEO：磁带 DV 摄像机工业标准，用于 AVI
- RAWVIDEO：零压缩原始像素数据，体积极大，用于专业剪辑母带
- MPEG1：第一代音视频统一编码，用于 VCD 与早期在线视频（MPG）

### 升级意图
新增能力的显著特征是大量对齐 Android 生态（networkSecurityConfig、vcf 联系人、H.26x 之外的编码），实质是降低安卓应用迁移到鸿蒙的摩擦，为存量 App 提供迁移路径。

### 配套资料
《鸿蒙 HarmonyOS 6 应用开发：从零基础到 App 上线》，每个新特性都对应书中章节，便于对照学习。

## 关联连接
- [[ArkUI]] — Text 组件的文本选择增强
- [[ArkWeb]] — 模拟点击检测
- [[模拟点击检测]] — 反设备墙与自动化作弊
- [[Exif元数据]] — Image Kit 元数据读取
- [[VCard]] — Telephony Kit 的联系人交换格式
- [[摘要-harmonyos-7十大升级一]] — 来源
