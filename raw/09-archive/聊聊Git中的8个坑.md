---
title: "聊聊Git中的8个坑"
source: "https://mp.weixin.qq.com/s/iJPVjPBWqI-OjtxicQP9mA"
---
苏三 苏三说技术 *2026年9月3日 08:20*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

对于程序员来说，Git是最常用的软件之一。

Git这东西，用好了是神器，用不好就是灾难。

今天这篇文章，盘了一下这些年在项目里遇到过的Git“坑”，挑出8个最常见的，跟大家好好聊聊。

希望对你会有所帮助。

## 一、git reset --hard 丢了代码

### 1.1 场景重现

> 有些小伙伴在工作中可能遇到过这样的场景：改了一堆代码，突然发现方向错了，想回到之前的某个版本。你很自信地敲了 `git reset --hard HEAD~3` ，然后——发现写了两天的代码全没了。

这不是段子，这是真事。

### 1.2 为什么会出现这个问题？

`git reset --hard` 是Git里最危险的操作之一。

它的作用是： **把当前分支的HEAD指针移到指定提交，同时强制更新工作目录和暂存区** 。

用最直白的话说，它会 **物理删除** 你工作目录里所有“多余”的文件和改动。

### 1.3 正确解法

**解法一：用 `git reflog` 救回来**

只要你还没执行 `git gc` （垃圾回收），所有的提交记录其实都还在Git的数据库里。

`git reflog` 记录了本地仓库的所有HEAD变动，包括reset之前的操作。

```
# 查看所有操作记录
git reflog

# 找到reset之前的commit hash，比如abc123
git reset --hard abc123
```

**解法二：用 `git reset --soft` 或 `git reset --mixed` 代替**

```
# --soft：只移动HEAD，保留暂存区和工作目录
git reset --soft HEAD~3

# --mixed（默认）：移动HEAD，重置暂存区，保留工作目录
git reset HEAD~3
```

**核心原则** ：

- 想丢弃修改用 `git checkout -- <file>` ，别用 `reset --hard`
- 每次 `reset` 之前先看一眼 `git status`
- 不确定的时候就先用 `git stash` 把改动存起来

**底层原理** ：Git的每次提交都是一个完整的快照，不会真正“删除”任何东西。

`reset` 只是移动了分支指针，被“丢弃”的提交在Git的垃圾回收机制运行前一直存在。

`git reflog` 就是找回它们的保险绳。

## 二、合并冲突解决后忘记提交

### 2.1 场景重现

解决完一个复杂的合并冲突，你松了口气，心想“总算搞定了”。

然后你切到另一个分支去处理别的任务。

等你切回来的时候，发现冲突标记还在文件里，之前辛辛苦苦解决的冲突全白干了，而且 **有的文件被改乱了，你甚至不知道哪些冲突已经解决过** 。

### 2.2 为什么会出现这个问题？

Git的工作区（Working Directory）是独立于分支的。

你切分支的时候，如果工作区有未提交的修改，Git的行为取决于这些修改是否会与新分支冲突。

如果切换目标分支没有修改这些文件，Git会 **直接带走未提交的修改** 。

**但问题在于** ：解决冲突留下的标记（ `<<<<<<<` 、 `>>>>>>>` ）不算“修改”——它们是文件内容的一部分。

Git不会帮你清理这些标记，也不会提醒你“还有冲突标记没处理”。

### 2.3 正确解法

**解法一：养成习惯——解决完冲突立即 `git commit`**

```
# 解决冲突后立即提交
git add .
git commit -m "合并XXX分支，解决冲突"
```

**解法二：用 `git merge --abort` 撤销合并**

如果在解决冲突的过程中你发现自己搞不定了，或者切错分支了：

```
# 完全撤销本次合并，回到合并前的状态
git merge --abort
```

这个命令会撤销一切，回到执行 `git merge` 之前的状态，不会留下任何冲突标记。

**解法三：用 `git stash` 暂存未提交的修改**

```
# 暂存当前所有未提交的修改
git stash push -u -m "正在解决冲突中，切分支处理紧急bug"

# 切换分支处理紧急事务
git checkout hotfix

# 处理完切回来，恢复工作状态
git checkout feature-branch
git stash pop
```

