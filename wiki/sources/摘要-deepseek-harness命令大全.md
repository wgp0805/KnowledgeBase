---
title: "摘要-deepseek-harness命令大全"
type: source
tags: [来源, DeepSeek, Harness, dsh, CLI, 命令速查]
sources: [raw/01-articles/2026-08-18 - DeepSeek Harness 命令大全.md]
last_updated: 2026-08-18
---

## 核心摘要
[[苏三]] 整理的 [[DeepSeekHarness]] 命令行入口 `dsh` 的完整速查手册。`dsh` 的核心作用是**启动 profile**——profile 由多个插件组合包按顺序叠加而成的运行配置。内置 `web`（Web UI）和 `headless`（一次性任务模式）两个 profile，首次使用从模板自动初始化。文章系统梳理了启动方式（npx/全局安装/源码）、Profile 启动、headless 任务、插件管理（`dsh plugin` 转发 pnpm）、配置查看（`--dump-config`/`--dump-default-config`）、临时覆盖（`--patch`）、Python SDK，并强调最易踩坑的规则：**启动器参数在前，应用参数在后**——从第一个无法识别的 token 起，后续全部归属应用参数。

## 关键信息

### dsh 本质
- `dsh` = DeepSeek Harness 命令行入口
- 核心作用：启动 profile（插件组合包按顺序叠加的运行配置）
- 内置 profile：`web`（Web UI）、`headless`（一次性任务，跑完退出）
- 其他 profile 需 `dsh plugin` 创建

### 启动方式
| 方式 | 命令 | 适用 |
|------|------|------|
| npx 一键 | `npx -y @deepseek-ai/dsh web` | 尝鲜，需 Node.js ≥ 22 |
| 全局安装 | `npm install -g @deepseek-ai/dsh` → `dsh web` | 日常使用 |
| 源码运行 | `git clone` → `pnpm install` → `pnpm run build` → `pnpm dsh web` | 二次开发 |

- 默认地址：`http://127.0.0.1:3080`

### Profile 启动
- `dsh web` = `dsh --profile web`（别名）
- `dsh --profile headless "任务描述"` — 一次性任务
- `dsh --profile my-agent` — 自定义 profile（需先创建）
- profile 位于 `$DSH_HOME/profiles/<名称>`

### headless 模式
- 适合脚本化、CI/CD、批处理
- 退出码：0 = 正常完成；非零 = 配置错误/启动失败/任务失败

### 插件管理
- `dsh plugin --profile <名称> <pnpm 参数>` — 转发 pnpm 到 profile 目录
- 安装：`dsh plugin --profile web add dsh-some-plugin`
- 移除：`dsh plugin --profile web remove dsh-compat`
- 变更后需重启 Harness 生效

### 配置查看与覆盖
- `dsh --dump-default-config` — 内置默认配置（未叠加 patch）
- `dsh --dump-config` — 叠加所有层后的最终配置
- `dsh --patch <文件路径> --profile web` — 一次性覆盖层启动（不改文件，替换整行 config 值，非深度合并）

### 帮助
- `dsh --help` — 启动器自己的帮助
- `dsh --profile web --help` — web 应用自己的参数帮助
- 关键区别：裸 `--help` 是启动器；加 `--profile` 是该应用参数

### ⚠️ 参数顺序规则（最易踩坑）
- **启动器只解析自己的 flag，从第一个无法识别的 token 开始，后面全部属于应用参数**
- ✅ `dsh --profile web --port 8080`（启动器在前，应用在后）
- ❌ `dsh --port 8080 --profile web`（启动器看不到 `--profile`）
- 口诀：启动器参数在最前，应用参数在最后

### Python SDK
- `pip install deepseek-harness`（库）
- `pip install deepseek-harness-cli`（CLI 工具）
- MCP 服务器：`npx -y @deepseek-harness/mcp`（stdio transport）

### 优缺点
- **优点**：命令简洁上手快（常用 ≤5 条）、双模式覆盖全场景、插件管理标准化（pnpm）、配置可审计、参数规则清晰
- **缺点**：参数顺序严格限制、仍为开发者预览版（0.1.0-rc.6，生产谨慎）、非内置 profile 需手动创建、依赖 Node.js ≥ 22

## 与现有知识的印证
本文与 [[DeepSeekHarness]] 实体中"官方 Entry modes（2026-08-18 核对）"完全一致，进一步印证了官方 profile 划分（`dsh --profile <name>` / `dsh --profile headless "job"` / `dsh web` / `dsh plugin`）为权威基准，而"TUI/Headless/Web UI/SDK"和"标准/PTC/极简/创造"均为第三方归纳。

## 关联连接
- [[DeepSeekHarness]] — 核心实体
- [[DeepSeek]] — 所属公司
- [[Harness]] — 通用概念
- [[苏三]] — 文章作者
- [[摘要-deepseek-harness教程-掉落的果实]] — 相关教程
- [[摘要-deepseek-harness必装10个插件]] — 插件推荐
- [[摘要-人类智力基线与2张显卡]] — 开源发布与本地部署
