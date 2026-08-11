---
title: "终于找到一个好用的 Nginx 日志分析工具了"
source: "https://mp.weixin.qq.com/s/iwsFy1RIZsnXRgvRYKmu0w"
---
终码一生 *2026年8月11日 10:20*

点击“终码一生”，关注，置顶公众号

每日技术干货，第一时间送达！

搞运维或者自己折腾服务器的朋友应该都有这个需求：想看看自己网站的访问情况。

之前试过 GoAccess、ELK 那一套，要么配置麻烦，要么太重量级。最近发现了一个叫 NginxPulse 的项目，用下来感觉还不错，分享给大家。

![图片](assets/%E7%BB%88%E4%BA%8E%E6%89%BE%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%94%A8%E7%9A%84%20Nginx%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E4%BA%86/cbcaaf22f406380157c49da576b866f9_MD5.webp)

01

这是啥？

一句话： 轻量级的 Nginx 日志分析面板 。

能干啥：

- 实时看 PV/UV 数据
- IP 归属地查询（国内用 ip2region 本地库，国外走 ip-api）
- 客户端/浏览器解析
- 支持多站点
- 支持自定义日志格式

看下效果图：

![图片](assets/%E7%BB%88%E4%BA%8E%E6%89%BE%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%94%A8%E7%9A%84%20Nginx%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E4%BA%86/9a6296ab81fecff65736bf009a223eb3_MD5.webp)

图片

![图片](assets/%E7%BB%88%E4%BA%8E%E6%89%BE%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%94%A8%E7%9A%84%20Nginx%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E4%BA%86/ee7116b9d2e5ead1a8b85f52c4302277_MD5.webp)

图片

