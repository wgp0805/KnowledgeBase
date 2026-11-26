---
title: "GitHub 38.1k Star 杀疯了！这个能联动 IDE 的终端 AI 编程神器你用了吗？"
source: "https://mp.weixin.qq.com/s/3emJgOj0y-dJBZzg0FtJ5Q"
author:
  - "[[程序汪]]"
published:
created: 2026-11-26
description:
tags:
  - "clippings"
---
程序汪 我是程序汪 *2026年11月26日 10:37*

大家好，我是程序汪。

> 在终端里跑 AI 编程助手这两年很普遍，但大多数对项目的理解停留在文本层面，不知道类型、引用和调试符号，改代码靠字符串匹配，遇到重命名、跨文件引用就容易出错。最近看了一个叫 oh-my-pi（命令名 omp）的开源项目，思路不太一样，它把 LSP、调试器这些 IDE 才有的能力接进了终端代理。

目录

一、omp 是什么

二、把 IDE 的能力接进终端

三、工具和代码执行

四、模型、配置和协作

五、短板和适用人群

---

## 一、omp 是什么

oh-my-pi 在命令行里叫 omp，由 Stencil Labs 出品，基于 Mario Zechner 的 Pi 项目 fork 扩展，采用 MIT 协议。代码用 TypeScript 和 Rust 写成，Rust 核心约 8 万行，运行时用 Bun，macOS、Linux、Windows 都能跑，Windows 上不需要 WSL。

它是一个跑在终端里的 TUI 编码代理。官方给出的数据是：60 多个模型提供商、31 个内置工具、14 个 LSP 操作、28 个 DAP 调试操作。

---

## 二、把 IDE 的能力接进终端

这是它和普通终端代理区别最大的地方。

LSP 方面，每次写文件都经过语言服务器。比如重命名，调用的是 `workspace/willRenameFiles`，文件移动之前，re-export、barrel 文件和别名导入会一起更新，和你在 VS Code 里做重命名是同一套机制，不会留下一堆没改干净的引用。

![图片](assets/GitHub%2038.1k%20Star%20%E6%9D%80%E7%96%AF%E4%BA%86%EF%BC%81%E8%BF%99%E4%B8%AA%E8%83%BD%E8%81%94%E5%8A%A8%20IDE%20%E7%9A%84%E7%BB%88%E7%AB%AF%20AI%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%E4%BD%A0%E7%94%A8%E4%BA%86%E5%90%97%EF%BC%9F/23d131ee216ff51ef69fee4f22c92f5e_MD5.gif)

omp 启动页，TypeScript 和 Biome 语言服务器处于运行状态

调试方面，它能直接驱动真实调试器。C 程序段错误可以挂 lldb 单步走到出错的指针，Go 服务卡住可以挂 dlv 查看 goroutine，Python 进程可以挂 debugpy 暂停后检查变量，不用靠到处加 print 来排查。

---

## 三、工具和代码执行

内置工具是原生实现，不是 shell 调外部命令。ripgrep、glob、find 都在进程内运行，还自带 bash 5.3 引擎和 58 个命令，包括 ls、sed、sort、jq，省掉了 fork/exec 的开销，所以在没装这些命令的机器上也能正常用。

代码执行部分提供持久的 Python 和 Bun 内核，内核还能反过来调用代理自己的 read、search 工具。可以在 Python 里读 CSV，再到 JavaScript 里画图，整个过程不离开当前会话。

![图片](assets/GitHub%2038.1k%20Star%20%E6%9D%80%E7%96%AF%E4%BA%86%EF%BC%81%E8%BF%99%E4%B8%AA%E8%83%BD%E8%81%94%E5%8A%A8%20IDE%20%E7%9A%84%E7%BB%88%E7%AB%AF%20AI%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%E4%BD%A0%E7%94%A8%E4%BA%86%E5%90%97%EF%BC%9F/72326d1fbc66f6c9a0182afa4409c699_MD5.png)

omp 会话内运行 Python 并用 matplotlib 渲染谐波图

文件编辑用的是 hashline，按内容哈希定位锚点，而不是把要改的整段重写一遍，空白冲突和字符串找不到的情况少了很多，输出 token 也随之下降。另外它有流式规则机制：规则平时不占上下文，模型一旦偏离要求，正则匹配会在生成中途中断，把规则注入后从断点重新生成。

---

## 四、模型、配置和协作

模型不绑定厂商，60 多个 provider 都支持，Anthropic、OpenAI、Gemini、Grok、MiniMax 可以用 `/model` 随时切换，还能额外配一个 advisor 模型，在旁边审查每一轮的输出。

配置上可以直接读取 Cursor、Cline、Codex 的 [AGENTS.md](http://agents.md/) 等八种已有文件，不需要迁移。扩展中心里能统一管理 skills 和各 provider 的配置。

![图片](assets/GitHub%2038.1k%20Star%20%E6%9D%80%E7%96%AF%E4%BA%86%EF%BC%81%E8%BF%99%E4%B8%AA%E8%83%BD%E8%81%94%E5%8A%A8%20IDE%20%E7%9A%84%E7%BB%88%E7%AB%AF%20AI%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%E4%BD%A0%E7%94%A8%E4%BA%86%E5%90%97%EF%BC%9F/89e30d1dd580fdedc2fbf9dc42b7c8da_MD5.png)

扩展控制中心，集中管理 skills、上下文和各 provider 配置

子代理用 `task` 命令把任务拆到隔离的 worktree 里并行处理，返回带 schema 校验的结果，按 `Alt+A` 可以查看每个子代理的实时状态。协作方面，`/collab` 会生成链接和二维码，同事在别的终端或浏览器就能加入同一个会话，数据帧在客户端加密。代码审查用 `/review`，针对分支、提交或未提交改动给出结论，问题按 P0 到 P3 分级。

![图片](assets/GitHub%2038.1k%20Star%20%E6%9D%80%E7%96%AF%E4%BA%86%EF%BC%81%E8%BF%99%E4%B8%AA%E8%83%BD%E8%81%94%E5%8A%A8%20IDE%20%E7%9A%84%E7%BB%88%E7%AB%AF%20AI%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%E4%BD%A0%E7%94%A8%E4%BA%86%E5%90%97%EF%BC%9F/ef218c69caa38205b56df2558e549b75_MD5.gif)

审查模式菜单，可选择按基线分支、提交或未提交改动审查

安装方式覆盖了主流平台：

```
# macOS / Linux 一键安装，安装过程会校验 SHA-256
curl -fsSL 
            https://omp.sh/install
           | sh
# 或者用 bun 安装
bun install -g @oh-my-pi/pi-coding-agent
# Homebrew
brew install can1357/tap/omp
# Windows PowerShell：irm 
            https://omp.sh/install.ps1
           | iex
```

---

## 五、短板和适用人群

- 项目很新，2025 年 12 月底才建仓，迭代速度快，目前 open issues 有 4000 多条，实际使用中可能遇到不稳定；
- 功能和配置项都多，上手成本比简单的聊天式代理高，需要理解 LSP、DAP 这些概念才能用好；
- 完整能力要配合模型 API Key，本地跑大模型另算，调用费用和其他 AI 工具一样客观存在；
- 它面向的是需要 IDE 级操作、认真写代码的开发者，不是想找一个简单问答工具的人。

项目地址： [https://github.com/can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)