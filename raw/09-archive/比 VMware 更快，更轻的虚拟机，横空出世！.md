---
title: "比 VMware 更快，更轻的虚拟机，横空出世！"
source: "https://mp.weixin.qq.com/s/35sFLLqKbTinSVwFJXf2JA"
---
小哈学Java *2026年10月21日 16:38*

将 小哈学Java设为“ **星标** **⭐** ”

第一时间收到文章更新

![图片](assets/%E6%AF%94%20VMware%20%E6%9B%B4%E5%BF%AB%EF%BC%8C%E6%9B%B4%E8%BD%BB%E7%9A%84%E8%99%9A%E6%8B%9F%E6%9C%BA%EF%BC%8C%E6%A8%AA%E7%A9%BA%E5%87%BA%E4%B8%96%EF%BC%81/5dff6f7b9316ff49163f6bc0fe6498e2_MD5.webp)

来源：网络

**在线 Java 面试刷题（已更新334题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- Multipass
- 开始使用
- 创建 Ubuntu 虚拟机
- 操作虚拟机
- 总结
- 相关链接

---

说起虚拟机工具大家最熟悉的自然是 VMware，功能很多很强大，最让我认可的地方就是可以非常方便的修改虚拟机的配置，让虚拟机达到自己想要的性能～～

可是 VMware 好用是真的好用，但就是要付费呀！还不便宜，每次续费的时候我多多少少都有点心疼～～

## Multipass

最近有读者给我推荐了一款虚拟机工具：Multipass，非常轻量级的虚拟机命令管理工具。运行环境支持 Linux、Windows 和 macOS。

![picture.image](assets/%E6%AF%94%20VMware%20%E6%9B%B4%E5%BF%AB%EF%BC%8C%E6%9B%B4%E8%BD%BB%E7%9A%84%E8%99%9A%E6%8B%9F%E6%9C%BA%EF%BC%8C%E6%A8%AA%E7%A9%BA%E5%87%BA%E4%B8%96%EF%BC%81/cb4e548c7a2a53dfc7ebb8af657af243_MD5.webp)

picture.image

## 开始使用

首先我们需要在官网下载并且安装 Multipass，选择自己对应的操作系统，因为我的是 Mac 电脑，所以选择 MacOS，点击 Download 开始下载

![选择对应版本安装](assets/%E6%AF%94%20VMware%20%E6%9B%B4%E5%BF%AB%EF%BC%8C%E6%9B%B4%E8%BD%BB%E7%9A%84%E8%99%9A%E6%8B%9F%E6%9C%BA%EF%BC%8C%E6%A8%AA%E7%A9%BA%E5%87%BA%E4%B8%96%EF%BC%81/13818d9622f3cb55da0e37ef672b9ce5_MD5.jpg)

Multipass 官网下载页面

安装之后，查看自己安装的版本

```
$ multipass version
```

## 创建 Ubuntu 虚拟机

首先查看可以下载使用的 Ubuntu 镜像，

```
$ multipass find
```

运行成功后，可以看到下面的这些镜像列表，包含各种版本的。

```
Image                       Aliases           Version          Description
snapcraft:core18                              20201111         Snapcraft builder for Core 18
snapcraft:core20                              20201111         Snapcraft builder for Core 20
core                        core16            20200818         Ubuntu Core 16
core18                                        20200812         Ubuntu Core 18
16.04                       xenial            20210128         Ubuntu 16.04 LTS
18.04                       bionic            20210129         Ubuntu 18.04 LTS
20.04                       focal,lts         20210223         Ubuntu 20.04 LTS
20.10                       groovy            20210209         Ubuntu 20.10
appliance:adguard-home                        20200812         Ubuntu AdGuard Home Appliance
appliance:mosquitto                           20200812         Ubuntu Mosquitto Appliance
appliance:nextcloud                           20200812         Ubuntu Nextcloud Appliance
appliance:openhab                            20200812         Ubuntu openHAB Home Appliance
appliance:plexmediaserver                    20200812         Ubuntu Plex Media Server Appliance
```

新建一个容器，

```
$ multipass launch --name dg
Launched: dg
```

然后下载最新版的 Ubuntu 镜像，之后我们就可以直接使用了。

```
$ multipass exec dg -- lsb_release -d
Description:    Ubuntu 18.04.4 LTS
```

## 操作虚拟机

**查看虚拟机列表**

虚拟机创建完成后，查看虚拟机列表。

```
Name                State             IPv4                Image
dg                  Running           192.168.24.5        Ubuntu 18.04 LTS
```

现在有一台 Ubuntu 18.04 版本的虚拟机在运行，对应的 IP 地址是：192.168.24.5。

**查看虚拟机信息**

通过命令你可以查看当前运行的虚拟机具体信息。

```
$ multipass info --all

Name:           dg
State:          Running
IPv4:           192.168.24.5
Release:        Ubuntu 18.04.4 LTS
Image hash:     fe3030933742 (Ubuntu 18.04 LTS)
Load:           0.00 0.00 0.00
Disk usage:     1.5G out of 4.7G
Memory usage:   112.1M out of 985.7M
```

**进入虚拟机**

使用下面的命令查看虚拟机的系统配置信息、内存、磁盘等的使用情况。

```
$ multipass shell dg
```

如果你不想进入系统内部，也可以通过上述提到的 multipass exce 命令，来操作 Ubuntu 系统。

**暂停/重启虚拟机**

```
# 暂停
$ multipass stop dg
# 启动
$ multipass start dg
```

**删除/释放虚拟机**

使用 delete 命令删除虚拟机之后，该虚拟机实际上还是存在了，想要彻底删除则需要释放虚拟机。

```
# 删除
$ multipass delete dg
# 释放
$ multipass purge dg
```

**配置自动化**

既要保持开发环境和线上环境一致，又要节省部署时间。我们可以使用 --cloud-init 对容器进行初始化配置:

```
$ multipass launch --name ubuntu --cloud-init 
            config.yaml
```

[config.yaml](http://config.yaml/) 是初始化配置文件，内容如下：

```
#cloud-config

runcmd:
- curl -sL 
            https://deb.nodesource.com/setup_12.x
           | sudo -E bash -
- sudo apt-get install -y nodejs
- wget 
            https://releases.leanapp.cn/leancloud/lean-cli/releases/download/v0.21.0/lean-cli-x64.deb
          
- sudo dpkg -i 
            lean-cli-x64.deb
```

runcmd 可以指定容器首次启动时运行的命令

## 总结

经过一段时间的使用，我认为这款工具确实是不错的！比如说我要搞点 linux 的小试验，通过 Multipass 几分钟就能搭起系统来测试。要测试小型数据库集群，也可以通过 Multipass 在本地快速搭建虚拟机集群，很不错！

唯一美中不足的是 Multipass 只能使用 Ubuntu 镜像，因为这款工具是由 Ubuntu 背后的 Canonical 公司开发开源的。

## 相关链接

官网： [https://multipass.run/](https://multipass.run/)

文档： [https://multipass.run/docs/](https://multipass.run/docs/)

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI [2.x](http://2.x/) + Spring Boot [4.x](http://4.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E6%AF%94%20VMware%20%E6%9B%B4%E5%BF%AB%EF%BC%8C%E6%9B%B4%E8%BD%BB%E7%9A%84%E8%99%9A%E6%8B%9F%E6%9C%BA%EF%BC%8C%E6%A8%AA%E7%A9%BA%E5%87%BA%E4%B8%96%EF%BC%81/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 阿里二面：main 方法可以继承吗？3. 面试题：Kafka 有几种选举过程？4. Java使用 try catch 会影响性能？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢啦
```

阅读原文