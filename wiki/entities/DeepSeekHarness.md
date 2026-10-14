---
title: "DeepSeekHarness"
type: entity
tags: [实体, 评测框架, Agent, DeepSeek, Harness]
sources:
  - raw/09-archive/DeepSeek员工：Harness开始内测，有plugin、skill、MCP、Agent开源项目者优先，并赠送API额度（附Agent面试题）.md
  - raw/09-archive/2026-07-31-倒反天罡！DeepSeek V4-Flash 正式版悄然上线：130亿激活参数，把自家1.6万亿旗舰「以下克上」 - 小白跃升坊.md
  - raw/01-articles/DeepSeek Harness必装的10个插件.md
  - raw/01-articles/2026-08-15-DeepSeek Harness 教程：一切皆插件的开源 Agent 框架 - 掉落的果实.md
  - raw/01-articles/抖音视频内容整理_人类智力基线与2张显卡.md
  - raw/01-articles/2026-08-18 - DeepSeek Harness 命令大全.md
  - raw/01-articles/2026-08-21 - DeepSeekHarness必装的10个插件.md
  - raw/01-articles/2026-09-16-DeepSeek-V4.1-Flash 的最佳 Harness 搭档，我觉得可能是 Claude Code.md
  - raw/01-articles/2026-09-25-DeepSeek Harness客户端来了，AI办公又多了一个王者？.md
  - raw/01-articles/DeepSeek桌面版真不错，再见了WebUI。.md
  - raw/01-articles/2026-10-01-福利贴：WorkBuddy、豆包、智谱…9家AI大厂Token会员免费领.md
  - raw/01-articles/2026-10-04-Claude Code 最新版更新 Mods 能力，致敬 DeepSeek Harness？.md
  - raw/01-articles/2026-10-05-我一行代码没写，DeepSeek Harness 自己组队给我造了个错题本插件.md
  - raw/01-articles/2026-10-05-万字拆解 DeepSeek Harness 桌面版：产品设计、任务实测与能力边界.md
  - raw/01-articles/2026-10-12-DeepSeek Harness 插件生态解析 - 我才是银古.md
  - raw/01-articles/REA 保姆级教程：DeepSeek Harness 实操.md
last_updated: 2026-10-14
---

## 定义
DeepSeek Harness（DSH）是 DeepSeek 官方自研的原生 Agent 框架，对标阿里 Qoder、月之暗面 Kimi Code、智谱 Zcode 等同类产品。遵循 **Model + Harness = Agent** 设计理念，模型负责推理，Harness 负责模型之外的一切：工具调用、记忆管理、上下文控制、MCP 协议、Skills 体系等。

## 关键信息
- **2026-08-06 开始内测**：优先招募有 plugin、skill、MCP、Agent 开源项目经验的开发者，并赠送 API 额度
- **2026-08-13 正式开源**：MIT 协议，TypeScript 实现，基于 Cordis 插件内核（Koishi 同源技术，4 年 4000+ 社区插件验证）
- **GitHub 涨星记录**：发布 2 小时破万，12 小时超 5 万，42 小时约 10 万——**GitHub 史上涨星最快项目**
- **对 Codex 和 Claude Code 已做深度兼容**，但官方原生 Harness 对 API 入参出参有更优适配
- **泄露架构信息**：支持 Sub-agent、KV Cache 智能复用、跨会话记忆持久化等特性
- **团队背景**：DeepSeek Agent Harness 团队成立于 2026 年 3 月；负责人崔添翼（90 后浙大计算机出身，6 枚 ACM 亚洲区域赛金牌，曾任 Jane Street 量化机构九年）
- **评测角色**：V4-Flash 正式版公开基准测试中的 Code Agent 任务均使用该框架测试（Terminal Bench 2.1 达 82.7，DeepSWE 54.4 等），相关基准成绩为官方自测
- **不绑定 DeepSeek API**：认 OpenAI 兼容端点，可接入本地 llama-server / Ollama 等任意 OpenAI 兼容推理后端，详见 [[摘要-人类智力基线与2张显卡]]

## 知识冲突（已解决）
- 旧信息（2026-07-31）：定义 DeepSeek Harness 为"Agent 评测框架"——用于测试模型在代码 Agent 任务上的基准性能
- 新信息（2026-08-06）：DeepSeek Harness 是用户端 Agent 产品，评测是其中一项用途而非本质
- **处理结果**：2026-08-06 以新信息覆盖，将评测框架定位降级为次要用途

