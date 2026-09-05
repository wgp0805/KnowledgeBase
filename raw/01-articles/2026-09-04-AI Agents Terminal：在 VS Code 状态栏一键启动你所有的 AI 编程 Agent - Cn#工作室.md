---
title: "AI Agents Terminal：在 VS Code 状态栏一键启动你所有的 AI 编程 Agent - Cn#工作室"
source: "博客园"
url: "https://www.cnblogs.com/cnsharp/p/22846543"
date: "2026-09-04T11:25:00Z"
score: 1.0
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# AI Agents Terminal：在 VS Code 状态栏一键启动你所有的 AI 编程 Agent - Cn#工作室

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/cnsharp/p/22846543  
> **抓取日期**: 2026-09-04  
> **相关性评分**: 1.0

[![VS Code Marketplace](https://img.shields.io/visual-studio-marketplace/v/cnsharp.ai-agents-terminal?label=VS%20Code%20Marketplace)](<https://marketplace.visualstudio.com/items?itemName=cnsharp.ai-agents-terminal>)

> 一个 VS Code 扩展，把你本机装好的 AI CLI 编程助手（Claude Code / Codex / Cursor / …）收进状态栏的一个按钮里。

## 我们到底在解决什么问题

如果你同时用着好几个 AI 编程 agent，一定熟悉这套动作：

  1. 打开终端；
  2. 想起来某个 agent 的命令到底是 `claude`、`cursor-agent` 还是 `traecli`；
  3. 想起来它的自动放行参数是 `--dangerously-skip-permissions`、`--full-auto` 还是 `--yolo`；
  4. 想续上刚才的会话，还得记它是 `-r` 还是 `--resume`；
  5. 最要命的：这个 agent 我到底装没装？



每一步都不难，但每一步都是摩擦。而这些信息本来就在你机器上——只是没人帮你收拢起来。

**AI Agents Terminal** 做的事很简单：在 VS Code 右下角放一个 `🤖 AI Agents` 按钮，点开就是**你本机已经装好的** 那些 agent，选一个，直接在一个带 logo 的终端标签页里打开。

## 它长什么样

状态栏右下角有三个按钮——`🤖 AI Agents` 是启动器，`Y` 是 YOLO 模式，`R` 是 Resume 模式：

![状态栏](https://raw.githubusercontent.com/cnsharp/ai-agents-terminal-vsc/main/media/screenshots/statusbar.png)

点击 `🤖 AI Agents` 弹出的 Quick Pick，只列出已安装的 agent，并带上各自的 logo：

![Quick Pick](https://raw.githubusercontent.com/cnsharp/ai-agents-terminal-vsc/main/media/screenshots/dropdown.png)

## 核心特性

### 只显示装了的

这是我觉得最实用的一条。扩展会在**登录 shell** 里跑一次 `<command> --version`，返回码为 0 就算已安装。

之所以强调登录 shell：macOS / Linux 上走 `$SHELL -lc`，Windows 上走 `where`，这样 nvm、fnm、brew、npm-global 这类靠 rc 文件注入 PATH 的安装方式也能被正确探测到——否则很多人的 agent 会被"漏判"成没装。

探测结果会缓存到全局配置里，跨窗口只探测一次，不会每次开窗口都去扫 PATH。

### YOLO 模式（自动放行）

点 `Y` 或按 `Ctrl+Alt+Y`（macOS `Cmd+Alt+Y`）开启。开启后启动 agent 会自动附加它自己的 `skipFlag`，不用再手动敲那一长串参数。

### Resume 模式（续上会话）

点 `R` 或按 `Ctrl+Alt+R`（macOS `Cmd+Alt+R`）开启。开启后启动 agent 会自动附加 `resumeFlag`，接着上一次的会话继续。

两者可以同时开启，参数顺序固定为 `baseArgs` → `skipFlag` → `resumeFlag`。

**关键是：这些 flag 是每个 agent 各自配置的** ，不是全局一刀切。因为现实就是这么乱——Claude 用 `-r`，Codex 和 Cursor 用 `--resume`。

### 17 个内置 agent，开箱即用

`agents.json` 里内置了以下 agent，每个都配好了自己的命令、参数和 logo：

id | 名称 | 命令 | 自动放行参数 (skipFlag) | 续会话参数 (resumeFlag)  
---|---|---|---|---  
claude | Claude Code | `claude` | `--dangerously-skip-permissions` | `-r`  
codex | Codex | `codex` | `--full-auto` | `--resume`  
cline | Cline | `cline` | — | `--taskId`  
codebuddy | CodeBuddy | `codebuddy` | `--permission-mode bypassPermissions` | `-r`  
continue | Continue | `cn` | `--auto` | —  
copilot | Copilot | `copilot` | `--allow-all-tools --allow-all-paths` | `-r`  
cursor | Cursor | `cursor-agent` | — | `--resume`  
gemini | Gemini | `gemini` | `--yolo` | —  
goose | Goose | `goose` | — | `-r`  
hermes | Hermes | `hermes` | — | `-r`  
kilo | Kilo Code | `kilo` | `--auto` | —  
kimi | Kimi | `kimi` | — | `-r`  
openclaw | OpenClaw | `openclaw` | — | —  
opencode | OpenCode | `opencode` | — | —  
pi | Pi | `pi` | — | `-r`  
qoder | Qoder | `qoder` | — | —  
trae | TraeCode | `traecli` | — | `--resume`  
  
（表中 `—` 表示该项未配置，此时对应模式下不追加任何参数。）

### 加自己的 agent，不用改代码

只需要在 `settings.json` 里加一条，连重新编译都不需要：
    
    
    {
      "aiAgentsTerminal.agents": [
        { "command": "myagent", "displayName": "My Agent", "baseArgs": "run", "skipFlag": "--auto", "iconFile": "myagent.png" }
      ]
    }
    

这个数组会和内置的 `agents.json` **按`command` 合并**：

  * 想改内置项 → 加一条相同 `command` 的覆盖项，只写你要改的字段；
  * 想隐藏内置项 → 设 `"enabled": false`；
  * 想加新的 → 用内置里没有的 `command`。



下次打开选择器就生效，运行时实时读取，不用重载窗口。

## 安装

### 从 VS Code 应用市场安装（推荐）

  * 打开 [AI Agents Terminal 市场页面](<https://marketplace.visualstudio.com/items?itemName=cnsharp.ai-agents-terminal>) 点击 **Install**
  * 或在 VS Code 扩展视图里搜索 `AI Agents Terminal`



## 写在最后

这个扩展没有发明任何新能力——它只是把散落在各个 agent、各个终端、各个参数里的东西，收拢到了一个按钮下面。

如果你也在几个 AI agent 之间反复横跳，希望它能省下你每天那几十次的"等等，这个参数叫什么来着"。

项目地址：<https://github.com/cnsharp/ai-agents-terminal-vsc>

应用市场：<https://marketplace.visualstudio.com/items?itemName=cnsharp.ai-agents-terminal>


---
> 原文链接: https://www.cnblogs.com/cnsharp/p/22846543