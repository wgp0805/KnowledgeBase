---
title: "MobileMCP"
type: entity
tags: [开源项目, MCP, 移动端, Agent]
sources: [raw/09-archive/2026-09-26-让 AI 帮你操作手机，这个 GitHub 开源项目支持安卓和 iPhone。.md]
last_updated: 2026-09-28
---

## 定义

Mobile MCP（github.com/mobile-next/mobile-mcp）是让 Agent 操作手机的开源 MCP 服务器，GitHub 近 7K Star。接好设备后 AI 可读取屏幕内容、点击按钮、滑动页面、填写文字，安卓与 iOS 的真机和模拟器均支持。

## 关键信息

- **MCP 工具集**：设备管理、应用管理、屏幕交互、输入导航四类
- **核心设计——无障碍优先**：优先读取系统提供的无障碍信息（App 为视障用户标注的文字、按钮、输入框及位置）；信息不完整或控件难识别时，回退为截图交给具备图像理解的 AI 分析后按坐标操作，双通道适配不同 App 界面结构
- **跨平台**：安卓真机/模拟器（需 Android SDK Platform-Tools、`ANDROID_HOME`、USB 调试授权，`adb devices` 验证）、iOS 模拟器（Xcode + `xcrun simctl list devices booted`）、iPhone 真机（需额外自动化环境配置）
- **接入**：`claude mcp add mobile-mcp -- npx -y @mobilenext/mobile-mcp@latest`，或在 mcpServers 配置中写入 command/args；运行环境要求 Node.js 22+
- **验证三步**：列出已连接设备 → 列出当前屏幕文字与可交互元素 → 截取当前屏幕，均正常后再尝试打开 App、输入内容
- **典型场景**：独立开发者改版后让 AI 打开设备检查按钮位置与页面跳转，替代人工回归；多设备时指令需写明设备名称或编号

## 关联连接
- [[mobile-agent]] — 所属品类概念
- [[MCP]] — 所依赖的接入协议
- [[ClaudeCode]] — 支持的 MCP 客户端
- [[Codex]] — 支持的 MCP 客户端
- [[BrowserAgent]] — 电脑端同类操作 Agent
- [[摘要-mobile-mcp-手机操作]] — 来源
