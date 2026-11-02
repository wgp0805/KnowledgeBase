---
source_url: "https://mp.weixin.qq.com/s/f_S-1gU2uT1Hi3dEqHjykQ"
title: "给ClaudeCode装上这个超酷的状态栏，逼格瞬间拉满！"
account: "终码一生"
published_at: "2026-10-31 23:27:09"
saved_at: "2026-11-02 07:34:07"
sync_id: "art_625d229106d04b91841c9a79c4f798d6"
parse_status: "ok"
---

# 给ClaudeCode装上这个超酷的状态栏，逼格瞬间拉满！

点击“终码一生”，关注，置顶公众号

每日技术干货，第一时间送达！

用Claude Code久了，有一个痛点一直让我不太舒服——你没法直观地看到它的运行状态。

当前在用哪个模型？上下文吃了多少？这个会话花了多少钱？现在在哪个分支上？全是两眼一抹黑。想知道这些信息，得一条一条敲命令去查。

尤其现在一些Coding Plan用量消耗比较快，工作时间段还有倍率什么的。如果你用的是朋友的套餐，大量使用的时候总得时不时去查一下用量，生怕某个时间段超了，影响别人正常使用。

GitHub上有个开源工具叫ccstatusline，正好完美解决了这个问题。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=0)

01

它是什么？

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg#imgIndex=1)

ccstatusline是给Claude Code CLI做的终端状态栏工具。它把模型名称、Git分支、Token用量、上下文占用、费用估算、实时速度这些数据，全部实时显示在终端底部。

GitHub上已经9k+ Star，版本迭代到了v2.2.19，更新挺勤快的。

它有个交互式的TUI配置界面，70个组件随便挑、随便排位置，还支持Powerline主题，终端颜值直接拉满。仓库README里有一个完整的演示动图，配置的时候不知道怎么弄，可以参考那个动图。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=2)

02

核心功能

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg#imgIndex=3)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/wzfB4YnnqWoicC71IgOUHxL9TBW0c6iaQB2cUj8mMwW2KR0tSjREEUVZ8BxkK6mHflWN4OppxV5YiaC2nk4HLGOON1MVDogYEB4Fmq7TkyicFRQ/640?wx_fmt=png&from=appmsg#imgIndex=4)

Token和费用监控

这个功能对我来说最实用。输入Token数、输出Token数、总量、当前会话的费用（美元），直接挂在状态栏上。如果你是按量付费的模式，这个功能真的能帮你控成本。

还有个Token速度组件（tok/s），支持配置0到120秒的滑动窗口。设成0就是整个会话的平均速度，设成30秒就是最近半分钟的实时速度。

上下文可视化

上下文快满的时候，Claude会自动做compaction（压缩），但你不看数据根本不知道什么时候会触发。它提供了好几个上下文相关的组件——长度、百分比、进度条，还有一个Compaction Counter显示压缩次数，帮你判断是不是该开新对话了。

Git信息拉满

不只是分支名。还能加暂存文件数、未暂存文件数、冲突数量、ahead/behind、SHA哈希、PR信息（支持GitHub和GitLab）、新增行数、删除行数。

有个小细节我特别喜欢：Git分支组件可以配成可点击的链接，在终端里直接跳转到浏览器。

Powerline主题

内置多套主题，箭头分隔符加上渐变配色，终端看起来跟IDE似的。支持16色、256色、真彩色三种模式，喜欢折腾美化的话可玩性很高。

交互式TUI配置

不用手写JSON。跑一条命令就弹出一个终端UI，在里面添加组件、删除组件、排序、设置颜色、切换主题、实时预览，全部可视化操作。还有模糊搜索功能，70个组件也不怕找不到。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=5)

03

安装很简单

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg#imgIndex=6)

方式一：让Claude Code帮你装

直接把GitHub地址丢给Claude Code终端，让它帮忙安装，等一会儿就能装好。不过这种方式有个注意事项：装完之后最好还是自己执行 ccstatusline-zh setup 命令去配置，不要让Claude Code来帮你配，容易出问题。

方式二：手动安装

全局安装中文版（推荐）：

```
npm install -g ccstatusline-zh
```

不想全局装的话，直接npx -y ccstatusline@latest也行。但网络不好的时候每次走npx会有延迟。

装完之后编辑~/.claude/settings.json（Windows是%USERPROFILE%\.claude\settings.json），加上这段配置：

```
{
  "statusLine":{
    "type":"command",
    "command":"ccstatusline-zh",
    "padding":0,
    "refreshInterval":10}
}
```

重启Claude Code，底部状态栏就出来了。refreshInterval 设1到60秒都行，Claude Code 2.1.97以下版本不支持的话就先不写这个字段。

![图片](https://mmecoa.qpic.cn/mmecoa_png/NYQt9rr8A02C3T5QEAYDkicr7qUALPHCSStuKSuobXBHeoLkiaRVbicicYUibISUmZrzuuQXwVGBJc3W2zZOOo6iaECg/640?from=appmsg#imgIndex=7)

04

自定义配置

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/a5yW0MNUS2B35YuvvOcHKH4Nyc8qkXE92WGR1H2T2y4EV3SSq0OuwIKTOw0akzKow9ibibGyLJmw5fywKWgrwYRg/640?from=appmsg#imgIndex=8)

运行 ccstatusline-zh setup 打开TUI配置界面，想加什么组件就加什么，想放哪个位置就放哪个位置。支持的配置项比较多，可以根据自己的习惯和关注点来动态调整。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/wzfB4YnnqWpetVUHjsTPA83cZgJucDfibTdlicCdrjksqVa85dREgg8gjdZw1JetwWUh81Nu3zQyiaOoYRSg2Tuj4ASpP3KzOCo2XZprkDtxzM/640?wx_fmt=png&from=appmsg#imgIndex=9)

如果你是个Claude Code重度用户，这个既有颜值又有功能的状态栏，非常值得装一个。

项目地址：

- 原版：https://github.com/sirmalloc/ccstatusline

- 中文版：https://github.com/huangguang1999/ccstatusline-zh

---
原文链接：https://mp.weixin.qq.com/s/f_S-1gU2uT1Hi3dEqHjykQ
