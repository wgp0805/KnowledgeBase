---
title: "官方点名，DeepSeek Harness 的 4 个神级插件。"
source: "https://mp.weixin.qq.com/s/rBlqya41_v0ZrqFunS9xgg"
author:
  - "[[沉默王二]]"
published:
created: 2026-11-12
description:
tags:
  - "clippings"
---
沉默王二 沉默王二 *2026年11月12日 14:34*

大家好，我是二哥呀。

真没想到，DeepSeek Harness 调用官方 API 的日活用户已经涨到了 `154` 万。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/rZm1sEcvdu0gOKNOZooz1nlT4qGHTOH4CSxicYyWBibgWVVtAPYhN4zEq5Lq5VDVvT5TmAd72c2Pk95DFeRvRibH0Hrv2LTqvFfLeVMUwU4jicY/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

这也太猛了。

满打满算，DeepSeek Harness 也没上线几个月啊，一个月还是两个月？第三方插件就已经有 `3.5` 万个了，真的是你爱我爱大家都 AI 啊。

官方还顺带从这么多插件中选出来了 4 个表扬了一番，一起来看看有没有你相中的。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rZm1sEcvdu1joLFwWkO9eNF8jBr6LRFT4fwQgvVnpNyx0K0V46c6twiacHIu5ticTSLwVnibvU0mtc8GIuWa83JVCUsM18UOcouleHdZEhfoNE/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

要是看完觉得不够用，完全可以发挥你聪明脑袋，自己动手创造一个。

## 01、自媒体工作台

现在不是人人都下海做自媒体嘛，反正某知名社区我就见过了很多很多大厂员工来做自媒体账号的。

并且做的风生水起。

那这个自媒体工作台 `dsh-media-desk` 绝对值得装一手，作者是科技博主“蜗牛的科技笔记”。

平时用 Agent 写稿或写视频脚本，往往要在一个会话里来回聊几十轮，初稿、修改意见和分镜全混在聊天记录里，回头再找很费劲。这个插件在左侧栏加了一个独立的工作台，从记录选题、生成稿件到安排发布，都可以在 DeepSeek Harness 里完成。

安装很简单。

打开桌面版，进入左侧栏的“插件”页面，点击右上角的“添加插件”，填入 `dsh-media-desk` ，安装完成后点击“立即启用”。

