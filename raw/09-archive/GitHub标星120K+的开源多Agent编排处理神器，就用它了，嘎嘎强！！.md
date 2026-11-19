---
title: "GitHub标星120K+的开源多Agent编排处理神器，就用它了，嘎嘎强！！"
source: "https://mp.weixin.qq.com/s/54qqxbJ9ZmOlpkSudZpRvg"
author:
  - "[[冰v河]]"
published:
created: 2026-11-19
description: "这个GitHub标星120K+的开源神器能让多个 Agent 并行处理任务，真的很强！\x0d\x0ahttps://binghe.site"
tags:
  - "clippings"
---
冰v河 冰河技术 *2026年11月19日 07:45*

**大家好，我是冰河~~**

终端开多了之后，问题往往不是机器跑不动，而是人开始记不住。一个窗口在跑测试，一个在改页面，还有一个在翻文档，切来切去，过一会儿连哪个任务在哪个标签页里都要想一下。

![图片](assets/GitHub%E6%A0%87%E6%98%9F120K+%E7%9A%84%E5%BC%80%E6%BA%90%E5%A4%9AAgent%E7%BC%96%E6%8E%92%E5%A4%84%E7%90%86%E7%A5%9E%E5%99%A8%EF%BC%8C%E5%B0%B1%E7%94%A8%E5%AE%83%E4%BA%86%EF%BC%8C%E5%98%8E%E5%98%8E%E5%BC%BA%EF%BC%81%EF%BC%81/21135dfa0484b6c5c82889f4daa46573_MD5.webp)

Orca 想处理的正是这一层：它不生产模型，也不替代你惯用的 Agent，而是把多个编码 Agent 的会话、工作目录和审查动作收进一个桌面应用里。

项目是 MIT 协议，创始团队有 Chrome 和 Uber 的背景，后来做了 Stably AI。仓库热度不低，更新也比较频繁。它支持 Claude Code、Codex CLI、OpenCode、Cursor CLI 等常见 Agent，桌面端之外还有移动端。

## 它先解决的是“找窗口”，但真正省事的不止这一点

Orca 的界面很直白：左侧是一列 Agent 会话，点哪个，右侧就切到哪个。每个 Agent 仍然在自己的环境里跑，但用户不需要关心这些环境散落在哪里，看到的是一份统一列表。

![图片](assets/GitHub%E6%A0%87%E6%98%9F120K+%E7%9A%84%E5%BC%80%E6%BA%90%E5%A4%9AAgent%E7%BC%96%E6%8E%92%E5%A4%84%E7%90%86%E7%A5%9E%E5%99%A8%EF%BC%8C%E5%B0%B1%E7%94%A8%E5%AE%83%E4%BA%86%EF%BC%8C%E5%98%8E%E5%98%8E%E5%BC%BA%EF%BC%81%EF%BC%81/d8a9c6aad4426d0f2232aa2cc8ca0a00_MD5.webp)

它的终端基于 Ghostty 那一档的实现，用 WebGL 渲染，分屏可以继续拆。比较实用的细节是：关掉应用再打开，滚动缓冲还在。

前面翻到过的报错不用重新跑命令去复现。这个功能单看不算惊艳，但在排查问题时能省掉不少重复动作。

不过，如果只是把多个终端塞进一个窗口，价值有限。Orca 真正花力气的地方，是它把“会话”和“工作目录”这两件容易互相踩的事一起接管了。

## 自动建 worktree，才是多 Agent 并行的前提

多个 Agent 同时改一个仓库，最怕的是互相覆盖。规范做法是给每个 Agent 一个独立的 git worktree，但手动建目录、配环境、处理端口冲突，一天重复几次就很烦。

![图片](assets/GitHub%E6%A0%87%E6%98%9F120K+%E7%9A%84%E5%BC%80%E6%BA%90%E5%A4%9AAgent%E7%BC%96%E6%8E%92%E5%A4%84%E7%90%86%E7%A5%9E%E5%99%A8%EF%BC%8C%E5%B0%B1%E7%94%A8%E5%AE%83%E4%BA%86%EF%BC%8C%E5%98%8E%E5%98%8E%E5%BC%BA%EF%BC%81%EF%BC%81/84c0f37775a7059840e0886d8e72c23c_MD5.png)

Orca 在新建 Agent 时会自动创建 worktree，Agent 删除时也会清理。官方还演示过一种更激进的用法：同一个提示同时交给五个 Agent，各自在独立 worktree 里跑，结束后把结果摆在一起比较，选最合适的合并。

因为 worktree 共享 git 对象库，磁盘不会因为多开几份就迅速膨胀。这一点我一开始没注意，用了一段时间才发现它确实没有带来明显的存储压力。

换句话说，Orca 把“并行”从一种需要手工维护的操作，变成了新建会话时的默认行为。多 Agent 协作的门槛，很多时候就卡在这一步。

## 批注和 Diff 反馈，把 review 揉进同一个界面

Agent 写完代码，审查环节通常很碎：看 diff，切到聊天窗口描述问题，等它改完，再回来看 diff。

Orca 把反馈入口放到了 diff 旁边。你觉得哪一段不对，直接高亮、写一句意见、发送，Agent 收到后去改。流程没有变短很多，但切换次数少了。

