---
title: "开源项目｜一个神级Skill：故事丢进去，AI自动生成上美影风短剧"
source: "https://mp.weixin.qq.com/s/mBQI2L0A_VzK9nqqUKhTDA"
---
终码一生 *2026年10月21日 22:47*

点击“终码一生”，关注，置顶公众号

每日技术干货，第一时间送达！

用AI生成动画，最难的不是让画面动起来，而是让画面“对味”。

尤其当你想要的是上美影那种风格——上海美术电影制片厂，《大闹天宫》《九色鹿》《葫芦兄弟》的缔造者。那种手工线条、矿物颜料的平涂色块、高度概括的造型，辨识度极高，但在AI生成里极难稳定复现。

你说“上美影风格”，AI给你一张油画；你说“平涂”，它还是给你渐变和阴影。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/fb73478cd5f68724a174f2cba5beef22_MD5.webp)

GitHub上有个项目专门解决这个问题：smy-seedance-storyboard。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/8e82d6bebb724fbeb50191b050ef957c_MD5.webp)

01

它是什么

一个Skill。你给它一个故事，它返回一套可以直接用于制作的短剧文档——剧本、出图提示词、分镜提示词，全部齐备，拿到手就能用。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/edd211187c4825a79d76e10e5bc8d383_MD5.webp)

作者liangdabiao，此前做过Seedance2-Storyboard-Generator（2600+ Star），是最早把“小说转多集视频”流程跑通的那批人之一。这个新项目目前一百多Star，八月下旬建库，最近仍有提交。

方向比上一个收得更窄——只做上美影这一种味道。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/e3415148a9018e581714e7cf7e6c0289_MD5.png)

02

交付物：五份文档，一套流程

你说一句“帮我做一个武松打虎的上美影短剧，5集”，它会依次给出：

1. 剧本：按5集、每集15秒拆分，带说书人旁白、台词、字幕卡点
2. 色盘：本剧专用颜色清单，比如朱砂红、鎏金、墨黑、青瓷绿
3. 素材清单：角色、场景、道具的出图提示词
4. 分镜提示词：按时间轴格式写好，整段复制就能出片
5. 尾帧说明：标注每集最后一帧停在哪，方便下一集衔接
![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/de68c0a0ae9c127f0522c8bce6093cd4_MD5.png)

全中文，中文平台直接可用。需要Midjourney的话，素材清单另附英文对照版。

剧本按四幕结构写，旁白采用说书人口吻——古典题材很吃这套，武松打虎、夸父逐日这类故事，旁白一开口氛围就对了。

每集开头先定情绪基调，后面的运镜、音效、色调都围绕这个基调走。

素材编号是固定规则：角色C01-C99，场景S01-S99，道具P01-P99。

分镜按0-3秒、3-6秒切成五段，每段写明景别、运镜、动作，末尾附音效与配乐设计，再用@图片挂上对应素材。格式对齐Seedance的输入习惯，整段粘贴即可使用。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/8782bf909b4f7ef091d03203864f6bf2_MD5.png)![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/e3415148a9018e581714e7cf7e6c0289_MD5.png)

03

三层机制锁住画风

这是项目最核心的设计。作者在说明里只写了一句话：都别改。

第一层：统一风格前缀

每条提示词开头粘贴同一段风格关键词，写死复古手绘动画、传统矿物颜料纯平涂色块、带手工感的不完美笔触。

第二层：结尾两句硬命令

必须纯2D平涂，绝对不要阴影、不要渐变、不要3D体积感，必须大面积留白。作者标注这是实测踩坑总结，少了这两句，AI立刻给你油画感的假上美影。

第三层：一剧一色盘

所有提示词逐字引用同一串颜色名，跨集不跑色。

风格关键词备了三份：中文完整版给生图模型，英文对照版配Midjourney这类模型，精简版贴在分镜提示词首行。

文档里特别标注：生图配方与视频配方分开维护，别互相套用。视频端写绝对化的“不要阴影不要渐变”反而容易出问题。

翻车了也有排查路径：先检查结尾两句硬命令还在不在（复制时容易手滑删掉），还在就补一组负面词——不要阴影、不要渐变、不要3D渲染、不要体积光、不要写实照片。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/e3415148a9018e581714e7cf7e6c0289_MD5.png)

04

安装与使用：三步走完

把仓库克隆下来，丢进Claude Code的skills目录即可。其他支持Skill机制的agent也能用，把仓库地址给它，让它自己安装。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/e679628e3d527d40f26ac7d895706b68_MD5.png)

作者用聊斋里聂小倩和宁采臣那段试了一集，15秒，先跑通流程。

1、第一步：说清需求 它会反问集数、画幅、基调，不想答就说用默认。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/f6600f56b772378292a2ab99ec2b1f3b_MD5.png)

2、第二步：生成三张资产图 作者改用豆包出图，原Skill写的是即梦，他觉得各家效果差距不大。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/c4e991f9fe0109656f63d5ed198de392_MD5.png)