![图片](assets/%E7%BB%88%E4%BA%8E%E6%89%BE%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%94%A8%E7%9A%84%20Nginx%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

02

技术栈

后端是 Go + Gin，前端是 Vue3 + Vite + PrimeVue，数据库就一个 SQLite，够轻量。

IP 归属地这块挺聪明的：先查内存缓存，然后走远程 API 批量查，失败了再用本地 ip2region 兜底。既保证速度又保证准确率。

![图片](assets/%E7%BB%88%E4%BA%8E%E6%89%BE%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%94%A8%E7%9A%84%20Nginx%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

03

怎么跑起来

Docker 一把梭

最简单的方式，一行命令搞定：

```
docker run -d --name nginxpulse \
  -p 8088:8088 \
  -p 8089:8089 \
  -e WEBSITES='[{"name":"主站","logPath":"/share/log/nginx/
            access.log","domains":["example.com"]}]'
           \
  -v /your/nginx/logs/
            access.log:/share/
          log/nginx/
            access.log:ro
           \
  -v $(pwd)/var/nginxpulse_data:/app/var/nginxpulse_data \
  magiccoders/nginxpulse:latest
```

把 /your/nginx/logs/ [access.log](http://access.log/) 换成你自己的日志路径就行。

Docker Compose

如果喜欢 compose，也行：

```
version: "3.8"
services:
nginxpulse:
    image:magiccoders/nginxpulse:latest
    container_name:nginxpulse
    ports:
      -"8088:8088"
      -"8089:8089"
    environment:
      WEBSITES:'[{"name":"主站","logPath":"/share/log/nginx/
            access.log","domains":["example.com"]}]'
          
    volumes:
      -./nginx_logs/
            access.log:/share/
          log/nginx/
            access.log:ro
          
      -./var/nginxpulse_data:/app/var/nginxpulse_data
    restart:unless-stopped
```

跑起来之后：

- 前端面板： http://localhost:8088
- 后端 API： http://localhost:8089

多网站怎么配？

如果你有多个站点， WEBSITES 传数组就行：

```
WEBSITES='[
  {"name":"主站","logPath":"/logs/
            main.log","domains":["www.example.com"]},
          
  {"name":"博客","logPath":"/logs/
            blog.log","domains":["blog.example.com"]}
          
]'
```

日志按天切割的话，支持通配符：

```
{"logPath": "/logs/access-*.log"}
```

.gz 压缩日志也能直接解析，不用手动解压。

![图片](assets/%E7%BB%88%E4%BA%8E%E6%89%BE%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%94%A8%E7%9A%84%20Nginx%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

04

几个实用功能

1. 日志不在本机？没关系，支持 SFTP、HTTP、S3/OSS 三种方式拉取远端日志。比如 SFTP：
	```
	{
	  "id": "sftp-main",
	"type": "sftp",
	"host": "1.2.3.4",
	"port": 22,
	"user": "nginx",
	"auth": { "keyFile": "/secrets/id_rsa" },
	"path": "/var/log/nginx/
	            access.log"
	          
	}
	```
2. Push Agent  
	如果服务器在内网或者边缘节点，可以用 Agent 主动推送日志。在日志服务器上跑一个轻量 agent，实时把日志推到 NginxPulse 主服务。
3. 自定义日志格式

不是默认的 combined 格式？可以自定义。支持两种方式：

- 方式一：直接写 log\_format 语法

```
{
  "logFormat": "$remote_addr - $remote_user [$time_local] \"$request\" $status $body_bytes_sent"
}
```

- 方式二：正则（命名分组）

```
{
  "logRegex": "^(?P<ip>\\S+) - (?P<user>\\S+) \\[(?P<time>[^\\]]+)\\]..."
}
```

1. Caddy 也支持  
	用 Caddy 的朋友也能用，配置 logType: "caddy" 就行，会按 JSON 格式解析。
2. 访问控制

生产环境可以加个密钥：

```
ACCESS_KEYS='["your-secret-key"]'
```

访问时需要带上 X-NginxPulse-Key 请求头，前端会自动弹窗让你输入。

![图片](assets/%E7%BB%88%E4%BA%8E%E6%89%BE%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%94%A8%E7%9A%84%20Nginx%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

05

常见问题

Q：跑起来后日志明细是空的？

A：多半是权限问题。给日志目录和数据目录加个权限：

```
chmod -R 777 /path/to/logs /path/to/nginxpulse_data
```

Q：有访问但是 PV/UV 都是 0？

A：默认排除内网 IP。如果想统计内网流量，把 PV *EXCLUDE* IPS 设成空数组：

```
PV_EXCLUDE_IPS='[]'
```

![图片](assets/%E7%BB%88%E4%BA%8E%E6%89%BE%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%94%A8%E7%9A%84%20Nginx%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

06

单体部署

如果不想用 Docker，可以构建成单个可执行文件：

```
./scripts/
            build_single.sh
```

会生成一个内置前端的二进制文件，直接运行就能同时提供前后端服务。支持 amd64 和 arm64。

![图片](assets/%E7%BB%88%E4%BA%8E%E6%89%BE%E5%88%B0%E4%B8%80%E4%B8%AA%E5%A5%BD%E7%94%A8%E7%9A%84%20Nginx%20%E6%97%A5%E5%BF%97%E5%88%86%E6%9E%90%E5%B7%A5%E5%85%B7%E4%BA%86/e3415148a9018e581714e7cf7e6c0289_MD5.png)

07

最后

GitHub 地址：

[https://github.com/likaia/nginxpulse](https://github.com/likaia/nginxpulse)

在线演示：

[https://nginx-pulse.kaisir.cn/](https://nginx-pulse.kaisir.cn/)

目前 2.6k star，MIT 协议，可以放心用。

如果你也在找 Nginx 日志分析工具，可以试试这个。比起重量级的 ELK 或者纯命令行的 GoAccess，这个算是个不错的中间选择。

来源： [juejin.cn/post/7597080391880343562](http://juejin.cn/post/7597080391880343562)

—END—

**PS：防止找不到本篇文章，可以收藏点赞，方便翻阅查找哦。**

往期推荐[领导：发现谁用 kill -9 关闭程序就开除！](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540180&idx=1&sn=c92c79fefbb5fab84eefa8af5c888e22&scene=21#wechat_redirect)[为什么越来越多人用Sa-Token？](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540180&idx=2&sn=b4ea9821aff418bd29836d20e903685d&scene=21#wechat_redirect)[想扔掉笨重的XXL-JOB？试试这个基于Nacos的优雅调度方案](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540167&idx=1&sn=eb1397564e204729fff4880acee59024&scene=21#wechat_redirect)[SpringBoot中获取真实客户端IP的终极方案，99%的人都没做对！](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540167&idx=2&sn=6350cda4488ac948f634ae16fab78a31&scene=21#wechat_redirect)[沉浸式AI编程：IDEA + Claude Code 的终极方案，非常丝滑！](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540142&idx=1&sn=8f7960fe25baecb80e97929d40a47377&scene=21#wechat_redirect)[面试官：SpringBoot在打包部署的时候打包成jar和war有什么不同?](https://mp.weixin.qq.com/s?__biz=MzU2OTMyMTAxNA==&mid=2247540142&idx=2&sn=8e4225716f18800e3fcb345ca518b78e&scene=21#wechat_redirect)

nginx · 目录

阅读原文