![图片](assets/GitHub%E6%A0%87%E6%98%9F120K+%E7%9A%84%E5%BC%80%E6%BA%90%E5%A4%9AAgent%E7%BC%96%E6%8E%92%E5%A4%84%E7%90%86%E7%A5%9E%E5%99%A8%EF%BC%8C%E5%B0%B1%E7%94%A8%E5%AE%83%E4%BA%86%EF%BC%8C%E5%98%8E%E5%98%8E%E5%BC%BA%EF%BC%81%EF%BC%81/4577584a21c2d7797e99915fb443964d_MD5.png)

它内置的 Markdown 编辑器也有类似思路。写完实时预览，表格、代码块、标题层级都能正常渲染。更好用的是可以在文档上标批注，把多处修改意见打包发给 Agent 统一处理。

让 Agent 写一份很长的 API 文档，然后在上面圈出若干处要改的地方，连描述带批注一起扔回去，等它集中改完，比自己逐条转述要省事。

## 会话能找回来，手机上也能接住

Agent 跑完任务、关掉终端之后，过几天再想找当时的记录，往往很麻烦。Orca 会把所有 Agent 会话存档，对话、diff、改过哪些文件都在，支持关键词搜索。找到旧会话后，可以拖回终端窗口继续聊。

![图片](assets/GitHub%E6%A0%87%E6%98%9F120K+%E7%9A%84%E5%BC%80%E6%BA%90%E5%A4%9AAgent%E7%BC%96%E6%8E%92%E5%A4%84%E7%90%86%E7%A5%9E%E5%99%A8%EF%BC%8C%E5%B0%B1%E7%94%A8%E5%AE%83%E4%BA%86%EF%BC%8C%E5%98%8E%E5%98%8E%E5%BC%BA%EF%BC%81%EF%BC%81/45d8123e39e3d1ce146117f042cba5cf_MD5.png)

移动端是另一个思路的伴侣应用。iOS 在 App Store 搜“Orca IDE”，Android 提供 APK。它能连到本机的 Agent，用来 review diff、编辑文件、查看进度。

下班路上收到通知，翻一遍 diff，标两处要改的地方发回去，家里的电脑接着跑，到家时第二轮可能已经完成。它不适合在手机上写完整项目，但 review、approve、给下一步指令这些动作，手机端够用。

## 一些零碎但实用的能力

Orca 内嵌了一个 Chromium 浏览器，Agent 可以在里面打开网页、跑交互测试、抓 DOM、走端到端流程。

以前 Agent 跑测试只能看终端日志，现在能直接看到页面上的操作。每个 worktree 还能挂一个移动端模拟器，iOS 和 Android 都支持。

对 Claude Code 重度用户来说，账号切换是个很实际的功能。跑到一半限流，可以一键切到另一个账号继续，上下文不会断。前提是你自己得有多个账号，Orca 不提供额度。

其他还包括：拖文件或图片进 Agent 聊天；通过 SSH 连远程机器跑 Agent，带文件编辑、git、终端、自动重连和端口转发。

在应用内打开 GitHub 和 Linear 的 PR、Issue；提供 Orca CLI，Agent 可以调用 `orca worktree create` 、 `snapshot` 、 `click` 、 `fill` 等命令，把流程写进脚本。

设计模式可以在改完前端后直接看效果、圈出要调的地方；全局快速打开能一次搜索 worktree、文件、Agent 和命令。

## 安装和成本要说清楚

桌面客户端从 [https://onorca.dev/download](https://onorca.dev/download) 下载，macOS、Windows、Linux 都有，包体两百多兆。macOS 也可以走 Homebrew，Arch 走 AUR：

```
brew install --cask stablyai/orca/orca
yay -S stably-orca-bin
```

Orca 本身不提供模型。你用的是哪个 Agent、哪份订阅，它就调哪个；所谓“免费”指的是这个壳免费，实际消耗仍然是你自己的 API 或订阅额度。

已经买了订阅的人不算新增成本，一个号都没有的人需要先把这一层准备好。

配置时选择要用的 Agent，填上 API Key 或订阅凭证。新建 Session 后，Orca 会自动开一个 git worktree，之后就和平时在终端里用 Agent 差不多。

左下角敲命令，上面是编辑器和浏览器面板，左边列表切换 Agent，跑完在 Diff 面板里审查。手机端需要另外安装，装完连到桌面 Agent 即可。

## 适合谁，以及一个需要正视的风险

如果平时只用一个大模型问问题，或者根本不常用编码 Agent，Orca 会显得偏重，暂时没必要装。

它更适合已经在日常大量使用 Agent、终端经常开到分不清哪个是哪个的人。它不是 IDE，也不是项目管理工具，定位更像“Agent 会话编排层”。

需要如实说的是，这个仓库目前开放的 issue 4.6K条。功能迭代快是好事，但也说明坑不少，遇到问题是正常的。把它当成一个正在快速演进的工具，而不是一个已经稳定的基础设施，预期会更合理。

项目地址： [https://github.com/stablyai/orca](https://github.com/stablyai/orca)

**好了，今天就到这儿吧，我是冰河，我们下期见~~**

推荐阅读：

[给大家推荐一款AI短剧生成平台](https://mp.weixin.qq.com/s?__biz=Mzg4MjU0OTM1OA==&mid=2247515806&idx=1&sn=6214e0ec2a9ebc09b1c68eb23e818eae&scene=21#wechat_redirect)

[给大家推荐一款可直接使用的AI-CR系统](https://mp.weixin.qq.com/s?__biz=Mzg4MjU0OTM1OA==&mid=2247515790&idx=1&sn=5aeda9e93df686b5e753cb9870fda0da&scene=21#wechat_redirect)

**微信扫一扫赞赏作者**

AI开源合集 · 目录

阅读原文