**核心原则** ：

- 解决完冲突 **立即提交** ，别拖
- 不确定的时候用 `git merge --abort` 安全退出
- 临时中断用 `git stash` 而不是硬切

## 三、git stash pop 冲突导致stash丢失

### 3.1 场景重现

你 `git stash push` 把代码暂存起来了。

切完分支回来，执行 `git stash pop` 想把代码恢复，结果 **啪，冲突了** 。

更糟糕的是，你发现 **stash里的内容也不见了** 。

### 3.2 为什么会出现这个问题？

`git stash pop` 等于 `git stash apply` + `git stash drop` 两条命令的合并。

如果应用时发生了冲突，Git只执行了 `git stash apply` ，然后把stash留在了栈里。

但从用户视角看，冲突发生了，stash好像也不见了，问题就卡住了。

### 3.3 正确解法

```
# 查看stash还在不在（大概率还在）
git stash list

# 如果冲突已经解决，手动清理stash
git stash drop

# 如果冲突还没解决，可以用git stash show查看stash里的内容
git stash show -p stash@{0}
```

**核心原则** ：

- 用 `git stash apply` 代替 `git stash pop`
- apply之后确认没问题，再手动 `git stash drop`
- 这样就算有冲突，stash也还在，可以重新apply

## 四、git push --force 覆盖了别人的代码

### 4.1 场景重现

> “我push的时候提示冲突了，我就用 `git push --force` 了一下，然后同事说他写的代码没了，这是怎么回事？”

这是团队Git协作里最常见、最严重的错误。

### 4.2 为什么会出现这个问题？

`git push --force` 的语义是： **把本地仓库的分支状态直接覆盖远程仓库** ，不做任何检查。

如果你的本地分支落后于远程， `--force` 会用旧数据强行覆盖新数据， **同事已经push上去的代码会被永久抹除** 。

### 4.3 正确解法

**解法一：用 `--force-with-lease` 代替 `--force`**

```
# 安全替代方案：只有在远程分支没有被其他人更新过的情况下才推送
git push --force-with-lease
```

`--force-with-lease` 会检查远程分支是否和你上次拉取时一致。

如果远程分支已经被别人更新了，推送会直接失败，提示你先pull。

**解法二：先pull再push，永远不用--force**

```
# 先拉取最新代码
git pull --rebase

# 再推送（用普通push）
git push
```

**核心原则** ：

- **绝对不用 `git push --force`**
- 用 `--force-with-lease` 替代
- push前先看一眼 `git status`

**底层原理** ： `git push --force` 是“盲写”，而 `--force-with-lease` 是“带条件地写”——只有在远程分支状态和自己预期一致时才执行强制推送。

## 五、git rebase 把分支基线搞错了

### 5.1 场景重现

你准备把feature分支变基到最新的master上，结果把master变基到了feature上。

整个master的分支线被分岔了，其他人的工作全乱套了。

### 5.2 正确解法

```
# 正确的rebase用法：站在feature分支，变基到master
git checkout feature
git rebase master

# 错误的用法：站在master，变基到feature（千万别干！）
git checkout master
git rebase feature  # ❌ 这一行会搞乱master的历史
```

**如果已经做了错误的rebase：**

```
# 用git reflog找到rebase之前的位置，用git reset --hard恢复到操作前的提交
git reflog
git reset --hard <commit-hash>
```

**核心原则** ：

- rebase的是 **当前分支** ， **目标分支** 不变
- 先切到要动的分支，再执行rebase
- 已经推送到远程的分支尽量不要rebase（会把远程协作变成灾难）

## 六、git cherry-pick 冲突处理的误区

### 6.1 场景重现

你cherry-pick了一个commit，发现冲突了，手动改完文件之后，直接执行 `git commit -m "xxx"` 。

然后发现cherry-pick的状态还没结束，提交历史变得乱七八糟。

### 6.2 正确解法

```
# 正确的cherry-pick冲突处理流程
git cherry-pick abc123

# 如果有冲突，解决冲突后
git add .

# 继续cherry-pick（而不是直接commit）
git cherry-pick --continue

# 如果搞乱了，可以撤销
git cherry-pick --abort
```

