---
title: "mobile-agent"
type: concept
tags: [概念, 移动端, Agent, 自动化, 无障碍]
sources: [raw/09-archive/2026-09-26-让 AI 帮你操作手机，这个 GitHub 开源项目支持安卓和 iPhone。.md]
last_updated: 2026-09-28
---

## 定义

移动端 Agent（Mobile Agent）是让 AI 读取并操作手机界面的工具类别：能读屏、点击按钮、滑动页面、填写文字，覆盖安卓与 iOS 的真机和模拟器。代表实现是 [[MobileMCP]]（通过 MCP 协议接入 Claude Code、Cursor 等客户端）。

## 关键信息

- **双通道感知**：
  1. **无障碍信息优先**——读取 App 为视障用户标注的元素说明（文字、按钮、输入框及位置），结构清晰的界面可直接据此完成控制
  2. **截图回退**——信息不完整或控件难识别时，截图交给具备图像理解的 AI 分析，再按坐标操作；两通道结合适配不同 App 的界面结构
- **与 [[BrowserAgent]] 的关系**：同属「AI 操作图形界面」品类，一个面向手机、一个面向网页；与传统 [[RPA]] 的差别同样是语义理解 vs 固定坐标脚本
- **典型场景**：改版后的页面检查（按钮位置、页面跳转）免人工回归；多设备并在时指令需指明设备名称或编号
- **接入前提**：Node.js 22+、MCP 客户端；安卓要 Android SDK Platform-Tools 与 USB 调试授权（`adb devices` 验证），iOS 模拟器要 Xcode（`xcrun simctl list devices booted` 验证）
- **验证习惯**：先列设备 → 读当前屏幕文字与元素 → 截图，三步全通再执行打开 App、输入等动作

## 关联连接
- [[MobileMCP]] — 代表实现
- [[BrowserAgent]] — 电脑端同类品类
- [[MCP]] — 接入协议
- [[ClaudeCode]] — 支持的客户端
- [[RPA]] — 传统自动化对照
- [[Agent]] — 上位概念
- [[摘要-mobile-mcp-手机操作]] — 来源
