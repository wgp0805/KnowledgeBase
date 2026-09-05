---
title: "Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜"
source: "博客园"
url: "https://www.cnblogs.com/buchizicai/p/21752482"
date: "2026-07-21T14:27:00Z"
score: 0.65
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# Hermes Agent 完全指南：比 Claude Code 更自由的开源 AI Agent，从安装配置到多 Agent 协作 - 不吃紫菜

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/buchizicai/p/21752482  
> **抓取日期**: 2026-07-21  
> **相关性评分**: 0.65

# Hermes Agent

# 一、安装使用

> 官方文档：<https://hermes-agent.nousresearch.com/docs/getting-started/installation>

## 支持环境

Windows、macOS、Linux、WSL2（Windows上的Linux虚拟机）、Android

## 安装步骤

> 以Windows11为例，其余的需执行上网找教程 或 参考官方文档安装教程（上面有链接）

  1. 前提工具安装：

     1. 自行下载 git 并安装（如果没有git，Hermes Agent是自动安装便携版 Git Bash，为了后续更好体验，建议自行安装完整版git）

     2. 更新power shell：自行上网下载更新

> 低版本power shell 有可能出现命令行安装中乱码问题

  2. 开始安装

     1. 方式一：命令行（什么系统执行对应命令即可）

        1. Linux / macOS / WSL2
               
               curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
               

        2. Windows（PowerShell，v0.14+ 原生支持）
               
               iex (irm https://hermes-agent.nousresearch.com/install.ps1)
               

        3. Termux (Android)

> v0.15 冷启动优化后，Termux 环境下 `hermes --version` 仅需 0.8 秒
               
               curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
               

     2. 方式二：桌面端安装

        1. 安装桌面版（图形化界面、中文支持）：<https://hermes-agent.nousresearch.com/docs/getting-started/desktop>

> 也可以不通过前面的命令行直接安装桌面版，会自动帮你安装所有内容。但存在访问GitHub超时问题，所以还是建议先使用前面的 命令行**【建议是使用方式一安装完后，下载桌面端。此时就可以正常使用桌面端了】**

  3. 配置Hermes Agent
         
         hermes model                 # 交互式选择模型和提供商
         hermes setup --portal        # 使用 Nous Portal 一键配置【推荐，但需要登录GitHub账号，绑定银行卡】
         hermes setup                 # 或者运行完整设置向导【次推荐，每一步都自行设置】
         

①**Nous Portal** 是 v0.16 推荐的一键配置方式，提供 400+ 模型，OAuth 登录后即可使用，无需手动管理 API Key（自动帮你配置好免费的 搜索工具、图片工具、语音转文字 等等）

②API Key 存储在 `~/.hermes/.env` 文件中（Windows 在 `%LOCALAPPDATA%\hermes\.env`）

  4. 配置完成后建议使用桌面版进行使用，有直观的UI界面（方式二有桌面版安装链接）




**补充：**

  1. 命令行安装/桌面版安装会自动安装 所需的环境（遇到报错查看命令行报错提示即可），自动执行以下内容：

     1. 拉取或更新 Hermes 源码。普通 Linux / macOS / WSL2 用户默认安装到 `~/.hermes/hermes-agent`；Windows 默认安装到 `%LOCALAPPDATA%\hermes\hermes-agent`
     2. 创建 Python 虚拟环境并安装依赖；必要时会安装 `uv`、Node.js、浏览器工具相关依赖
     3. 创建 `hermes` 命令入口，并提示把它所在目录加入 `PATH`
     4. 初始化数据目录。Linux / macOS / WSL2 默认是 `~/.hermes`；Windows 默认是 `%LOCALAPPDATA%\hermes`
     5. 仅在文件不存在时创建 `config.yaml`、`.env`、`SOUL.md`，已有配置会保留
     6. 交互式终端中会继续运行 setup 向导



## 桌面版使用

桌面版的使用很直白不做过多介绍（此处省略一万字）

## CLI使用

> **注意：** 如果cmd输入无效，就使用power shell

### 交互式对话（终端）
    
    
    hermes                       # 启动交互式对话
    hermes --tui                 # 使用 TUI 启动（v0.11+，React/Ink 终端界面）
    

**TUI 模式** （v0.11+）提供：

  * 实时 token 流式输出
  * 每轮对话耗时统计
  * 子 Agent 可观测性面板
  * 多会话管理
  * 固定输入栏（类似聊天应用）



### 单次对话（非交互式）
    
    
    hermes chat -q "查看系统资源占用情况"
    

适合脚本调用或一次性任务。

### 诊断
    
    
    hermes doctor                # 检查环境健康状态，诊断潜在问题
    

### 常用快捷键

快捷键 | 功能  
---|---  
`Alt + V` | 从剪贴板粘贴图像  
`Ctrl + C` | 中断当前操作  
`Ctrl + D` | 退出会话  
`Ctrl + Z` | 暂停并挂起到后台，`fg` 恢复  
`Alt + Enter` | 插入新行，输入多行文本  
`Ctrl + J` | 插入新行，输入多行文本  
`Shift + Enter` | 插入新行，需终端支持独立按键序列  
  
### 更新/备份
    
    
    hermes update
    

> **建议** ：升级前备份 `~/.hermes/auth.json` 和 `~/.hermes/config.yaml`。大版本升级时建议直接跳到最新补丁版本（如 v0.15.1 而非 v0.15.0）。

### 卸载
    
    
    hermes uninstall
    

如需完全清理所有数据：
    
    
    # Linux / macOS / WSL2
    rm -rf ~/.hermes
    
    # Windows
    Remove-Item -Recurse -Force $env:LOCALAPPDATA\hermes
    

## Web界面使用

> 由于已经有了桌面版，所以更推荐使用桌面版，Web版了解即可。

Hermes 提供了一个基于浏览器的 Web 管理界面（Dashboard），替代手动编辑 YAML 和 CLI 命令，用于配置管理、API 密钥设置和会话监控。

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard>

### 启动与配置
    
    
    hermes dashboard                       # 启动，自动打开浏览器 http://127.0.0.1:9119
    hermes dashboard --port 8080           # 自定义端口
    hermes dashboard --tui                 # 启用浏览器内 Chat 标签页
    hermes dashboard --status              # 查看运行状态
    hermes dashboard --stop                # 停止运行
    hermes dashboard &>/dev/null &         # 后台运行
    hermes dashboard &>/dev/null & disown  # 后台运行并脱离终端
    

### v0.16 Web 管理面板

v0.16 将 Dashboard 升级为完整的 Web 管理面板，支持：

  * **消息渠道配置** ：在网页中配置 Telegram、Discord、Slack 等平台
  * **MCP 目录管理** ：浏览和配置 MCP 服务器
  * **凭证管理** ：可视化编辑 `.env` 和 `auth.json`
  * **Webhooks** ：配置外部系统回调
  * **Gateway 控制** ：启动、停止、监控 Gateway 状态
  * **简体中文界面** ：完整的中文本地化



## Hermes目录介绍

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/configuration>

Hermes目录位置：  
①普通 Linux / macOS / WSL2 用户默认在 `~/.hermes/hermes-agent`；  
②Windows 默认安装到 `%LOCALAPPDATA%\hermes\hermes-agent`

例如我的Windows电脑目录为：C:\Users\conan\AppData\Local\hermes\hermes-agent

### 配置目录结构
    
    
    ~/.hermes/
    ├── config.yaml        # 主配置文件（模型、终端、TTS、压缩等）
    ├── .env               # API 密钥和机密信息
    ├── auth.json          # OAuth 提供商凭证（Nous Portal 等）
    ├── SOUL.md            # 主 Agent 的身份 / 人格文件，会拼入系统提示词开头部分
    ├── memories/          # 持久化记忆（MEMORY.md、USER.md）
    ├── skills/            # 技能
    ├── cron/              # 定时任务
    ├── sessions/          # 会话
    └── logs/              # 日志（errors.log、gateway.log — 密钥自动脱敏）
    

### 配置管理命令
    
    
    hermes config                        # 查看当前配置
    hermes config edit                   # 用 $EDITOR 打开 config.yaml 编辑
    hermes config set section.key value  # 直接设置某个配置项
    

会话内也可以通过斜杠命令调整部分配置：

命令 | 功能  
---|---  
`/config` | 查看当前配置  
`/model [model-name]` | 查看或切换当前会话使用的模型  
`/personality [name]` | 切换预设交互风格 / 人格  
`/reasoning [level/show/hide]` | 调整或查看模型推理级别  
`/voice [on/off/tts/status]` | 开启、关闭或查看语音输入 / TTS 输出状态  
`/yolo` | 切换绕过确认模式，减少工具执行确认；只建议在可信环境和低风险任务使用  
  
# 二、基本功能

## 1\. 会话管理

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/sessions>

每一次与 Hermes 的对话都是一个会话（Session），系统会自动保存和索引。

### 1.1 基本操作
    
    
    hermes sessions list                                    # 列出近期会话
    hermes sessions browse                                  # 打开交互式会话选择器
    hermes --continue                                       # 继续上次会话
    hermes -c                                               # 继续上次会话的短参数
    hermes --resume 20250225_143052_a1b2c3                  # 按会话 ID 恢复
    hermes -r "我的项目设置"                                  # 按标题恢复
    hermes sessions rename 20250225_143052_a1b2c3 "后端 API 开发"  # 重命名会话
    hermes sessions delete session_id                       # 删除会话
    hermes sessions prune --older-than 30                   # 清理 30 天前的旧会话
    

### 1.2 会话内斜杠命令

命令 | 功能  
---|---  
`/new` | 开始新会话  
`/clear` | 清屏并开始新会话  
`/undo` | 撤销上一次用户/Agent 交互记录  
`/undo [N]` | v0.16+：撤销最近 N 轮交互  
`/title <session_name>` | 为当前会话命名  
`/history` | 显示对话历史  
`/sessions` | 查看和管理会话  
`/compress` | 手动压缩上下文  
`/stop` | 停止后台进程  
`/background <prompt>` | 在后台运行任务  
`/goal <text>` | v0.13+：设置持续性目标。辅助评判模型检查目标是否完成，未完成则自动继续  
  
### 1.3 会话存储

Hermes 主要使用 SQLite 数据库（`~/.hermes/state.db`）保存会话状态：会话元数据、完整消息历史、模型配置、token / 费用统计，以及用于跨会话搜索的 FTS5 索引。数据库采用 WAL（预写日志）模式，支持并发读取和单个写入。

早期版本使用 `~/.hermes/sessions/` 下的 JSONL 文件保存逐会话转录；当前 `state.db` 是会话查询、恢复和搜索的主要存储。

SQLite 中主要有这几张表：

表 | 内容  
---|---  
`sessions` | 会话元数据：会话 ID、来源平台、用户 ID、模型配置、系统提示词、会话标题等  
`messages` | 完整消息历史：所属会话、角色、正文、工具调用、工具名称、时间戳、结束原因、推理内容等  
`state_meta` | 键值元数据表，用于记录状态型信息  
`schema_version` | 数据库 schema 版本号，用于迁移判断  
  
Hermes 还会维护 FTS5 搜索索引表：`messages_fts` 用于英文 / 拉丁语系全文搜索，`messages_fts_trigram` 用于 CJK（中日韩）子串搜索。SQLite 中还包括 `messages_fts_data`、`messages_fts_idx`、`messages_fts_content`、`messages_fts_docsize`、`messages_fts_config` 等影子表，以及对应的 `messages_fts_trigram_*` 表。

### 1.4 上下文压缩

当会话上下文接近模型限制时，Hermes 会自动压缩历史消息，保留关键信息并维持上下文窗口可用（官方配置好的，不建议修改）
    
    
    # ~/.hermes/config.yaml
    compression:
      enabled: true       # 启用/禁用压缩
      threshold: 0.50     # 当 prompt tokens 达到模型上下文窗口的 50% 时触发压缩
      target_ratio: 0.20  # 最近消息保留预算：threshold_tokens 的 20%，即默认保留约 10% 总上下文不压缩
      protect_last_n: 20  # 最少保留不压缩的最近消息数
    

也可通过 `/compress` 斜杠命令手动触发压缩。

### 1.5 Session Search 会话搜索（★ v0.15 重建）

> **简单来说就是：可以跨会话知道前面其他会话的内容**

v0.15 重大更新：`session_search` 在 v0.15 中被完全重建，去除了 LLM 依赖，速度提升 4,500 倍（从 ~90s 降至 ~20ms），且零费用。旧版本中每次搜索都要调用 LLM 做摘要，既慢又贵。

Agent 内置 `session_search` 工具，用 SQLite FTS5 在过去所有会话中做全文搜索。它解决的是"我之前是不是和 Hermes 说过这件事"的问题。Agent 被提示在用户提到过去对话，或者怀疑历史会话里有相关上下文时，先调用 `session_search` 回忆历史，而不是直接要求用户重复信息。借助这个工具 Agent 可以先搜索命中的会话，再沿着同一个会话向前或向后翻看更多上下文。

`session_search` 没有显式 `mode` 参数，而是根据传入参数自动判断调用形态：

调用形态 | 参数 | 用途  
---|---|---  
Discovery | `query` | 按关键词搜索历史会话，返回最相关的若干会话  
Scroll | `session_id` \+ `around_message_id` | 在某个命中的会话里，以指定消息为中心继续向前 / 向后翻看  
Browse | 无参数 | 按时间列出最近会话，适合用户只问"我之前在做什么"  
  
Discovery 搜索结果通常包含：

  * `session_id`、标题、时间、来源平台
  * FTS5 命中的高亮片段
  * 会话开头几条用户 / assistant 消息，用来还原任务开始时的目标
  * 命中消息前后的一小段上下文
  * 会话结尾几条用户 / assistant 消息，用来判断最后结论或决策
  * 命中的 `message_id`，后续可用它继续 Scroll



Agent 调用 `session_search` 时，`query` 参数支持常见 FTS5 查询语法：
    
    
    docker deployment        # 多关键词，默认 AND
    "exact phrase"           # 精确短语
    docker OR kubernetes     # 布尔 OR
    python NOT java          # 排除关键词
    deploy*                  # 前缀匹配
    

`session_search` 常用可选输入参数：

参数 | 说明  
---|---  
`limit` | Discovery 返回的会话数量  
`window` | Scroll 时围绕锚点消息返回前后多少条消息  
`sort` | `newest` / `oldest`，在相关性之外按时间排序  
`role_filter` | 限制搜索角色；默认搜索 `user,assistant`，需要调试工具输出时可包含 `tool`  
  
**使用示例：Agent 内部调用流程**

当用户问「上次我们讨论的那个 Docker 部署方案，后来怎么解决的？」时，Agent 的内部调用链：
    
    
    # 第一步：Discovery —— 按关键词找到相关会话
    search_result = session_search(
        query="Docker deployment",
        limit=3,
    )
    
    # 返回结果（简化）：
    # [
    #   {session_id: "20260610_143052_a1b2c3", title: "Docker 部署问题排查",
    #    snippet: "...Docker 部署到生产环境后遇到端口冲突...",
    #    matched_message_id: "msg_789"},
    #   ...
    # ]
    
    # 第二步：Scroll —— 围绕命中消息上下翻看完整上下文
    detail = session_search(
        session_id="20260610_143052_a1b2c3",
        around_message_id="msg_789",
        window=5,  # 前后各取 5 条
    )
    
    # Agent 基于拿到的上下文回答用户，而不需要让用户再讲一遍
    

## 2\. 上下文文件

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files>

Hermes Agent 会自动发现并加载上下文文件。这里的"上下文文件"分两类：

  1. 项目上下文文件用于描述当前仓库或目录规则（会话当前目录中的MD文档）
  2. Hermes的安装目录中`SOUL.md` 用于描述当前 Hermes 实例的人格和沟通风格



### 2.1 支持的上下文文件

> `.hermes.md` / `HERMES.md`是Hermes安装目录里写的全局规则。进入A文件夹创建`AGENTS.md`/`CLAUDE.md`，在A文件夹进入cmd开启Hermes会话，当前会话就会 启动加载 读取当前文件夹下的`AGENTS.md`/`CLAUDE.md`作为会话规则。

文件 | 用途 | 发现方式  
---|---|---  
`.hermes.md` / `HERMES.md` | Hermes 专用项目说明，优先级最高 | 从当前目录向上查找到 git root  
`AGENTS.md` | 项目说明、架构、约定、注意事项 | 启动目录；子目录中可渐进发现  
`CLAUDE.md` | 兼容 Claude Code 的上下文文件 | 启动目录；子目录中可渐进发现  
`.cursorrules` | 兼容 Cursor 的项目规则 | 启动目录；子目录中可渐进发现  
`.cursor/rules/*.mdc` | Cursor 规则模块 | 启动目录  
`SOUL.md` | 当前 Hermes 实例的人格、语气和沟通风格 | 只从 `HERMES_HOME/SOUL.md` 加载  
  
### 2.2 加载流程与安全处理【重要，原理须知】

项目上下文有两条加载路径：启动加载和渐进加载。

#### 启动加载

发生在会话开始时。流程如下：

  1. 扫描当前工作目录，按优先级查找项目上下文文件
  2. 以 UTF-8 文本格式读取
  3. 执行安全扫描
  4. 超过 20,000 字符时截断，保留头部和尾部
  5. 组合到 `# Project Context` 部分并注入系统提示词



启动时的项目上下文只加载一种类型，**优先级是** ：`.hermes.md` / `HERMES.md` → `AGENTS.md` → `CLAUDE.md` → `.cursorrules` / `.cursor/rules/*.mdc`。`SOUL.md` 优先独立加载，不参与这个优先级竞争。

截断策略：启动加载的默认截断上限是 20,000 字符。超过上限后，Hermes 保留前 70% 和后 20%，中间插入截断标记：  
（也就是说，**重要规则最好放在文件开头或结尾** ）
    
    
    [...truncated AGENTS.md: kept 14000+4000 of 35620 chars. Use file tools to read the full file.]
    

#### 渐进加载

发生在会话进行中：

  1. Agent 调用工具时，如果有文件路径，Hermes 会从这些路径推断当前正在访问的目录
  2. 从该路径所在目录向上检查最多 5 层父目录
  3. 每个目录按 `AGENTS.md` → `CLAUDE.md` → `.cursorrules` 优先级只加载首个匹配项
  4. 执行安全扫描
  5. 单个渐进提示文件超过 8,000 字符时，只保留前 8,000 字符
  6. 内容追加到工具结果中



#### 安全扫描

安全扫描检查以下内容：

  1. **指令覆盖** — 例如 `ignore previous instructions`、`disregard your rules`
  2. **欺骗行为** — 例如 `do not tell the user`
  3. **系统提示词覆盖** — 例如 `system prompt override`
  4. **隐藏 HTML 注释** — 例如 `<!-- ignore instructions -->`
  5. **隐藏 div 元素** — 例如 `<div style="display:none">`
  6. **凭证外泄** — 例如 `curl ... $API_KEY`
  7. **敏感文件读取** — 例如 `cat .env`、`cat credentials`
  8. **不可见字符** — 零宽空格、双向文本覆盖符、词连接符等



命中任意威胁模式后，文件将被阻止加载，上下文位置替换为：
    
    
    [BLOCKED: AGENTS.md contained potential prompt injection (prompt_injection). Content not loaded.]
    

核心实现位于 `agent/prompt_builder.py`，使用 `_CONTEXT_THREAT_PATTERNS` 正则列表和 `_CONTEXT_INVISIBLE_CHARS` 危险字符集合进行两步检测。

### 2.3 @ 上下文引用（v0.4+）

> 基本不用，因为桌面版直接上传文件/输入url链接就行

Hermes 支持在对话中通过 `@file` 和 `@url` 注入上下文：
    
    
    @file:README.md  这个项目的 README 写了什么？
    @url:https://example.com/doc  根据这个文档回答问题
    

配合 Tab 补全，可以快速引用项目中的文件路径。

### 2.4 SOUL.md 与 /personality

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/personality>
> 
> SOUL.md是全局的角色设定。 /personality是会话级别的角色设定。  
>  （两者是共存的，一个全局一个局部，使用局部会话时是加载 局部设定+全局设定）

Hermes 的个性主要由 `SOUL.md` 控制。它是 Agent 的主身份文件，会拼入系统提示词开头部分。默认位置在 `~/.hermes/SOUL.md`。

`SOUL.md` 适合写长期稳定的个性和沟通偏好：

  * 语气
  * 风格
  * 直接程度
  * 默认互动方式
  * 不希望出现的表达习惯
  * 面对不确定性、分歧、模糊需求时的处理方式



不适合写项目规则、文件路径、仓库约定、临时流程。这些应该放进 `AGENTS.md`。

`/personality` 是一层额外的系统提示覆盖。它不会修改 `SOUL.md`，而是在当前基础系统提示之后追加一段 personality prompt。

Hermes 内置以下人格，可通过 `/personality` 切换：

人格 | 说明  
---|---  
`helpful` | 友好、通用的基础助手  
`concise` | 简短直接，回答尽量切中要点  
`technical` | 详细、准确的技术专家模式  
`creative` | 创新发散，偏向非常规方案和新思路  
`teacher` | 耐心教学，用清晰解释和示例辅助理解  
`kawaii` | 可爱、闪亮、热情的表达风格  
`catgirl` | Neko-chan 猫娘风格，带猫系口癖和可爱表达  
`pirate` | Captain Hermes，懂技术的数字海盗船长风格  
`shakespeare` | 莎士比亚式文风，戏剧化、华丽而夸张  
`surfer` | 轻松随性的冲浪者语气  
`noir` | 硬汉侦探小说式叙述，偏黑色电影氛围  
`uwu` | 极致可爱和 uwu-speak  
`philosopher` | 哲学家模式，会追问问题背后的意义和原因  
`hype` | MAXIMUM ENERGY，极高能量和强烈鼓舞式回应  
  
## 3\. 持久记忆

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/memory>
> 
> 这个是全自动的，了解即可。

Hermes 有一套有容量上限、由 Agent 自己维护的持久记忆系统。它会跨会话保存用户偏好、项目环境、工具习惯和经验教训，并在新会话开始时注入系统提示词。

### 3.1 工作原理

内置记忆由两个文件组成，默认存储在 `~/.hermes/memories/`：

文件 | 用途 | 字符上限  
---|---|---  
`MEMORY.md` | Agent 的个人笔记：环境事实、项目约定、工具细节、经验教训 | 2,200 字符（约 800 tokens）  
`USER.md` | 用户画像：用户信息、沟通风格、期望和习惯 | 1,375 字符（约 500 tokens）  
  
  * 两个文件会在会话开始时注入系统提示词
  * 会话中通过 `memory` 工具新增、替换或删除的记忆会立即写入磁盘，但不会立刻改变当前会话已经注入的提示词快照
  * 新的记忆会在下一个会话生效。这样可以保持 LLM prefix cache 稳定



记忆相关配置示例：
    
    
    # ~/.hermes/config.yaml
    memory:
      memory_enabled: true        # 启用持久记忆
      user_profile_enabled: true  # 启用用户档案
      memory_char_limit: 2200     # 记忆字符上限（约 800 tokens）
      user_char_limit: 1375       # 用户档案字符上限（约 500 tokens）
    

系统提示词中的记忆大致长这样：
    
    
    ══════════════════════════════════════════════
    MEMORY (your personal notes) [67% — 1,474/2,200 chars]
    ══════════════════════════════════════════════
    User's project is a Rust web service at ~/code/myapi using Axum + SQLx
    §
    This machine runs Ubuntu 22.04, has Docker and Podman installed
    §
    User prefers concise responses, dislikes verbose explanations
    

`§`（节号符号）用来分隔不同记忆条目，标题会显示当前容量占用。

### 3.2 memory 工具

> 一般不用这个工具，直接去目录里修改：`~/.hermes/memories/`

Agent 通过 `memory` 工具管理记忆，常用动作：

动作 | 用途  
---|---  
`add` | 添加新的记忆条目  
`replace` | 替换已有条目，使用 `old_text` 做短唯一子串匹配  
`remove` | 删除已有条目，使用 `old_text` 做短唯一子串匹配  
  
没有 `read` 动作。记忆内容会自动注入系统提示词，Agent 在会话里本来就能看到当前快照。

`replace` 和 `remove` 不需要传完整条目，只要传能唯一定位的短文本：
    
    
    memory(action="replace", target="memory",
           old_text="dark mode",
           content="User prefers light mode in VS Code, dark mode in terminal")
    

使用 `old_text` 匹配时，会先去掉首尾空白，并在每条记忆中进行精确子串匹配。必须刚好匹配 1 条记忆。

### 3.3 记忆管理原则

记忆管理由 `MEMORY_GUIDANCE` 提示词驱动。核心原则：

**应该保存到记忆：**

  * 用户偏好：例如「用户偏好 TypeScript 而不是 JavaScript」
  * 环境事实：例如「这台服务器运行 Debian 12 和 PostgreSQL 16」
  * 用户纠正：例如「Docker 命令不要用 sudo，用户已在 docker 组」
  * 项目约定：例如「项目使用 tabs、120 字符行宽、Google 风格 docstring」
  * 显式要求：例如「记住 API key 每月轮换」



**不应该保存到记忆：**

  * 太模糊的信息：例如「用户问过 Python」
  * 容易重新查询的通用知识
  * 大段代码、日志、数据表
  * 临时任务状态、一次性文件路径、短期 TODO
  * 已经写在 `SOUL.md`、`AGENTS.md` 等上下文文件里的内容



**记忆应该写成陈述性事实** ，而不是命令式指令：

  * ✓ `User prefers concise responses`
  * ✗ `Always respond concisely`



容量管理：记忆有严格字符上限。当新增内容会超过上限时，`memory` 工具会返回错误，Agent 应该先合并、替换或删除旧条目。

安全扫描：记忆条目在写入前还会做安全扫描，包含提示词注入、凭证外泄、SSH 后门、不可见 Unicode 字符等风险模式的内容会被阻止。

> **v0.15 新增 Promptware Defense** ：记忆在加载时也会被扫描。这是 Brainworm 级攻击防护的三道关卡之一（另外两道是工具输出分隔符标记和控制文件写保护）。

### 3.4 session_search vs memory

除了 `MEMORY.md` 和 `USER.md`，Hermes 还可以通过 `session_search` 搜索过去的完整会话。两者用途不同：

对比项 | 持久记忆memory | Session Search  
---|---|---  
容量 | 约 1,300 tokens，总量很小 | 理论上包含所有历史会话  
速度 | 会话开始时直接进入系统提示词 | 需要按需查询数据库（v0.15：~20ms）  
用途 | 必须一直可见的关键事实 | 查找过去某次讨论的具体内容  
管理方式 | Agent 主动维护、压缩、替换 | 自动保存所有会话  
token 成本 | 每个会话固定占用少量上下文 | 返回的消息片段占用上下文  
  
memory 保存「以后经常要用的稳定事实」；session_search 用来回答「上次我们讨论过什么」。

**补充：memory VS SKILL VS Session Search**

  1. memory是在记忆文件中保存简单的一句话（一个用户喜好、当前工作环境 等等）
  2. SKILL是将复杂任务提取成SKILL，便于后续执行该任务时调用
  3. Session Search是其他会话持久存储在数据库中，后续用户询问其他会话内容时会自动查询数据库



### 3.5 外部记忆提供商

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers>

Hermes 内置了 8 个外部记忆提供商插件，提供比 `MEMORY.md` / `USER.md` 更强的跨会话记忆能力。外部记忆不会替代内置记忆，而是作为叠加能力并行工作。同一时间只能启用一个外部记忆提供商。

> holographic是本地的，不需要key，可以直接选择使用。
    
    
    hermes memory setup   # 交互式选择并配置外部记忆提供商
    hermes memory status  # 查看当前启用状态
    hermes memory off     # 关闭外部记忆提供商
    

可选 provider：

分档 | Provider | 重点功能 / 优势  
---|---|---  
入门 | `honcho` | 跨会话用户建模、session 级上下文、基于历史上下文的综合判断  
入门 | `mem0` | 服务端 LLM 事实抽取、语义搜索、重排和自动去重  
进阶 | `openviking` | 文件系统式知识层级、分层读取、自动抽取 6 类记忆  
进阶 | `byterover` | CLI 驱动的层级知识树、分层检索、压缩前自动提取洞察  
复杂 | `hindsight` | 知识图谱、实体关系、多策略检索、跨记忆综合  
复杂 | `holographic` | FTS5 全文搜索、信任评分、HRR 组合查询、冲突检测  
复杂 | `retaindb` | Vector + BM25 + Reranking 混合搜索、7 类记忆、增量压缩  
复杂 | `supermemory` | 语义长期记忆、用户画像、会话图谱摄取、上下文防污染  
  
选择建议：

  * 只是想让记忆更智能，先从 `honcho` 或 `mem0` 开始
  * 更偏本地 / 文件系统式知识管理，可以看 `openviking` 或 `byterover`
  * 需要知识图谱、实体关系和复杂关联检索，再考虑 `hindsight`
  * 需要混合检索、评分、冲突检测等进阶能力，再看 `holographic`、`retaindb` 或 `supermemory`



## 4\. Toolsets 工具集

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/tools>

工具（Tools）是 Hermes 调用外部能力的基本单元——搜索网页、执行命令、读写文件、控制浏览器等。工具按功能分组为「工具集」（Toolsets），可以按平台按需启用或禁用，从而精确控制 Agent 的能力范围。

### 4.1 基本操作

> 桌面版UI直观，可以不用命令行
    
    
    hermes tools                  # 交互式管理工具集
    hermes tools list             # 查看所有工具集
    hermes tools list --platform weixin  # 查看指定平台的工具集
    hermes tools enable yuanbao   # 启用 yuanbao 工具集
    hermes tools disable yuanbao  # 禁用 yuanbao 工具集
    
    /tools    # 会话内查看 / 管理可用工具
    /verbose  # 切换工具执行展示模式（all → verbose → off → new）
    

`/verbose` 控制工具执行过程在会话里显示多少信息：

模式 | 含义  
---|---  
`off` | 只显示最终回复，不展示工具调用、日志或推理信息  
`new` | 工具调用发生时显示简短的一行进度  
`all` | 显示所有工具活动，包括工具结果  
`verbose` | 显示最完整细节，包括工具参数和输出，适合调试问题  
  
### 4.2 工具分类

Hermes 内置的工具按用途分为以下几类：

类别 | 包含工具 | 用途  
---|---|---  
**Web** | `web_search`, `web_extract`, `x_search` | 搜索网页、提取页面内容、跨平台搜索  
**终端与文件** | `terminal`, `process`, `read_file`, `patch` | 执行命令、读写文件  
**浏览器** | `browser_navigate`, `browser_snapshot`, `browser_vision`, `computer_use` | 交互式浏览器自动化，支持文本与视觉  
**媒体** | `vision_analyze`, `image_generate`, `text_to_speech`, `video_analyze` | 多模态分析与内容生成  
**编排** | `todo`, `clarify`, `execute_code`, `delegate_task` | 任务规划、澄清需求、代码执行、委托子 Agent  
**记忆与召回** | `memory`, `session_search` | 持久化记忆、搜索历史会话  
**自动化与推送** | `cronjob`, `send_message` | 定时任务、消息推送  
**集成** | `ha_*`, MCP 工具, `rl_*` | Home Assistant、MCP 服务器、RL 训练等  
  
#### 新增工具（v0.13~v0.14）

工具 | 版本 | 用途  
---|---|---  
`computer_use` | v0.14+ | 桌面自动化操作（点击、输入、截图）  
`x_search` | v0.14+ | 跨平台聚合搜索  
`video_analyze` | v0.13+ | 视频内容理解（需 Gemini 或兼容模型）  
  
#### 关键工具用法示例

**web_search — 网页搜索**
    
    
    # Agent 调用示例
    web_search(
        query="Hermes Agent v0.16 Kanban Swarm architecture",
        max_results=10,
    )
    
    # 返回结果包含：标题、URL、摘要
    # Agent 可以进一步用 web_extract 获取完整页面内容
    

**web_extract — 页面内容提取**
    
    
    web_extract(
        url="https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban",
        extract_mode="markdown",   # 将 HTML 转为 Markdown
    )
    # 返回页面的结构化文本内容
    

**browser_navigate / browser_snapshot — 浏览器自动化**
    
    
    # 打开一个需要 JS 渲染的页面
    browser_navigate(url="https://example.com/spa-app")
    
    # 截取当前页面的无障碍树快照（纯文本，不下载图片）
    browser_snapshot()
    # 返回页面中所有可交互元素：按钮、输入框、链接及其标识符
    
    # 需要视觉判断时（如图表、布局问题）
    browser_vision(query="首页首屏的主要内容和布局结构")
    # 这会截取实际截图并送给视觉模型分析
    

**read_file / patch — 文件读写**
    
    
    # 读取文件，支持指定行范围
    read_file(
        file_path="/home/user/project/src/main.py",
        offset=40,    # 从第 40 行开始
        limit=80,     # 读 80 行
    )
    
    # 精确字符串替换（不改动无关代码）
    patch(
        file_path="/home/user/project/src/main.py",
        old_string="def process(data):\n    return data.strip()",
        new_string="def process(data: str) -> str:\n    return data.strip()",
    )
    # patch 要求 old_string 在文件中唯一匹配，否则报错拒绝执行
    

**todo — 任务规划**
    
    
    # Agent 在执行复杂多步骤任务时，先用 todo 工具制定计划
    todo(
        action="create",
        todos=[
            {"content": "搜索 Hermes Agent Kanban Swarm 文档", "status": "pending"},
            {"content": "提取关键架构信息", "status": "pending"},
            {"content": "整理成结构化摘要", "status": "pending"},
        ]
    )
    
    # 逐步推进
    todo(action="update", todo_id=0, status="in_progress")
    # ... 完成第一步 ...
    todo(action="update", todo_id=0, status="completed")
    todo(action="update", todo_id=1, status="in_progress")
    

### 4.3 终端后端【重要，操作实用】

终端工具支持 7 种后端，适应不同的安全隔离和运行环境需求：

> 选择建议：
> 
>   * 默认先用 `local`，适合本机开发和可信任务
>   * 不信任任务内容、担心误改本机文件时，用 `docker`
>   * 目标环境在远程服务器上时，用 `ssh`
>   * HPC / 集群环境优先考虑 `singularity`
>   * 需要云端隔离或弹性资源时，考虑 `modal`、`daytona`、`vercel_sandbox`
> 


后端 | 说明 | 适用场景  
---|---|---  
`local` | 在本机直接执行（默认） | 本地开发、可信任务  
`docker` | 隔离容器中执行 | 安全隔离、可复现环境  
`ssh` | 远程服务器执行 | 沙箱化，防止 Agent 修改自身代码  
`singularity` | HPC 容器（Apptainer） | 集群计算、无 root 环境  
`modal` | 云端无服务器执行 | 弹性伸缩  
`daytona` | 云端沙箱工作区 | 持久化远程开发环境  
`vercel_sandbox` | Vercel 云端微虚拟机 | 部署与长期运行进程  
  
**桌面版切换后端：**

> 修改完询问 Hermes Agent 当前工作目录是什么，是指定目录才修改正确。如果修改失败用命令行更稳妥

  1. 切换终端后端为docker：设置——高级——执行后端下拉选择 docker

![image-20260705223409060](https://img2024.cnblogs.com/blog/2729274/202607/2729274-20260721221114192-1207486929.png)

  2. 修改工作区：设置——工作区——工作目录（默认是`.`，修改成`/workspace`）

![image-20260705223433357](https://img2024.cnblogs.com/blog/2729274/202607/2729274-20260721221128094-2029946505.png)

  3. cmd拉取镜像：docker pull nikolaik/python-nodejs:python3.11-nodejs20

> 前提：需要已经安装并打开了Docker Desktop

  4. 重启Hermes Agent桌面版，后面Hermes Agent执行的命令和输出的文件都是在docker镜像中了




**命令行切换后端：**
    
    
    # 切换终端后端为docker
    hermes config set terminal.backend docker
    
    # 切换终端后端为本地电脑
    hermes config set terminal.backend local
    
    
    
    # 【Docker安装时配置过可以忽略】配置国内的镜像（在docker desktop中配置）
    "registry-mirrors": [
        "https://docker.xuanyuan.me",
        "https://docker.1ms.run"
      ]
      
    # 使用docker desktop拉取正确的镜像
    docker pull nikolaik/python-nodejs:python3.11-nodejs20
    

各后端的具体配置示例：
    
    
    # ~/.hermes/config.yaml
    terminal:
      backend: docker
      modal_mode: auto
      cwd: /workspace
      timeout: 180
      daemon_term_grace_seconds: 2
      env_passthrough: []
      home_mode: auto
      shell_init_files: []
      auto_source_bashrc: true
      docker_image: nikolaik/python-nodejs:python3.11-nodejs20
      docker_forward_env: []
      docker_env: {}
      singularity_image: docker://nikolaik/python-nodejs:python3.11-nodejs20
      modal_image: nikolaik/python-nodejs:python3.11-nodejs20
      daytona_image: nikolaik/python-nodejs:python3.11-nodejs20
      container_cpu: 1
      container_memory: 5120
      container_disk: 51200
      container_persistent: true
      docker_volumes: []
      docker_mount_cwd_to_workspace: false
      docker_extra_args: []
      docker_run_as_host_user: false
      persistent_shell: true
      lifetime_seconds: 300
        # 如需挂载宿主机目录：
        # volumes:
        #   - /home/user/project:/workspace
    
      # SSH 后端 — 在远程服务器上执行命令
      # backend: ssh
      # ssh:
      #   host: "192.168.1.100"
      #   port: 22
      #   user: "hermes"
      #   # 认证方式二选一：
      #   key_path: "~/.ssh/id_ed25519"    # SSH 密钥
      #   # password: "***"                 # 或密码（推荐放 .env）
    
      # Modal 后端 — 云端无服务器执行
      # backend: modal
      # modal:
      #   token_id: "ak-xxxx"           # Modal API token ID（放 .env）
      #   token_secret: "as-xxxx"       # Modal API token secret（放 .env）
    

当命令需要 sudo 权限时，终端会提示输入密码（会话内缓存）。也可以在 `~/.hermes/.env` 中设置 `SUDO_PASSWORD` 环境变量。

### 4.4 并行工具执行

Hermes 支持通过 `ThreadPoolExecutor` 并行执行多个独立的工具调用（最多 8 个并行 worker）。当 Agent 在同一轮中发出多个互不依赖的工具调用时，它们会自动并行执行，显著减少总耗时。

### 4.5 Smart Approvals 智能审批

受 Codex CLI 启发，Hermes 会**学习** 哪些命令是安全的。当你反复批准同一类命令（如 `git status`、`ls`），Hermes 会逐步减少审批提示。审批模式可以通过 `/yolo` 切换。

### 4.6 Post-Write Linting 写入后检查（v0.13+）

Agent 通过 `patch` 或 `write_file` 写入文件后，会自动进行格式检查，支持 Python、JSON、YAML、TOML。这减少了 Agent 写入格式错误内容的概率。

## 5\. MCP 协议

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp>

MCP（Model Context Protocol）可以把外部工具服务器接入 Hermes。

### 5.1 添加 MCP 服务器

配置示例：**project-fs是本地MCP案例；company_api是外部MCP案例**
    
    
    # ~/.hermes/config.yaml
    mcp_servers:
      project-fs:
        command: "npx"
        args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/my-project"]
    
      company_api:
        url: "https://mcp.internal.example.com/mcp"
        headers:
          Authorization: "Bearer ***"
    

上面两个 server 分别代表两种传输方式：

模式 | 配置方式 | 工作方式 | 适用场景  
---|---|---|---  
stdio | `command` \+ `args` | Hermes 在本机启动 MCP server 进程，通过 stdin / stdout 与其通信 | 本地文件系统、CLI 工具、开发环境里的集成  
HTTP | `url` | Hermes 连接一个已经运行的 MCP server | 公司内部服务、远程 API、共享的工具服务器  
  
常用配置项：

配置项 | 说明  
---|---  
`command` | 本地 stdio MCP Server 的启动命令  
`args` | 传给启动命令的参数  
`env` | 传给 stdio server 的环境变量  
`url` | 远程 HTTP MCP Server 地址  
`headers` | 远程 HTTP 请求头  
`auth: oauth` | 仅用于 HTTP server，启用 OAuth 2.1 授权流程  
`enabled` | 是否启用该 server  
`timeout` | 工具调用超时时间  
`connect_timeout` | 初次连接超时时间  
  
`auth: oauth` 通常需要一次浏览器交互式授权。授权完成后，Hermes 会缓存授权结果，后续调用复用已授权 token。

推荐使用魔搭广场 <https://www.modelscope.cn/mcp>

可以在每个 server 下配置 `tools.include` 或 `tools.exclude`，来控制注册工具白名单或黑名单：
    
    
    # ~/.hermes/config.yaml
    mcp_servers:
      github:
        command: "npx"
        args: ["-y", "@modelcontextprotocol/server-github"]
        env:
          GITHUB_PERSONAL_ACCESS_TOKEN: "***"
        tools:
          include: [list_issues, create_issue, update_issue, search_code]
          resources: false
          prompts: false
    
      stripe:
        url: "https://mcp.stripe.com"
        headers:
          Authorization: "Bearer ***"
        tools:
          exclude: [delete_customer, refund_payment]
    

### 5.2 管理与重载

> 桌面版可以直接管理并重载
    
    
    hermes mcp list                  # 列出已配置的服务器
    hermes mcp test project-fs       # 测试连接
    hermes mcp configure project-fs  # 管理服务器中的工具启用状态
    hermes mcp remove project-fs     # 移除服务器
    
    /reload-mcp  # 修改配置后，在会话内重载 MCP 工具
    

Hermes 启动时会自动发现 MCP 工具。修改 `mcp_servers` 配置后，用 `/reload-mcp` 重新加载；如果 MCP Server 支持动态工具变更通知，Hermes 可以自动刷新工具列表。

### 5.3 MCP Server Mode 反向暴露【重要，操作实用】

MCP Server Mode 是 Hermes 的一个独特功能：它**反过来** 把 Hermes 的会话暴露给 MCP 兼容的客户端。这意味着你可以在 Claude Desktop、VS Code、Cursor 等支持 MCP 的工具中，把 Hermes 当作一个工具服务器来使用。

配置方式：在 MCP 客户端配置中将 Hermes 注册为 MCP server，客户端就可以调用 Hermes 的能力。

例如在 **Claude Desktop** 中，编辑 `claude_desktop_config.json`：
    
    
    {
      "mcpServers": {
        "hermes-agent": {
          "command": "hermes",
          "args": ["mcp", "serve"]
        }
      }
    }
    

配置后重启 Claude Desktop，即可在对话中调用 Hermes 的所有已启用工具。VS Code 和 Cursor 的配置方式类似，将同样的 server 定义加入对应客户端的 `mcpServers` 配置块即可。

### 5.4 Nous-Approved MCP Catalog（v0.15+）

v0.15 引入了 Nous 精选的 MCP 服务器目录，提供交互式选择器。不用再去 GitHub 搜索 MCP server，直接在 Hermes 里浏览和安装：
    
    
    hermes mcp catalog    # 浏览精选 MCP 目录
    

## 6\. SKILL 技能系统

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>

Skills 是 Hermes Agent 最核心的差异化能力——**自进化** 。Agent 解决复杂问题后，会把可复用流程保存为 Skill，下次遇到类似任务时自动加载。Skill 是透明的人类可读 Markdown 文件，你可以随时查看、编辑或删除。

Skills 系统包含 **166 个已追踪的技能** （87 个内置 + 79 个可选），覆盖 26+ 个类别。已安装的技能会以斜杠命令的形式提供。

### 1.1 基本操作
    
    
    hermes skills list                                      # 列出已安装的技能
    hermes skills browse                                    # 浏览可用的技能
    hermes skills search honcho                             # 搜索技能
    hermes skills install honcho                            # 通过 ID 安装技能
    hermes skills install https://example.com/my-skill/SKILL.md  # 通过 URL 安装技能
    hermes skills uninstall honcho                          # 卸载技能
    
    /skills  # 会话内管理技能
    

### 1.2 技能目录结构

所有技能默认存放在 `~/.hermes/skills/`：以下是HermesSKILL目录的解释
    
    
    ~/.hermes/skills/
    ├── mlops/                 # 类别目录
    │   ├── axolotl/           # 技能目录
    │   │   ├── SKILL.md       # 主说明文件，必需
    │   │   ├── references/    # 额外参考资料
    │   │   ├── templates/     # 输出模板
    │   │   ├── scripts/       # 技能可调用的辅助脚本
    │   │   └── assets/        # 图片、数据等附加资源
    │   └── vllm/
    │       └── SKILL.md
    ├── devops/
    │   └── deploy-k8s/
    │       ├── SKILL.md
    │       └── references/
    ├── .hub/                  # Skills Hub 状态
    │   ├── lock.json
    │   ├── quarantine/
    │   └── audit.log
    └── .bundled_manifest      # 记录内置技能同步状态
    

`SKILL.md` 是每个技能的入口文件。`references/`、`templates/`、`scripts/`、`assets/` 都是可选目录。

可以把 Skill 粗略分成三种层级：

类型 | 例子 | 含义  
---|---|---  
普通具体 Skill | `mlops/axolotl` | 面向某个具体工具或流程  
总括型 Skill（umbrella） | `mlops/training` | 覆盖一组相关流程  
类别级总括型 Skill | `software-development/debugging` | 抽象到任务类别  
  
**一个完整的 SKILL.md 示例** （`~/.hermes/skills/writing/tech-blog/SKILL.md`）：
    
    
    # Technical Blog Post Writing
    
    Write technical blog posts targeting AI/ML developers. Follow this workflow:
    
    ## Pre-writing
    1. Read all provided research summaries
    2. Identify 3-5 key takeaways that readers will find actionable
    3. Check for conflicting claims — flag them before writing
    
    ## Structure
    - **Hook** (100-150 words): Start with a real problem or surprising finding
    - **Background** (200-300 words): Context that makes the topic accessible
    - **Deep Dive** (1000-1500 words): Core content with code examples
    - **Implications** (200-300 words): Why this matters for practitioners
    - **Key Takeaways** (bullet points): 3-5 actionable conclusions
    
    ## Code Examples
    - Must be complete and runnable
    - Use Python 3.11+ syntax
    - Include error handling in production-facing code
    - Prefer `uv` over `pip` for package management commands
    
    ## Language
    - Main content in Chinese, technical terms in English
    - Target 2000-2500 words
    - Avoid passive voice in Chinese
    
    ## Frontmatter Template
    ```yaml
    ---
    title: "<English Title>"
    date: <YYYY-MM-DD>
    tags: [<3-5 relevant tags>]
    author: "AI+Human"
    ---
    

可以看到，SKILL.md 就是一份结构化的工作指南，Agent 加载后会自动按照其中的流程执行。

### 1.3 外部技能目录

如果团队已经有共享技能目录，可以让 Hermes 额外扫描：
    
    
    # ~/.hermes/config.yaml
    skills:
      external_dirs:
        - ~/.agents/skills
        - /home/shared/team-skills
        - ${SKILLS_REPO}/skills
    

外部目录支持 `~` 展开和 `${VAR}` 环境变量替换。规则：

  * **只读扫描** ：Agent 创建或修改技能时仍然写入 `~/.hermes/skills/`
  * **本地优先** ：本地版本覆盖外部同名技能
  * **完整集成** ：出现在技能索引、`skills_list`、`skill_view` 和斜杠命令中
  * **路径可选** ：不存在的外部目录会被静默跳过



### 1.4 Skill Bundles

Skill Bundles 允许用一个斜杠命令同时加载多个技能。例如，创建一个 `writing-day` bundle：
    
    
    hermes skills bundle create writing-day --skills blogwatcher,markdown-style,seo-check
    

之后只需执行 `/writing-day` 即可加载全部三个技能。

### 1.5 Skills Hub 与 agentskills.io

Hermes Skills 兼容 [agentskills.io](<https://agentskills.io>) 开放标准。你可以：

  * 从 Skills Hub 浏览和安装社区技能
  * 将自定义技能发布到 Hub 共享
  * 通过 URL 直接安装技能



v0.16 精简了内置技能集，将 NVIDIA/skills 添加为内置可信 Skills Hub tap。

### 1.6 Conditional Activation（条件激活）

技能可以根据**工具可用性** 自动显示/隐藏。例如，如果 Firecrawl API Key 缺失，Hermes 会自动回退到 DuckDuckGo 搜索技能。

### 1.7 Platform-Specific Skills（平台特定技能）

技能可以限定在特定操作系统上生效：（就是在SKILL的元数据中写明支持的系统）
    
    
    # SKILL.md frontmatter
    platforms:
      - linux
      - macos
      # - windows  # 此技能不在 Windows 上显示
    

### 1.8 Agent-Managed Skills (skill_manage)【重要，操作实用】

Hermes 可以通过 `skill_manage` 工具创建、修改和删除自己的技能。这是 Agent 的「程序记忆」：当它解决了一个有复用价值的复杂问题，就可以把流程沉淀成 Skill。

触发策略主要靠提示词驱动。整体规则：

  * 复杂任务成功、克服错误、用户纠正后的方法有效、发现可复用流程，或用户要求记住流程时，可以创建 Skill
  * 发现 Skill 过时、缺步骤、命令错误、OS 相关失败或新坑点时，应优先 `patch` 现有 Skill



`skill_manage` 常见动作：

动作 | 用途  
---|---  
`create` | 从零创建一个新技能  
`patch` | 对现有技能做小范围修改，优先使用  
`edit` | 整体重写技能内容  
`delete` | 删除技能  
`write_file` | 添加或更新 `references/`、`scripts/` 等支持文件  
`remove_file` | 删除支持文件  
  
**`create` 完整调用示例**：当 Agent 发现一个值得沉淀的工作流程后：
    
    
    skill_manage(
        action="create",
        name="docker-troubleshooting",
        category="devops",
        description="Systematic Docker troubleshooting workflow for production environments.",
        content="# Docker Troubleshooting\n...",
        umbrella="devops/troubleshooting",  # 可选：归到已有 umbrella 下
    )
    # 返回：技能已创建在 ~/.hermes/skills/devops/docker-troubleshooting/SKILL.md
    

**`patch` 使用示例**：发现已有技能需要修正一小部分：
    
    
    skill_manage(
        action="patch",
        name="docker-troubleshooting",
        old_string="docker logs --tail 50",
        new_string="docker logs --tail 100 --timestamps",
        reason="增加时间戳和日志行数，便于关联时间线排查",
    )
    

**Agent 优先使用`patch` 而非 `edit`，**避免意外覆盖用户手动调整的内容。

### 1.9 Curator 技能维护系统【重要，原理须知】

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/curator>
> 
> **默认：** 非官方的SKILL（具体解释看本节最后一句话）超过30天未使用会被标记为 低活跃；超过90天没用会移动到归档中，再去会话中Agent无法自动调用，需要用户指定才会重新唤醒这个SKILL，唤醒成功后这个SKILL重新被标记为 活跃 。

Curator 是 Hermes 的技能维护系统，专门管理由后台自我改进 review agent 创建并标记的本地技能。它会跟踪这些技能的查看、使用和修改频率，把长期不用的技能从 `active` 推进到 `stale`，再归档到 `~/.hermes/skills/.archive/`。

Curator 的存在是为了防止通过自我提升循环产生的技能无限累积。如果不进行维护，最终会导致数十个功能相近但范围狭窄的重复技能，污染目录并浪费 token。

#### Pinned 技能保护

如果某个技能很重要，可以把它 pin 住。Pinned 技能有三层保护：

  * Curator 不会把它自动迁移到 `stale` 或 `archived`
  * Curator 的 LLM Review 会跳过它
  * Agent 的 `skill_manage delete` 也不能删除它，但仍然可以 `patch` / `edit`



#### 运行机制

Curator 在 Hermes 启动或 Gateway 后台 tick 时检查。自动运行需要同时满足：

  * `curator.enabled` 未被设为 `false`
  * 未被 `hermes curator pause` 暂停
  * 距离上次运行超过 `interval_hours`（默认 168 小时 / 7 天）
  * Agent 已空闲超过 `min_idle_hours`（默认 2 小时）



每次运行按两阶段执行：

  1. **自动状态迁移** （不调用 LLM）：超过 `stale_after_days` (30天) 未使用的技能变成 `stale`，超过 `archive_after_days` (90天) 未使用的移动到 `.archive/`
  2. **LLM Review** ：启动辅助模型，决定保留、修补、合并或归档。目标是构建"类别级指令和经验知识"的库



#### 配置
    
    
    # ~/.hermes/config.yaml
    curator:
      enabled: true
      interval_hours: 168
      min_idle_hours: 2
      stale_after_days: 30
      archive_after_days: 90
    

可以为 Curator 指定更便宜的辅助模型：
    
    
    # ~/.hermes/config.yaml
    auxiliary:
      curator:
        provider: openrouter
        model: google/gemini-3-flash-preview
        timeout: 600
    

#### 常用命令
    
    
    hermes curator status                   # 查看技能状态
    hermes curator run                      # 手动运行策展
    hermes curator run --background         # 后台运行
    hermes curator run --dry-run            # 只预览，不修改技能库
    hermes curator pause                    # 暂停自动运行
    hermes curator resume                   # 恢复自动运行
    hermes curator pin my-important-skill   # 固定某个技能
    hermes curator unpin my-important-skill # 取消固定
    hermes curator restore my-skill         # 恢复已归档的技能
    hermes curator rollback                 # 恢复最新备份
    

同样的子命令也可以在会话中通过 `/curator` 斜杠命令使用。

#### 哪些技能会被处理

Curator 只处理同时满足以下条件的技能：

  * 位于本地技能目录 `~/.hermes/skills/`
  * 不是 bundled 内置技能
  * 不是 Skills Hub 安装的技能
  * 被标记为 `created_by: "agent"` 或 `agent_created: true`



用户手写的 SKILL.md、外部技能目录中的 Skill、bundled 内置技能和 Skills Hub 安装的技能都不会被 Curator 自动归档或合并。

## 7\. Hooks 钩子系统

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks>

Hermes 提供了三种钩子系统，允许在关键生命周期点执行自定义代码。所有钩子都是非阻塞设计，错误会被捕获并记录，不会影响Agent 运行。

三种钩子对比：

维度 | Shell Hooks | Plugin Hooks | Gateway Hooks  
---|---|---|---  
语言 | 任意（Bash、Python、Go 等） | 仅 Python | 仅 Python  
运行环境 | CLI + Gateway | CLI + Gateway | 仅 Gateway  
事件名 | Agent 内部事件名 | Agent 内部事件名 | 带冒号的 Gateway 事件名  
注册位置 | `~/.hermes/config.yaml` 的 `hooks:` | 插件 `register(ctx)` 中注册 | `~/.hermes/hooks/<name>/HOOK.yaml`  
典型用例 | 阻止危险命令、自动格式化、注入 git 状态 | 工具拦截、指标采集、防护措施、记忆召回 | 日志记录、告警通知、Webhook 回调  
  
常见钩子事件：

钩子 | 适用系统 | 触发时机 | 常见用途 | 是否能影响流程  
---|---|---|---|---  
`pre_tool_call` | Shell / Plugin | 工具执行前 | 阻止危险命令、检查参数、审计调用 | 可以返回 `block` 阻止  
`post_tool_call` | Shell / Plugin | 工具返回后 | 记录结果、采集指标、跟踪生成文件 | 观察型  
`pre_llm_call` | Shell / Plugin | 每轮 LLM 调用前 | 注入 git 状态、外部上下文、策略提示 | 可以返回 `context` 注入  
`post_llm_call` | Shell / Plugin | 每轮 LLM 调用结束后 | 记录响应、同步记忆、采集 token 指标 | 观察型  
`on_session_start` | Shell / Plugin | 新会话开始时 | 初始化会话状态、打开外部连接 | 观察型  
`on_session_end` | Shell / Plugin | 会话结束、重置或退出时 | 清理资源、flush 缓存、发送通知 | 观察型  
`gateway:startup` | Gateway | Gateway 进程启动时 | 启动检查、告警、注册 Webhook | 观察型  
`session:start` / `session:end` / `session:reset` | Gateway | Gateway 会话创建、结束或重置时 | 记录消息平台会话、审计用户行为 | 观察型  
`agent:start` / `agent:step` / `agent:end` | Gateway | Gateway 中 Agent 处理消息的过程 | 监控长任务、记录工具循环、统计耗时 | 观察型  
`command:*` | Gateway | Gateway 里执行任意斜杠命令时 | 命令审计、权限统计、外部通知 | 观察型  
  
### 7.1 Shell Hook 示例：会话结束后弹出桌面通知

适合在 WSL / Git Bash / Windows 终端里使用 Hermes。

  1. Linux注册 shell hook：


    
    
    # ~/.hermes/config.yaml
    hooks:
      on_session_end:
        - command: "~/.hermes/agent-hooks/windows-session-end-popup.sh"
          timeout: 15
    

​ windows注册 shell hook：
    
    
    # xxxx/hermes/config.yaml
    hooks:
      on_session_end:
      - command: C:/PROGRA~1/Git/bin/bash.exe "C:/Users/merge/AppData/Local/hermes/hooks/windows-session-end-popup.sh"
        timeout: 15
    hooks_auto_accept: true
    

  2. 创建脚本目录：


    
    
    mkdir -p ~/.hermes/agent-hooks
    

  3. 创建脚本 `~/.hermes/agent-hooks/windows-session-end-popup.sh`：


    
    
    #!/usr/bin/env bash
    cat - >/dev/null     # 丢弃 hook payload（stdin）
    
    if command -v powershell.exe >/dev/null 2>&1; then
      powershell.exe -NoProfile -WindowStyle Hidden -Command '
        Add-Type -AssemblyName System.Windows.Forms
        Add-Type -AssemblyName System.Drawing
    
        $f = New-Object System.Windows.Forms.Form
        $f.Text = "Hermes"
        $f.Width = 300
        $f.Height = 100
        $f.FormBorderStyle = "None"
        $f.StartPosition = "CenterScreen"
        $f.BackColor = [System.Drawing.Color]::FromArgb(32, 32, 32)
        $f.ForeColor = [System.Drawing.Color]::White
        $f.TopMost = $true
        $f.ShowInTaskbar = $false
    
        $label = New-Object System.Windows.Forms.Label
        $label.Text = "Session finished"
        $label.Font = New-Object System.Drawing.Font("Segoe UI", 10, [System.Drawing.FontStyle]::Bold)
        $label.ForeColor = [System.Drawing.Color]::White
        $label.AutoSize = $true
        $label.Location = New-Object System.Drawing.Point(20, 30)
        $f.Controls.Add($label)
    
        $timer = New-Object System.Windows.Forms.Timer
        $timer.Interval = 3000
        $timer.Add_Tick({ $f.Close() })
        $timer.Start()
    
        $f.ShowDialog()
        $f.Dispose()
      ' >/dev/null 2>&1 &
    fi
    
    printf '{}\n'
    

  4. 赋予执行权限：


    
    
    chmod +x ~/.hermes/agent-hooks/windows-session-end-popup.sh
    

首次运行时 Hermes 会询问是否允许这个 `(event, command)` 组合。

### 7.2 pre_tool_call 安全拦截示例

`pre_tool_call` 是唯一能**阻止** 工具执行的钩子，适合安全防护场景。

**场景** ：阻止 Agent 执行危险的终端命令（如 `rm -rf /`、`DROP TABLE`、未授权的 SSH 连接）。

  1. 注册 hook：


    
    
    # ~/.hermes/config.yaml
    hooks:
      pre_tool_call:
        - command: "~/.hermes/agent-hooks/danger-guard.sh"
          timeout: 5
    

  2. 创建 `~/.hermes/agent-hooks/danger-guard.sh`：


    
    
    #!/usr/bin/env bash
    PAYLOAD=$(cat)  # Hermes 把工具调用信息通过 stdin 传入（JSON 格式）
    
    TOOL_NAME=$(echo "$PAYLOAD" | python3 -c "import sys,json; print(json.load(sys.stdin).get('name',''))")
    PARAMS=$(echo "$PAYLOAD" | python3 -c "import sys,json; print(json.dumps(json.load(sys.stdin).get('parameters',{})))")
    
    # 仅检查 terminal 工具
    if [ "$TOOL_NAME" != "terminal" ]; then
      printf '{"action":"allow"}\n'   # 返回 allow 表示放行
      exit 0
    fi
    
    # 从参数中提取命令
    CMD=$(echo "$PARAMS" | python3 -c "import sys,json; print(json.load(sys.stdin).get('command',''))")
    
    # 危险模式黑名单
    if echo "$CMD" | grep -qiE "rm\s+-rf\s+/|DROP\s+TABLE|shutdown|mkfs\.|>\/dev\/sda|chmod\s+-R\s+777\s+/"; then
      printf '{"action":"block","reason":"Dangerous command blocked by guard hook"}\n'
      exit 0
    fi
    
    printf '{"action":"allow"}\n'
    

  3. 赋予权限：


    
    
    chmod +x ~/.hermes/agent-hooks/danger-guard.sh
    

关键：`pre_tool_call` 脚本返回 `{"action":"block"}` 会阻止工具执行并告知 Agent 原因；返回 `{"action":"allow"}` 则放行。

## 8\. Plugins 插件系统

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins>

Hermes 拥有一个插件系统，无需修改核心代码即可添加自定义工具、钩子和集成。

### 8.1 插件能做什么

插件通过 `register(ctx)` 函数接入 Hermes，`ctx` 上所有公开 API 均可使用：

扩展类型 | 说明  
---|---  
工具 | 给模型增加可调用能力，例如外部 API、本地服务或自定义逻辑  
钩子 | 在工具调用、LLM 调用、会话开始 / 结束等生命周期点执行代码  
命令 | 增加 `/name` 斜杠命令，或增加 `hermes <plugin> ...` 子命令  
会话注入 | 把外部事件、消息或数据注入当前会话  
Skill / 数据 | 随插件附带 Skill、模板、配置、静态数据等资源  
Gateway 平台 | 接入新的消息平台或自定义平台适配器  
后端提供商 | 接入新的记忆、上下文压缩、图像生成、视频生成或 LLM 提供商  
  
> **v0.14+** 插件可以通过 `ctx.llm` 直接在插件代码中调用当前活跃的模型提供商。

> **v0.13+** 第三方提供商可通过 `ProviderProfile` ABC（抽象基类）实现自定义 LLM 提供商插件。

### 8.2 插件目录【重要，操作实用】

用户插件目录是 `~/.hermes/plugins/`，每个插件一个独立子目录。最小可用插件只需要两个文件：
    
    
    ~/.hermes/plugins/hello-world/
    ├── plugin.yaml      # 插件清单：名称、版本、描述等元信息
    └── __init__.py      # 定义 register(ctx)，在这里注册工具 / hook / 命令
    

`plugin.yaml` 让 Hermes 知道"这里有一个插件"，`register(ctx)` 决定"这个插件实际提供什么能力"。

### 8.3 插件示例：shake_window

注册一个 `shake_window` 工具，让当前 Windows 前台窗口轻微晃动。

创建目录：
    
    
    mkdir -p ~/.hermes/plugins/shake-window
    

创建 `~/.hermes/plugins/shake-window/plugin.yaml`：
    
    
    name: shake-window
    version: "1.0"
    description: Provides a shake_window tool that briefly shakes the current Windows foreground window.
    

创建 `~/.hermes/plugins/shake-window/__init__.py`：
    
    
    import json
    import shutil
    import subprocess
    
    
    POWERSHELL_SHAKE = r"""
    Add-Type @"
    using System;
    using System.Runtime.InteropServices;
    
    public static class Win32 {
        [DllImport("user32.dll")]
        public static extern IntPtr GetForegroundWindow();
        [DllImport("user32.dll")]
        public static extern bool GetWindowRect(IntPtr hWnd, out RECT rect);
        [DllImport("user32.dll")]
        public static extern bool MoveWindow(IntPtr hWnd, int X, int Y, int nWidth, int nHeight, bool bRepaint);
    }
    
    [StructLayout(LayoutKind.Sequential)]
    public struct RECT {
        public int Left; public int Top; public int Right; public int Bottom;
    }
    "@
    
    $hwnd = [Win32]::GetForegroundWindow()
    if ($hwnd -eq [IntPtr]::Zero) { exit 1 }
    $rect = New-Object RECT
    [Win32]::GetWindowRect($hwnd, [ref]$rect) | Out-Null
    $x = $rect.Left; $y = $rect.Top
    $w = $rect.Right - $rect.Left; $h = $rect.Bottom - $rect.Top
    
    for ($i = 0; $i -lt 8; $i++) {
        [void][Win32]::MoveWindow($hwnd, $x - 12, $y, $w, $h, $true)
        Start-Sleep -Milliseconds 45
        [void][Win32]::MoveWindow($hwnd, $x + 12, $y, $w, $h, $true)
        Start-Sleep -Milliseconds 45
    }
    [void][Win32]::MoveWindow($hwnd, $x, $y, $w, $h, $true)
    """
    
    
    def register(ctx):
        schema = {
            "name": "shake_window",
            "description": "Shake the current Windows foreground window.",
            "parameters": {
                "type": "object",
                "properties": {},
            },
        }
    
        def handle_shake(params, **kwargs):
            del params, kwargs
            powershell = shutil.which("powershell.exe")
            if powershell is None:
                return json.dumps({"ok": False, "error": "powershell.exe not found"})
            result = subprocess.run(
                [powershell, "-NoProfile", "-Command", POWERSHELL_SHAKE],
                text=True, capture_output=True, check=False,
            )
            return json.dumps({
                "ok": result.returncode == 0,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip(),
            })
    
        ctx.register_tool(
            name="shake_window",
            toolset="desktop_fun",
            schema=schema,
            handler=handle_shake,
            description="Shake the current Windows foreground window.",
        )
    

启用插件：
    
    
    hermes plugins enable shake-window
    

重新启动 Hermes 后，模型就能调用 `shake_window` 工具。如：`使用shake_window 工具震动窗口`

### 8.4 插件发现

Hermes 会从多个来源发现插件：

来源 | 路径 / 方式 | 用途  
---|---|---  
Bundled | Hermes 仓库内置 `plugins/` | 官方随 Hermes 发布的插件  
User | `~/.hermes/plugins/` | 用户自己的本地插件  
Project | `.hermes/plugins/` | 当前工作目录插件；默认不扫描，需设置 `HERMES_ENABLE_PROJECT_PLUGINS=true`  
pip | `hermes_agent.plugins` entry points | 通过 Python 包分发的插件  
  
### 8.5 管理插件
    
    
    hermes plugins                    # 交互式开关插件
    hermes plugins list               # 查看已安装插件
    hermes plugins install user/repo  # 从 GitHub 安装插件
    hermes plugins update <name>      # 更新插件
    hermes plugins remove <name>      # 移除插件
    hermes plugins enable <name>      # 启用插件
    hermes plugins disable <name>     # 禁用插件
    

新安装或捆绑的插件默认不启用，必须加入 `~/.hermes/config.yaml`：
    
    
    # ~/.hermes/config.yaml
    plugins:
      enabled:
        - my-plugin
      disabled:
        - noisy-plugin
    

`plugins.disabled` 是拒绝列表，如果同一个插件同时出现在 `enabled` 和 `disabled`，禁用优先。

* * *

## 9\. Cron 定时任务

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/cron>

Hermes 内置定时任务系统，可以用自然语言、cron 表达式安排任务。

定时任务通过 Gateway daemon 执行：Gateway 每 60 秒 tick 一次，检查到期任务。为每个到期任务启动一个新的 Agent 会话执行 prompt，然后投递最终结果。Cron 运行时会禁用 cron 管理工具，避免递归创建更多定时任务造成调度循环。

### 9.1 创建任务【重要，操作实用】

可在会话中通过 `/cron`，或使用 CLI 命令 `hermes cron` 来创建：
    
    
    /cron add 30m "提醒我检查构建结果"
    /cron add "every 2h" "检查服务器状态"
    /cron add "every 1h" "总结新动态" --skill blogwatcher
    /cron add "every 1h" "加载两个技能并合并结果" --skill blogwatcher --skill maps
    
    hermes cron create "every 2h" "检查服务器状态"
    hermes cron create "every 1h" "总结新动态" --skill blogwatcher
    

也可以直接用自然语言让 Hermes 创建：
    
    
    每天早上 9 点检查 Hacker News 上的 AI 新闻，然后发一份摘要到 Telegram。
    

Hermes 会在内部调用 `cronjob` 工具完成创建：
    
    
    cronjob(
        action="create",
        schedule="every 1d at 09:00",
        prompt="检查 Hacker News 上的 AI 新闻，筛选值得关注的条目，并写成中文摘要。",
        name="HN AI daily",
        deliver="telegram",
    )
    

### 9.2 调度格式

类型 | 示例 | 行为  
---|---|---  
相对延迟 | `30m`、`2h`、`1d` | 一次性运行  
循环间隔 | `every 30m`、`every 2h`、`every 1d` | 持续重复运行  
Cron 表达式 | `0 9 * * *`、`0 9 * * 1-5`、`0 */6 * * *` | 按 cron 规则重复运行  
ISO 时间 | `2026-03-15T09:00:00` | 指定时间运行一次  
  
Cron 表达式格式为 `分 时 日 月 周`：

  * `0 9 * * *` 每天 9:00 执行
  * `0 9 * * 1-5` 工作日每天 9:00 执行
  * `0 */6 * * *` 每 6 小时执行
  * `30 8 1 * *` 每月 1 日 8:30 执行



### 9.3 管理任务
    
    
    /cron list                                          # 查看定时任务
    /cron list --all                                    # 查看所有任务，包括已暂停的
    /cron edit <job_id> --schedule "every 4h"           # 修改调度时间
    /cron edit <job_id> --prompt "使用新的任务说明"       # 修改任务说明
    /cron edit <job_id> --skill blogwatcher --skill maps # 替换技能列表
    /cron edit <job_id> --add-skill maps               # 追加技能
    /cron edit <job_id> --remove-skill blogwatcher     # 移除指定技能
    /cron pause <job_id>                               # 暂停任务
    /cron resume <job_id>                              # 恢复任务
    /cron run <job_id>                                 # 下一个 scheduler tick 触发任务
    /cron remove <job_id>                              # 删除任务
    
    hermes cron status     # 查看调度器状态
    hermes cron tick       # 手动触发一次 scheduler tick
    

任务存储在 `~/.hermes/cron/jobs.json`，运行输出保存到 `~/.hermes/cron/output/{job_id}/{timestamp}.md`。

### 9.4 运行结果投递方式

`deliver` 控制定时任务运行完成后，把 Agent 的最终回复发送到哪里：

deliver | 说明  
---|---  
`origin` | 回到创建任务的聊天来源，消息平台默认值  
`local` | 只保存到本地文件，CLI 默认值  
`telegram`、`discord`、`slack` | 投递到对应平台的 home channel  
`telegram:123456` | 投递到指定 Telegram chat ID  
`discord:#engineering` | 投递到指定 Discord 频道  
`all` | 投递到所有已配置 home channel 的平台  
`telegram,discord` | 投递到多个指定平台  
`origin,all` | 投递到来源聊天 + 所有 home channel  
`ntfy` | v0.15+：推送通知，无需账号  
  
示例：
    
    
    hermes cron create "every 30m" "检查服务状态" --deliver telegram
    hermes cron create "every 1d" "生成日报" --deliver telegram,discord
    

如果 Agent 的最终回复以 `[SILENT]` 开头，成功运行时会抑制投递，但输出仍会保存到本地。失败任务仍会投递错误信息。适合只有出现问题才需要报告的作业：
    
    
    Check if nginx is running. If everything is healthy, respond with only [SILENT].
    Otherwise, report the issue.
    

### 9.5 No-Agent 模式

对于不需要 LLM 推理的周期性任务（监控程序、磁盘/内存警报、心跳检测、CI ping 等），可传递 `no_agent=True`：
    
    
    hermes cron create "every 5m" \
      --no-agent \
      --script memory-watchdog.sh \
      --deliver telegram \
      --name "memory-watchdog"
    

脚本必须放在 `~/.hermes/scripts/` 中。`.sh` / `.bash` 用 `/bin/bash` 执行，其他脚本用当前 Python 解释器执行。

脚本运行默认超时 120 秒，可调整：
    
    
    # ~/.hermes/config.yaml
    cron:
      script_timeout_seconds: 300
    

### 9.6 使用 context_from 链接作业

Cron 任务彼此之间默认隔离。`context_from` 用来把一个任务的最新输出接到另一个任务的 prompt 前面。它只能由 Agent 通过 `cronjob` 工具设置，CLI 命令不支持。

典型流程：
    
    
    Job 1：收集原始数据
    Job 2：读取 Job 1 的最新输出，筛选 / 排序
    Job 3：读取 Job 2 的最新输出，生成最终报告并投递
    

示例：
    
    
    # Job 1：收集 AI 新闻
    cronjob(action="create", name="ai-news-fetch",
            schedule="0 7 * * *",
            prompt="Fetch the top 10 AI/ML stories from Hacker News.")
    
    # Job 2：使用 Job 1 的最新输出做筛选
    cronjob(action="create", name="ai-news-rank",
            schedule="30 7 * * *",
            context_from="<job1_id>",
            prompt="Score each story for novelty and engagement. Keep the top 5.")
    
    # Job 3：使用 Job 2 的最新输出生成日报
    cronjob(action="create", name="ai-news-brief",
            schedule="0 8 * * *",
            context_from="<job2_id>",
            prompt="Write a concise daily brief and deliver it to Telegram.")
    

`context_from` 支持单个或多个 job ID。多个上游输出会按列表顺序拼接，每个上游输出在注入前被截断至 8,000 字符。

> **注意** ：`context_from` 读取的是上游任务「最近一次已完成输出」，不会等待同一个 tick 中仍在运行的上游任务。需要强依赖同一批数据时，应把上下游任务错开足够长时间。

# 三、协作交互

## 1\. Gateway 消息网关

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/>

Gateway 是 Hermes 的消息平台接入层，可以作为前台进程或后台服务运行。它负责连接 Telegram、Discord、Slack、微信等平台，接收消息，维护每个聊天对应的会话，把消息转发给 Hermes Agent 处理，再把回复发回原平台。

Gateway 和 CLI 模式使用同一套 Hermes 程序、配置、会话、记忆、技能和工具。区别在于：CLI 是终端里的单次交互入口，Gateway 是长期运行的消息平台适配进程。Gateway 还会运行 cron 调度循环，用来触发到期的计划任务。

### 1.1 命令
    
    
    hermes gateway setup                 # 交互式配置消息平台
    hermes gateway                       # 前台启动 Gateway
    hermes gateway install               # 安装为用户服务（Linux）/ launchd 服务（macOS）
    sudo hermes gateway install --system # 仅 Linux：安装为开机启动的系统服务
    hermes gateway start                 # 启动默认服务
    hermes gateway restart               # 重启网关
    hermes gateway stop                  # 停止默认服务
    hermes gateway status                # 查看默认服务状态
    hermes gateway status --system       # 仅 Linux：检查系统服务状态
    

#### Telegram Bot 端到端搭建

以 Telegram 为例，完整的 Gateway 接入流程如下：

**步骤 1：创建 Bot**

在 Telegram 中搜索 `@BotFather`，发送 `/newbot`，按提示设置名称和用户名，获得 Bot Token（格式：`1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`）。

**步骤 2：配置 Hermes**
    
    
    # 将 Bot Token 写入 .env
    echo "TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz" >> ~/.hermes/.env
    
    # 交互式配置 Gateway（Telegram 选项）
    hermes gateway setup
    

**步骤 3：启动 Gateway**
    
    
    # 前台运行（调试用）
    hermes gateway
    
    # 安装为系统服务（推荐生产环境）
    hermes gateway install
    hermes gateway start
    

**步骤 4：验证配对**

首次与 Bot 私信时，Bot 会回复配对码。管理员在本机批准：
    
    
    hermes pairing list          # 查看待审批的配对请求
    hermes pairing approve telegram XKGH5N7P
    

此后该用户即可与 Hermes 自由对话。

### 1.2 支持的消息平台【重要，操作实用】

> （每次修改配置文件后需要重启网关，命令上面有 ）

Hermes Gateway 支持 **23 个以上的消息平台** ：

Telegram、Discord、Slack、WhatsApp、Signal、DingTalk、SMS (Twilio)、Mattermost、Matrix、Webhook、Email (IMAP/SMTP)、Home Assistant、Feishu/Lark、WeCom、Weixin（微信）、BlueBubbles (iMessage)、QQBot、Yuanbao、IRC、Microsoft Teams、Google Chat、LINE、SimpleX Chat、**ntfy** （v0.15+，无需账号的推送通知）

**配置邮箱的步骤（只能手动修改配置文件）：**

  1. 打开邮箱的**POP3/SMTP/IMAP** （不同邮箱入口不同，自行百度）

  2. 开启服务：IMAP/SMTP服务、POP3/SMTP服务

  3. 记录SMTP服务器地址、IMAP服务器地址

  4. 找到自己邮箱平台的端口号（不同邮箱端口不同，自行百度）

  5. 进入到安装目录下hermes/.env文件，添加：
         
         # Hermes代理的邮箱配置  .env
         EMAIL_PASSWORD=QHaqxxxxxxxxxxxxxxxxxxxxx
         EMAIL_IMAP_HOST=imap.163.com
         EMAIL_SMTP_HOST=smtp.163.com
         EMAIL_SMTP_PORT=465
         EMAIL_ADDRESS=yaohm7788@163.com
         # 允许什么人发消息给你（桌面版：消息平台——email——Allowed users 填写 true 就是所有人，也可以填某个邮箱）
         EMAIL_ALLOW_ALL_USERS=true
         

  6. 打开/重启网关：hermes gateway start / hermes gateway restart

  7. 测试：用自己邮箱A 发消息给 Hermes代理的邮箱B。B会回复一个邮箱。  
（必须 EMAIL_ALLOW_ALL_USERS=true 或者 是A邮箱的地址）




**配置微信的步骤：**

  1. cmd进入网关设置界面：hermes gateway setup

  2. 选择WeiXin，输入 y。出现二维码

  3. 手机个人微信扫描二维码即可登录

  4. 登录成功，后续设置配置自行决定（命令行会提供选项）

> 建议都使用默认，也就是它推荐的

  5. 自动询问是否要重启网关，确认重启（如果没出现就手动输入命令重启，**不要关闭网关界面后续有用** ）

  6. 完成以上步骤基本配置完成，进入安装目录下hermes/.env文件查看
         
         # 微信配置 https://hermes-agent.nousresearch.com/docs/zh-Hans/user-guide/messaging/weixin
         WEIXIN_ACCOUNT_ID=c94b6aa27d45@im.bot
         WEIXIN_TOKEN=c94b6aa27d45@im.bot:06xxxxxxxxxxxxxxxxxxxxx
         WEIXIN_BASE_URL=https://ilinkai.weixin.qq.com
         WEIXIN_CDN_BASE_URL=https://novac2c.cdn.weixin.qq.com/c2c
         WEIXIN_DM_POLICY=pairing
         WEIXIN_ALLOW_ALL_USERS=false
         WEIXIN_ALLOWED_USERS=
         WEIXIN_GROUP_POLICY=disabled
         WEIXIN_GROUP_ALLOWED_USERS=
         WEIXIN_HOME_CHANNEL=o9cq800SHCEm-xxxxxxxxxxxxxxxxxxxxx@im.wechat
         

  7. 微信会自动出现一个clawbot的对话框，发送消息给这个对话框，发送失败

  8. 此时网关界面会出现：有一个无权限的用户尝试访问，并指出给出`会话id` （以@im.wechat结尾的字符串）

  9. 授权

     1. 全部授权（所有人都可以和Hermes对话）：WEIXIN_ALLOW_ALL_USERS=true
     2. 指定授权（指定会话才可以和Hermes对话）：WEIXIN_ALLOWED_USERS=xxxxx@im.wechat
  10. cmd重启网关：hermes gateway restart

  11. 现在可以开始对话了




### 1.3 网关配对

默认情况下，网关会拒绝所有不在允许列表中或未通过私信配对的用户。

#### 允许列表

在 `~/.hermes/.env` 中配置：（每次修改配置文件后需要重启网关，命令上面有 ）
    
    
    # 按平台限制用户
    TELEGRAM_ALLOWED_USERS=123456789,987654321
    WEIXIN_ALLOWED_USERS=123456789,987654321
    
    # 或配置通用允许列表
    GATEWAY_ALLOWED_USERS=123456789,987654321
    
    # 显式允许所有用户（不推荐给有终端访问权限的机器人使用）
    GATEWAY_ALLOW_ALL_USERS=true
    

#### 私信配对

无需手动配置用户 ID，未知用户在私信机器人时会收到一次性配对码，例如 `Pairing code: XKGH5N7P`。之后管理员在本机批准：
    
    
    hermes pairing approve telegram XKGH5N7P  # 批准配对
    hermes pairing list                       # 查看配对列表
    hermes pairing revoke telegram <user_id>  # 撤销配对
    

配对码 1 小时后过期，有速率限制，并使用加密随机数生成。

#### 斜杠命令权限控制

权限分层只控制斜杠命令，不影响普通聊天。规则：

  1. 先判断用户是否被允许使用 Gateway
  2. 再判断当前作用域是否启用了命令权限分层
  3. 未配置 admin 列表时，所有已允许用户都可以运行斜杠命令
  4. 配置了 admin 列表时，管理员可运行所有命令，普通用户只能运行显式允许的命令（以及始终可用的 `/help` 和 `/whoami`）


    
    
    # ~/.hermes/config.yaml
    gateway:
      platforms:
        discord:
          extra:
            allow_from: ["111", "222", "333"]
            allow_admin_from: ["111"]
            user_allowed_commands: [status, model]
            group_allow_admin_from: ["111"]
            group_user_allowed_commands: [status]
    

用 `/whoami` 查看当前平台、作用域、权限层级和可运行的斜杠命令。

## 2\. Profile 多实例

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/profiles>

通过 Profile 运行多个独立的 Hermes Agent，每个 Agent 有独立的配置、会话、技能和记忆。

### 2.1 什么是 Profile

Profile 是一个独立的 Hermes home 目录。其中包含各自的 `config.yaml`、`.env`、`SOUL.md`、记忆、会话、技能、cron 任务、状态数据库和 Gateway 状态。

通过 Profile 可以运行用于不同用途的 Agent 而不会混淆 Hermes 状态。

创建 Profile 后，Hermes 会自动生成同名命令别名。例如创建 `coder` 后，可以直接使用 `coder chat`、`coder setup`、`coder gateway start`，本质上等价于 `hermes -p coder ...`。

### 2.2 创建 Profile【重要，操作实用】
    
    
    hermes profile create coder                     # 创建空白 Profile，内置技能会初始化
    hermes profile create coder --description "负责阅读源码、实现已明确的代码修改、修复测试或构建问题、运行必要验证，并在完成后汇报改动、测试结果和剩余风险"
    hermes profile create coder --clone             # 克隆当前 Profile 的 config.yaml、.env、SOUL.md
    hermes profile create backup --clone-all        # 克隆完整状态
    hermes profile create coder --clone --clone-from backup  # 从指定 Profile 克隆
    hermes profile describe coder --text "..."      # 为 Profile 添加描述@
    hermes profile describe coder --auto            # 用辅助模型自动生成描述  
    hermes profile delete coder                     # 删除 Profile
    

### 2.3 使用 Profile
    
    
    coder chat                                      # 启动 coder profile 的交互式对话
    coder setup                                     # 运行 coder profile 的配置向导
    coder gateway start                             # 启动 coder profile 的 Gateway 服务
    coder doctor                                    # 检查 coder profile 的健康状态
    coder skills list                               # 查看已安装的 skills
    coder config set model.default anthropic/claude-sonnet-4  # 修改默认模型
    

别名本质上等价于 `hermes -p <name>`。也可以显式指定：`hermes -p coder chat`。

设置默认 Profile：
    
    
    hermes profile use coder    # 默认使用 coder Profile
    hermes profile use default  # 恢复为 default
    

### 2.4 工作原理

Profile 使用 `HERMES_HOME` 环境变量。运行 `coder chat` 时，包装脚本会在启动 Hermes 前设置 `HERMES_HOME=~/.hermes/profiles/coder`。每个 Profile 都可以作为独立进程运行自己的 Gateway，拥有自己的 bot token。

## 3\. Delegation 任务委派【重要，原理须知】

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation>

Hermes 可以创建子 Agent 来处理独立的任务。子 Agent 有自己的对话和终端环境，互不干扰。

### 3.1 单任务与并行批量

**单任务：**
    
    
    delegate_task(
        goal="Debug why tests fail",
        context="Error: assertion in test_foo.py line 42",
        toolsets=["terminal", "file"],
    )
    

**并行批量（默认最多 3 并发，可通过`max_concurrent_children` 调高）：**
    
    
    delegate_task(tasks=[
        {"goal": "Research topic A", "toolsets": ["web"]},
        {"goal": "Research topic B", "toolsets": ["web"]},
        {"goal": "Fix the build", "toolsets": ["terminal", "file"]},
    ])
    

超过 `max_concurrent_children` 的批量请求会直接返回工具错误。结果按输入顺序排列。父 Agent 中断会传播到所有活跃子 Agent。

### 3.2 子 Agent 上下文

子 Agent 启动时拥有全新对话，不知道父会话之前的任何内容。唯一上下文来自接收的 `goal` 和 `context` 两个字段：

  * `goal`：任务目标（必填）
  * `context`：完成目标所需的全部背景信息



子 Agent 完成后，只有结构化摘要回传到父会话，详细对话过程不保留，以此控制 token 开销。

### 3.3 工具集限制

toolsets | 适用场景  
---|---  
`["terminal", "file"]` | 编码、调试、文件编辑  
`["web"]` | 调研、查文档  
`["terminal", "file", "web"]` | 全栈任务（默认）  
  
某些工具限制为子 Agent 无法使用：

工具 | 原因  
---|---  
`delegation` | 叶子节点禁止再次委派（orchestrator 保留）  
`clarify` | 子 Agent 不能与用户交互  
`memory` | 不写入共享持久记忆  
`code_execution` | 子 Agent 应逐步推理  
`send_message` | 无跨平台副作用  
  
### 3.4 嵌套委派与配置【推荐，操作实用】

默认委派是扁平的：父 Agent（深度 0）→ 子 Agent（深度 1，不可再委派）。如需多阶段工作流，需要如下配置：

配置项 | 作用  
---|---  
`role` | `leaf` 是叶子节点，`orchestrator` 申请保留委派能力  
`max_spawn_depth` | 全局最大委派深度；`1` 表示只允许一层叶子 Agent  
`orchestrator_enabled` | 嵌套委派总开关  
      
    
    # ~/.hermes/config.yaml
    delegation:
      max_concurrent_children: 3 # 全局并发任务上限
      max_async children: 3      # 异步IO型任务单独上限
      max_spawn_depth: 1
      orchestrator_enabled: true
    

配置交互关系：

配置组合 | 结果  
---|---  
`role="leaf"`，任意 `max_spawn_depth` | 子 Agent 是叶子节点，不能继续委派  
`role="orchestrator"`，`max_spawn_depth: 1` | 仍不能继续委派  
`role="orchestrator"`，`max_spawn_depth: 2` | 可以再委派一层叶子 Agent  
`orchestrator_enabled: false` | 全局禁用嵌套委派  
  
## 4\. Kanban 多 Agent 协作

>   * 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/kanban>
>   * 架构 PDF：<https://github.com/NousResearch/hermes-agent/blob/main/docs/hermes-kanban-v1-spec.pdf>
> 


Hermes Kanban 是一个多 Agent 协作层：一个可恢复、可审计、可中途介入的工作队列。它把任务、依赖、评论、运行记录和工作目录放进一个持久任务板里，让多个具名 profile 以异步方式协作。

### 4.1 从 delegate_task 到 Kanban

`delegate_task` 适合短的、自包含的推理子任务，但无法覆盖：

  1. **研究分流与综合** ：多个专家型 Agent 并行产出候选发现，一个或多个审查者选择、合并
  2. **定时循环工作流** ：日报、周报、小时级收件箱分流等会跨运行积累知识
  3. **数字分身 / 持久助手** ：具名、长期存在的 Agent 身份在数周或数月里积累记忆
  4. **端到端工程流水线** ：拆解、并行实现、审查、迭代、提交



Kanban 的目标就是补上这些能力，提供：跨运行持久状态、工作可见性、不同技能 Agent 之间的交接、人类或对等 Agent 随时介入。

### 4.2 架构【重要，原理须知】

三层架构：

![hermes_kanban_architecture](https://img2024.cnblogs.com/blog/2729274/202607/2729274-20260721221244658-1638134660.png)

  * **Control Plane（控制层）** ：CLI、Gateway、Dashboard — 用户交互入口
  * **State Plane（状态层）** ：SQLite board + dispatcher — 唯一事实来源，决定哪些任务可运行
  * **Execution Plane（执行层）** ：独立 profile worker 进程，每个都有隔离状态



所有协调都通过任务板流转，profile 之间没有直接的进程间通信。

### 4.3 核心概念

#### Board（任务板）

Board 是一个独立的任务队列，拥有自己的 SQLite 数据库、workspaces 目录和调度循环。默认 board 数据库位于 `~/.hermes/kanban.db`。非默认 board 位于 `~/.hermes/kanban/boards/<slug>/`。

#### Task（任务）

Task 是 Kanban 的基本工作单元。一个 task 只有一个 `assignee`，通常是 Hermes profile 名称。

Task 状态：

状态 | 说明  
---|---  
`triage` | 待分流 / 待明确  
`todo` | 已创建但尚未满足运行条件  
`scheduled` | 已暂缓调度，等待恢复  
`ready` | 可以被 dispatcher 认领  
`running` | worker 正在执行  
`blocked` | 需要人工输入或等待外部条件  
`review` | 等待审查  
`done` | 已完成  
`archived` | 已归档  
  
**Task 生命周期状态流转** ：
    
    
                        ┌──────────────┐
                        │   triage     │  ← 粗略想法 / 高层目标
                        └──────┬───────┘
                               │ specify / decompose（自动或手动）
                               ▼
                        ┌──────────────┐
                   ┌────│    todo      │  ← 已创建，等待依赖满足
                   │    └──────┬───────┘
                   │           │ 所有父任务 done/archived
                   │           ▼
                   │    ┌──────────────┐
                   │    │   ready      │  ← 可以被 dispatcher 认领
                   │    └──────┬───────┘
                   │           │ dispatcher atomic claim
                   │           ▼
                   │    ┌──────────────┐
                   │    │   running    │  ← worker 进程中执行
                   │    └──┬───┬───┬───┘
                   │       │   │   │
                   │       │   │   └──────────┐
                   │       │   │              │
                   │       ▼   ▼              ▼
                   │  ┌────────┐ ┌────────┐ ┌──────────┐
                   │  │  done  │ │blocked │ │ crashed/ │ ← 自动恢复或超过重试上限
                   │  └────────┘ └───┬────┘ │ timed_out│    进入 blocked
                   │       ▲        │      └─────┬─────┘
                   │       │   unblock（人工/自动化） │
                   │       │        │      ┌────────┘
                   │       │        ▼      ▼
                   │       │   ┌──────────────┐
                   │       └───│   ready      │  ← 重新进入调度队列
                   │           └──────────────┘
                   │
                   ▼
            ┌──────────────┐
            │  archived    │  ← 归档（不再参与调度）
            └──────────────┘
    

关键点：

  * `triage` 是入口态，经过 decompose 拆解后变成 `todo` 子任务（原始 triage 变成 root task）
  * `todo` → `ready` 由 dispatcher 在每次 tick 中自动推进（检查依赖是否满足）
  * `ready` → `running` 通过 SQLite 原子 CAS 更新完成，保证并发安全
  * `running` 结束后进入 `done`（正常完成）或 `blocked`（需要人工介入）
  * `blocked` 经 `unblock` 后回到 `ready`，重新进入调度队列
  * 崩溃/超时任务由 dispatcher 的 stale recovery 自动回收



关键字段包括 `title`、`body`、`assignee`、`priority`、`workspace_kind`、`workspace_path`、`claim_lock`、`consecutive_failures`、`max_retries` 等。

#### Link（任务依赖）

Link 是 task 之间的父子依赖（`parent_id -> child_id`）。父任务完成之前，子任务保持在 `todo`；所有父任务完成（`done`/`archived`）后，dispatcher 推进子任务到 `ready`。支持 fan-out 和 fan-in。

#### Comment（评论 / 交接记录）

Comment 是人类和 Agent 在 task 上追加的持久消息，也是 Kanban 的跨 Agent 交接协议。Worker 启动时会读取完整评论串。人类可通过评论补充要求，Agent 可留下中间发现或交接说明。

#### Event（任务事件）

Event 是 Kanban 的审计日志，记录 task 生命周期里的状态变化、人工编辑和 worker 执行遥测。常见事件：

  * **生命周期** ：`created`、`promoted`、`claimed`、`completed`、`blocked`、`unblocked`、`archived`
  * **人工编辑** ：`assigned`、`edited`、`reprioritized`、`status`
  * **遥测** ：`spawned`、`heartbeat`、`reclaimed`、`crashed`、`timed_out`、`stale`、`gave_up`



#### Workspace（工作目录）

Task 绑定的工作目录，worker 执行时所在位置。

  * `scratch`：默认模式，为 task 创建新的临时工作目录
  * `dir:<path>`：使用已有绝对路径
  * `worktree`：为代码任务创建 git worktree



### 4.4 协作模式

Kanban 可衍生出 6 种可重用协作模式：

模式 | 说明 | 典型场景  
---|---|---  
**Fan-out（扇出）** | 一个目标拆成多个同级 task，并行执行 | 多角度研究、并行实现  
**Pipeline（流水线）** | 上游完成 → 下游启动，阶段式传递 | researcher → analyst → writer → reviewer  
**Fan-in（扇入）** | 多个 task 汇总到一个聚合 task | 研究综合、方案评审  
**Long-running journal** | 同一 profile 通过定时任务在共享 workspace 反复处理 | 日报、周报、监控巡检  
**Human-in-the-loop** | worker 阻塞 → 人工评论 → unblock → 重新启动 | 不确定决策、需要审批  
**Fleet farming** | 一个 profile 管理 N 个对象，每个对象独立 workspace | 多账号管理、多服务器巡检  
  
### 4.5 Dispatcher 调度器

Dispatcher 是一个长期循环，默认运行在 Gateway 内部。每 N 秒（默认 60 秒）扫描 board，执行四类动作：

  1. **stale recovery** ：处理异常的 `running` 任务（认领过期、进程退出、超时）
  2. **recompute ready** ：推进依赖满足的任务到 `ready`
  3. **atomic claim** ：通过"比较并交换"式 SQL 更新认领任务
  4. **启动 worker** ：认领成功后启动 assignee 对应的 profile worker



核心并发语义：
    
    
    UPDATE tasks
       SET status = 'running',
           claim_lock = ?,
           claim_expires = ?
     WHERE id = ?
       AND status = 'ready'
       AND claim_lock IS NULL;
    

更新命中 1 行 = 认领成功；命中 0 行 = 已被其他调度器认领。

失败与恢复：连续失败超过重试上限后，任务自动进入 `blocked`，等待人类介入。

### 4.6 案例展示

安装目录中config.yaml修改kanban的配置：
    
    
    delegation:
      max_concurrent_children: 3
      max_async_children: 3
      max_spawn_depth: 1
      orchestrator_enabled: true # 必须开启，多Agent看板调度依赖
    kanban:
      dispatch_interval_seconds: 10 # 自动扫描任务间隔
      dispatch_in_gateway: true
    

**命令行案例：**
    
    
    # 1. 初始化看板（如果还没创建）
    hermes kanban init
    # 启动网关+看板调度器（后台常驻，自动轮询任务）
    hermes gateway start --daemon
    hermes dispatcher start --daemon
    # 验证服务状态
    hermes gateway status
    hermes kanban status
    
    # 2. 创建一条演示任务
    hermes kanban create '阅读 Hermes Agent 文档并小结,永久保存到桌面' --body '重点看 agent loop、skills、gateway 三个部分' --assignee default
    
    # 3. 查看任务
    hermes kanban list
    
    # 4. 看某条任务的详情
    hermes kanban show <task_id>
    
    # 5. Worker 认领任务（会打印工作目录）
    hermes kanban claim <task_id>
    
    # 6. 再启动task
    hermes kanban unblock  <task_id>
    

**桌面版案例：** researcher、engineer分别是不同的profile角色
    
    
    帮我在看板创建任务，让researcher调研2026主流AI测试框架，engineer写demo代码
    

### 4.7 Orchestrator Profile【重要，操作实用】

Kanban 把编排分成两个阶段：

  1. **Decomposer 处理`triage` task**：判断目标是否需要拆分、创建子任务图、写入 assignee 和依赖关系
  2. **Orchestrator profile 承接 root task** ：子任务完成后，汇总结果，判断总目标是否完成



Orchestrator profile 的职责是协调，不是执行。推荐约束：

  1. **禁用执行型工具** ：只保留 `kanban`、`memory`，必要时加 `messaging`
  2. **加载`kanban-orchestrator` skill**：注入"你是编排者不是执行者"的行为约束
  3. **基于真实 profile 路由** ：根据本机 profile 的 description 路由任务



创建 orchestrator profile：
    
    
    hermes profile create orchestrator --clone \
      --description "Kanban 编排者。负责拆解高层目标、创建任务、指派真实存在的 profile、建立依赖关系、汇总下游结果；不直接执行研究、写作、编码或运维任务。"
    
    orchestrator tools disable terminal file web browser code_execution
    
    hermes config set kanban.orchestrator_profile orchestrator
    hermes config set kanban.auto_decompose true
    

### 4.8 Multi-Tenant Context

`tenant` 是 task 上的可选命名空间，让同一个 profile 服务多个业务上下文。
    
    
    hermes kanban create "monthly report" \
      --assignee researcher \
      --tenant business-a \
      --workspace dir:/home/user/tenants/business-a/data/
    

Tenant 主要影响 Workspace、记忆（命名约定）、Board 过滤和审计。Tenant 是软隔离，不是安全边界。

### 4.9 命令工具【重要，操作实用】

所有命令也支持 `/kanban` 斜杠形式在会话内使用。
    
    
    hermes kanban init                                   # 幂等创建 kanban.db
    hermes kanban create "research Hermes Agent" --assignee researcher
    hermes kanban list [--mine] [--assignee P] [--status S] [--tenant T]
    hermes kanban show <id>
    hermes kanban assign <id> <profile>
    hermes kanban link <parent_id> <child_id>
    hermes kanban comment <id> "<text>"
    hermes kanban complete <id> [--result "..."] [--summary "..."]
    hermes kanban block <id> "<reason>"
    hermes kanban unblock <id>
    hermes kanban archive <id>
    hermes kanban watch [--assignee P] [--kinds completed,blocked,...]
    hermes kanban tail <id>
    hermes kanban stats
    hermes kanban dispatch [--dry-run] [--max N]
    hermes kanban swarm <prompt>                         # v0.15+
    hermes kanban boards list
    hermes kanban boards create <slug> --name "Display Name"
    hermes kanban boards switch <slug>
    hermes kanban boards rm <slug>                       # 归档
    hermes kanban boards rm <slug> --delete              # 硬删除
    hermes kanban decompose <id>                         # 把 triage task 拆成子任务图
    hermes kanban specify <id>                           # 补全 triage task 成明确 spec
    hermes kanban gc                                     # 清理归档 task 的 scratch workspace
    

**案例：** 这条命令会在看板创建一个总任务，自动分出 3 个并行子任务worker分头调研 Hermes 三大模块，完成后verifier校验内容再synthesizer合并生成一份完整架构报告。（default意思是实用默认的profile角色）
    
    
    hermes kanban swarm "研究 Hermes Agent 的架构并写一份分析报告,输出到桌面" \
      --worker "default:Agent Loop 分析" \
      --worker "default:Skills 系统分析" \
      --worker "default:Gateway 架构分析" \
      --verifier default \
      --synthesizer default
    

**补充：**

命令 | 能力 | 协作模式  
---|---|---  
kanban create | 单任务，单 Agent 执行 | 串行，无自动拆分 / 校验 / 汇总  
kanban swarm | 集群多子任务，多 Agent 并行 | 自动拆分→并行执行→校验→汇总，一站式流水线  
  
## 5\. Mixture-of-Agents（MoA）

> 官方文档：<https://hermes-agent.nousresearch.com/docs/user-guide/features/mixture-of-agents>
> 
> Mixture-of-Agents（MoA）是 v0.18 升级为一等公民的核心能力——多个 LLM 同时处理同一个 prompt，各自独立推理，最后由一个聚合模型综合所有参考模型的输出，生成最终答案。简单来说就是「多个 AI 开会讨论，最后由主持人总结」。MoA 适用于需要高质量、多角度推理的复杂任务（如架构决策、深度分析、多方案对比等）。

### 5.1 基本原理【重要，原理须知】

用大白话说：**普通模式** 是 1 个 AI 回答你的问题；**MoA 模式** 是 3~5 个 AI 各自独立回答，最后由第 4 个 AI 综合所有人的回答给你最终答案。

就像公司开会：3 个专家各自发表意见，最后老板拍板总结。每个人只看到你的问题，看不到彼此的回答——避免了「随大流」。
    
    
    ┌─────────────────────────────────────────────────┐
    │                   你的问题                        │
    │  "设计一个高并发的用户认证系统，给出架构方案"      │
    └──────────┬──────────┬──────────┬────────────────┘
               │          │          │
               ▼          ▼          ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │  GPT-5   │ │ Claude   │ │  Grok    │
        │  独立推理 │ │ 独立推理 │ │ 独立推理 │
        └────┬─────┘ └────┬─────┘ └────┬─────┘
             │            │            │
             ▼            ▼            ▼
        ┌──────────────────────────────────────┐
        │     Gemini 2.5 Pro（聚合器）          │
        │     综合三个模型的分析 → 最终答案      │
        └──────────────────────────────────────┘
    

MoA 的工作流程：

  1. 用户发送 prompt
  2. Hermes 把 prompt 同时发给多个**参考模型** （Reference Models），例如 GPT-5、Claude Sonnet、Grok
  3. 每个参考模型独立推理，产生各自的完整回答
  4. 所有参考回答汇总到一个**聚合模型** （Aggregator），由它综合出最终答案
  5. 聚合器的答案流式传输给用户



参考模型之间互相独立，不会看到彼此的回答。聚合器能看到所有参考模型的输出，但不会看到原始 prompt 的完整上下文（减少 token 开销）。

### 5.2 MoA 预设配置【重要，操作实用】

>   1. 在 `config.yaml` 中添加一个 MoA 预设（参考 5.2 的配置示例）
> 
>   2. 用 `hermes moa list` 确认预设已加载
> 
>   3. 用 `/model <预设名> --provider moa` 切换到 MoA（参考 5.3），桌面版直接在切换模型的地方切换moa
> 
> （或者用 `/moa 你的问题` 一次性使用）
> 
>   4. 观察终端/桌面中每个参考模型的独立输出
> 
> 


MoA 预设在 `~/.hermes/config.yaml` 的 `moa` 部分定义。每个预设指定参考模型列表和聚合模型：
    
    
    # ~/.hermes/config.yaml
    moa:
      # ──────────────────────────────────────────────
      # MoA 总配置入口
      # ──────────────────────────────────────────────
    
      # 默认使用的预设名称。执行 /moa（不带名字）时，就用这个预设
      # 也可以用 /model deep --provider moa 来切换
      default_preset: deep
    
      # 全局开启推理追踪：每个参考模型的输入输出、聚合器的输入输出
      # 都会保存为 JSONL 文件到 ~/.hermes/sessions/，用于事后分析和评估
      # 设为 false 或不写 = 不保存（默认）
      save_traces: true
    
      # ──────────────────────────────────────────────
      # 预设列表：每个预设就是一个「开会方案」
      # ──────────────────────────────────────────────
      presets:
    
        # ====== 预设 1：deep（深度推理） ======
        deep:
    
          # 预设的描述文字，会显示在模型选择器里（桌面版、hermes model 都能看到）
          description: "三模型深度推理"
    
          # 参考模型列表：这些模型会同时收到你的问题，各自独立回答
          # 参考模型看不到系统提示词和工具调用记录，只看到你和AI的对话内容
          # 所以它们的调用成本比较低，且不受严格provider限制
          reference_models:
    
            # 第 1 个参考模型：通过 openai-codex provider 调用 GPT-5.5
            # provider：你要用哪个API服务（对应 .env 里配的 key）
            # model：该服务下的具体模型名
            - provider: openai-codex
              model: gpt-5.5
    
            # 第 2 个参考模型：通过 openrouter 调用 DeepSeek V4 Pro
            # openrouter 是一个聚合平台，可以访问多家厂商的模型
            - provider: openrouter
              model: deepseek/deepseek-v4-pro
    
          # 聚合器：等所有参考模型回答完毕后，由它来综合出最终答案
          # 聚合器能看到：系统提示词 + 完整对话 + 所有参考模型的输出 + 工具调用能力
          # 所以聚合器才是真正的「主模型」，负责写回复、调工具、做决策
          aggregator:
            provider: openrouter
            model: anthropic/claude-opus-4.8
    
          # 参考模型的最大输出 token 数（重要！直接影响速度）
          # 设置后参考模型只输出这么多 token，避免它们写长篇大论拖慢整体速度
          # 不设置（或设为0）= 不限制，参考模型可能输出几千 token，等得久
          # 建议值：300~600，聚合器只需要参考模型的「核心观点」就够了
          reference_max_tokens: 600
    
          # 是否启用此预设
          # 设为 false 后，虽然配置还在，但选择器里看不到它，也无法使用
          # 相当于「临时关闭」而不是「删除」
          enabled: true
    
          # 按预设单独开启推理追踪（覆盖全局 save_traces 设置）
          # 不写则继承全局设置
          save_traces: true
    
        # ====== 预设 2：quick（快速轻量） ======
        # 适用场景：简单问题、日常对话，不想等太久
        quick:
    
          description: "轻量双模型，适合简单任务"
    
          # 只用 2 个参考模型（比 deep 少 1 个），速度更快，成本更低
          reference_models:
            - provider: anthropic
              model: claude-sonnet-4     # Anthropic 的中等模型，性价比高
    
            - provider: openai
              model: gpt-4.1            # OpenAI 的中等模型
    
          # 聚合器：用最强的 Opus 来做最终综合
          # 即使参考模型用的是中等模型，聚合器用强模型也能保证输出质量
          aggregator:
            provider: openrouter
            model: anthropic/claude-opus-4.8
    
          # 比 deep 的 600 更严格，进一步压缩参考模型输出，加速
          reference_max_tokens: 300
    
          enabled: true
    

无注释的版本：
    
    
    moa:
      default_preset: deep
      save_traces: true
      presets:
        deep:
          description: "三模型深度推理"
          reference_models:
            - provider: openai-codex
              model: gpt-5.5
            - provider: openrouter
              model: deepseek/deepseek-v4-pro
          aggregator:
            provider: openrouter
            model: anthropic/claude-opus-4.8
          reference_max_tokens: 600
          enabled: true
          save_traces: true
        quick:
          description: "轻量双模型，适合简单任务"
          reference_models:
            - provider: anthropic
              model: claude-sonnet-4
            - provider: openai
              model: gpt-4.1
          aggregator:
            provider: openrouter
            model: anthropic/claude-opus-4.8
          reference_max_tokens: 300
          enabled: true
    

配置项说明：

配置项 | 说明  
---|---  
`default_preset` | 执行 `/moa`（不带名字）时用哪个预设  
`presets` | MoA 预设字典，每个 key 是预设名称（即虚拟模型名）  
`description` | 预设描述，展示在模型选择器中  
`reference_models` | 参考模型列表——同时收到你的问题，各自独立回答，**看不到系统提示词和工具调用** ，成本低  
`aggregator` | 聚合器——**真正的主模型** ，能看到完整上下文 + 所有参考输出，负责写回复、调工具  
`reference_max_tokens` | ⚠️ 最重要的一项：限制参考模型输出长度，直接决定速度。不设置=可能等久  
`save_traces` | 推理追踪开关。全局或按预设开启后，保存 JSONL 到 `~/.hermes/sessions/`，用于调试和评估  
`enabled` | 设 `false` = 临时关闭（选择器里看不到），不是删除  
  
参考模型数量不限，但数量越多 token 开销越大（每个参考模型都会消耗独立的上下文 token）。推荐 2~5 个模型。

### 5.3 选择 MoA 模型

> 前提：已经在 5.2 中配置好了 MoA 预设。没有配置的话，选择器里看不到 MoA 选项。

v0.18 将 MoA 从「模式切换」升级为「模型选择」——每个 MoA 预设（Preset）现在以虚拟模型的形式出现在所有模型选择器中，使用方式和选 Claude、GPT 完全一样：

**CLI / TUI 模型选择器：**
    
    
    hermes model                    # 交互式选择，moa/ 前缀的都是 MoA 预设
    hermes model moa/deep           # 直接指定 MoA 预设
    

**会话内切换：**
    
    
    /model deep --provider moa              # 切换到 MoA 预设
    /model --provider moa                   # 不写名字，用 default_preset 指定的默认预设
    

**桌面版：** 在状态栏模型选择器中，`MoA:` 开头的选项即为 MoA 预设，点击即可切换。

**单次调用（不切换默认模型，用完自动切回）：**
    
    
    /moa 我的问题                   # 用默认 MoA 预设跑一次，之后恢复原模型
    /moa                            # 不带问题 = 打印用法说明
    

### 5.4 推理过程展示

v0.18 的核心体验升级：MoA 运行时，每个参考模型的推理过程以**独立标签块** 展示，你可以看到每个模型各自的想法，最后再看聚合器的综合结论。

**实际效果示例——限流方案设计：**
    
    
    ┌─ Reference: GPT-5 ─────────────────────────────────┐
    │ 令牌桶方案：                                         │
    │ - 实现简单，内存占用固定                             │
    │ - 适合突发流量场景                                   │
    │ - 10 万 QPS 下，每秒补充 10 万个令牌...              │
    │                                                      │
    │ 滑动窗口方案：                                       │
    │ - 精确度更高，无临界突发问题                         │
    │ - 内存开销较大，需存储每个请求时间戳...               │
    └──────────────────────────────────────────────────────┘
    
    ┌─ Reference: Claude Sonnet ──────────────────────────┐
    │ 从工程实践角度：                                     │
    │ - 令牌桶在 Redis 中实现时，批量补充令牌有原子性问题  │
    │ - 滑动窗口用 Redis Sorted Set，10 万 QPS 下...      │
    │ - 建议：混合方案，粗粒度用令牌桶，细粒度用滑动窗口  │
    └──────────────────────────────────────────────────────┘
    
    ┌─ Reference: Grok ───────────────────────────────────┐
    │ 另一个被忽视的角度：                                  │
    │ - 分布式场景下的一致性问题                            │
    │ - 令牌桶的「预补充」在多节点时会导致超发             │
    │ - 建议引入中央令牌池或 Lua 脚本保证原子性...          │
    └──────────────────────────────────────────────────────┘
    
    ▶ Aggregator (Gemini 2.5 Pro) — streaming...
      综合三位模型的分析，以下是最终建议：
    
      1. **方案选择**：推荐混合架构（Claude 的建议）
         - 全局限流用令牌桶（简单、高效）
         - 精确限流用滑动窗口（准确）
    
      2. **实现要点**：
         - Redis + Lua 脚本保证原子性（Grok 的关键补充）
         - 每个节点本地缓存 + 定期同步（减少 Redis 压力）
    
      3. **性能预估**：
         - 令牌桶：单 Redis 实例可支撑 15 万 QPS
         - 滑动窗口：单实例约 8 万 QPS，需分片
    

聚合器的答案是**实时流式传输** 的——不再是长时间等待后一次性出现，而是像普通对话一样逐字输出。

**对比普通模式** ：如果只用 Claude Sonnet，你会得到一个「还不错」的答案。但 MoA 模式下，Grok 补充了分布式一致性这个你可能没想到的角度，Gemini 综合后给出了更全面的方案。

### 5.5 高级技巧

#### 技巧 1：用 `reference_max_tokens` 控制速度

参考模型的输出越长，聚合器等待时间越久。设置 `reference_max_tokens` 可以让参考模型给出简洁建议，大幅加快响应速度：
    
    
    moa:
      presets:
        fast:
          reference_max_tokens: 300    # 参考模型最多输出 300 token
          # 聚合器输出不受限制
    

#### 技巧 2：按场景选预设
    
    
    moa:
      presets:
        deep:           # 深度分析，用强模型
          reference_models:
            - provider: openai-codex
              model: gpt-5.5
            - provider: anthropic
              model: claude-opus-4.8
            - provider: openrouter
              model: deepseek/deepseek-v4-pro
          aggregator:
            provider: anthropic
            model: claude-opus-4.8
    
        quick:          # 快速任务，用轻量模型
          reference_models:
            - provider: anthropic
              model: claude-sonnet-4
            - provider: openai
              model: gpt-4.1
          aggregator:
            provider: openrouter
            model: anthropic/claude-opus-4.8
          reference_max_tokens: 300
    

使用时：
    
    
    /model deep --provider moa    # 复杂任务
    /model quick --provider moa   # 简单任务
    /moa 简单问题                  # 用默认预设
    

#### 技巧 3：一个参考模型失败不影响整体

如果某个参考模型 API 报错或超时，Hermes 会跳过它，用剩余的参考模型继续。不会因为一个模型挂了就整个任务失败。

#### 技巧 4：MoA 和普通模式随时切换
    
    
    /model deep --provider moa      # 切到 MoA
    # ... 使用 MoA 回答几个问题 ...
    /model claude-sonnet-4              # 切回普通模型
    

切换不会丢失对话历史，也不会破坏 prompt 缓存。

#### 技巧 5：用 `save_traces` 调试推理过程

开启 `save_traces` 后，每个参考模型的输入输出、聚合器的输入输出都会保存为 JSONL 文件，便于事后分析哪个模型贡献了什么观点：
    
    
    moa:
      save_traces: true        # 全局开启
      presets:
        deep:
          save_traces: true    # 也可按预设单独开启
    

追踪文件保存在 `~/.hermes/sessions/` 目录下，文件名包含会话 ID 和时间戳。

### 5.6 注意事项

  1. **MoA 比单模型慢** ：需要等所有参考模型输出完才能聚合。设置 `reference_max_tokens: 300~600` 可以显著加快速度。

  2. **MoA 比单模型贵** ：token 开销约是单模型的 4~6 倍。建议只在复杂任务时使用，简单问题用普通模型。

  3. **参考模型不需要来自不同 provider** ：可以用同一个 provider 的多个模型，也可以混合使用。

  4. **参考模型的视野有限** ：能看到当前对话历史（包括工具调用），但看不到系统提示词和工具 schema。这是设计如此，保证参考调用的轻量化。

  5. **参考模型可以使用工具** ：v0.18 起，参考模型在每次用户消息或工具返回时都会被触发，可以像主 agent 一样调用工具（搜索、读文件等）辅助推理，但工具调用结果不会传递给其他参考模型。

  6. **聚合器不能是另一个 MoA 预设** ：MoA 递归调用被显式禁止，防止无限嵌套。

  7. **一个参考模型失败不影响整体** ：如果某个参考模型 API 报错或超时，Hermes 会跳过它，用剩余的参考模型继续。

  8. **MoA 和普通模式可随时切换** ：用 `/model` 切换不会丢失对话历史，也不会破坏 prompt 缓存。

  9. **`save_traces` 会产生大量文件**：调试用的 JSONL 追踪文件会占用磁盘空间，生产环境建议关闭。




### 5.7 Delegation /Kanban /MoA 区别总结

  1. Delegation = "我拆活，临时工干"——轻量、临时、一次性，子 Agent 干完就销毁
  2. Kanban = "项目看板，多人协作"——重型、持久、可审计，任务有状态机，支持 block/unblock、评论、依赖链
  3. MoA = "多个 AI 开会讨论"——不是 Agent 协作，是模型协作，多个 LLM 独立推理后由聚合器综合，用于提升回答质量而非完成工程任务

维度 | 任务委派 (Delegation) | Kanban | MoA  
---|---|---|---  
一句话概括 | 父 Agent 拆子任务，子 Agent 干完汇报 | 多个 Profile Agent 通过看板异步协作 | 多个 LLM 同时回答同一问题，聚合器综合输出  
参与的是什么 | 子 Agent（同一进程内 spawn 的轻量实例） | 独立的 Profile Worker 进程（各有自己的 config/session/memory） | 多个 LLM 模型（不是 Agent，是纯模型推理）  
协调机制 | 父→子 直接委派，结果摘要回传 | SQLite 任务板 + Dispatcher 调度，状态机驱动 | 并行调用多个参考模型，聚合器综合  
任务持久性 | ❌ 无。父会话结束，子 Agent 全部丢失 | ✅ 有。Board 在 SQLite 中持久化，跨运行可恢复 | ❌ 无。就是一次推理调用  
人类可中途介入 | ❌ 不行（子 Agent 不能 clarify） | ✅ 可以。通过 comment 补充要求、block/unblock 任务 | ❌ 不行  
典型场景 | 短平快子任务：调试某段代码、调研某个问题、并行查 3 个方向 | 长期工程流水线：拆解→并行实现→审查→汇总；日报周报；多账号管理 | 需要多角度推理的复杂问题：架构决策、深度分析、多方案对比  
成本 | 中等（子 Agent 有独立上下文） | 高（每个 Worker 是独立 Profile，有完整系统提示词+工具） | 高（N 个参考模型 + 1 个聚合器，token 约 4~6 倍）  
速度 | 快（子 Agent 执行完立即返回） | 慢（依赖 Dispatcher 60s 一轮扫描 + Worker 异步执行） | 中等（要等所有参考模型输出完再聚合）  
配置复杂度 | 低，开箱即用 | 高（需配 kanban + orchestrator profile + dispatcher） | 中（配好 MoA 预设即可）  
类比 | 老板把任务分配给临时工 | 项目管理看板（Jira/Trello），多人协作 | 开评审会，3 个专家各发表意见，领导拍板总结


---
> 原文链接: https://www.cnblogs.com/buchizicai/p/21752482