---
title: "Python"
type: entity
tags:
  - 语言
  - 生态
sources: ["raw/09-archive/2026-09-27-并发编程（五）：Atomic——语言层的原子性、可见性与有序性 - ThinkerQAQ.md", "raw/09-archive/2026-10-25-Day02 · 开发环境搭建 - 小嘉游戏.md"]
last_updated: 2026-10-26
---

## 定义
通用解释型编程语言，AI 生态的主导语言；requests、aiohttp、httpx 等库的 SOCKS5 代理兼容性差异是常见坑。

## 关键信息
- **应用层没有对称的 Atomic API**（来源：[[摘要-atomic语言层三性质]]）：Python 标准库目前没有与 Java `AtomicInteger`、Go `atomic.Int64` 对称的通用整数 Atomic API；`counter += 1` 不是语言层定义的 Atomic 操作，也不能因某个 CPython 配置存在 GIL、或 Runtime 内部使用 `_Py_atomic_*`，就把它当作应用层可依赖的跨实现 Atomicity/Visibility/Ordering 保证
- `_Py_atomic_*` 如何落到编译器与 CPU 属于 Runtime 实现细节，不是 Python 应用层公开语义的一部分

### 开发环境与版本（来源：[[摘要-python-day02-开发环境搭建]]）
- **版本基准**：课程技术基准为 Python 3.15.0，务必从官网 python.org/downloads 下载（第三方下载站可能捆绑推广软件或旧版本）
- **Windows 安装**：第一步就要勾选 "Add python.exe to PATH"，漏掉会导致 `'python' 不是内部或外部命令`（修复：重装勾选，或手动把 `C:\Users\你的用户名\AppData\Local\Programs\Python\Python315\` 与 `...\Scripts\` 加入系统环境变量 PATH）
- **验证命令**：`python --version`、`py -3 --version`；REPL 交互模式提示符 `>>>`，`exit()` 或 Ctrl+Z 退出
- **跨平台**：macOS 用官网安装包或 `brew install python@3.15`；Ubuntu/Debian 用 `sudo apt install python3`，日常推荐 apt 自带版本再叠加 pyenv 管理多版本
- **编码**：Python 3 源码默认 UTF-8（中文乱码先检查文件保存编码；Windows 控制台可执行 `chcp 65001` 切换 UTF-8 代码页）
- **语法边界**：`print` 在 Python 3 中是函数必须加括号，`print "hi"` 属 Python 2 遗留写法，在 3.15 中直接报 SyntaxError

## 关联连接
- [[FastAPI]]
- [[SOCKS5]]
- [[摘要-socks5代理认证兼容性问题]]
- [[原子性-可见性-有序性]] — 三语言 Atomic 对照中的 Python 结论
- [[AtomicInteger]] — Java 侧对照
- [[Golang]] — Go 侧对照
- [[摘要-atomic语言层三性质]] — 来源
- [[摘要-python-day02-开发环境搭建]] — 来源（开发环境与版本增补）
- [[Venv虚拟环境]] — 标准库内置的项目级依赖隔离工具
- [[PyLauncher]] — Windows 版本启动器 `py`
- [[IDLE]] — 官方自带轻量 IDE
- [[PyCharm]] — JetBrains 专业 IDE
- [[Anaconda]] — 数据科学发行版
