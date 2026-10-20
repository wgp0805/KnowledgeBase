---
title: "开源项目｜Star16.3k一站式AI短剧生成平台"
source: "https://mp.weixin.qq.com/s/SZKvhVQXg8xx74zLsApRZg"
---
## 开源项目｜ Star16.3k一站式AI短剧生成平台

点击关注 👉 IT码徒 *2026年10月20日 10:40*

点击“IT码徒”，关注，置顶公众号

每日技术干货，第一时间送达！

先把一个数字摆出来：2026年上半年，抖音新增的AI剧漫剧超过二十万部，破亿率不到半个百分点，每分钟制作成本几百元。

这说明一件事——产能已经不是瓶颈了。

真正卡住人的，是那条从剧本到成片的线。

火宝短剧：

```bash
git clone 
            https://github.com/chatfire-AI/huobao-drama.gitcd
           huobao-drama/frontendnpminstallcd../backendnpminstallnpm run dev
```

目前16.3k万Star，做的事就是把剧本、角色、分镜串成一条视频生产线。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9CStar16.3k%E4%B8%80%E7%AB%99%E5%BC%8FAI%E7%9F%AD%E5%89%A7%E7%94%9F%E6%88%90%E5%B9%B3%E5%8F%B0/cbcaaf22f406380157c49da576b866f9_MD5.webp)

01

整体架构

它的架构分四层，项目拆成四块：

- frontend/：Nuxt 3、Vue 3、TypeScript
- backend/：Hono、Drizzle、Mastra、SQLite
- backend/workspace/skills/：Agent技能
- desktop/：Electron桌面版
- data/：资源和库

前端管界面，后端管逻辑，skills目录放Agent能力，desktop是独立桌面端，data存生成出来的素材。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9CStar16.3k%E4%B8%80%E7%AB%99%E5%BC%8FAI%E7%9F%AD%E5%89%A7%E7%94%9F%E6%88%90%E5%B9%B3%E5%8F%B0/d309b8dbd27a2fc4a07e68f35327ec4f_MD5.webp)

02

核心功能设计

四个Agent，各管一段

内置了四个Mastra Agent：

- script\_rewriter：用大语言模型把小说改写成剧本
- extractor：提取角色、场景、道具，并做去重
- storyboard\_breaker：拆出分镜
- prompt\_generator：写图片和视频的提示词

界面支持中英日韩四种语言，生成语言可以全局设置。

注意一点：它没有独立的配音Agent。声音是视频模型生成画面时一并产出的，不单列一层。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9CStar16.3k%E4%B8%80%E7%AB%99%E5%BC%8FAI%E7%9F%AD%E5%89%A7%E7%94%9F%E6%88%90%E5%B9%B3%E5%8F%B0/fff4b298cc9c545eaef6cf20526e887e_MD5.png)

对接外部模型，不自行训练

模型全部来自外部厂商，它自己一个都不训：

- 文本：OpenAI兼容接口、Gemini
- 图片：OpenAI、Gemini、火山引擎
- 视频：火山Seedance 2.0、MiniMax H3、阿里云百炼Wan 3.0

资产积累式角色管理

角色管理能做三件事：AI生成角色形象、批量角色生成、角色图片上传和管理。

角色形象和场景背景由AI绘图生成——先生成参考图，生视频时注入，一致性靠攒。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9CStar16.3k%E4%B8%80%E7%AB%99%E5%BC%8FAI%E7%9F%AD%E5%89%A7%E7%94%9F%E6%88%90%E5%B9%B3%E5%8F%B0/d8d47c73bb892090c89d759bc766a787_MD5.png)

分镜头攒制视频

视频任务分三样：AI自动生成视频任务、生成场景描述和视频提示词、按任务批量生成视频。

视频生成也分三样：文生视频自动生成、FFmpeg单镜头合成与字幕处理、整集拼接导出。

分镜视频靠文生视频、图生视频模型生成。大生成拆成小镜头，失败可以重试。

