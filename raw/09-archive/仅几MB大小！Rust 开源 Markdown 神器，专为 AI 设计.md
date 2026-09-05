---
title: "仅几MB大小！Rust 开源 Markdown 神器，专为 AI 设计"
source: "https://mp.weixin.qq.com/s/vrGZtCUHjtcRDVAo_x1xxQ"
---
java1234 *2026年7月16日 09:06*

大家好，我是锋哥。

今天分享一个非常火爆的开源项目 - markamd

![图片](assets/%E4%BB%85%E5%87%A0MB%E5%A4%A7%E5%B0%8F%EF%BC%81Rust%20%E5%BC%80%E6%BA%90%20Markdown%20%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%93%E4%B8%BA%20AI%20%E8%AE%BE%E8%AE%A1/25b6ae80bce8f1a93f632e1643bf75b5_MD5.webp)

---

## 目录

- 写在前面
- [marka.md](http://marka.md/) 是什么？
- 为什么说是「专为 AI 设计」？
- 核心工作流
- 主要功能一览
- 技术栈：Rust 做壳，前端做面
- 安装与上手

---

## 写在前面

如果你经常用 Claude、ChatGPT、Gemini 或者本地 AI 助手写东西，大概率遇到过这种场景：项目里散落着一堆 `.md` 笔记，要发给 AI 时得一个个打开、复制、粘贴，文件名和路径还乱糟糟的。

[marka.md](http://marka.md/) 就是来解决这个问题的——一款 **本地优先** 的 Markdown 编辑器，安装包只有几 MB，底层用 Rust + Tauri 构建，体积远小于常见的 Electron 应用，却专门围绕「整理笔记 → 编辑 → 打包发给 AI」这条链路做了优化。

---

## marka.md 是什么？

一句话概括： **一款安静、轻量的本地 Markdown 编辑器，帮你把笔记整理成 AI 能直接读懂的上下文包。**

它不像 Obsidian 那样功能庞杂，也不像 VS Code 那样什么都往里塞。 [marka.md](http://marka.md/) 只做一件事，并把它做好：

> 收集笔记 → 编写内容 → 一键复制，粘贴给 AI

你的文件始终保存在本地硬盘上， **没有账号、没有云同步、没有遥测** 。数据离开你的电脑，只发生在你主动点击「复制」的那一刻。

---

## 为什么说是「专为 AI 设计」？

市面上 Markdown 编辑器不少，但 [marka.md](http://marka.md/) 在 AI 场景下有几个很实用的设计：

**1\. Context Tray（上下文托盘）**

侧边栏里可以把多个 Markdown 文件「暂存」起来，编辑器会实时显示文件数量和 Token 估算。准备好之后，一键复制成一个 **AI 就绪的上下文包** ，粘贴到任意 AI 对话窗口即可。

**2\. 相对路径，不泄露本机信息**

打包出来的内容使用相对路径，保留项目结构，但不会把 `C:\Users\xxx\...` 这类本地绝对路径暴露给 AI。

**3\. 未保存的编辑也会带上**

当前正在编辑、还没保存的文件，复制上下文包时会用编辑器里的最新内容，不用担心改了一半忘记保存。

**4\. 兼容所有「能读文本」的 AI**

Claude、ChatGPT、Gemini、Cursor、本地 Agent……只要接受纯文本 Markdown，都能直接用。

![图片](assets/%E4%BB%85%E5%87%A0MB%E5%A4%A7%E5%B0%8F%EF%BC%81Rust%20%E5%BC%80%E6%BA%90%20Markdown%20%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%93%E4%B8%BA%20AI%20%E8%AE%BE%E8%AE%A1/329f78f5e04fd8839ad91a9b55314917_MD5.jpg)

---

## 核心工作流

[marka.md](http://marka.md/) 的整个使用逻辑可以用下面这张图概括：

![图片](assets/%E4%BB%85%E5%87%A0MB%E5%A4%A7%E5%B0%8F%EF%BC%81Rust%20%E5%BC%80%E6%BA%90%20Markdown%20%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%93%E4%B8%BA%20AI%20%E8%AE%BE%E8%AE%A1/f2827f6549e4ba17d27c501dbf6d886e_MD5.png)

三步走： **收集 → 编写 → 分享** 。没有多余步骤，也没有学习曲线。

---

## 主要功能一览

| 类别 | 功能 |
| --- | --- |
| 写作体验 | 左右分屏实时预览、Shiki 代码高亮、Mermaid 图表、任务列表、阅读模式、可选 Vim 模式 |
| AI 上下文 | Context Tray 暂存多文件、Token 计数、一键复制 Bundle |
| 文件管理 | 多标签页、文件夹侧边栏、收藏夹、搜索、拖拽移动、撤销文件操作 |
| 导出 | PDF 导出、代码块一键复制 |
| 个性化 | 14 套主题（含 Claude / Cursor / Gemini 等品牌色）、透明度调节、会话恢复 |

值得一提的是「懒加载」策略：Shiki 主题和语言包、Mermaid 渲染器都只在真正用到时才加载，启动快、占内存也控制得比较克制。

---

## 技术栈：Rust 做壳，前端做面

[marka.md](http://marka.md/) 的架构是典型的 Tauri 应用模式——Rust 负责桌面壳和系统能力，Web 技术负责界面和编辑体验。

![图片](assets/%E4%BB%85%E5%87%A0MB%E5%A4%A7%E5%B0%8F%EF%BC%81Rust%20%E5%BC%80%E6%BA%90%20Markdown%20%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%93%E4%B8%BA%20AI%20%E8%AE%BE%E8%AE%A1/129f3b79502d8b2bc76eaf383e0f3b19_MD5.png)

| 层级 | 技术选型 |
| --- | --- |
| 桌面壳 | Tauri 2.11（Rust + 系统 WebView） |
| 前端 | React 19 + Vite 7 + TypeScript |
| 编辑器 | CodeMirror 6，可选 Vim 模式 |
| 渲染 | markdown-it + Shiki + Mermaid |

---

## 安装与上手

**macOS**

- Homebrew： `brew install --cask mattenarle10/tap/marka-md`
- 或从 [https://github.com/mattenarle10/markamd/releases/latest](https://github.com/mattenarle10/markamd/releases/latest) 下载 `.dmg` 安装

**Windows 10+**

- 下载 `              marka.md_*-setup.exe            ` 运行即可（首次可能需通过 SmartScreen 确认）

**Linux**

- AppImage（通用）、`.deb` （Debian/Ubuntu 系）、`.rpm` （Fedora/RHEL 系）三种格式任选

几个常用快捷键（Windows/Linux 把 ⌘ 换成 Ctrl）：

| 快捷键 | 作用 |
| --- | --- |
| ⌘K | 命令面板 |
| ⌘⇧O | 打开文件夹 |
| ⌘⇧C | 复制 Markdown 到剪贴板 |
| ⌘. | 切换阅读模式（仅预览） |
| ⌘P | 导出 PDF |

---

项目地址：

[https://github.com/mattenarle10/markamd](https://github.com/mattenarle10/markamd)

[2026年，锋哥又开始收Python+AI大模型学员了！目前活动，送AI编程+Java编程 VIP](https://mp.weixin.qq.com/s?__biz=MzkxNzQ5ODQ1Nw==&mid=2247492744&idx=1&sn=c83350935458250c6d0a6084302bd3b7&scene=21#wechat_redirect)

最近锋哥录制了一些AI编程视频教程

![图片](assets/%E4%BB%85%E5%87%A0MB%E5%A4%A7%E5%B0%8F%EF%BC%81Rust%20%E5%BC%80%E6%BA%90%20Markdown%20%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%93%E4%B8%BA%20AI%20%E8%AE%BE%E8%AE%A1/dc637afc5701a580aa932b71f5a5aa35_MD5.webp)

高清视频+源码+领取。

```
扫描下方公众号【小锋学AI 】回复：888，可获取下载链接👇👇👇
👆长按上方二维码 2 秒回复「888」即可获取
```