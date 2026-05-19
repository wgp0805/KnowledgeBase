---
title: git推送远程方法
tags:
  - git
categories:
  - git
date: 2022-06-23 18:30:42
---

1.初始化：创建一个git仓库，创建之后就会在当前目录生成一个.git的文件

```
git init
```

2.添加文件：把文件添加到缓冲区

```
git add filename
```

3.添加所有文件到缓冲区（从目前掌握的水平看，和后面加“.”的区别在于，加all可以添加被手动删除的文件，而加“.”不行）：

```
git add .
git add --all
```

4.提交：提交缓冲区的所有修改到仓库(注意：如果修改了文件但是没有add到缓冲区，也是不会被提交的)

```
git commit -m "提交的说明"
```

5.推送到远程分支

```
git push origin master
```

6.如果vscode每次都要输入账号密码,在控制台执行命令:

```
git config --global credential.helper store
```

再次输入账号密码重启命令

PS1:指定仓库的推送

```
git remote add origin git@github.com:michaelliao/learngit.git #添加远程仓库
git push -u origin master #初始化推送
git push origin master #提交主分支
```

PS2: 使用vscode拉取代码提示：在签出前，请清理存储库工作树

解决方法：

```
1、git stash （把当前未提交的修改暂存起来，让仓库还原到最后一次提交的状态。）
2、git pull （拉取远程仓库的代码，让你现在的代码和远程仓库一致）
3、git stash pop （恢复第一步储存起来的代码，也就是恢复当前未提交的修改）
```

## git更新

1.如果本地当前分支设置了上游分支通过：git branch -vv 查看、后运行：git pull 即可更新最新代码
2.如果没有设置上游分支可先设置上游分支：git branch -u origin/分支名、再执行：git pull。
3.直接执行：git pull origin 分支名。

### git回退

查看版本

> git log

可以看到有很多版本，每个版本的第一行是commit接一串字符串（部分打码了） 。要退出git log只需要按Q键。

2、选择想要回退到的版本，复制commit后面的一串字符串

3、输入命令

> **git reset --hard** 字符串

比如我复制图上第一个commit后的字符串，其结果如下：

> HEAD is now at 2b345e3 RobotRotate 夹具和关节一起动

## git 合并代码

一、git 如何把分支代码合并到master
 1.首先切换到分支；
 	git checkout hellomonkey
 2.使用git pull 把分支代码pull下来；
 	git pull
 3.切换到主分支；
    git checkout master
 4.把分支的代码merge到主分支；
    git merge hellomonkey
 5.git push推上去ok完成,现在 你自己分支的代码就合并到主分支上了。
    git push
 同样，主分支的文件也可以合并的分支上。 
二、git 如何把master分支代码合并到自己的分支
 master分支的代码领先自己的分支,git 如何把master分支代码合并到自己的分支
 1.首先切换到主分支
    git checkout master
 2.使用git pull 把领先的主分支代码pull下来
    git pull
 3.切换到自己的分支
    git checkout xxx(自己的分支)
 4.把主分支的代码merge到自己的分支
    git merge master
 5.git push推上去ok完成,现在 你自己分支的代码就和主分支的代码一样了
    git push origin 自己分支名

### git 本地分支推送其他仓库

可以同时提交到多个远程代码仓库，包括 GitHub 和码云（Gitee）等。
首先，在本地使用 Git 克隆 GitHub 上的代码仓库，然后将其添加为本地 Git 仓库的远程仓库：

```
# 添加码云的仓库作为远程仓库
git remote add gitee https://gitee.com/user/repo.git  

# 克隆 GitHub 上的代码仓库
git clone https://github.com/user/repo.git  
```

在这个例子中，我们添加了一个名为 gitee 的远程仓库，其 URL 是码云上对应仓库的地址。在将代码推送到远程仓库时，可以使用 Git 的 push 命令：
```
 # 推送代码到 GitHub
git push -u origin "main" 
 # 推送代码到码云
git push -u gitee "main"   
# 这里的-u是啥意思暂时还不清楚
```

这将会将代码分别推送到 GitHub 和码云上。
需要注意的是，在同时推送到多个远程仓库时，如果两个仓库的代码在某些地方产生了冲突，需要手动解决冲突后再进行推送。此外，如果同时使用多个远程仓库，需要时刻保持代码的同步，以避免出现分歧和错误。
