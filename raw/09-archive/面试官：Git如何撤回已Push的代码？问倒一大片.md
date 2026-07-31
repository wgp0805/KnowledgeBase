---
title: "面试官：Git如何撤回已Push的代码？问倒一大片"
source: "https://mp.weixin.qq.com/s/if7w5v-CaK9CJ97UKMvI2A"
---
终码一生 *2026年7月30日 22:34*

点击“终码一生”，关注，置顶公众号

每日技术干货，第一时间送达！

面试官问：Git 如何撤回已 Push 的代码？ 如果问你，你会吗？

在日常的开发中，我们经常使用Git来进行版本控制。有时候，我们可能会不小心将错误的代码 Push 到远程仓库，或者想要在本地回退到之前的某个版本重新开发。

或者像我一样，写了一些感觉以后很有用的优化方案push到线上，又接到了一个新的需求。但是呢，项目比较重要，没有经过测试的方案不能轻易上线，为了承接需求只能先把push上去的优化方案先下掉。

现在我的分支是这样的，我想要在本地和远程仓库中都恢复到 help文档提交 的部分。

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2Push%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87/cbcaaf22f406380157c49da576b866f9_MD5.webp)

01

基础的手动操作（比较笨，不推荐）

这样的操作非常不推荐，但是如果你不了解git，确实是我们最容易理解的方式。

如果你的错误代码不是很多，那么你其实可以通过与你想要恢复到的commit进行对比，然后手动删除错误代码，然后删除不同的代码。

按住 ctrl 选择想要对比的两个commit，然后选择 Compare Versions 就能通过对比删除掉你想要删除的代码。

这个方案在代码很简单时时非常有效的，甚至还能通过删除后最新commit和想要退回的commit在 Compare 一下保障代码一致。

但是这个方法对于代码比较复杂的情况来说就不太好处理了，如果涉及到繁杂的配置文件，那更是让人头疼。只能通过反复的Compare Version来进行对比。

这样的手动操作显然显得有些笨拙了，对此git有一套较为优雅的操作流程，同样能解决这个问题。

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2Push%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87/e3415148a9018e581714e7cf7e6c0289_MD5.png)

02

git Revert Commit（推荐）

同样的，我第三次提交了错误代码，并且已经push到远程分支。想要撤回这部分代码，只需要 右键点击错误提交记录

git自动产生一个Revert记录，然后我们会看到git自动将我第三次错误提交代码回退了，这个其实就相当于git帮我们手动回退了代码。

后续，只需要我们将本次改动 push到远程，即可完成一次这次回退操作，

revert相当于自动帮我们进行版本回退操作，并且留下改动记录，非常安全。这也是评论区各位大佬非常推荐的。

但是revert还是存在一点不足，即一次仅能回退一次push。如果我们有几十次甚至上百次的记录，一次次的单击回退不仅费时费力而且还留下了每次的回退记录，我个人觉得 revert 在这种情况下又不太优雅。

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2Push%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87/e3415148a9018e581714e7cf7e6c0289_MD5.png)

03

增加新分支（推荐撤回较多情况下使用)

如果真的需要回退到上百次提交之前的版本，我的建议是直接新建个分支。

在想要回到的版本处的提交记录右键，点击new branch

新建分支的操作仅仅增加了一个分支，既能保留原来的版本，又能安全回退到想要回退的版本，同时不会产生太多的回退记录。

但是此操作仍然建议慎用，因为这个操作执行多了，分支管理就又成了一大难题。

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9AGit%E5%A6%82%E4%BD%95%E6%92%A4%E5%9B%9E%E5%B7%B2Push%E7%9A%84%E4%BB%A3%E7%A0%81%EF%BC%9F%E9%97%AE%E5%80%92%E4%B8%80%E5%A4%A7%E7%89%87/e3415148a9018e581714e7cf7e6c0289_MD5.png)

04

Reset Current Branch 到你想要恢复的commit记录（不太安全，慎用）

这个时候会跳出四个选项供你选择，我这里是选择 hard 。

其他选项的含义 仅供参考 ，因为我也没有一一尝试过。

- Soft ：你之前写的不会改变，你之前暂存过的文件还在暂存。
- Mixed ：你之前写的不会改变，你之前暂存过的文件不会暂存。
- Hard ：文件恢复到所选提交状态，任何更改都会丢失。 你已经提交了，然后你又在本地更改了，如果你选hard，那么提交的内容和你提交后又本地修改未提交的内容都会丢失。
- keep ：任何本地更改都将丢失，文件将恢复到所选提交的状态，但本地更改将保持不变。 你已经提交了，然后你又在本地更改了，如果你选keep，那么提交的内容会丢失，你提交后又本地修改未提交的内容不会丢失。

然后，之前错误提交的commit就在本地给干掉了。但是远程仓库中的提交还是原来的样子，你要把目前状态同步到远程仓库。 也就是需要把那几个commit删除的操作push过去。

打开push界面，虽然没有commit需要提交，需要点击 Force Push ，强推过去。需要注意的是对于一些被保护的分支，这个操作是不能进行的。需要自行查看配置，我这里因为不是master分支，所以没有保护。

可以看到，远程仓库中最新的commit只有我们的 help文档 。在其上的三个提交都没了。

注意:以上使用的是2023版IDEA,如果有出入的话可以考虑搜索使用git命令

来源： [juejin.cn/post/7307066452290043958](http://juejin.cn/post/7307066452290043958)

—END—

**PS：防止找不到本篇文章，可以收藏点赞，方便翻阅查找哦。**

往期推荐[Jetbrains 里最好用的 AI Coding 插件，强烈推荐！！](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540099&idx=1&sn=bf3b12a66f9a35358578faaa8c4b7ee0&scene=21#wechat_redirect)[13秒插入30万条数据，这才是批量插入正确的姿势！](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540099&idx=2&sn=62459fa98abc1396413f5517775405a7&scene=21#wechat_redirect)[用雪花 id 和 uuid 做 MySQL 主键，被领导怼了](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540093&idx=1&sn=63336785e209ad0360ffba695bc1ff57&scene=21#wechat_redirect)[SpringBoot+OnlyOffice：优雅实现在线 Word 编辑、转化、保存等功能](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540093&idx=2&sn=296153bcb4d27b6e7bf4bcb4ab46eeb9&scene=21#wechat_redirect)[我宣布，AI编程终于不用"更快地生产漏洞"了！！](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540045&idx=1&sn=9d8a37ff62c7cf8abceec4fdf8fafd8d&scene=21#wechat_redirect)[面试官：一台服务器最大能支持多少条TCP连接？问倒一大片。。。](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540028&idx=1&sn=e30f2452afcb37fa1cdc9757ebb852ac&scene=21#wechat_redirect)

git · 目录

阅读原文