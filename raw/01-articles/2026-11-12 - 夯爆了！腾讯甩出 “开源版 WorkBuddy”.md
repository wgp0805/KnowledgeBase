---
source_url: "https://mp.weixin.qq.com/s/37JqAllw7y6mgp2AL3rkGA"
title: "夯爆了！腾讯甩出 “开源版 WorkBuddy”"
account: "java1234"
published_at: "2026-11-12 10:55:01"
saved_at: "2026-11-12 11:03:01"
sync_id: "art_b9c6e30aa5aa44c89f90d2546c74039a"
parse_status: "ok"
---

# 夯爆了！腾讯甩出 “开源版 WorkBuddy”

**大家好，我是锋哥。**

> 最近腾讯开箱即用的AI 办公助手WorkBuddy非常火爆，同时也发布了功能类似的开源项目Octop，目前Github星标11.9K。今天锋哥和大家来好好聊聊Octop这个优秀的开源项目。

![](https://mmbiz.qpic.cn/mmbiz_jpg/N3iaBf9dM5ibGlvhKiasYcXfNb9icObs5pHUPML3Yrq7KsibAmBYZzYZ2Peb0ZX1ABHFfUqhNjBic1OW7hHynnAyoBM2CVSZY6MgUWaKt6CJK53B8/640?wx_fmt=jpeg&from=appmsg)

## 目录

- 先来认识下Octop
- 大家为啥叫它开源版 WorkBuddy
- 装上就能开聊
- 三个可以照着试的用法
- 一句话发出去之后去了哪
- 数据躺在自己机器上

## 先来认识下Octop

Octop 是一套能装在你自己电脑、NAS 或云服务器上的 AI 助手。网页能聊，飞书、微信、钉钉、企业微信、QQ、Telegram 也能聊。一套部署可以开好几个账号，家里一人一个，小团队一人一个。每个人下面还能再养几位专家：写周报的、看服务器的、陪孩子记疫苗的，各干各的，记忆和文件分开。

软件免费。模型要自己接，可以用云上的接口，本机 Ollama 也可以。模型调用的费用，还是模型服务商那边算。

下面这张就是运行后的聊天页。左边一列菜单，中间一位“运维工程师”专家，下面是输入框。第一次打开，大概就是这个样子。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N3iaBf9dM5ibG2vPUmFHYFF8EsbMO8UFgTjz6QtSbpl1o21icQzYZk02vgxiaicqOtex5ptBaQfWeL5IlRiabQ4HcNucCeYbufhaz7LM1xlQymDag/640?wx_fmt=jpeg&from=appmsg)

## 大家为啥叫它开源版 WorkBuddy

WorkBuddy 是腾讯云那款开箱即用的 AI 办公助手，登录就能用，模型和算力都在云上。Octop 上能看到不少熟悉的功能，专家、技能、连接器、知识库、定时任务都有，所以大家口头上都叫它“开源版 WorkBuddy”。

官方说法会克制一些。两个都是腾讯云的 AI Agent：WorkBuddy 是已经做好的成品；Octop 面向个人、家庭和小团队，更强调开源、自己部署，而且每个人的专家和工作区是隔开的。

这两条线其实对应两类人。不想折腾安装和密钥的，用 WorkBuddy；希望对话、文件、密钥都留在自己机器上的，就选 Octop。

## 装上就能开聊

个人电脑最省事。Windows 打开 PowerShell：

```bash
irm https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.ps1 | iex
octop init
octop run
```

macOS 和 Linux 是另一条安装命令，装完同样是初始化再启动：

```bash
curl -fsSL https://finnie-1258344699.cos.ap-guangzhou.myqcloud.com/octop/install.sh | bash
octop init
octop run
```

安装器会自己准备 Python 3.12，放在  `~/.octop/`  里，不折腾系统里原来的 Python。 `octop init`  让你设管理员。密码至少 8 位，还得同时有字母和数字。浏览器打开  `http://127.0.0.1:8088`  就能进。

要给同事一起用，或者丢到服务器上一直开着，用 Docker 更合适。国内拉镜像可以走南京大学的镜像：

```apache
docker run -d \
  --name octop \
  -p 8088:8088 \
  -v octop-data:/data/.octop \
  -e HOME=/data \
  -e OCTOP_ADMIN_USERNAME=admin \
  -e OCTOP_DEFAULT_PASSWORD='Passw0rd2026' \
  ghcr.nju.edu.cn/tencentcloud/octop:latest
```

 `Passw0rd2026`  只是个能通过密码规则的例子，上线前换成你自己的。设了合格密码，第一次启动就会建好管理员，说明写在数据卷里的  `credential.txt` 。没设密码的话，网页会走进设置向导，解锁口令在  `octop-login.txt` 。

模型在网页的「管理 → 模型」里加。官方预设了腾讯云、OpenAI、DeepSeek、Ollama 这些。密钥也可以直接写进  `~/.octop/env` ，下次启动就会带上：

```ini
OPENAI_API_KEY=sk-你的密钥
DASHSCOPE_API_KEY=sk-你的通义密钥
```

## 三个可以照着试的用法

