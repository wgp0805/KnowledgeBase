---
title: "又一个神级画图 Skill 开源，再见 draw.io！"
source: "https://mp.weixin.qq.com/s/seakLQf0iQZ9ErHTOAxs1Q"
---
java1234 *2026年7月9日 09:06*

大家好，我是锋哥。

今天分享一个非常火爆的开源项目 - architecture-diagram-generator

![图片](assets/%E5%8F%88%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BE%20Skill%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%86%8D%E8%A7%81%20draw.io%EF%BC%81/d067ad7bb5bb937dae77ad206346cc52_MD5.webp)

---

## 目录

- 先说结论：它到底能干什么？
- 为什么我说它可能替代 [draw.io？](http://draw.io？)
- 三分钟上手
- 效果长什么样？
- 几个让人省心的细节

---

## 先说结论：它到底能干什么？

最近 GitHub 上有个项目挺火—— **Architecture Diagram Generator** （架构图生成器），来自 Cocoon AI 团队。

说白了，它不是一个让你手动拖拖拽拽的画图软件，而是一个 **Claude AI Skill** （技能包）。你用人话描述系统架构，Claude 帮你生成一张 **深色主题、排版整齐** 的架构图，输出是一个 **HTML 文件** ，浏览器打开就能看，还能一键导出 PNG 或 PDF。

---

## 为什么我说它可能替代 draw.io？

做过技术方案、写文档、做汇报的人应该都懂： [draw.io](http://draw.io/) 功能很强，但 **上手和改图都费时间** 。组件要一个个拖，连线要一点点调，改一个模块名字，周围布局可能全乱。

这个 Skill 的思路完全不同—— **用对话代替手工** ：

| 传统方式（ [draw.io）](http://draw.io\)/) | 这个 Skill |
| --- | --- |
| 自己画框、连线、配色 | 描述架构，AI 自动生成 |
| 改一处，手动调整布局 | 聊天里说「把 Redis 换成 Memcached」 |
| 导出还要额外操作 | HTML 里自带 Copy / PNG / PDF 按钮 |
| 需要安装或打开在线编辑器 | 一个 HTML 文件，发给别人就能看 |

它特别适合那种「结构已经想清楚了，就是懒得画」的场景。评审稿、技术分享、 onboarding 文档—— **先把图画出来，比完美更重要** 。

---

## 三分钟上手

整个流程就三步，官方 README 写得很清楚，这里用更直白的话总结一下：

### 第一步：安装 Skill

1. 从 [https://github.com/Cocoon-AI/architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) 下载 `              architecture-diagram.zip            `
2. 打开 [https://claude.ai/](https://claude.ai/) → **Customize** → **Skills**
3. 点 **+** → **Upload a skill** ，上传 zip，然后打开开关

> 注意：需要在 Claude 设置里开启 **Code Execution** （代码执行）能力，Free / Pro / Max 等计划都支持。

### 第二步：准备架构描述

你不需要会写代码，只要能把系统说清楚就行。三种常见做法：

- **让 AI 读你的代码** ：在 Cursor、Claude Code 里问一句「分析这个项目的架构，列成组件清单」
- **自己写** ：比如「React 前端 → [Node.js](http://node.js/) API → PostgreSQL，Redis 做缓存，部署在 AWS」
- **让 Claude 给模板** ：问「一个典型 SaaS 应用长什么样？」

### 第三步：让 Claude 画图

把描述贴给 Claude，加上一句：

```
Use your architecture diagram skill to create an architecture diagram from this description:

[粘贴你的架构描述]
```

等一会儿，你会拿到一个 HTML 文件。双击打开，图就在那儿了。不满意？继续聊：「把 API Gateway 放到中间」「加一个 Kafka」——改起来比 [draw.io](http://draw.io/) 快多了。

---

## 效果长什么样？

项目文档 里放了几张官方示例，风格统一： **深色背景、语义化配色、箭头清晰** 。前端、后端、数据库、云服务各用一种颜色，一眼能分清。

### Web 应用（React + Node.js + PostgreSQL）

![图片](assets/%E5%8F%88%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BE%20Skill%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%86%8D%E8%A7%81%20draw.io%EF%BC%81/b843bf85935d32d69ebebe2a6753c759_MD5.jpg)

### AWS 无服务器架构（Lambda + API Gateway + DynamoDB）

![图片](assets/%E5%8F%88%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BE%20Skill%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%86%8D%E8%A7%81%20draw.io%EF%BC%81/e1768255b28c40c27e690f8f83e5b340_MD5.jpg)

### 微服务架构（Kubernetes + API Gateway）

![图片](assets/%E5%8F%88%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BE%20Skill%20%E5%BC%80%E6%BA%90%EF%BC%8C%E5%86%8D%E8%A7%81%20draw.io%EF%BC%81/ac5998bd37a9b4dc4ff4e7e2f00a5d17_MD5.jpg)

说实话，这种完成度如果手动画，熟练的人也要大半小时；用 Skill 描述几句， **几十秒到几分钟** 就能出初稿。

---

## 几个让人省心的细节

**1\. 单文件，到处能用**

生成的是自包含 HTML，CSS 和 SVG 都内嵌在里面。发邮件、丢飞书、挂静态页，不用对方装任何软件。

**2\. 导出很方便**

页面顶部有工具栏：

- **Copy** — 复制高清 PNG 到剪贴板，直接贴进 PPT 或文档
- **PNG** — 下载图片
- **PDF** — 下载 PDF，深色主题会保留

**3\. 配色有规矩，不会乱**

| 类型 | 颜色倾向 | 典型用途 |
| --- | --- | --- |
| 前端 | 青色 | 网页、App、边缘设备 |
| 后端 | 绿色 | API、服务 |
| 数据库 | 紫色 | 数据库、存储 |
| 云服务 | 琥珀色 | AWS 等基础设施 |
| 安全 | 玫瑰色 | 认证、加密 |

**4\. 开源、MIT 协议**

代码在 GitHub 上，可改可分发。Claude Code 用户也可以解压到 `~/.claude/skills/` 本地使用。

**5\. 有「姐妹 Skill」**

如果要做 **流程图、审批流、自动化流水线** 这类「按时间展开」的图，同团队还有 [https://github.com/Cocoon-AI/process-flow-diagram-generator](https://github.com/Cocoon-AI/process-flow-diagram-generator) ，设计语言一致，换场景不用重新适应。

项目链接： **[https://github.com/Cocoon-AI/architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator)**

**[最近，锋哥又开始收Java+AI大模型编程学员了！](https://mp.weixin.qq.com/s?__biz=Mzg4ODA3NTk0Nw==&mid=2247540001&idx=1&sn=53a79ccbfab297d01d4fa5e8ea556fe2&scene=21#wechat_redirect)**