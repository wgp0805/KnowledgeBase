---
title: "VCard"
type: entity
tags: [数据格式, 联系人, HarmonyOS, vcf]
sources: [raw/09-archive/2026-09-08-一文读懂 HarmonyOS 7.0 带来的十大重要升级（一）.md]
last_updated: 2026-09-09
---

## 定义
电子名片的文件格式标准（VCard），对应文件格式扩展名为 .vcf。可包含姓名、地址资讯、电话号码、URL、logo、相片等信息，是移动设备间交换联系人的通用载体。

## 关键信息
- HarmonyOS 7.0 的 Telephony Kit 新增 VCard 模块，提供 VCard 能力
- **importVCard**：将 VCard 文件（.vcf）导入联系人数据库
- **exportVCard**：将联系人导出为 VCF（vcard file）文件
- 引入动机：安卓手机导入/导出联系人数据时使用 vcf 文件，即 VCard 标准对应的格式；新增该模块方便开发者把安卓手机导出的联系人文件导入鸿蒙手机
- 书中对应《鸿蒙 HarmonyOS 6 应用开发》"5.3.4 拨号页面和通讯录页面"小节

## 关联连接
- [[HarmonyOS]] — 提供 VCard 模块的系统
- [[摘要-harmonyos-7十大升级一]] — 来源
