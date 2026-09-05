---
title: "给 Claude Code 装上这个超酷的状态栏，逼格瞬间拉满！"
source: "https://mp.weixin.qq.com/s/9jsBgmHvS1NXrkV5VhJ-Yg"
---
Java技术栈 *2026年7月17日 10:41*

大家好，我是R哥。

使用 Claude Code 终端有一点不好就是，终端里信息密度很高， **很多常用信息都需要敲命令才能看到** ，极不方便。

比如，总要敲 `/status` 看模型和思考程度，敲 `/context` 看上下文，要么凭感觉判断是不是该 `/compact` ，等等，费时又费力。

虽然官方也支持使用 `/statusline` 命令自定义状态栏，但需要使用自然语言交流，还是通过脚本的形式，定制起来挺麻烦的。

今天我就 **推荐两个市面上比较火的状态栏工具** ，都是开源的，安装和配置比官方自带的都简单太多了，而且要更强、更美观。

它们都能给 Claude Code 装一个更好看的状态栏，把 **模型、目录、Git 分支、上下文、Token、用量** 这些信息，直接挂在终端底部。

装上状态栏之后，就不用来回切了，常用信息一眼就能看到。

> Claude Code 安装和使用教程：
> 
> - • [Claude Code 保姆级安装和使用教程分享](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247485429&idx=1&sn=9b3e6c5c2a3f81646de119e6bc90e889&scene=21#wechat_redirect)
> - • [玩转 Claude Code 的 23 个实用小技巧，效率拉满！！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247485524&idx=1&sn=dfabb331208e1b3cef651ec766c9f618&scene=21#wechat_redirect)
> - • [Claude Code 官方桌面端安装和使用教程](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487743&idx=1&sn=ea660ae13ff3b6058c2aed89e8c82aeb&scene=21#wechat_redirect)

## 1、ccstatusline

ccstatusline 的安装和配置是 **最简单、最快** 的，官方提供了交互式配置界面，几乎不用动手写配置文件，而且比较灵活，配置起来非常方便、快速。

开源地址：

> [https://github.com/sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline)

![图片](assets/%E7%BB%99%20Claude%20Code%20%E8%A3%85%E4%B8%8A%E8%BF%99%E4%B8%AA%E8%B6%85%E9%85%B7%E7%9A%84%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%8C%E9%80%BC%E6%A0%BC%E7%9E%AC%E9%97%B4%E6%8B%89%E6%BB%A1%EF%BC%81/7e3cfeaa56d3895e46ccfa207a82ba1b_MD5.png)

**功能特性：**

- • 📊 **实时指标** ：实时显示模型名称、Git 分支、Token 使用量、各模型每周用量、额外使用额度、语音输入状态、会话时长、上下文压缩次数、阻塞计时器等信息。
- • 🎨 **高度可定制** ：可自由选择显示内容，并为每个组件单独自定义颜色。
- • ⚡ **支持 Powerline** ：提供精美的 Powerline 风格状态栏，支持箭头分隔符、端点样式及自定义字体。
- • 📐 **支持多行状态栏** ：可配置多条相互独立的状态栏。
- • 🖥️ **交互式 TUI** ：内置基于 React/Ink 的交互式配置界面。
- • 🔎 **快速组件选择器** ：支持按分类搜索并智能匹配，快速添加或切换状态栏组件。
- • ⚙️ **全局配置** ：支持统一设置所有组件的样式，包括内边距、分隔符、加粗、极简模式及颜色覆盖等。
- • 🚀 **跨平台支持** ：同时兼容 Bun 和 [Node.js](http://node.js/) 运行环境。
- • 🔧 **灵活配置** ：支持通过 `CLAUDE_CONFIG_DIR` 环境变量指定自定义 Claude Code 配置目录。
- • 📏 **智能宽度适配** ：自动适配终端宽度，并通过弹性分隔符优化布局。
- • ⚡ **开箱即用** ：内置合理的默认配置，无需额外设置即可直接使用。

ccstatusline 最吸引我的地方，不是它花里胡哨，而是它把一些常用的信息放到了最显眼的位置，有了这些信息常驻，少敲命令，就是真正的效率。

### 安装方法

安装很简单，官方推荐直接用 `npx` 或 `bunx` 启动配置界面。

如果你本机有 [Node.js，可以直接执行：](http://Node.js，可以直接执行：)

```
# 使用 npx 启动 ccstatusline 配置界面。
# -y 表示自动确认安装临时依赖，不需要手动输入 yes。
# @latest 表示使用 npm 上最新发布的 ccstatusline。
npx -y ccstatusline@latest
```

如果你用 Bun，也可以这样：

```
# 使用 bunx 启动 ccstatusline 配置界面。
# bunx 和 npx 类似，都是临时运行 npm 包里的命令。
# 一般 Bun 启动会更快一点，但前提是你本机已经安装了 Bun。
bunx -y ccstatusline@latest
```

命令跑起来之后，会进入一个终端配置界面。

第一次安装时，按提示选择安装到 Claude Code，工具会帮你把 `statusLine` 配置写入 Claude Code 的 `              settings.json            ` 。

如果你不想每次都跟着 `@latest` 自动更新，可以在安装流程里选择 `Pinned global install` 。这样它会把当前版本固定安装到全局，后面直接执行：

```
# 打开已经全局安装好的 ccstatusline 配置界面。
# 适合选择过 Pinned global install 的用户。
ccstatusline
```

这个方式更稳一点，适合日常长期用。

### 配置指南

输入 `ccstatusline` 命令就能配置状态栏：

![图片](assets/%E7%BB%99%20Claude%20Code%20%E8%A3%85%E4%B8%8A%E8%BF%99%E4%B8%AA%E8%B6%85%E9%85%B7%E7%9A%84%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%8C%E9%80%BC%E6%A0%BC%E7%9E%AC%E9%97%B4%E6%8B%89%E6%BB%A1%EF%BC%81/49c3946b4b1b4b27f157b725371eb085_MD5.png)

然后选择「 **Edit Lines** 」项回车，就可以在配置界面里添加、删除、调整状态栏组件：

![图片](assets/%E7%BB%99%20Claude%20Code%20%E8%A3%85%E4%B8%8A%E8%BF%99%E4%B8%AA%E8%B6%85%E9%85%B7%E7%9A%84%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%8C%E9%80%BC%E6%A0%BC%E7%9E%AC%E9%97%B4%E6%8B%89%E6%BB%A1%EF%BC%81/af872e0d2d99b313305c201296474f77_MD5.png)

最多可以添加 3 行状态栏，但是状态栏这东西，信息越多不一定越好，刚开始先保持清爽，后面再慢慢加。

所以，别一上来就塞满一整排。

**我个人最建议先放这几项：**

- • **模型** ：确认当前是不是你想用的模型。
- • **思考程度** ：确认当前模型的思考程度。
- • **Git 分支** ：确认没改错分支。
- • **上下文** ：快满了就及时压缩。
- • **用量** ：避免一不小心把额度干穿。

以下是我自己的配置，供参考：

![图片](assets/%E7%BB%99%20Claude%20Code%20%E8%A3%85%E4%B8%8A%E8%BF%99%E4%B8%AA%E8%B6%85%E9%85%B7%E7%9A%84%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%8C%E9%80%BC%E6%A0%BC%E7%9E%AC%E9%97%B4%E6%8B%89%E6%BB%A1%EF%BC%81/8bd645f34953e3abbbcfe2012031b72c_MD5.png)

如果你喜欢更酷一点的终端风格，可以打开 Powerline 模式：

![图片](assets/%E7%BB%99%20Claude%20Code%20%E8%A3%85%E4%B8%8A%E8%BF%99%E4%B8%AA%E8%B6%85%E9%85%B7%E7%9A%84%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%8C%E9%80%BC%E6%A0%BC%E7%9E%AC%E9%97%B4%E6%8B%89%E6%BB%A1%EF%BC%81/8719e97306fcfb52f786539e1015f636_MD5.png)

效果如下图所示：

![图片](assets/%E7%BB%99%20Claude%20Code%20%E8%A3%85%E4%B8%8A%E8%BF%99%E4%B8%AA%E8%B6%85%E9%85%B7%E7%9A%84%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%8C%E9%80%BC%E6%A0%BC%E7%9E%AC%E9%97%B4%E6%8B%89%E6%BB%A1%EF%BC%81/8cf99b952d496e009320c83ea7549508_MD5.png)

不过我个人还是喜欢简洁点的，所以就没开 Powerline。

ccstatusline 会往 Claude Code 的配置里写入类似这样的内容：

```
{
  "statusLine": {
    // type 表示 Claude Code 要执行一个命令来生成状态栏。
    "type": "command",

    // command 是实际执行的命令。
    // 这里用 npx 运行 ccstatusline，由它读取会话 JSON 并渲染状态栏。
    "command": "npx -y ccstatusline@latest",

    // padding 控制状态栏左右缩进。
    // 设为 0 一般就够了，终端空间比较紧张时更清爽。
    "padding": 0,

    // refreshInterval 控制定时刷新间隔，单位是秒。
    // 比如显示时钟、用量重置倒计时这类信息时，定时刷新会更自然。
    "refreshInterval": 10
  }
}
```

这段不用你手写，走正常安装流程就行。

我放出来主要是为了让你知道它到底改了哪里。以后如果状态栏不显示，排查方向也很明确，可以先看 Claude Code 的 `              settings.json            ` 里有没有 `statusLine` 。

配置文件一般在这里：

```
# Claude Code 用户级配置文件。
~/.claude/
            settings.json
```

ccstatusline 自己的配置一般保存在：

```
# ccstatusline 自己的样式和组件配置。
~/.config/ccstatusline/
            settings.json
```

以下是我自己的配置，供参考：

```
{
  "version": 3,
  "lines": [
    [
      {
        "id": "1",
        "type": "model",
        "color": "cyan"
      },
      {
        "id": "9bf7b6cb-12ae-4380-8216-cc70f7560ac1",
        "type": "thinking-effort"
      },
      {
        "id": "8c3eb2c4-15b4-472d-a1fa-125f8d009166",
        "type": "context-percentage"
      },
      {
        "id": "b0be5bdf-ad50-4e13-851f-59fb8174a345",
        "type": "git-branch"
      },
      {
        "id": "753b91ae-e939-44a4-bb70-b5412542f8e6",
        "type": "remote-control-status"
      }
    ],
    [
      {
        "id": "60a232da-9b74-43de-98d9-13c0753615fd",
        "type": "session-usage"
      },
      {
        "id": "98a1cd66-9da3-4753-8977-3525d042e2c5",
        "type": "reset-timer"
      },
      {
        "id": "7a0141be-d512-415c-84d3-2a8917875446",
        "type": "weekly-usage"
      },
      {
        "id": "0e449124-c3e7-483b-8f3a-13167b55fb59",
        "type": "weekly-reset-timer"
      }
    ],
    []
  ],
  "flexMode": "full-minus-40",
  "compactThreshold": 60,
  "colorLevel": 2,
  "defaultPadding": " ",
  "inheritSeparatorColors": false,
  "globalBold": false,
  "gitCacheTtlSeconds": 5,
  "minimalistMode": false,
  "powerline": {
    "enabled": false,
    "separators": [
      ""
    ],
    "separatorInvertBackground": [
      false
    ],
    "startCaps": [],
    "endCaps": [],
    "theme": "custom",
    "autoAlign": false,
    "continueThemeAcrossLines": false
  },
  "installation": {
    "method": "auto-update",
    "packageManager": "bun"
  },
  "defaultSeparator": "|"
}
```

所以，也可以通过这个配置文件，进行添加、删除、调整状态栏组件。

### 如何禁用

可以通过 `ccstatusline` 命令移除 Claude Code 的 `statusLine` 配置，或者直接把 `              settings.json            ` 里的 `statusLine` 删除。

如果只想临时禁用，建议改配置文件，把 `~/.claude/             settings.json           ` 中的 `statusLine` 删除，或者改名即可：

```
"statusLine": {
    "type": "command",
    "command": "bunx -y ccstatusline@latest",
    "padding": 0,
    "refreshInterval": 10
}
```

比如，改成 `statusLine1` 状态栏就消失了。

## 2、claude-hud

claude-hud 也是最近比较火热的状态栏工具，功能和 ccstatusline 类似，但配置略微复杂一些，状态栏的配置也没有 ccstatusline 灵活。

开源地址：

> [https://github.com/jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)

![图片](assets/%E7%BB%99%20Claude%20Code%20%E8%A3%85%E4%B8%8A%E8%BF%99%E4%B8%AA%E8%B6%85%E9%85%B7%E7%9A%84%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%8C%E9%80%BC%E6%A0%BC%E7%9E%AC%E9%97%B4%E6%8B%89%E6%BB%A1%EF%BC%81/fb5cd904a7a1ed7d66c13d5547f2defe_MD5.png)

### 安装方法

**步骤 1：添加市场**

> /plugin marketplace add jarrodwatts/claude-hud

**步骤 2：安装插件**

> /plugin install claude-hud

安装完成后，重新加载插件：

> /reload-plugins

### 配置指南

使用下面的命令配置：

> /claude-hud:setup

![图片](assets/%E7%BB%99%20Claude%20Code%20%E8%A3%85%E4%B8%8A%E8%BF%99%E4%B8%AA%E8%B6%85%E9%85%B7%E7%9A%84%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%8C%E9%80%BC%E6%A0%BC%E7%9E%AC%E9%97%B4%E6%8B%89%E6%BB%A1%EF%BC%81/ae3deb891fee7b60d76ceb3e217c55e5_MD5.png)

这个命令要和大模型进行交互，所以配置起来比较慢，而且不是固定的格式，命令后面可以跟自然语言，比如你想怎么定制这个状态栏，就直接告诉它。

原理都是一样的，claude-hud 也会往 Claude Code 的配置里写入 `statusLine` ，然后通过它自己的命令来渲染状态栏。

**claude-hud 的配置文件路径为：**

> ~/.claude/plugins/claude-hud/ [config.json](http://config.json/)

以下是我自己的配置，供参考：

```
{
  "lineLayout": "expanded",
  "showSeparators": false,
  "elementOrder": ["project", "context", "usage", "addedDirs", "promptCache", "memory", "environment", "tools", "skills", "mcp", "agents", "todos", "sessionTime"],
  "display": {
    "showModel": true,
    "showContextBar": true,
    "showTools": false,
    "showAgents": true,
    "showTodos": true,
    "showProject": false,
    "showConfigCounts": false,
    "showTokenBreakdown": true,
    "showSpeed": false,
    "showUsage": true,
    "usageBarEnabled": true,
    "showSessionName": false,
    "showDuration": true,
    "showAddedDirs": false,
    "customLine": "",
    "showEffortLevel": true,
    "mergeGroups": [["project", "context"]]
  },
  "gitStatus": {
    "enabled": true,
    "showDirty": false,
    "showAheadBehind": false,
    "showFileStats": false
  }
}
```

效果如下：

![图片](assets/%E7%BB%99%20Claude%20Code%20%E8%A3%85%E4%B8%8A%E8%BF%99%E4%B8%AA%E8%B6%85%E9%85%B7%E7%9A%84%E7%8A%B6%E6%80%81%E6%A0%8F%EF%BC%8C%E9%80%BC%E6%A0%BC%E7%9E%AC%E9%97%B4%E6%8B%89%E6%BB%A1%EF%BC%81/7c3ccad08edec08febeae14dc54830e3_MD5.png)

### 如何禁用

和 ccstatusline 一样，可以通过 `/plugin uninstall claude-hud` 卸载插件，或者直接把 `~/.claude/             settings.json           ` 中的 `statusLine` 删除或者改名。

如果想临时关闭，官方也提供了环境变量 `CLAUDE_HUD_DISABLE` ，启动 Claude 时进行设置：

> CLAUDE\_HUD\_DISABLE=1 claude

这样启动 Claude 后，即可在本次会话中关闭 HUD，无需从 `              settings.json            ` 中移除 `statusLine` 配置。不设置（或设为否定值： `0` 、 `false` 、 `off` 、 `no` ）则保持 HUD 启用。

## 写在最后

Claude Code 本身已经很强了，但它毕竟跑在终端里，信息密度很高。你一边让它改代码，一边还要盯着模型、上下文、目录、分支、成本、用量，时间一长，人就容易麻。

所以这一类状态栏的价值就是， **把这套能力包装成了一个可配置的终端 UI，把一些关键状态常驻显示出来** ，不用你反复敲命令确认。

如果你也在重度使用 Claude Code，可以试试这类工具，因为 Claude Code 已经很强了，给它再装个好状态栏，就更强大了。

总的来说， **ccstatusline** 是最灵活、最简单、最炫酷的，官方的 `/statusline` 命令和 `claude-hud` 工具配置起来略微复杂，大家可以根据自己的喜好选择。

未完待续，R哥会继续分享更多 Claude Code、AI 编程的实战干货，关注「 **AI技术宅** 」公众号和我一起学 AI。

> ⚠️ **版权声明：**
> 
> 本文系公众号 "AI技术宅" 原创，未经授权禁止转载，严禁搬运、抄袭、洗稿、侵权一律投诉，并保留追究其法律责任的权利。

< END >

推荐阅读：

[GPT-5.6 出大事了，会清空电脑所有文件！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487906&idx=1&sn=4ba81e98fe2b03b048b68ee532dcc6dd&scene=21#wechat_redirect)

[重磅：Codex 宣布取消 5h 用量限制！！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487878&idx=1&sn=142247a5b6487bcca8b4def4e2f74ed4&scene=21#wechat_redirect)

[突发！阿里全面禁用 Claude Code！！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487827&idx=1&sn=5f71cca460f76b17e6cc16a61f0f9bb6&scene=21#wechat_redirect)

[从夯爆到夯，锐评 7 个主流 AI 编程模型！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487663&idx=1&sn=0b7de8d3f7a2a6ed1673746d31d57713&scene=21#wechat_redirect)

[Claude 封号的原因终于被人找到了！！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487816&idx=1&sn=2836d8b1d88794d69bb96131b233108d&scene=21#wechat_redirect)

[Claude Code 成本爆降 92% 开源工具！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487651&idx=1&sn=a7e7c1b4bee4061bd84c47d96f8c59b4&scene=21#wechat_redirect)

[Claude Code 命令大全（2026 最新版！）](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487805&idx=1&sn=7ce88b8eeabe31f31af93528806b3291&scene=21#wechat_redirect)

[Claude Code 最佳实践开源，一网打尽！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247487757&idx=1&sn=1ebdb09e42a9620c1c49b437fe393f8a&scene=21#wechat_redirect)

[玩转 Claude Code 的 23 个实用小技巧！](https://mp.weixin.qq.com/s?__biz=MzU0OTc0NzAxMg==&mid=2247485524&idx=1&sn=dfabb331208e1b3cef651ec766c9f618&scene=21#wechat_redirect)

更多 ↓↓↓ 关注公众号 ✔ 标星⭐ 哦