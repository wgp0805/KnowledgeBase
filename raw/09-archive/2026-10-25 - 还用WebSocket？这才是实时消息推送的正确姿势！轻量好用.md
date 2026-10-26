---
source_url: "https://mp.weixin.qq.com/s/FWzWAGpRZmkgT9ZZ4Av0WA"
title: "还用WebSocket？这才是实时消息推送的正确姿势！轻量好用"
account: "IT码徒"
published_at: "2026-10-25 19:03:08"
saved_at: "2026-10-26 07:35:22"
sync_id: "art_24dee6adff944dcba51d86fa5d52d45d"
parse_status: "ok"
---

# 还用WebSocket？这才是实时消息推送的正确姿势！轻量好用

点击“IT码徒”，关注，置顶公众号

每日技术干货，第一时间送达！

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/e3415148a9018e581714e7cf7e6c0289_MD5.png)

01

前言

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/ea730ad34a93d53950aeb779339a74ef_MD5.png)

在日常的开发中，我们经常能碰见服务端需要主动推送给客户端数据的业务场景，比如数据大屏的实时数据，比如消息中心的未读消息，比如聊天功能等等。

本文主要介绍SSE的使用场景和如何使用SSE。

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/e3415148a9018e581714e7cf7e6c0289_MD5.png)

02

服务端推送数据的实现方案

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/ea730ad34a93d53950aeb779339a74ef_MD5.png)

我们常规实现这些需求的方案有以下三种：

- 轮询

- websocket

- SSE

轮询简介

在很久很久以前，前端一般使用轮询来进行服务端向客户端进行消息的伪推送，为什么说轮询是伪推送？

因为轮询本质上还是通过客户端向服务端发起一个单项传输的请求，服务端对这个请求做出响应而已。通过不断的请求来实现服务端向客户端推送数据的错觉。并不是服务端主动向客户端推送数据。显然，轮询一定是上述三个方法里最下策的决定。

轮询的缺点：

- 首先轮询需要不断的发起请求，每一个请求都需要经过http建立连接的流程（比如三次握手，四次挥手），是没有必要的消耗。
- 客户端需要从页面被打开的那一刻开始就一直处理请求。虽然每次轮询的消耗不大，但是一直处理请求对于客户端来说一定是不友好的。
- 浏览器请求并发是有限制的。比如Chrome 最大并发请求数目为 6，这个限制还有一个前提是针对同一域名的，超过这一限制的后续请求将会被阻塞。而轮询意味着会有一个请求长时间的占用并发名额。

- 而如果轮询时间较长，可能又没有办法非常及时的获取数据

websocket简介

websocket是一个双向通讯的协议，他的优点是，可以同时支持客户端和服务端彼此相互进行通讯。功能上很强大。

缺点也很明显，websocket是一个新的协议，ws/wss。也就是说，支持http协议的浏览器不一定支持ws协议。

相较于SSE来说，websocket因为功能更强大。结构更复杂。所以相对比较重。

websocket对于各大浏览器的兼容性↓

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/481b0d139cc4c7c34394bf681d0575dc_MD5.jpg)

SSE简介

sse是一个单向通讯的协议也是一个长链接，它只能支持服务端主动向客户端推送数据，但是无法让客户端向服务端推送消息。

长链接是一种HTTP/1.1的持久连接技术，它允许客户端和服务器在一次TCP连接上进行多个HTTP请求和响应，而不必为每个请求/响应建立和断开一个新的连接。长连接有助于减少服务器的负载和提高性能。

SSE的优点是，它是一个轻量级的协议，相对于websockte来说，他的复杂度就没有那么高，相对于客户端的消耗也比较少。

而且SSE使用的是http协议（websocket使用的是ws协议），也就是现有的服务端都支持SSE，无需像websocket一样需要服务端提供额外的支持。

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/881a8aea14790a031a3796c51f9cae68_MD5.png)

注意:IE大魔王不支持SSE

