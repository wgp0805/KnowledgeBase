---
source_url: "https://mp.weixin.qq.com/s/1JxDBHkEkHRQelHOWubNBg"
title: "开源项目｜100k+ Star！GitHub爆火的多智能体神器，一条命令搭起AI一人公司"
account: "终码一生"
published_at: "2026-10-29 22:17:44"
saved_at: "2026-10-30 06:04:14"
sync_id: "art_60c760a6acda4e87b6693fd6f9969dee"
parse_status: "ok"
---

# 开源项目｜100k+ Star！GitHub爆火的多智能体神器，一条命令搭起AI一人公司

点击“终码一生”，关注，置顶公众号

每日技术干货，第一时间送达！

现在很多开发者的桌面是这样的：Claude Code开一个窗口，Cursor开一个标签页，Codex CLI在另一个终端里跑着。

三个代理各忙各的，互不认识。想让它们配合做一件事，只能自己当中间人，在几个窗口之间来回传话。

Paperclip想解决的就是这个问题。它不做代理，它做“公司”——给这些各自为战的AI安排岗位、划定汇报线、分配预算、跟踪进度。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/81db368432fd66c4a2da752b2396c1e9_MD5.jpg)

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/e3415148a9018e581714e7cf7e6c0289_MD5.png)

01

它扮演的角色：不是员工，是公司

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/ea730ad34a93d53950aeb779339a74ef_MD5.png)

项目是Node.js服务端加React前端，MIT协议，今年三月开源，目前十万多Star。

开发者自己的比喻很到位：OpenClaw是员工，Paperclip是公司。

具体怎么理解？Claude Code可以当CTO，Codex当工程师，Cursor当设计师。Paperclip负责给它们定目标、派任务、设预算、盯进度。上级往下布置，下级完成后往上交。心跳机制定时唤醒每个代理，该干活干活，该汇报汇报。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/9b2d3f6d495fe8874df97234e11a9947_MD5.png)

它不关心代理写的代码好不好，只保证每件事都有人负责。

02

接入方式：填空就能“入职”

支持接入的类型不少：Claude Code、Codex、Cursor、Gemini CLI、bash脚本、OpenClaw，甚至自己写的HTTP机器人。

每个代理需要配置角色、职称、汇报关系、预算。官方把适配器都写好了，把接入点填进去即可。

接入本身已经简化成填空题，真正需要动脑的是：你希望这堆代理协同完成什么。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/881a8aea14790a031a3796c51f9cae68_MD5.png)

开发者有句话说得朴实但准确：只要能接收心跳，就能入职。

任务跟公司目标、项目目标、具体工单绑定。代理清楚自己为什么做这件事，而不是只看到一个任务标题。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/1b3de86bc8af51d49898871642ba7de0_MD5.png)

心跳按时间表唤醒代理，检查状态，把结果往上汇报。一个目标拆到哪一层、谁负责哪一段，面板上都能追溯。

03

刹车机制：预算和审批

每个代理有月度预算，花到上限自动停止。不会出现某个代理陷入循环、把额度烧光的情况。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/e9158fa37177d853fc9ffc4e6a755753_MD5.png)

雇佣、暂停、终止代理，都需要审批。

所有操作留审计日志，配置变更带版本控制，改错了能回滚。

这条设计的分量比看起来重。代理跑起来之后，人很难逐条盯着它做了什么。“能查、能回滚”这两件事必须由系统兜底。

组织架构也是完整的一套。代理有老板、有头衔、有职位描述。工单系统记录每次对话和每次工具调用。任务之间有依赖关系，阻塞项没解决，下游不会启动。

上下文从任务往上流到项目和公司目标，代理始终清楚自己在做什么。

一个实例可以跑多个公司，数据互相隔离，手机上也能监控。同时折腾几个side project的人，这一条能省不少切换成本。

04

安装：一行命令起一个实例

开源、自托管、不需要注册账号。默认走本地回环，第一次跑最快：

```nginx
npx paperclipai onboard --yes
```

想配成局域网或Tailscale，加一个参数：

```nginx
npx paperclipai onboard --yes--bind lan
# 或者走tailnetnpx
paperclipai onboard --yes--bind tailnet
```

npx报错多半是私有npm registry的问题，强制走公共源：

```nginx
npx --registry https://registry.npmjs.org paperclipai onboard --yes
```

也可以手动拉源码：

```bash
git clone https://github.com/paperclipai/paperclip.gitcd paperclippnpminstallpnpm dev
```

API服务跑在3100端口，嵌入式PostgreSQL自动创建，不用手动配。前置要求是Node.js 20以上、pnpm 9.15以上。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/3d3c6501595641896f88c65a77be1d0b_MD5.png)

整个流程没有账号体系要打通，也没有云端控制台要点，链路全在本机。

05

首次使用：先建一家公司

打开后会看到新手引导页，点新建公司。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/c3c95b32e855b5a808bd988d0ddffa53_MD5.png)

公司名随便起，填完进控制面板。这一步是把“一家公司”当成隔离单位，后面的代理、工单、预算都挂在它下面。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/4e2a34ed7fa2b253e9bc6e4164b57790_MD5.png)

面板初始是空的，先加至少一个员工。第一个加进去的会自动成为CEO，建议用你能打的那个模型。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/eb2d9e8c1c284b5027e8f205438f1b56_MD5.png)

然后选适配器。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/8023342f24a90a815b365f7c2252ca07_MD5.png)

按这个模式加完几个员工，配置心跳间隔，创建代理。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/f694736ed8608f3ac86d4ffbbdd346ee_MD5.png)

创建完先别派活。到代理详情页点一下测试环境，确认配置通了。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/0b5ec6b9287ee736278222b57a691d02_MD5.png)

通了之后就能让员工干活了。

![](assets/2026-10-29%20-%20%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C100k+%20Star%EF%BC%81GitHub%E7%88%86%E7%81%AB%E7%9A%84%E5%A4%9A%E6%99%BA%E8%83%BD%E4%BD%93%E7%A5%9E%E5%99%A8%EF%BC%8C%E4%B8%80%E6%9D%A1%E5%91%BD%E4%BB%A4%E6%90%AD%E8%B5%B7AI%E4%B8%80%E4%BA%BA%E5%85%AC%E5%8F%B8/6b848e28329eb50af9b156f97b8401d2_MD5.png)

这套流程跑通之后，再接第二个、第三个代理会快很多，适配器和心跳参数都能复用。

06

现状：方向对，但仍需打磨

同时开多个代理干不同的事，管理成本只会越来越高。Paperclip把自己定位成公司而不是员工，这个区分很有价值。眼下流行的“一人公司”模式，前提就是得有人把这些Agent调度起来。

生态还在生长，社区在推插件，Star也还在涨。

一年前，让几个不同的AI代理围绕同一个目标协作，还得自己写调度脚本。现在这件事被收进了一个界面里。

但它离成熟还有距离。开源才半年多，issue区还堆着六千多个未关闭的问题，说明坑不少。

现阶段它更适合爱折腾、能接受边用边修的人。想找一个装上就零维护的团队工具，还得再等等。

- 开源地址：https://github.com/paperclipai/paperclip

---
原文链接：https://mp.weixin.qq.com/s/1JxDBHkEkHRQelHOWubNBg
