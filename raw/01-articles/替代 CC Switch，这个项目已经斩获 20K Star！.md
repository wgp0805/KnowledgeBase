---
title: "替代 CC Switch，这个项目已经斩获 20K Star！"
source: "https://mp.weixin.qq.com/s/srj61JGnon89dwkDaSoCpg"
author:
  - "[[小G]]"
published:
created: 2026-10-27
description:
tags:
  - "clippings"
---
我是程序汪 *2026年10月27日 08:30*

CC Switch 我用了很久。它把 Claude Code、Codex、Gemini CLI 这些工具的配置收在一个窗口里，点一下就能换供应商，不用手改配置文件；本地路由、熔断、MCP 和 Skills 面板、会话管理、云同步，该有的它都有。

刚开始用的一段时间里我没发现什么毛病，直到切换了一次供应商之后，我发现 `~/.claude/             settings.json           ` 里少了几处。状态栏配置不见了，13 个 hook 没了， `enabledPlugins` 和 `extraKnownMarketplaces` 被清空， `              permissions.deny            ` 里针对特定命令的拒绝规则被删，还多了一个我不认识的环境变量。

原因后来查清楚了，当时 CC Switch 保存供应商配置的办法是复制：加一个供应商，它就把你当时的配置整份复制一份存进库里，切换时写回你的文件。从 3.16.5 起，切换时会先把公共部分（ `hooks` 、 `enabledPlugins` 、 `env` 这类）按你实时的 `              settings.json            ` 重新收一份进它存的通用配置，免得这些改动在下次切换时被静默丢掉。只是这道保护只对开了通用配置的供应商生效，我库里唯一没开的那个正好是 DeepSeek，于是它写回的是整份旧快照。

为了不再丢，我写了一个 skill、两个 hook 和一段对账脚本守着 `              settings.json            ` ，来解决供应商配置回退的问题。

> CC Switch 4.0 <sup>[1]</sup> 已经把写回改成只替换几个字段，写入前还会检查文件有没有被别处改过。

国庆节那会，我偶然看到 magpie，决定暂停 CC Switch，换上试试。这篇文章记录这段时间的使用感受，以及我对 magpie 的一些看法。

![图片](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/deed85d1392b7e807a82308ba7f3afe8_MD5.webp)

## 我不用再手动切供应商

装完 magpie，机器上会多一个网关，地址是 `127.0.0.1:3425` 。它能在 OpenAI 的 Chat Completions 和 Responses、Anthropic Messages、Google Gemini 这几种 API 格式之间转换。CC Switch 也有协议转换功能，具体支持的转换方向要看接入的客户端和上游接口。

让我省事的是模型列表。以前我用 CC Switch 时，习惯进页面手动切供应商；现在在 magpie 里，各家供应商的模型摆在一起，Claude Code 的模型列表里也能选。不过 CC Switch 4.0 也增加了类似的聚合模式。

![CC 模型列表展示](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/ebd2a81b0966dfa03b3563620959f9d1_MD5.png)

CC 模型列表展示

magpie 给 Claude Code 的 opus、sonnet、haiku、fable 四档各留了一个下拉框。可以四档指向同一个模型，也可以给 opus 挑个贵的、给 haiku 挑个快的，也可以单独给子 Agent 指一个。

![claude code模型配置](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/fe600a4b98da6e7c363a0344beab2da6_MD5.png)

claude code模型配置

添加也很简单，内置预设都在“添加供应商”里，预设里没有的可以自定义。

![供应商配置展示](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/a39a614b5f5742689fc83e057dd88ff1_MD5.png)

供应商配置展示

![供应商配置界面](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/fd9f132a5e815d922b1f3cb83d93db17_MD5.png)

供应商配置界面

需要额外登录或请求逻辑的供应商，还可以用插件接入。插件可以来自 npm 包、git 仓库或者本地文件夹，可以用别人写好的，也可以自己定制。比如浏览器授权、设备码登录、定期刷新 token 这些场景，就可以交给插件。

![插件](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/664e20cf9c6b7a4d8247ee30ba718108_MD5.png)

插件

## 它替我挑供应商，也替我挑账号

开启“自动创建路由组”后，多个供应商提供的同名模型会自动组成一个组。我的截图里就有一个 `group/auto-deepseek-v4-1-flash` ，底下是 OpenCode Go 和火山引擎两个来源。当前文档把自动组写作 `auto/<模型 ID>` ，旧的 `group/auto-…` 名称仍兼容。也可以手动建组，把不同模型放在一起。在 Agent 里选中这个组之后，请求才会按组里的策略分给这些来源。