SSE对于各大浏览器的兼容性↓

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/3f5a65b7ba75c1d2ff3207feae866270_MD5.jpg)

注意哦，上图是SSE对于浏览器的兼容不是对于服务端的兼容。

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/e3415148a9018e581714e7cf7e6c0289_MD5.png)

03

websocket和SSE的区别

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/ea730ad34a93d53950aeb779339a74ef_MD5.png)

轮询

对于当前计算机的发展来说，几乎很少出现同时不支持websocket和sse的情况，所以轮询是在极端情况下浏览器实在是不支持websocket和see的下策。

Websocket和SSE

我们一般的服务端和客户端的通讯基本上使用这两个方案。首先声明:这两个方案没有绝对的好坏，只有在不同的业务场景下更好的选择。

SSE的官方对于SSE和Websocket的评价是

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/881a8aea14790a031a3796c51f9cae68_MD5.png)

WebSocket是全双工通道，可以双向通信，功能更强；SSE是单向通道，只能服务器向浏览器端发送。
WebSocket是一个新的协议，需要服务器端支持；SSE则是部署在HTTP协议之上的，现有的服务器软件都支持。
SSE是一个轻量级协议，相对简单；WebSocket是一种较重的协议，相对复杂。
SSE默认支持断线重连，WebSocket则需要额外部署。
SSE支持自定义发送的数据类型。

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/e3415148a9018e581714e7cf7e6c0289_MD5.png)

04

websocket和SSE适用场景

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/ea730ad34a93d53950aeb779339a74ef_MD5.png)

对于SSE来说，它的优点就是轻，而且对于服务端的支持度要更好。换言之，可以使用SSE完成的功能需求，没有必要使用更重更复杂的websocket。

比如：数据大屏的实时数据，消息中心的消息推送等一系列只需要服务端单方面推送而不需要客户端同时进行反馈的需求，SSE就是不二之选。

对于Websocket来说，他的优点就是可以同时支持客户端和服务端的双向通讯。所适用的业务场景：最典型的就是聊天功能。这种服务端需要主动向客户端推送信息，并且客户端也有向服务端推送消息的需求时，Websocket就是更好的选择。

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/e3415148a9018e581714e7cf7e6c0289_MD5.png)

05

SSE的主要API

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/ea730ad34a93d53950aeb779339a74ef_MD5.png)

建立SSE链接

 `var source = new EventSource(url);`

SSE连接状态

source.readyState

0，相当于常量 EventSource.CONNECTING，表示连接还未建立，或者连接断线。

1，相当于常量 EventSource.OPEN，表示连接已经建立，可以接受数据。

2，相当于常量 EventSource.CLOSED，表示连接已断，且不会重连。

SSE相关事件

- open事件(连接一旦建立，就会触发open事件，可以定义相应的回调函数)

- message事件(收到数据就会触发message事件)

- error事件(如果发生通信错误（比如连接中断），就会触发error事件)

数据格式

```
Content-Type: text/event-stream //文本返回格式
Cache-Control: no-cache  //不要缓存
Connection: keep-alive //长链接标识
```

SSE相关文档：

https://www.w3cschool.cn/nwfchn/wpi3cozt.html

显然，如果直接看api介绍不论是看这里还是看官网，大部分同学都是比较懵圈的状态，那么我们写个demo来看一下?

我更建议您先把Demo跑起来，然后在看看上面这个w3cschool的SSE文档。两个配合一起看，会更方便理解些。

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/e3415148a9018e581714e7cf7e6c0289_MD5.png)

06

实操Demo

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/ea730ad34a93d53950aeb779339a74ef_MD5.png)

这里Demo前端使用的就是最基本的html静态页面连接，没有使用任何框架。

后端选用语言是node，框架是Express。

理论上，把这两段端代码复制过去跑起来就直接可以用了。

- 第一步，建立一个 index.html 文件，然后复制前端代码Demo到 index.html 文件中，打开文件
- 第二步，进入一个新的文件夹，建立一个 index.js 文件，然后将后端Demo代码复制进去，然后在该文件夹下执行

