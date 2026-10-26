---
title: "REA"
type: entity
tags: [实体, 开源项目, 逆向工程, Agent, MCP]
sources: [raw/09-archive/REA 保姆级教程：DeepSeek Harness 实操.md, raw/09-archive/霸榜 GitHub 的 AI 逆向神器，玩疯了！.md]
last_updated: 2026-10-20
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

## 二次爆火与官方案例（2026-10-19，程序员追风）
- **Star 增速**：发文时已达 24.1 万 Star（两天前 15 万），作者称"全民逆向"热度堪比当时的 [[OpenClaw]]"全民养虾"，增速连 OpenClaw 也自愧不如
- **工作流**：Coding Agent 通过 MCP 调用 REA，执行"提问、检查、读证据、实现和测试"的严密流程；不让大模型凭空猜测或脑补伪代码，最终输出带确凿证据的结构化分析报告，并指导精准代码重构或功能复现
- **案例一（Notion 剪贴板）**：分析 Notion Desktop 7.6.1 应用包，沿页面 API、预加载脚本和进程通信找到主进程调用 Electron 剪贴板接口的位置，并解释复制的 HTML 如何通过一个 ID 关联本地保存的文档块数据
- **案例二（DX-Ball 声音算法）**：砖块横向位置影响左右声道偏向；反编译缺关键计算时，结合原始指令、调用方和数值常量重建 C 函数——3205 组输入与原始 x86 函数一致，指定编译器复现全部 63 个字节
- **一键安装**：`npx rea-agents setup` 交互式向导自动识别本地 Coding Agent、多选写入 MCP 配置（写入前自动备份）、提示接入本机 Ghidra/Hopper/IDA；`npx rea-agents doctor` 做健康检查；可 `npm install -g rea-agents` 全局安装 `rea` 命令；系统要求 macOS 12+/Linux，Node 建议 22.19+
- **最佳实践**：作者推荐 GLM-5.3（非 Flash）+ REA——Benchmark 上 GLM 5.3 逆向能力更强；REA 出图风格不佳，可搭配 [[Archify]] 生成交互式架构图；最佳用法不是逆向完事，而是对 App 做二开和定制化
- **定位论断**："有了 REA 之后，你的所有 App 都被迫开源了"；REA 把传统高门槛逆向工程平民化，变成标准化的证据链推演

## 关联连接
- [[摘要-rea保姆级教程-deepseek-harness实操]] — 来源（沉默王二教程）
- [[摘要-霸榜github-ai逆向神器-rea-archify]] — 来源（程序员追风：爆火观察 + 官方案例 + Archify 搭配）
- [[逆向工程]] — 核心概念
- [[DeepSeekHarness]] — 接入 Harness 的实操载体
- [[MCP协议]] — 工具化接入协议（170 个工具）
- [[AgentSkills]] — 配套 Skill（证据链规范）
- [[沉默王二]] — 教程作者
- [[Cordis]] — DSH 接入时的补丁配置文件机制
- [[Archify]] — 配套架构可视化工具（弥补 REA 出图短板）
- [[GLM-5.3]] — 作者推荐的逆向搭配模型
- [[OpenClaw]] — 爆火热度对比参照