## 知识冲突（已解决，2026-08-18 核对官方文档）
- 旧信息 A（2026-08-15 教程）：四种运行模式为 TUI / Headless / Web UI / SDK
- 旧信息 B（2026-08-18 抖音视频）：四种运行模式为 标准模式 / PTC 模式 / 极简模式 / 创造模式
- **官方文档核对**（2026-08-18，https://github.com/deepseek-ai/deepseek-harness/blob/master/apps/cli/README.md）：
  - 官方 **Entry modes** 按 profile（配置文件）划分：`dsh --profile <name>`、`dsh --profile headless "job"`、`dsh web`（= `--profile web` 别名）、`dsh plugin --profile <name>`
  - 官方**没有**"TUI/Headless/Web UI/SDK"四分法，也**没有**"标准/PTC/极简/创造"四分法
- **处理结果**：两组分类均为第三方归纳，非官方术语
  - 教程的 TUI/Headless/Web UI 对应官方 profile 概念（web 和 headless 是官方明确 entry mode，TUI 是文档示例中提到的 `--profile tui`，SDK 指独立的 Python SDK 指南）
  - 抖音视频的标准/PTC/极简/创造更像是**工具集预设（preset）或 profile 配置**，描述的是工具集与行为，而非 entry mode
  - 两者是**不同维度的切面**：前者按交互形态，后者按工具集配置。已将两组并存并标注来源，以官方 Entry modes 为权威基准

## 官方 Entry modes（2026-08-18 核对，权威基准）
| 命令 | 用途 |
|------|------|
| `dsh --profile <name>` | 启动命名 profile（位于 `$DSH_HOME/profiles/<name>`） |
| `dsh --profile headless "job"` | 无界面运行一次性任务，打印最终答案后退出 |
| `dsh web` | `--profile web` 的别名，启动 Web UI（默认 `http://127.0.0.1:3080`） |
| `dsh plugin --profile <name> <pnpm args>` | 管理 profile 的插件（转发给 pnpm） |

- 调用目录是默认工作区根目录
- `web` 和 `headless` profile 首次使用时从内置模板自动初始化
- 其他 profile 必须通过 `dsh plugin` 创建
- Profile 目录包含 `package.json`（out-of-tree 插件依赖 + `dsh.profile` 清单）、`cordis.patch.yml`（用户补丁层）

## 第三方归纳：按交互形态（2026-08-15 教程，详见 [[摘要-deepseek-harness教程-掉落的果实]]）
1. **TUI 模式**：终端交互（默认），`dsh` 启动
2. **Headless 模式**：无界面自动化，`dsh --headless -p "任务"`，适合 CI/CD
3. **Web UI 模式**：`dsh --web`，浏览器访问，支持可视化调试
4. **SDK 模式**：作为库嵌入，`import { DSH } from '@deepseek/harness'`

## 第三方归纳：按工具集预设（2026-08-18 抖音视频，详见 [[摘要-人类智力基线与2张显卡]]）
| 预设 | 特点 | 适用场景 |
|------|------|----------|
| 标准模式 | 完整工具集：文件编辑、Shell、搜索、Skills、子 Agent、工作流 | 日常开发 |
| PTC 模式 | 模型写 TypeScript 代码一次性组合多步工具调用，大幅省 Token | 批量自动化 |
| 极简模式 | 仅保留 bash + 文件编辑器 | 模型基准测试 |
| 创造模式 | 标准模式 + 运行时检查 + 插件实验 + 自定义预设 | 插件开发、定制 Agent |

## 插件生态（2026-08-15）
- **设计理念**："一切皆插件"，工具/技能/MCP/记忆全部通过插件实现
- **插件协议**：定义 name/version/tools/skills/hooks，支持生命周期钩子（onSessionStart/onToolCall/onSessionEnd）
- **脚手架**：`dsh plugin create <name>` 快速创建插件模板
- **配置文件**：`dsh.config.json` 管理模型、插件、MCP、记忆
- **必装 10 插件**（详见 [[摘要-deepseek-harness必装10个插件]]）：[[ModLens]]、Code Review、Test Generator、Doc Generator、Refactor Helper、Security Scanner、Performance Profiler、Git Helper、API Tester、Visual Debugger

