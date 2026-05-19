---
title: docker安装及使用-window环境
tags:
  - Docker
categories:
  - Docker
date: 2025-07-16 14:25:21
---

# 一、环境准备

1. windows 10以上
2. CPU支持虚拟化技术

# 二、安装docker

## 1、访问docker官网下载docker安装器

![image-20251120110850253](image-20251120110850253.png)

点击下载即可

![image](c9d6d38e740a0367b1d3e992e334e5f9.png)

## 2、安装前准备

因为docker desktop 是可以部署在windows 上来运行docker的应用服务的，其基于windows 的 Hyper-V服务和WSL2内核的Windows上创建一个子系统（linux）,从而实现其在windows上运行docker。所以电脑上需要**开启Hyper-V**服务和安装**WSL2**。

在系统中搜索控制面板，打开程序，点击启用或关闭windows功能，开启`Hyper-V`,`windows虚拟机监控程序平台`，`适用于Liunx的windows的子系统`

![image](1461d89e473a5c5f4869b9b57edc281e.png)

![image-20251120111047829](image-20251120111047829-1763608858411-5.png)

配置完毕后，重启电脑

**备注：**

> 由于 Windows 家庭版没有 Hyper-V，因此必须先安装它。

如下所示，没有Hyper-V选项

![image](13cd908219a63e78ca93c6cd0a7b8eb7.png)

Windows 11 家庭版，请按照以下步骤安装 Hyper-V：

复制以下批处理代码，新建空白文本后保存，保存更改文本 .txt 后缀为 .bat 格式，这样就能变为批处理脚本。右键以管理员身份运行即可。

```bash
pushd "%~dp0"
dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt
for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"
del hyper-v.txt
Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL
pause
```

![image](c192af8d783b63762482027ffdc7b544.png)

![image](e8e6f195b3d54b59e4f3473d2bf38940.png)

![image](7dcfc4c8dd59ff20760a2ada4ca3a112.png)

重新启动后，Hyper-V 将在您的 Windows 上安装并自动启用，如下所示：

![image](a4cf50c24bf63573186e24f86cb22339.png)

## 3、安装DockerDesktop

![image](5398452d68c5c382abd3e1e49ecdc36f.png)

![image](5eb134ce70462d1a4d004cc7b21b948b.png)

![image](f4690b6b31b02fbe6a9a447d7e842ced.png)

安装完成

![image](0fd74e61c0e17f55c6445645ec4359a2.png)

![image](5e4653a1d4720be9a56af5cde982f731.png)

## 4、总结

1. 我这里安装的Docker，即使配置了国内镜像，如果想要搜索及必须要登录，想登录就必须要魔法上网，不登录就不能搜索，然后我配置的国内镜像也没生效，不知道为啥
2. 一些简单的应用直接在dockerdesktop上直接操作就可以，但是一些比较复杂的还是命令比面板好使，面板上总会出现各种问题，例如部署RocketMQ的时候面板部署就起不来，命令就可以，还是多学命令吧
