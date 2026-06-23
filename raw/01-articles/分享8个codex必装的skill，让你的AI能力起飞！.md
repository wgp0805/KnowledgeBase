---
title: "分享8个codex必装的skill，让你的AI能力起飞！"
source: "https://mp.weixin.qq.com/s/_Mc5H3vcntXQ61ks9zE2Rg"
---
程序员小灰 *2026年6月20日 10:37*

大家好，我是程序员小灰。

很多人刚开始用 CodeX，第一反应还是把它当成桌面版的 ChatGPT。

你或许会惊喜地发现，它能够帮你修改文件、编写代码、排查报错，但这些其实只是 CodeX 最基础的能力。

一旦你开始给它安装 Skill，它就可以接上更多不同的工具，把能力扩展到代码之外。

这篇就整理几个我认为普通人都能用上且非常好的Skill。

## 1\. Web-access

[https://github.com/eze-is/web-access](https://github.com/eze-is/web-access)

如果你在 CodeX 发现官方 Chrome 插件控制不了浏览器。

![图片](assets/%E5%88%86%E4%BA%AB8%E4%B8%AAcodex%E5%BF%85%E8%A3%85%E7%9A%84skill%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84AI%E8%83%BD%E5%8A%9B%E8%B5%B7%E9%A3%9E%EF%BC%81/df9e1a67b65f2a8516817b8661a2cbe7_MD5.webp)

可以试试下面这个 Skill，Web-access 是一个无法使用官方浏览器插件时的平替方案。

它可以让 CodeX 操作你自己的 Chrome 或 Edge，带着登录态点页面、截图、滚动、读取动态加载内容。

这个Skill非常适合读取动态展示内容的网页和需要登录的页面，你还可以将一些固定浏览器操作封装为自动化流程，比如定时检查页面、截图、提交表单。

它背后主要用的是 Chrome DevTools Protocol，也就是 CDP。

简单说，就是让 CodeX 通过浏览器调试接口去控制真实浏览器。

使用前需要打开远程调试开关：

Edge：edge://inspect/#remote-debugging

Chrome：chrome://inspect/#remote-debugging

下图以 Chrome 为例：

![图片](assets/%E5%88%86%E4%BA%AB8%E4%B8%AAcodex%E5%BF%85%E8%A3%85%E7%9A%84skill%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84AI%E8%83%BD%E5%8A%9B%E8%B5%B7%E9%A3%9E%EF%BC%81/ff905de47f6b9bff5413a77802a4236b_MD5.webp)

## 2\. Agent-Reach

[https://github.com/Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)

上面的 Web-access 偏操作浏览器，而Agent-Reach 就是让 CodeX 读一些社交媒体的内容。

比如 YouTube、Reddit、X、GitHub、B站、小红书、RSS。

安装这个工具后，CodeX 相当于拥有了一份全网站点信息地图。

该 Skill 会预先告知 CodeX 目标数据所在页面，以及需要提取的关键数值。

统统都已经标记好，CodeX跟着这份地图到这个站点里获取信息和总结就行。

非常适合在各个平台做调研任务、内容总结、社区口碑搜索和竞品内容观察。

![图片](assets/%E5%88%86%E4%BA%AB8%E4%B8%AAcodex%E5%BF%85%E8%A3%85%E7%9A%84skill%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84AI%E8%83%BD%E5%8A%9B%E8%B5%B7%E9%A3%9E%EF%BC%81/fbb33f53834f31f424f97513b66d3e02_MD5.webp)

## 3\. Humanizer-zh

https:// [github.com/op7418/Humanizer-zh](http://github.com/op7418/Humanizer-zh)

这个 Skill 是专门用来去除 AI 味的。

如果你觉得 CodeX 产出的内容太机械、太模板，或者太像「正确但没感情的总结」，可以试试它。

它会处理一些常见的 AI 写作痕迹，比如空泛拔高、三段式、宣传腔、过度连接词、结尾强行升华。比较适合用在推文、公众号、情感文、演讲稿这类更需要「人味」的文本里。

## 4\. Guizang PPT Skill · 网页 PPT / 配图 / 封面

[https://github.com/op7418/guizang-ppt-Skill](https://github.com/op7418/guizang-ppt-Skill)

这是归藏大佬做的网页 PPT Skill。

它主要有两套设计风格，一套是电子杂志 × 电子墨水，另一套是瑞士国际主义。

我个人更喜欢电子杂志 × 电子墨水，很适合做一些带观点、带干货、又不会太商务的模板。

![图片](assets/%E5%88%86%E4%BA%AB8%E4%B8%AAcodex%E5%BF%85%E8%A3%85%E7%9A%84skill%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84AI%E8%83%BD%E5%8A%9B%E8%B5%B7%E9%A3%9E%EF%BC%81/f5ab085cd979d65c69c97272a40ff497_MD5.webp)

它做出来的是单文件 HTML PPT。

对 CodeX 来说，这种方式很友好，因为 HTML/CSS 本来就是它擅长生成和修改的东西。

## 5\. html-anything

[https://github.com/nexu-io/html-anything](https://github.com/nexu-io/html-anything)

5 月的时候，Claude Code 工程师 Thariq 在 X 上发过一篇文章，意思大概是：AI 经常输出 Markdown，但 Markdown 一旦超过 100 行，阅读体验就开始变差。

他的解决办法也很直接：让 AI 把内容转成视觉体验更好的 HTML。

![图片](assets/%E5%88%86%E4%BA%AB8%E4%B8%AAcodex%E5%BF%85%E8%A3%85%E7%9A%84skill%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84AI%E8%83%BD%E5%8A%9B%E8%B5%B7%E9%A3%9E%EF%BC%81/6de90dbaa606a5061f87bf0ddb80dbc6_MD5.webp)

html-anything 的作用，就是帮大家实现这个需求。

它可以把 AI 输出的内容，转成很多更适合阅读和传播的形式，比如主题演讲、网页原型、数据报告、海报、小红书卡片、推文卡片等。

你把草稿给 CodeX，它负责生成内容，前端负责预览和导出。

![图片](assets/%E5%88%86%E4%BA%AB8%E4%B8%AAcodex%E5%BF%85%E8%A3%85%E7%9A%84skill%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84AI%E8%83%BD%E5%8A%9B%E8%B5%B7%E9%A3%9E%EF%BC%81/8a0e37b13f9ced6f31414027eaf89e84_MD5.webp)

## 6\. HyperFrames

[https://github.com/heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

HyperFrames 不只是一个 Skill 文件，它本身就是一个完整的视频生成框架。

它的思路是让 CodeX 写 HTML、CSS、动画和媒体内容，然后通过 Headless Chrome 渲染画面，再用 FFmpeg 转成 MP4。

也就是说，CodeX 不需要学传统剪辑软件。

它只要写网页，HyperFrames 负责把网页变成视频。

用户可以直接在本地用命令行跑，也可以让 CodeX 配合对应 Skill 一起使用。

它比较适合做产品介绍、代码讲解、数据动画和短视频内容。

![图片](assets/%E5%88%86%E4%BA%AB8%E4%B8%AAcodex%E5%BF%85%E8%A3%85%E7%9A%84skill%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84AI%E8%83%BD%E5%8A%9B%E8%B5%B7%E9%A3%9E%EF%BC%81/f59b6f3b488f12f20af96855f5070bb7_MD5.gif)

## 7\. GitNexus

[https://github.com/abhigyanpatwari/GitNexus](https://github.com/abhigyanpatwari/GitNexus)

GitNexus 做的是把代码库变成知识图谱。

它会把一个仓库里的依赖、调用链、模块关系、执行流程整理出来，再通过工具暴露给 CodeX。

这件事对大仓库很有用。因为 CodeX 如果只靠搜索文件，很容易漏上下文。

![图片](assets/%E5%88%86%E4%BA%AB8%E4%B8%AAcodex%E5%BF%85%E8%A3%85%E7%9A%84skill%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84AI%E8%83%BD%E5%8A%9B%E8%B5%B7%E9%A3%9E%EF%BC%81/076eb88cbd2b96b32c051b0d4836c02b_MD5.webp)

但如果有了代码图谱，它就能更快理解“这个函数被谁调用“、”这个模块和哪里有关”、“改这里会影响什么”。

## 8\. CodeX Skills / Skill Creator

最后这个我觉得可以单独说一下。

这是一个可以专门 “制作Skill” 的Skill，你可以把反复使用的流程沉淀成 Skill。

你如果每天都需要 CodeX 帮你整理汇报内容、做数据分析，那你只要把这个做过一遍的事情，在同个对话窗口中，让他帮你做出 Skill，你下次就可以直接拿来复用。

![图片](assets/%E5%88%86%E4%BA%AB8%E4%B8%AAcodex%E5%BF%85%E8%A3%85%E7%9A%84skill%EF%BC%8C%E8%AE%A9%E4%BD%A0%E7%9A%84AI%E8%83%BD%E5%8A%9B%E8%B5%B7%E9%A3%9E%EF%BC%81/887048960af0b73b9c3fa0ba64c6e379_MD5.webp)

## 写在最后

好了，以上就是我们今天介绍的 8 个强力 Skill。

刚开始用 CodeX，不一定要一次装很多 Skill。你可以先从自己的需求出发，像CodeX如果自带的Chrome无法用，就装 Web-access。

想CodeX帮你读取不同平台的内容，就看 Agent-Reach；觉得文字太 AI，就用 Humanizer-zh 去掉AI创作痕迹。

最后，你如果自己有某个经常会的流程，就让 CodeX 帮你做成自己的 Skill。这也是新手最应该尽快掌握的，让 CodeX 成为一个不断增强的本地工作台。

2026下半年，希望有更多强大的AI工具诞生，为我们的工作和生活带来十倍百倍的效率提升，让我们做到以前不敢想象的事情。

我是程序员小灰，我会持续为大家分享最新的AI工具和AI副业经验。如果想第一时间收到推送，也可以给我个星标⭐我们下次再见~~

继续滑动看下一个

程序员小灰

向上滑动看下一个