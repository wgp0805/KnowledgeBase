---
title: "codex windows平台中elevated sandbox机制学习 - 三国梦回"
source: "博客园"
url: "https://www.cnblogs.com/grey-wolf/p/22643567"
date: "2026-08-23T13:31:00Z"
score: 0.7
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# codex windows平台中elevated sandbox机制学习 - 三国梦回

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/grey-wolf/p/22643567  
> **抓取日期**: 2026-08-23  
> **相关性评分**: 0.7

# 背景

大家好啊，我是逐日。本篇继续梳理下我对codex desktop中沙箱（elevated sandbox）的理解（windows平台，非使用windows上wsl2）。

本文主要学习了：<https://openai.com/zh-Hans-CN/index/building-codex-windows-sandbox/>

原文比较不好懂，可能要多看两遍。

我上一篇文章已经讲过了unelevated sandbox的理解，可以先看一下再来看本篇。

[codex windows平台中unelevated sandbox机制学习 ](<https://www.cnblogs.com/grey-wolf/p/22633410>)

# 未提权沙箱的实现机制

## 什么是令牌、受限令牌

令牌其实就是我们平时说的token。

windows中，进程会拿到一个token，进程在做事的时候，比如读写文件，操作系统就会检查进程的token，看看这个token是否允许你读写该文件。突然想起一句：你拿明朝的剑，来斩清朝的官？

本来进程一般拿的是普通token，token里包含了所属颁发人信息。读写文件时，检查只需要检查下颁发人是否能操作该文件就行。

见：

<https://learn.microsoft.com/zh-cn/windows/win32/secauthz/interaction-between-threads-and-securable-objects>

<https://learn.microsoft.com/zh-cn/windows/win32/secauthz/how-dacls-control-access-to-an-object>

![image-20260823205240630](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823205240630.png)

![image-20260823210112137](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823210112137.png)

但是受限令牌不一样，它是在令牌的基础上派生出来的权限更低的令牌，操作系统进行的检查项会更多：

<https://learn.microsoft.com/zh-cn/windows/win32/secauthz/restricted-tokens>

![image-20260823205745717](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823205745717.png)

可以先不想那么多，反正write-restricted token的限制更多就是了，具体怎么限制，往下看。

## 未提权沙箱中，write-restricted token在codex中的应用

未提权沙箱的情况下，使用codex的人可以全程不需要管理员权限。比如张三就是一个普通用户，张三运行codex时，codex会创建一个write-restricted token，这个token的所有人还是张三，所以codex理论上可以读写任何张三拥有权限的文件夹。文件或文件夹的权限通过右键属性-安全-高级，就能看到的。

下面这每一行也叫做一个ace(Access Control Entry)，多个ace就叫acl(Access Control List,)。这块可以参考网上一个文章：

<https://zhuanlan.zhihu.com/p/2034977828370912249>

![image-20260823202019950](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823202019950.png)

但是假设张三拥有多个文件夹的权限，如：

‪E:\zhangsan-project1

‪E:\zhangsan-project2

但我们在codex中创建project的时候，假设选了（‪E:\zhangsan-project2）为workspace目录，那么理论上，codex只能写‪E:\zhangsan-project2下才行；不能写‪E:\zhangsan-project1.

怎么才能实现这个呢？

这就是靠write-restricted token中的SidsToRestrict字段来实现，SidsToRestrict字段包含了一个sid（可以理解为用户id，假设为111111），在codex需要写、修改某个文件夹时，就需要校验这个文件夹的是否允许该sid（111111）来写。由于这个sid是codex随机生成的，系统上别的程序都不知道这个sid的存在，那么，就不可能有任何一个目录对该sid有ace（Access Control Entry），所以，codex就无法写入任何目录。

但是codex可以自己去给某个目录（如：‪E:\zhangsan-project2）设置一条ace（允许111111这个sid修改该文件夹）。

codex自己也会记录下来，某个sid可以修改某个目录。

.codex目录下有个cap_sid文件，大家可以看下。  
![image-20260823203145034](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823203145034.png)

![image-20260823203244622](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823203244622.png)

通过上述方式，就实现了：使用该write-restricted token的codex，只能改‪E:\zhangsan-project2这个目录，别的张三名下的目录却改不了。

## 未提权沙箱中，该write-restricted token存在的问题

在codex该token的颁发人还是张三，一般来说，除非防火墙有限制，否则张三肯定是可以上网的。所以这个token是具有访问互联网的能力的。

codex拿着这个token，假设大模型让codex执行一些shell，shell中需要curl访问互联网啥的。我们是没法控制shell不让它访问互联网的，技术手段限制不住。

具体看看下文的：限制网络访问这一节。

<https://openai.com/zh-Hans-CN/index/building-codex-windows-sandbox/>

这块能采取的办法就是，对于curl这类知名程序，如果你设置了HTTPS_PROXY这类环境变量，curl就会把请求先发给你HTTPS_PROXY设置的地方，你可以把HTTPS_PROXY的值设为无法访问的值，保证curl无法访问互联网。但是不是所有程序都是curl，程序完全可以不理会这些环境变量。

这也就是未提权沙箱的最大短板，无法控制网络访问，所以诞生了提权沙箱。

# 提权沙箱的实现机制

## 控制CodexSandboxOffline用户访问互联网

提权沙箱的提权，意思是需要你使用管理员权限。

它的思路也比较简单，上面说的write-restricted token还是继续用，但是token的颁发人不能是当前的真实用户，而是codex自己创建出来的用户。

我们先查看codex创建出来的用户:

打开计算机管理：按下Win+R键，输入compmgmt.msc，然后按Enter键打开计算机管理。

导航到用户账户：在计算机管理中，依次点击“系统工具”>“本地用户和组”>“用户”。这将显示当前计算机上的所有用户账户。

可以看到，创建了一个用户组：codexSandboxUsers，组内包含两个用户：CodexSandboxOffline、CodexSandboxOnline![image-20260823211300635](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823211300635.png)

我们再去看看防火墙：

一共有三条：

![image-20260823211507615](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823211507615.png)

第三条是限制访问外网的：

![image-20260823211651884](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823211651884.png)

![image-20260823211714335](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823211714335.png)

这里就限制了CodexSandboxOffline不能访问任何外网ip。

## write-restricted token（授权人为CodexSandboxOffline）

write-restricted token中的授权人现在变成了CodexSandboxOffline，由于防火墙中对CodexSandboxOffline的控制，这个token已经无法上外网了。

但是CodexSandboxOffline这个用户的问题是，对文件夹的权限少了。它不像之前未提权机制里，token里的张三，张三可以读写张三的文件夹；但是CodexSandboxOffline可无法读取张三的文件夹啊，所以，codex就需要单独去修改各个文件夹的acl。

比如，假设对于某个project，workspace是E:\zhangsan-project2，那就需要在‪E:\zhangsan-project2的acl中增加CodexSandboxOffline的acl，这样CodexSandboxOffline才能读写‪E:\zhangsan-project2。

见下图就是例证：

![image-20260823212759354](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823212759354.png)

另外，张三可是可以读取全电脑的文件夹啊，那是不是全电脑的文件夹的acl都要增加CodexSandboxOffline对应的ace呢？

也不是。目前只是增加一些常用的，从文章中看出来，目前只加了一些常用目录，如`C:\Program Files\`这类：

<https://openai.com/zh-Hans-CN/index/building-codex-windows-sandbox/>

![image-20260823212329603](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823212329603.png)

而且由于`C:\Program Files\`这类文件夹下文件太多了，增加CodexSandboxOffline对应的ace的开销也是不小的。所以这块是codex异步在后台进行的。

为此，还专门把这部分弄到了一个单独的exe里，codex-windows-sandbox-setup.exe：

![image-20260823212600982](https://dump-1252523945.cos.ap-shanghai.myqcloud.com/img/image-20260823212600982.png)

# 参考

write-restricted token的官方资料：

<https://learn.microsoft.com/zh-cn/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken>

<https://learn.microsoft.com/zh-cn/windows/win32/secauthz/interaction-between-threads-and-securable-objects>


---
> 原文链接: https://www.cnblogs.com/grey-wolf/p/22643567