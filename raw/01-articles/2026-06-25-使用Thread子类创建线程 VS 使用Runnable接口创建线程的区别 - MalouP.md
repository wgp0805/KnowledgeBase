---
title: "使用Thread子类创建线程 VS 使用Runnable接口创建线程的区别 - MalouP"
source: "博客园"
url: "https://www.cnblogs.com/mhpblog/p/20778612/thread-vs-runnable-java-multithreading"
date: "2026-06-24T10:49:00Z"
score: 0.4
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 使用Thread子类创建线程 VS 使用Runnable接口创建线程的区别 - MalouP

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/mhpblog/p/20778612/thread-vs-runnable-java-multithreading  
> **抓取日期**: 2026-06-25  
> **相关性评分**: 0.4

  * [ ![博客园logo](//assets.cnblogs.com/logo.svg) ](<https://www.cnblogs.com/> "开发者的网上家园")
  * [会员](<https://cnblogs.vip/>)
  * [周边](<https://cnblogs.vip/store>)
  * [新闻](<https://news.cnblogs.com/>)
  * [博问](<https://q.cnblogs.com/>)
  * [闪存](<https://ing.cnblogs.com/>)
  * [赞助商](<https://www.cnblogs.com/cmt/p/19316348>)
  * [Chat2DB](<https://chat2db-ai.com/>)


  * ![搜索](//assets.cnblogs.com/icons/search.svg) ![搜索](//assets.cnblogs.com/icons/enter.svg)
    * ![搜索](//assets.cnblogs.com/icons/search.svg)

所有博客
    * ![搜索](//assets.cnblogs.com/icons/search.svg)

当前博客
  * [ ![写随笔](//assets.cnblogs.com/icons/newpost.svg) ](<https://i.cnblogs.com/EditPosts.aspx?opt=1> "写随笔") [ ![我的博客](//assets.cnblogs.com/icons/myblog.svg) ](<https://www.cnblogs.com/my> "我的博客") [ ![短消息](//assets.cnblogs.com/icons/message.svg) ](<https://msg.cnblogs.com/> "短消息") [ ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg) ](<javascript:void\(0\)> "简洁模式启用，您在访问他人博客时会使用简洁款皮肤展示")

[ ![用户头像](//assets.cnblogs.com/icons/avatar-default.svg) ](<https://home.cnblogs.com/>)

[我的博客](<https://www.cnblogs.com/my>) [我的园子](<https://home.cnblogs.com/>) [账号设置](<https://account.cnblogs.com/settings/account>) [会员中心](<https://vip.cnblogs.com/my>) [ 简洁模式 ... ](<javascript:void\(0\)> "简洁模式会使用简洁款皮肤显示所有博客") [退出登录](<javascript:void\(0\)>)

[注册](<https://account.cnblogs.com/signup>) [登录](<javascript:void\(0\);>)



[![返回主页](/skins/custom/images/logo.gif)](<https://www.cnblogs.com/mhpblog/>)

# [小bo波](<https://www.cnblogs.com/mhpblog>)

## 

  * [ 博客园](<https://www.cnblogs.com/>)
  * [ 首页](<https://www.cnblogs.com/mhpblog/>)
  * [ 新随笔](<https://i.cnblogs.com/EditPosts.aspx?opt=1>)
  * [ 联系](<https://msg.cnblogs.com/send/MalouP>)
  * [ 订阅](<javascript:void\(0\)>)
  * [ 管理](<https://i.cnblogs.com/>)



#  [ 使用Thread子类创建线程 VS 使用Runnable接口创建线程的区别 ](<https://www.cnblogs.com/mhpblog/p/20778612/thread-vs-runnable-java-multithreading> "发布于 2026-06-24 18:48")

Java中创建线程的两种方式——继承Thread类与实现Runnable接口，表面上是语法差异，实则是设计思想的根本不同。本文从代码耦合性、资源共享、继承限制、源码层面等多个维度深入对比两者的区别，并结合售票系统等经典场景说明为什么"组合优于继承"，帮助读者理解Java并发编程中"职责分离"的核心设计原则。 

## 一、两种创建线程的方式

在Java中，创建线程主要有两种方式：

### 方式一：继承 Thread 类
    
    
    class MyThread extends Thread {
        @Override
        public void run() {
            System.out.println("当前线程：" + Thread.currentThread().getName());
        }
    }
    
    // 使用
    MyThread t = new MyThread();
    t.start();
    

### 方式二：实现 Runnable 接口
    
    
    class MyRunnable implements Runnable {
        @Override
        public void run() {
            System.out.println("当前线程：" + Thread.currentThread().getName());
        }
    }
    
    // 使用
    Thread t = new Thread(new MyRunnable());
    t.start();
    

* * *

## 二、核心区别对比

对比维度 | 继承 Thread 类 | 实现 Runnable 接口  
---|---|---  
**代码耦合性** | 线程与任务逻辑强耦合 | 任务与线程解耦，更灵活  
**资源共享** | 多个线程各自独立，难以共享数据 | 同一个 Runnable 实例可被多个线程共享  
**继承限制** | Java 单继承，无法再继承其他类 | 不影响继承其他类，可再实现多个接口  
**代码复用** | 任务逻辑与线程绑定，复用性差 | 任务作为独立对象，可被任意线程执行  
**设计思想** | 面向继承（"is-a" 关系） | 面向组合（"has-a" 关系），更符合设计原则  
**异常处理** | 无法向调用方抛出 checked 异常 | 同样无法抛出，但可通过 Callable + Future 解决  
  
* * *

## 三、深入分析：为什么更推荐 Runnable？

### 1\. 解耦：任务与执行分离

`Runnable` 代表**任务（Task）** ，`Thread` 代表**执行器（Executor）** 。将两者分离是优秀的设计：
    
    
    // 任务定义
    Runnable task = () -> System.out.println("执行任务");
    
    // 可以交给 Thread 执行
    new Thread(task).start();
    
    // 也可以交给线程池执行（这才是生产环境的标准做法）
    ExecutorService pool = Executors.newFixedThreadPool(4);
    pool.submit(task);
    

如果使用继承 Thread，任务就无法交给线程池执行，灵活性大打折扣。

### 2\. 资源共享的经典场景

假设有一个售票系统，多个窗口同时售票：
    
    
    class TicketTask implements Runnable {
        private int tickets = 100;  // 共享的票池
    
        @Override
        public void run() {
            while (tickets > 0) {
                System.out.println(Thread.currentThread().getName() + " 售出第 " + tickets-- + " 张票");
            }
        }
    }
    
    // 三个窗口共享同一个票池
    TicketTask task = new TicketTask();
    new Thread(task, "窗口1").start();
    new Thread(task, "窗口2").start();
    new Thread(task, "窗口3").start();
    

如果用继承 Thread，每个线程对象都有自己的 `tickets` 变量，无法实现共享。

### 3\. 符合"组合优于继承"原则

> 《Effective Java》第18条：**Favor composition over inheritance.**

`Runnable` 是组合思想的体现：线程"拥有"一个可运行的任务，而不是线程"是"一个任务。

* * *

## 四、源码层面的理解

看看 `Thread` 类的核心源码：
    
    
    public class Thread implements Runnable {
        private Runnable target;  // 持有一个 Runnable 对象
    
        @Override
        public void run() {
            if (target != null) {
                target.run();  // 委托给 target 执行
            }
        }
    }
    

**关键洞察：**

  * `Thread` 本身也实现了 `Runnable` 接口
  * 继承 Thread 并重写 `run()`，相当于**自己实现任务逻辑**
  * 传入 Runnable，相当于**把任务委托给外部对象**



无论哪种方式，最终都是调用 `run()` 方法，但设计哲学截然不同。

* * *

## 五、实际开发中的选择建议

场景 | 推荐方式  
---|---  
简单测试、快速验证 | 继承 Thread（代码量少）  
生产环境、正式项目 | **实现 Runnable / 使用线程池**  
需要返回执行结果 | 使用 `Callable<T>` \+ `Future<T>`  
需要定时/周期性任务 | 使用 `ScheduledExecutorService`  
大规模并发任务 | 使用 `ForkJoinPool` 或并行流  
  
* * *

## 六、总结

> **继承 Thread 是"把线程当任务"，实现 Runnable 是"把任务给线程执行"。**

在Java并发编程中，**实现 Runnable 接口是更优雅、更灵活、更符合设计原则的选择** 。它让任务与线程解耦，便于资源共享，也为后续使用线程池、CompletableFuture 等高级并发工具奠定了基础。

理解这个区别，不仅是掌握一个语法点，更是理解 **"职责分离"** 这一软件设计核心思想的开始。

* * *

> **参考资料：**
> 
>   * 《Java并发编程实战》
>   * 《Effective Java》第3版
>   * [JDK 17 Thread 源码](<https://github.com/openjdk/jdk/blob/master/src/java.base/share/classes/java/lang/Thread.java>)
> 


posted @ 2026-06-24 18:48  [MalouP](<https://www.cnblogs.com/mhpblog>)  阅读(33)  评论(0)    [收藏](<javascript:void\(0\)>)  [举报](<https://report.cnblogs.com?targetLink=https%3A%2F%2Fwww.cnblogs.com%2Fmhpblog%2Fp%2F20778612%2Fthread-vs-runnable-java-multithreading&targetId=20778612&targetType=0>)

刷新页面返回顶部

[ ![](assets/2026-06-25-%E4%BD%BF%E7%94%A8Thread%E5%AD%90%E7%B1%BB%E5%88%9B%E5%BB%BA%E7%BA%BF%E7%A8%8B%20VS%20%E4%BD%BF%E7%94%A8Runnable%E6%8E%A5%E5%8F%A3%E5%88%9B%E5%BB%BA%E7%BA%BF%E7%A8%8B%E7%9A%84%E5%8C%BA%E5%88%AB%20-%20MalouP/31f2f8bc4f9df511b9d79843cbce27cf_MD5.webp) ](<https://www.volcengine.com/activity/codingplan?utm_campaign=hw&utm_content=hw&utm_medium=devrel_tool_web&utm_source=OWO&utm_term=cnblogs>)

### 公告

[博客园](<https://www.cnblogs.com/>)  ©  2004-2026   
[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](<http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771>) [浙ICP备2021040463号-3](<https://beian.miit.gov.cn>)


---
> 原文链接: https://www.cnblogs.com/mhpblog/p/20778612/thread-vs-runnable-java-multithreading