---
title: "SpringBoot3.2 + jdk21 + GraalVM上手体验"
source: "https://mp.weixin.qq.com/s/ox-UR05tGPuvgooZBe5snA"
---
小哈学Java *2026年6月29日 14:21*

![图片](assets/SpringBoot3.2%20+%20jdk21%20+%20GraalVM%E4%B8%8A%E6%89%8B%E4%BD%93%E9%AA%8C/3d79c4162abe4f51b7a4867de3e2cea8_MD5.webp)

来源： [juejin.cn/post/7307522662287851558](http://juejin.cn/post/7307522662287851558)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 快速体验（二进制部署）
- 快速体验（jar 部署）
- 对比 golang
- 对比 Rust
- 结论

---

![在这里插入图片描述](assets/SpringBoot3.2%20+%20jdk21%20+%20GraalVM%E4%B8%8A%E6%89%8B%E4%BD%93%E9%AA%8C/a4cd3c00ac8afad062514d78a838e706_MD5.webp)
- 可以参考官方文章进行体验： [spring.io/blog/2023/09/09/all-together-now-spring-boot-3-2-graalvm-native-images-java-21-and-virtual](http://spring.io/blog/2023/09/09/all-together-now-spring-boot-3-2-graalvm-native-images-java-21-and-virtual)
- 通过官方快速得到一个基于 jdk21 的项目： [start.spring.io/](http://start.spring.io/)

## 快速体验（二进制部署）

```
@RestController
@SpringBootApplication
publicclassDemoApplication{

    publicstaticvoidmain(String[] args){
        
            SpringApplication.run(DemoApplication
          .class, args);
    }

    @GetMapping("/customers")
    Collection<Customer> customers(){
        return 
            Set.of(
          new Customer(1, "A"), new Customer(2, "B"), new Customer(3, "C"));
    }

    record Customer(Integer id, String name){
    }
}
```

启动非常快，秒启动

![image-20231201173556211](assets/SpringBoot3.2%20+%20jdk21%20+%20GraalVM%E4%B8%8A%E6%89%8B%E4%BD%93%E9%AA%8C/a1a48a70ff0730813780fd821cb8ba4f_MD5.jpg)

image-20231201173556211

压测环境内存占用大概 70MB 左右，空闲时在 20MB 左右（由于直接打成二进制文件了，不能再使用 jconsole、arthas 之类的进行监控了），性能上由于不需要 JVM 预热，性能启动即巅峰。

```
$ ab -c 50 -n 10000 http://localhost:8080/customers
Server Software:
Server Hostname:        localhost
Server Port:            8080

Document Path:          /customers
Document Length:        61 bytes

Concurrency Level:      50
Time taken for tests:   1.413 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1660000 bytes
HTML transferred:       610000 bytes
Requests per second:    7076.39 [#/sec] (mean)
Time per request:       7.066 [ms] (mean)
Time per request:       0.141 [ms] (mean, across all concurrent requests)
Transfer rate:          1147.15 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2   8.0      2     144
Processing:     1    5   6.7      4     147
Waiting:        0    4   5.6      3     145
Total:          1    7  10.4      6     149
```
![image-20231201173732084](assets/SpringBoot3.2%20+%20jdk21%20+%20GraalVM%E4%B8%8A%E6%89%8B%E4%BD%93%E9%AA%8C/c23833d79ffbdca9e060acab8e901c2c_MD5.jpg)

image-20231201173732084

## 快速体验（jar 部署）

jar 包占用只有 19MB，已经不能算是小胖 jar 了 😊

![image-20231201175815773](assets/SpringBoot3.2%20+%20jdk21%20+%20GraalVM%E4%B8%8A%E6%89%8B%E4%BD%93%E9%AA%8C/ff62bd236c258113dd1a414fb0d3971c_MD5.jpg)

image-20231201175815773

内存占用在压测时大概在 200MB 左右，空闲时在 160MB 左右。性能显然也不是启动即巅峰，可以看出其实还是需要进行 JVM 预热才能达到性能巅峰的

```
$ ab -c 50 -n 10000 http://localhost:8080/customers
Server Software:
Server Hostname:        localhost
Server Port:            8080

Document Path:          /customers
Document Length:        61 bytes

Concurrency Level:      50
Time taken for tests:   17.930 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      1660000 bytes
HTML transferred:       610000 bytes
Requests per second:    557.72 [#/sec] (mean)
Time per request:       89.651 [ms] (mean)
Time per request:       1.793 [ms] (mean, across all concurrent requests)
Transfer rate:          90.41 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   38 430.2      2    7004
Processing:     0   14  90.4      8    1773
Waiting:        0   12  88.7      6    1771
Total:          1   53 439.0     10    7011
```
![image-20231201180038447](assets/SpringBoot3.2%20+%20jdk21%20+%20GraalVM%E4%B8%8A%E6%89%8B%E4%BD%93%E9%AA%8C/fc51e09876325178325ddc7b3c434ae7_MD5.jpg)

image-20231201180038447

## 对比 golang

```
package main

import (
    "encoding/json"
    "flag"
    "fmt"
    "net/http"
)

var port = 
            flag.String(
          "p", "8080", "please input port")

funcmain() {
    
            http.HandleFunc(
          "/customers", func(writer 
            http.ResponseWriter,
           request *
            http.Request)
           {
        data, _ := 
            json.Marshal(request.URL)
          
        
            writer.Write(data)
          
    })
    e := make(chan error)
    gofunc() {
        e <- 
            fmt.Errorf(
          "error[%v]", 
            http.ListenAndServe(
          ":"+*port, nil))
    }()
    
            fmt.Println(
          "http 服务器启动...")
    
            fmt.Println(<-e)
          
}
```

这里 golang 没有使用框架，仅使用标准库，所以内存占用较低，仅 10MB 左右，不过即使使用 Gin 之类的 web 框架，内存也不会超过 20MB

```
$ ab -c 50 -n 10000 http://localhost:8080/customers
Server Software:
Server Hostname:        localhost
Server Port:            8080

Document Path:          /customers
Document Length:        161 bytes

Concurrency Level:      50
Time taken for tests:   1.380 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      2790000 bytes
HTML transferred:       1610000 bytes
Requests per second:    7247.68 [#/sec] (mean)
Time per request:       6.899 [ms] (mean)
Time per request:       0.138 [ms] (mean, across all concurrent requests)
Transfer rate:          1974.71 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    2  16.5      2     459
Processing:     0    4  27.9      2     460
Waiting:        0    2  10.5      2     459
Total:          1    7  32.3      4     462
```
![image-20231201174441704](assets/SpringBoot3.2%20+%20jdk21%20+%20GraalVM%E4%B8%8A%E6%89%8B%E4%BD%93%E9%AA%8C/0fc6538fc01dbfd14b58bb644c1881b2_MD5.jpg)

image-20231201174441704

## 对比 Rust

```
[dependencies]
actix-web = "4"

use actix_web::{get, App, HttpRequest, HttpResponse, HttpServer, Responder};

#[get("/customers")]
asyncfnecho(req: HttpRequest) -> impl Responder {
    let url = 
            req.uri().to_string();
          
    HttpResponse::Ok().body(url)
}

#[actix_web::main]
asyncfnmain() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .service(echo)
    })
    .bind(("127.0.0.1", 8080))?
    .run()
    .await
}
```

Actix-web 空闲时内存占用大概 3MB 左右，压测时占用大概 6MB 左右

```
$ ab -c 50 -n 10000 http://localhost:8080/customers
Server Software:
Server Hostname:        127.0.0.1
Server Port:            8080

Document Path:          /customers
Document Length:        10 bytes

Concurrency Level:      50
Time taken for tests:   1.091 seconds
Complete requests:      10000
Failed requests:        0
Total transferred:      860000 bytes
HTML transferred:       100000 bytes
Requests per second:    9163.48 [#/sec] (mean)
Time per request:       5.456 [ms] (mean)
Time per request:       0.109 [ms] (mean, across all concurrent requests)
Transfer rate:          769.59 [Kbytes/sec] received

Connection Times (ms)
             min  mean[+/-sd] median   max
Connect:       0    2  11.0      2     189
Processing:    0    3   7.0      3     190
Waiting:       0    2   7.0      2     189
Total:         2    5  13.1      4     193
```
![image-20231204115913574](assets/SpringBoot3.2%20+%20jdk21%20+%20GraalVM%E4%B8%8A%E6%89%8B%E4%BD%93%E9%AA%8C/2f80ef648188f9c3833546610f1d5724_MD5.jpg)

image-20231204115913574

rust 虽然有非常厉害的零成本抽象，但作为代价其编译时间会比较长（在实际项目中真的特别长 😢）

```
$ time cargo build
cargo build  213.00s user 23.08s system 258% cpu 1:31.39 total
```

## 结论

AOT-processed 已经相对成熟，效果可以说非常惊艳，解决了 JVM 启动慢、需要预热、内存占用大等问题。

美中不足的是编译速度非常慢，笔者电脑是 2017 款 mac book pro 编译花费大概 15 分钟左右

```
Finished generating 'demo'in 14m 33s.
[INFO] ------------------------------------------------------------------------
[INFO] BUILD SUCCESS
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  15:45 min
[INFO] Finished at: 2023-12-01T17:00:21+08:00
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 15:45 min [INFO] Finished at: 2023-12-01T17:00:21+08:00
[INFO] ------------------------------------------------------------------------
```

可以看出 java 在云原生大环境下已经取得了不错的进步的

**参考资料**

\[1\] [spring.io/blog/2023/0…:](http://spring.io/blog/2023/0%E2%80%A6:) [https://spring.io/blog/2023/09/09/all-together-now-spring-boot-3-2-graalvm-native-images-java-21-and-virtual](https://spring.io/blog/2023/09/09/all-together-now-spring-boot-3-2-graalvm-native-images-java-21-and-virtual) \[2\] [start.spring.io/:](http://start.spring.io/:) [https://start.spring.io/](https://start.spring.io/)

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/SpringBoot3.2%20+%20jdk21%20+%20GraalVM%E4%B8%8A%E6%89%8B%E4%BD%93%E9%AA%8C/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 腾讯一面：路由器与交换机的区别是什么？我：咋还问网络相关的...3. MyBatis Plus 封神玩法：这12个骚操作让开发效率直接起飞！4. 一个 Token 就够了，JWT 续签为什么要搞 Access Token + Refresh Token 双 Token？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文