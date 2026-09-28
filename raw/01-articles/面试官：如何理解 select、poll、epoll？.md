---
title: "面试官：如何理解 select、poll、epoll？"
source: "https://mp.weixin.qq.com/s/gN6dApg57xQNf7CLbKT37w"
---
犬小哈 小哈学Java *2026年9月27日 10:00*

将 小哈学Java设为“ **星标** **⭐** ”

第一时间收到文章更新

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E5%A6%82%E4%BD%95%E7%90%86%E8%A7%A3%20select%E3%80%81poll%E3%80%81epoll%EF%BC%9F/f2ec1b961f9a3e80ba7cb1c709ff615e_MD5.webp)

**在线 Java 面试刷题（已更新334题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

## 面试考察点

1. **IO 多路复用的本质理解** ：面试官不仅仅是想知道三个 API 的区别，更是想看你是否理解 “一个线程监听多个 socket” 这个需求是怎么一步步演化解决的。
2. **性能瓶颈的分析能力** ：select 为什么慢？慢在哪？poll 改了什么、没改什么？epoll 又解决了什么？这条演化线能不能讲清楚，直接暴露你的功力。
3. **联系实际框架** ：Java NIO 的 `Selector` 、Netty、Redis、Nginx 底层都靠这套机制。能不能把八股文落到实际项目，一聊就知道了。

## 核心答案

先说结论： **select、poll、epoll 都是 IO 多路复用的实现方案，核心目标就一个：让单个线程同时监听多个文件描述符（socket），谁的内核数据准备好了就通知谁，避免为每个连接开一个线程干等。**

三者是演进关系，一张表看懂：

| 对比项 | select | poll | epoll |
| --- | --- | --- | --- |
| 发布时间 | 1983 年（4.2BSD） | 1986 年（System V） | 2002 年（Linux 2.5.44，2.6 正式可用） |
| 跨平台 | ✅ 几乎所有平台 | ✅ Unix 系 | ❌ Linux 专属（对应 macOS 的 kqueue、Windows 的 IOCP） |
| fd 数量上限 | `FD_SETSIZE`  \= 1024 | 无硬限制（链表存储） | 无硬限制（受限于系统内存） |
| fd 传递方式 | 每次调用全量拷贝到内核 | 每次调用全量拷贝到内核 | `epoll_ctl`  注册一次，内核长期维护 |
| 内核检测方式 | 线性扫描所有 fd | 线性扫描所有 fd | 事件回调，只返回就绪的 fd |
| 时间复杂度 | O(n) | O(n) | epoll\_wait 对就绪集合接近 O(1) |
| 每次调用后 | 必须重置 `fd_set` | 不需要重置 | 不需要重置 |
| 适用场景 | 连接数少、跨平台 | 连接数中等 | 连接数巨大、活跃比例低（万级连接常态） |

一句话总结演进逻辑： **select 有数量上限还有全量拷贝的开销，poll 解决了数量上限，epoll 把 “全量拷贝 + 全量扫描” 两个瓶颈全干掉了。**

![select poll epoll 演进关系](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E5%A6%82%E4%BD%95%E7%90%86%E8%A7%A3%20select%E3%80%81poll%E3%80%81epoll%EF%BC%9F/16e32113b69b58a9659c1cb6b1183961_MD5.jpg)

select poll epoll 演进关系

## 深度解析

### 一、为什么需要 IO 多路复用

先补个背景，不然这三个东西不好理解。

假设你写了一个 TCP 服务器，同时有 1000 个客户端连上来。最朴素的做法：一个连接配一个线程，每个线程调 `read()` 阻塞等着读数据。

问题立马来了：

- 1000 个连接就是 1000 个线程，内存和上下文切换开销都顶不住
- 大部分时间这些连接根本没数据，线程全在那干等，纯浪费

那能不能一个线程同时盯着 1000 个 socket？谁有数据了我就处理谁，这就是 **IO 多路复用** 。select、poll、epoll 就是实现这个目标的三个方案，一个比一个强。

### 二、select：元老级方案

select 是 1983 年随 4.2BSD 发布的老将，思路很直接：

