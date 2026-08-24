---
source_url: "https://mp.weixin.qq.com/s/P468jKoeBSE7jBILsdNr3w"
title: "阿里开源的 Agent 项目在 Github 又爆了 ！"
account: "java1234"
published_at: "2026-08-23 09:06:00"
saved_at: "2026-08-23 10:26:43"
sync_id: "art_d7ea1a5e4e0843ee8f0f0a5648c80ac0"
parse_status: "ok"
---

# 阿里开源的 Agent 项目在 Github 又爆了 ！

**大家好，我是锋哥。**

> 最近刷 GitHub 的时候，又看到一个阿里项目冲上热门。名字不花哨，就叫 **Open Code Review**，仓库在 alibaba/open-code-review。点进去一看，star 已经两万出头了，评论区里全是“终于等到官方开源”这种话。它不是又一个会聊天的 Coding Agent。它更像一个专门给人看代码的同事：你改完一堆 diff，它先把该看的文件筛出来，再让模型去翻上下文，最后把意见钉到具体某一行上。今天锋哥和大家好好聊聊这个开源项目。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N3iaBf9dM5ibHBbRmX0lUzPfBpLyzaTVJG4z4sYtQNSiaCCrO4HVVnYcR8ITiaHfiaNricw1YicdcvxHnoAGz9JibhskRCBgYl77Lz3fqeSbws5AytI/640?wx_fmt=jpeg&from=appmsg)

## 目录

- 这波热度从哪来
- 它到底在干什么
- 和普通 AI Review 有啥不一样
- 十分钟上手
- 几个真实一点的使用案例

## 这波热度从哪来

Open Code Review 不是实验室里刚做出来的 Demo。过去两年，它一直是阿里内部的官方 AI 代码评审助手，服务过上万名开发，扫过上百万个真实缺陷。2026 年开源之后，社区反应很直接：终于有一个“专门干 Code Review”的 Agent，而不是把通用聊天机器人硬塞进 PR 里。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N3iaBf9dM5ibESfJlAQIlAkR97ibCr9L7lN7JVkA7le8QSxibJ7ApYziaCVARDZroe4IT8ic7eRbiasYavFcicjwUhiacmg4ugxSPSvwKhpvasHcqW3M/640?wx_fmt=jpeg&from=appmsg)

官方介绍写得很硬核：混合架构、行级评论、内置多语言规则，还兼容 OpenAI 和 Anthropic 协议。翻译成人话就是——工程流程负责不跑偏，模型负责看懂代码。

官网在 open-codereview.ai，协议是 Apache-2.0，想接自己的模型、私有化部署都可以。

## 它到底在干什么

最常见的用法就一句：

```bash
ocr review
```

它会读当前仓库的 Git 改动，把变更文件交给一个带工具调用能力的 Agent。这个 Agent 不只看 diff 那几行，还会读完整文件、搜索仓库、对照其他改动文件，最后吐出带行号的评审意见。

本地改完还没提交？直接  `ocr review` 。两个分支要比差异？ `ocr review --from main --to feature-auth` 。接手一个陌生目录、仓库里也没什么有意义的 diff？换成  `ocr scan` 。

内置规则覆盖 Java、TypeScript、Go、Python、Kotlin、Rust、C++ 等十几种语言，常见坑它都认：空指针、线程安全、XSS、SQL 注入。评论不是“这段写得不太好”这种空话，而是尽量钉到某一行。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N3iaBf9dM5ibGnvzywfGqnQTzsTBkvicnMgVZCQt23nmw7lhavbVdnHKzYpRBvPgarvnulvRcJAE8CjtHG7dPJME7uKnzxHu6oI4NjtoIUrxwI/640?wx_fmt=jpeg&from=appmsg)

## 和普通 AI Review 有啥不一样

用过通用 Agent 做 Review 的人，大概都踩过这几个坑：

- 改动一大，它就开始偷懒，有的文件看，有的文件直接跳过
- 意见说得挺对，行号却对不上，点进去根本不是那一行
- 同样的 PR 跑两次，质量忽高忽低

Open Code Review 的思路很朴素：**不该交给模型的事情，就别交给模型。**

