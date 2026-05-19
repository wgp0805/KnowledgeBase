---
title: 服务器上搭建git
tags:
  - git
categories:
  - Git
date: 2022-12-02 14:25:58
---

转载自：[在CentOS下搭建私有的git服务器 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/468091233)

## 1. 系统环境

系统： Linux：`CentOS 7.9 64位`

查看ssh版本如下图：

![img](v2-24669b44e7cb6c46c3a070599a21a9fc_720w.jpg)

输出表示没问题，可以继续。 版本可能不一致，能用即可

如果您的系统没有，请自行安装

## 2. 安装git

```text
$ yum install -y git

# 验证是否安装成功
$ git --version

# 输出如下内容表示成功：
git version 1.8.3.1
```

![img](v2-52f1e338411d05d6c3b96704d439802b_720w.jpg)

## 3. 添加git的管理的账户和设置密码

```text
# 添加git账户
$ adduser git

# 修改git的密码
$ passwd git

# 然后两次输入git的密码确认后。

# 查看git是否添加成功
$ cd /home && ls -al
# 如果已经有了git，那么表示成，参考如下：
drwxr-xr-x.  5 root       root       4096 Feb 16 12:22 .
dr-xr-xr-x. 21 root       root       4096 Feb 16 12:26 ..
drwx------   2 git        git        4096 Feb 16 12:22 git

# 默认还给我们分配一个名字叫git的组。
```

## 4. git的权限管理

