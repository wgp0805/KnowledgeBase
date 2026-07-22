---
title: "MinIO 社区版被故意阉割，Web管理功能全面移除，来试试国产的RustFS？"
source: "https://mp.weixin.qq.com/s/vUXDPCiSxO700-zDYOr97g"
---
Java学习者社区 *2026年7月21日 13:52*

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/e38c157f93d62c6de2e7a80babd7ee85_MD5.webp)

来源： [juejin.cn/post/7523256725127987226](http://juejin.cn/post/7523256725127987226)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 一、MinIO 牺牲开源精神走向商业利益
- 二、寻找平替，尝试 RustFS
- 2.1. 准备好以下目录结构
	- 2.2. /mnt/rustfs/ 目录下启动
	- 2.3. 开放安全组
	- 2.4. 测试访问
	- 2.5. 配置 https
- 总结

---

## 一、MinIO 牺牲开源精神走向商业利益

今天部署好 minio 后打开 web 界面发现只剩下纯对象存储：

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/65c8ff382dea0246c1f61e82166221c2_MD5.webp)

MinIO Web 界面只剩纯对象存储

图来源于小众软件

原因是 2 月 26 号的一个 PR 以"精简控制台"为由删了 114736 行代码：

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/116ac52f89cddfe48fc1feb79d4de318_MD5.jpg)

精简控制台 PR 删除 114736 行代码

而官方这么说：\*\*"对于需要图形界面完成管理的场景，请迁移到我们的商业产品（AiStor），社区用户则可以使用 mc 命令"。\*\* 网友对此表示强烈谴责：）

## 二、寻找平替，尝试 RustFS

RustFS 是一个用 Rust 语言构建的高性能分布式对象存储系统，定位为 MinIO 的替代方案。

Rust 的安全性和高性能以及 Apache 2.0 的开源协议是我将它作为 MinIO 的平替的主要原因。

因为 RustFS 是比较新的项目，按照官网的 docker 部署命令有点问题。

但官方在相关 issue 中已经给了解决方案，下面是我结合该方案并使用 `docker-compose` 部署成功的实操记录：

### 2.1. 准备好以下目录结构

```
/mnt/rustfs/
├── data/
└── 
            docker-compose.yml
```

[docker-compose.yml](http://docker-compose.yml/) 文件内容：

```
services:
  rustfs:
    image:rustfs/rustfs:latest
    container_name:rustfs
    ports:
      -"9000:9000"# API 端口
      -"9001:9001"# Console 端口
    volumes:
      -./data:/data# 数据存储
    environment:
      -RUSTFS_ROOT_USER=rustfsadmin
      -RUSTFS_ROOT_PASSWORD=rustfsadmin
      -RUSTFS_ADDRESS=:9000
      -RUSTFS_CONSOLE_ADDRESS=:9001
      -RUSTFS_CONSOLE_ENABLE=true
      -RUSTFS_LOG=warn
    restart:unless-stopped
```

### 2.2. /mnt/rustfs/ 目录下启动

`docker-compose up -d` 启动容器：

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/60ee139e8e105728ef11f30c3c23ef11_MD5.jpg)

docker-compose 启动容器

`docker compose ps` 查看状态：

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/6d537b030ec215a66a64d8f251bd25ec_MD5.jpg)

docker compose ps 查看状态

### 2.3. 开放安全组

如果访问不了记得新增安全组，开放 `9000/9001` 的端口：

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/9fcf5094e7660db77cd127a911e3fa40_MD5.jpg)

开放安全组端口

### 2.4. 测试访问

控制台页面访问 9001 端口：

默认的账号密码： `rustfsadmin/rustfsadmin`

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/4c2a79de0868ec7fddc27256aeea80ec_MD5.jpg)

RustFS 登录页

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/7c96173ef7d7097dad8f655edebfc617_MD5.jpg)

RustFS 控制台界面

### 2.5. 配置 https

为了安全考虑，我希望服务只能由 https 协议通过 nginx 转发来访问，而不能直接通过 ip 访问：

首先将 `              docker-compose.yml            ` 文件做如下改动：

