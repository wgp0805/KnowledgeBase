---
title: hexo博客部署到自己的服务器
tags:
  - hexo
categories:
  - hexo
date: 2022-07-09 14:20:55
---

# 将 hexo 部署到云服务器

之前在使用在使用github的时候查看你自己的博客真的是慢的一批，但是有一次也是云服务器打折，再加上本身自己就是想了解下服务器的一部分操作，所以就买了一个但是快过去一年了也没想把博客部署在自己的服务器上，所以浪费了半年的时间，直到前阶段发现真的是太慢了，受不了了，下定决心部署到自己的服务器上，要不服务器在那闲着也是浪费，这篇博客是把博客部署到阿里云服务器上

## 1. 前提

1. 已经搭建好 hexo 的相关环境，并将 hexo 部署到了 GitHub 上
2. 已经购买好云服务器
3. 已经购买并备案好域名 （可选项，没有也可以用 ip 地址访问 hexo）

## 2. 安装宝塔面板

宝塔面板可以[可视化](https://so.csdn.net/so/search?q=可视化&spm=1001.2101.3001.7020)地操作远端服务器（这样就不用自己手动装 nginx 了）

进入宝塔面板的下载页面 [宝塔面板下载](https://www.bt.cn/new/download.html) ，找到 Linux 面板，点击安装脚本 **(如果买的服务器是 Windows 的就点 Windows 的)**

这个很简单就不贴图了，去官网复制对应代码在服务器上执行就可以了

在宝塔中的应用商店直接选择安装nginx 然后就可以直接用了

## 3.安装 并配置 Git 仓库

在远程服务器上配置好 Git 仓库后，才能将本地的 hexo push 到远端。

安装 git **（远程服务器上）**

```shell
yum install git
```

配置 git 用户

```shell
adduser git
```

赋予用户权限

```shell
chmod 740 /etc/sudoers
vim /etc/sudoers
```

输入 i 进入 insert 模式 ，找到 root ALL=(ALL) ALL ，在其下方加入一行 git ALL=(ALL) ALL

```shell
root    ALL=(ALL)       ALL
// 在这里加入代码
git     ALL=(ALL)       ALL
```

按下 ESC ，输入 wq ，保存 vim 文件。

修改 sudoers 文件权限

```shell
chmod 400 /etc/sudoers 
```

设置 git 用户的密码

```shell
sudo passwd git
```

给 git 用户添加 [ssh](https://so.csdn.net/so/search?q=ssh&spm=1001.2101.3001.7020) 秘钥 （找到本地的 ssh 公钥，部署 hexo 到 GitHub 时有生成，以 .pub 结尾）

```shell
su git
mkdir -p ~/.ssh
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorzied_keys
chmod 700 ~/.ssh
vim ~/.ssh/authorized_keys    #将ssh密钥粘贴进去
```

在本地打开一个终端，以 ssh 的方式登录云服务器

```shell
ssh -v git@你的 ip 地址
// 输入密码 即可成功登录云服务器
```

创建一个 git 仓库，新建一个 post-receive 文件，用来存储本地的提交。

```shell
su root
cd /home/git
git init --bare blog.git  #在/home/git下创建新仓库blog.git
chown git:git -R blog.git #给予git用户权限
```

在 blog.git/hooks 文件夹下创建一个 post-receive 钩子，把提交到 git 仓库的文件同步到 home/hexo文件夹中

```shell
cd blog.git/hooks
vim post-receive
```

在 post-receive 文件中输入以下代码

```shell
git --work-tree=/home/hexo --git-dir=/home/git/blog.git checkout -f
```

记得要去创建hexo的文件夹，之后配置nginx也是指定的这个目录

授予 post-receive 文件可执行权限

```shell
chmod +x /home/git/blog.git/hooks/post-receive
```

至此服务端已经配置完成。

## 4. 部署 hexo

打开 hexo 的配置文件 _config.yml 修改 Deployment 位置的配置

```yml
deploy:
    type: git
    repo: root@你的ip地址:/home/git/blog.git    #仓库地址
    branch: master    #分支
```

保存配置文件，打开终端进入 hexo 博客所在文件夹

```shell
cd blog //进入自己博客所在文件夹
hexo clean
hexo g //编译
hexo d //部署
```

此时已经可以通过 ip:80 来访问了

## 5. 通过域名访问 hexo

接下来就是解析域名并指定反向代理了 

这样做完之后，需要配置nginx了，点击网站名–配置文件，如下

```shell
 server
{
listen 80;
server_name 127.0.0.1	\# server_name 填写自己的域名
index index.php index.html index.htm default.php default.htm default.html;
root /home/hexo;	\# 这里root填写自己的网站根目录，修改为/home/hexo
```

解析域名，不同家的域名，解析地址也不太一样，这个自行百度吧，总之就是找到域名-》解析-》添加记录，然后在记录值的部分增加自己的额ip即可

打开宝塔面板，依次点击网站，添加站点

![在这里插入图片描述](bcb512e2cd2a1e112706a4647232a8aa.png)

输入刚才创建的二级域名，设置根目录，创建网站

![img](9fe31cfb0ec98899417cd58d16cc6ec7.png)

## 6. 配置SSL

现在我们的网站还是 http 开头，会被标识为不安全，所以需要配置 SSL ,将 http 转化为 https.

如图所示，依次点击

![在这里插入图片描述](a4bf6585a38233e5e1e3aceb29fca434.png)

选择域名，点击申请。申请成功后点击强制 https

![在这里插入图片描述](24ab5fc13f3a2f5400b671b6175d5794.png)

**http 运行在 80 端口，而 https 运行在 443 端口。强制 https 后会打开 443端口，但这个并不会生效。**

所以我们需要先关闭 443 端口，再重新打开 443 端口。

在安全页面，删除 443 端口，再放行 443 端口

![在这里插入图片描述](ce41c542a42bb6fadc5ecd60531e8a64.png)

现在就可以用 你的域名来访问博客了
