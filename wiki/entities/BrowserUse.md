---
title: "BrowserUse"
type: entity
tags: [AI产品, 开源项目, 浏览器自动化, BrowserUse, Agent]
sources: [raw/09-archive/2026-10-23-这个GitHub 119K+ Star的开源神器，可以让AI像人一样操作浏览器！.md]
last_updated: 2026-10-23
---

## 定义
Browser-Use 是一个 GitHub Star 超过 119k 的开源浏览器自动化项目（MIT 协议），核心思路是把浏览器里的**无障碍树**交给大模型，让模型根据页面语义判断下一步操作；用户用自然语言描述目标，Agent 自己完成打开页面、找控件、填内容、翻页、截图的整条操作链路。

## 关键信息
- **架构三层**：上层 Python API → 中间 Rust 高性能核心 → 底层由 Playwright 驱动浏览器；不是 Playwright 的包装，而是把"元素定位"从代码里转移到模型推理里
- **技术路线对比**：
  - 硬编码选择器（Selenium/Playwright）：可控、快，但页面改版维护成本高
  - 截图视觉方案：不依赖 DOM，但每轮处理图像，token 消耗与响应时间高
  - Browser-Use：读取原生 Accessibility Tree，不依赖 CSS/class，在稳定性与成本间折中
- **模型开放**：支持 OpenAI GPT、Anthropic Claude、Gemini、Ollama 本地模型；官方还有针对浏览器任务优化的 BU 2.0 专用模型 ChatBrowserUse（bu-2-0）
- **安装要求**：Python 3.11+，推荐用 uv 管理依赖；`uvx browser-use install` 安装 Playwright 浏览器
- **使用形态**：
  - 命令行：`browser-use run "自然语言任务"`、`browser-use screenshot "..."`、`--file test_cases.txt` 批量执行
  - Python API：`Agent(task=..., llm=..., browser=...)`，复杂页面可开 `use_vision=True`
  - 自定义工具：`Tools()` + `@tools.action` 注册任务后动作（如发通知邮件）
- **CI 接法**：Jenkins/GitLab CI 无头执行 `BrowserConfig(headless=True, save_recording=True)`，失败时回看录像
- **本地模式 vs 云端模式**：本地（MIT、自控浏览器实例，适合调试/内网/私有化，需自己处理反爬与验证码）；云端（托管浏览器，内置指纹伪装、代理轮换、验证码处理，可复用登录 Profile）
- **适用边界**：页面常改、任务偏一次性、非技术同学参与的场景合适；高频、稳定、接口级测试仍是传统方案的主场

## 关联连接
- [[摘要-browser-use浏览器自动化]] — 来源（冰河详解安装/实践/踩坑）
- [[无障碍树]] — 核心技术机制
- [[Agent]] — 所属产品形态
- [[Ollama]] — 可接入的本地模型
- [[冰河]] — 文章作者