**核心区别** ： `git commit` 和 `git cherry-pick --continue` 都会产生一个新提交，但 `--continue` 会保留cherry-pick的元信息（作者、时间、提交信息）并正确完成操作。

直接 `git commit` 会中断cherry-pick流程，导致操作不完整。

## 七、git branch -D 误删分支

### 7.1 场景重现

你删了一个以为自己不需要的分支，结果发现上面还有几个重要的commit没合并。

直接 `git branch -D feature` ，分支没了，commit也找不到了。

### 7.2 正确解法

```
# 删除分支前先用-d检查是否已合并
git branch -d feature  # 安全删除：只删除已合并的分支

# 强制删除前确认
git branch -D feature  # 危险命令

# 如果已经误删，用reflog找回
git reflog
# 找到分支最后一次commit的hash
git checkout -b feature <commit-hash>
```

**底层原理** ：Git的分支本质上只是指向某个commit的指针。

删除分支只是删除了这个指针，commit本身还在（直到垃圾回收）。

所以误删分支通常可以找回，关键是不要拖太久。

## 八、git commit --amend 推送后的问题

### 8.1 场景重现

你刚推送了一个commit到远程，突然发现漏了一个文件，或者提交信息写错了。

你很自然地执行了 `git commit --amend` ，然后 `git push` ，结果被拒绝了。

### 8.2 为什么会出现这个问题？

`git commit --amend` 会创建一个 **新的commit** ，替换掉当前的commit。

**commit的hash会变** 。

而远程仓库的分支还指向旧的commit。当你执行 `git push` 时，Git发现你本地的commit历史和远程不一致，于是拒绝推送。

更麻烦的是，如果其他人已经基于旧的commit做了工作，你的变基会让团队协作乱套。

### 8.3 正确解法

**解法一：还没push，随便amend**

```
git add .
git commit --amend -m "新的提交信息"
```

**解法二：已经push了，绝对不要amend**

```
# ❌ 错误做法
git commit --amend
git push --force  # 千万不要！会覆盖远程历史

# ✅ 正确做法：追加一个新的修复commit
git add .
git commit -m "fix: 补充遗漏的文件"
git push
```

**核心原则** ：

- `amend` 只适用于 **还没push到远程** 的commit
- 已经push的commit，用追加commit替代amend
- 如果一定要改，用 `git push --force-with-lease` ，但 **仅限于你一个人使用该分支** 的情况

## 九、Git操作速查表

| 操作 | 安全做法 | 危险做法 | 原因 |
| --- | --- | --- | --- |
| **回退代码** | `git reset --soft` | `git reset --hard` | \--hard会删除工作目录改动 |
| **推送覆盖** | `git push --force-with-lease` | `git push --force` | \--force会覆盖别人代码 |
| **删除分支** | `git branch -d` | `git branch -D` | \-D不检查是否已合并 |
| **恢复stash** | `git stash apply`  \+ `git stash drop` | `git stash pop` | pop冲突时会丢stash |
| **提交修正** | `git commit --amend`  （未推送时） | `git commit --amend`  （已推送后） | 已推送的amend会改变历史 |
| **合并冲突中断** | `git merge --abort` | 直接 `git commit` | 直接commit会留下冲突标记 |
| **暂存工作** | `git stash push -u` | 直接切分支 | 直接切可能带脏工作区 |

## 十、写在最后

在版本控制的世界里， **最大的误区就是以为Git会自动保护你** 。

事实恰恰相反—— **工具越强大，误操作的成本就越高** 。

`reset --hard` 删除的是物理文件， `push --force` 抹除的是团队协作的历史记录， `git commit --amend` 改变的是已经发布的事实。

我见过被 `git push --force` 搞得被迫回退整个版本的大项目，也见过 `git stash pop` 搞丢了一整周工作量的案例。

这些事之所以反复发生，不是开发者不够小心，而是Git的设计本身给了你一把能拆房子的锤子——你看到的是“撤销”，它执行的是“抹除”。

如果你从这篇文章带走一句话，我希望是： **每次操作Git之前，先看一眼 `git status` 。**

它能告诉你你在哪个分支、工作区是否干净、有没有未跟踪的文件——这些信息能帮你避开90%的坑。

养成习惯，比学会所有命令更重要。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)