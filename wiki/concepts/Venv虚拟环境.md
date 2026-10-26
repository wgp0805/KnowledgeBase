---
title: "Venv虚拟环境"
type: concept
tags: [概念, Python, 依赖管理, 隔离]
sources: ["raw/09-archive/2026-10-25-Day02 · 开发环境搭建 - 小嘉游戏.md"]
last_updated: 2026-10-26
---

# Venv虚拟环境

## 定义
Python 标准库内置（3.3 起自带、无需安装）的项目级依赖隔离工具，可理解为给每个项目单独开一个独立的"装包小仓库"。

## 关键信息
- **动机**：不同项目第三方库版本互相打架（项目 A 要 Flask 2、项目 B 要 Flask 3），全装进全局 site-packages 会环境污染、版本冲突、换机跑不起来；核心直觉"每个项目一个环境，各装各的，互不污染"
- **创建**：`cd` 进项目目录后 `py -3 -m venv .venv`；目录名约定带点，主流 IDE 自动识别；用 `py -3` 而非 `python` 是为锁定 Python 3.15.0、防其他版本接管
- **激活**：PowerShell `. .\.venv\Scripts\Activate.ps1`；CMD `.venv\Scripts\activate.bat`；Linux/macOS `source .venv/bin/activate`；成功后提示符前出现 `(.venv)` 标记
- **PowerShell 坑**：报"禁止运行脚本"可先执行 `Set-ExecutionPolicy -Scope Process Bypass -Force`（只放开当前窗口）或改用 CMD；非交互脚本可不激活，直接点名解释器 `.\.venv\Scripts\python.exe -m pip install 包名`，效果等价
- **验证隔离**（作者 3.15.0 本机实测）：全新 venv `pip list` 只有 pip 26.2.1 一个包（全局装了九十个包如 requests/numpy/pytest，一个也看不见）；`sys.executable`/`sys.prefix` 指向项目 `.venv`，`sys.base_prefix` 指向全局解释器（"借来的"）；装 six 1.17.0 后 `pip show six` 的 Location 为 `.venv\Lib\site-packages`，证明包装进小环境未污染全局
- **退出与工程惯例**：`deactivate` 退出（包不删，再激活同一 `.venv` 可继续用）；`.venv/` 写进项目 `.gitignore`，依赖靠 `requirements.txt` 在别处重建，不进版本库
- **后续**：Day03 系统练 venv + pip + requirements.txt
- **边界注记**：本知识库自身因目录 ACL 带 Sandbox/Low Integrity 标签，SYSTEM 账户启动库内 python.exe 报 0xC0000142，故 venv 置于仓库外（`D:\java\KnowledgeBase-venv`，base 为 mise Python 3.15.0，见 wiki/log.md）——是"项目内 .venv"惯例的环境特例，不构成矛盾

## 关联连接
- [[摘要-python-day02-开发环境搭建]] — 来源
- [[Python]] — 标准库所属语言
- [[PyLauncher]] — `py -3 -m venv` 锁定版本创建
- [[Mise]] — 本知识库 venv 实践的多版本底座
