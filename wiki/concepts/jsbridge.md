---
title: "jsbridge"
type: concept
tags: [架构模式, H5, 原生通信]
sources: [raw/09-archive/程序汪4万20天接的肉鸽类小游戏，二期项目.md]
last_updated: 2026-07-24
---

## 定义

JSBridge 是 H5 页面与原生 APP（Android/iOS）之间双向通信的桥梁模式，通过约定接口实现 WebView 中 JavaScript 调用原生能力和原生调用 H5 回调。

## 关键信息

- **通信方向**：H5 → APP（调用原生能力）、APP → H5（注入数据/事件通知）
- **H5 → APP 典型接口**：
  - `getAppContext()` — 获取环境信息（版本、平台、安全区、语言）
  - `refreshLaunchCode()` — 登录续期
  - `closeGame()` — 关闭页面
  - `setOrientation(mode)` — 锁定横竖屏
  - `openNativePage(route, params)` — 打开原生页面（地址、客服等受控页面）
  - `showRewardedAd(request)` — 调起原生激励视频
  - `reportClientEvent(event)` — 补充端侧埋点
- **安全约束**：桥接层必须版本化，限制来源域名、方法名和参数结构；禁止向H5暴露任意原生调用或任意URL跳转能力
- **WebView安全**：Android/iOS WebView应关闭非必要文件访问、调试能力和混合内容，线上只允许HTTPS
- **令牌管理**：访问令牌只保存在内存中，过期后通过受控JSBridge请求APP刷新，不把长期token放在URL、localStorage或日志中

## 关联连接

- [[摘要-程序汪-肉鸽小游戏二期]] — 来源
- [[摘要-无人图书柜项目]] — 另一程序汪项目的APP-H5模式
- [[Token认证机制]] — 免登录令牌交换相关