```
ports:
  # - "9000:9000"   # API 端口
  # - "9001:9001"   # Console 端口
  - "127.0.0.1:9000:9000"   # API 端口
  - "127.0.0.1:9001:9001"   # Console 端口
```

然后创建一个子域名 `              rustfs.yourdomain.cn            ` 映射到 `              yourdomain.cn:9001            ` ，nginx 配置如下：

```
upstream rustfs_console {
    server localhost:9001;
}

upstream rustfs_api {
    server localhost:9000;
}

# RustFS Console (Web UI)
server {
    listen 443 ssl;
    server_name 
            rustfs.yourdomain.cn;
          

    ssl_certificate /etc/letsencrypt/live/
            yourdomain.cn-0001/fullchain.pem;
          
    ssl_certificate_key /etc/letsencrypt/live/
            yourdomain.cn-0001/privkey.pem;
          
    include /etc/letsencrypt/
            options-ssl-nginx.conf;
          
    ssl_dhparam /etc/letsencrypt/
            ssl-dhparams.pem;
          

    location / {
        proxy_pass http://rustfs_console;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Forwarded-Host $host;
        proxy_set_header X-Forwarded-Port $server_port;

        # WebSocket 支持
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}

# RustFS API
server {
    listen 443 ssl;
    server_name 
            rustfsapi.yourdomain.cn;
          

    ssl_certificate /etc/letsencrypt/live/
            yourdomain.cn-0001/fullchain.pem;
          
    ssl_certificate_key /etc/letsencrypt/live/
            yourdomain.cn-0001/privkey.pem;
          
    include /etc/letsencrypt/
            options-ssl-nginx.conf;
          
    ssl_dhparam /etc/letsencrypt/
            ssl-dhparams.pem;
          

    location / {
        proxy_pass http://rustfs_api;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

# HTTP 重定向到 HTTPS
server {
    listen 80;
    server_name 
            rustfs.yourdomain.cn
           
            rustfsapi.yourdomain.cn;
          
    return 301 https://$server_name$request_uri;
}
```

测试 https 访问：

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/e7d9e2f11147da53dec36af409c4ebe3_MD5.jpg)

测试 https 访问

## 总结

随着 MinIO 社区版自 2024 年 2 月起全面移除 Web 管理界面，标志着其加速向商业化闭源演进，对广大习惯图形化管理的用户来说无疑是一种"背刺"。

尽管 MinIO 声称 CLI（如 mc）功能更专业，但对中小企业、个人开发者甚至初学者而言，图形界面不可或缺。

同时，RustFS 作为国产、开源、Rust 编写的分布式对象存储项目，凭借以下优势，已具备成为 MinIO 替代品的潜力：

| 对比项 | MinIO（社区版） | RustFS |
| --- | --- | --- |
| 开源协议 | AGPL v3（限制较多） | Apache 2.0（更宽松） |
| 管理界面 | ✅ 已被移除（需付费） | ✅ 自带 Web 控制台 |
| 命令行支持 | mc | REST API + 后续工具支持 |
| 部署复杂度 | 简单 | 较简单，支持 Docker Compose |
| 性能与安全性 | 高，但维护封闭 | Rust 架构，天生安全高效 |
| 中文社区与生态支持 | 较少（商业倾向） | 正在建设中 |

注意：RustFS 项目还处于早期阶段，功能在逐步完善，生产环境部署需做额外验证。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/MinIO%20%E7%A4%BE%E5%8C%BA%E7%89%88%E8%A2%AB%E6%95%85%E6%84%8F%E9%98%89%E5%89%B2%EF%BC%8CWeb%E7%AE%A1%E7%90%86%E5%8A%9F%E8%83%BD%E5%85%A8%E9%9D%A2%E7%A7%BB%E9%99%A4%EF%BC%8C%E6%9D%A5%E8%AF%95%E8%AF%95%E5%9B%BD%E4%BA%A7%E7%9A%84RustFS%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 面试官：一台服务器最大能支持多少条 TCP 连接？问倒一大片。。。3. 用雪花 id 和 uuid 做 MySQL 主键，被领导怼了4. SpringBoot 实现电子文件签字+合同系统！
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文