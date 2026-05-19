---
title: git常用命令
tags:
  - git
categories:
  - git
date: 2023-06-07 08:28:39
---

# 1. 初始化

您可以通过键入以下内容来初始化当前目录中的 Git 版本控制系统：

```
git init
```

或者，您可以在特定目录中初始化 Git。

```
git init <directory>
```

![image-20230607083004767](image-20230607083004767.png)

# 2. 克隆

**clone** 命令会将所有项目文件从远程服务器复制到本地计算机。它还将添加一个远程名称作为“源”，以将文件与远程服务器同步。

Git 克隆需要 HTTPS 链接和安全连接 SSH 链接。

```
git clone <HTTPS/SSH>
```

# 3. 添加遥控器

您可以通过添加远程名称和 HTTPS/SSH 地址来连接到单个或多个远程服务器。

```
git remote add <remote name> <HTTPS/SSH>
```

> **注意：**从 GitHub 或任何远程服务器克隆存储库会自动将远程添加为“源”。

# 4. 创建分支

分支是处理新功能或调试代码的最佳方式。它允许您在不干扰“主”分支的情况下隔离工作。

基本 Git 概念

默认分支名称：main

默认远程名称：origin

当前分支参考：HEAD

HEAD 的父级：HEAD^ 或 HEAD~1

HEAD 的祖父母：HEAD^^ 或 HEAD~2

使用带有“-b”标记和分支名称的 **checkout** 命令创建新分支。

```
git checkout -b <branch-name>
```

或者使用带有“-c”标签和分支名称的**开关**

```
git switch -c <branch-name>
```

或者干脆使用**分支**命令

```
git branch <branch-name>
```

![image-20230607083033342](image-20230607083033342.png)

有用的标志：

-a：显示所有分支（本地和远程）

-r：显示远程分支

-v：显示最后一次提交的分支

# 5. 切换分支

要将分支从当前分支切换到其他分支，可以使用**签出**或**切换**命令，后跟分支名称。

```
git checkout <branch-name>

git switch <branch-name>
```

# 6. 拉动

要将更改与远程服务器同步，我们需要首先使用 **pull** 命令将更改从远程拉取到本地存储库。在远程存储库中进行更改时，这是必需的。

```
git pull
```

您可以添加远程名称后跟分支名称以拉取单个分支。

```
git pull <remote name> <branch> 
```

默认情况下，pull 命令提取更改并将其与当前分支合并。要变基，您可以在远程名称和分支之前添加“--rebase”标志，而不是合并。

```
git pull --rebase origin master
```

# 7. 添加

使用**添加**命令将文件添加到暂存区域。它需要文件名或文件名列表。

```
git add <file-name>
```

您还可以使用“.”或“-A”标志添加所有文件。

```
git add .
```

# 8. 提交

将文件添加到暂存区域后，可以使用**提交**命令创建版本。

提交命令需要使用“-m”标志来获取提交的标题。如果进行了多项更改并希望将它们全部列出，请使用另一个“-m”标志将它们添加到说明中。

```
git commit -m "Title" -m "Description"
```

![image-20230607083055356](image-20230607083055356.png)

如果要添加对跟踪文件所做的所有更改并提交。

```
git commit -a -m "<message>"# orgit commit -am "<message>"
```

> **注意：**在提交更改之前，请确保已配置**用户名**和**电子邮件**。

```
git config --global user.name <username>

git config --global user.email <youremail@yourdomain.com>
```

# 9. 推送

使用 **push** 命令将本地更改同步到远程服务器。您只需键入“git push”即可将更改推送到远程存储库。

要将更改推送到特定的远程服务器和分支，请使用以下命令。

```
git push <remote name> <branch-name>
```

# 10. 撤消提交

Git **还原**将更改撤消回特定提交，并将其添加为新提交，保持日志不变。要还原，您需要提供特定提交的哈希。

```
git revert <commit>
```

您还可以使用**重置**命令撤消更改。它将更改重置回特定提交，丢弃之后进行的所有提交。

```
git reset <commit>
```

> **注意：**不建议使用 reset 命令，因为它会修改您的 git 日志历史记录。

# 11. 合并

合并命令将简单地将特定分支的更改**合并**到当前分支中。该命令需要分支名称。

```
git merge <branch>
```

当您使用多个分支并希望将更改合并到主分支时，此命令非常方便。

--no-ff：即使合并解析为快进，也创建合并提交

--squash：将指定分支中的所有提交压缩为单个提交

建议不要使用 --squash 标志，因为它会将所有提交压缩为单个提交，从而导致提交历史混乱。

# 12. 日志

要检查以前提交的完整历史记录，可以使用 **log** 命令。

要显示最新的日志，您可以添加“-”后跟数字，它将显示有限数量的最近提交历史记录。

例如，将日志限制为 5：

```
git log -5
```

您还可以检查特定作者所做的提交。

```
git log --author=”<pattern>”
```

> **注意：**git log 有多个标志来过滤掉特定类型的提交。查看完整文档。

![image-20230607083125301](image-20230607083125301.png)

# 13. 区别

使用 **diff** 命令将显示未提交的更改与当前提交之间的比较。

```
git diff
```

要比较两个不同的提交，请使用：

```
git diff <commit1> <commit2>
```

要比较两个分支，请使用：

```
git diff <branch1> <branch2>
```

# 14. 状态

命令状态显示工作目录的当前**状态**。它包括有关要提交的更改、未合并的路径、未暂存的提交更改以及未跟踪文件列表的信息。

```
git status
```

# 15.从暂存区删除一个文件

```
git reset <file>
```

# 16.移动或重命名文件

```
git mv <current path> <new path>
```

您也可以仅使用 --cached 标志将其从暂存区中删除

```
git rm --cached <file>
```

# 17.从存储库中删除文件

```
git rm <file>
```

# 18.列出存储

```
git stash list
```

# 19.申请一个藏匿处

应用存储不会将其从存储列表中删除。

```
git stash apply <stash id>
```

如果不指定，将应用最新的 stash（适用于所有类似的 stash 命令）

您还可以使用格式 stash@{} 应用存储（适用于所有类似的存储命令）

```
git stash apply stash@{0}
```

# 20.删除一个藏匿处

```
git stash drop <stash id>
```

# 21.删除所有藏匿处

```
git stash clear
```

# 22.应用和删除存储

```
git stash pop <stash id>
```