```
int select(int nfds,
           fd_set *readfds,    // 关注可读事件的 fd 集合
           fd_set *writefds,   // 关注可写事件的 fd 集合
           fd_set *exceptfds,  // 关注异常事件的 fd 集合
           struct timeval *timeout);
```

它用一张 `fd_set` 位图（bitmap）来记录要监听的 fd，操作位图的宏你肯定见过： `FD_ZERO` 、 `FD_SET` 、 `FD_CLR` 、 `FD_ISSET` 。

一次 select 调用的流程：

1. 应用程序把 `fd_set` 从用户空间 **全量拷贝** 到内核空间
2. 内核 **线性扫描** 每个 fd，检查它的数据是否就绪
3. 有就绪的就返回，没有就阻塞（或超时返回）
4. 返回后， `fd_set` 已被内核改写（没就绪的位被清掉了），应用程序要 **线性扫描** 找出哪些 fd 就绪了
5. 想继续监听？把 `fd_set` 重新设置一遍，再来一轮

这套流程有三个致命伤：

- **1024 上限** ： `fd_set` 是固定长度的位图， `FD_SETSIZE` 默认 1024，想改只能重新编译 glibc，实际没人这么干
- **重复的全量拷贝** ：哪怕 1000 个 fd 里只有 1 个活跃，每次调用都要把整张位图拷进内核
- **重复的线性扫描** ：内核扫一遍，用户态还得再扫一遍，两头都是 O(n)

还有一个容易忽略的坑：因为内核会修改传入的 `fd_set` ，每次调用前都得用 `FD_ZERO` + `FD_SET` 重新构建一遍，写起来特别啰嗦。

![select 全量拷贝和线性扫描](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E5%A6%82%E4%BD%95%E7%90%86%E8%A7%A3%20select%E3%80%81poll%E3%80%81epoll%EF%BC%9F/54bd7adde2ccc257e113aefcb82e0114_MD5.jpg)

select 全量拷贝和线性扫描

### 三、poll：select 的改良版

poll 出现在 System V 里，针对 select 的位图结构做了改良：

```
struct pollfd {
    int fd;         // 要监听的 fd
    short events;   // 关注的事件
    short revents;  // 内核填写的实际发生事件
};

int poll(struct pollfd *fds, nfds_t nfds, int timeout);
```

关键改进有两点：

- **换成了 pollfd 数组** ：数组长度自定义，突破了 1024 的数量上限
- **事件和结果分离** ： `events` 由用户设置， `revents` 由内核填写，两者分开存。这样每次调用后不用重新设置关注的事件，比 select 舒服多了

但说实话，poll 只动了皮毛。每次调用依然要把整个数组全量拷贝进内核，内核依然要线性扫描所有 fd， **O(n) 的本质一点没变** 。连接数一上去，开销照样爆炸。所以 poll 更像是个过渡方案，真正的革命者是 epoll。

![poll 数组和 O(n) 开销](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E5%A6%82%E4%BD%95%E7%90%86%E8%A7%A3%20select%E3%80%81poll%E3%80%81epoll%EF%BC%9F/57072389fa122cf09b725d6c47eb9de2_MD5.jpg)

poll 数组和 O(n) 开销

### 四、epoll：Linux 的杀手锏

epoll 是 Linux 2.5.44 引入（2002 年）、2.6 内核正式可用的方案，Redis、Nginx 的高并发底气全靠它。跟 select/poll 的 “一次调用干所有事” 不同，epoll 拆成了三个系统调用，各管一段：

```
// 1. 创建 epoll 实例，返回一个 epfd
int epoll_create(int size);

// 2. 注册/修改/删除要监听的 fd（ADD / MOD / DEL）
int epoll_ctl(int epfd, int op, int fd, struct epoll_event *event);

// 3. 等待事件发生，只返回就绪的 fd
int epoll_wait(int epfd, struct epoll_event *events,
               int maxevents, int timeout);
```

整个流程画出来是这样：

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E5%A6%82%E4%BD%95%E7%90%86%E8%A7%A3%20select%E3%80%81poll%E3%80%81epoll%EF%BC%9F/928ded5492e55209a48bdce3cdfb0bfb_MD5.jpg)

上图是 epoll 的完整工作流程，拆开看关键设计：

