---
title: "Claude Code 自定义状态栏工具：安装、配置与 Subagent 状态展示 - fbincon"
source: "博客园"
url: "https://www.cnblogs.com/fbincon/p/23347837"
date: "2026-10-18T12:47:00Z"
score: 1.0
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# Claude Code 自定义状态栏工具：安装、配置与 Subagent 状态展示 - fbincon

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/fbincon/p/23347837  
> **抓取日期**: 2026-10-18  
> **相关性评分**: 1.0

> 摘要：本文介绍一个Claude Code 自定义状态栏工具 claude-code-statusline，并说明安装与 Claude Code 接入，配置显示模型、Git、上下文、token 和任务用时等，通过终端界面或 CLI 配置主状态栏、子 Agent 行及可选实时指标。

## 一、为什么给 Claude Code 加一个状态栏？

用 Claude Code 做任务时，除了看回复内容，我们还会关心：当前使用什么模型、正在操作哪个目录、Git 工作区有没有变化、上下文还剩多少，以及这次任务已经运行了多久。

**claude-code-statusline** 这个工具把这些信息集中到会话底部，并提供可配置的子 Agent 状态行。主栏支持 60 个显示项，子 Agent 行支持 14 个显示项，可以按自己的工作习惯选择和排序。

刚开始使用时，保留模型、目录、Git、上下文余量和任务用时就够了。下面从安装开始，逐步配出一套日常可用的界面。

## 二、准备环境，完成安装与接入

### 2026.10.18 更新：TypeScript 重构与 npm 安装

仓库已使用 **TypeScript 重构原 Python 实现** 。从 **v3.0.0** 开始，软件包通过 npm 分发，后续新版不再支持通过 pipx 安装或更新；Python/pipx 方式保留用于历史版本。

工具版本 | 安装与更新方式 | 软件包名  
---|---|---  
v2.0.0 及之前 | Python + pipx；pipx 支持的最后一个版本为 v2.0.0 | `fbincon-claude-code-statusline`  
v3.0.0 及之后 | Node.js + npm；npm 分发的首个正式版本为 v3.0.0 | `@fbincon/claude-code-statusline`  
  
已有 pipx 安装的用户，请先阅读第七节新增的“从 Python/pipx 迁移到 npm”，再切换安装方式。

#### 1\. 准备新版运行环境

平台 | 运行环境  
---|---  
Linux / WSL | Node.js 22.x 或 24.x，x64  
Windows 10/11 | Node.js 22.x 或 24.x，x64  
macOS 14+ | Node.js 22.x 或 24.x，Intel / Apple Silicon  
  
Windows ARM 设备使用 x64 Node 仿真；原生 Windows ARM64 和 32 位运行时暂不在支持范围。WSL 用户在 WSL 内安装，并使用同一环境中的 Claude Code。

先准备 Node.js、npm 和 Claude Code CLI，在终端检查：
    
    
    node --version
    npm --version
    claude --version
    

要显示 Git 信息，还需让 `git --version` 正常运行。新版 npm 包已包含受支持平台的原生依赖，正常安装和运行无需 Python、pipx 或编译器。

#### 2\. 安装 npm 软件包

首次安装新版，在 Bash、Zsh 或 PowerShell 中执行：
    
    
    npm install --global --ignore-scripts @fbincon/claude-code-statusline
    

安装后确保 npm 的全局命令目录位于 PATH 中；调整 PATH 后重新打开终端。

运行命令仍为 `claude-statusline`。**Windows 的 npm 入口使用`claude-statusline.cmd`**，本节新增步骤及后文通用配置命令均按此替换；原文中的 `claude-statusline.exe` 对应历史 Python/pipx 安装。

#### 3\. 将新版接入 Claude Code

在终端依次执行；Windows 将命令名替换为 `claude-statusline.cmd`：
    
    
    claude-statusline --version
    claude-statusline install --dry-run
    claude-statusline install
    claude-statusline doctor
    

`--version` 确认实际运行的是新版；`install --dry-run` 预览接入改动；`install` 写入本工具的 Claude Code 接入；`doctor` 检查环境与接入状态。**npm 安装软件包后，还需要执行接入步骤** 。检查通过后，在受信任终端重启 Claude Code，加载状态栏、命令和插件。

