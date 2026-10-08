---
title: "WindowsShell引号陷阱"
type: concept
tags: [踩坑, Windows, CLI, Shell, 跨平台]
sources: [raw/01-articles/2026-09-29-Windows 下 CLI 参数的引号陷阱：为什么 --resume 'uuid' 会失败 - fox_charon.md]
last_updated: 2026-10-08
---

## 定义
Windows 的 cmd.exe 不把单引号 `'...'` 当作引号、而是当字面字符原样传给程序，导致沿用 Bash 习惯写的 `--resume 'uuid'` 实际把首尾两个 `'` 一起传入，参数匹配失败。根因是 Unix 与 Windows shell 的引号语义差异，是跨平台开发者与 AI 生成命令的高频坑。

## 关键信息
- **三 shell 对比**：Bash/Zsh 单引号强引用（剥引号、内容原样）、双引号弱引用（剥引号、允许变量展开）；cmd.exe 单引号是字面字符（原样传给程序）、双引号剥引号；PowerShell 单引号强引用剥引号（不展开）、双引号弱引用剥引号（展开变量）
- **现象**：`--resume '0691d0aa-...'` 报找不到 session，去掉引号正常——程序收到的是 `'0691d0aa-...'`
- **Bash 为何无感**：引号处理发生在 shell 层，程序永远拿到去引号后的参数，三种写法 `'uuid'`、`"uuid"`、`uuid` 等价
- **规则**：参数无空格/特殊字符 → 不加引号；含空格（如 `C:\Program Files\...`）→ 双引号；含 `%`、`&` 等 cmd 特殊字符 → 双引号包裹或转义；跨平台脚本 → 避免单引号，用双引号或干脆不加
- **AI 生成命令的系统性偏差**：LLM 训练语料以 Linux/macOS Bash 语法占绝对多数，生成 Windows 命令时容易惯性给 UUID、数字等无空格参数加单引号"以防万一"（Bash 里无害，cmd.exe 里就是 bug）
- **Prompt 对策**：给 AI 写 Windows 命令时明确指定目标 shell（cmd / PowerShell / Git Bash），并要求"不含空格的参数不加引号"

## 关联连接
- [[摘要-windows-cli-引号陷阱]] — 来源
- [[AI幻觉]] — AI 惯性套用 Bash 语法的现象根因
- [[Windows]] — 陷阱发生的平台
