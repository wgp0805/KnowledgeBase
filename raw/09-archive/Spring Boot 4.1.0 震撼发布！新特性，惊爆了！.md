---
title: "Spring Boot 4.1.0 震撼发布！新特性，惊爆了！"
source: "https://mp.weixin.qq.com/s/U2aDPmeGbQrZMS__oZnMbw"
---
java1234 *2026年6月25日 09:06*

大家好，我是锋哥。

> 2026 年 6 月 10 日，Spring Boot 4.1.0 正式发布了。如果你还在手动折腾 gRPC 依赖、担心 HTTP 客户端被恶意利用，或者觉得 Redis 监听要写一堆配置——这一版，真的值得花十分钟了解一下。

---

![图片](assets/Spring%20Boot%204.1.0%20%E9%9C%87%E6%92%BC%E5%8F%91%E5%B8%83%EF%BC%81%E6%96%B0%E7%89%B9%E6%80%A7%EF%BC%8C%E6%83%8A%E7%88%86%E4%BA%86%EF%BC%81/ea443c16b894dae2708611905dcc2986_MD5.webp)

## 目录

- 一、这次升级，到底改了什么？
- 二、官方 gRPC 支持：终于不用自己拼 Starter 了
- 三、HTTP 客户端防 SSRF：给出站请求加一道门
- 四、懒加载 JDBC 连接：事务开了，连接先别急
- 五、@RedisListener 自动配置：监听 Redis 更省事
- 六、可观测性升级：OpenTelemetry 更好用了
- 七、其他值得留意的改进
- 八、升级前的小提醒

---

## 一、这次升级，到底改了什么？

Spring Boot 4.1.0 是在 4.0 基础上的第一个小版本大更新。官方博客用一句话概括： **更好写、更安全、更好观测** 。

几个关键词先记住：

| 方向 | 代表特性 |
| --- | --- |
| 微服务通信 | 内置 gRPC 服务端 / 客户端自动配置 |
| 安全加固 | HTTP 客户端 `InetAddressFilter` 防 SSRF |
| 性能优化 | JDBC 连接懒加载 |
| 开发体验 | `@RedisListener` 自动配置、Jackson 配置更统一 |
| 运维观测 | OpenTelemetry 增强、Info 端点新增进程信息 |

下面挑几个最实用的，配上 Demo 走一遍。

---

## 二、官方 gRPC 支持：终于不用自己拼 Starter 了

以前想在 Spring Boot 里用 gRPC，往往得找第三方 Starter，版本对齐、拦截器、健康检查都要自己琢磨。 **4.1 开始，Spring 官方下场了** ——引入 `spring-boot-starter-grpc-server` ，写个服务类，应用跑起来 gRPC 端口就起来了（默认 9090）。

### 第一步：加依赖

```xml
<dependency>    <groupId>
            org.springframework.boot
          </groupId>    <artifactId>spring-boot-starter-grpc-server</artifactId></dependency>
```

### 第二步：写个 Hello 服务

假设你已经根据 `.proto` 文件生成了 `              HelloWorldGrpc.HelloWorldImplBase            ` ：

```java
import 
            io.grpc.stub.StreamObserver;
          import 
            org.springframework.grpc.server.service.GrpcService;
          
@GrpcServicepublic class HelloService extends HelloWorldGrpc.HelloWorldImplBase {
    @Override    public void sayHello(HelloRequest request, StreamObserver<HelloReply> responseObserver) {        String message = "你好，" + 
            request.getName()
           + "！欢迎体验 Spring Boot 4.1 的 gRPC！";        HelloReply reply = 
            HelloReply.newBuilder().setMessage(message).build();
                  
            responseObserver.onNext(reply);
                  
            responseObserver.onCompleted();
              }}
```

### 第三步：启动应用

```cs
@SpringBootApplicationpublic class DemoApplication {    public static void main(String[] args) {        
            SpringApplication.run(DemoApplication.
          class, args);    }}
```