选哪些文件、怎么把相关文件捆在一起、套哪套规则、评论钉在哪一行，这些都由确定性工程模块先做完。模型只负责动态决策：这段代码有没有风险、要不要再翻一下调用方、问题到底算不算真问题。

后面还有一层独立反思：反思模块只看 diff，不看 Agent 刚才搜到的那些上下文，专门用来挡幻觉。听起来有点较真，但评审这事，宁可少报一条，也不要每天给你灌十条文不对题的废话。

官方基准也顺着这个思路走。他们拿 50 个热门开源仓库、200 个真实 PR、80 多位资深工程师标出来的 1505 条问题做对比。同一套模型底下，Open Code Review 的精确率和 F1 明显高于通用 Agent，Token 大概只要九分之一左右。召回会低一点，这是刻意的：先保证报出来的问题靠谱。

流程大概是这样：

![](https://mmbiz.qpic.cn/mmbiz_png/N3iaBf9dM5ibEBQQ9AlLjqsBtSkZmSOY4hMiaVUSNXVCp1hKZOg3iaviaJWGSxjNPXE49dVOoCyNGsvGQQeRVS3ZzMOB4PWUQTrKoKDHtwUAR9bY/640?wx_fmt=png&from=appmsg)

左边保证不漏、不乱、不跑偏，右边负责把代码看明白。两边各干各擅长的事，这就是它和“把整个仓库丢给聊天框”最大的差别。

## 十分钟上手

环境要求不苛刻，Git 2.41 以上就行。安装一句搞定：

-
-

```nginx
# 全局安装，装完就有 ocr 命令npm install -g @alibaba-group/open-code-review
```

然后配置模型。交互式最省事：

-
-
-

```nginx
# 选供应商、填 API Key、选模型，最后自动测连通性ocr config providerocr config model
```

内置了 Anthropic、OpenAI、通义、DeepSeek 这些常见供应商。更喜欢命令行、或者要上 CI，也可以直接写：

-
-
-
-
-
-
-
-
-
-

```bash
# 评审意见改成中文，读起来更顺ocr config set language 中文
# 非交互配置，适合脚本和流水线ocr config set provider dashscopeocr config set model qwen3-maxocr config set providers.dashscope.api_key sk-xxxxxxxx
# 测一下模型通不通ocr llm test
```

配置文件在  `~/.opencodereview/config.json` 。配完进项目目录，直接开审。

## 几个真实一点的使用案例

### 案例一：提交前先自己过一遍

最常用，也最值得养成习惯。改完本地代码，先让它看一眼，再推给同事。

-
-
-
-
-
-
-
-
-
-
-

```bash
cd your-project
# 工作区模式：暂存、未暂存、未跟踪的改动一起看ocr review
# 只看某个提交ocr review --commit abc123
# 中途断了，可以接着跑ocr session listocr review --resume <session-id>
```

举个它很爱抓的例子。下面这段 Java 看起来能跑，但用户名直接拼进了 SQL：

-
-
-
-
-

```typescript
// 登录查询：看起来能跑，其实把用户输入直接拼进了 SQLpublic User findByName(String username) {    String sql = "SELECT * FROM t_user WHERE username = '" + username + "'";    return jdbcTemplate.queryForObject(sql, new UserRowMapper());}
```

这种问题，内置 SQL 注入规则基本不会放过。你本地就能看到类似“请改成参数绑定”的行级意见，不用等同事在 PR 里翻旧账。

### 案例二：给功能分支做一次完整 Review

功能分支要合回  `main`  之前，按 merge-base 把整段差异审一遍：

-
-

```css
# 从 main 分出去之后，feature-auth 上的全部改动ocr review --from main --to feature-auth
```

文件多也不用慌。它会把相关文件捆成一组，比如中英文配置文件会放一起看，每组再开一个子 Agent 并行处理。大 PR 不容易漏文件，速度也比一个模型从头聊到尾快。

想先看看它到底会审哪些文件，别急着烧 Token：

-
-

```css
# 只预览文件筛选结果，不调用模型ocr review --from main --to feature-auth --preview
```

### 案例三：接手陌生目录，直接全量扫描

有些仓库刚 clone 下来，或者某个模块很久没人动，diff 几乎没意义。这时用扫描：

-
-
-
-
-
-

```bash
# 整仓扫描，不依赖 Git 历史ocr scan
# 只扫登录和支付相关目录ocr scan --path src/authocr scan --path src/pay
```

这块特别适合“我刚接手这块代码，先帮我找找雷”。

### 案例四：给项目加一点自己的规矩

内置规则已经覆盖常见语言，但每个团队都有自己的红线。项目根目录放一份  `.opencodereview/rule.json`  就行，还可以提交进仓库，大家共用：

-
-
-
-
-
-
-
-
-
-
-
-
-

```css
{  "exclude": ["**/*.gen.ts", "**/generated/**"],  "rules": [    {      "path": "src/api/**/*.go",      "rule": "所有对外 Handler 必须先校验请求体，再访问字段；涉及事务时，创建后立刻 defer tx.Rollback()。"    },    {      "path": "**/*mapper*.xml",      "rule": "重点看 SQL 注入、参数没绑定、XML 标签没闭合这三类问题。"    }  ]}
```

不确定某份文件套的是哪条规则，可以查：

-

```css
ocr rules check src/main/java/com/example/UserService.java
```

它会告诉你：这条规则来自系统内置、全局配置，还是项目自己的  `rule.json` 。

### 案例五：PR 一开，自动在 GitHub 上留言

本地审着爽，真正省时间的是把它挂到 CI 上。官方提供了现成的 GitHub Action，PR 打开或更新时自动评审，还能直接在 diff 上留行内评论。

把下面这份工作流放到  `.github/workflows/ocr-review.yml` ：

-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-

```bash
# PR 打开或更新时自动评审，并在 diff 上留行内评论name: OpenCodeReview PR Review
on:  pull_request_target:    types: [opened, synchronize, reopened]
permissions:  contents: read  pull-requests: write
jobs:  code-review:    runs-on: ubuntu-latest    timeout-minutes: 30    steps:      - name: Run OpenCodeReview        uses: alibaba/open-code-review@main        with:          llm_url: ${{ secrets.OCR_LLM_URL }}          llm_auth_token: ${{ secrets.OCR_LLM_AUTH_TOKEN }}          llm_model: ${{ vars.OCR_LLM_MODEL }}          llm_use_anthropic: ${{ vars.OCR_LLM_USE_ANTHROPIC }}
```

仓库 Secrets 里填模型地址和 Key，Variables 里填模型名。之后每次开 PR，它都会先看一遍。官方示例还支持在评论区发  `/open-code-review`  手动重审。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N3iaBf9dM5ibFLLwFUeSu1606ibQYT8kV0bzMGzpiaHdOuIZX8k6kUjSFOulZy93yHAibx1ic3U35TdhzWg1ibiacScFmDFKYicdloXKOfe3dT0Rk0hs/640?wx_fmt=jpeg&from=appmsg)

