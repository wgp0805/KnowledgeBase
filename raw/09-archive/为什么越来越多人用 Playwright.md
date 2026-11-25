---
title: 为什么越来越多人用 Playwright？
source: https://mp.weixin.qq.com/s/BagUV7IiT_Fvuf-o9N2pQA
author:
  - "[[../../wiki/entities/苏三]]"
published:
created: 2026-11-25
description:
tags:
  - clippings
---
苏三 苏三说技术 *2026年11月25日 08:59*

## 大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

最近跟几位球友聊天，聊到一个有意思的现象：前几年大家做 UI 自动化，清一色 Selenium，没得选。

但这两年，不管是招人还是做技术选型，简历上不写点 Playwright 都不好意思说自己是搞自动化的。

今天这篇文章就专门跟大家一起聊聊Playwright，希望对你会有所帮助。

## 一、先说说 Selenium 那些年让我们加过的班

有些小伙伴在工作中可能遇到过这种场景：昨天跑得好好的用例，今天 Chrome 自动更新了，全线飘红。

你查了一上午，发现是 chromedriver 版本跟浏览器对不上。然后你手动下载驱动、改环境变量、重新跑，好了。

下个月，又来了。

这不是你代码写得烂，是 Selenium 的架构决定的。

Selenium 基于 W3C WebDriver 协议，客户端代码跟浏览器之间隔着一个驱动进程。

通信走的是 HTTP 短连接，每次操作都要：客户端 → 驱动 → 浏览器 → 驱动 → 客户端，来回五趟。

我画个时序图你就懂了：

![Mermaid 时序图：测试脚本](../../assets/为什么越来越多人用%20Playwright/file-20261125091502478.png)

Playwright 呢？

它走的是 WebSocket 长连接，一次握手，全程全双工通信。  

![Mermaid 流程图：Playwright 客户端 SDK](../../assets/为什么越来越多人用%20Playwright/file-20261125091502454.png)

Mermaid 流程图：Playwright 客户端 SDK

  
客户端直接跟 Playwright Server 对话，Server 再通过浏览器原生的 DevTools 协议（CDP）驱动内核。

**没有第三方驱动这个中间商赚差价。**

实测数据：同样打开百度搜索一个关键词，Selenium 平均 2.1 秒，Playwright 只要 0.7 秒。差了整整三倍。

## 二、自动等待：这才是 Playwright 真正封神的地方

如果只让我说一个 Playwright 最让人上瘾的特性，不是速度，是 **自动等待** 。

有些小伙伴在工作中写 Selenium 的时候，是不是经常这么干：

```
// Selenium 的经典写法
WebDriverWait wait = new WebDriverWait(driver, 
            Duration.ofSeconds(
          10));
WebElement button = 
            wait.until(
          
    
            ExpectedConditions.elementToBeClickable(By.id(
          "submit"))
);

            button.click();
```

或者更粗暴一点的：

```
Thread.sleep(
3000); // 别笑，我见过太多项目里全是这个

  driver.findElement(By.id(
"submit")).click();
```

`              Thread.sleep            ` 的问题在哪？ **你是在赌** 。赌 3 秒够不够，赌 CI 机器今天心情好不好。快的时候浪费 2.5 秒，慢的时候照样失败。这就是 flaky test 的万恶之源。

Playwright 的做法是：你直接调 `click`， **剩下的交给框架** 。

```
// Playwright Java 写法，一行搞定

            page.locator(
          "#submit").click();
```

这行代码背后发生了什么？

Playwright 在执行点击之前，会做一系列 **可操作性检查** ：

![图片](../../assets/为什么越来越多人用%20Playwright/file-20261125091502461.png)

这个“稳定”的判定很有意思：Playwright 会检查元素的 bounding box 是否连续两个动画帧没有移动过。

也就是说，如果有个弹窗正在滑入、有个 loading 动画正在转，它会 **继续等** ，直到元素真的停稳了再点。

有些小伙伴可能会问：那如果元素被一个 cookie 弹窗挡住了呢？

