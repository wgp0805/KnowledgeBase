---
title: "一行命令，解锁 Claude Code 全部权限-ClawGod - 绝不原创的飞龙"
source: "博客园"
url: "https://www.cnblogs.com/apachecn/p/23178662"
date: "2026-10-01T02:17:00Z"
score: 0.95
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 一行命令，解锁 Claude Code 全部权限-ClawGod - 绝不原创的飞龙

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/apachecn/p/23178662  
> **抓取日期**: 2026-10-01  
> **相关性评分**: 0.95

# ClawGod，把官方藏起来的功能全部打开

> 你有没有这种感觉：明明Claude Code是最强的AI编程工具，但总有些地方“差点意思”？
> 
> 用最强的Opus模型，告诉你“订阅等级不够”。让多个AI同时协作，发现功能根本没开。想问个安全相关的问题，直接被拒绝回答。
> 
> 这些限制不是技术上做不到的，是官方关掉

于是我们进行了二开魔改推出---ClawGod，用简单的方法，把这些被关掉的功能全部打开了

## **🔗链接**

**GitHub：<https://github.com/0Chencc/clawgod>**

**官网：<https://clawgod.0chen.cc/>**

## **先说结论**

ClawGod 是一个开源补丁工具（GPL-3.0）

一行命令安装，30秒完成，不满意卸载恢复原样

安装后你能得到什么：

  * 安全研究相关提问不再被拒绝（CYBER_RISK_INSTRUCTION 已删除）

  * 破坏性操作不再弹出强制确认（操作审慎指令已删除）

  * URL生成限制已解除

  * 可以自定义API地址和模型（支持代理、中转、兼容API）

  * 功能开关归你管（本地JSON覆盖远程功能标志）

  * 绿色主题初步了解状态

  * 遥测数据违约关闭




## **1 模型解锁：Opus 4.6 + 百万上下文**

Claude Code 的模型分配是按订阅等级来的：

订阅等级

原版可用模型

ClawGod解锁后

自由的

基础模型

**全部模型**

专业版

十四行诗

**Opus 4.6 + 1M上下文**

最高

作品（无1M）

**Opus 4.6 + 1M上下文**

> 💡ClauGod 让 Claude Code 认为你是 Anthropic 的内部，所有模型和上下文窗口全部开放

* * *

## **2 内部用户模式：伪装为 Anthropic 内部员工**

ClawGod 将 Claude Code 的用户类型从`external`（外部用户）改为`ant`（Anthropic 内部），解锁部分内部行为：

  * GrowthBook功能开关系统可被本地配置覆盖

  * 消息过滤规则放宽，显示对非隐藏内部用户的内容




## **3 多AI协作：Agent Teams客户端解锁**

Agent Teams 是 Claude Code 的多智能体协作功能，多个 AI Agent 组成“团队”分工处理复杂任务：

> **Agent 1** 负责分析架构
> 
> **Agent 2** 负责写测试
> 
> **Agent 3** 负责审查代码它们同时工作，互不干扰

ClawGod 在客户端移除了 Agent Teams 的条件检查（`return!0`强制开启）

原版需要设置实验性环境变量，ClawGod 直接默认启用。

* * *

## **4 限制安全研究解禁 + 操作移除**

原版Claude Code有三条内部限制指令：

  * **CYBER_RISK_INSTRUCTION** ：遇到渗透测试、漏洞利用、C2框架等直接话题拒绝回答

  * **URL生成限制** ：禁止生成或猜测任何URL

  * **操作审慎指令** （Executing actions with care）：删除文件等破坏性操作前强制弹确认




对于安全研究人员、CTF学员、渗透测试工程师来说，这是最大的痛点之一

**ClawGod 将这三条限制全部删除**

**安全研究问题不再被拒绝，破坏性操作不再反复确认。**

* * *

## **5 功能开关归你管（实测可用）**

Anthropic用一个叫GrowthBook的系统远程控制哪些功能对你开放。你以为某些功能不存在，其实只是服务端帮忙关了。

ClawGod注入`CLAUDE_INTERNAL_FC_OVERRIDES`环境变量，让你用本地JSON文件覆盖这些交换机：
    
    
    {  "tengu_harbor": true,  "tengu_session_memory": true,  "tengu_amber_flint": true,  "tengu_auto_background_agents": true}
    

**哪些开、哪些关，你说了算。**

* * *

## **6 自定义API：换你自己的控制台**
    
    
    {  "apiKey": "your-key",  "baseURL": "https://api.anthropic.com",  "model": "claude-opus-4-6"}
    

想用代理？兼容API？中转服务？改一下`baseURL`就行。

* * *

## **📦 如何安装**

**macOS / Linux**

`curl -fsSL https://github.com/0Chencc/clawgod/releases/latest/download/install.sh | bash`

Windows

`irm https://github.com/0Chencc/clawgod/releases/latest/download/install.ps1 | iex`

需要提前准备的：Node.js 18+ · npm · 一个有效的 Claude Code 账号

安装完成后你会得到两个命令：（`claude`补丁版）和`claude.orig`（原版备份）

* * *

## **🟢如何确认生效**

打开克劳德码，看颜色：

颜色

状态

🟠**橙色**

官方原版，限制都在

🟢**绿色**

ClawGod 补丁已生效，全部解锁

* * *

## **🗑不需要了怎么办**

**macOS / Linux**
    
    
    claude --uninstall
    

Windows
    
    
    claude --uninstall
    

一行命令，恢复官方原版。没有任何残留。

* * *

## **❓您可能关心的问题**

**Q：这算不算破解？会不会封号？**

ClawGod 不认证流程，不修改账号，不绕过服务端限流。你的 API 请求仍然走官方通道，仍然需要修改有效的 Claude Code 账号。它只是本地客户端的行为。

**Q：Claude Code更新了怎么办？**

ClawGod使用正则坐标补偿器偏移量匹配，小版本更新大兼容概率。如果不兼容，等作者更新补丁即可。

**Q：安全吗？开源的吗？**

开源，GPL-3.0协议。所有补丁代码都可以在GitHub上完全逐行审查。

* * *

一行命令·30秒安装·🟢绿色亮起开始体验完整的克劳德代码

ClawGod 是独立开源项目，与 Anthropic 相关 · 使用前请了解相关风险


---
> 原文链接: https://www.cnblogs.com/apachecn/p/23178662