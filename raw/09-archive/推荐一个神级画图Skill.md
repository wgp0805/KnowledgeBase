---
title: "推荐一个神级画图Skill"
source: "https://mp.weixin.qq.com/s/5oqmJnx_mX3gi7zKbwc6TA"
---
苏三说技术 *2026年7月20日 09:00*

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

> 之前用 [draw.io的MCP画架构图，能用，但样式总感觉差点意思——配色偏老气，布局也不够精致。](http://draw.xn--iomcp,,,-7n3da4750kd2ay9fc4eet8aozh8ko9khslao2pbsg2san6m6k277kecbx1gq52b9y4aw11ayqap35a0t7c6fxau1hzlj5ye4p2gcj5c./) 最近发现一款叫 `architecture-diagram-generator` 的开源Skill，跟Claude描述一下系统结构，几秒钟就出一张高大上的架构图，效果比我之前画的强多了，这里给大家分享下。

## 简介

`architecture-diagram-generator` 是一款专为AI设计的系统架构图生成Skill，支持Cursor、Claude Code、Windsurf等AI编程工具，目前在Github上已有 `6.3k+star` 。实际用下来，几秒钟就能出一张像样的架构图，你只管描述系统长什么样，剩下的交给AI。

该Skill具有如下特性：

- **零设计门槛** ：仅需描述你的项目架构就行，不用懂配色、不用懂布局。
- **迭代飞快** ：想加组件、调布局、换样式？一句话的事，AI秒改。
- **分享零成本** ：输出就是一个HTML文件，浏览器打开即看，不用装任何东西。
- **内置导出** ：图表自带复制/PNG/PDF按钮——这点真的省心，不用再截图了。

下面是该Skill生成的架构图，效果还是挺炫酷的！

![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BESkill/5448dc3576e09d0d0123dfdf952da066_MD5.webp)

## 安装

> architecture-diagram-generator的安装非常简单，下载压缩包，导入就可以使用了，这里以Claude Desktop为例。

- 首先我们需要去它的release页面下载对应的压缩包，地址： [https://github.com/Cocoon-AI/architecture-diagram-generator/releases](https://github.com/Cocoon-AI/architecture-diagram-generator/releases)
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BESkill/85408a47cbe62bf84cbafd920cb95c8f_MD5.png)

- 在Claude Desktop中选择 `自定义->技能->上传技能` 功能，然后选择下载好的压缩包上传即可完成安装。
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BESkill/31aa9fc3d3ac8126b25bb8dd76dbfe7a_MD5.png)

## 使用

### 画架构图

- architecture-diagram-generator的使用还是非常方便的，例如我想画一张mall电商实战项目的系统架构图，通过 `/architecture-diagram` 命令调用skill来画图即可，具体提示词如下：
```
/architecture-diagram 画一张mall项目的系统架构图，项目地址：D:\developer\github\mall
```
- 最终画出的mall项目架构图如下，项目的分层结构非常清晰，配色也不错，比 [draw.io画的感觉更上档次；](http://draw.xn--io;-w28di68f7yhprcq8h3o0a93co40f/)
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BESkill/7901dab3047a4fd97cfc881ad2ca82bc_MD5.png)

- 最终的产物是一个html文件，点击右上角的按钮可以选择图片的下载格式，支持复制/PNG和PDF三种；
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BESkill/c70f8fa52efea6d79e04061e70ca2fc3_MD5.png)

### 画流程图

- architecture-diagram-generator是专门用来画架构图的，如果你想画流程图的话需要使用 `process-flow-diagram-generator` 这个Skill，地址： [https://github.com/Cocoon-AI/process-flow-diagram-generator](https://github.com/Cocoon-AI/process-flow-diagram-generator)
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BESkill/77b64219bead9cb4989dd0e9272371fe_MD5.png)

- 我这里根据mall项目中的generateConfirmOrder方法，画了一张订单功能中生成确认单的流程图，具体提示词如下；
```
/process-flow-diagram 根据mall项目中生成确认单流程（generateConfirmOrder方法），画一张业务流程图
```
- 最终效果如下，流程非常清晰，简单而直观；
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BESkill/3605df5216e77803409436e88f778c7a_MD5.png)

- 为了测试下这个Skill的能力，我还让它生成了一个相当复杂的订单生成流程图，也是顺利完成的，效果如下；
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E4%B8%AA%E7%A5%9E%E7%BA%A7%E7%94%BB%E5%9B%BESkill/02e1974e7fa077e6512514e6b0e5d8a0_MD5.png)

## 总结

architecture-diagram-generator是一款非常实用的架构图生成Skill，无需设计基础，几段描述就能生成一张高颜值的深色主题架构图，输出为独立HTML文件，分享和导出都很方便。

搭配同系列的process-flow-diagram-generator，架构图和流程图都能轻松搞定，相比 [draw.io不仅上手门槛更低，出图效果也更现代化，感兴趣的小伙伴可以尝试下它。](http://draw.xn--io,,-194fiak27dt2axixa73d5kkm88yf8b9zhzte3ztp5v3tc6ip03hqhgt0u2hkga618biquys3eolsp39mnpmbq2e./)

## 项目地址

[https://github.com/Cocoon-AI/architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)