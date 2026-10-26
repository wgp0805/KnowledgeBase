---
title: "IDLE"
type: entity
tags: [工具, IDE, Python, 入门]
sources: ["raw/09-archive/2026-10-25-Day02 · 开发环境搭建 - 小嘉游戏.md"]
last_updated: 2026-10-26
---

# IDLE

## 定义
Python 官方自带的轻量 IDE（Integrated Development and Learning Environment），随安装包一同提供、零配置，特别适合初学者。

## 关键信息
- 随官网安装包一同提供，零配置；打开方式为开始菜单搜 "IDLE" 或命令行 `python -m idlelib`
- **两种模式**：启动即 `>>>` 提示符的交互模式（适合试小段代码）；File → New File 新建 `.py` 的脚本模式，写多行代码后按 F5（Run Module）运行、输出显示在 Shell 窗口
- **常用快捷键**：F5 运行当前脚本、Alt+P/Alt+N 上/下一条历史命令（交互模式）、Tab 自动补全、Ctrl+C 中断运行中的程序
- 第一个脚本 `hello.py`：`print("Hello, World!")`，按 F5 运行，Shell 输出 Hello, World!
- **两个坑**：① 新建文件必须先保存为 .py 才能按 F5 运行（否则报错）；② `print` 在 Python 3 中是函数必须加括号，`print "hi"` 属 Python 2 遗留写法，在 3.15 中直接报 SyntaxError
- 工具分工定位：初学用 IDLE、专业开发用 [[PyCharm]]、数据科学用 [[Anaconda]]

## 关联连接
- [[摘要-python-day02-开发环境搭建]] — 来源
- [[Python]] — 语言本体
- [[PyCharm]] — 进阶专业 IDE 对照
