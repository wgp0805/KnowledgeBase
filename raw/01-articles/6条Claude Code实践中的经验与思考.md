---
title: "6条Claude Code实践中的经验与思考"
source: "https://mp.weixin.qq.com/s/uoX8fEIUPX7p5FwWEtU9jA"
author:
  - "[[二师兄]]"
published:
created: 2026-05-19
description: "随着Claude Code使用的越来越多，实践经验和感受也在逐步累积，而且对AI Coding的理解和感知也在不断的发生着变化。希望这一切都能与大家分享，共同探讨。"
tags:
  - "clippings"
---
二师兄 *2026年5月7日 07:00*

## Claude Code系列回顾

目前在实践和应用Claude Code，顺便分享一些在实践过程中的经验，没想竟然写成一个系列了。如果你也对Claude Code感兴趣，可以先回顾一下之前的文章，然后开始今天的文章。

第1篇：《 [国内环境下的Claude Code安装与使用教程](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078571&idx=1&sn=c64cf5ad80192b3edfaa92d7e719dc06&scene=21#wechat_redirect) 》

第2篇：《 [使用Claude Code最需要做的一件事：与AI签订一份契约（](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078583&idx=1&sn=7aaec3eed61957b6f42681dc89604045&scene=21#wechat_redirect) [CLAUDE.md）](http://claude.md\)/) 》

第3篇：《 [Claude Code实践：从零开始，一行代码不写生成一个项目](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078609&idx=1&sn=00b81ef0ee9936fd8b5b5bce1c0ed5ad&scene=21#wechat_redirect) 》

第4篇：《 [Claude Code的Skills实践及利器推荐：工欲善其事，必先利其器](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078644&idx=1&sn=d5dd4cb82f5bb3ded9687140f88a6295&scene=21#wechat_redirect) 》

## 前言

随着Claude Code使用的越来越多，实践经验和感受也在逐步累积，而且对AI Coding的理解和感知也在不断的发生着变化。希望这一切都能与大家分享，共同探讨。

在这篇文章中，重点会聊一聊两方面的内容：第一，Claude Code实战中的一些技巧，当然技巧是需要练习和实践的，当你看完相关的文章之后，还是要动手的；第二，AI对编程以及行业的改变，当使用AI Coding越多，也能够感知到AI对编程的冲击，当你了解它有多强大时，才会知道它有多可怕。

下面是这篇文章与你分享的6条经验和思考：

## 01、能用插件尽量使用插件

这一条很简单，就是在AI Coding的过程中，如果能用现成的插件或Skills，那就尽量使用现成的。在《 [Claude Code的Skills实践及利器推荐：工欲善其事，必先利其器](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078644&idx=1&sn=d5dd4cb82f5bb3ded9687140f88a6295&scene=21#wechat_redirect) 》一文中，我们专门介绍了Superpowers这款插件，这里再次推荐，非常好用。

用插件的好处是，插件本身实现的Workflow（工作流）可以极大的规避模型的幻觉，让编码的过程极具工业化标准化，像工业生产线一样。而且，优秀的插件或Skills本身就是集大成于一身，汇集了大量优秀开发人员的成果。

相比使用优秀的插件，自己用不够清晰，逻辑不够全面的语言来描述，开发效率和输出的真的天差地别。有的人说AI Coding好用，有的人说AI Coding不好用，这一条导致这一评价两极化的核心原因之一。

## 02、工程师要具备Leader的能力

之前，工程师的核心工作在于理解需求，想清楚怎么实现，然后一行一行的编写代码。随着AI Coding的发展，工程师的工作方式发生了变化。

工程师需要具备的能力变为：理解需求，拆分任务，定义任务目标，然后把任务用自然语言（文字）描述出来，然后在与AI的不断沟通中完成任务（管理任务），最终还要检查任务是否执行成功。

在之前的编程范式中，工程师是执行者，在新的AI Coding范式中，工程师更像是一个小领导，需要任务管理，需要与下属反复沟通，需要拍板做选择，需要验收结果等。

这里的角色改变以及相应的能力改变是巨大的，你可以仔细感受一下，此时，具有清晰有逻辑的语言（或文字）表达能力的人将非常具有竞争优势。

## 03、任务拆分越细越好

这条可以说是实践过程中的必备技能了，任务不仅要描述清晰，而且还需要粒度适中。模型本身的幻觉导致它可能会犯错，用户的描述缺失可能会导致模型有更大的“发挥空间”，多Agent之间的错误传递和放大效应会导致结果差了十万八千里。

因此，细粒度的拆分任务变得非常必要。既可以保证模型在有限的空间内进行最小化的修改，又可以保证在出现错误时能够及时回滚。

以用户管理为例，个人在实践的过程中，甚至会精确到增、删、改、查每个页面和逻辑的沟通。先与AI沟通设计用户表，设计完成验证没问题就可以提交一次commit，然后适时clear上下文（减少token消耗，减少模型上下文过多导致的错误）。

然后再描述列表展示逻辑和UI风格，AI执行完，启动验证，再提交一次commit和clear。这里附带一个技巧就是做好版本管理，以便AI走的太偏时回滚重来，当然，如果你用Superpowers插件，它会帮你自动做这一步。

虽然这样比较繁琐，但这种逐步迭代，“结硬寨，打打仗”的模式，反而更适合在复杂业务中进行编程。当然，如果你的AI Coding经验已经非常丰富，则可以适当的放宽任务的粒度。

## 04、尽量培养完全AI Coding的感觉

在AI Coding的过程中，有时候有很小的修改，比如修改一个文案，修改一个菜单的排序，修改一个样式风格，修改一个小功能。对于这样的修改，经验丰富的开发者在IDE中分分钟就可以直接修改代码搞定。那么，此时你会作何选择？

对于我来说，我倾向于选择让AI来改，哪怕只是修改一个文案。为什么呢？就是培养完全的AI Coding的感觉。当你把自己“逼”到必须用AI，自己不手动改一行代码的时候，你才真正能够体验到AI Coding的感觉，而且这种感觉会越来越上头，你也能够修炼出一项新的能力。试想，要做一个好的领导是不是就是只指导下属如何改，那怕只是改一个字，也不会亲自替下属动手的。

既然要做AI Coding，那就要全然的去做。当然，如果是老旧项目以及涉及到资金安全等相关的项目，可能需要更慎重一些，酌情考虑。

## 05、编程经验依旧非常重要

在网络充斥着大量的无编程经验使用AI Coding实现项目的案例，但个人在实践的过程中却有不一样的感受，那就是，编程经验（包括架构设计经验）依旧非常非常重要。

因为在使用AI Coding的时候，AI会给出不同的方案选择，如果你没有一点编程经验，甚至看不懂AI给出的方案有什么利弊，是否适合当前的项目。

![方案选择](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

方案选择

以上图为例，虽然已经给出了非常明确的优缺点，但如果对这些框架没有基础的了解和认识，还是很难做出针对当前项目合理的选择的。

这只是一个示例，不一定贴切，如果你进行一段时间AI Coding后，你会发现，AI 让你做的每一个抉择，都像是你的下属在与沟通一个问题的解决方案，如果你不懂，你就很难跟它沟通明白，让它做的符合你的预期。

虽然你不用写代码，但你不能不懂功能应该怎么设计，代码应该怎么写。

## 06 尽量培养自己的产品感觉

AI Coding让代码变得廉价，开发人员的一部分价值（甚至是大部分价值）被AI替代，开发成本变得极低。那么，作为相关从业人员，真正区分一个人的能力的标志就是是否具有产品感觉，是否对一个行业有深入的理解。

当AI把开发的门槛抹平之后，行业经验（行业Know-How），Idea的好坏判断，产品实现的感觉就被放大了。当你拥有了产品感觉，产品能力，这个时代对于你来说便是最好的创业时代，最好的实现自己想法的时代。

![口号的变化](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

口号的变化

最后附带编程时代与AI时代的两个口号的变化，之前是“Talk is cheap. Show me the code.”，现在是“Code is cheap. Show me the the talk(prompt).”

全文完，感谢阅读，如果喜欢请三连。

近期精选文章：

- [Claude Code的Skills实践及利器推荐：工欲善其事，必先利其器](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078644&idx=1&sn=d5dd4cb82f5bb3ded9687140f88a6295&scene=21#wechat_redirect)
- [Claude Code实践：从零开始，一行代码不写生成一个项目](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078609&idx=1&sn=00b81ef0ee9936fd8b5b5bce1c0ed5ad&scene=21#wechat_redirect)
- [使用Claude Code最需要做的一件事：与AI签订一份契约（CLAUDE.md）](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078583&idx=1&sn=7aaec3eed61957b6f42681dc89604045&scene=21#wechat_redirect)
- [国内环境下的Claude Code安装与使用教程](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078571&idx=1&sn=c64cf5ad80192b3edfaa92d7e719dc06&scene=21#wechat_redirect)
- [写作和思考，应该被AI改变么？](https://mp.weixin.qq.com/s?__biz=MzI0NDAzMzIyNQ==&mid=2654078555&idx=1&sn=5f0e668424711c340751c42eb4603780&scene=21#wechat_redirect)

---

**▲** **”师兄奇谈** **“：职场&生活&自我提升**

**个人书籍：** **《Spring Boot技术内幕》&&** **《Drools 8规则引擎》**

**微信号：541075754**

**作者新书—— **《Drools 8规则引擎》：****

![图片](data:image/svg+xml,%3C%3Fxml version='1.0' encoding='UTF-8'%3F%3E%3Csvg width='1px' height='1px' viewBox='0 0 1 1' version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'%3E%3Ctitle%3E%3C/title%3E%3Cg stroke='none' stroke-width='1' fill='none' fill-rule='evenodd' fill-opacity='0'%3E%3Cg transform='translate(-249.000000, -126.000000)' fill='%23FFFFFF'%3E%3Crect x='249' y='126' width='1' height='1'%3E%3C/rect%3E%3C/g%3E%3C/g%3E%3C/svg%3E)

AI&amp;LLM · 目录

继续滑动看下一个

师兄奇谈

向上滑动看下一个