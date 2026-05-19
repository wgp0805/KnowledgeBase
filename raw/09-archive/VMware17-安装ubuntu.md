---
title: VMware17 安装ubuntu
tags:
  - Liunx
categories:
  - Liunx
date: 2025-07-16 10:19:45
---

## 一、安装VMware

现在的vmware的下载地址有变化了，好像是被一个叫博通的公司收购了变成了他们的免费软件了，现在这个工具也无需在四处寻找激活了。

官网搜索VMware下载后，点击下载会跳转到博通的注册登录页，注册登录很简单，不会就自行百度吧

![image-20250716102934350](/img/VMware17-安装ubuntu/image-20250716102934350.png)

依次点击就可以看到想要下载的软件了

![6ad83ab8-4207-4dde-a592-a5695c974782](/img/VMware17-安装ubuntu/6ad83ab8-4207-4dde-a592-a5695c974782.png)

点击下载即可

## 二、安装ubuntu

1. 新建虚拟机

![image-20250716104340714](/img/VMware17-安装ubuntu/image-20250716104340714.png)

2. 默认即可

![image-20250716104401845](/img/VMware17-安装ubuntu/image-20250716104401845.png)

3. 选择稍后创建

![image-20250716104415739](/img/VMware17-安装ubuntu/image-20250716104415739.png)

4. 选择liunx选择Ubuntu 64位

![image-20250716104503296](/img/VMware17-安装ubuntu/image-20250716104503296.png)

5. 根据对应位置选择即可

![image-20250716104520134](/img/VMware17-安装ubuntu/image-20250716104520134.png)

6. 选择对应处理器信息及其他硬盘信息

![image-20250716104547114](/img/VMware17-安装ubuntu/image-20250716104547114.png)

![image-20250716104557009](/img/VMware17-安装ubuntu/image-20250716104557009.png)

![image-20250716104606516](/img/VMware17-安装ubuntu/image-20250716104606516.png)

![image-20250716104617293](/img/VMware17-安装ubuntu/image-20250716104617293.png)

![image-20250716104624517](/img/VMware17-安装ubuntu/image-20250716104624517.png)

![image-20250716104632318](/img/VMware17-安装ubuntu/image-20250716104632318.png)

![image-20250716104644076](/img/VMware17-安装ubuntu/image-20250716104644076.png)

7. 这里可以默认但是一搬不建议，建议选择其他目录

![image-20250716104737499](/img/VMware17-安装ubuntu/image-20250716104737499.png)

![image-20250716104748393](/img/VMware17-安装ubuntu/image-20250716104748393.png)

![image-20250716104811584](/img/VMware17-安装ubuntu/image-20250716104811584.png)

然后点击编辑虚拟机选择镜像就可以启动了，启动时镜像安装完成后，会提示让你把cd推出，这时虚拟机下边有一个我已安装完成，点击后，在系统界面点击回车即可，就相当于把cd推出了。

## 三、安装SSH

刚安装好的系统，可能没有ssh，那么fianlshell就会出现连不上的问题，这时只需执行命令安装即可

```shell
更新工具包
sudo apt update
安装ssh
sudo apt install openssh-server
重启ssh
sudo systemctl start ssh
查看ssh状态
sudo systemctl status ssh
设置ssh开机自启
sudo systemctl enable ssh
```



