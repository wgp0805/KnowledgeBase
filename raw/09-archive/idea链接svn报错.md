---
title: idea链接svn报错
tags:
  - SVN
categories:
  - IDEA
date: 2024-05-08 13:25:52
---

重新安装windows10后，使用idea下代码时报了错E170013 E230001: Server SSL certificate verification failed: certificate issued、

网上找了下相同的问题，在此记录下解决方案

 

cmd打开运行窗口，执行以下命令

svn ls https://xxx

xxx是具体的svn项目地址

最后会显示(R)eject, accept (t)emporarily or accept (p)ermanently?

输入p即可

然后根据提示输入svn账户名UserName和密码Password

最后checkout from subversion刷新一下就好了
