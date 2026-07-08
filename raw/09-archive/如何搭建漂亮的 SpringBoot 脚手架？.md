---
title: "如何搭建漂亮的 SpringBoot 脚手架？"
source: "https://mp.weixin.qq.com/s/NE7MXtUv7UadZiN0qxpshA"
---
Java学习者社区 *2026年7月6日 15:02*

![图片](assets/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E6%BC%82%E4%BA%AE%E7%9A%84%20SpringBoot%20%E8%84%9A%E6%89%8B%E6%9E%B6%EF%BC%9F/a4e6bbf28e3a1ff5323a81b2f9610e62_MD5.webp)

来源： [juejin.cn/post/7360947498943578139](http://juejin.cn/post/7360947498943578139)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 1.项目初始化
- 2.版本管理
- 3.废话不多说，直接看脚手架
- 3.1 常用工具
- 总结

---

## 1\. 项目初始化

如果你问研发同学，在开发过程中最讨厌、最痛苦的事情是什么？大部分同学会告诉环境，环境，还是环境。

我带你走一趟你就知道环境搭建是多么头疼的事情了。

在开发一个新项目之前，先下载 IDE，光是 IDE 这个事情，可能就折腾半天。为啥要折腾这么久呢，下载倒是非常快，可现在的 IDE 基本上都收费，所以网上就出现了各种破解软件，有每 30 天需要激活一次的，有各种 lisence 的，总之这些方法在你尝试了很多次之后，基本无一奏效，jetBrains 是靠这个挣钱的，如果大家都破解了，人家怎么生存？找各种方法破解，最终都是浪费时间。

为啥大家喜欢用盗版呀，不是喜欢，有免费的会用收费的吗？这是一种心理。说起用盗版这个成因可能就比较复杂了，大部分程序员是随着免费环境成长起来的，一说到收费，第一反应是很难适应的，还记得 Mp3 吗？刚开始的时候大家都免费下载 MP3，但后来因为版权问题开始收费了，下载量跌了 50%。

可能还有另外一个原因，作为程序员还不能找一个破解的方法？虽然你道高一尺，但我魔高一丈。

除此之外，大家觉得收费并不便宜，所以望而却步了。

虽然有诸多限制，但 IDE 必须还得用啊，官方提供了社区版，很多同学用着社区版，还有一部分同学继续走着破解之路。接下来咱们先看看如何用 IDE 创建 springboot 项目，然后一路 next 就行了

![图片](assets/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E6%BC%82%E4%BA%AE%E7%9A%84%20SpringBoot%20%E8%84%9A%E6%89%8B%E6%9E%B6%EF%BC%9F/1f098c213b7d7e78fde92c7d58c7c1b2_MD5.jpg)

这就是刚创建好的项目，新鲜出炉，有启动类、配置文件、测试启动类。

![图片](assets/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E6%BC%82%E4%BA%AE%E7%9A%84%20SpringBoot%20%E8%84%9A%E6%89%8B%E6%9E%B6%EF%BC%9F/2e7d7703ab60df35542594fcd1cc6f97_MD5.jpg)

## 2\. 版本管理

咱们的项目就这么轻松的创建成功了，是不是可以上手开发了，先别着急。先给你看个东西。

这是 springCloud 和 springboot 版本之间的对应关系：

![图片](assets/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E6%BC%82%E4%BA%AE%E7%9A%84%20SpringBoot%20%E8%84%9A%E6%89%8B%E6%9E%B6%EF%BC%9F/a3c2f4c87b65a7e304ddb40ea36bdc90_MD5.jpg)

- `              https://spring.io/projects/spring-cloud            `

这是 springboot 和 kafka 的版本对应关系：

![图片](assets/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E6%BC%82%E4%BA%AE%E7%9A%84%20SpringBoot%20%E8%84%9A%E6%89%8B%E6%9E%B6%EF%BC%9F/3fe534bde9087a25b160b8b37113229d_MD5.jpg)

- `              https://spring.io/projects/spring-kafka            `

很复杂吧，瞬间就想骂娘了？

我先给你讲个最近发生的故事，让你平复一下心情。我最近就在 spring-kakfa 版本上面栽了跟头

事情是这样的：我们生产环境用的 kafka-server 是 0.11 版本的，但我们的客户端用的是 3.0.4 版本，我的 springboot 用的是 2. [7.x](http://7.x/) 版本，从上边表中看到 springboot 的版本和 kafka-client 的版本是适配的，但 kafka-client 的版本和 server 的版本是不适配的

这是当时的报错信息

```
?,?:Exception thrown when sending a message with key='null' and payload='byte[205]' to topic notify

            org.apache.kafka.common.errors.UnsupportedVersionException:
           Attempting to use idempotence with a broker which does not support the required message format (v2). The broker must be version * 0.11* or later.
```

你可能会问这是非常容易发现的问题呀，也很容易测试出来呀，对，问题很容易复现

关键就是生产环境的版本和测试环境的 server 版本不一样，不一样，不一样，真是没想到啊，所以就栽了跟头。

有一款神器不是叫 Maven 吗，这个不就是解决版本之间的依赖关系吗？

在说 maven 之前，先简单说一下 springboot 的自动配置，在 springboot 出来之前，大家依赖关系都是通过手动添加，springboot 的 autoconfiuration 功能解决了包之间依赖关系，至少让研发的开发效率提升了 50%，但有些场景下依赖的冲突还是未能解决。

Apache Maven is a software project management and comprehension tool

我们最常用的 maven 命令是 build，package，在构建上真的是一把利器，maven 确实提升了研发的效率。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E6%BC%82%E4%BA%AE%E7%9A%84%20SpringBoot%20%E8%84%9A%E6%89%8B%E6%9E%B6%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

## 3\. 废话不多说，直接看脚手架

![图片](assets/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E6%BC%82%E4%BA%AE%E7%9A%84%20SpringBoot%20%E8%84%9A%E6%89%8B%E6%9E%B6%EF%BC%9F/e8a79280febf3a1a226c5bab9f5e72c2_MD5.jpg)

接下来我们来看看都有哪些核心类，我把代码贴到下方。

![图片](assets/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E6%BC%82%E4%BA%AE%E7%9A%84%20SpringBoot%20%E8%84%9A%E6%89%8B%E6%9E%B6%EF%BC%9F/61236f32dcf2999cb356a4479ca60149_MD5.jpg)

全局异常处理

```
@RestControllerAdvice
@ResponseBody
@Slf4j
publicclass GlobalExceptionHandler {

    @ExceptionHandler(value = {MethodArgumentNotValidException.class})
    public ResponseResult<String> handleValidException(MethodArgumentNotValidException ex, HttpServletResponse httpServletResponse) {
        
            log.error(
          "[GlobalExceptionHandler][handleValidException] 参数校验exception", ex);
        return wrapperBindingResult(
            ex.getBindingResult(),
           httpServletResponse);
    }

    private ResponseResult<String> wrapperBindingResult(BindingResult bindingResult, HttpServletResponse httpServletResponse) {
        StringBuilder errorMsg = new StringBuilder();
        for (ObjectError error : 
            bindingResult.getAllErrors())
           {
            if (error instanceof FieldError) {
                
            errorMsg.append(((FieldError)
           error).getField()).append(": ");
            }
            
            errorMsg.append(error.getDefaultMessage()
           == null ? "" : 
            error.getDefaultMessage());
          
        }
        
            httpServletResponse.setStatus(HttpStatus.BAD_REQUEST.value());
          
        return 
            ResponseResult.failed(ResultCode.FAILED.getCode(),
           null);
    }
}
```

日志处理

```
@Aspect
@Slf4j
@Component
publicclass WebLogAspect {

    @Pointcut("@within(
            org.springframework.stereotype.Controller)
           || @within(
            org.springframework.web.bind.annotation.RestController)"
          )
    public void cutController() {
    }

    @Before("cutController()")
    public void doBefore(JoinPoint point) {
        // 获取拦截方法的参数
        HttpServletRequest request = ((ServletRequestAttributes) 
            RequestContextHolder.getRequestAttributes()).getRequest();
          
        String url = 
            request.getRequestURL().toString();
          
        List list = 
            Lists.newArrayList();
          
        for (Object object : 
            point.getArgs())
           {
            if (object instanceof MultipartFile || object instanceof HttpServletRequest || object instanceof HttpServletResponse || object instanceof BindingResult) {
                continue;
            }
            
            list.add(object);
          
        }
        
            log.info(
          "请求 uri:[{}],params:[{}]", url, 
            StringUtils.join(list,
           ","));
    }

    /**
     * 返回通知：
     * 1. 在目标方法正常结束之后执行
     * 1. 在返回通知中补充请求日志信息，如返回时间，方法耗时，返回值，并且保存日志信息
     *
     * @param response
     * @throws Throwable
     */
    @AfterReturning(returning = "response", pointcut = "cutController()")
    public void doAfterReturning(Object response) {
        if (response != null) {
            
            log.info(
          "请求返回result:[{}]", 
            JSONUtil.toJsonStr(response));
          
        }
    }
}
```

跨域类

```
@Configuration
publicclass GlobalCorsConfig {
    /**
     * 允许跨域调用的过滤器
     */
    @Bean
    public CorsFilter corsFilter() {
        CorsConfiguration config = new CorsConfiguration();
        // 允许所有域名进行跨域调用
        
            config.setAllowedOrigins(Lists.newArrayList(
          "*"));
        // 允许跨越发送 cookie
        
            config.setAllowCredentials(
          true);
        // 放行全部原始头信息
        
            config.addAllowedHeader(
          "*");
        // 允许所有请求方法跨域调用
        
            config.addAllowedMethod(
          "*");
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        
            source.registerCorsConfiguration(
          "/**", config);
        returnnew CorsFilter(source);
    }
}

@Configuration
@EnableOpenApi
publicclass SwaggerConfig {
    @Bean
    public Docket docket() {
        returnnew Docket(
            DocumentationType.OAS_30)
          
                .apiInfo(apiInfo()).enable(true)
                .select()
                // apis：添加 swagger 接口提取范围
                .apis(
            RequestHandlerSelectors.basePackage(
          "
            com.vines.controller"
          ))
                //.apis(
            RequestHandlerSelectors.withMethodAnnotation(ApiOperation.class))
          
                .paths(
            PathSelectors.any())
          
                .build();
    }

    private ApiInfo apiInfo() {
        returnnew ApiInfoBuilder()
                .title("项目描述")
                .description("基础服务项目描述")
                .contact(new Contact("作者", "作者URL", "作者Email"))
                .version("1.0")
                .build();
    }
}
```

响应体

```
@Data
publicclass ResponseResult<T> {
    privateint code;
    private String message;
    private T data;

    publicstatic <T> ResponseResult<T> success(T data) {
        ResponseResult<T> responseResult = new ResponseResult<>();
        
            responseResult.setCode(ResultCode.SUCCESS.getCode());
          
        
            responseResult.setMessage(ResultCode.SUCCESS.getMessage());
          
        
            responseResult.setData(data);
          
        return responseResult;
    }

    publicstatic <T> ResponseResult<T> success() {
        ResponseResult<T> responseResult = new ResponseResult<>();
        
            responseResult.setCode(ResultCode.SUCCESS.getCode());
          
        
            responseResult.setMessage(ResultCode.SUCCESS.getMessage());
          
        return responseResult;
    }

    publicstatic <T> ResponseResult failed(int code, String message) {
        ResponseResult<T> responseResult = new ResponseResult<>();
        
            responseResult.setCode(code);
          
        
            responseResult.setMessage(message);
          
        return responseResult;
    }

    public static boolean isSucceed(ResponseResult responseResult) {
        return 
            responseResult.getCode()
           == 
            ResultCode.SUCCESS.getCode();
          
    }
}
```

### 3.1 常用工具

除了这些基本的工具之外，我再推荐几款我们项目中常用的工具

我们项目常常依赖中间件，比如 mysql，kafka，redis 等，如果要单元测试，我们通常的做法是在 dev 环境部署一套项目中依赖的中间件，非常麻烦，而且数据还不容易隔离，所以内存版的中间件就是来解决这个问题的。

内存版 Redis：

- `              https://github.com/kstyrc/embedded-redis            `

内存版 DB：

- `              https://github.com/mariadb            `

内存版 kafka，springboot 提供了测试依赖，直接引入 starter 即可

```
<groupId>
            org.springframework.kafka
          </groupId>
<artifactId>spring-kafka</artifactId>
```

hutool：

- `              https://hutool.cn/            `

mybatis plus：

- `              https://baomidou.com/            `

mapStruct：

- `              https://mapstruct.org/            `

redisson:

- `              https://github.com/redisson/redisson            `

## 总结

在真实的工作中，IDE 的配置工作其实不是最麻烦的和最浪费的时间的，有一件事情更加浪费时间，每次搞的我都特别的崩溃，这件事情也和环境相关，同时也和其他人相关。你们猜猜是什么事情呢？

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E5%A6%82%E4%BD%95%E6%90%AD%E5%BB%BA%E6%BC%82%E4%BA%AE%E7%9A%84%20SpringBoot%20%E8%84%9A%E6%89%8B%E6%9E%B6%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 我们放弃了Nacos作为配置中心，转而选择了这款神器~
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文