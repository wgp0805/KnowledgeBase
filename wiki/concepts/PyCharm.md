---
title: "PyCharm"
type: entity
tags: [工具, IDE, Python, JetBrains]
sources: ["raw/09-archive/2026-10-25-Day02 · 开发环境搭建 - 小嘉游戏.md"]
last_updated: 2026-10-26
---

# PyCharm

## 定义
JetBrains 出品的最流行 Python 专业 IDE，社区版（Community）免费。

## 关键信息
- 官网 jetbrains.com/pycharm 下载 Community 版一路 Next 安装，社区版足够课程使用
- **基本使用流程**：
  1. File → New Project 新建项目（选项目目录，解释器选系统 Python 3.15，PyCharm 会自动创建虚拟环境）
  2. 项目右键 New → Python File 建文件（如 `hello.py`）
  3. 编辑区右键 Run 'hello' 或点右上角绿三角运行，输出显示在 Run 面板
  4. 调试：行号左侧点击设断点（红点），点右上角甲虫图标（Debug），程序在断点处暂停、可逐行查看变量值
  5. File → Settings → Project → Python Interpreter 可切换系统 Python 或虚拟环境
- **带参数运行**：Run → Edit Configurations 在 Parameters 填参数，等价于命令行 `python demo.py hello python`；脚本用 `sys.argv` 打印脚本名（demo.py）、参数个数（`len(sys.argv) - 1`）、参数内容（`['hello', 'python']`）；`sys.argv` 详情 Day10 再讲

## 关联连接
- [[摘要-python-day02-开发环境搭建]] — 来源
- [[JetBrains]] — 出品厂商
- [[IDLE]] — 初学者官方编辑器对照
- [[Anaconda]] — 数据科学全家桶对照