Playwright 也会检测到，它发现点击坐标上实际命中的是另一个元素，就会继续等待遮挡消失。

**这才是真正的智能等待。**

不是等一个固定时间，也不是等一个简单的 `presence` 条件，而是等“这个操作真的可以执行了”。

而且断言也一样。Selenium 里你写 `assert              element.isDisplayed()           `，元素没出来直接挂。Playwright 的 `expect(locator).toBeVisible()` 会 **自动重试直到超时** ，默认 5 秒内只要出现过就算通过。

```
// 错误示范：取出来再断言，没有重试
boolean visible = 
            page.locator(
          ".toast").isVisible();
assertTrue(visible); // 元素晚出来 100ms 就挂了

// 正确示范：Web-first 断言，自动重试
assertThat(
            page.locator(
          ".toast")).isVisible(); // 5秒内出现就算过
```

我在团队里做过统计， **仅仅把 Selenium 的显式等待换成 Playwright 的自动等待，用例的不稳定率从 12% 降到了 2% 以下** 。

## 三、浏览器上下文：并行测试的核武器

做 UI 自动化的都知道，最耗时的不是操作，是 **启动浏览器** 和 **隔离状态** 。

Selenium 的方案是每个测试启动一个全新的 driver 实例，开销大、速度慢。如果你想并行跑 10 个用例，就得开 10 个 Chrome 窗口，内存直接爆炸。

Playwright 引入了一个概念叫 **BrowserContext** 。它相当于一个“隐身窗口”——同一个浏览器进程里，可以创建 N 个完全隔离的上下文，每个有自己的 cookie、localStorage、sessionStorage，互不干扰。

![Mermaid 流程图：Browser 进程 只启动一次](../../assets/为什么越来越多人用%20Playwright/file-20261125091502470.png)

这意味着什么？

**一个浏览器进程，可以并行跑几十个测试** 。

每个 context 创建的开销极小，几乎可以忽略不计。而 Selenium 要开一个新窗口，就得新起一个 driver 进程。

而且这个特性在做 **多用户场景测试** 的时候简直是神器。比如你要测一个聊天功能：用户 A 发消息，用户 B 收到。

传统做法要开两个 driver，Playwright 里直接两个 context：

```
// 创建两个隔离的上下文，模拟两个用户
BrowserContext adminCtx = 
            browser.newContext();
          
BrowserContext userCtx = 
            browser.newContext();
          

Page admin = 
            adminCtx.newPage();
          
Page user = 
            userCtx.newPage();
          

            admin.navigate(
          "
            https://chat.example.com"
          );

            user.navigate(
          "
            https://chat.example.com"
          );

            admin.locator(
          "#message").fill("Hello");

            admin.locator(
          "#send").click();

// 用户侧收到消息，自动等待断言
assertThat(
            user.locator(
          ".message-bubble")).containsText("Hello");
```

两个用户完全隔离，但共享同一个浏览器进程。 **内存省了，速度还快了。**

## 四、网络拦截：从“做不到”到“一行代码”

有些小伙伴在工作中可能接过这种需求：测试一个支付流程，但不想真的调支付接口。

Selenium 时代怎么办？

要么起一个 mock server，要么用代理工具，折腾半天。

Playwright 把网络拦截做成了 **一等公民** 。

```
// 拦截所有支付请求，直接返回 mock 数据

            page.route(
          "**/api/pay", route -> {
    
            route.fulfill(
          new Route.FulfillOptions()
        .setStatus(200)
        .setBody("{\"code\": 0, \"msg\": \"success\"}")
    );
});

// 然后正常走支付流程，实际上根本没调真实接口

            page.locator(
          "#pay-button").click();
assertThat(
            page.locator(
          ".pay-success")).isVisible();
```

底层原理是 Playwright 通过 CDP 的 `Fetch` 域直接拦截浏览器网络栈的请求，在请求发出之前就能修改、伪造、或者阻断。这不是什么外挂手段，是 **浏览器内核原生支持的能力** 。

还有一个更实用的场景： **等待特定的网络请求完成** 。

Selenium 时代你只能 `              Thread.sleep            ` 或者轮询页面元素。Playwright 可以直接等请求：

