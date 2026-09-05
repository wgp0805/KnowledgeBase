---
source_url: "https://mp.weixin.qq.com/s/ORYQrnwOC5IIiCtXLnNHzA"
title: "DeepSeek Harness 命令大全"
account: "苏三说技术"
published_at: "2026-08-18T01:00:00.000Z"
saved_at: "2026-08-18T05:52:29.046Z"
sync_id: "art_385c2db96bd14c4c8ffd91a094082b71"
parse_status: "ok"
---

# DeepSeek Harness 命令大全

**大家好，我是苏三，又跟大家见面了。**

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐13个牛逼的SpringBoot项目](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535420&idx=1&sn=037a80b21a6207a9aafcb7aaa0fd68b1&scene=21#wechat_redirect)

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

DeepSeek Harness 开源之后，很多小伙伴第一时间就装上了。

装完之后发现一个问题—— **命令好多，记不住**。

 `dsh web`  能跑起来，但  `--profile headless`  是干嘛的？

 `--patch`  什么时候用？

 `--dump-config`  和  `--dump-default-config`  有什么区别？

插件怎么装？

参数顺序有什么讲究？

这些问题我一开始也懵。

翻了一晚上官方文档和社区资料，才把整个命令体系摸清楚。

今天这篇文章，我就把 dsh 的所有命令从头到尾整理一遍，形成一份完整的速查手册。

希望对你会有所帮助。

## 一、dsh 到底是什么？

在聊具体命令之前，我们先花 2 分钟搞清楚一件事：**dsh 到底是什么？**

 `dsh`  是 **DeepSeek Harness 的命令行入口**。

它的核心作用是**启动 profile**——所谓 profile，就是由多个插件组合包按顺序叠加而成的运行配置。

简单说：**你告诉 dsh 用哪个 profile，dsh 就把对应的插件组合加载起来，跑成一个 Agent 实例**。

内置了两个 profile：

- **  `web`  **：启动 Web UI
- **  `headless`  **：一次性任务模式，跑完打印结果就退出

这两个 profile 首次使用时都会从随附模板自动初始化。

其他 profile 需要通过  `dsh plugin`  命令自行创建。

## 二、启动命令

### 2.1 方式一：npx 一键启动（尝鲜首选）

这是最快的方式，适合首次体验、不想装全局包：

```
npx -y @deepseek-ai/dsh web
```

执行后浏览器会自动打开本地界面，默认地址  `http://127.0.0.1:3080` 。首次使用会自动初始化配置目录。

**前置条件**：需要 Node.js ≥ 22。

### 2.2 方式二：全局安装（日常使用）

如果你打算长期使用，建议全局安装：

```
npm install -g @deepseek-ai/dsh
dsh web
```

装好后，后续直接输入  `dsh web`  即可启动，不用每次都敲  `npx` 。

> **npx 和 dsh 的区别**： `npx @deepseek-ai/dsh`  是首次安装/临时调用；装好后可以直接用  `dsh`  命令。两者后续参数完全一致。

### 2.3 方式三：从源码运行（适合二次开发）

如果你想修改源码或开发插件：

```
git clone https://github.com/deepseek-ai/deepseek-harness.git
cd deepseek-harness
pnpm install
pnpm run build
pnpm dsh web
```

构建完成后用  `pnpm dsh`  代替  `dsh`  命令即可，参数用法完全一致。

## 三、Profile 启动命令

这是 dsh 最核心的命令模式：

```
dsh --profile <名称>
```

启动位于  `$DSH_HOME/profiles/<名称>`  的指定 profile。

**内置 profile**：

```
# 启动 Web UI（最常用）
dsh web                    # --profile web 的别名

# 启动 Web UI（完整写法）
dsh --profile web

# 一次性任务模式
dsh --profile headless "任务描述"
```

**自定义 profile**：

```
# 启动名为 my-agent 的自定义 profile
dsh --profile my-agent
```

> **注意**： `web`  和  `headless`  以外的 profile 必须通过  `dsh plugin`  命令先创建才能使用。

## 四、一次性任务命令（headless 模式）

不想开界面，直接跑一个任务拿结果——这是 headless 模式的核心价值：

```
dsh --profile headless "你的任务描述"
```

**实际示例**：

```
# 让 Agent 总结当前仓库
dsh --profile headless "Summarize this repository and identify its main packages."

# 跑测试并汇总结果
dsh --profile headless "把当前目录的测试跑一遍并汇总结果"

# 验证 CLI 链路是否正常
dsh --profile headless "Say hello in one line."
```

运行后会打印 Agent 的最终回答并退出，**适合脚本化、CI/CD 流水线、批处理场景**。

**退出码的含义**：

- 0 ：headless 任务正常完成（最终轮次结束）
- 非零 ：配置错误、启动失败或任务失败

写脚本时可以直接用退出码判断成败。

## 五、插件管理命令

Harness 的口号是“一切皆插件”，插件管理自然也是高频操作：

```
dsh plugin --profile <名称> <pnpm 参数>
```

这个命令把 pnpm 操作转发到指定 profile 目录，用来给 profile 安装、移除插件。

**安装插件**：

```
# 给 web profile 安装社区插件
dsh plugin --profile web add dsh-some-plugin

# 安装特定版本的插件
dsh plugin --profile web add @rvaim/dsh-compat@latest

# 给 tui profile 安装终端插件
dsh plugin --profile tui add @wxgmjfhy/dsh-tui

# 给 headless profile 安装插件
dsh plugin --profile headless add @useorgx/deepseek-harness-plugin@0.1.0
```

**移除插件**：

```
dsh plugin --profile web remove dsh-compat
dsh plugin --profile tui remove @wxgmjfhy/dsh-tui
```

> **注意**：插件变更后通常需要重启 Harness 才能生效。在 Web UI 中也可以通过“设置 → 插件”进行可视化管理。

## 六、查看帮助与配置

### 6.1 查看帮助

```
# 查看启动器自己的帮助（profile 启动器的参数）
dsh --help

# 查看 Web 应用自己的参数（而不是启动器的）
dsh --profile web --help

# 查看 headless 应用的参数
dsh --profile headless --help
```

> **关键区别**：裸  `--help`  显示的是启动器的帮助；加  `--profile`  后显示的是该应用的参数帮助。

### 6.2 查看配置（排查问题很有用）

```
# 查看内置默认配置（未叠加任何 patch）
dsh --dump-default-config

# 查看叠加所有层后的最终配置
dsh --dump-config
```

这两个命令在不启动的情况下检查组合后的配置树，**排查配置问题时非常有用**。

### 6.3 临时覆盖配置

```
# 用一次性覆盖层启动（不改文件）
dsh --patch <文件路径> --profile web
```

 `--patch`  会替换目标行的整个 config 值，而不是深度合并其中的键。

## 七、最重要的规则：参数顺序

这是 dsh 命令最容易踩的坑。**启动器只解析自己的 flag，从第一个无法识别的 token 开始，后面全部属于应用参数**。

```
# ✅ 正确：启动器参数在前，应用参数在后
dsh --profile web --port 8080        # --port 是 web 应用的参数
dsh --profile tui --resume <id>      # --resume 是终端应用的参数
dsh --profile headless "run tests"   # 任务文本是应用参数

# ❌ 错误：应用参数跑到了启动器前面
dsh --port 8080 --profile web        # 启动器看不到 --profile

# 看帮助的区别
dsh --profile web --help             # 看 web 应用自己的参数
dsh --help                           # 看启动器的参数
```

**判断口诀**：启动器参数在最前，应用参数在最后。

## 八、Python SDK 调用

除了 CLI 命令，Harness 还提供了 Python SDK：

```
# 安装 Python 库
pip install deepseek-harness

# 安装 CLI 工具
pip install deepseek-harness-cli

# MCP 服务器（stdio transport）
npx -y @deepseek-harness/mcp
```

在 Python 代码中调用 Harness 的完整示例可以参考官方 Python SDK 文档。

## 九、完整命令速查表

| 命令 | 作用 |
| --- | --- |
|  `npx @deepseek-ai/dsh web`  | 一键启动 Web UI |
|  `dsh web`  | 启动 Web UI（全局安装后） |
|  `dsh --profile <name>`  | 启动指定 profile |
|  `dsh --profile headless "任务"`  | 一次性任务，跑完退出 |
|  `dsh plugin --profile <name> <pnpm args>`  | 管理 profile 插件 |
|  `dsh --help`  | 启动器自己的帮助 |
|  `dsh --dump-default-config`  | 打印内置默认配置 |
|  `dsh --dump-config`  | 打印叠加后的最终配置 |
|  `dsh --patch <file>`  | 用一次性覆盖层启动 |
|  `pnpm dsh web`  | 从源码启动（构建后） |

## 十、优缺点

### 优点

**1. 命令简洁，上手快**核心命令只有十几条，日常常用的不超过 5 条。 `dsh web`  一条命令就能跑起来。

**2. 双模式覆盖全场景**Web UI 适合日常开发，headless 模式适合脚本和 CI/CD。

**3. 插件管理标准化**一条  `dsh plugin`  命令搞定所有插件操作，统一通过 pnpm 管理。

**4. 配置可审计** `--dump-config`  和  `--dump-default-config`  让配置问题一目了然。

**5. 参数规则清晰**“启动器在前，应用在后”的规则一旦记住，基本不会出错。

### 缺点

**1. 参数顺序有严格限制**启动器的 flag 必须写在最前面，否则会被误解为应用参数。

**2. 目前仍是开发者预览版**dsh 当前为  `0.1.0-rc.6` （预发布阶段），生产环境请谨慎评估。

**3. 非内置 profile 需要手动创建** `web`  和  `headless`  以外的 profile 必须通过  `dsh plugin`  先创建。

**4. 依赖 Node.js 环境**需要 Node.js ≥ 22 才能运行。

## 十一、常见问题速查

**Q：npx 和 dsh 命令有什么区别？**A： `npx @deepseek-ai/dsh`  是首次安装/临时调用；装好后可以直接用  `dsh`  命令。

两者后续参数完全一致。

**Q：提示找不到 dsh 命令？**A：确认是否已安装，或改用  `npx @deepseek-ai/dsh`  前缀。

**Q：启动后浏览器没自动打开？**A：手动访问  `http://127.0.0.1:3080` ，确认端口没被占用。

**Q： `--help`  显示的不是我要的命令？**A：加  `--profile <name>`  后  `--help`  显示的是该应用参数；裸  `--help`  是启动器。

**Q：headless 任务卡住了？**A：它等 Agent 完成全部工作才退出，长任务属正常。

**Q：想临时改配置但不影响文件？**A：用  `--patch`  一次性覆盖层。

## 十二、写在最后

回到最初的问题：**DeepSeek Harness 的所有命令到底怎么用？**

我把 dsh 的命令体系整理成了一张表：

- 启动 ：  `dsh web`  （Web UI）和  `dsh --profile headless "任务"`  （一次性任务）
- 配置 ：  `dsh --dump-config`  和  `dsh --dump-default-config`
- 插件 ：  `dsh plugin --profile <name> <pnpm args>`
- 帮助 ：  `dsh --help`
- 规则 ：启动器参数在前，应用参数在后

这套命令体系很简洁——日常用  `npx @deepseek-ai/dsh web`  启动 Web UI，批处理用  `dsh --profile headless "任务"` ，排查用  `dsh --dump-config` ，管理插件用  `dsh plugin` 。

记住“**启动器参数在前、应用参数在后**”这条规则，基本就能顺畅使用了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐13个牛逼的SpringBoot项目](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535420&idx=1&sn=037a80b21a6207a9aafcb7aaa0fd68b1&scene=21#wechat_redirect)

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

---
原文链接：https://mp.weixin.qq.com/s/ORYQrnwOC5IIiCtXLnNHzA