选了模型组，magpie 会根据策略安排组内模型、账号和 Key 的使用顺序。默认智能策略下，不同供应商的账号和 Key 可以放在一起比较额度和重置时间；供应商另设了与分组不同的路由策略时，则保留它自己的排序方式。就本文关注的自动选择而言，CC Switch 的 failover 机制主要是每个工具一条供应商队列，当前供应商不可用时跳到下一个；magpie 还会在请求开始前，根据额度和重置时间安排这一轮先交给谁。

一个供应商挂多个账号的时候，也能单独设置路由。下面是几个常用策略，名称沿用截图里的叫法。

| 界面上的叫法 | 它会怎么做 | 适合什么时候用 |
| --- | --- | --- |
| 智能（默认） | 在还有额度的账号里挑重置时间最早的 | 不想管，别让额度白过期 |
| 按顺序 | 按你排好的顺序走，前一个答不了才轮到下一个 | 有明确的主力和备用 |
| 轮流 | 重新选择时，轮到下一个账号或 key | 想把用量摊平 |
| 最少使用 | 有额度数据时优先选已用比例低的；普通 Key 按近期 token 用量排序 | 想优先使用消耗较少的账号或 Key |
| 重置前用完 | 比较各账号重置前每小时还能用掉多少，多的先上 | 周额度想用干净 |

路由策略决定重新选择时的顺序；是否重新选择，还要看下面的会话保持设置。

拿默认的智能举例，假如两个账号的额度都还充足，一个周额度明天重置，一个下周重置，它先用前者，快到期的不用就浪费了。只有 5 小时窗没有周窗的账号，比如 Claude 企业版，按 5 小时算，排在所有周窗更晚重置的前面。相关额度窗口已用到 90% 或以上的账号会靠后，先让额度充足的账号回答。

策略下面还有一项叫“被限流时”，可以选“保持原位”或者“排到最后”。另外额度用完的账号会休息到额度重置，欠费停用的歇半小时等人充值，厂商限流的按它给的 Retry-After 跳过，报错的账号退避，越错越久。这类故障转移的前提是回复尚未发给 Agent：前一个没答成，可以转给下一个；不能理解成回复已经发到一半，也能无缝换账号接着答。这类失败切换 CC Switch 也有；magpie 在这些之上多做了一件事，它提前替你安排账号的使用顺序。

![路由页面](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/1c9f7a65186595a625bdabda563fd567_MD5.png)

路由页面

选完策略，接着要定一次选择保持多久。Agent 收到你一条消息，往往会连着调好几次工具，每次把结果发回来都可能产生新请求。这些请求要是不断换账号或模型，前面对话的缓存优势可能就丢了，有些厂商还不接受别家模型写出来的 reasoning。所以还有一组会话保持的设置，下面列出截图中的四项。

| 设置 | 保持多久 |
| --- | --- |
| 自动（默认） | 同一轮内保持；跨轮时看厂商缓存的那部分还值不值得留 |
| 整个会话 | 只要还能正常响应，整个会话都用同一个 |
| 一轮之内 | 这一轮的工具调用保持不变，你再次发言时重新选 |
| 关闭 | 每次请求都重新选 |

这里的一轮是从你发出消息开始，到 Agent 回完为止。保持也有例外，当前账号答不了还是会换人，上下文涨过当前模型能装的上限也会挪给容量更大的那个。

账号之外，还能按请求本身的样子分流。一个模型组里的规则可以看长度（token 数超过多少）、有没有带图、要不要 reasoning、来自哪个 Agent、是不是在压缩上下文，以及意图，还能限定在哪些时段、星期几、哪些文件夹（或排除某些文件夹）生效。

比如遇到不能识图的模型时，可以让一个识图模型把图片描述给它；不能联网搜索时，可以指定用哪个搜索 API 或哪个模型代它去搜，再把结果交给它，不用撞上了再手动换。还有我以前常遇到 Agent 陷入死循环：思考或正文反复绕着同样几句打转，就是不往下走。magpie 对这种也做了防御，检测到就把这一条回复结束掉，交回一个 Agent 可以重试的错误。

![图模型设置、搜索和循环打断](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/1a353ce7954f1d09756d7087840cf667_MD5.png)

