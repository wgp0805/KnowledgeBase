---
title: "摘要-mobile-mcp-手机操作"
type: source
tags: [来源, 原始文件]
sources: [raw/09-archive/2026-09-26-让 AI 帮你操作手机，这个 GitHub 开源项目支持安卓和 iPhone。.md]
last_updated: 2026-09-28
---

# 摘要-mobile-mcp-手机操作

## 核心摘要

Mobile MCP 是 mobile-next 开源的「让 Agent 操作手机」的 MCP 项目（GitHub 近 7K Star）：接好设备后 AI 能读屏、点击按钮、滑动页面、填写文字，安卓与 iOS 的真机和模拟器都支持，可接入 Claude Code、Cursor 等 MCP 客户端，常见用法是独立开发者做改版后的页面检查（按钮位置、页面跳转）免人工回归。其设计特点是**优先利用系统无障碍信息**（App 提供给视障用户的元素说明，含文字、按钮、输入框及位置），信息不完整或控件难识别时再截图交给具备图像理解的 AI 分析并按坐标操作，双通道结合适配不同 App 界面结构；工具集覆盖设备管理、应用管理、屏幕交互、输入导航四类。接入步骤：Node.js 22+、安卓配 Android SDK Platform-Tools 并 `adb devices` 确认连接、iOS 模拟器用 Xcode 并 `xcrun simctl list devices booted` 检查，然后 `claude mcp add mobile-mcp -- npx -y @mobilenext/mobile-mcp@latest` 或写入 mcpServers 配置，最后用「列出设备→读取当前屏幕文字与元素→截图」三步验证。

## 关联连接
- [[MobileMCP]] — 该文介绍的开源项目实体
- [[mobile-agent]] — 该文提炼的移动端 Agent 概念
- [[MCP]] — 所依赖的接入协议
- [[ClaudeCode]] — 可接入的 MCP 客户端
- [[Codex]] — 可接入的 MCP 客户端
- [[BrowserAgent]] — 同类的电脑端操作 Agent 对照