## 插件生态（2026-08-18，社区爆发）
- 上线 5 天，社区插件已超 **1400+** 个
- GitHub 搜索话题 `dsh-plugin`
- 代表插件：dsh-web-ui 全家桶（任务看板/Git 图谱/右侧面板/桌宠/Token 统计/皮肤中心）、[[ModLens]]（给纯文本模型补视觉）、dsh-genui（交互式 UI 渲染）、dsh-at-file（@ 引用文件）、dsh-tool-git（模型侧 Git）、dsh-browser-bridge（浏览器自动化）、dsh-memory-evolve（跨会话长期记忆+自我进化）、梁神模式（V4 Pro 调优预设，两阶段锚定 trick）

## 插件生态（2026-08-21，[[程序汪]] 盘点必装 10 插件，详见 [[摘要-deepseek-harness必装10个插件-程序汪]]）
- **生态数据（2026-08-15）**：Oh-My-DSH 目录收录精选插件 **1117** 个、监测生态仓库 **1521** 个、累计 Star **301295** 颗
- **安装命令**：`dsh plugin --profile web add "github:owner/repo#ref"`
- **重要坑**：启动 Web UI 必须加 `--patch` 参数，否则很多插件和技能不生效：`npx @deepseek-ai/dsh web --patch`
- **三层分类**：
  - 第一层（核心体验层）：dsh-web-ui、dsh-better-sidebar——界面从"毛坯"变"精装"
  - 第二层（交互方式层）：dsh-TUI（终端）、deepseek-harness-desktop（桌面 App）、dsh-at-file（@引用）
  - 第三层（能力扩展层）：ModLens（看图）、dsh-agent-teams（多 Agent）、dsh-plan-execute（双模型）、dsh-context-doctor（上下文审计）、dsh-reverse-skill（安全技能）

### 必装 10 插件清单（2026-08-21）
| 序号 | 插件名 | 仓库 | Star | 核心价值 |
|------|--------|------|------|----------|
| 1 | [[ModLens]] | liustack/modlens | 905+ | 给纯文本模型装"眼睛"，图片转结构化文本（锁版本 `@3.17.2`） |
| 2 | dsh-web-ui | zhu1090093659/dsh-web-ui | 1013+ | 全家桶：任务看板/Git 图谱/右侧面板/桌宠/Token 统计/皮肤中心 |
| 3 | dsh-better-sidebar | omdsh-dev/DSH-better-sidebar | 684+ | Codex 风格侧边栏工作台：文件树/终端/Git/子代理 |
| 4 | dsh-TUI | ccch1mneyyy/dsh-TUI | 793+ | 全屏终端界面，`dsh --profile cc-tui` |
| 5 | deepseek-harness-desktop | anywhere-labs/deepseek-harness-desktop | 4745+ | Electron 桌面应用，无需 Node.js，双击即跑 |
| 6 | dsh-at-file | omdsh-dev/dsh-at-file | - | `@` 引用文件，对标 Codex |
| 7 | dsh-agent-teams | NanmiCoder/dsh-agent-teams | - | 多智能体团队协作，邮箱直达+唤醒无队长中转 |
| 8 | dsh-plan-execute | dsh-external/dsh-plan-execute | - | 双模型路由：规划用推理模型，执行用经济模型 |
| 9 | dsh-context-doctor | Zhenyu98/dsh-context-doctor | - | 量化上下文 Token 账单，检测重复冲突，只读 |
| 10 | dsh-reverse-skill | dhicoc/dsh-reverse-skill | - | 85 个安全研究 SKILL.md（逆向/渗透/安全研究） |

## 本地部署接入（2026-08-18）
- DSH 认 OpenAI 兼容端点，不绑定 DeepSeek API
- 接入本地 [[LlamaCpp]] / [[Ollama]]：Settings → Models → 添加自定义模型 → 填本地地址（如 `http://127.0.0.1:8080/v1`）→ API 协议选 `openai-completions` → 保存即时生效
- 配合 [[Qwen3.8-27B]] + 2× [[RTX5090]] 构成完全本地 Agent 工作站，详见 [[本地Agent工作站]]
- 注意：DSH 仍是开发者预览版，会有破坏性变更，不适合直接上生产；Agent 有读写文件/执行 shell 权限，工作区选空测试文件夹

