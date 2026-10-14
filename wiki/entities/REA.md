---
title: "REA"
type: entity
tags: [实体, 开源项目, 逆向工程, Agent, MCP]
sources: [raw/01-articles/REA 保姆级教程：DeepSeek Harness 实操.md]
last_updated: 2026-10-14
---

## 定义
REA（Reverse Engineer Anything，逆向万物工程）是一个开源项目，让 Agent 在没有源码的情况下，从程序的安装文件和运行轨迹出发，查清一个功能到底是怎么实现的，再照做一个自己的版本。网页、桌面应用、安卓 App，甚至 1996 年的老游戏都能逆向。

## 关键信息
- **爆火记录**：2026-10-13 冲上 GitHub 日榜第一，单日新增 45327 颗 Star，截止发稿前（2026-10-13）已有 17 万星标；AI 圈热议，有博主称"以后不存在闭源项目了，因为反正会被逆向"
- **当前版本**：6.4.0（`rea-agents@6.4.0`），共 170 个 MCP 工具

## REA 做的三件事
1. **把专业逆向工具打包成 MCP 工具**
   - 原生程序：背后是 Hopper、Ghidra、IDA 等反汇编器（把机器码翻译成汇编和伪代码的工具）
   - 网页：通过 Chrome 调试协议 CDP 读取页面
   - 安卓应用：使用 JADX
   - 安全性：Ghidra 每次都以只读模式启动一个临时工程，分析完就删掉，不会改动原程序的任何一个字节
2. **把逆向老手的套路固化成工具**
   - 老手三步：搜界面上出现的关键字 → 找出哪些地方引用了这个关键字 → 定位到引用所在的函数
   - REA 串成 `trace_feature` 工具：Agent 调用一次就能拿到"哪个函数用到了这个关键字"
   - 结果太长先做摘要，完整结果持久化，Agent 再用 `inspect_analysis_view` 分页读取，每页默认 64 条
3. **每条结论都能拿出证据**
   - 每次返回结果生成一条 Evidence 记录：分析了哪个文件、调用了什么操作、得到了什么结果
   - 配套 Skill 规定：Agent 的每条结论都要分清哪些是观察到的、哪些是推断的、哪些还不确定
   - 搜不到关键字时 REA 会说明"搜不到不代表不存在"

## 接入与使用
- **Node 版本要求**：22.19 以上、24.11 以上或 26 以上；23 和 25 都不行
- **Skill 安装目录**：`~/.agents/skills/reverse-engineer-anything`
- **常用工具**：`list_browser_targets`（找页面）、`inspect_web_page`（被动读取页面已加载脚本源码，不执行 Runtime.evaluate、不点击跳转）
- **DeepSeek Harness 接入方式**：详见 [[DeepSeekHarness]] 与 [[摘要-rea保姆级教程-deepseek-harness实操]]

## 法律边界（免责声明）
用 REA 分析别人的软件之前先看对方许可协议；REA 明确不支持：绕过 DRM、破解授权校验、做游戏外挂、复制别人的专有代码。

## 关联连接
- [[摘要-rea保姆级教程-deepseek-harness实操]] — 来源
- [[逆向工程]] — 核心概念
- [[DeepSeekHarness]] — 接入 Harness 的实操载体
- [[MCP协议]] — 工具化接入协议（170 个工具）
- [[AgentSkills]] — 配套 Skill（证据链规范）
- [[沉默王二]] — 教程作者
- [[Cordis]] — DSH 接入时的补丁配置文件机制