- **注册与等待分离** ： `epoll_ctl` 把 fd 注册进内核的红黑树，信息在内核里长期保存。之后每次 `epoll_wait` 不需要重新传入监听列表，全量拷贝的问题直接消失
- **红黑树管理 fd** ：增删改 fd 都是 O(log n)，查找高效，还能天然去重
- **事件回调代替轮询** ：数据到达时，内核通过中断触发挂在该 socket 上的回调 `ep_poll_callback` ，把就绪的 fd 挂到就绪链表（rdllist）上。内核不用再挨个问 “你有数据吗”
- **只返回就绪的 fd** ： `epoll_wait` 拿到的就是就绪列表本身，应用程序不用再从 10000 个 fd 里筛出那 10 个活跃的
![epoll 红黑树和就绪链表](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E5%A6%82%E4%BD%95%E7%90%86%E8%A7%A3%20select%E3%80%81poll%E3%80%81epoll%EF%BC%9F/a74a605c6595bbcd7bf57798a911e115_MD5.jpg)

epoll 红黑树和就绪链表

这里必须辟个谣：网上很多文章说 “epoll 用 mmap 共享内存减少拷贝”， **这是错的** 。epoll 并没有用 mmap， `epoll_wait` 返回时就绪事件依然要从内核拷贝到用户空间，只是拷贝量从 “全部 fd” 变成了 “就绪 fd”。这一点面试官要是追问，答错了会很减分。

### 五、三者性能对比

用一张图直观感受一下，假设 10000 个连接、其中 100 个活跃：

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E5%A6%82%E4%BD%95%E7%90%86%E8%A7%A3%20select%E3%80%81poll%E3%80%81epoll%EF%BC%9F/2b988f2fe09c224fa5eb9b79df2f642d_MD5.jpg)

两边的差距一目了然：

- select/poll 的工作量跟 **总连接数** 挂钩，连接越多越惨，而且每次调用都要重复付出
- epoll 的工作量跟 **活跃连接数** 挂钩，10 万连接里 1000 个活跃，开销就只有这 1000 的量级

这也解释了为什么说 “epoll 适合连接数多但活跃少的长连接场景”（比如即时通讯、推送系统）。反过来，如果连接数不多但几乎全活跃，epoll 相比 poll 的优势就不明显了——毕竟红黑树和回调机制本身也有维护成本。

### 六、LT 与 ET：epoll 的两种触发模式

这是面试官最爱挖的深水区。epoll 有两种工作模式：

| 模式 | 全称 | 触发时机 | 特点 |
| --- | --- | --- | --- |
| LT（水平触发） | Level-Triggered | 只要缓冲区还有数据，每次 `epoll_wait` 都会通知 | 默认模式，可以分次读写，编程简单 |
| ET（边缘触发） | Edge-Triggered | 仅在状态变化那一刻通知一次（比如新数据到达） | 必须一次把数据读写干净（循环处理到 `EAGAIN` ），配合非阻塞 fd 使用 |

打个比方：LT 像一个贴心的助理，只要你桌上还有没处理的文件，他每次路过都会提醒你；ET 像一个高冷的助理，只在 “新文件放上来” 那一瞬间喊你一嗓子，处理没处理干净他不管。

ET 模式减少了重复通知的次数，效率更高，但编程复杂度也上去了：\*\*必须搭配非阻塞 fd，循环 `read` 直到返回 `EAGAIN` \*\*，否则残留数据再也不会被通知，就丢事件了。Nginx 用的就是 ET 模式。

![epoll LT 和 ET 触发模式](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E5%A6%82%E4%BD%95%E7%90%86%E8%A7%A3%20select%E3%80%81poll%E3%80%81epoll%EF%BC%9F/babd8ffbfbf97302e4b3db255c5ac271_MD5.jpg)

epoll LT 和 ET 触发模式

还有个相关的知识点：Redis 6.0 之前一直是单线程处理命令，但照样扛住 10 万+ QPS，靠的就是 epoll（LT 模式）+ 事件驱动那套 “单线程 Reactor” 模型。

### 七、和 Java 体系的关系

作为 Java 工程师，光懂 C 接口还不够，得知道这套东西怎么落到我们身边：

