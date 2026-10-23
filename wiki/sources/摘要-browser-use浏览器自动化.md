---
title: "摘要-browser-use浏览器自动化"
type: source
tags: [来源, BrowserUse, 浏览器自动化, 无障碍树, Agent]
sources: [raw/09-archive/这个GitHub 119K+ Star的开源神器，可以让AI像人一样操作浏览器！.md]
last_updated: 2026-10-23
---

## 核心摘要
冰河（冰河技术公众号，2026-10-23 发布）解读 GitHub 119k+ Star 的开源项目 Browser-Use：传统网页自动化最耗人的是元素定位，页面一改版 CSS 选择器/XPath 就整片失效。Browser-Use 的思路是把浏览器原生的无障碍树交给大模型，让模型按页面语义判断下一步操作，用自然语言描述目标即可跑完整条操作链路（打开页面、找控件、填内容、翻页、截图）。架构分三层：上层 Python API、中层 Rust 高性能核心、底层 Playwright 驱动浏览器；模型开放接入 OpenAI GPT、Claude、Gemini、Ollama 本地模型，并有针对浏览器任务优化的 BU 2.0 模型 ChatBrowserUse。文章对比三种路线——硬编码选择器（快但脆）、截图视觉方案（通用但图像 token 贵且慢）、无障碍树方案（稳定性与成本之间的折中），并提醒复杂动态渲染页面仍可能误判：它更适合作为传统自动化（Selenium/Playwright）的补充而非全面替代，适合页面频繁改版、任务一次性、非技术同学参与的场景。

## 关联连接
- [[冰河]] — 作者
- [[BrowserUse]] — 项目本体
- [[无障碍树]] — 核心技术路线（读 Accessibility Tree 代替选择器）
- [[浏览器自动化]] — 所在领域背景
- [[浏览器Agent]] — 同类产品形态
- [[Agent]] — 自然语言驱动的执行者
- [[Ollama]] — 支持的本地方案之一