git仓库的权限管理，我们可以手动进行管理和配置，也可以通过其他辅助工具。如果小团队的话，直接通过ssh公钥进行管理即可，如果大点的团队，最好用[gitolite](https://link.zhihu.com/?target=https%3A//github.com/sitaramc/gitolite) 或者 [gitosis](https://link.zhihu.com/?target=https%3A//github.com/res0nat0r/gitosis)，两者都差不多，一个是Perl开发，一个是Python开发。

## 5. git的手动权限管理

经过以上步骤，其实服务器的基本已经配置好，但是需要设置权限和配置远程访问git仓库的方式。ssh的方式

### 5.1 配置服务端的ssh访问

切换到git账号,并创建ssh的默认目录和校验公钥的配置文件

```text
# 1.切换到git账号
$ su git

# 2.进入 git账户的主目录
$ cd /home/git

# 3.创建.ssh的配置，如果此文件夹已经存在请忽略此步。
$ mkdir .ssh

# 4. 进入刚创建的.ssh目录并创建authorized_keys文件,此文件存放客户端远程访问的 ssh的公钥。
$ cd /home/git/.ssh
$ touch authorized_keys

# 5. 设置权限，此步骤不能省略，而且权限值也不要改，不然会报错。
$ chmod 700 /home/git/.ssh/
$ chmod 600 /home/git/.ssh/authorized_keys
```

此时，服务端的配置基本完成。接下需要把客户端的公钥拷贝到`authorized_keys`文件中。

### 5.2 配置客户端的ssh私钥并上传服务器(先安装客户端)

**第一步： 创建客户端的ssh私钥和公钥**
检查是否已经拥有ssh公钥和私钥：进入用户的主目录。
用户主目录：
Windows系统：`C:\Users\用户名`
Linux系统：`/home/用户名`
Mac系统：`/Users/用户名`
然后查看是否有`.ssh`文件夹，此文件夹下是否有如下几个文件。

用户主目录的.ssh文件夹下
.ssh
├── id_rsa
└── id_rsa.pub # 我们要用的私钥

如果没有，那么用ssh-keygen创建ssh的私钥。

$ ssh-keygen -t rsa

\# 接下来，三个回车默认即可。

创建私钥成功后，在查看用户目录是否有意加有了公钥文件id_rsa.pub

![img](v2-bd77d8794282a72d4af6a7be9bfa5c68_720w.jpg)

**第二步： 拷贝私钥到git的服务器**



### 5.3 服务器端添加客户端的SSH公钥

切换到服务器端，把刚才上传的laoma.pub文件的内容添加到 authorized_keys中，就可以允许客户端ssh访问了。

```text
# 切换到git账户
$ su git
$ cd /home/git/.ssh

$ ls -al
# 查看一下.ssh目录是否有authorized_keys和laoma.pub文件
drwx------ 2 git git 4096 Feb 16 13:10 .
drwx------ 5 git git 4096 Feb 16 12:32 ..
-rw------- 1 git git    0 Feb 16 12:32 authorized_keys
-rwx------ 1 git git  583 Feb 16 13:10 lzx.pub

# 如果有，那么进行下面的把laoma.pub文件中的内容添加到authorized_keys中.
$ cat lzx.pub >> authorized_keys

# >> 是在文件后面追加的意思，主要如果用其他编辑器，每个ssh的pub要单独一行，建议用cat命令方便简单。
```

到此为止，您配置的客户端应该可以ssh的方式直接用git账号登录服务器。(当然不安全，后面可以控制)

\# 在客户端用ssh测试连接远程服务器,请将域名[http://aicoder.com](https://link.zhihu.com/?target=http%3A//aicoder.com)换成你的ip地址或者域名
$ ssh git@aicoder.com

\# 第一次连接有警告，输入yes继续即可。如果可以连接上，那么恭喜你的ssh配置已经可以了。

![img](v2-d0655ca82025c3b1a0f81e74737867f7_720w.jpg)

### 5.4 服务器端创建测试git仓库

进入服务器的终端。

```text
# 切换到git账号
$ su git

# 进入git账号的用户主目录。
$ cd /home/git

# 在用户主目录下创建 test.git仓库的文件夹
$ mkdir test.git  && cd test.git

# 在test.git目录下初始化git仓库
$ git init --bare

# 输出如下内容，表示成功
Initialized empty Git repository in /home/git/test.git/
```

git init --bare 是在当前目录创建一个裸仓库，也就是说没有工作区的文件，直接把git仓库隐藏的文件放在当前目录下，此目录仅用于存储仓库的历史版本等数据

到此，客户端就可以进行clone或者remote add此仓库了。

### 5.5 客户端测试连接git远程仓库

客户端，可以新建一个文件夹，初始化一个仓库，然后跟远程服务器上的空仓库建立连接。

```text
# 以下shell代码，纯手写没有验证，如果有错误请自行纠正。
$ mkdir demos && cd demos
$ git init
$ touch q.txt
$ echo 'aicoder.com' >> a.txt
$ git add .
$ git commit -m 'the first commit'

# 把当前仓库跟远程仓库添映射
$ git remote add origin git@aicoder.com:test.git

# 把当前仓库push到远程仓库。
$ git push -u origin master
```

![img](v2-7d3f00b0c90d94c51edd28cd8c62a5f8_720w.jpg)

出示此报错，按照提示设置其邮箱以及用户名，设置完毕再次commit，commit成功，然后push至远程仓库

```text
git config --global user.email "13578456@163.com"
git config --global user.name "lsdf"
git commit -m "first commit"
```

![img](v2-907553e72ad65198163d513f4c113414_720w.jpg)

到此为止，可以尽情的享用git私服了，但是！但是！但是！客户端可以直接ssh登录啊，这是bug，也是不安全的隐患，且看下面怎么禁用git账号的shell登录

### 5.6 禁止客户端shell登录

因为添加了客户端的ssh的公钥到远程服务器，所以客户端可以直接通过shell远程登录服务器，这不安全，也不是我们想要的。且看下面如何禁用shell登录：

第一步：

给`/home/git`下面创建`git-shell-commands`目录，并把目录的拥有者设置为git账户。可以直接用git账号登录服务器终端操作。

```text
$ su git
$ mkdir /home/git/git-shell-commands
```

第二步：修改`/etc/passwd`文件，修改

$ vim /etc/passwd

\# 可以通过 vim的正则搜索快速定位到这行， 命名模式下 :/git:x

\# 找到这句, 注意1002可能是别的数字

```
git:x:1002:1002::/home/git:/bin/bash
```

\# 改为：
```
git:x:1002:1002::/home/git:/bin/git-shell
```

\# 最好不要直接改，可以先复制一行，然后注释掉一行，修改一行，保留原始的，这就是经验！！！
\# vim快捷键： 命令模式下：yy复制行， p 粘贴 0光标到行首 $到行尾 x删除一个字符 i进入插入模式
\# 修改完后退出保存： esc进入命令模式， 输入：:wq! 保存退出。

好了，此时我们就不用担心客户端通过shell登录，只允许使用git-shell进行管理git的仓库。

如果有其他小伙伴要连接git服务器，仅需要把他的公钥也添加到authorized_keys即可