- **Java NIO** ： `Selector` 就是 IO 多路复用的 JDK 封装。JVM 会根据操作系统选实现：Linux 2.6+ 用 epoll，Windows 上用 `select` （WinSock 实现），macOS 用 kqueue。你写的是同一套 `              Selector.open()            ` 、 `select()` 、 `selectedKeys()` ，底层自动适配
- **Netty** ：除了 NIO 的 `NioEventLoopGroup` ，还提供了 `EpollEventLoopGroup` ，直接走 JNI 调用 Linux 原生 epoll，省掉 JDK 层的封装开销，还能用到 `SO_REUSEPORT` 等特性。Linux 生产环境用 Netty，强烈建议换成 Epoll 系列
- **Redis / Nginx** ：Redis 的 ae 事件循环在 Linux 上就是 epoll；Nginx 的高并发就是靠 epoll + ET 模式撑起来的

面试时把 select/poll/epoll 讲完，再主动带一句 “Java NIO 的 Selector 底层就是这套机制”，主动权就到自己手里了。

## 面试高频追问

1. **追问一：epoll 一定比 select/poll 快吗？**

不一定。连接数少且几乎全活跃的场景下，epoll 的回调机制和红黑树维护反而是额外开销，select/poll 表现不差。epoll 的主场是 “连接数巨大 + 活跃比例低” 的长连接场景。

2. **追问二：epoll\_wait 为什么快？**

因为它不做扫描，只检查就绪链表 rdllist。链表非空就拷贝就绪事件返回，空就阻塞。工作量只和就绪 fd 数量相关，跟总连接数无关。

3. **追问三：select 的 1024 限制能改吗？**

能改 `FD_SETSIZE` 后重新编译 glibc，但没人这么干——位图全量拷贝和线性扫描的 O(n) 开销还在，改了上限也扛不住大连接数，不如直接换 epoll。顺带说一句，这个 1024 是 glibc 用户态的定义，内核本身没做这个限制，知道这一层算加分项。

4. **追问四：ET 模式为什么必须配非阻塞 fd？**

ET 只通知一次，你必须循环读直到读完。如果用阻塞 fd，最后一次 `read` （缓冲区已空）会直接阻塞线程，整个事件循环卡死。非阻塞 fd 空读会返回 `EAGAIN` ，循环才能正常退出。

5. **追问五：水平触发和边缘触发，Nginx 和 Redis 分别用哪个？**

Nginx 用 ET（效率优先，自己控制读写循环），Redis 用 LT（编程简单可靠，事件循环单线程不宜复杂化）。

## 常见面试变体

- 变体一：“IO 多路复用和 BIO、NIO、AIO 的关系是什么？”
- 变体二：“epoll 用了什么数据结构？为什么选红黑树？”
- 变体三：“Reactor 模式和 epoll 是什么关系？单 Reactor 单线程、多线程、主从 Reactor 分别怎么配？”
- 变体四：“Netty 的 `EventLoop` 和 epoll 是什么关系？”

## 记忆口诀

**三代演进** ：select 位图限一千，poll 数组破上限，epoll 红黑树上挂回调。

**epoll 三板斧** ： `create` 建实例、 `ctl` 挂红黑树、 `wait` 收就绪链表。

**两个模式** ：LT 没读完就一直喊，ET 只喊一嗓子（记得一口气读完）。

## 总结

一句话：select、poll、epoll 都是 IO 多路复用方案，让一个线程盯住海量连接。select 有 1024 上限且两头全量扫描，poll 破了上限但没破 O(n)，epoll 用红黑树 + 就绪链表 + 事件回调把开销降到只和活跃连接数相关，是 Linux 高并发的基石。再把 LT/ET 和 Java NIO、Netty 的关系串起来，这道题你就赢麻了。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E5%A6%82%E4%BD%95%E7%90%86%E8%A7%A3%20select%E3%80%81poll%E3%80%81epoll%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 服务器被入侵怎么办？看我操作3. 分库分表，可能真的要退出历史舞台了！4. 面试官：有用过 Dubbo 的异步调用吗？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

Java 面试题 | 八股文汇总 · 目录

阅读原文