兼容宿主上的两个编辑器入口默认启用，保留已有明确关闭偏好；原生计时与高级实时采集的新安装默认值见第六节更新。若遇到已有状态栏或同名入口冲突，按[新版冲突处理说明](<https://github.com/fbincon/claude-code-statusline/blob/v3.1.0/docs/USER_GUIDE.zh-CN.md#%E5%A4%84%E7%90%86%E5%B7%B2%E6%9C%89-statusline-%E6%88%96%E5%90%8C%E5%90%8D-skill>)检查归属后处理。

### **以下保留原 Python/pipx 安装与接入内容，适用于 v2.0.0 及之前。** 如需明确安装最后一个 Python 版，可执行 `pipx install "fbincon-claude-code-statusline==2.0.0"`；这一路径不会安装 npm 新版。

#### 1\. 检查前置环境

平台 | Python 环境  
---|---  
Linux / WSL | Python 3.10+  
Windows 10/11 | CPython 3.10–3.14，x86/x64；自动安装 windows-curses 依赖  
macOS 14+ | 提供 curses 的 CPython 3.10–3.14，Intel / Apple Silicon  
  
Windows ARM 设备可使用 x64 Python 仿真，原生 ARM64 Python 暂不在支持范围。WSL 用户在 WSL 内完成安装，并使用同一环境中的 Claude Code。

在 Linux、WSL、macOS 终端检查 Python：
    
    
    python3 --version
    

Windows PowerShell 使用 Python 启动器检查；未安装启动器时可用 `python --version`：
    
    
    py --version
    

还需要 pipx，用它管理这个命令行工具。缺少环境时，按 [Python 官方下载页](<https://www.python.org/downloads/>)选择表中支持的版本，按 [pipx 官方安装说明](<https://pipx.pypa.io/latest/how-to/install-pipx.html>)完成安装，再检查：
    
    
    pipx --version
    claude --version
    

要显示 Git 信息，还需让 `git --version` 能正常运行。

#### 2\. 安装软件包

下面的单行命令适用于 Bash、Zsh 和 PowerShell：
    
    
    pipx install fbincon-claude-code-statusline
    pipx ensurepath
    

执行后**重新打开终端** ，让 PATH 更新生效。安装包名是 `fbincon-claude-code-statusline`，运行命令是 `claude-statusline`。Windows 将下文的命令名替换为 `claude-statusline.exe`，参数相同。

#### 3\. 接入 Claude Code

在新终端依次执行：
    
    
    claude-statusline --version
    claude-statusline install --dry-run
    claude-statusline install
    claude-statusline doctor
    

第一条确认工具可用；`--dry-run` 预览接入修改；`install` 写入接入配置；`doctor` 检查当前环境与集成状态。软件包安装和 Claude Code 接入是两个步骤。

检查通过后，在受信任终端重启 Claude Code，底部应出现状态栏。已有第三方状态栏或同名配置入口时，先按[冲突处理说明](<https://github.com/fbincon/claude-code-statusline/blob/v1.7.5/docs/USER_GUIDE.zh-CN.md#%E5%A4%84%E7%90%86%E5%B7%B2%E6%9C%89-statusline-%E6%88%96%E5%90%8C%E5%90%8D-skill>)处理。

## 三、先理解状态栏里的信息

信息 | 主要含义  
---|---  
模型与 effort | 当前模型，以及宿主提供的思考强度  
当前目录 | 当前会话所在的工作目录  
Git | 分支、与上游的提交差距、工作区变化  
Context remaining | 当前上下文窗口的剩余比例  
使用限额 | 宿主提供的五小时、每周或网关额度  
Token | 当前会话累计记录的输入、缓存和输出用量  
Task total time | 当前或最近一次人类任务的总耗时  
  
Git 中的 `↑N`、`↓N` 表示领先、落后上游的提交数；`●N` 是暂存文件数，`~N` 是未暂存文件数，`?N` 是未跟踪文件数，`!N` 是冲突文件数。非 Git 目录会省略这一项。

`Context 73% left` 表示上下文窗口还剩约 73%。它与账户限额、会话累计 token 分别统计。`tokens` 中，`hit` 是缓存读取输入，`miss` 是普通输入与缓存创建之和，`out` 是输出；统计包含可发现的子 Agent transcript。

任务计时包含排队、用户等待、所属子 Agent 工作和主 Agent 收尾。`⏱` 表示运行，`✓` 表示成功，`■` 表示中断，`✗` 表示失败。需要排除已核实的用户等待时，可另选 `task-active-timer`；只有原生计时观测完整时才显示。

这些字段依赖宿主输入或本地记录，缺失时可能省略。完整口径见[显示项与指标定义](<https://github.com/fbincon/claude-code-statusline/blob/v1.7.5/docs/DISPLAY_ITEMS.zh-CN.md>)。

## 四、通过终端界面调整显示内容

### 1\. 先用独立 TUI 配置

在 Claude Code 外的真实终端运行：
    
    
    claude-statusline configure
    

窗口至少需要 64×18。进入后，可以看到四个页面：

页面 | 用途  
---|---  
Main | 选择主状态栏条目，调整顺序  
Subagents | 配置子 Agent 独立行  
Settings | 设置颜色、格式、目录样式、刷新行为及预设  
Layout | 设置分行、条目优先级和最大宽度  
  
  
_图 1：Main 页面。下方 Preview 使用固定样例数据，用于检查排版。_

可以先在 Main 页选一个条目，用 Space 开关，再用左右方向键调整顺序；输入文字可筛选条目。需要修改单项标签、图标或格式时，选中后按 Ctrl+E。

独立／外部 TUI 按键 | 操作  
---|---  
Tab / Shift+Tab | 切换页面  
↑ / ↓、Space、← / → | 选择、开关、排序或调整设置值  
Ctrl+E / Ctrl+G | 打开逐项格式／返回或取消输入  
Ctrl+S | 完成字段输入后保存完整草稿  
Esc | 先取消输入；未处于输入状态时放弃草稿退出  
  
Enter 在项目页可保存，在高级字段中用于编辑或确认输入。**保存整份配置统一用 Ctrl+S** ，更容易记住。回到 Claude Code 后，下一次状态栏刷新会使用新配置。

### 2\. 在 Claude Code 内启动配置

下面两条命令输入到 **Claude Code 会话** ，按需选择一个：

命令 | 打开位置 | Claude Code 版本  
---|---|---  
`/statusline-configure` | 支持的外部终端中打开同一个 TUI | 2.1.258+  
`/statusline-configure-native` | 当前会话内的 Client 配置面板 | 2.1.287+  
  
外部入口在 Linux 使用 tmux 或 GNOME Terminal，在 macOS 使用 tmux 或 Terminal.app，在 Windows 使用新控制台；启动器不可用时使用独立 `configure`。

会话内 Client 打开后，先点击面板区域，再用键盘。它的保存方式是 **S 保存留页、F 保存并退出、Q 放弃未保存修改** ；取消字段输入用 Ctrl+G。按页面底部提示操作即可。

各入口共享当前用户的配置，对该配置目录下的 Claude Code 项目生效。`/statusline-config` 则提供问答配置，会使用模型回合；状态栏渲染本身读取宿主输入和本地状态，不额外发起网络请求或消耗模型 token。

下面按平台展示会话内配置面板，点击对应标题展开。截图中的 **Preview 是固定样例数据** ，会话底部的主状态栏显示会话数据。

Linux：会话内 Main、Subagents、Settings、Layout（点击展开）

**Main：选择主状态栏条目并调整顺序。**

**Subagents：配置子 Agent 独立行及条目顺序。**

**Settings：调整外观、刷新行为与显示格式。**

**Layout：设置分行、条目优先级与最大宽度。**

Windows：会话内 Main、Subagents、Settings、Layout（点击展开）

**Main：选择主状态栏条目并调整顺序。**

**Subagents：配置子 Agent 独立行及条目顺序。**

**Settings：调整外观、刷新行为与显示格式。**

**Layout：设置分行、条目优先级与最大宽度。**

macOS：会话内 Main（点击展开）

**Main：主状态栏条目配置与样例预览。**

当前仅提供 Main 截图。macOS 会话内 Client 仍有已记录的输入交互限制，截图不代表问题已解决；遇到操作问题时，可在独立终端使用 `claude-statusline configure`。

## 五、三组可以直接使用的配置

以下命令都在系统终端执行。前两组是主栏的两种选择，第三组单独配置子 Agent 行。`set-items` 会**替换该栏启用集合并确定顺序** ；想追加某项时用 `enable`。

### 1\. 精简开发视图
    
    
    claude-statusline config set-items model-with-effort current-dir git context-remaining task-timer
    claude-statusline config set directory-style home
    claude-statusline config set separator-style compact
    claude-statusline config show
    

这组保留模型、目录、Git、上下文余量和任务用时。`home` 会将主目录前缀缩写为 `~`，`compact` 使用紧凑分隔符；`show` 可确认保存结果。

如果希望主栏分为两行，接着执行：
    
    
    claude-statusline config layout explicit model-with-effort,current-dir,git context-remaining,task-timer
    

每个参数表示一行，逗号连接同行条目，顺序与刚才启用的条目一致。在 Layout 页也能设置行边界，并为重要条目分配较高优先级、为长目录限制宽度。

  
_图 2：Layout 页面；截图中的 Preview 为样例数据。自动布局会折行，显式布局在宽度不足时按限制截短并精简低优先级项。_

### 2\. 限额与 token 视图
    
    
    claude-statusline config set-items five-hour-limit weekly-limit spend-limit tokens
    claude-statusline config layout auto
    

适合主要关注用量的场景。`spend-limit` 依赖宿主和网关提供的额度数据，账户或端点未提供时会省略；选择显示项不会让缺失数据自动出现。

### 3\. 子 Agent 状态行

子 Agent 行需要 Claude Code 2.1.205+，逐任务 effort 需 2.1.214+。默认已启用自定义行，可设置为：
    
    
    claude-statusline config subagents set-items status-elapsed name model-with-effort context-remaining task
    claude-statusline config set subagent-hide-completed on
    claude-statusline config set subagent-row-limit 6
    

真实任务运行子 Agent 时，每行会展示对应任务的状态与用时、名称、模型、上下文和任务标签。上述设置隐藏已完成代理，最多显示六行。主栏仍属于主会话，每条子 Agent 行使用自己的任务数据；子 Agent 的 `tokens` 表示上下文占用。

  
_图 3：Subagents 页面及样例预览，展示子 Agent 行的可配置内容。_

### 4\. 用预设起步，保存自己的方案

也可以从 `minimal`、`developer`、`monitoring`、`multi-agent` 四套预设开始。例如先预览，再应用开发预设：
    
    
    claude-statusline config preset developer --dry-run
    claude-statusline config preset developer
    

预设展开后仍可编辑。在 Settings 中调整颜色、数字和模型名称格式；Main/Subagents 中的 Ctrl+E 可覆盖单项格式。

满意后导出到当前目录的新文件：
    
    
    claude-statusline config export ./statusline.json
    

在另一台已安装并接入工具的电脑上，将文件放到当前目录，先检查再导入：
    
    
    claude-statusline config import ./statusline.json --dry-run
    claude-statusline config import ./statusline.json
    

文件已存在时，导出请换一个文件名。可移植配置包含显示设置及工具管理的刷新等选项，运行状态和插件接入偏好需在各机器分别管理。

## 六、按需开启实时指标

> **2026.10.18 更新（npm 版）：** 新安装默认关闭原生计时和高级实时采集，并保留已有明确偏好。只启用原生计时可执行 `claude-statusline install --native-timing`；启用完整采集使用下文的 `claude-statusline install --live-metrics`。两者均要求 Claude Code 2.1.289+，执行后运行 `doctor` 并重启 Claude Code。以下原文保留，其中“新安装默认采集原生计时”的描述适用于历史 Python 版。

需要查看运行状态、活动 Agent 数量、结构化任务进度和最近工具时，先确认 Claude Code 为 2.1.289+，在系统终端执行：
    
    
    claude-statusline install --live-metrics
    claude-statusline config enable run-state permission-mode active-agents task-progress last-tool
    claude-statusline doctor
    

检查后重启 Claude Code，加载采集器；后续运行任务时观察新增字段。这一步同时涉及采集器接入和显示项选择，仅在编辑器中勾选字段还不够。

高级实时指标默认关闭，与兼容宿主新安装默认采集的原生计时元数据分别管理。没有有效观测时显示 `—`，有限覆盖或最近观测可能带 `*`。其中任务进度来自结构化任务记录，不能据此推算还剩多久。

## 七、常见问题、升级与卸载

### 2026.10.18 更新：npm 版排查、更新、迁移与卸载

以下新增说明适用于 v3.0.0 及之后；Windows 使用 `claude-statusline.cmd`。原 Python/pipx 说明保留在本节后半部分。

#### 1\. npm 安装后找不到命令

全局安装后，先检查软件包与安装前缀：
    
    
    npm list --global --depth=0
    npm prefix --global
    

确认 npm 的全局命令目录已加入 PATH，调整后重新打开终端。Linux／WSL／macOS 可用 `command -v claude-statusline` 核对入口；Windows PowerShell 可用 `Get-Command claude-statusline.cmd`。若仍指向 Python/pipx 旧版，先按下方迁移步骤处理同名入口。

#### 2\. 更新已全局安装的 npm 版

先退出 Claude Code 和配置编辑器，再执行：
    
    
    npm install --global --ignore-scripts @fbincon/claude-code-statusline
    claude-statusline --version
    claude-statusline install
    claude-statusline doctor
    

检查通过后重启 Claude Code。重新执行 npm 安装命令会更新软件包，随后仍需执行 `install` 同步命令路径、hooks、skills 和插件资源。**`pipx upgrade` 只管理历史 Python 包，不能更新到 v3.x。**

如果采用下方的独立目录安装，更新时保持同一个 `--prefix ./statusline-node`，通过同一 Node/JavaScript 入口执行 `--version`、`install` 和 `doctor`；全局 npm 更新命令不更新该独立目录。

#### 3\. 从 Python/pipx 迁移到 npm

切换前先退出 Claude Code 和配置编辑器，备份整个 Claude 配置目录（默认 `~/.claude`，使用 `CLAUDE_CONFIG_DIR` 时备份对应目录），记录原 Python 命令的绝对路径与版本，并保留原 pipx 环境用于回退。新旧版不要同时向同一配置目录写入。

为避开 PATH 中已有的同名 Python 命令，可先在一个长期保留的位置使用独立目录安装。以下命令从该位置执行，将新版安装到 `./statusline-node`，并明确使用 Node 入口完成接入：
    
    
    npm install --prefix ./statusline-node --ignore-scripts @fbincon/claude-code-statusline@3.1.0
    node ./statusline-node/node_modules/@fbincon/claude-code-statusline/bin/claude-statusline.js --version
    node ./statusline-node/node_modules/@fbincon/claude-code-statusline/bin/claude-statusline.js install --dry-run
    node ./statusline-node/node_modules/@fbincon/claude-code-statusline/bin/claude-statusline.js install
    node ./statusline-node/node_modules/@fbincon/claude-code-statusline/bin/claude-statusline.js doctor
    

使用自定义配置目录时，为上述 `install` 和 `doctor` 命令传入相同的 `--config-dir`。检查通过后重启 Claude Code；接入会绑定实际 Node 和 JavaScript 入口，因此使用期间须保留该安装目录和 Node 可执行文件。

独立目录安装不会把终端里的 `claude-statusline` 自动切换到新版；后续配置、更新和卸载应继续通过上述 `node .../claude-statusline.js` 入口操作。已有显示配置、明确的编辑器与采集偏好及无关 Claude 设置会保留。不要用 npm `--force` 覆盖归属不明的同名命令。

如需保留 Python 回退环境，可继续使用独立目录；如需改用全局 npm 命令，在新版验证通过后，先用 `pipx list` 核实旧包名称，再用 `pipx uninstall fbincon-claude-code-statusline` 移除对应旧包，随后按第二节完成全局 npm 安装和接入。确认全局版本接入正常后，再删除独立安装目录。需要回退时，按[新版迁移与恢复指南](<https://github.com/fbincon/claude-code-statusline/blob/v3.1.0/docs/USER_GUIDE.zh-CN.md#%E4%BB%8E-python-%E8%BF%81%E7%A7%BB>)恢复切换前兼容备份和原 Python 接入。

#### 4\. 卸载 npm 版

先退出 Claude Code 和配置编辑器，在命令仍可用时移除接入，再卸载软件包。对于全局 npm 安装：
    
    
    claude-statusline uninstall --dry-run
    claude-statusline uninstall
    npm uninstall --global @fbincon/claude-code-statusline
    

仅在接入卸载成功后执行最后一条。工具会移除归属本工具的接入资源，保留第三方设置，以及显示配置、偏好、缓存、任务状态和备份，便于重装复用。

若使用独立目录安装，通过同一 `node .../claude-statusline.js` 入口依次执行 `uninstall --dry-run` 和 `uninstall`，确认成功后再删除当初专门创建的 `statusline-node` 安装目录。`npm uninstall --global` 不负责移除这类独立目录安装。

### **以下保留原常见问题、Python/pipx 升级与卸载内容。涉及 pipx 或`.exe` 的步骤适用于 v2.0.0 及之前；npm 版请使用以上更新说明。**

**找不到命令：** 先运行 `pipx list` 确认包已安装，再执行 `pipx ensurepath` 并重新打开终端。Windows 使用 `claude-statusline.exe`。

**状态栏没出现：** 运行 `claude-statusline doctor`，检查 PATH、接入是否完成、显示项是否为空，以及宿主是否禁用了 hooks/statusline；接入修复后重启 Claude Code。若提示因信任被跳过，按宿主提示完成对应信任操作。

**配置入口不可用：** 检查 `claude --version`、安装偏好和插件状态。不兼容入口会暂挂；宿主升级后重新执行 `install` 与 `doctor`。macOS 的会话内 Client 仍有已记录的交互限制，可使用独立 TUI 或 CLI。

**部分数据暂时缺失：** 首次真实模型响应前，transcript 或用量信息可能尚未产生；限额和 effort 等字段也取决于宿主是否提供。`doctor` 的 `[WARN]` 表示有降级情况，需结合具体提示判断。

升级时先退出 Claude Code，在终端执行：
    
    
    pipx upgrade fbincon-claude-code-statusline
    claude-statusline install
    claude-statusline doctor
    

随后重启 Claude Code。软件包升级后还要同步接入。若使用过本仓库旧分发名，先核实安装来源，再按[包名迁移说明](<https://github.com/fbincon/claude-code-statusline/blob/v1.7.5/docs/USER_GUIDE.zh-CN.md#%E8%BF%81%E7%A7%BB%E6%97%A7%E5%88%86%E5%8F%91%E5%90%8D%E7%A7%B0>)处理。

卸载时先退出 Claude Code，再移除接入，最后卸载软件包：
    
    
    claude-statusline uninstall --dry-run
    claude-statusline uninstall
    pipx uninstall fbincon-claude-code-statusline
    

显示配置、运行状态和备份会保留，便于重装复用。更多排查步骤见[完整使用指南](<https://github.com/fbincon/claude-code-statusline/blob/v1.7.5/docs/USER_GUIDE.zh-CN.md#%E6%95%85%E9%9A%9C%E6%8E%92%E6%9F%A5>)。

## 八、项目与文档入口

项目使用 [MIT 许可证](<https://github.com/fbincon/claude-code-statusline/blob/v1.7.5/LICENSE>)。源码、发行包和详细文档可从以下入口获取：

  * [GitHub 主仓库](<https://github.com/fbincon/claude-code-statusline>)
  * [Gitee 同步仓库](<https://gitee.com/fbincon/claude-code-statusline>)
  * [npm 软件包（TypeScript 版）](<https://www.npmjs.com/package/@fbincon/claude-code-statusline>)
  * [中文使用指南](<https://github.com/fbincon/claude-code-statusline/blob/v3.1.0/docs/USER_GUIDE.zh-CN.md>)
  * [CLI 参考](<https://github.com/fbincon/claude-code-statusline/blob/v3.1.0/docs/reference/cli.zh-CN.md>)



保留 Python 版供参考：

  * [PyPI 软件包（最后一个版本为 v2.0.0）](<https://pypi.org/project/fbincon-claude-code-statusline/>)
  * [v2.0.0 中文使用指南（最后一个 Python 版）](<https://github.com/fbincon/claude-code-statusline/blob/v2.0.0/docs/USER_GUIDE.zh-CN.md>)



欢迎结合自己的开发习惯调整显示内容。


---
> 原文链接: https://www.cnblogs.com/fbincon/p/23347837