## 命令速查（2026-08-18，详见 [[摘要-deepseek-harness命令大全]]）
| 命令 | 作用 |
|------|------|
| `npx -y @deepseek-ai/dsh web` | 一键启动 Web UI（尝鲜） |
| `dsh web` | 启动 Web UI（全局安装后） |
| `dsh --profile <name>` | 启动指定 profile |
| `dsh --profile headless "任务"` | 一次性任务，跑完退出（适合 CI/CD） |
| `dsh plugin --profile <name> <pnpm args>` | 管理 profile 插件 |
| `dsh --help` | 启动器帮助 |
| `dsh --profile <name> --help` | 该应用参数帮助 |
| `dsh --dump-default-config` | 打印内置默认配置 |
| `dsh --dump-config` | 打印叠加后最终配置 |
| `dsh --patch <file> --profile <name>` | 一次性覆盖层启动 |

- **参数顺序铁律**：启动器参数在前，应用参数在后；从第一个无法识别的 token 起全部归属应用参数
- **前置条件**：Node.js ≥ 22
- **版本**：0.1.0-rc.6（开发者预览版，生产谨慎）
- **Python SDK**：`pip install deepseek-harness` / `deepseek-harness-cli`；MCP 服务器 `npx -y @deepseek-harness/mcp`

## V4.1-Flash 在 DSH 不同模式下的表现（2026-09-17，详见 [[摘要-deepseek-v4-1-flash-harness横评]]）
[[老章]] 用 [[SimonWillison|Simon Willison]] 的 Space Invaders 原题横评 [[DeepSeek-V4.1-Flash]] 在四种 Harness 下的表现，DSH 标准模式与极简模式对比：

| DSH 模式 | 用时 | Token | TPS | 结果 | 综合分 |
|----------|------|-------|-----|------|--------|
| 标准模式 | 8分54秒 | 4.2M tok | 275 tok/s | 完成 | 8.7（最稳最规整） |
| 极简模式 | 40分04秒 | 1.5M tok | 295 tok/s | **失败** | 7.2（刷新后卡死） |

**反常识发现**：DSH Minimal 在两项官方测试中都高于 Standard 和 PTC——功能更多更复杂并没有换来更高成功率。极简模式虽省 84.5% Token，但缺乏全局视野，总用时全场最慢且最终失败。

**整体排名**：① Claude Code 9.2 分 ② Pi Agent 8.9 分 ③ DSH 标准 8.7 分 ④ DSH 极简 7.2 分。[[ClaudeCode]] 接 DeepSeek-V4.1-Flash 开箱即用接近峰值。

## 官方桌面客户端（2026-09-25，nightly，详见 [[摘要-deepseek-harness桌面客户端]]）
[[欧阳俊杰]] 实测社区流传的 DeepSeek 官方桌面客户端（作者称之为"DeepSeek 的 AI 办公版"）：
- **平台与分发**：Windows / macOS（暂无 Linux），走 **nightly 通道**；macOS 版带 DeepSeek 公司主体开发者签名并通过 Apple 公证，官方尚未正式官宣
- **工作区模式**：启动第一步即选择本地文件夹作为工作区，读写本地文件、联网搜索、终端操作、多智能体协作全部围绕工作区进行——从"聊天框"进入本地工作目录
- **登录方式**：DeepSeek 账号（**账号模式**）或 API Key（**API 模式**），二者与登录方式不匹配会出现"能输入任务但不干活"
- **初始化配置**：询问用途（办公与创作 / 代码与开发）与过程可见度（只看结果 / 关键步骤 / 全部过程），把"AI 干活给用户看多少"交给用户选择
- **四种模式**：标准、PTC、极简、创造——与上文"第三方归纳：按工具集预设"一致，桌面客户端将其作为可选模式呈现（官方 Entry modes 仍以 profile 为权威基准）
- **内置插件**：智能体团队（多 Agent 分工协作 + 角色配置）、语音输入、终端、Agent Loop、Subagent、网页搜索，继续贯彻 **Everything is a Plugin**
- **产品意义**：与社区插件 `deepseek-harness-desktop`（anywhere-labs 的 Electron 壳）不同，这是 DeepSeek 自家官方客户端，标志 DeepSeek 从"模型、网页、App、API"扩展到 AI 办公赛道，与 [[WorkBuddy]]、[[豆包工作]]、千问办公正面相撞