资源管理同样三样：素材库统一管理、本地存储支持、任务进度追踪。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9CStar16.3k%E4%B8%80%E7%AB%99%E5%BC%8FAI%E7%9F%AD%E5%89%A7%E7%94%9F%E6%88%90%E5%B9%B3%E5%8F%B0/20089ddab59bc8f5cf44c8d961e7f5a4_MD5.png)

03

一站式工作流步骤

从小说到成片，中间六步：

1. 创建项目，定宽高比和风格
2. 配好AI服务
3. 剧本阶段：把小说改成带场次和角色的拍摄稿
4. 资产制作：产出角色、场景、道具参考图
5. 分镜与视频：生成镜头视频
6. 拼接导出：用FFmpeg合成整集
![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9CStar16.3k%E4%B8%80%E7%AB%99%E5%BC%8FAI%E7%9F%AD%E5%89%A7%E7%94%9F%E6%88%90%E5%B9%B3%E5%8F%B0/cbb23d8a462bb3d07a00ba1f95d8ef10_MD5.png)

这就是一站式工作流。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9CStar16.3k%E4%B8%80%E7%AB%99%E5%BC%8FAI%E7%9F%AD%E5%89%A7%E7%94%9F%E6%88%90%E5%B9%B3%E5%8F%B0/e3415148a9018e581714e7cf7e6c0289_MD5.png)

04

部署与使用说明

装它只要一台电脑，跑它得先配三样东西

环境要求： [Node.js](http://node.js/) 20+、npm 9+。SQLite和FFmpeg免装。

···bash

git clone [https://github.com/chatfire-AI/huobao-drama.git](https://github.com/chatfire-AI/huobao-drama.git)

cd huobao-drama/frontend

npm install

cd../backend

npm install

npm run dev

它不出模型，三类服务得先在设置页配好。“火宝快捷配置”粘一个Key写三条。

桌面版走腾讯云COS镜像，双击即装，数据存用户目录，卸载也不会丢。或者走Docker，镜像huobao/huobao-drama:4.0.5，端口5679，挂huobao-data卷。

生成视频需要支付第三方模型调用费用，具体单价与折扣以平台当前价目表为准。

许可证是CC BY-NC-SA 4.0，禁止商用，商用需要作者授权。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9CStar16.3k%E4%B8%80%E7%AB%99%E5%BC%8FAI%E7%9F%AD%E5%89%A7%E7%94%9F%E6%88%90%E5%B9%B3%E5%8F%B0/e3415148a9018e581714e7cf7e6c0289_MD5.png)

05

结语

产能不再是瓶颈之后，难的是另一件事

它把“做出来”变便宜了，“做什么”反而变贵了。

流水线替你搭好了，拍什么，替不了你决定。

- 开源地址： [https://github.com/chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)

—END—

**PS：防止找不到本篇文章，可以收藏点赞，方便翻阅查找哦。**

往期推荐[MySQL 宣布正式拥抱AI](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514783&idx=1&sn=bd6b4c719878743424e58ac5fc3bc2dc&scene=21#wechat_redirect)[开源项目｜本地跑大模型，选型这件事终于有人管了](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514783&idx=2&sn=4bf92c933658a95c9cec980cef1c604e&scene=21#wechat_redirect)[全网显示IP归属地，准确率99.9%，这个开源的API离线库强大到离谱！](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514775&idx=1&sn=7b51d1455e75f4c73975946b0b5d6e3d&scene=21#wechat_redirect)[突然要求所有接口都用post请求，为什么？](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514775&idx=2&sn=34663d2a31a9e074cafd159167f529f1&scene=21#wechat_redirect)[把AI装进了SSH终端，这款强大的远程终端工具开源了！](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514749&idx=1&sn=5e510609ba4d62372a5a7194a9585f26&scene=21#wechat_redirect)[微信为什么使用 SQLite 保存聊天记录？](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514743&idx=1&sn=5508ad3d343add932570aa6cf82a88d3&scene=21#wechat_redirect)

开源 · 目录

阅读原文