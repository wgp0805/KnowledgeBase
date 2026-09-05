---
title: "推荐一个节省token的AI编程神器！"
source: "https://mp.weixin.qq.com/s/v9NGIgaTxM11-u9Fw7R1uw"
---
苏三说技术 *2026年8月12日 16:20*

> Pi 是 Mario Zechner（libGDX 作者、OpenClaw 底层 harness）做的极简终端编码代理，87.3k stars，MIT 协议，最新 [v0.84.1。核心工具只有](http://v0.84.1.xn--h6qp3d7wov0bd2o2wb/) read / write / edit / bash 等六个，没有内置 plan mode、子代理、MCP、权限弹窗——这些全都靠 TypeScript 扩展、skills、提示词模板和包来补齐。它的设计哲学是「适配你的工作流，而不是反过来」。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247540717&idx=1&sn=38b6274ac70dd2d421f515f5d5af27f3&scene=21#wechat_redirect)

**#Pi** **#编码代理** **#Harness** **#最佳实践**

## Pi 是什么

一句话定位：极简的编码代理 harness，核心小，上下文开销小，小模型也能跑。它和 Claude Code、Codex 的差别不在模型能力，而在你能完全掌控上下文里有什么、工具能碰什么、出问题怎么恢复。

系统提示词只有 ~1000 token，Claude Code 是 ~14,000。单轮就省 1.3 万输入 token，长会话省得更多。

## 安装与初始配置

三选一，装完直接 `pi` 启动：

```
bashcurl -fsSL 
            https://pi.dev/install
           | sh
npm install -g --ignore-scripts @earendil-works/pi-coding-agent
pnpm add -g --ignore-scripts @earendil-works/pi-coding-agent
```

配置模型： `/login` → 选 “Use an API key” → 选 provider → 填 key，之后 Pi 存好凭据直接用。也可以直接设环境变量（ `ANTHROPIC_API_KEY` 、 `DEEPSEEK_API_KEY` 等）。支持 15+ provider：Anthropic、OpenAI、Google、DeepSeek、Groq、xAI、OpenRouter、Kimi、MiniMax、Ollama。

| 操作 | 方式 |
| --- | --- |
| 切换模型 | `/model`  或 Ctrl+L 打开选择器 |
| 循环已选模型 | Ctrl+P |
| 切换思考级别 | Shift+Tab（off 到 max 七档） |
| 查看全部快捷键 | `/hotkeys` |

模型切换是即时的，这是 Pi 效率的核心之一：重活切大模型，批量活切便宜小模型，成本差距能到几十倍。

## 上下文工程：token 优势是省出来的

Pi 的 token 优势是「省出来的」不是「自动给的」。Alex Dunlop 把 Claude Code 的 [CLAUDE.md（含全部](http://claude.xn--md\(-gw1e89juz4j/) skills、MCP、规划工作流）原样搬到 Pi，一小时烧掉 400 万 token。Claude Code 的 14K 提示词是安全网，会静默处理上下文管理、吸收写得烂的指令文件；Pi 没有兜底，指令文件膨胀直接变账单。

三条铁律：

- [AGENTS.md](http://agents.md/) 只放行为规则：工具偏好、工作风格、禁止事项。不放项目百科。
- 全局指令放 `~/.pi/agent/             AGENTS.md           ` ，项目指令放项目根目录 [AGENTS.md，按目录层级自动向上加载。](http://agents.xn--md,-x28ds3slb92pj3zmqg3kkx60d5mtfwje11c./)
- 长文档用 skills 承载（渐进式披露，用的时候才读全文），别塞进 [AGENTS.md。](http://agents.md./)

[AGENTS.md](http://agents.md/) 加载顺序： `~/.pi/agent/             AGENTS.md           ` → 从当前目录向上逐级 → 当前目录。某个目录有 [AGENTS.override.md](http://agents.override.md/) 就整体替换该目录的 [AGENTS.md。不想要上下文文件用](http://agents.md.xn--fhqce84g117d8iga3213akj2b/) `pi -nc` 或 `--no-context-files` 。

想整体换系统提示词：`.pi/             SYSTEM.md           ` （项目级）或 `~/.pi/agent/             SYSTEM.md           ` （全局）替换默认提示词； [APPEND\_SYSTEM.md](http://append_system.md/) 在默认提示词后面追加。

上下文窗口自动压缩，阈值可调：

```
json{
  "compaction": {
    "enabled": true,
    "reserveTokens": 16384,
    "keepRecentTokens": 20000
  }
}
```
- 自动压缩：contextTokens 超过 contextWindow - reserveTokens（预留 16K 给模型回复）时触发。
- 手动压缩： `/compact [instructions]` ，instructions 可以聚焦摘要方向，比如「重点保留架构决策和未完成事项」。
- 分支摘要： `/tree` 切换分支时，Pi 会问要不要总结被放弃的分支，把关键上下文带进新分支。

## 会话管理：/tree 是杀手锏

会话自动存 `~/.pi/agent/sessions/` ，按工作目录分。JSONL 格式，天然可回放、可分享。

| 命令 | 用途 |
| --- | --- |
| `pi -c` | 继续最近会话 |
| `pi -r` | 启动时浏览历史会话 |
| `/resume` | 会话选择器（可搜索、重命名、删除） |
| `/tree` | 会话树导航，回到任意历史点重新分支 |
| `/fork` | 从某条历史消息开新会话文件 |
| `/clone` | 复制当前分支到新会话 |
| `/name <名称>` | 给会话命名，方便以后找 |
| `/export`  、 `/share` | 导出 HTML / 分享为私有 GitHub gist |
| `/session` | 查看当前会话文件、ID、token、费用 |

`/tree` 的用法：会话是树结构，可以跳到任何历史点从那里继续，不新建文件。设计探索有风险就 `/fork` 开新会话，搞砸了放弃分支，而不是在混乱的对话里修补。切换分支时让 Pi 总结被放弃的分支，上下文不丢。

长任务开工前先 `/name` 命名， `/resume` 里一眼找到。

## 模型策略：多模型分工

工具免费、模型自备（BYO-Model），这意味着模型选择完全由你控制。社区实测的配置思路（DeepakNess）：

| 模型 | 用途 |
| --- | --- |
| DeepSeek v4 Pro | 默认主力，质量成本平衡 |
| DeepSeek v4 Flash | 批量重复任务，抓 285K URLs 跑了 1.5 小时只花 $1 |
| Kimi [K2.7](http://K2.7) Code | 第二意见，或撞限流时备用 |
| Cursor（pi-cursor-sdk） | 复用已有订阅，不另付 API 费 |
| 大模型 | 复杂推理任务偶尔用 |

Ctrl+P 在 scoped models 之间循环， `/model` 随时换。循环列表用 enabledModels 配：

```
json{
  "enabledModels": ["claude-*", "gpt-4o", "deepseek-v4-flash"]
}
```

## 让 Pi 自己写扩展

这是 Pi 和其他编码代理最大的区别：需要什么功能，直接让 Pi 写扩展。它在官方文档里原话就是「pi can create extensions. Ask it to build one for your use case.」

扩展是 TypeScript 模块，放 `~/.pi/agent/extensions/` （全局）或 `.pi/extensions/` （项目级），写完 `/reload` 热重载，不用重启。 `pi -e ./             path.ts           ` 只适合快速测试，不会热重载。

能做的事：

- 注册自定义工具，模型可以直接调用（ `              pi.registerTool            ` ）
- 事件拦截：权限门（rm -rf 前确认）、Git checkpoint（每轮 stash、分支时恢复）、路径保护（禁止写.env）
- 自定义命令： `/mycommand`
- 自定义 compaction 摘要逻辑

官方给了 50+ 示例扩展。社区案例：DeepakNess 让 Pi 写了个 minimal footer 扩展，只显示工作目录、git 分支、模型名、思考级别、上下文占用，一句话描述需求它就写出来了——这种事在别的工具里做不到。

包生态用 `pi install` ： `pi install npm:xxx` 或 `pi install git:             github.com/user/repo@v1           ` ，npm/git 源都支持。

## Skills 与提示词模板

Skills 走 Agent Skills 标准（ [SKILL.md](http://skill.md/) + 渐进式披露），Claude Code / Codex 的技能直接复用：

```
json{
  "skills": ["~/.claude/skills", "~/.codex/skills"]
}
```

加载位置： `~/.pi/agent/skills/` 、 `~/.agents/skills/` 、项目 `.pi/skills/` 和 `.agents/skills/` 。 `/skill:name` 强制加载某个技能（模型不总是自动读 skill，手动加载更可靠）。

方法论用 skill 承载。一句「use TDD」远不如一个完整 TDD skill：定义哲学、反模式、逐步工作流。Dillon Mulroy 共享的会话里，这就是高质量产出的关键区别之一。

提示词模板： `~/.pi/agent/prompts/*.md` ，文件名即命令名。

```
markdown---
description: Review staged git changes
---
Review the staged changes (\`git diff --cached\`). Focus on:
- Bugs and logic errors
- Security issues
- Error handling gaps
```

支持参数： `$1` `$2` 位置参数， `${1:-default}` 带默认值， `${@:N}` 从第 N 个开始取， `${@:N:L}` 取 L 个。frontmatter 里 `argument-hint: "<PR-URL>"` 在自动补全里显示参数提示。常用模板： `/review` 、 `/component Button "click handler"` 。

## 编辑技巧与消息队列

| 技巧 | 操作 |
| --- | --- |
| 引用文件 | 输入 `@` 模糊搜索项目文件 |
| 路径补全 | Tab |
| 多行输入 | Shift+Enter |
| 复制上一条响应 | Ctrl+X |
| 粘贴图片 | Ctrl+V 或拖进终端 |
| 跑 shell 并把输出发给模型 | `!command` |
| 跑 shell 但不发给模型 | `!!command` |
| 打开外部编辑器 | Ctrl+G（配 `code --wait` 等） |

消息队列：agent 干活时还能继续输入。

- Enter：steering 消息，当前 turn 的 tool 执行完后送达
- Alt+Enter：follow-up 消息，全部工作完成后送达
- Escape：取消排队；Alt+Up：把排队的消息取回编辑器

长任务时这个功能很实用：不用等它跑完，先把下一步指令排队。

## 工作流：像监督资深同事一样用 Pi

Dillon Mulroy 的共享会话比文档教得多。核心转变：不是把 Pi 当快速代码生成器，而是当受监督的资深实现伙伴。给它 spec、约束、示例、评审意见、清晰流程。

- 先写 spec：目标、约束、路由、数据模型、边界情况、测试计划，再让 Pi 实现。
- [AGENTS.md](http://agents.md/) 加工作风格规则：「prefer 3-5 个小 prompt 而不是一个大 prompt」、「重写文件前先给我看 diff」。
- 写码前先做架构 review：让 Pi 检查现有文件，指出设计哪里弱、哪里 cohesion 断裂、该改什么。
- 请求调用图和 seams：public API、call graph、注入点、生产 vs 测试适配器，坏设计在写码前暴露。
- 垂直切片：一个失败测试 → 一个小实现 → 一个通过的检查。别一次就把 dashboard 建完。
- 硬约束：no new package、no mock data、no broad rewrite、no touching unrelated files。
- Markdown annotations 评审：粘贴「Section 4.1: update status to implemented / Line 42: rename fetchUrl to resolveShortLink」这类注释，让 Pi 只应用这些修改。
- 错误永久化：Pi 反复犯同样的错，把规则写进 [AGENTS.md，后续会话自动继承。](http://agents.xn--md,-0y9do6nlncqz6bfm4cqba985cqr3a./)
- 参考仓库：框架相关任务，本地留 clone 或 examples，先让 Pi 读真实代码再动手。
- 结束 handoff：让 Pi 总结改了什么、跑了哪些测试、动了哪些文件、遗留问题、下 5 个 todo。

完整循环：

```
review 现有设计 → 画选项 → 对齐形状 → 写/更新 spec → 实现一个垂直切片 → 跑检查 → annotations 评审 → 新规则写进 
           AGENTS.md
          → 清晰交接
```

## 安全：没有内置沙箱

Pi 没有内置沙箱，工具以你账号的权限运行。这是有意设计——真实隔离要靠 OS 或容器，进程内伪沙箱反而容易被误解成安全边界。

- project trust：项目里有 `.pi/             settings.json           ` 、扩展、skills 等资源时，首次进入询问是否信任（ `defaultProjectTrust`: ask / always / never）。不信任就不加载这些项目资源，但 [AGENTS.md](http://agents.md/) 照常加载。
- 未受信仓库、无人值守的自动化：放容器 / VM / 沙箱里跑，只挂载需要的目录，最小化 API key，限制网络。
- 权限门扩展：rm -rf、sudo 等危险操作先确认。

## 常见问题与避坑

- token 烧得快？ [AGENTS.md](http://agents.md/) 太肥，砍到只剩行为规则。
- 模型不读 skill？用 `/skill:name` 强制加载。
- 项目配置不生效？检查 project trust，未信任的项目不加载 `.pi/             settings.json           ` 和项目扩展。
- 扩展不生效？确认放对位置（ `~/.pi/agent/extensions/` 或 `.pi/extensions/` ）并 `/reload` 。 `pi -e` 只适合临时测试。
- 只读审查不想让模型改文件？ `pi --tools read,grep,find,ls -p "Review the code"` 只读模式。
- 不想留痕？ `pi --no-session` 临时会话，不保存。
- 上下文乱了？ `/compact` 压缩，或 `/tree` 回到分支点重来。

## 总结

- token 优势靠精简 [AGENTS.md](http://agents.md/) 省出来，不是 Pi 白送的。
- `/tree`
	、 `/fork` 用起来，搞砸了就放弃分支，别修补混乱的对话。
- 需要什么功能就让 Pi 写扩展，这是它和其他代理最大的不同。
- 模型按任务分工，Ctrl+P 随时切，成本能差几十倍。
- 把 Pi 当受监督的资深同事：spec 先行、垂直切片、annotations 评审、错误写进 [AGENTS.md。](http://agents.md./)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247540717&idx=1&sn=38b6274ac70dd2d421f515f5d5af27f3&scene=21#wechat_redirect)