3、第三步：出片 作者用Seedance 2.5，工具不限，WorkBuddy、Codex或其他能调视频模型的地方都行。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/f6c8dfa183ae4385d59d8e1c96354c19_MD5.jpg)

每集分镜末尾附尾帧说明，告诉下一集画面停在哪。做第二集时，上传上一集视频，提示词开头写“将@视频1延长”，它就从尾帧接着生成，中间不用手动剪辑。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/e3415148a9018e581714e7cf7e6c0289_MD5.png)

05

四种子风格，一剧限一种

默认手绘平涂主线，想换点名即可，但一部剧只能用一种：

- 石蓝淡墨绘本：石蓝加淡墨，疏离怪谈感，带怪色点缀
- 水墨淡彩：淡雅写意，大量留白，参照《小蝌蚪找妈妈》
- 剪纸风：分层剪影，对称纹样，参照《葫芦兄弟》
- 敦煌重彩：壁画矿物色，飘带飞天，参照《九色鹿》
![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/b7235be1c9d9d5894746ca2cce549762_MD5.png)

仓库里有两个完整示例：“鲁智深醉闹五台山”（醉闹喜剧，打斗的慢速夸张和动静对比写得很细）和“罗刹市奇幻故事”（敦煌重彩，颜色清单里能看到青瓷绿、朱砂红、鎏金、墨黑、石青、藤黄是怎么定的）。

剧本、素材清单、分镜、使用指南四件套齐全，不想从零开始的照着抄。

另有七份细则手册：风格指南、平台手册、剧本质量标准、故事改编模板、分镜优化公式、配音与音效指南各一份，还有一份最早那批实测提示词留着溯源。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/e3415148a9018e581714e7cf7e6c0289_MD5.png)

06

几个绕不开的限制

- 素材上限：图片最多9张，视频和音频各最多3个、各自总时长不超过15秒，合计不超过12个文件。角色多的故事容易撞上限，得提前规划哪些素材真要出镜。
- 集数灵活：每集固定15秒，5集75秒，10到20集也撑得住。
- 敏感词是黑箱：有作者反馈，“江湖人士”这种普通词都会导致生成失败，平台不告诉你是哪个词，只回“内容不合规”，只能二分排查。
- 长提示词会漏指令：三四百字以后，某段运镜可能没按写的来，或者某角色在那几秒消失了，只能重跑。
- 视频无法局部修改：15秒里哪三秒不满意，没法单独修，只能整段重来。

这些不是项目本身的问题，是当前平台能力的边界，换工具也一样。

![图片](assets/%E5%BC%80%E6%BA%90%E9%A1%B9%E7%9B%AE%EF%BD%9C%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7Skill%EF%BC%9A%E6%95%85%E4%BA%8B%E4%B8%A2%E8%BF%9B%E5%8E%BB%EF%BC%8CAI%E8%87%AA%E5%8A%A8%E7%94%9F%E6%88%90%E4%B8%8A%E7%BE%8E%E5%BD%B1%E9%A3%8E%E7%9F%AD%E5%89%A7/e3415148a9018e581714e7cf7e6c0289_MD5.png)

07

它的价值在于“克制”

作者自己的评价是：它什么都没多做。

没有界面，没堆功能。就是把风格锁定、色盘、分镜格式、集间衔接这几个最容易出问题的环节，写成文档模板，让AI照着填。

上手很简单。

两点提醒：仓库未声明开源许可证，使用前最好跟作者确认；它不适合真人写实类内容，上美影风格本身是为动画准备的。

开源地址： [https://github.com/liangdabiao/smy-seedance-storyboard](https://github.com/liangdabiao/smy-seedance-storyboard)

—END—

**PS：防止找不到本篇文章，可以收藏点赞，方便翻阅查找哦。**

往期推荐[开源项目｜81k Star！装完不用配的 AI 全栈监控利器](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540730&idx=1&sn=94cca76d63058fc8e9be15df2b09328a&scene=21#wechat_redirect)[告别SpringSecurity！Sa-Token+Gateway+Nacos极简鉴权实战](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540730&idx=2&sn=ca6aaf0f16004e172206202190dead84&scene=21#wechat_redirect)[开源项目｜Star 16.3k 一站式 AI 短剧生成平台](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540697&idx=1&sn=bd0038eec90166583bc9d51df00f16e5&scene=21#wechat_redirect)[xxl-job已正式接入AI](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540697&idx=2&sn=06e73db4eb8e1309799adcdf8397df89&scene=21#wechat_redirect)[MySQL 宣布正式拥抱 AI](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540679&idx=1&sn=f5b2c0ad3af18b6b7e6c8809c32ef904&scene=21#wechat_redirect)[开源项目｜本地跑大模型，选型这件事终于有人管了](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540679&idx=2&sn=df1a40fad36cef44f0faec850b04e3f7&scene=21#wechat_redirect)

开源项目 · 目录

阅读原文