## 桌面版源码解析（2026-09-28，[[沉默王二]]，详见 [[摘要-dsh桌面版-electron源码解析]]）
- **架构**：Electron 打包未重写界面——主窗口加载完整 WebUI，子进程跑 `dsh web` 同一套本地服务（端口 3080→19387），自动升级到 v0.1.7-rc.2（nightly 通道、10 分钟检查、需手动确认下载）
- **登录**：OAuth PKCE，令牌存 `~/.dsh/credentials.yaml`（0600 权限）
- **profile 隔离**：WebUI 用 `~/.dsh/profiles/web`，桌面版用 `~/.dsh/profiles/desktop`——会话/设置/凭证共享但**插件不共享**，desktop profile 只归 Electron 应用管
- **插件无沙箱**：服务端插件与宿主共用同一 Electron Node 进程，页面同页运行无 iframe 隔离（SAFETY.md 警告勿装来路不明插件），详见 [[everything-is-a-plugin]]
- **记忆现状**：无官方长期记忆工具，靠 `~/.dsh/AGENTS.md` + 项目 AGENTS.md/CLAUDE.md（首请求注入，预算 65536 字节）；`session_search` 源码存在但内置预设未启用
- **推荐三件套**：DSH-better-sidebar（侧边栏+上下文自动注入的 Side Chat）、dsh-TUI（Sixel/Kitty 图片预览、时间回溯）、deepseek-harness-plugin.com 插件库

## 与 Claude Code Mods 的架构对照（2026-10-04，详见 [[摘要-claude-code-mods机制]]）
Claude Code 推出 [[Mods]] 被媒体拿来对比 DSH 的"一切皆插件"，两者演化方向一致但实现独立、**无协议兼容或继承关系**：
- **共同特征**：把定制单元从外部提示词/工具挂载推进到 Agent 运行时内部，内置与扩展共享同一套底层机制；调用链引入类似中间件的流水线（前一个扩展处理完调用 next 交控制权，或提前返回接管）；生命周期与状态管理成为干预接缝
- **核心差异**：DSH 启动时按配置与 Profile 组装整棵 Cordis 插件树，由依赖注入驱动服务挂载，AgentLoop/模型适配/工具注册均以服务契约提供、可换 Provider，插件间靠注册服务与 Typed 事件 + 生命周期 Effects 协同，**服务契约级组件插拔**；Claude Code Mods 随插件包安装、会话启动时进入中间件事件链，宿主引擎保持完整运行、官方逐步把内置能力迁成 Mod，用户可干预单轮模型路由与工具执行，**会话流水线级事件拦截与改写**
- **边界**：基于 Cordis Context 的服务提供者无法直接塞进 Claude Code，Mods 的 register 与事件钩子也无法在 dsh 中运行——审计逻辑可互相参考，代码必须针对各自宿主单独编写

## 6 元体验赠金活动（2026-10-01，详见 [[摘要-9家ai大厂token福利]]）
- 符合条件用户登录即得 **6 元体验赠金**，按官方典型 Agent 用量估算约覆盖 1.2 亿缓存命中输入 Token、148 万缓存未命中输入 Token、52 万输出 Token
- 名额有限先到先得，**到账后 7 天有效**；覆盖范围为活动开始前已注册的 DeepSeek 用户，以及活动开始后用 +86 中国大陆手机号注册的新用户；活动前登录过的可退出重登再查

## 错题本插件实战：零代码组队开发（2026-10-05，详见 [[摘要-deepseek-harness-错题本插件]]）
桌面版 v0.2 预览版（macOS/Windows，可自定义模型，作者全程用 [[Kimi]] K3）实测"创造模式"造"错题本工作台"插件：
- **三步提示词工作法**：需求梳理（只写 AI 猜不到的核心差异/用户/场景/硬约束 + "有不确定的地方先问我"）→ 20 分钟可点击 HTML 原型 → 开发（"你作为技术负责人合理安排团队分工"）
- **需求反问价值**：先摸 Harness 插件体系能提供什么，弹 6 个问题，抓出作者"数据只存本地"与"调云端模型推理"自相矛盾；作者反挑 3 个问题（手机扫码直传、整页拍照泄露姓名学校、已掌握状态可手动改）5 分钟改完
- **自组开发团队**：T0 验证安装与接口通路 → T1 把接口契约写成文档冻结 → 后端 subagent A + 前端 subagent B 并行 → 联调主链路；首装翻车（API 请求失败）查日志加埋点 7 分钟修复；作者中途回答问题打断执行，靠"进行中的目标"自动续上、上下文不丢
- **关键架构发现**：动态方式定义的插件重启就没，必须打包成本地插件装进软件；插件一个模型没配（识图/讲解/出题用宿主统一接好的模型），**功能归插件、模型归宿主**是"一切皆插件"的直接好处；"智能体团队/子智能体"本身也是官方插件——帮它造插件的和被造出来的是同一种东西

