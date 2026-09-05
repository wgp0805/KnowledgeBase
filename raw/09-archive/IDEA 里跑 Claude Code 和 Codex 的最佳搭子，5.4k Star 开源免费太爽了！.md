---
title: "IDEA 里跑 Claude Code 和 Codex 的最佳搭子，5.4k Star 开源免费太爽了！"
source: "https://mp.weixin.qq.com/s/sDC_HeBQO7LYmWU4A4WYHQ"
---
程序汪 我是程序汪 *2026年8月18日 08:24*

JetBrains 用户用编程 Agent，最容易被低估的成本不是 Token，而是注意力。

代码在 IDEA，Claude Code 或 Codex 跑在终端。Agent 说改了三个文件，你切回项目树找文件；测试挂了，你再把控制台报错复制回终端；中途来了一个权限确认，又得找刚才那个窗口。每一步都不难，但连续做十几次，思路就散了。

CC GUI 想解决的正是这件事：把 Claude Code、Codex 这类 CLI Agent 接进 JetBrains 的工具窗口，让文件引用、执行过程、权限确认、Diff 和历史会话回到同一处。

不过，到了 2026 年再介绍它，不能只说“JetBrains 没有好用的官方 Agent 界面”。IntelliJ IDEA 2026.2 的 AI Assistant 已经原生接入 Claude Agent、Codex 和 ACP Agent，也支持 Skills、MCP、项目指令以及修改保留或回滚。问题已经从“有没有”变成了“哪条工作流更适合自己”。

CC GUI 将两个 CLI Agent 接入 IDEA

*图 1：IDEA 仍是编码中心，Claude Code 和 Codex 负责读取、执行和返回修改。*

*![图片](assets/IDEA%20%E9%87%8C%E8%B7%91%20Claude%20Code%20%E5%92%8C%20Codex%20%E7%9A%84%E6%9C%80%E4%BD%B3%E6%90%AD%E5%AD%90%EF%BC%8C5.4k%20Star%20%E5%BC%80%E6%BA%90%E5%85%8D%E8%B4%B9%E5%A4%AA%E7%88%BD%E4%BA%86%EF%BC%81/992ac4e8b97471f3c2a64bb2aaaa8465_MD5.webp)*

## 先看项目本身：它不是模型，也不只是聊天框

