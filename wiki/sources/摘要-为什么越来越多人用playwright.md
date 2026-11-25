---
title: "摘要-为什么越来越多人用playwright"
type: source
tags: [来源, 原始文件, Playwright, UI自动化, 测试, 苏三]
sources: [raw/09-archive/为什么越来越多人用 Playwright.md]
last_updated: 2026-11-25
---

## 核心摘要

苏三（2026-11-25）回答"为什么越来越多人用 Playwright"：**它不是 Selenium 的替代品，而是为现代 Web 重新设计的自动化工具**。三个核心优势按重要性排序：自动等待 > 架构代差 > 调试体验。

- **一、Selenium 的加班史**：基于 W3C WebDriver 协议，客户端与浏览器之间隔着驱动进程，HTTP 短连接每次操作来回五趟；Chrome 自动更新后 chromedriver 版本对不上导致全线飘红是架构决定的。Playwright 走 WebSocket 长连接一次握手全双工，客户端直连 Playwright Server，Server 再经浏览器原生 CDP 协议驱动内核，"没有第三方驱动这个中间商赚差价"。实测打开百度搜索关键词：Selenium 平均 2.1 秒，Playwright 0.7 秒，差三倍
- **二、自动等待（最上瘾的特性）**：Selenium 的 `WebDriverWait` 显式等待与 `Thread.sleep(3000)`（"你是在赌"，flaky test 万恶之源）→ Playwright 直接 `page.locator("#submit").click()`，背后做**可操作性检查**（可见、可点击、稳定——检查 bounding box 连续两个动画帧未移动；不被遮挡——点击坐标命中别的元素就继续等）。Web-first 断言 `expect(locator).toBeVisible()` 自动重试直到超时（默认 5 秒内出现过就算通过），而 `isVisible()` 取出来再断言没有重试。团队统计：仅把显式等待换成自动等待，用例不稳定率从 12% 降到 2% 以下。详见 [[自动等待]]
- **三、BrowserContext 并行隔离**：Selenium 每测试起新 driver 实例（并行 10 用例开 10 个 Chrome 内存爆炸）；Playwright 的 BrowserContext 相当于"隐身窗口"，同一浏览器进程里创建 N 个完全隔离上下文（各自 cookie/localStorage/sessionStorage），一个进程并行跑几十个测试。多用户场景（A 发消息 B 收到）用两个 context 即可，共享进程内存省速度快
- **四、网络拦截一等公民**：`page.route("**/api/pay", route -> route.fulfill(...))` 通过 CDP 的 Fetch 域在请求发出前修改/伪造/阻断，是浏览器内核原生支持的能力；`waitForResponse` 在触发操作前就开始等——"等的是信号，不是时间"
- **五、Trace Viewer（最被低估的杀手锏）**：Selenium 失败只有截图+日志；Playwright 记录整个执行过程时间线（每步 DOM 快照/网络请求/console 日志/光标位置），像视频回放拖到任意时间点。排查 flaky 用例平均时间从半天缩短到十几分钟；CI 可自动生成 trace 失败时上传制品库
- **六、优缺点与选型**：对比表（首次发布 2020 vs 2004、通信协议、自动等待、浏览器支持、移动端、语言、生态、速度、调试、并行）。适合新项目新团队、稳定性要求高（金融电商）、多浏览器不需 IE；Selenium 不可替代场景：IE11/老 Safari、移动端真机（Appium）、已有大量稳定 Selenium 资产（策略：新用例用 Playwright，旧的不动，逐步替换最不稳定的那部分）
- **七、Java 入门**：一个依赖 `com.microsoft.playwright:playwright:1.49.0`，`mvn exec:java ... install` 自动下载适配浏览器，"再也不用手动管驱动版本"；示例串起 route 拦截 / fill-click 自动等待 / Web-first 断言 / `context.close()` 而非 `browser.close()` 让进程跨测试复用
- **总结**：三优势——自动等待（flaky test 根治）、架构代差（WebSocket 直连无驱动层）、调试体验（Trace Viewer 降维打击）。Selenium 不会死（IE11/Appium/二十年生态）

实体详见 [[Playwright]]，核心特性详见 [[自动等待]]。

## 关联连接
- [[Playwright]] — 本文主角：微软出品的现代 Web 自动化工具
- [[自动等待]] — 本文最强调的特性，flaky test 根治方案
- [[浏览器Agent]] — 上位对照：Playwright 是传统自动化底座，非 AI 浏览器 Agent
- [[苏三]] — 作者
