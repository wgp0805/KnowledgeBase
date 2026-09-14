---
source_url: "https://mp.weixin.qq.com/s/FEg7-5mRxodCRHdWdoDd2g"
title: "使用 Shadcn UI 构建 Java 桌面应用"
account: "小哈学Java"
published_at: "2026-09-11 16:33:10"
saved_at: "2026-09-14 07:28:25"
sync_id: "art_9f0b534c656d4e6b8e0028789fd6bbaa"
parse_status: "ok"
---

# 使用 Shadcn UI 构建 Java 桌面应用

![图片 1](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smqRvQnK9pYstBzJqdKVNhI9RqE3b7b3BHWFkCMduuqG4lI1d6vicSsibftibYFNG2fvVZqV0oEUCTIVtF8xRsiaic1Gw2EMpuWwQ2fU/640?wx_fmt=png&from=appmsg)

![图片 2](https://mmbiz.qpic.cn/sz_mmbiz_jpg/joHKZKxvyOrfTib7Fxy04nBY8ibMGfWpD7s3eibCRzHTL0QLOiapMEwvcBVdVoFT3I6raDdBx44KITsXJBU4yPAIHzOwVwHCheEXAMS7PsvTviag/640?wx_fmt=other&from=appmsg#imgIndex=1)

![图片 3](https://mmbiz.qpic.cn/mmbiz_jpg/joHKZKxvyOp21DCfFhUv3WbCYTeTFnBB1w1jKqUkzaWgicoW0ZjxQ6WJCpqriacl6WRENyJKOBhO6BVeLibFF5JSzTo8fb5K1iazlMm7cdhFmKU/640?wx_fmt=other&from=appmsg#imgIndex=2)

![图片 4](https://mmbiz.qpic.cn/mmbiz_png/joHKZKxvyOphD8ZqicUJyBbxB6oLczv3SYxjqtdcVnSHicCX8TzE8X09ibRicPRSCoHmmgGhdcHPNpLX8yOMbW8XRkiaDDc0fjUxxLCJlT6G8uLQ/640?wx_fmt=png&from=appmsg#imgIndex=3)

![图片 5](https://mmbiz.qpic.cn/mmbiz_gif/sTnayibHfVq6k58yrsWFU0zS4MhOFVPH9ib8lFF40iahdfmiaz8IicbvIfia8icp3F3Y5OG1BJAKthCic72w2IiboDVBicYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=65h7dnft&tp=webp#imgIndex=1)

![图片 6](https://mmbiz.qpic.cn/sz_mmbiz_png/knmrNHnmCLEdM2gtRgy5eLztKXrUhee76MZ9wAicNPicsnAHPibicaSHUVqFkkibxWlrGO0acUxQmycZpqCNGcibaicxA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=6)

![图片 7](https://mmbiz.qpic.cn/mmbiz_gif/TNUwKhV0JpTGQqtlGfEHkjibtshlaDwVKzjqq2pnpmYC14bKxDtSuhpWZWfVcicj5PFsoSMzuzicKIWZbsBpGXiaicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&randomid=t3kyqhaj&retryload=1&tp=webp#imgIndex=46)

![图片 8](https://mmbiz.qpic.cn/sz_mmbiz_gif/knmrNHnmCLEVGGmicJODkfibhcqyUwmTSC8CUvAMG78wPemfibvQ502uFs9jlziaLP50YcTs4rL9hQuzX32PAUOPHA/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&randomid=ers09cbt&tp=webp#imgIndex=47)

将 **小哈学Java**** **设为“**星标****⭐**”

第一时间收到文章更新

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smqRvQnK9pYstBzJqdKVNhI9RqE3b7b3BHWFkCMduuqG4lI1d6vicSsibftibYFNG2fvVZqV0oEUCTIVtF8xRsiaic1Gw2EMpuWwQ2fU/640?wx_fmt=png&from=appmsg)

**在线 Java 面试刷题（已更新334题，图文并茂）**：https://www.quanxiaoha.com/java-interview

**目录**

- Swing/JavaFX 为什么不够用了？
- 整体方案：JxBrowser + React + shadcn/ui
- 窗口与 Web 视图
- 资源加载：开发 vs 生产
- 开发环境
- 生产环境

- Java ↔ Web 通信
- 方案一：JS-Java Bridge（小项目够用）
- 方案二：Protobuf + gRPC（正经项目首选）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/joHKZKxvyOrfTib7Fxy04nBY8ibMGfWpD7s3eibCRzHTL0QLOiapMEwvcBVdVoFT3I6raDdBx44KITsXJBU4yPAIHzOwVwHCheEXAMS7PsvTviag/640?wx_fmt=other&from=appmsg#imgIndex=1)

Slack、Notion、Teams、Linear——这些桌面应用有什么共同点？**它们的 UI 全是 Web 技术写的。** 这不是偷懒，而是务实的工程选择。

本文用 shadcn/ui + React + TypeScript 构建一个跨平台的 Java 桌面应用，解决三个核心问题：怎么嵌、怎么加载、怎么通信。完整源码在 GitHub。

## Swing/JavaFX 为什么不够用了？

Java 的原生 UI 工具包（Swing、JavaFX、SWT）有几个共同的硬伤：

- 改 UI 痛苦 ：想实现个现代化的动画过渡？自己造轮子
- 生态荒漠 ：组件库少、社区活跃度低、招人也难
- 颜值掉队 ：默认控件的外观停留在十年前

Web UI 恰好是反面：**组件库多到选不过来、高 DPI / 触屏 / 响应式开箱支持、跨平台一致性天然具备。** 把 Web 技术塞进桌面壳子里，既能用上前端生态的红利，又不用再和过时的 UI 框架搏斗。

## 整体方案：JxBrowser + React + shadcn/ui

我们要构建的是一个偏好设置对话框，用户选好设置后保存到本地文件系统，重启后依然保留。

![基于 Web UI 的桌面应用界面截图](https://mmbiz.qpic.cn/mmbiz_jpg/joHKZKxvyOp21DCfFhUv3WbCYTeTFnBB1w1jKqUkzaWgicoW0ZjxQ6WJCpqriacl6WRENyJKOBhO6BVeLibFF5JSzTo8fb5K1iazlMm7cdhFmKU/640?wx_fmt=other&from=appmsg#imgIndex=2)

基于 Web UI 的桌面应用界面截图要让这套东西跑起来，得解决三件事：

- 可靠的 Web 视图 ：Java 内置的 WebView 跟不上现代 Web 标准
- 无服务器加载 ：生产环境不依赖本地/远程服务器
- Java ↔ JS 通信 ：读写文件系统等操作不走 Web 服务器

## 窗口与 Web 视图

用 Swing 的  `JFrame`  建窗口，塞一个 JxBrowser 提供的 Chromium 内核 Web 视图进去：

```
var engine = Engine.newInstance(HARDWARE_ACCELERATED);
var browser = engine.newBrowser();

SwingUtilities.invokeLater(() -> {
    var view = BrowserView.newInstance(browser);
    var frame = new JFrame("Application");
    frame.addWindowListener(new WindowAdapter() {
        @Override
        public void windowClosing(WindowEvent e) {
            engine.close();
        }
    });
    frame.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
    frame.add(view, BorderLayout.CENTER);
    frame.setSize(1280, 900);
    frame.setLocationRelativeTo(null);
    frame.setVisible(true);
});
```

## 资源加载：开发 vs 生产

Web 部分就是个标准的 React 应用，但加载方式在开发和生产环境完全不同。

### 开发环境

直接起 dev server，热更新照常用：

```
./gradlew startDevServer
if (!AppDetails.isProduction()) {
   browser.navigation().loadUrl("http://localhost:[port]");
}
```

### 生产环境

**生产环境不能用 dev server** ——不仅多一个进程，还有安全隐患：用户可以通过浏览器直接访问 localhost 看到源码。

解法：用 JxBrowser 的自定义协议拦截器，把 Web 资源打包进 JAR，通过  `jxb://`  协议从 classpath 直接提供：

```
var options = EngineOptions.newBuilder(HARDWARE_ACCELERATED)
       .addScheme(Scheme.of("jxb"), new UrlRequestInterceptor());
var engine = Engine.newInstance(options.build());
```

浏览器请求  `jxb://my-app.com`  → 拦截器从资源目录返回  `index.html`  → 后续 CSS/JS 请求同理。**所有加载发生在应用内部，外部无法访问。** 同时不影响正常的 HTTPS/API 请求。

```
if (!AppDetails.isProduction()) {
    browser.navigation().loadUrl("http://localhost:[port]");
} else {
    browser.navigation.loadUrl("jxb://my-app.com");
}
```

## Java ↔ Web 通信

Web 前端需要调用 Java 代码来读写偏好设置文件。两种方案：

### 方案一：JS-Java Bridge（小项目够用）

JxBrowser 支持从 JavaScript 直接调 Java 方法：

```
@JsAccessible
class PrefsService {
    void setFontSize(int size) { }
}

// TypeScript 侧
declare class PrefsService {
    setFontSize(size: number): void;
}
prefsService.setFontSize(12);
```

通信方法少的时候没问题。**一旦接口多了，没有编译期检查、没有自动补全，维护成本指数上升。**

### 方案二：Protobuf + gRPC（正经项目首选）

用  `.proto`  文件定义 API，自动生成类型安全的 Java 和 TypeScript 代码：

```
service PrefsService {
  rpc SetFontSize(FontSize) returns (google.protobuf.Empty);
}

enum FontSize {
  SMALL = 0;
  DEFAULT = 1;
  LARGE = 2;
}
```

Java 端起 gRPC 服务器，Web 端用 Connect 客户端连接：

```
// Java 服务端
class PrefsService extends PrefsServiceImplBase {
    @Override
    public void setTheme(Theme request, StreamObserver<Empty> responseObserver) { }
}

// TypeScript 客户端
const transport = createGrpcWebTransport({
    baseUrl: `http://localhost:50051`,
});
const prefsClient = createClient(PrefsService, transport);
prefsClient.setFontSize(FontSize.SMALL);
```

![通信示意图](https://mmbiz.qpic.cn/mmbiz_png/joHKZKxvyOphD8ZqicUJyBbxB6oLczv3SYxjqtdcVnSHicCX8TzE8X09ibRicPRSCoHmmgGhdcHPNpLX8yOMbW8XRkiaDDc0fjUxxLCJlT6G8uLQ/640?wx_fmt=png&from=appmsg#imgIndex=3)

通信示意图**好处很明确**：类型安全、代码自动生成、IDE 补全、编译期检查——项目越大越值。

**参考资料**

GitHub：

https://github.com/TeamDev-IP/JxBrowser-Gallery

[加入小哈的星球](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / Java 学习路线 / **社群讨论 / **学习打卡 / 每月赠书**

- 《仿小红书（微服务架构 ）》 已完结，基于 Spring Cloud Alibaba + Spring Boot 3.x + JDK 17..., [点击查看项目介绍](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247538491&idx=1&sn=576995017721766d0fe15723fd135619&chksm=fd5787bdca200eab54d2fb8ca07fcc2bffdec3eaab4ab82ab5eaf949f0254c1683455e02010b&token=343952052&lang=zh_CN&scene=21#wechat_redirect) ； 演示地址： http://116.62.199.48:7070/
- 《 Spring AI 应用（RAG 智能客服） 》已完结, 基于 Spring AI + Spring Boot 3.x + JDK 21
- 《 秒杀系统设计 》正在更新中，单体到微服务高并发架构演进

- 《 前后端分离博客项目（全栈开发） 》 已完结,演示链接： http://116.62.199.48/
- 项目阅读地址： https://quanxiaoha.com/column

截止目前，**累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/sTnayibHfVq6k58yrsWFU0zS4MhOFVPH9ib8lFF40iahdfmiaz8IicbvIfia8icp3F3Y5OG1BJAKthCic72w2IiboDVBicYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=65h7dnft&tp=webp#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/knmrNHnmCLEdM2gtRgy5eLztKXrUhee76MZ9wAicNPicsnAHPibicaSHUVqFkkibxWlrGO0acUxQmycZpqCNGcibaicxA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=6)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~
2. 面试题：ES 不支持 decimal，如何避免丢失精度？
3. 四大软件外包公司
4. 吊打 ThreadLocal，谈谈FastThreadLocal为啥能这么快？
```

```

```

```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。
获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。
```

```
PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。
点“在看”支持小哈呀，谢谢
```


---
原文链接：https://mp.weixin.qq.com/s/FEg7-5mRxodCRHdWdoDd2g
