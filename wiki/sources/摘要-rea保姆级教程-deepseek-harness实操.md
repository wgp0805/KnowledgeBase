---
title: "摘要-rea保姆级教程-deepseek-harness实操"
type: source
tags: [来源, REA, DeepSeekHarness, 逆向工程, MCP]
sources: [raw/01-articles/REA 保姆级教程：DeepSeek Harness 实操.md]
last_updated: 2026-10-14
---

## 核心摘要
本文是沉默王二（二哥）撰写的 REA（Reverse Engineer Anything，逆向万物工程）接入 DeepSeek Harness（DSH）的保姆级实操教程。REA 能让 Agent 在没有源码的情况下，从程序安装文件和运行轨迹出发查清某个功能的实现方式，再照着重做一个自己的版本——网页、桌面应用、安卓 App 甚至 1996 年老游戏均可。2026-10-13 REA 冲上 GitHub 日榜第一，单日新增 45327 Star，发稿前已达 17 万星标。文章回答了三个问题：REA 凭什么能让 Agent 做逆向（三件事：MCP 工具化、套路固化、Evidence 证据链）；DSH 没有官方一键接入命令时如何手动接入（Node 版本检查 + cordis.patch.yml 写 MCP 配置 + 装 Skill，三步）；接好后如何跑通官方恐龙游戏逆向案例（CDP 调试端口启动 Chrome → list_browser_targets/inspect_web_page 读 index.js → 照规则做新游戏 → 自己验收速度曲线）。文末提醒：REA 不支持绕过 DRM、破解授权校验、做外挂、复制专有代码，逆向前先看许可协议。

## REA 做的三件事
1. **把专业逆向工具打包成 MCP 工具**：6.4.0 版本共 170 个工具。分析原生程序用 Hopper/Ghidra/IDA 反汇编器（机器码→汇编/伪代码）；分析网页走 Chrome 调试协议 CDP；分析安卓应用用 JADX。Ghidra 每次以只读模式启动临时工程，分析完即删，不改原程序一个字节。
2. **把逆向老手的套路固化成工具**：老手三步（搜界面关键字 → 找引用处 → 定位函数）被串成 `trace_feature` 工具，Agent 调一次即得"哪个函数用了这个关键字"；结果过长先摘要再持久化，Agent 用 `inspect_analysis_view` 分页读取（每页默认 64 条）。
3. **每条结论都能拿出证据**：每次返回结果生成一条 Evidence 记录（分析了哪个文件、调了什么操作、得到什么结果）；配套 Skill 规定每条结论必须分清"观察到的/推断的/不确定的"；搜不到关键字时说明"搜不到不代表不存在"。

## DeepSeek Harness 接入 REA 三步
1. **确认 Node 版本**：REA 要求 22.19+、24.11+ 或 26+，23 和 25 都不行（`node --version`）。
2. **接入 MCP**：创建/打开 `~/.dsh/cordis.patch.yml`（DSH 桌面端与命令行都读此文件），写入 insert 补丁：name 指定自带 MCP 客户端插件 `@deepseek-ai/dsh-mcp-client`，serverName 为 `rea`（接入后工具显示为 `mcp__rea__` 前缀），transport 为 `stdio`（DSH 自己用 npx 启动 REA，标准输入输出通信），版本号固定 `rea-agents@6.4.0` 防止自动升级改变行为。
3. **安装 Skill**：先 `--dry-run` 预览再 `--yes` 执行，Skill 装进 `~/.agents/skills/reverse-engineer-anything`，DSH 自动扫描该目录。重启 DSH 新建会话发"列出你能用的 REA 工具"，看到 `mcp__rea__` 前缀工具即接入成功。也可以直接问 DSH"要接入 REA 该怎么做"让它自己调研安装。

## 官方恐龙游戏逆向案例（t-rex-runner）
- 启动带调试端口的 Chrome（`--remote-debugging-port=9222` + 独立 `--user-data-dir` 临时目录，不动日常浏览器和登录状态）
- 提示词：让 REA 调查 https://wayou.github.io/t-rex-runner/ ，调试地址 http://127.0.0.1:9222 ，先 `list_browser_targets` 找页面，再 `inspect_web_page` 开 `include_script_sources` 读 index.js，查"从什么速度开始、怎样加速、什么时候停止加速"，每条结论给出代码出处
- **内行细节**：`inspect_web_page` 是被动读取——通过 CDP 拿页面已加载脚本源码，不调 `Runtime.evaluate`，不在页面里执行任何 JS，也不点击跳转；正常至少看到两次 REA 工具调用
- 仿制验收：让 Agent 按查到的加速规则在当前文件夹创建 `dino-demo.html`（恐龙能跳、仙人掌从右来、2-18 速度滑块、自动加速选项从 6 开始沿用原规则）；再从速度 6 排除碰撞计算 0/1000/4000/10000 次更新后的速度，保留三位小数与 6.000/7.000/10.000/13.001 逐项比较

## 关联连接
- [[REA]] — 本文主题：逆向万物开源工程
- [[DeepSeekHarness]] — 接入 REA 的 Harness 载体
- [[逆向工程]] — 核心概念（无源码反推实现）
- [[MCP协议]] — REA 工具化的接入协议
- [[Cordis]] — DSH 的补丁文件机制（cordis.patch.yml）
- [[AgentSkills]] — REA Skill 的安装与作用
- [[沉默王二]] — 本文作者
