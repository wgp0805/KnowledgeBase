---
source_url: "https://mp.weixin.qq.com/s/IZv8LykgPe6vvVSb3JDaoQ"
title: "3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。"
account: "码农学习联盟"
published_at: "2026-10-09 11:41:00"
saved_at: "2026-10-09 13:23:29"
sync_id: "art_7ce86d55823447b9bcb4df74862227d7"
parse_status: "ok"
---

# 3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。

01

**Rakazo：Grok Bot 的开源平替**

![](assets/2026-10-09%20-%203%20%E4%B8%AA%E6%9C%80%E8%BF%91%E7%88%86%E7%81%AB%E7%9A%84%20Personal%20Agent%20%EF%BC%8C%E5%9C%A8%20GitHub%20%E4%B8%8A%E6%9C%89%E5%BC%80%E6%BA%90%E5%B9%B3%E6%9B%BF%E4%BA%86%E3%80%82/6d06908ef941f6b3f7d7a031d3ff9983_MD5.png)

Rakazo 可以搭建持续运行的 AI Bot，**每个 Bot 都有自己的对话、记忆、例行任务和工作历史。**

你可以给它连接模型，再配置一套执行任务用的电脑环境。

有了这套环境，Bot 就能使用**浏览器、终端、文件和图形桌面。**

它可以在网页里查资料，把结果保存成文件，也可以运行命令处理工作。实际能操作哪些工具，取决于你连接的服务和给它的权限。

[📹 点击播放视频](https://mp.weixin.qq.com/mp/readtemplate?t=pages/video_player_tmpl&action=mpvideo&auto=0&vid=wxv_4725504054582624263)

Rakazo 还支持创建**多个 Bot 分工**。一个 Bot 可以把任务交给其他 Bot，或者临时创建子 Agent 处理其中一部分。

比如，你可以安排一个 Bot 研究资料，再把后续写作交给另一个。

电脑环境也能按工作需要选择：**多个 Bot 共用团队电脑，或者各自使用隔离的私有电脑。**

它提供网页、桌面和移动端入口，也支持语音交互。

模型和电脑服务都能自行选择，整套服务可以在本地运行，也能连接外部电脑服务。

如果把后端放在持续运行的服务器上，Bot 就能继续工作，你再从手机或电脑连接过去。

```bash
开源地址：https://github.com/elie222/rakazo
```

除了这一个，下面这个也是 Grok Bot 的开源平替。

```javascript
开源地址：https://github.com/milind-soni/OpenMausBot
```

02

**OpenMuse：Muse 的开源平替**

![](assets/2026-10-09%20-%203%20%E4%B8%AA%E6%9C%80%E8%BF%91%E7%88%86%E7%81%AB%E7%9A%84%20Personal%20Agent%20%EF%BC%8C%E5%9C%A8%20GitHub%20%E4%B8%8A%E6%9C%89%E5%BC%80%E6%BA%90%E5%B9%B3%E6%9B%BF%E4%BA%86%E3%80%82/d687ad255c375aab0d30760aa2f4a906_MD5.png)

OpenMuse 是最近爆火的 Meta 的 Muse 的开源平替。

支持 iOS、Android 和网页端。

你可以让它查资料、处理邮件和 PDF，也能在同一个应用里**查看任务计划和执行进度。**

遇到需要补充信息或确认的步骤，助手会把请求展示出来。

[📹 点击播放视频](https://mp.weixin.qq.com/mp/readtemplate?t=pages/video_player_tmpl&action=mpvideo&auto=0&vid=wxv_4726220716113805313)

[📹 点击播放视频](https://mp.weixin.qq.com/mp/readtemplate?t=pages/video_player_tmpl&action=mpvideo&auto=0&vid=wxv_4726221068904792066)

它也有**持久化浏览器**，可以阅读公开网页，并让你接管同一个浏览器会话。

需要处理文件或运行命令时，可以配置可选的 Linux 工作区。

它还可以**定期检查公开页面**，发现内容变化、可用状态变化，或者价格达到设定阈值时发出提醒。

任务的**计划和状态会保存下来**，能暂停、继续、取消等。只要后端服务持续运行，关闭前端后，后台工作仍能继续。

目前它处于 Alpha 阶段，实际使用时需要自行部署，并连接模型、Intelligence 和相关服务，适合拿来搭建或改造自己的个人助手。

![](assets/2026-10-09%20-%203%20%E4%B8%AA%E6%9C%80%E8%BF%91%E7%88%86%E7%81%AB%E7%9A%84%20Personal%20Agent%20%EF%BC%8C%E5%9C%A8%20GitHub%20%E4%B8%8A%E6%9C%89%E5%BC%80%E6%BA%90%E5%B9%B3%E6%9B%BF%E4%BA%86%E3%80%82/edbd5e6987fbcc43dc4e714bf277f7b1_MD5.png)

```bash
开源地址：https://github.com/CopilotKit/openmuse
```

03

**OpenDots：Dots 的开源平替**

OpenDots 可以搭建一个有多个专业助手的 AI 工作台。

**每个 Dot 都能设置自己的名字、职责、工作要求和工具权限**，你可以创建研究助手、写作助手，并决定它们能访问哪些工作空间。

![](assets/2026-10-09%20-%203%20%E4%B8%AA%E6%9C%80%E8%BF%91%E7%88%86%E7%81%AB%E7%9A%84%20Personal%20Agent%20%EF%BC%8C%E5%9C%A8%20GitHub%20%E4%B8%8A%E6%9C%89%E5%BC%80%E6%BA%90%E5%B9%B3%E6%9B%BF%E4%BA%86%E3%80%82/b97744987adb7da57ff7d20ae31b5297_MD5.png)

目前各个 Dot 有独立的角色和对话，你需要组织材料、安排交接。

接好电脑服务后，每个 Dot 可以有自己的浏览器、工作文件和终端。

浏览器环境和文件会在电脑停止、重新启动后保留。

**你可以查看操作和命令输出，也可以接管浏览器，这些能力按助手分别授权。**

成果可以放进 **Space**，也就是按项目组织文档的工作空间。

保存后的 Page 是可以继续编辑的文档。

你可以要求助手先交草稿，通过审核确认后再保存。打开文档后，还能手动改改内容，或者让助手继续修改。

[📹 点击播放视频](https://mp.weixin.qq.com/mp/readtemplate?t=pages/video_player_tmpl&action=mpvideo&auto=0&vid=wxv_4726226190116503553)

它还支持周期任务、语音通话和 Slack 接入。

后台任务在原来的对话里运行，配置好 Slack 后，可以在消息线程中继续交流。

OpenDots 基于 CopilotKit 和 AG-UI 构建，目前是早期的单用户模板，聊天需要连接 Intelligence 和模型服务，电脑、语音及 Slack 则需要分别配置。

```javascript
开源地址：https://github.com/CopilotKit/OpenDots
```

除了这一个，还有其他的开发者开源的 OpenAI Dots 的开源平替。

```bash
开源地址：https://github.com/Anil-matcha/open-dots
```

---
原文链接：https://mp.weixin.qq.com/s/IZv8LykgPe6vvVSb3JDaoQ
