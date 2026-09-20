---
source_url: "https://mp.weixin.qq.com/s/ZFIjPP8HTBXCTKndzVY_RA"
title: "MiniMax 版 Claude Code 开源，夯。"
account: "沉默王二"
published_at: "2026-09-19 16:57:00"
saved_at: "2026-09-19 19:55:59"
sync_id: "art_bf96807e05b24bc89d21fc10378238e3"
parse_status: "ok"
---

# MiniMax 版 Claude Code 开源，夯。

大家好，我是二哥呀。

好家伙，MiniMax 直接把他们的 Code CLI v0.4.12 开源了，还是 MIT 协议。

我只能说，伟大无需多言。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/5db2d7c2772abcf925fefda0c6216005_MD5.png)

这样的话，我就可以去研究 MiniMax Code CLI 的源码，从而升级我的终端 Agent PaiCLI 了，舒服了呀。

我先放一个我用 MiniMax Code CLI + DeepSeek V4.1 Flash 开发的魂斗罗录屏，整体给我的感受还是 OK 的。

[📹 点击播放视频](https://mp.weixin.qq.com/mp/readtemplate?t=pages/video_player_tmpl&action=mpvideo&auto=0&vid=wxv_4701233179091992576)

从官方给出的跑分来看，不管是速度还是任务的成功率，都挺出色。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/5b21d6c1b38dbe6f2826edb5a7ab58ea_MD5.png)

在 FrontierHarness Eval 上拿到了 SOTA 通过率、最快完成时间、第二低 token 消耗。

此处应该有掌声。

> 开源让开发者能审计、改造并复用整个工具链，CLI + Agent 的组合正在把实验快速推向真实工作流。

除了 Codex，对 Claude Code、Gemini，我其实更喜欢在终端里使用，原因很简单，这些桌面端做的有点垃圾。比如说 Antigravity，真的是烦死了，每次都要确认权限，整个输入界面竟然没有 auto 模式，我理解不了。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/331d87bf58ce1e3f89a53a93edfb7521_MD5.png)

纯纯的反人类设计。

## 01、安装和配置

安装很简单，终端直接输入一行命令。

```
curl -fsSL https://filecdn.minimax.chat/public/install.sh | bash
```

当然也可以使用源码构建。

```
git clone https://github.com/MiniMax-AI/minimax-code.git
cd minimax-code
pnpm install --frozen-lockfile
pnpm build
pnpm mcode
```

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/8001d918b6cf46387a62a3fb3c6f7405_MD5.png)

安装完成后，来配置 DeepSeek V4.1 Flash。

配置需要两步。

第一步，在终端输入以下命令，然后键入 DeepSeek API Key。

```
read -rs "DEEPSEEK_API_KEY?请输入 DeepSeek API Key: "; echo
export DEEPSEEK_API_KEY
```

第二步，键入以下命令在 MiniMax Code CLI 中添加第三方模型，无需登录。

```
mcode provider add \
  --name "DeepSeek V4.1 Flash" \
  --base-url "https://api.deepseek.com" \
  --api-format openai-completions \
  --model deepseek-flash \
  --api-key-env DEEPSEEK_API_KEY
```

配置完成后，启动  `mcode` ，确认一下。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/5ad03dba56cc7a7c9a80fee93f88ff63_MD5.png)

随便输入一个提示词，看看有没有返回就行了。

## 02、上手体验

刚好我沉淀了很多 Case，直接让 mcode 自己挑一个跑跑看。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/c425a5194b8ff7d731833d5ad63287e1_MD5.png)

我觉得目前最大的问题是权限设计，一直弹出权限确认，没办法像Claude Code那样直接快捷键设置。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/00aa7e17bd8d01648459576434505ebf_MD5.png)

不过整体长程任务的处理还是不错的，我这个跑了 32 分钟，仍然没出问题。中间涉及文件读写、命令执行、多轮工具调用，没有出现卡死或上下文丢失的情况。能跑稳长任务，说明底层的 Turn Loop 和上下文管理是靠谱的。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/ae860ff607a6b6c47871a7f1d6b45a8f_MD5.png)

## 03、Pi 框架和整体架构

MiniMax 没有从零开始写 Agent 框架，他们用了一个叫 Pi 的开源编码 Agent 框架做底座。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/8ae5c889a80e538be5fb27662ab50b1d_MD5.png)

说实话，用 Pi 自研 Harness 和自己从头自研一个 Harness 没有任何区别，但减少了极多的工作量，还能白嫖社区维护。

 `agent-core`  这个包负责定义一轮对话（Turn）的数据结构、工具协议、事件类型。

 `agent-runtime`  提供扩展注册表， `agent-extension`  实现内置的 Skills、权限、MiniApp 等扩展。

 `local-runtime-v2`  是完整的宿主实现，管 Session 和 Turn 的生命周期，用 SQLite 做持久化，负责模型选择和权限系统。

 `tui`  包负责终端渲染和 CLI 命令解析。

界面和运行时之间通过事件流通信。这意味着 TUI 可以换成 Web UI、IDE 插件或者 Headless CLI，运行时完全不需要改动。MiniMax Code 就同时支持三种入口，交互式 TUI（ `mcode` ）、无头模式（ `mcode exec` ）和 ACP 协议（ `mcode acp` ，给编辑器用的）。同一套运行时代码跑三种入口，全靠分层解耦。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/601589da7fe185837cb29aafbc2c8f1c_MD5.png)

