---
title: wgp-vue管理系统（长期更新文章，除了工作时间以外写的，不知道啥时候结束，总之慢慢写吧）
tags:
  - 管理系统 
  - spring-boot
categories:
  - 管理系统
date: 2023-06-21 10:11:11
---

z之前一直想写一个管理系统，但是总说没时间，其实最关键的原因就是自己懒，再有就是真的有的地方不会，而且现在有好多好的管理系统可以去借鉴，索性现在就不愿意自己去写了，现在最近发现自己做的事情始终都是CURD，但是这个对于自己来说实在是闭门造车，人啊还是要走出舒适圈的，总是醉在温柔乡中，早晚会沉沦迷失，为了让自己更有方向，自己要自己写一个属于自己的管理系统，这时一件长远的事情，但是希望自己可以坚持，当然这里要声明一下，因为自己的能力问题，这里会明确的去抄Ruoyi-Vue的代码，因为人家的已经很完善了，所以希望自己在借鉴别人的同时找到属于自己的风格!

ruoyi的系统真不错，以下为官网链接，[RuoYi](http://doc.ruoyi.vip/)，有兴趣的可以去看下

# 创建项目

这里我采用的是父子工程，因为感觉这样的话如果有什么新的整合或者拓展会很方便

|    名称    | 版本号  |
| :--------: | :-----: |
| SpringBoot | 2.7.12  |
|    JAVA    |   17    |
|   mysql    | 5.7.34  |
|   lombok   | 1.18.26 |
|            |         |
|            |         |
|            |         |
|            |         |
|            |         |

![image-20230621103717399](image-20230621103717399.png)

然后把除了pom文件夹以外的东西全都删除掉

新建wgp-admin模块 点击file->new->module新建wgp-admin即可

![image-20230621103926018](image-20230621103926018.png)

新建即可，以后新建模块的方式都是这样的 

# 关联git

这里我关联的是国内的gitee毕竟没有网络的限制，具体的仓库创建方法就不写了自行百度吧很简单

这里主要说下关联的问题，创建完成之后会出现一个让你关联的步骤但是个人感觉不是很好用

1. 进入项目根路径，然后打开git执行命令 

```
先设置用户名和邮箱
git config --global user.name "汪广平"
git config --global user.email 1217310848@qq.com
//初始化git
git init
//关联远程git
git remote add origin https://12345xxxx.git
//然后加入全部文件
git add .
//远程库与本地同步合并， 
git pull origin master
//此处可能会报错：fatal: refusing to merge unrelated histories
git pull origin master --allow-unrelated-histories
//提交
git commit -m "第一次提交"
//将本地的分支版本上传到远程并合并
git push origin master
```

# 编写pom的父子依赖关系

ceshi 