## 桌面版万字拆解：定制三层与能力边界（2026-10-05，详见 [[摘要-deepseek-harness-桌面版万字拆解]]）
AI 产品经理视角的实测拆解：
- **入口设计**：四种任务模式（标准/PTC/极简/创造）+ 独立访问模式（只读/工作区内修改/完全权限）；标准 vs PTC 同题对照（DeepSeek-V41-Flash、High 推理）差异在执行路径——PTC 用代码调工具+本机浏览器完成页面检查，标准模式直接启 Chrome 无头浏览器遇权限错误失败；两份报告犯同一处分类错误，执行模式不同判断不会自动变准
- **定制三层**：工作方法（流程文档）/ 工具与界面（Skill+工具封装）/ 运行组件（模型适配、工具注册、会话日志、Agent 循环皆插件化可替换）；不同需求停在不同层次，不必全改
- **生效状态坑**：配置可热更新，但已安装插件改代码要重启进程；"界面显示启用但运行时仍是旧版工具说明"让用户困惑，作者建议应用优先把"当前加载版本/待生效改动/下一步操作"放同一位置
- **核验通过≠任务正确**：核验工具限制了目录却把具体输入文件选择留给调用方，Agent 悄悄把第二批材料也纳入核验、工具照样返回通过——修法是任务开始时按指定文件固定本轮**输入清单**（单独任务配置，报告生成步骤不得改动）
- **流程文档 vs 插件**：判断规则还在变时放可读文档，稳定可确定的检查封装成工具；规则保存前要用"能触发冲突的样例"检验（版本号 vs 开发启动命令的形态判断冲突第一版就出现过）
- **三种变化要分清**：材料增加（重新检查判断）、规则修订（更新工作方法）、新批次（重新划定输入输出范围）——不能都理解成"继续上一段聊天"
- **竞品定制对比**：Harness 把运行部件纳入插件组合（按运行配置管理，一次改多会话生效）；[[Mods]] 按会话试用（热重载、默认仅创建它的会话，跨会话需保留加载或市场分发）；[[Codex]] plugins 按项目控制启停（重启应用生效、Hooks 需用户审阅信任）
- **插件生态的游戏化样本（2026-10-08，详见 [[摘要-dsh-合成大鲸鱼插件]]）**：侧边栏"合成大鲸鱼"小游戏插件（合成大西瓜玩法、11 级海洋生物、33 张 AI 知识卡片、图鉴/成就/相册收集），一行配置 `github:lqshow/dsh-whale-merge` 安装、代码开源数据本地存；关键设计是**交作业奖励**——AI 干完活催用户回看成果、看完才给珍珠（救局面道具），把游戏动机从摸鱼反转为提醒回看 AI 成果

## 插件生态全量数据（2026-10-12，详见 [[摘要-dsh插件生态解析]]）
- **规模与活跃度**：清单收录 4,349 个仓库 / 4,508 条插件条目（476 条指向 monorepo 子包）/ 23 个类目；**57%（2,478/4,327）近 30 天有提交**，头部 100 个原生插件里 96 个活跃——不是"发完就死"的坟场
- **star 极度头部化**：中位数 2⭐、P90 20⭐、P99 687⭐，全站 373,850 star 中 **Top 25 占 79.8%**，903 个仓库一个 star 都没有
- **类目冷热**：Memory（209 条 / 100,218⭐）+ Docs & Rendering（68 条 / 83,320⭐）合计占全站 49%；WSL 互操作 77 条仅 160⭐、语音 65 条仅 401⭐——平台缝隙天花板极低
- **原生 vs 上游集成**：原生插件仓库 4,009 个，上游集成子包 313 个。star 第一是原生 monorepo `dsh-web`（8,650⭐），单包形态第一是 `dsh-routing-suite`（7,019⭐）。archify、hindsight、OpenViking、WeKnora、BrowserSkill、loopx、ouroboros、mirage、ReMe、memsearch 均为"上游借船"——主流 agent 工具链已把给 dsh 出包当作标配分发渠道
- **插件身份机制**：唯一硬门槛是 `package.json` 中 `"dsh": { "bundle": { "patch": "./cordis.patch.yml" } }`，装配是 Cordis 声明式补丁描述而非 `require()`；peer 依赖写在非标准 `peer` 字段
- **⚠️ semver 预发布陷阱**：不带显式预发布分支的 peer 范围会静默排除所有预发布构建——`>=0.0.0-0 <0.2.0-0` 也匹配不到 `0.1.0-rc.6`，用户装时撞 ERESOLVE 却看不出原因
- **四个趋势**：右侧边栏成为扩展总线（占据侧边栏者成为二级平台）；插件互相依赖（better-sidebar 依赖 better-locale）；手机远程审批成刚需（dsh-pocket / dsh-reach 等一整条产品线）；娱乐化程度惊人（137 个 Just for Fun）
- **安全提醒**：装插件 = 以本人权限跑第三方代码，且**工具审批不会沙箱化插件代码**；"被收录"≠"被审计"（准入门槛只有能装、描述相符、类目正确、有人维护）；头部插件 `dsh-infinite-gen-4`（2,671⭐）以最高优先级往系统提示追加"无条件服从"段落