## 04、核心循环

Agent 的核心是 Turn Loop，也就是一轮对话从用户输入到模型回复的完整流程。

MiniMax Code 的核心循环实现在  `pi-turn-runner.ts`  里：

```
async runTurn(input) {
  // 1. 构建本轮状态（全新对象，不复用上一轮的）
  const turn = newTurn(input, deps);
  // 2. 通知外部"开始执行"
  await emitRunning(turn);
  // 3. 创建 Agent 实例
  const agent = newAgent(turn);
  // 4. 创建历史游标
  const history = newHistory(turn, agent);
  // 5. 安装工具钩子（beforeTool / afterTool）
  setToolHooks(agent, turn);
  // 6. 安装模型钩子（beforeLLM / afterLLM）
  setLLMHook(agent, turn, history);
  // 7. 订阅事件流，串行队列保证顺序
  const events = subscribeEvents(agent, turn, history);
  // 8. 驱动 Agent 循环（模型调用 → 工具执行 → 再调用）
  await runAgent(agent, turn, events.convergeAtIdle);
  // 发送结束事件
  await emitTerminal(turn, termination);
}
```

两个设计让我印象深刻。

第一个是每轮状态隔离。每次执行都会创建全新的 turn、agent、history 对象，上一轮的状态不会泄漏到下一轮。好处是天然线程安全，调试也方便，出了问题只需要看当前 turn 的状态。

第二个是钩子（Hook）机制。工具执行前后、模型调用前后，都预留了钩子。扩展只需要注册一个 Hook 函数，就能在对应阶段插入自己的逻辑。举个例子，性能统计放在 afterLLM 钩子里做，权限检查放在 beforeTool 钩子里做，上下文压缩放在 onHistoryChanged 钩子里做。

## 05、工具和扩展

MiniMax Code 的工具定义有一个我很喜欢的设计，LLM 看到的 schema 和运行时执行的代码分开存放。

在  `define.ts`  里，定义一个工具只需要调用一个函数：

```
// packages/agent-core/src/tools/define.ts
const readFileTool = defineRuntimeTool({
  name: 'read_file',
  description: '读取指定路径的文件内容',
  schema: Type.Object({
    file_path: Type.String()
  }),
  async execute(ctx, input, signal) {
    // 运行时的实际文件读取逻辑
    return { text: content, content: [...] };
  }
});
```

返回值自动拆成两部分。 `def`  是定义，包含工具名称、描述、参数 schema，这些信息发给 LLM，让模型理解这个工具能干什么、参数格式是什么样的。 `impl`  是实现，包含实际的执行逻辑，留在本地运行。

换模型的时候可以调整工具定义（比如某些模型不支持复杂嵌套的 schema），而执行逻辑完全不用动。反过来也成立，优化执行逻辑的时候不影响 LLM 看到的接口描述。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/60514081226fe45dd922b1a269dc7483_MD5.png)

工具的执行上下文通过闭包注入。每个工具执行时能拿到 sessionId、turnId、toolCallId 这些信息，但这些信息是在 Turn 创建时就绑好的，不用 AsyncLocalStorage，也不用全局变量。Java 里对应的做法是通过构造方法注入一个 Context 对象。

扩展系统建在工具系统之上。 `registry.ts`  是扩展注册表，管理所有扩展的生命周期。

每个扩展在初始化时可以注册四类，工具、系统提示词、提醒、钩子。Skills 就是用这套扩展机制实现的。它在初始化时扫描项目目录和用户目录下的 Skill 文件，生成一个可用 Skills 清单注入到系统提示词里。同时注册了一个提醒器，每轮对话都会检查用户的输入是否匹配某个 Skill，匹配到了就插入一条提醒。

Skills 的实现里还有一个细节让我印象深刻。它用 WeakMap 缓存每轮对话的 Skill 快照，同一轮对话里多次访问 Skills 清单拿到的是同一份缓存，不同轮次之间旧的缓存随着对话上下文被垃圾回收自动释放，不会内存泄漏。

![](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/45b34926433c1fe4419055b47c56ebf7_MD5.png)

扩展注册表有一个清晰的生命周期状态机，new → initializing → ready（或 failed）。状态到了 ready 之后就不允许再注册新扩展了，防止运行时意外修改工具列表。初始化过程中如果任何一个扩展出错，整个注册表进入 failed 状态，不可恢复。

## ending

用了大半天跑 MiniMax Code CLI，又花了一个下午读源码。

还是挺有收获的。

其实AI时代最大的便利就是学习的成本大幅降低，几乎就没有学不会的知识，因为GitHub上有大量优质的开源项目。

加上可以用 Codex 和 Claude Code 无痛阅读源码，架构、细节、产品这些都可以覆盖到。

PaiCLI就是开源的，当时用Codex从0到1撸出来的，看来对读者的帮助就挺大。

![对读者帮助很大](assets/2026-09-19%20-%20MiniMax%20%E7%89%88%20Claude%20Code%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%A4%AF%E3%80%82/163373b30cdcab1589ecc6eb0c0200fa_MD5.jpg)

对读者帮助很大骄傲+充实。

我们下期见。

---
原文链接：https://mp.weixin.qq.com/s/ZFIjPP8HTBXCTKndzVY_RA
