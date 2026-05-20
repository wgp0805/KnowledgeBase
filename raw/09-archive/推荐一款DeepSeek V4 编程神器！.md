---
title: "推荐一款DeepSeek V4 编程神器！"
source: "https://mp.weixin.qq.com/s/U4vlvvWtirsE7RZJjC9iYA"
---
> 这两天在逛Github的时候，发现一款基于DeepSeek V4的开源终端编程神器`DeepSeek TUI`，开源不到1个月就收获了`31k+star`！ 原生支持`100万token上下文`，让你无需频繁压缩上下文，配合DeepSeek性价比也很高，今天给大家分享下这个项目！

## DeepSeek TUI简介

DeepSeek TUI是一款基于DeepSeek V4的开源终端编程智能体（类似Claude Code），原生支持100万token的上下文和思考模式流式输出，目前在在Github上已有`31k+star`。

DeepSeek TUI的主要功能如下：

- **Auto 模式**：每轮对话能根据任务复杂度自动选择模型和推理强度。
- **思考模式流式输出**：能实时观察模型在解决问题时的思维链。
- **完整工具集**：内置文件操作、shell 执行、git、网页搜索/浏览、子智能体、MCP服务器等工具。
- **100万token上下文**：支持上下文跟踪、手动或配置压缩。
- **三种交互模式**：Plan（只读模式）、Agent（任务执行需审批的默认模式）、YOLO（工作区任务自动执行模式）。
- **推理强度档位**：有`off → high → max`三种不同档位。
- **MCP协议**：支持通过MCP服务器扩展智能体的能力。
- **多语言和主题选择器**：支持中文界面，有亮/暗色主题。

下面是DeepSeek TUI使用过程中的效果图，界面还是挺炫酷的！

![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E6%AC%BEDeepSeek%20V4%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%EF%BC%81/10dd439eeb9dd62b70167ca0a2c02f29_MD5.webp)

## 安装及配置

> 使用npm来安装DeepSeek TUI是非常方便的，下面将采用此种方法。

- 首先通过如下命令全局安装deepseek-tui；
```
npm install -g deepseek-tui@0.8.37
```
- 安装完成后使用如下命令启动，`--model auto`开启自动模式，可以自动选择模型和推理强度。
```
deepseek --model auto
```
- 首次启动将弹出设置界面，会引导用户进行设置；
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E6%AC%BEDeepSeek%20V4%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%EF%BC%81/06f60cd641470ef6d6db337942c50159_MD5.webp)

- 在第二步中可以进行语言设置，这里选择简体中文；
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E6%AC%BEDeepSeek%20V4%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%EF%BC%81/4fe7eeb22a079c339b43775720bb8a23_MD5.webp)

- 第三步中需要设置Deepseek API密钥，设置完成就可以开始使用了，API密钥可以从Deepseek官网获取： [https://platform.deepseek.com](https://platform.deepseek.com)
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E6%AC%BEDeepSeek%20V4%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%EF%BC%81/0aef31f26cdc442f68153fa091790a6a_MD5.webp)

## 使用

> 接下来我们就以开发一个Markdown编辑器为例，来介绍下DeepSeek TUI的使用。

- 首先我们在DeepSeek TUI中输入如下提示词；
```
用户需求：开发一个Markdown编辑器功能描述：- 左侧为Markdown编辑器编辑器，右侧为Markdown预览区- Markdown文件的列表、编辑、删除、保存功能- Markdown文件的重命名功能- 支持深色和浅色两种主题模式UI设计规范遵循Material Design（谷歌）开发技术栈：Vue3+Element-Plus+TypeScript
```
- 我们可以通过`Tab`键进行模式切换，这里先切换到`plan`模式，让DeepSeek TUI生成一份计划文档到项目的根目录下；
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E6%AC%BEDeepSeek%20V4%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%EF%BC%81/63d3aae07ba1d303b542c345972bf887_MD5.webp)

- 我看了下计划文档没啥问题，就让DeepSeek TUI执行了，其中出现了两个小BUG，我把错误提交给它就很快解决了，不得不说DeepSeek的输出速度还是非常快的，最终也页面效果如下：
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E6%AC%BEDeepSeek%20V4%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%EF%BC%81/c975c294bf2e03ad5d1520552a1c4911_MD5.webp)

- 全程使用的`deepseek-v4-pro`模型，花费不到2块钱，消耗`200多万token`，这性价比也是很高的；
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E6%AC%BEDeepSeek%20V4%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%EF%BC%81/305e9976b3dbfbcec7925380fbc342ee_MD5.webp)

- 通过`/config`命令可以对DeepSeek TUI进行配置，之前我们配置的语言（locale）和模型（model）都可以在里面进行设置；
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E6%AC%BEDeepSeek%20V4%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%EF%BC%81/192d3616704473d21a302a77a1da3286_MD5.webp)

- 通过`/theme`命令可以切换DeepSeek TUI的主题，内置了8种主题，选择可以实时预览主题，还是很酷的！
![图片](assets/%E6%8E%A8%E8%8D%90%E4%B8%80%E6%AC%BEDeepSeek%20V4%20%E7%BC%96%E7%A8%8B%E7%A5%9E%E5%99%A8%EF%BC%81/52ff8b299bf5fa57ee097d217b5b0e98_MD5.webp)

## 总结

DeepSeek TUI确实是一款不错的终端编程神器，内置工具很全，100万token的上下文，足够塞入一个中小项目了，配合DeepSeek使用性价比也很高，感兴趣的小伙伴可以尝试下它！

## 项目地址

[https://github.com/Hmbown/DeepSeek-TUI](https://github.com/Hmbown/DeepSeek-TUI)