```
// 在触发操作之前就开始等，避免竞态
var responseFuture = 
            page.waitForResponse(
          
    resp -> 
            resp.url().contains(
          "/api/order") && 
            resp.status()
           == 200
);

            page.locator(
          "#submit-order").click();

var response = 
            responseFuture.get();
           // 拿到响应了，确定接口已返回
assertThat(
            response.status()).isEqualTo(
          200);
```

这个模式彻底解决了“点击之后到底该等多久”的千古难题。 **等的是信号，不是时间。**

## 五、Trace Viewer：排查失败的时光机

这个功能，我愿称之为 **Playwright 最被低估的杀手锏** 。

Selenium 用例挂了，你能拿到什么？

一张截图，一段日志。

然后你盯着截图想：刚才到底发生了什么？是元素没出来？还是点错了位置？还是接口超时了？

Playwright 的 Trace Viewer 记录的是 **整个执行过程的时间线** ：每一步操作的 DOM 快照、网络请求、console 日志、光标位置，全部录下来。

用例失败后，你打开 trace 文件，可以像看视频回放一样，拖到任意时间点，看到当时的页面长什么样。

我在项目里推行 Playwright 之后， **排查 flaky 用例的平均时间从半天缩短到了十几分钟** 。因为不用猜了，直接看回放。

而且这个 trace 可以在 CI 里自动生成，失败了自动上传到制品库。

测试同学第二天上班，打开 trace 链接，拖进度条，一目了然。

## 六、优缺点和使用场景

吹了这么多，也得说说 Playwright 的短板。

**没有银弹，我们需要知道什么场景用什么工具。**

先上对比表：

| 维度 | Playwright | Selenium |
| --- | --- | --- |
| 首次发布 | 2020 年（微软） | 2004 年 |
| 通信协议 | WebSocket 长连接 + CDP/原生协议 | HTTP 短连接 + WebDriver |
| 自动等待 | 内置，可操作性检查 | 需手动实现 |
| 浏览器支持 | Chromium / Firefox / WebKit | 全浏览器含 IE11 |
| 移动端真机 | 仅模拟（视口/设备） | 通过 Appium 支持真机 |
| 语言支持 | Java / Python / JS / C# | Java / Python / JS / Ruby / C# / Kotlin |
| 生态成熟度 | 快速增长，但偏年轻 | 20 年积累，极成熟 |
| 执行速度 | 快（无驱动层，长连接） | 较慢（多层转发） |
| 调试体验 | Trace Viewer（时光机级别） | 截图 + 日志 |
| 并行能力 | 内置 BrowserContext 隔离 | 需 Grid 或框架支持 |

**Playwright 适合谁？**

第一， **新项目、新团队** 。如果你从零开始搭自动化体系，没有历史包袱，Playwright 是当前的最优解。Java 团队直接用 Playwright Java，API 设计干净，跟 JUnit 5 集成顺滑。

第二， **对稳定性要求高的场景** 。金融、电商这类 flaky test 成本很高的业务，自动等待 + Trace Viewer 的组合能省下大量排查时间。

第三， **需要多浏览器但不需要 IE 的项目** 。Chromium、Firefox、WebKit 三引擎覆盖了现代 Web 的 99% 场景。

**Selenium 仍然不可替代的场景：**

**需要测 IE11 或者老旧 Safari 的** 。Playwright 官方明确不支持 IE，这是硬边界。

**需要移动端真机测试的** 。Playwright 的移动端只是视口模拟，不是真机。真要测 Android/iOS 原生浏览器，还是得 Appium + Selenium 体系。

**已有大量 Selenium 资产且运行稳定的** 。迁移有成本，如果现有套件维护得好好的，没必要为了追新而重写。我建议的策略是： **新用例用 Playwright，旧用例不动，逐步替换最不稳定的那部分** 。

## 七、给 Java 小伙伴的入门代码

最后上一段完整的 Playwright Java 示例，把前面说的特性串起来。依赖就一个：