### 1. 先换一位对口的专家

装完会留一个默认专家，名字叫  `main` ，先跟它打招呼完全够用。真要拿来干活，去「专家」里挑内置模板更顺手。一位写周报，一位看机器，文件和聊天记录不会搅成一锅。

下面这张图就是专家页。内置模板点一下就能装上。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N3iaBf9dM5ibGfibShs1iaZguC6E5iaLCxsfKFicX0zP2IIsPRLCwsziaYsRQSoO2bvFmIhQ9opyricKl4sREluCF7BYGpV8xgrnuoBFD1Lxt2WpVibE/640?wx_fmt=jpeg&from=appmsg)

比如装上「小办」之后，聊天框里可以直接说：

```markdown
把我这周做的三件事整理成一份周报：
1. 把登录页改成了短信验证
2. 修了导出超时
3. 给新人写了部署说明
语气平实一点，控制在 400 字以内，最后补一条下周要跟进的事。
```

专家的口气还能换。里面有 16 种 MBTI 人格模板，嫌默认说话太板，就换一种，或者自己做个小测试让它按结果来。

### 2. 让它去翻你自己的资料

连接器就是你授权过一次的应用。腾讯文档、腾讯会议、邮箱、Notion，点一下连上，以后用大白话吩咐。知识库则是你丢进去的 PDF、Word、表格，它回答的时候会标出引用了哪一段。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/N3iaBf9dM5ibGFX2v8V60OGQ8kKFSDzsdVkZYOoNuJd6busm9Odo3u7D9RhaLDAhGtoEZkW1TkVic3bmPfklicCDlL5uChxNiaw15CVh5x3UVGa4/640?wx_fmt=jpeg&from=appmsg)

会议和一份项目方案都接好之后，在飞书里对绑定的那位专家说：

```
看一下我明天的会议，并把知识库里的项目方案整理成 300 字摘要。
摘要里写清：会议时间、我要准备什么、方案里和这次会相关的结论。
```

飞书只负责传话。查会议、翻方案，是专家自己去干的。网页里聊天，效果是同一条路。

### 3. 写代码时把它接到编辑器

已经在用 Zed、OpenCode 这类支持 ACP 的工具，可以让它们调用你这台机器上的专家：

```css
octop acp --agent main
```

反过来也行。在 Octop 网页的 ACP 里配上 OpenCode、Claude Code、CodeBuddy，聊天时把写代码的活交出去。危险操作还会先停下来等你点头，不是放出去就不管了。

定时任务也很好玩。每天早上想收一条待办，就在「任务」里用白话建一条，到点它自己开口，不用你守着网页。

## 一句话发出去之后去了哪

不用先啃源码。网页、聊天软件、定时任务，进来的话都进同一个进程，最后落到同一份数据上。默认数据库是本机 SQLite，人多了、要正经跑了，可以换成 PostgreSQL。中间没有 Redis，也没有一堆要单独养的服务。

![](https://mmbiz.qpic.cn/mmbiz_png/N3iaBf9dM5ibFOYIX7k6HFtiaomjb52ylqzTRKpHNybOnJziaB3GQS6ibvXTFmMLgaqGdlvibKDEYvJdr41kQlonmDNc02BJ2x1SQ4gcPKnI34Ee0/640?wx_fmt=png&from=appmsg)

重启也不可怕。进程起来的时候，会按数据库把专家、通道、定时任务重新拉起来。聊天记录还在原来的目录里。

## 数据躺在自己机器上

对话、专家的工作区、密钥，默认都在  `~/.octop/` 。Docker 部署时，它们在你挂出去的那个数据卷里。容器删掉，卷还在，数据就还在。

目录里常见的是这几样：

| 路径 | 里面是什么 |
| --- | --- |
|  `config.json`  | 端口、数据库这类进程配置 |
|  `octop.db`  | 用户、专家、通道、定时任务 |
|  `secrets/`  | 登录用的密钥 |
|  `agents/`  | 每位专家自己的文件和记忆 |

换电脑之前先跑一次  `octop backup` 。搬走的是你自己的目录。

开源主页：https://github.com/TencentCloud/Octop

[2026年，锋哥又开始收Java+AI大模型编程学员了！目前活动，送AI编程+Python+AI大模型VIP。。](https://mp.weixin.qq.com/s?__biz=MzIxNTAwNjA4OQ==&mid=2247572972&idx=1&sn=b1a5984d81f733dde57e775e57d41ac2&scene=21#wechat_redirect)

#### 最近锋哥录制了一些AI编程视频教程 ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/N3iaBf9dM5ibEIVBvuR0zTd8w0Rfib2V4zaxr8KFuibraGlh4ReWBGTIIzW814cpV89PBhZuaqvQhPtyx9FyMxbicxZkWpRQeVmFktWyILKok174/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=4) 高清视频+源码+领取。

```
扫描下方公众号【小锋学AI 】回复：888，
可获取下载链接
👇👇👇

👆长按上方二维码 2 秒回复「888」即可获取
```

---
原文链接：https://mp.weixin.qq.com/s/37JqAllw7y6mgp2AL3rkGA