就这么几行，gRPC 服务就注册好了。另外还支持 `@GrpcAdvice` 做统一异常处理，以及和 Micrometer 联动的链路追踪拦截器——做微服务的朋友应该会松一口气。

---

## 三、HTTP 客户端防 SSRF：给出站请求加一道门

SSRF（服务端请求伪造）是个老问题：你的接口如果允许传 URL，攻击者可能让服务器去访问内网地址，比如 `http://127.0.0.1` 、内网数据库端口等。

4.1 新增了 `InetAddressFilter` ，可以限制 HTTP 客户端 **只允许访问哪些 IP 段** ，阻塞和响应式客户端都支持。

### 方式一：只允许访问公网地址

```java
import 
            org.springframework.boot.http.client.HttpClientSettings;
          import 
            org.springframework.boot.http.client.InetAddressFilter;
          import 
            org.springframework.http.client.ClientHttpRequestFactory;
          import 
            org.springframework.stereotype.Service;
          import 
            org.springframework.web.client.RestClient;
          
@Servicepublic class SafeApiClient {
    private final RestClient restClient;
    public SafeApiClient() {        // 只允许访问外部公网地址，内网 IP 一律拒绝        InetAddressFilter filter = 
            InetAddressFilter.externalAddresses();
                  HttpClientSettings settings = 
            HttpClientSettings.defaults()
                          .withInetAddressFilter(filter);        ClientHttpRequestFactory factory = 
            ClientHttpRequestFactoryBuilder.jdk().build(settings);
                  this.restClient = 
            RestClient.builder()
                          .requestFactory(factory)                .baseUrl("
            https://api.example.com"
          )                .build();    }
    public String fetchData(String path) {        return 
            restClient.get().uri(path).retrieve().body(String.class);
              }}
```

### 方式二：注册全局 Bean，白名单 + 黑名单组合

```kotlin
import 
            org.springframework.boot.http.client.InetAddressFilter;
          import 
            org.springframework.context.
          annotation.Bean;import 
            org.springframework.context.
          annotation.Configuration;
@Configurationpublic class HttpSecurityConfig {
    @Bean    public InetAddressFilter httpClientInetAddressFilter() {        // 允许 192.168.1.0/24 网段，但排除 .1 和 .10 两个地址        return 
            InetAddressFilter.of(
          "192.168.1.0/24")                .andNot("192.168.1.1", "192.168.1.10");    }}
```

如果你的业务需要根据用户输入去请求外部 URL， **强烈建议** 加上这层过滤，比事后补漏洞省心多了。

---

## 四、懒加载 JDBC 连接：事务开了，连接先别急

做过数据库开发的朋友可能遇到过：方法加了 `@Transactional` ，但里面其实没执行 SQL，连接却已经从池里借出来了——白白占着资源。

4.1 新增了 `              spring.datasource.connection-fetch            ` 配置，设为 `lazy` 后，只有 **真正要执行 SQL 语句时** 才会从连接池取物理连接。

### 配置示例

```bash
spring:  datasource:    url: jdbc:mysql://localhost:3306/db_demo    username: root    password: 123456    connection-fetch: lazy   # 可选值：eager（默认）、lazy
```

### 效果对比（伪代码理解）

```typescript
@Servicepublic class OrderService {
    @Transactional    public void processOrder(Long orderId) {        // eager 模式：进入方法时就已经借了连接        // lazy  模式：下面这行执行前，连接还没真正借出        if (orderId == null) {            return;  // 提前返回，lazy 模式下连接从未被占用        }        // 执行 SQL 时，连接才真正从池里取出        orderRepository.findById(orderId);    }}
```

对于事务方法多、但不一定每次都查库的场景，这个开关挺实用。

---

## 五、@RedisListener 自动配置：监听 Redis 更省事

