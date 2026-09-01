---
title: "一个SKILL.md拿下2.3万Star：让Codex/ClaudeCode少说废话、先给答案"
source: "https://mp.weixin.qq.com/s/rSJQHy1EIIHbDFljySVA2A"
---
## 一个 SKILL.md拿下2.3万Star：让Codex/ClaudeCode少说废话、先给答案

我是程序汪 *2026年9月1日 09:52*

**程序汪大量接私活案例： [程序汪接私活项目目录，2026年总结](https://mp.weixin.qq.com/s?__biz=MzA4NzQ0Njc4Ng==&mid=2247520080&idx=1&sn=da5201e8b5503122cfb022ea27bcd7ef&scene=21#wechat_redirect)**

用 Coding Agent 改代码，最磨耐心的情况之一，就是它明明答对了，答案却藏在一堆废话里。

你让 Codex 排查一个接口为什么返回 `401` ，它可能先查认证流程，再分析中间件、Token 和 Cookie，顺手提醒你依赖版本也该升级了。全部看完之后，真正要执行的命令只有一条。

任务再长一点，人更容易跟丢。Agent 写了很多，却没说现在做到第几步；测试失败了，也没告诉你先看哪个文件。最后再来一句“希望这能帮到你”，问题还停在原地。

前几天技术群里有朋友分享了一个名字很有意思的项目 **i-have-adhd** ，被名字吸引打开，发现刚好能够解决前面提到问题。

它给 Coding Agent 加了一套回答规则： **第一行先放行动，多步骤任务编号，报错直接写位置和原因，每轮重新交代进度，结尾只留一个明确的下一步。**

![图片](assets/%E4%B8%80%E4%B8%AASKILL.md%E6%8B%BF%E4%B8%8B2.3%E4%B8%87Star%EF%BC%9A%E8%AE%A9CodexClaudeCode%E5%B0%91%E8%AF%B4%E5%BA%9F%E8%AF%9D%E3%80%81%E5%85%88%E7%BB%99%E7%AD%94%E6%A1%88/cc3ffec72ad0e14ecc302e9c0a615728_MD5.webp)

i-have-adhd GitHub 仓库

截至发文，这个项目在 GitHub 上已经有约 **23.9K Star、1.5K Fork** ， MIT 协议。

## i-have-adhd 是什么？

`i-have-adhd` 是一套给 Coding Agent 使用的输出规则。

你可以把它理解成 Agent 的回答规则。模型还是原来的模型，读代码、改文件和执行命令的工具也没有变化。Skill 主要通过一组指令调整回答顺序、步骤长度、进度表达和错误说明方式，让你先看到接下来该做什么。

它的核心写在一个 `              SKILL.md            ` 文件里。

![图片](assets/%E4%B8%80%E4%B8%AASKILL.md%E6%8B%BF%E4%B8%8B2.3%E4%B8%87Star%EF%BC%9A%E8%AE%A9CodexClaudeCode%E5%B0%91%E8%AF%B4%E5%BA%9F%E8%AF%9D%E3%80%81%E5%85%88%E7%BB%99%E7%AD%94%E6%A1%88/ff2b0c0dbd2f7aedf54e3eb78e71eefd_MD5.png)

核心原理其实非常简单，直接看 [SKILL.md](http://skill.md/) 里面写了啥就行了，其实就 10 条规则，可以分成四组：

- **先行动** ：第一行先给答案或下一步行动；如果答案里有命令、路径或代码片段，就把它们放在解释前面。
- **说进度** ：复杂任务拆成编号步骤，每轮说明已经完成什么。
- **讲具体** ：用明确的单位估算时间，报错写明位置、原因和修复动作。
- **删干扰** ：列表不超过 5 项，不写客套开场、重复总结和无关支线。
![i-have-adhd 项目 Logo](assets/%E4%B8%80%E4%B8%AASKILL.md%E6%8B%BF%E4%B8%8B2.3%E4%B8%87Star%EF%BC%9A%E8%AE%A9CodexClaudeCode%E5%B0%91%E8%AF%B4%E5%BA%9F%E8%AF%9D%E3%80%81%E5%85%88%E7%BB%99%E7%AD%94%E6%A1%88/feee757587cc95dc93ea45e66a32202e_MD5.png)

i-have-adhd 项目 Logo

这个项目名称还挺有意思的，adhd 是 **Attention-Deficit/Hyperactivity Disorder** 的缩写，也就是多动症的意思。

它不做诊断，也不涉及治疗，只管 Agent 怎么组织回答。项目作者松散参考了 \_The Adult ADHD Tool Kit\_，再把这套思路改成 LLM 能执行的输出规则。

除了 Claude Code，Codex、Gemini CLI、GitHub Copilot、OpenCode、Pi、OMP、Qwen Code 和 Zed 也都有对应的安装方式。你正在用哪个，照着 `              INSTALL.md            ` 里那一段安装就行。

## i-have-adhd 解决了什么问题？

用 Coding Agent 久了，很容易碰到一种情况：它说了不少，你还是不知道先干什么。

一条命令可能藏在两屏解释后面，改哪个文件也要往回找。它顺手给了好几个建议，却没告诉你哪个先做。看完回复，人还得自己把任务重新排一遍。

对话一长，这种感觉更明显。前面改过什么、测试跑没跑、现在卡在哪，散在不同的消息里。

Agent 说一句“已经处理”，你还得追问处理了什么；它说“测试失败”，又得问报错在哪。

`i-have-adhd` 这个项目要解决的就是这些痛点。

它的核心思想是： **能执行的东西先放第一行，事情多了就按顺序列出来。任务没结束，顺手报一下当前进度；出了错，把位置、原因和修法一起说完。**

**它不会让 Agent 突然变聪明。它的目标是减少来回翻屏和追问“然后呢”的次数，让下一步行动更容易被看到。**

![官方 README 中的 Before 与 After 对比](assets/%E4%B8%80%E4%B8%AASKILL.md%E6%8B%BF%E4%B8%8B2.3%E4%B8%87Star%EF%BC%9A%E8%AE%A9CodexClaudeCode%E5%B0%91%E8%AF%B4%E5%BA%9F%E8%AF%9D%E3%80%81%E5%85%88%E7%BB%99%E7%AD%94%E6%A1%88/d78a2ca2abe50c510ff47019a1138547_MD5.png)

官方 README 中的 Before 与 After 对比

## i-have-adhd 有什么亮点？

### 第一屏先出现能执行的东西

很多 Agent 喜欢先证明自己理解了问题。

“这是一个很好的问题”“你的认证流程涉及多个部分”“让我先分析一下”，这些话单独看没什么，连续出现就会把命令往下推。屏幕里塞满了背景，人却还没开始处理问题。

`i-have-adhd` 要求第一行先给答案或下一步行动。如果答案里有命令、文件路径或代码片段，它们会排在解释前面。背景没有被一刀删掉，用户明确要求详细讲解时，Agent 仍然可以完整展开。

这套顺序很适合排错、改配置、补测试这类任务。读者当前只想知道“先动哪里”，没必要先读一篇认证机制小论文。

### 多轮任务不用猜现在做到哪

单轮问答结束就结束了。Coding Agent 经常要连续工作十几轮，任务状态很容易散在前面的聊天记录里。

`i-have-adhd` 要求 Agent 每轮重新说明状态，例如：

> 第 3/5 步已完成：数据库结构已经更新。下一步回填新字段。

如果当前工具带有任务或计划功能，它会优先使用现成的任务列表，每次只保留一个进行中的步骤，不再用一整段话复述计划。

中途去开会，过一会儿再回来，也不必完全依赖前面的聊天记录。按照这套规则，Agent 会在最新一条回复里重新说明当前进度。

### 报错和完成状态都说具体

![i-have-adhd 的 10 条输出规则](assets/%E4%B8%80%E4%B8%AASKILL.md%E6%8B%BF%E4%B8%8B2.3%E4%B8%87Star%EF%BC%9A%E8%AE%A9CodexClaudeCode%E5%B0%91%E8%AF%B4%E5%BA%9F%E8%AF%9D%E3%80%81%E5%85%88%E7%BB%99%E7%AD%94%E6%A1%88/aa8b52364b35f91a28d31e1c8863df65_MD5.png)

i-have-adhd 的 10 条输出规则

“好像出了点问题”没有多少信息， `i-have-adhd` 会要求 Agent 把错误写成下面这种格式：

```
测试失败于 
            auth.spec.ts:42：预期
           200，实际返回 401。
原因：请求缺少认证头。
修复：为请求添加 Authorization: Bearer ${token}。
```

任务做完以后也一样。它不能只说“已经处理好了”，还要具体说明现在哪些内容已经能工作；有合适的验证命令时，再一并给出来。

时间估算也会从“一会儿”“要花些时间”改成“已有测试时约 15 分钟，没有测试时可能需要一个下午”。这个数字仍然只是 Agent 的估算，不能当成计时器，但至少能帮助你决定现在做，还是先放到后面。

### 该解释和确认的时候不会硬压缩

回答短，不代表所有问题都只能用三句话结束。

用户要求“详细解释”或“带我一步步理解”时，Skill 允许 Agent 正常展开，只保留没有客套开场、方便回看等基本格式。

要执行大范围删除、强制推送、数据库迁移这类破坏性操作，确认步骤也不能省。如果连续三轮修复都没有解决问题，Agent 应该停下来指出可能判断错的前提，再问一个诊断问题，而不是继续盲改代码。

输出规则只负责降低阅读负担，不能为了追求短，连必要解释和安全确认一起删掉。

## i-have-adhd 怎么使用？

项目首页现在把下面这句话放在安装部分的最前面。可以把它交给具备网络和文件权限的 CLI Agent，让它参考仓库里的 `              AGENTS.md            ` 选择安装方式：

```
Install the i-have-adhd skill/plugin from 
            https://github.com/ayghri/i-have-adhd,
           refer to the repo's 
            AGENTS.md
           for instructions.
```

如果更喜欢自己执行命令，Codex 和 Claude Code 也有单独的安装方式。

我就是直接让 Codex 帮我安装并测试的：

![图片](assets/%E4%B8%80%E4%B8%AASKILL.md%E6%8B%BF%E4%B8%8B2.3%E4%B8%87Star%EF%BC%9A%E8%AE%A9CodexClaudeCode%E5%B0%91%E8%AF%B4%E5%BA%9F%E8%AF%9D%E3%80%81%E5%85%88%E7%BB%99%E7%AD%94%E6%A1%88/ca05f61ed4248db5319eb77777adac1f_MD5.png)

![图片](assets/%E4%B8%80%E4%B8%AASKILL.md%E6%8B%BF%E4%B8%8B2.3%E4%B8%87Star%EF%BC%9A%E8%AE%A9CodexClaudeCode%E5%B0%91%E8%AF%B4%E5%BA%9F%E8%AF%9D%E3%80%81%E5%85%88%E7%BB%99%E7%AD%94%E6%A1%88/5d6e5fb715547129e5bf3e8450ecad0a_MD5.png)

### Codex

在终端中添加插件市场并安装插件：

```
codex plugin marketplace add ayghri/i-have-adhd --ref main
codex plugin add i-have-adhd@i-have-adhd
```

安装完成后可以检查插件列表：

```
codex plugin list
```

进入 Codex 会话，输入下面的命令启用：

```
$i-have-adhd
```

Codex 安装插件后不会自动开启这套模式，需要显式调用 `$i-have-adhd` 。如果希望所有会话默认使用，可以把官方提供的常驻规则加入 `~/.codex/             AGENTS.md           ` 。

### Claude Code

Claude Code 的安装只有两条命令：

```
claude plugin marketplace add ayghri/i-have-adhd
claude plugin install i-have-adhd@i-have-adhd
```

插件装好后，直接在 Claude Code 中输入 `/i-have-adhd` 。如果当前会话没有识别到新插件，可以先输入 `/reload-plugins` 重新加载。只安装、不调用，回答方式不会发生变化。

确定每个会话都想用，再创建常驻标记：

```
touch ~/.claude/.i-have-adhd-always
```

这个文件存在时， `SessionStart` Hook 会从会话开始就加载规则。当前会话想临时关闭，输入 `stop adhd mode` 或 `normal mode` ；想彻底恢复按需启用，删除标记文件：

```
rm ~/.claude/.i-have-adhd-always
```

keyi先保留按需启用。排错、执行修改和推进长任务时打开；需要讨论方案、讲源码或审文章时，再决定要不要保留更完整的解释。

用上一段时间，确定自己确实喜欢这种回答方式，再设成默认也不迟。

## 总结

这篇文章介绍了 `i-have-adhd` 的定位、输出规则和使用方法。

它用一组面向 Coding Agent 的规则，约束答案与下一步行动的顺序、多步骤任务的进度表达，以及报错、时间估算和完成状态的写法。

文章还整理了项目在 Codex 和 Claude Code 中的安装、启用与常驻配置，并给出了其他支持平台的安装文档入口。

项目地址： **[https://github.com/ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)**

**程序汪大量接私活案例： [程序汪接私活项目目录，2026年总结](https://mp.weixin.qq.com/s?__biz=MzA4NzQ0Njc4Ng==&mid=2247520080&idx=1&sn=da5201e8b5503122cfb022ea27bcd7ef&scene=21#wechat_redirect)**