---
title: "摘要-windows-cli-引号陷阱"
type: source
tags: [来源, 原始文件, Windows, CLI, Shell, 踩坑]
sources: [raw/09-archive/2026-09-29-Windows 下 CLI 参数的引号陷阱：为什么 --resume 'uuid' 会失败 - fox_charon.md]
last_updated: 2026-10-08
---

## 核心摘要
在 Windows 终端执行 `qoderclicn --resume '0691d0aa-...'` 报"找不到对应的 session"，去掉单引号后正常——根因是 Unix 与 Windows shell 的引号语义差异：cmd.exe 不认单引号，把 `'` 当普通字符连同 UUID 原样传给程序，程序实际收到 `'0691d0aa-...'`（首尾各多一个单引号），匹配 session ID 自然失败。三种 shell 行为对比：Bash/Zsh 单引号是强引用会剥掉引号、双引号弱引用允许变量展开；cmd.exe 单引号是字面字符原样传递、双引号弱引用剥掉引号；PowerShell 单双引号都会剥引号（单引号强引用不展开、双引号弱引用展开变量）。Bash 中 `--resume 'uuid'`、`--resume "uuid"`、`--resume uuid` 三种写法等价，因为引号处理发生在 shell 层，程序拿到的永远是去引号后的参数——很多开发者习惯"单引号=安全包裹"后照搬到 cmd 就踩坑。规则总结：参数无空格/特殊字符不加引号；含空格（如 `C:\Program Files\...` 路径）用双引号；含 `%` 或 `&` 等 cmd 特殊字符用双引号包裹或转义；跨平台脚本避免单引号。延伸观点：LLM 训练语料以 Linux/macOS 的 Bash 语法为绝对多数，AI 生成 Windows 命令时容易惯性给 UUID、数字等无空格参数加单引号"以防万一"（在 Bash 无害、在 cmd.exe 就是 bug），给 AI 写 prompt 时应明确指定目标 shell（cmd/PowerShell/Git Bash）并要求"不含空格的参数不加引号"。

## 关联连接
- [[WindowsShell引号陷阱]] — 本文提炼的核心概念
- [[AI幻觉]] — AI 生成命令惯性加单引号的根因