如果你已经在用 Cursor、Claude Code、Codex，也不用换工具。仓库里带了插件和 Skill，可以让这些 Agent 直接调用 OCR 的评审能力。还有一种委托模式：文件筛选和规则匹配仍由 OCR 做，真正调用模型的事情交给你手头那个 Agent，这样就不用再给 OCR 单独配一把 Key。

开源主页：https://github.com/alibaba/open-code-review/

[2026年，锋哥又开始收Java+AI大模型编程学员了！目前活动，送AI编程+Python+AI大模型VIP。。](https://mp.weixin.qq.com/s?__biz=MzIxNTAwNjA4OQ==&mid=2247571915&idx=1&sn=6deb7659b60dc4dc3647a22babe9aad3&scene=21#wechat_redirect)

#### 最近锋哥录制了一些AI编程视频教程 ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/N3iaBf9dM5ibEIVBvuR0zTd8w0Rfib2V4zaxr8KFuibraGlh4ReWBGTIIzW814cpV89PBhZuaqvQhPtyx9FyMxbicxZkWpRQeVmFktWyILKok174/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4) 高清视频+源码+领取。

```
扫描下方公众号【小锋学AI 】回复：888，
可获取下载链接
👇👇👇

👆长按上方二维码 2 秒回复「888」即可获取
```

---
原文链接：https://mp.weixin.qq.com/s/P468jKoeBSE7jBILsdNr3w