![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu09FiaicicUN4oaPyXagTsAyEYaFExhFAyjZh0CNpmcicBvHnmTSZ71cvuSFqyss6EOcic0IFekxWVpN9lG1iamy3C2iazibex81oe1l8w/640?wx_fmt=png&from=appmsg#imgIndex=2)

启用后，左侧栏会多出一个“自媒体工作台”入口。第一次进入时里面是示例数据，点击右上角的“示例数据 · 清空”就能清掉。工作台顶部有五个模块：

![自媒体工作台像素风动图：记录选题、一键成稿与对话微调](https://mmbiz.qpic.cn/mmbiz_gif/rZm1sEcvdu2mYIeGcua0CTiaHiciavnHMTaWF8xrUkaiaIPQVZrcOltLVpHfe5mP4gypP0FqCSnD0Zwx1DDY7oaMSFchiaJVfl1ibwIYaUq3x6Xk0/640?wx_fmt=gif&from=appmsg#imgIndex=3)

自媒体工作台像素风动图：记录选题、一键成稿与对话微调

- 灵感：一面灵感墙，可以按卡片或时间线排列，贴入一句话、一个链接或一张图片，就能存成一张选题卡片
- 内容：按灵感、成稿、待发布、已发布四种状态，集中管理所有稿件
- 排期：发布日历，把写好的稿子从右侧拖到某一天，就排好了发布时间
- 复盘：录入已发布内容的数据，把表现好的经验总结成写作规则，还能导出为 Skill
- 风格：内置科技数码、干货教程等 8 个类别共 15 种预设风格，也可以贴入自己的旧稿，提炼出个人风格卡

我把“用一句话讲清 Transformer 的注意力机制”存进灵感墙，点击卡片上的“一键成稿”，右侧的稿件区一次性生成了候选标题、口播正文和分镜脚本。

![图片](https://mmbiz.qpic.cn/mmbiz_gif/rZm1sEcvdu32lwVxhK7HSCXuKXxiaQVANmTo3cGKP6uHfWMMyjBfynrLZhfuPIiaO8DHWZP9iaSNcXTCQvE5X57ETLibr3XuuRvdMweUrgUXCGk/640?wx_fmt=gif&from=appmsg#imgIndex=4)

实测中也发现了一个需要注意的地方。

插件本身不带生图服务的密钥，想把封面和 6 个分镜生成图片，需要在设置里填入一个兼容 OpenAI 接口格式的生图 API Key。

## 02、归藏设计

平时让 Agent 写网页或做 PPT，每次生成的配色和字号都不一样，跟开盲盒似的。

`dsh-guizang-design` 把五个常用的内容生成 Skill 和一套统一的配色、排版规范打包进了同一个插件。在“插件”页面安装并启用后，左侧栏会多出“归藏设计”入口。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rZm1sEcvdu1bHGwyIf1jXTGPSDBOTxIX5vPiaDU0RNBN65tfYAFrYg8CDsgOP7OJOzBgVWmIibONmMsQBICV4OyTdia8Wb77aBnKZkLJl0haXs/640?wx_fmt=png&from=appmsg#imgIndex=5)

在会话输入框里输入 `/` 就能看到这五个 Skill，也可以在插件面板里点击对应的卡片启动：

![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu1rbF0PVTk4nVjtjINVwjNeiaHD5jhVgaLvHDa8zRFXonGAK25LUnNkibAG93nAKpNxVZp3WciaCsztsoHS4Coc7EPgwdwtWcbZ7s/640?wx_fmt=png&from=appmsg#imgIndex=6)

- 网页 PPT：对应 `/guizang-ppt-skill` ，生成单个 HTML 文件的演示稿，支持左右翻页、演讲者视图和讲稿备注
- 网页排版：对应 `/guizang-page-skill` ，把文章排成杂志风或瑞士风的单页网页，支持导出 PDF 和长图
- 去 AI 味：对应 `/humanizer-zh` ，删掉中文稿件里的空话、套话和生硬的排比句，保留核心事实和原来的语气
- 语气档案：对应 `/guizang-voice` ，从历史会话和旧文章里总结你的用词、句子长短和标点习惯

前三个负责视觉的 Skill 共用同一套设计规范，内置墨水经典、靛蓝瓷等 6 套杂志风主题，以及克莱因蓝、柠檬黄等 4 套瑞士风主题。

实测时我打开“归藏设计”，选择“网页排版”，发了两句讲注意力机制的文字，让它生成一个单页网页。

![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu0SkzpO4nHtkoia0iayvYOqYoulat3Vibr1QjCM0vwGba27LicxzL4bZxKibMfDESPU0ia3MRqm31jRT3g2BXBu8a0ZxdrF8Vw9SVgRA/640?wx_fmt=png&from=appmsg#imgIndex=7)

## 03、上下文洞察

平时在会话输入框下方，只能看到一个 Token 总数和一个百分比圆环。

至于这一轮为什么涨到了十几万 Token，是历史对话太长、读取的文件太大，还是工具定义占了大头，界面上看不出来。

![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu1LHMkicxCXqsTsb8R9MyMlJt5c1lozLJ9qQcTMicxCjuXkCbWDCuAkrGbpJGMUN62WvtLrK0I3VoWAciaN0w7s8CnKQFVaKc7Lf0/640?wx_fmt=png&from=appmsg#imgIndex=8)

Bowen 开发的 `dsh-context` 就是来解决这个问题的，它会把 Token 花在了哪里一项项列出来。

在插件页面搜索 `dsh-context` ，安装并启用即可。它提供了四个查看入口：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rZm1sEcvdu13LGeQX1414RgRiczibL1ORHdic4WB3joAjJibxLqCaYKS4icexhA8rdoUNpeSD09fBzmcd2mnHNw5BPMdmmVDtr80TdFR5ZUp6c54/640?wx_fmt=png&from=appmsg#imgIndex=9)

- 上下文洞察页面：在左侧导航栏，汇总所有会话的数据，展示最近 7 天计费的 Token 数和预估费用、最近 8 周的使用热力图，以及每个会话的卡片
- Context 标签页：在单个会话的顶部，展示这个会话的 Token 构成、每次请求的 Token 变化、读写过的文件和执行过的命令
- Fleet 标签页：也在单个会话的顶部，用实时更新的卡片展示主 Agent 和各个子 Agent 之间的分工，以及各自的 Token 消耗
- `/context` 命令：在输入框输入 `/context` 并回车，不用离开当前对话，就能在弹窗里查看上下文构成

我用 `dsh-context` 打开刚才生成《一句话理解注意力》网页的那个会话，切到 Context 标签页，马上就看出了 Token 主要花在哪里。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rZm1sEcvdu0pMxVJWMKeYUM0kdpukusntP49c6b2IiaLo1DiciajedeiaEibqmBpHyJqe6OJeASR80m0DZt9sg7IuuoQBMDfxcnfF0YSV8nXicjIA/640?wx_fmt=png&from=appmsg#imgIndex=10)

## 04、论文阅读

这个对于要做论文的同学，可就太有用了。

比如说你想阅读 Transformer 的原始论文《Attention Is All You Need》。

![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu086o30xucvz84Nb20QmYHQlQofEQBfRsGNNm0OhiaVtDD9RloQ1voJYDibdVAWUgrr9uEeuKBicg6tObPNxY691YpVB9Mw8q5B0Q/640?wx_fmt=png&from=appmsg#imgIndex=11)

可以用 Phil-Fan 团队开发的 `agentero-dsh` ，这是一个论文阅读和科研插件。

它把科研工具 Agentero 接进了 DeepSeek Harness 客户端，Agentero 的特点是所有数据都存在本地。插件由四个模块组成，分别负责和客户端通信、管理文献库、记笔记和阅读 PDF。装好后，窗口中间是和 Agent 对话的区域，右侧是文献库、PDF 阅读器和笔记面板。

![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu34p7LSslZmOjlwbryrSYHq1rwA7ibibPcaWEYov8fFj1EsZMSfYEpZ39RubcTf6x2dn6iazLyddrWyib6cCN0JWwRntaSgeJyOL1A/640?wx_fmt=png&from=appmsg#imgIndex=12)

`agentero-dsh` 比前三个插件多一步环境准备，按下面三步来：

- 安装插件：要求本机 [Node.js](http://node.js/) 版本不低于 `24.9.0` ，在桌面版的“插件”页面添加 `agentero-dsh` 并启用
- 安装 Agentero CLI：打开插件的配置项，点击 Agentero CLI 右侧的“安装”按钮，插件会自动下载适合当前系统的官方 CLI，并填好路径
- 绑定本地知识库：在设置里点击“新建知识库”或“选择目录”，指定一个本机文件夹来存放论文

导入的 PDF、高亮标注和笔记都保存在这个文件夹里。

## 05、自动化终端插件

看完这四个插件，我手里也很痒。

于是就顺手搞了一个自动化终端插件 paiwarp-dsh，可以用自然语言描述你的需求，让 DeepSeek Harness 驱动插件帮你做终端命令的输入、截图、录屏。

完全自动化。

平常像 Codex、Claude Code、DeepSeek Harness 都是没办法直接驱动终端的，没有 terminal use。

![通用 PaiWarp 已经在桌面启用](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu0yqrBHSZmHD3GxiaSibPxB5NmDzfaSRTfCBkmXWXQdYkC2k05akMrMvicm07FwOBK5NnWg3Pvx01yMX4ia0S5icxmRPqVh8hjdcRVU/640?wx_fmt=png&from=appmsg#imgIndex=13)

通用 PaiWarp 已经在桌面启用

`paiwarp-dsh` 不限定项目，无论是 Java 写的 `PaiCLI` 、Python 脚本，还是带彩色进度条的构建任务，都可以用自然语言让 DeepSeek Harness 打开本机的真实终端，一步步输入命令或按键，读取屏幕上的输出，检查程序的退出码和生成的文件，同时自动保存高清 PNG 截图和 MP4 录屏。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/rZm1sEcvdu3EWZ237a9RAleUeIHEr0SBHCkrrJrmSKFQ8zehT9HXZ70IJPuY0wnOZxFs5MlMRcicHBFWHTxYZW0DUpmwO98DgNRUFclOiaq4s/640?wx_fmt=gif&from=appmsg#imgIndex=14)

想自己试试 `paiwarp-dsh` ，按下面四步操作即可：

- 克隆源码并安装 Python 依赖：执行下面的命令，装好 Playwright 和 Chromium；如果要录制 MP4，还需要用 `brew install ffmpeg` 装上 FFmpeg
```
git clone 
            https://github.com/itwanger/paiwarp-dsh.git
          
cd paiwarp-dsh
python3 -m venv .venv
.venv/bin/python -m pip install playwright
.venv/bin/python -m playwright install chromium
.venv/bin/python lib/
            doctor.py
```
- 启动桌面端：在 `paiwarp-dsh` 目录下执行下面的命令启动
```
open -a "DeepSeek Harness" \
  --env "PAIWARP_PYTHON=$PWD/.venv/bin/python" \
  --env "PATH=$PATH"
```
- 安装插件：打开桌面端的“插件 → 添加插件”，填入 `paiwarp-dsh` 目录的绝对路径，安装后点击“立即启用”
- 开始测试：在标准模式下打开要测试的项目目录，在右侧栏点开 **PaiWarp** 面板，面板顶部有“终端”和“素材”两个页签
![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu0P7DwBtHqkIHBcibyA92ibibxAT3ypcM0x0KxrucjLWhvOadpzibXiaKX3CuLbzzqKibb1Z5x8Mtv85ibcRBYIHUjL1TtNibuluEQrC0g/640?wx_fmt=png&from=appmsg#imgIndex=15)

可以先用插件自带的示例练手。

新建一个目录，把 `examples/python-cli/` 下的 `              todo.py            ` 和测试说明 `              CASE.md            ` 复制进去，把这个目录作为工作区打开，然后在对话框里发送下面这段提示词。

```
请按当前工作区 
            CASE.md，用
           PaiWarp 在真实 Bash 终端逐步测试 
            todo.py。
          
根据现场输出决定下一步，验证 JSON 文件、错误输入和程序重启后的状态，
保存关键截图与完整录像，最后关闭本次终端，报告真实结果和素材位置。
```

发出后，DeepSeek Harness 会自动打开一个真实的 Bash 终端并开始录屏，然后根据屏幕上的实际输出，依次输入 `add 买咖啡` 、 `add review pull request` 、 `done 1` 、 `list` ，最后输入 `done 99` ，测试编号不存在时程序能否正确报错。

![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu3nuk3wepbpL2MvkocYJibaX4p3Pm42ciaumKSOlT2c2g0Y69J0unoQqg4B3fcTiaT22bkzpuMKiaefQE5QQ2ibm1Yvt8oRTNE1OoaE/640?wx_fmt=png&from=appmsg#imgIndex=16)

Agent 操作终端时，右侧栏的“终端”页签会实时显示彩色画面。中途想自己敲几条命令，可以随时点击面板上的“接管键盘”，插件会立刻暂停 Agent，不再接受它的输入，改由你来操作；敲完再点“交回 Agent”，Agent 会从当前状态接着往下测。

![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu3DbO9sqVwib1HEvRciaYv6VNgUPZme8ootvdgOyuYQ5Lib1AJZN8oTpU8cAknMlHHJb4MWlYv11XMeLPPFzcO627YIERFCHF5MicQ/640?wx_fmt=png&from=appmsg#imgIndex=17)

所有截图、录像和检查报告都保存在工作区的 `.paiwarp/runs/<运行编号>/` 目录下。

![在 Harness 素材页播放真实终端录像](https://mmbiz.qpic.cn/sz_mmbiz_png/rZm1sEcvdu38uGxw0p4MtcQavbalfHicpXbnVahgia7VKf66y3ocdxyZJvvialORy5ic4p8UH2wBT2apunDhc28tRXWBJxic9ElEDHLpqZ1W4wt0/640?wx_fmt=png&from=appmsg#imgIndex=18)

在 Harness 素材页播放真实终端录像

## ending

Agent 时代的操作系统。

搞完这五个插件，我对 DeepSeek Harness 官方这句话有了更具象化的理解。

换句话说，你可以把 DeepSeek Harness 定制成任何你想要它成为的样子，任何你之前繁琐的工作流都可以借助它来完成。

就像之前，我测试 PaiCLI 是用终端自己敲命令完成的，现在让 DeepSeek Harness 帮我直接完成自动化测试，并收集好证据。

命令不用敲了，截图不用截了，AI 直接搞定。

![图片](https://mmbiz.qpic.cn/mmbiz_png/rZm1sEcvdu1s5rBk4ma9hiakibR88NsvHyVwnGHiakOaDkEq0KcEPZbu7XsD8R6czh4k6ZdSI1rjbKrT1X6SwNuOc2siajXpDe8JKhGcSST6HoU/640?wx_fmt=png&from=appmsg#imgIndex=19)

我们下期见。

AI编程进阶之路 · 目录

作者提示: 个人观点，仅供参考