## 关联连接
- [[DeepSeek]] — 所属公司
- [[崔添翼]] — 团队负责人
- [[Harness]] — 通用概念（Model + Harness = Agent）
- [[摘要-deepseek-harness内测]] — 来源
- [[摘要-deepseek-v4-flash发布]] — 来源
- [[摘要-deepseek-harness必装10个插件]] — 来源（插件推荐）
- [[摘要-deepseek-harness必装10个插件-程序汪]] — 来源（2026-08-21 程序汪盘点 10 插件）
- [[程序汪]] — 10 插件盘点文章作者
- [[摘要-deepseek-harness教程-掉落的果实]] — 来源（完整教程）
- [[ModLens]] — 推荐插件
- [[掉落的果实]] — 教程作者
- [[小哈]] — 插件推荐作者
- [[PaiCLI]] — 同类开源 Agent 项目
- [[ClaudeCode]] — 已兼容的第三方 Agent 框架
- [[Codex]] — 已兼容的第三方 Agent 框架
- [[摘要-人类智力基线与2张显卡]] — 来源（开源发布 + 本地部署接入）
- [[Qwen3.8-27B]] — 本地部署配套模型
- [[RTX5090]] — 配套硬件
- [[LlamaCpp]] — 本地推理引擎
- [[本地Agent工作站]] — 完整本地方案
- [[TensorSplit]] — 多卡分摊技术
- [[GGUF量化]] — 模型量化技术
- [[摘要-deepseek-v4-1-flash-harness横评]] — 来源（V4.1-Flash Harness 横评）
- [[摘要-deepseek-harness桌面客户端]] — 来源（官方桌面客户端实测）
- [[摘要-dsh桌面版-electron源码解析]] — 来源（桌面版 Electron 源码解析）
- [[沉默王二]] — 源码解析作者
- [[Cordis]] — 插件框架底座
- [[everything-is-a-plugin]] — 桌面版源码解析提炼的概念
- [[Electron]] — 桌面版打包框架
- [[欧阳俊杰]] — 桌面客户端实测作者
- [[办公Agent]] — 桌面客户端进入的赛道
- [[桌面Agent]] — 产品形态上位概念
- [[DeepSeek-V4.1-Flash]] — 被测模型
- [[老章]] — 横评作者
- [[ClaudeCode]] — 综合排名第一的 Harness
- [[摘要-9家ai大厂token福利]] — 来源（6 元体验赠金活动）
- [[摘要-claude-code-mods机制]] — 来源（与 Claude Code Mods 的架构对照）
- [[Mods]] — Claude Code 侧的对照机制
- [[摘要-deepseek-harness-错题本插件]] — 来源（错题本插件零代码组队实战）
- [[摘要-deepseek-harness-桌面版万字拆解]] — 来源（定制三层、生效状态与能力边界）
- [[Kimi]] — 错题本实战全程使用的宿主模型
- [[摘要-dsh-合成大鲸鱼插件]] — 来源（合成大鲸鱼侧边栏小游戏插件与交作业奖励设计）
- [[摘要-dsh插件生态解析]] — 来源（插件生态全量数据与趋势）
- [[插件生态]] — 生态分析框架