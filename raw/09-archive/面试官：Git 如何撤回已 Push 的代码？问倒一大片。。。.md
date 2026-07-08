---
title: "面试官：Git 如何撤回已 Push 的代码？问倒一大片。。。"
source: "https://mp.weixin.qq.com/s/W9JhURFEDSTGB5aH19g44g"
---
小哈学Java *2026年7月8日 14:05*

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/515ff7207a96d46a0e161b34e5cbf1b5_MD5.webp)

来源： [https://juejin.cn/post/7307066452290043958](https://juejin.cn/post/7307066452290043958)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 背景
- 方案一：手动复制恢复
- 方案二：git revert commit
- 方案三：基于旧提交新建分支
- 方案四：reset current branch 到指定 commit
- 总结建议

在日常的开发中，我们经常使用Git来进行版本控制。有时候，我们可能会不小心将错误的代码 Push 到远程仓库，或者想要在本地回退到之前的某个版本重新开发。

或者像我一样，写了一些感觉以后很有用的优化方案push到线上，又接到了一个新的需求。但是呢，项目比较重要，没有经过测试的方案不能轻易上线，为了承接需求只能先把push上去的优化方案先下掉。

现在我的分支是这样的，我想要在本地和远程仓库中都恢复到 **help文档提交** 的部分。

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/63144734fc40418b842363f2e8521a8a_MD5.webp)

[image.png](http://image.png/)

## 1.基础的手动操作（比较笨，不推荐）

> “
> 
> 这样的操作非常不推荐，但是如果你不了解git，确实是我们最容易理解的方式。

如果你的错误代码不是很多，那么你其实可以通过与你想要恢复到的commit进行对比，然后手动删除错误代码，然后删除不同的代码。

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/271289f58fe4cc667b85a01611040462_MD5.jpg)

[image.png](http://image.png/)

> “
> 
> 按住 ctrl 选择想要对比的两个commit，然后选择 **Compare Versions** 就能通过对比删除掉你想要删除的代码。

这个方案在代码很简单时时非常有效的，甚至还能通过删除后最新commit和想要退回的commit在 **Compare** 一下保障代码一致。

但是这个方法对于代码比较复杂的情况来说就不太好处理了，如果涉及到繁杂的配置文件，那更是让人头疼。只能通过反复的Compare Version来进行对比。

**这样的手动操作显然显得有些笨拙了，对此git有一套较为优雅的操作流程，同样能解决这个问题。**

## 2\. git Revert Commit（推荐）

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/733ab54a8cd157bad984464ccd4271aa_MD5.jpg)

[image.png](http://image.png/)

同样的，我第三次提交了错误代码，并且已经push到远程分支。想要撤回这部分代码，只需要 **右键点击错误提交记录**

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/8cfe04631ab9c827f813730bd3e54730_MD5.jpg)

[image.png](http://image.png/)

git自动产生一个Revert记录，然后我们会看到git自动将我第三次错误提交代码回退了，这个其实就相当于git帮我们手动回退了代码。

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/58e4bfa2fb847fcda1ce07d4e4032e61_MD5.jpg)

[image.png](http://image.png/)

后续，只需要我们将本次改动 **push到远程，即可完成一次这次回退操作，**

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/ba24d422eda600806aa538469542612b_MD5.jpg)

[image.png](http://image.png/)

> “
> 
> **revert相当于自动帮我们进行版本回退操作，并且留下改动记录，非常安全。这也是评论区各位大佬非常推荐的。**

但是revert还是存在一点不足，即一次仅能回退一次push。如果我们有几十次甚至上百次的记录，一次次的单击回退不仅费时费力而且还留下了每次的回退记录，我个人觉得 `revert` 在这种情况下又不太优雅。

## 3\. 增加新分支（推荐撤回较多情况下使用)

如果真的需要回退到上百次提交之前的版本，我的建议是直接新建个分支。

**在想要回到的版本处的提交记录右键，点击new branch**

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/af60e26ae4756a7179bef1fe82eb868c_MD5.jpg)

> “
> 
> 新建分支的操作仅仅增加了一个分支，既能保留原来的版本，又能安全回退到想要回退的版本，同时不会产生太多的回退记录。
> 
> 但是此操作仍然建议慎用，因为这个操作执行多了，分支管理就又成了一大难题。

## 4\. Reset Current Branch 到你想要恢复的commit记录（不太安全，慎用）

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/25348d098acfb16b90daa54e1cea1b64_MD5.jpg)

[image.png](http://image.png/)

这个时候会跳出四个选项供你选择，我这里是选择 **hard** 。

其他选项的含义 **仅供参考** ，因为我也没有一一尝试过。

> “
> 
> 1. **Soft** ：你之前写的不会改变，你之前暂存过的文件还在暂存。
> 2. **Mixed** ：你之前写的不会改变，你之前暂存过的文件不会暂存。
> 3. **Hard** ：文件恢复到所选提交状态，任何更改都会丢失。 **你已经提交了，然后你又在本地更改了，如果你选hard，那么提交的内容和你提交后又本地修改未提交的内容都会丢失。**
> 4. **keep** ：任何本地更改都将丢失，文件将恢复到所选提交的状态，但本地更改将保持不变。 **你已经提交了，然后你又在本地更改了，如果你选keep，那么提交的内容会丢失，你提交后又本地修改未提交的内容不会丢失。**

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/6d165489cb83a7bde17d067b0c9bee85_MD5.jpg)

[image.png](http://image.png/)

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/c55e1ad59e24c22e976434f0d13be999_MD5.jpg)

[image.png](http://image.png/)

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/e5d7d52f0c5dc82b4b57f453337e7ea1_MD5.jpg)

[image.png](http://image.png/)

然后，之前错误提交的commit就在本地给干掉了。但是远程仓库中的提交还是原来的样子，你要把目前状态同步到远程仓库。 **也就是需要把那几个commit删除的操作push过去。**

打开push界面，虽然没有commit需要提交，需要点击 **Force Push** ![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/c55e1ad59e24c22e976434f0d13be999_MD5.jpg)

需要注意的是对于一些被保护的分支，这个操作是不能进行的。需要自行查看配置，我这里因为不是master分支，所以没有保护。

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/7f3ce5375e8e0ba9492269ced42e2e2a_MD5.jpg)

[image.png](http://image.png/)

可以看到，远程仓库中最新的commit只有我们的 **help文档** 。在其上的三个提交都没了。

![image.png](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/a86ecfc32bb5a7b5fd5037f9eaeaaebc_MD5.jpg)

[image.png](http://image.png/)

**注意:以上使用的是2023版IDEA,如果有出入的话可以考虑搜索使用git命令。**

## 好书推荐

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/0b0b8e4468575af50171f20d53078cc3_MD5.jpg)

操作入门+核心设计+实战演练+进阶展望，从人设定义到记忆系统，从知识库到工作流编排，图解优先化繁为简，实践驱动即学即练，从零上手Coze智能体开发。

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/9069539af9175935863a94fc28764ede_MD5.jpg)

一键解锁AI驱动的学术新范式，从文献综述到论文发表，让研究更高效、更智能！

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%20%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2%20Push%20%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87%E3%80%82%E3%80%82%E3%80%82/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 美团二面：Agent、Tools、Workflow 这三个的概念和区别介绍一下？我：没接触过...3. Claude Code从失控到起飞，只用了这些技巧。。。4. 面试官：满足什么条件时，一个 Java 类会被卸载？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文