CC GUI 原名 Claude Code GUI，后来为规避商标风险改名。项目采用 MIT 许可证。写稿时，GitHub 仓库约有 5.4k Star、615 Fork 和 1837 次提交，最新 changelog 已到 2026 年 8 月 12 日的 [v0.5.2。](http://v0.5.2。)

它不提供模型能力，真正干活的仍是 Claude Code、Codex 或其他已配置的 CLI。插件负责补齐 IDE 这一侧的体验：

- 在编辑器里用 `@文件` 、代码选区、图片和控制台输出组织上下文；
- 把流式文本、思考、命令、工具调用和子 Agent 状态拆开显示；
- 把文件修改整理成 Diff，支持跳转、保留和撤销；
- 管理历史会话、搜索、收藏、导出、Token 与配额；
- 在界面中管理 Provider、Skills 和 MCP；
- 从编辑器、项目树、Run/Debug 控制台和 VCS 区域直接发起动作。

这几个能力单看都不稀奇，组合起来才有价值。它减少的不是一次复制粘贴，而是一整轮任务里反复切上下文的次数。

## 为什么它需要 Java、React 和 Node 三套代码

仓库目录很能说明问题：

```
src/main/java/   JetBrains 插件层
webview/         React + TypeScript 交互界面
ai-bridge/       
            Node.js
           CLI 适配和事件转换
```

Java 层负责理解 IDE：当前项目、编辑器选区、文件导航、原生 Diff、通知和插件生命周期。React WebView 负责把会话、权限弹窗、工具调用和流式结果组织成人能读懂的界面。Node `ai-bridge` 则面对各家 CLI，把不同格式的事件归一成统一消息。

一条消息大致会这样走：

```
输入框
  → Java Bridge
  → ai-bridge
  → Claude/Codex CLI
  → 流式事件与文件补丁
  → Java 回调
  → React 更新消息和 Diff
```

Codex 的 `function_call` 、 `custom_tool_call` 和 patch 并不是直接扔给前端。仓库里的 `              codex-event-handler.js            ` 会先把它们整理成工具调用、工具结果和文件操作。前端再通过 `useWindowCallbacks` 、 `useStreamingMessages` 等 Hook 处理增量消息和状态竞态。项目的前端架构文档把这条链路写得很清楚。

CC GUI 三层架构

*图 2：插件并非直接把网页塞进 IDEA，中间还有 IDE API 和 CLI 事件适配。*

*![图片](assets/IDEA%20%E9%87%8C%E8%B7%91%20Claude%20Code%20%E5%92%8C%20Codex%20%E7%9A%84%E6%9C%80%E4%BD%B3%E6%90%AD%E5%AD%90%EF%BC%8C5.4k%20Star%20%E5%BC%80%E6%BA%90%E5%85%8D%E8%B4%B9%E5%A4%AA%E7%88%BD%E4%BA%86%EF%BC%81/ed32739100a799971ec6f1f7bbf1045c_MD5.jpg)*

## 官方 Agent、CC GUI、纯终端，怎么选才不拧巴

参考文章把官方 ACP 描述成“轻量接入”，这个判断放到今天已经不够准确。JetBrains 2026.2 的官方文档明确列出了 Claude Agent、Codex、Skills、MCP、项目上下文和变更回滚；ACP 也已经成为官方支持的 Agent 接入层。

三条路线现在更像是不同取舍：

| 路线 | 更强的地方 | 需要接受的代价 |
| --- | --- | --- |
| JetBrains 官方 Agent / ACP | 官方维护、IDE 集成统一、Agent 注册和团队治理更顺 | 能力和登录方式受 JetBrains 版本、AI Assistant 与 Provider 支持范围影响 |
| CC GUI | MIT 开源、CLI 会话和 Provider 管理更细、历史与配额界面丰富、可读源码 | 多一层 Java/JCEF/Node bridge，升级和兼容问题需要社区处理 |
| 纯终端 | 链路最短、脚本化方便、CLI 新能力通常最先可用 | 文件、Diff、报错和权限确认分散在多个窗口 |

如果公司统一采购 JetBrains AI、需要集中管理，官方路线更稳。如果已经长期使用 Claude Code 或 Codex CLI，希望保留原来的配置、会话和供应商习惯，CC GUI 更贴手。终端用户也没必要为了“看起来完整”强行换 GUI。

三种 Agent 使用路线对比

*图 3：三条路线没有绝对胜负，差别主要在维护责任和操作习惯。*

*![图片](assets/IDEA%20%E9%87%8C%E8%B7%91%20Claude%20Code%20%E5%92%8C%20Codex%20%E7%9A%84%E6%9C%80%E4%BD%B3%E6%90%AD%E5%AD%90%EF%BC%8C5.4k%20Star%20%E5%BC%80%E6%BA%90%E5%85%8D%E8%B4%B9%E5%A4%AA%E7%88%BD%E4%BA%86%EF%BC%81/223ea9f29b73989309020b41b2c3ac67_MD5.jpg)*

## 安装时别急着点到底，先把三件事弄清楚

第一步是在 JetBrains 插件市场搜索 `CC GUI (Claude or Codex)` 。安装后，右侧会出现 `CCG` 工具窗口。当前构建脚本声明的 JetBrains Build 兼容范围为 `233` 到 `263.*` ，但具体 IDE 版本仍建议以插件市场页面为准。

第二步是确认本机运行环境。插件会检测 [Node.js](http://node.js/) 和相关 CLI 依赖，但最好先在自己的终端里确认：

```
node --version
claude --version
codex --version
```

用哪一个 Agent，就至少保证对应命令能正常启动。Windows、WSL、nvm、自定义 Node 路径是最容易出问题的几类环境。

第三步是选择凭证来源。插件支持手动配置 Provider、显式读取本地配置、CLI Login，以及兼容 cc-switch。这里不要只看“能连上”：还要确认请求发往官方地址还是代理地址、使用订阅登录还是 API Key、代码会经过谁的服务器。

第一次对话建议只做读取：

```
只读分析当前项目，列出模块、启动入口和测试目录。
不要修改文件，不要执行安装命令。
```

等文件引用、流式输出和权限弹窗都正常，再开始让它改代码。

## 一个更适合 Agent 的实战：给退款回调补幂等

“接入一个完整支付渠道”范围太大，不适合拿来测试插件。更合理的任务是：已有 Spring Boot 退款回调偶尔被重复投递，需要补幂等控制和并发测试。

先进入规划模式，把边界说清楚：

```
/plan

只读分析 RefundNotifyController、RefundService、退款记录表和现有测试。
目标：同一 refundNo 重复回调时不能重复更新余额，也不能重复发送消息。
请输出调用链、事务边界、幂等键、数据库约束、并发测试和回滚方案。
暂时不要修改代码。
```

这一步的重点不是让 Agent 写一份漂亮方案，而是逼它回答几个工程问题：唯一约束放在哪里，插入日志和更新余额是否处于同一事务，消息发送失败怎么补偿，并发回调是否真的被测试覆盖。

方案过关后再切执行模式，限定修改范围：

```
按刚才的方案执行，只修改退款回调相关类、数据库迁移和测试。
完成后运行目标测试，展示完整 Diff；不要顺手重构其他支付代码。
```

一种可能的核心代码会接近这样：

```
@Transactional
public void handle(RefundCallback callback) {
    boolean first = 
            callbackLogRepository.tryInsert(callback.refundNo());
          
    if (!first) {
        return;
    }
    
            refundRepository.markSuccess(callback.refundNo());
          
    
            eventPublisher.publish(
          new RefundCompleted(
            callback.refundNo()));
          
}
```

这只是示意，真正要审的是数据库唯一索引、事务提交与消息一致性。CC GUI 的作用是把“读代码、出计划、确认权限、看 Diff、跑测试”串在一起，不是替你跳过这些判断。

规划到测试验收的安全工作流

*图 4：先只读规划，再人工复核，最后才让 Agent 修改和测试。*

*![图片](assets/IDEA%20%E9%87%8C%E8%B7%91%20Claude%20Code%20%E5%92%8C%20Codex%20%E7%9A%84%E6%9C%80%E4%BD%B3%E6%90%AD%E5%AD%90%EF%BC%8C5.4k%20Star%20%E5%BC%80%E6%BA%90%E5%85%8D%E8%B4%B9%E5%A4%AA%E7%88%BD%E4%BA%86%EF%BC%81/20be9a064085398baf8f7ed3d4184e99_MD5.jpg)*

## 真正值得长期用的，不是功能数量

我会优先关注下面五项，而不是模型下拉框有多少个：

1. **上下文入口** ：选区、文件路径、控制台错误能否快速送入会话。
2. **权限可见性** ：命令、写文件和 MCP 调用是否清楚地要求确认。
3. **Diff 与回退** ：Agent 改了什么，能不能按文件检查和撤销。
4. **会话恢复** ：长任务中断后，历史、模型和工作目录能否正确恢复。
5. **进程稳定性** ：IDE 重启、系统休眠或网络抖动后，Node daemon 会不会留下僵尸进程。

从 changelog 看，维护者确实在处理这些脏活：Windows CLI 解析、JCEF 中文输入法、密集流式输出、权限 watcher、后台子 Agent 和 Codex patch 恢复都出现过专项修复。这比一句“支持双引擎”更能说明项目已经进入真实使用阶段。

## 最后说点不那么爽的

CC GUI 是社区插件，不是 JetBrains、Anthropic 或 OpenAI 官方产品。仓库更新快，同时也有数百个 issue；升级前看 changelog、重要项目先建分支，是很正常的使用成本。

它也没有让数据边界自动消失。配置第三方 Provider 或代理端点时，源码和提示词会进入对应服务；API Key、CLI 登录和本地配置文件是不同的凭证路径，不能混着理解。权限模式更不能为了省一次点击就长期全开。

所以我的结论不是“JetBrains 用户闭眼装”。更准确的说法是：已经在用 Claude Code 或 Codex CLI，又希望把会话、文件和 Diff 拉回 IDEA 的人，CC GUI 值得试；已经满意官方 Agent，或者习惯纯终端的人，没必要为了功能表再叠一层。

它最有价值的地方，不是让 AI 看起来更像 IDE，而是让开发者在 Agent 动手时，依然看得见上下文、权限和改动。

项目地址：zhukunpenglinyutong/jetbrains-cc-gui

参考资料：JetBrains AI Assistant｜Agent Client Protocol｜CC GUI README｜CHANGELOG