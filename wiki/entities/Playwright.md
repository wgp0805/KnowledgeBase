---
title: "Playwright"
type: entity
tags: [实体, UI自动化, 测试, 微软, Web]
sources: [raw/09-archive/为什么越来越多人用 Playwright.md]
last_updated: 2026-11-25
---

## 定义
Playwright 是微软 2020 年发布的 Web UI 自动化工具，走 WebSocket 长连接 + 浏览器原生 CDP 协议直连内核，以自动等待、BrowserContext 隔离和 Trace Viewer 为核心特性，定位是"为现代 Web（SPA/微前端/实时渲染）重新设计的自动化工具"而非 Selenium 的替代品。

## 关键信息
- **架构代差**：Selenium 基于 W3C WebDriver，客户端—驱动—浏览器之间 HTTP 短连接来回五趟，chromedriver 与浏览器版本不匹配是常态；Playwright 客户端直连 Playwright Server，Server 经 CDP 驱动内核，无第三方驱动层。实测打开百度搜索关键词：Selenium 平均 2.1 秒，Playwright 0.7 秒
- **自动等待**（详见 [[自动等待]]）：可操作性检查（visible/stable/enabled/receives events，稳定判定为 bounding box 连续两帧未移动、点击不被遮挡）+ Web-first 断言自动重试（默认 5 秒内出现即通过）。团队统计不稳定率从 12% 降至 2% 以下
- **BrowserContext**：同一浏览器进程内创建 N 个隔离上下文（各自 cookie/localStorage/sessionStorage），一个进程并行跑几十个用例；天然适合多用户场景测试（A 发消息 B 收到，两个 context 即可）。收尾只关 context、复用 browser 进程
- **网络拦截**：`page.route()` 经 CDP Fetch 域在请求发出前 fulfill/mock/阻断，是浏览器内核原生支持的能力；`waitForResponse()` 在操作前开始等信号——"等的是信号，不是时间"
- **Trace Viewer**：录制每步 DOM 快照/网络请求/console 日志/光标位置的时间线，失败后像视频回放拖到任意时间点；排查 flaky 用例平均从半天缩短到十几分钟，CI 可自动生成并上传制品库
- **选型**：适合新项目新团队、稳定性要求高的金融电商、多浏览器不需 IE（Chromium/Firefox/WebKit 覆盖现代 Web 99% 场景）；不适合 IE11/老 Safari、移动端真机（需 Appium）、已有大量稳定 Selenium 资产（策略：新用例用 Playwright、旧的不动、逐步替换最不稳定的那部分）
- **Java 入门**：依赖 `com.microsoft.playwright:playwright:1.49.0`；`mvn exec:java -Dexec.mainClass=com.microsoft.playwright.CLI -Dexec.args="install"` 自动下载适配浏览器，再也不用手动管驱动版本
- **生态位置**：是 [[浏览器Agent]] 与传统自动化共用的浏览器底座（Browser-Use/OpenMuse 等底层也由 Playwright 驱动），但其本身是硬编码选择器的传统方案，与用无障碍树/模型推理定位元素的路线不同

## 关联连接
- [[摘要-为什么越来越多人用playwright]] — 来源
- [[自动等待]] — 核心特性，flaky test 根治方案
- [[浏览器Agent]] — 上位对照（传统自动化底座 vs AI 浏览器 Agent）
- [[苏三]] — 作者