以前用 Spring Data Redis 做消息监听，得自己配 `RedisMessageListenerContainer` 。4.1 帮你把这一步省掉了——只要项目里有 Redis，没自定义容器，框架会自动注册一个默认容器，扫描 `@RedisListener` 方法。

### Demo：监听订单取消频道

```kotlin
import 
            org.springframework.
          data.
            redis.connection.Message;
          import 
            org.springframework.
          data.
            redis.connection.MessageListener;
          import 
            org.springframework.
          data.
            redis.listener.adapter.MessageListenerAdapter;
          import 
            org.springframework.stereotype.Component;
          
@Componentpublic class OrderEventListener {
    @RedisListener(topics = "order:cancel")    public void onOrderCancel(String message) {        System.out.println("收到订单取消消息：" + message);        // 在这里做库存回滚、通知用户等逻辑    }}
```

### 可选配置

```bash
spring:  data:    redis:      host: localhost      port: 6379      listener:        enabled: true   # 默认开启
```

注意： `spring-boot-starter-data-redis` 现在会自动引入 `spring-messaging` 依赖，不用你再手动加了。

---

## 六、可观测性升级：OpenTelemetry 更好用了

链路追踪和日志采集在 4.1 里又前进了一步，几个常用配置如下：

```bash
management:  opentelemetry:    enabled: true                          # 可一键关闭 SDK，用 no-op 实现    tracing:      sampler: parentbased_always_on       # 采样策略      limits:        max-attributes: 128    logging:      limits:        max-attributes: 128
  otlp:    metrics:      export:        compression-mode: gzip             # OTLP 指标 gzip 压缩
```

另外， `@Async` 异步方法现在可以自动传播上下文了——异步线程里也能串起完整的 Trace，排查问题更顺。

访问 `/actuator/info` ，还能看到这些进程信息：

- 运行时长（uptime）
- 启动时间（startTime）
- 时区、语言环境
- 工作目录

运维同学查问题时会少问几句「这服务跑了多久了」。

---

## 七、其他值得留意的改进

篇幅有限，再列几个「知道就赚到」的点：

**Jackson 配置更统一**

JSON、XML、CBOR 通用的读写特性，可以用统一前缀配置：

```bash
spring:  jackson:    read:      fail-on-unknown-properties: true    write:      indent-output: true
```

**配置文件导入可指定编码**

```cpp
spring:  config:    import: classpath:import.properties[encoding=utf-8]
```

以前属性文件默认 ISO-8859-1，中文注释或值容易乱码，现在可以显式指定 UTF-8。

**Spring Batch 支持 MongoDB 后端**

新增 `spring-boot-batch-data-mongo` Starter，不想用关系型库存批处理元数据的团队有了新选择。

**Log4j 日志轮转**

支持按大小、时间、Cron 表达式等多种轮转策略，生产环境日志管理更灵活。

**Kotlin 基线升到 2.3**

Kotlin 项目可以直接享受新版本语言特性，并支持 Java 25。

---

## 八、升级前的小提醒

从 Spring Boot 4.0 升上来，注意这几件事：

1. **4.0 里已废弃的 API 在本版本被移除了** ，升级前先扫一遍编译警告。
2. **Apache Derby 集成已废弃** ，还在用的建议迁到 H2 或 HSQL。
3. Maven 跳过测试时， `-DskipTests` 不再跳过 AOT 处理，请改用 `-             Dmaven.test.skip=true           ` 。
4. 如果之前用过 Spring gRPC 1.0 的第三方 Starter，官方提供了迁移指南，建议对照升级。

[2026年，锋哥又开始收AI编程学员了！目前活动，送Java+Python+AI大模型VIP。。。](https://mp.weixin.qq.com/s?__biz=Mzg4ODA3NTk0Nw==&mid=2247539909&idx=2&sn=d1cb9c17a83d521d4bc91ae66e4a85b1&scene=21#wechat_redirect)