```
npm init          //初始化npm
npm i express     //下载node express框架
node index        //启动服务
```

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/7061339623e70bce410c578ea839b670_MD5.jpg)

在这一层文件夹下执行命令。

完成以上操作就可以把项目跑起来了

前端代码Demo

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <ul id="ul">

    </ul>
</body>
<script>

//生成li元素
function createLi(data){
    let li = document.createElement("li");
    li.innerHTML = String(data.message);
    return li;
}

//判断当前浏览器是否支持SSE
let source = ''
if (!!window.EventSource) {
    source = new EventSource('http://localhost:8088/sse/');
 }else{
    thrownewError("当前浏览器不支持SSE")
 }

//对于建立链接的监听
 source.onopen = function(event) {
   console.log(source.readyState);
   console.log("长连接打开");
 };

//对服务端消息的监听
 source.onmessage = function(event) {
   console.log(JSON.parse(event.data));
   console.log("收到长连接信息");
   let li = createLi(JSON.parse(event.data));
   document.getElementById("ul").appendChild(li)
 };

//对断开链接的监听
 source.onerror = function(event) {
   console.log(source.readyState);
   console.log("长连接中断");
 };

</script>
</html>
```

后端代码Demo（node的express）

```
const express = require('express'); //引用框架
const app = express(); //创建服务
const port = 8088; //项目启动端口

//设置跨域访问
app.all("*", function(req, res, next) {
//设置允许跨域的域名，*代表允许任意域名跨域
 res.header("Access-Control-Allow-Origin", '*');
//允许的header类型
 res.header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Requested-With");
//跨域允许的请求方式
 res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
// 可以带cookies
 res.header("Access-Control-Allow-Credentials", true);
if (req.method == 'OPTIONS') {
  res.sendStatus(200);
 } else {
  next();
 }
})

app.get("/sse",(req,res) => {
    res.set({
        'Content-Type': 'text/event-stream', //设定数据类型
        'Cache-Control': 'no-cache',// 长链接拒绝缓存
        'Connection': 'keep-alive'//设置长链接
      });

      console.log("进入到长连接了")
      //持续返回数据
      setInterval(() => {
        console.log("正在持续返回数据中ing")
        const data = {
          message: `Current time is ${new Date().toLocaleTimeString()}`
        };
        res.write(`data: ${JSON.stringify(data)}\n\n`);
      }, 1000);
})

//创建项目
app.listen(port, () => {
console.log(`项目启动成功-http://localhost:${port}`)
})
```

效果

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/b5d86f6ca4a9060b79ecca945dbe5844_MD5.gif)

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/e3415148a9018e581714e7cf7e6c0289_MD5.png)

07

总结

![图片](assets/2026-10-25%20-%20%E8%BF%98%E7%94%A8WebSocket%EF%BC%9F%E8%BF%99%E6%89%8D%E6%98%AF%E5%AE%9E%E6%97%B6%E6%B6%88%E6%81%AF%E6%8E%A8%E9%80%81%E7%9A%84%E6%AD%A3%E7%A1%AE%E5%A7%BF%E5%8A%BF%EF%BC%81%E8%BD%BB%E9%87%8F%E5%A5%BD%E7%94%A8/ea730ad34a93d53950aeb779339a74ef_MD5.png)

- SSE比websocket更轻

- SSE是基于http/https协议的

- websocket是一个新的协议，ws/wss协议

- 如果只需要服务端向客户端推送消息，推荐使用SSE

- 如果需要服务端和客户端双向推送，请选择websocket

- 不论是SSE还是websocket，对于浏览器的兼容性都不错

- 轮询是下策，很占用客户端资源，不建议使用。（不过偷懒的时候他确实方便）

- IE不支持SSE

- 对了，小程序不支持SSE哦

来源：juejin.cn/post/7325730345840066612

---
原文链接：https://mp.weixin.qq.com/s/FWzWAGpRZmkgT9ZZ4Av0WA