图模型设置、搜索和循环打断

意图路由则是让一个判断模型来决定请求属于哪一类，比如简单问答、写测试，再优先交给你为这一类指定的模型。我还没给自己配意图规则，下面只说明它的机制，没有实际检验过分类效果。

按 [v0.1.1564](http://v0.1.1564) 的实现 <sup>[2]</sup> ，判断模型会看到最新用户消息，以及经过截断的上一条用户消息和其后助手最后一条文字回复，用来理解“继续”“修一下”这类追问。系统提示、思考内容、工具调用参数和工具结果不会一起发过去，Claude Code 添加的 `system-reminder` 也会被剥掉。

判断默认最多等 8 秒，可在设置里调长，最高 60 秒。调用出错、超时或回答无效时，如果上一轮的意图仍在本轮候选中，就沿用它；没有可沿用的意图，才按其他规则或默认策略走。这一点以当前版本的失败处理逻辑 <sup>[3]</sup> 为准。判断需要额外的模型调用，用量页能看到；也可以用 Ollama 或 LM Studio 上的本地模型来判断。

![路由组编辑](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/c6b6fe5dce62a0760037c6a4679a8afd_MD5.png)

路由组编辑

![路由组编辑（2）](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/e95d64be0a97212a7f76d10d4b300ee4_MD5.png)

路由组编辑（2）

组不用从零写。路由页面没有自己的组时，会给出三个模板，点一下就能建好。“难题给强模型，简单的给便宜模型”把难活交给强模型，压缩之类的杂活交给便宜的；“便宜优先”先用便宜模型，需要高推理或者便宜的都不行了再交给强的；“永不卡住”让各家供应商最强的模型依次给对方当后备。这些组也能从命令行创建和调整。

![路由组模板](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/0c47260fd5f2e4c9e3b90b8874f91d82_MD5.png)

路由组模板

## 它做了什么，我看得见

magpie 让我能看到本机网关的请求状态，以及它对 Agent 配置做了哪些修改。

在 Agent 的模型配置界面，magpie 会给你展示它改了什么，比如 Claude Code：

![claude code settings 修改提示](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/e8a1998f46e61ae87559824e5952bc0e_MD5.png)

claude code settings 修改提示

用量页按模型和账号统计 token 数、缓存命中率和折算出来的费用，还可以看账号的明细，显示尝试、应答、失败、已用额度和多久重置。

![用量页面](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/0a0e30872b50e8b3fc1ca0fd33e6dcd0_MD5.png)

用量页面

在路由页面顶上是一条流水，Agent 经 magpie 发出的每个请求都列在这里：由谁应答、为何选它，以及每次尝试。

![路由页顶部实时状态](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/527832ebf91ba8f77cc5997bdff480d4_MD5.png)

路由页顶部实时状态

下面还能看到请求的实时状态，比如上下文、缓存命中、时间和费用。

![路由请求实时界面](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/0c8dbf2d4713eb65fe8c2aeefde92697_MD5.png)

路由请求实时界面

这些记录让我排查路由问题时有据可查。在网关页，还能查看结构化展示的最近调用的原始消息。

![网关](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/93b140bc26731ee13f190636da305e60_MD5.png)

网关

## 参数可以细调，接入配置可以还原

供应商详情里的参数可以按模型覆盖。上下文窗口、单次最大输出、压缩阈值都能自己填，还能写成 `deepseek-v4-flash=272k` 这样按模型分别指定。上下文窗口和最大输出留空时按厂商和 [models.dev](http://models.dev/) 的数据补全；压缩阈值留空时则跟随设置里的“长对话”选项。

每个账号还能单独设置网络连接方式，可以沿用供应商的设置，也可以按需单独配置。不同账号有不同的连接需求时，不用共用同一套设置。再下面还有并发上限，默认不限制。

接入网关要改 Agent 的配置，这是最容易出事的地方，magpie 在这上面做得比较小心。它每次写入前都先读一遍原文件，只更新接入模型需要的字段，注释、键的顺序、缩进都保留，落盘是原子写。以 Claude Code 为例，连接上游用到的是 `~/.claude/             settings.json           ` 的 `env` 段： `ANTHROPIC_BASE_URL` 、 `ANTHROPIC_AUTH_TOKEN` ，以及 opus、sonnet、haiku、fable 四档各自的模型变量。我这台机器上 base URL 指向 `127.0.0.1:3425` ，token 就是字符串 `magpie` 。Codex 那边是在 `~/.codex/             config.toml           ` 里加一张 `[             model_providers.magpie]           ` 表和一个模型名，模型清单另外放进 `              magpie-models.json            ` ，官方明说不碰你原来的 ChatGPT 登录状态。

不过我翻它自己的记录才知道，为了给 Claude Desktop 接第三方供应商，它新建了一整个 `Claude-3p` 配置目录。所以除了更新接入需要的字段，它也可能添加新的配置文件。

改过什么它也会记着。 `              applied.json            ` 存每个 Agent 最近一次应用了哪些字段、什么时候写的， `              stash.json            ` 保留接入前的原值，以及部分还原所需的状态。想退回去，可以在界面里点“断开并还原”，也可以跑 `magpie <agent> default` ，它会撤掉自己写的内容，还原被替换的值，包括你接入之前就有的那个 `ANTHROPIC_BASE_URL` 。

## 一些值得说的细节

**第一眼是界面** ，我觉得 magpie 的 UI 做得比 CC Switch 舒服，看久了不累。

**托盘也值得说** 。magpie 只留一个图标，鼠标指上去就能看到所选订阅还剩多少额度，点开是快捷面板，也能设成直接开主窗口，不用把主窗口翻出来。

对支持重置卡的订阅，magpie 的卡片里会写还剩几张、什么时候过期，还可以打开 **自动使用重置卡** 。有可用卡时，它会自动尝试重置额度，减少手动处理和等待。

![托盘](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/2835b5a4bf86d58709f29bf29405e282_MD5.png)

托盘

对按首次请求启动 5 小时窗口的订阅，设置里有两项能提前启动计时： **窗口重置时预热** 会在窗口重置后发一条极小的请求，让下一个窗口开始计时； **每日定时预热** 则在每天指定的时间，为各账号启动窗口。这样，早上打开电脑时，窗口可能已经跑了一段。如果工作时段刚好跨过重置点，就能先后使用前后两个窗口的额度；每个窗口的额度上限仍由厂商决定。

![窗口预热](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/a0e347942758a470ddc94f9beb9aa493_MD5.png)

窗口预热

隐私页还提供了脱敏和掩码设置，具体选项可以在界面里查看。

![隐私](assets/%E6%9B%BF%E4%BB%A3%20CC%20Switch%EF%BC%8C%E8%BF%99%E4%B8%AA%E9%A1%B9%E7%9B%AE%E5%B7%B2%E7%BB%8F%E6%96%A9%E8%8E%B7%2020K%20Star%EF%BC%81/7c142334b7c656d484806f6bd1b2fe51_MD5.png)

隐私

## 总结

CC Switch 4.0 已经修复了我当时遇到的配置写回问题，也增加了模型聚合。不过在我目前的多供应商、多账号用法里，magpie 的自动路由和额度安排更合我的习惯，所以暂时没有换回去的打算。

magpie 的界面和功能更新频繁，适应新设置也要花时间。如果你已经用习惯了 CC Switch，现有功能也够用，就没有必要因为我这次换工具而跟着迁移。

magpie 也有 CLI 版本给不想开桌面窗口的人用。 `magpie tui` 提供终端里的完整界面；习惯在终端里管模型和路由的话，可以翻官方中文文档 <sup>[4]</sup> 。

CC Switch 的后续更新可以在官方仓库 <sup>[5]</sup> 查看。

参考资料

\[1\]

CC Switch 4.0: *[https://github.com/farion1231/cc-switch/releases/tag/v4.0.0](https://github.com/farion1231/cc-switch/releases/tag/v4.0.0)*

\[2\]

[v0.1.1564](http://v0.1.1564) 的实现: *[https://github.com/yetone/magpie/blob/v0.1.1564/internal/gateway/classify.go](https://github.com/yetone/magpie/blob/v0.1.1564/internal/gateway/classify.go)*

\[3\]

失败处理逻辑: *[https://github.com/yetone/magpie/blob/v0.1.1564/internal/gateway/rules.go](https://github.com/yetone/magpie/blob/v0.1.1564/internal/gateway/rules.go)*

\[4\]

官方中文文档: *[https://usemagpie.ai/docs/zh/](https://usemagpie.ai/docs/zh/)*

\[5\]

官方仓库: *[https://github.com/farion1231/cc-switch](https://github.com/farion1231/cc-switch)*