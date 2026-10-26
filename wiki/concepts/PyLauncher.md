---
title: "PyLauncher"
type: entity
tags: [工具, Windows, Python, 版本管理]
sources: ["raw/09-archive/2026-10-25-Day02 · 开发环境搭建 - 小嘉游戏.md"]
last_updated: 2026-10-26
---

# PyLauncher

## 定义
Windows 官方 Python 安装器默认自带的版本启动器 `py`，专门用来管理多个 Python 版本。

## 关键信息
- 随 Windows 安装器默认安装（自定义安装时注意勾上 py launcher）
- **验证**：`py -3 --version` 输出 Python 3.15.0；`py -3` 表示"使用 Python 3 系列解释器"，`py -3.14`、`py -3.15` 可精确指定版本；课程所有"用 3.15 运行"的示例都可用 `py -3` 执行
- **多版本排障**：系统装有多个 Python 分不清时，`py -0` 列出所有已装版本、`py -3.15` 精确调用
- **与 venv 的配合**：创建虚拟环境用 `py -3 -m venv .venv` 而非 `python -m venv`，目的是明确锁定 Python 3.15.0，避免被机器上其他版本顺手接管
- **关联坑**：`python` 命令被微软商店版占用时，在"设置 → 应用执行别名"里关闭，或用官网版并配置 PATH

## 关联连接
- [[摘要-python-day02-开发环境搭建]] — 来源
- [[Venv虚拟环境]] — `py -3 -m venv` 锁定版本创建
- [[Mise]] — 多版本管理的替代路线
- [[Python]] — 管理其多个版本