```
<dependency>
    <groupId>
            com.microsoft.playwright
          </groupId>
    <artifactId>playwright</artifactId>
    <version>1.49.0</version>
</dependency>
```

跑之前记得 `mvn exec:java -e -             Dexec.mainClass=com.microsoft.playwright.CLI            -             Dexec.args="install"           ` 装浏览器，Playwright 会自动下载适配版本的 Chromium/Firefox/WebKit， **再也不用手动管驱动版本了** 。

```
import 
            com.microsoft.playwright.*;
          
import 
            org.junit.jupiter.api.*;
          

import static 
            org.assertj.core.api.Assertions.assertThat;
          

public class LoginTest {

    static Playwright playwright;
    static Browser browser;
    BrowserContext context;
    Page page;

    @BeforeAll
    static void launchBrowser() {
        playwright = 
            Playwright.create();
          
        // 一行代码切换浏览器：chromium / firefox / webkit
        browser = 
            playwright.chromium().launch(
          
            new BrowserType.LaunchOptions().setHeadless(true)
        );
    }

    @BeforeEach
    void createContext() {
        // 每个测试一个全新上下文，天然隔离
        context = 
            browser.newContext();
          
        page = 
            context.newPage();
          
    }

    @Test
    void shouldLoginSuccessfully() {
        // 拦截后端登录接口，返回 mock 数据（不依赖真实环境）
        
            page.route(
          "**/api/login", route -> {
            
            route.fulfill(
          new Route.FulfillOptions()
                .setStatus(200)
                .setContentType("application/json")
                .setBody("{\"token\":\"mock-token\",\"username\":\"susan\"}")
            );
        });

        
            page.navigate(
          "
            https://your-app.example.com/login"
          );

        // 自动等待：元素可编辑、可点击后才会执行
        
            page.locator(
          "#username").fill("susan");
        
            page.locator(
          "#password").fill("secret");
        
            page.locator(
          "#login-btn").click();

        // Web-first 断言：自动重试，5 秒内出现即通过
        assertThat(
            page.locator(
          ".welcome-text")).containsText("susan");
    }

    @AfterEach
    void closeContext() {
        
            context.close();
           // 只关 context，浏览器进程复用
    }

    @AfterAll
    static void closeBrowser() {
        
            browser.close();
          
        
            playwright.close();
          
    }
}
```

这段代码里有三个细节值得注意：`route` 拦截让测试 **不依赖后端** ，`fill`/`click` 全自动等待让代码 **没有一行 sleep** ，`              context.close()            ` 而不是 `              browser.close()            ` 让浏览器进程 **跨测试复用** 。

三个点叠加，执行速度和不稳定性都会比同等 Selenium 代码好一个量级。

## 总结

回到标题的问题：为什么越来越多人用 Playwright？

我的答案很简单： **它不是 Selenium 的替代品，它是为现代 Web 重新设计的自动化工具。**

Selenium 诞生于 2004 年，那时候 Ajax 都还没普及，页面是静态的，等元素出来就是 `              Thread.sleep            ` 的事。

二十年过去了，Web 应用变成了 SPA、微前端、实时渲染，Selenium 的架构决定了它只能缝缝补补，而 Playwright 是从底层协议开始重新设计的。

三个核心优势，按重要性排序：

**第一，自动等待。** 这是最直接的体验提升，也是 flaky test 的根治方案。可操作性检查 + Web-first 断言，让“等多久”这个问题从代码里消失了。

**第二，架构代差。** WebSocket 长连接直连浏览器内核，没有驱动层，没有版本地狱，速度快、稳定性高、跨语言 API 统一。

**第三，调试体验。** Trace Viewer 是降维打击。用例失败不再靠猜，时间线回放直接把现场还原给你。

当然， **Selenium 不会死** 。IE11 还在一些企业内网跑着，Appium 的真机测试无可替代，二十年积累的生态不是一朝一夕能追上的。

但如果你现在开始一个新项目，或者团队正在被 flaky test 折磨得死去活来， **Playwright 值得你试试** 。

**参考资料**

[https://github.com/microsoft/playwright](https://github.com/microsoft/playwright)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)