---
title: "IntelliJIDEA"
type: entity
tags: [IDE, Java]
sources: [raw/09-archive/idea的特殊用法及远程DEBUG的方法.md, raw/09-archive/idea控制台输出中文乱码.md, raw/09-archive/idea链接svn报错.md, raw/01-articles/IDEA使用Git提交报错 unable to read askpass response from.md, raw/01-articles/IDEA 2026.2 必装插件 Top 100.md, raw/01-articles/2026-09-30 - 这五款牛逼的 IDEA 插件，堪称代码质量检查利器！.md]
last_updated: 2026-10-08
---

## 定义
IntelliJ IDEA 是 JetBrains 公司开发的 Java 集成开发环境，被广泛认为是 Java 开发的最佳 IDE。

## 关键信息
- 远程调试：JDWP 参数配置（-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005）
- 中文乱码解决：文件编码 UTF-8、properties 文件编码、JVM 编码参数
- SVN 集成：SSL 证书验证失败（E170013/E230001）的解决方案
- Git 集成：askpass 响应错误时在远程 URL 中嵌入凭据

### 2026.2 重大更新（2026-09-29，详见 [[摘要-idea-2026-2-必装插件-top100]]）
- **AI 原生化**：[[GitHubCopilot]] 从插件变为原生内置；Junie 支持 MCP 自动配置；AI Agent Skills Manager 统一管理 AI 代理技能；ACP 原生支持 Agent 接入
- **MCP 标准化**：MCP 升格一等公民——主工具栏 MCP Server Widget、自动检测 Claude/Codex TUI 配置、项目级工具集
- **LSP 开源化**：LSP Client API 全面开源
- **内置替代旧插件**：[[Logpoints]] 日志断点（非侵入式调试）、终端拖拽路径、Resolve All Simple Conflicts 一键解冲突
- **语言与构建**：Java 27 首发、Kotlin 2.4 稳定、Gradle 10 早期支持、TypeScript 7.0；多文件 AI 辅助 J2K 转换 + LLM 校验
- **性能**：后台异步文件保存、紧凑对象头默认开启、140 个冻结修复
- **插件市场趋势（2026）**：84% 开发者用或计划用 AI 编码工具；MCP 扩展 4148 个；开源阵营（Cline/Roo Code/Continue）与国产（[[通义灵码]]、CodeGeeX、TRAE AI）崛起

### 五款代码质量检查插件（2026-09-30，详见 [[静态代码检查]]）
用工具减少 code review 工作量的常用组合：**Alibaba Java Coding Guidelines**（查代码规范首选，Blocker>Critical>Major 三级、大部分可自动修复）、**CheckStyle**（只管文法层风格，对 bug 几乎无发现能力）、**PMD**（安全编码规则 + 数据流分析，自定义规则能力强）、**FindBugs**（专注找真实 bug：空指针、资源未关闭、== 比较字符串）、**SonarLint**（层级最高，覆盖依赖/耦合/复杂度/重复代码等整体健康度，可关联 Sonar 平台、commit 时自动检查）。选型：查规范用 Alibaba 规约，找 bug 用 PMD + FindBugs + SonarLint 互补。详见 [[摘要-idea五款代码质量检查插件]]。

## 关联连接
- [[Java]] — 开发语言
- [[Git]] — 版本控制集成
- SVN — 版本控制集成
- [[SpringBoot]] — 常用项目框架
- [[摘要-idea控制台输出中文乱码]] — 解决 IntelliJ IDEA 控制台中文乱码问题，涉及文…
- [[Junie]] — JetBrains AI coding agent（IDE 内 agent mode 集成）
- [[JetBrains]] — 出品方
- [[摘要-idea-2026-2-必装插件-top100]] — 2026.2 更新与 100 插件盘点
- [[GitHubCopilot]] — 2026.2 起原生内置
- [[通义灵码]] — 同台竞争的国产 AI 插件
- [[Logpoints]] — 2026.2 新增内置调试方式
- [[MCP]] — 2026.2 升格为一等公民
- [[ACP]] — Agent 接入协议（2026.1 起原生支持）
- [[idea-ai-assistant-guide]] — IDEA AI Assistant 能力全貌
- [[摘要-idea五款代码质量检查插件]] — 五款代码质量检查插件的选型与用法
- [[静态代码检查]] — 这些插件对应的概念
