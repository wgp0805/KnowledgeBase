---
title: "ArkWeb"
type: entity
tags: [Web框架, HarmonyOS, 鸿蒙, 方舟, JavaScript]
sources: [raw/09-archive/2026-09-08-一文读懂 HarmonyOS 7.0 带来的十大重要升级（一）.md]
last_updated: 2026-09-09
---

## 定义
HarmonyOS 的方舟 Web 框架，通过 Web 组件承载 H5 网页，并提供 JavaScript 与 Web 页面交互的能力。

## 关键信息
- **HarmonyOS 7.0 新特性**：新增支持 Web 应用模拟点击检测
- **调用方式**：Web 应用通过 JavaScript 调用 window.detectSimulatedClickRiskEnhanced 接口获取检测结果
- **调用配额**：每 30 秒最多调用 10 次；每个应用在每个设备上每天最多调用 20 次
- **引入动机**：自动化测试过程中需要在 Web 应用上模拟用户点击行为；该特性可用于自动化点击、设备墙等作弊行为检测，应用可根据检测结果评估如何进行业务操作
- **验证方式**：按《鸿蒙 HarmonyOS 6 应用开发》"12.4.3 网页脚本交互"小节，在 H5 网页中用 JS 接口回调该接口，根据检测结果判断是真人点击还是机器点击

## 关联连接
- [[HarmonyOS]] — 所属操作系统
- [[ArkUI]] — 同属方舟体系的 UI 框架
- [[模拟点击检测]] — 该接口实现的能力
- [[摘要-harmonyos-7十大升级一]] — 来源
