---
source_url: "https://mp.weixin.qq.com/s/1XO9l0eFULUQ3ZVU3v30Sg"
title: "告别Swagger UI！一款更适合 SpringBoot 的API文档新选择"
account: "小哈学Java"
published_at: "2026-11-01 19:52:24"
saved_at: "2026-11-02 07:26:45"
sync_id: "art_bc40334980cb49c0841060be2e51b466"
parse_status: "ok"
---

# 告别Swagger UI！一款更适合 SpringBoot 的API文档新选择

将 **小哈学Java**** **设为“**星标****⭐**”

第一时间收到文章更新

![](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/b1f41f68b702a9bcd9334521c0a3f083_MD5.png)

来源：blog.csdn.net/2503_92695612

**在线 Java 面试刷题（已更新334题，图文并茂）**：https://www.quanxiaoha.com/java-interview

**目录**

- SpringDoc 是什么
- 与 Swagger 的关系
- 为什么要选择 SpringDoc

- 正式开始
- 总结

## SpringDoc 是什么

SpringDoc 是一个专为 Spring Boot 应用设计的库，能够自动生成符合 OpenAPI 3 规范的 API 文档。它通过扫描项目中的控制器、方法注解及配置，动态生成 JSON/YAML/HTML 格式的文档，并提供交互式界面（如 Swagger UI）供开发者查看和测试 API

### 与 Swagger 的关系

Swagger 作为 OpenAPI 规范的前身，贡献了 API 设计理念并推动了 OpenAPI 的标准化。其核心工具 Swagger UI 用于展示交互式文档。

SpringDoc 并非 Swagger 的替代品，而是基于 OpenAPI 3 规范的实现工具，并天然集成 Swagger UI 作为文档展示界面

### 为什么要选择 SpringDoc

在 SpringDoc 面世之前，Spring 生态中集成实现 Swagger 的技术为 SpringFox，SpringFox 与 Swagger 之间的协作关系如下

##### SpringFox

- 代码扫描：SpringFox 在运行时扫描 Spring MVC 控制器（如  `@RestController`  ）、方法注解（如  `@RequestMapping`  ）以及 Swagger 专用注解（如  `@ApiOperation`  ），提取接口的路径、参数、响应等信息
- 生成 OpenAPI 规范文档： 将扫描结果转换为符合 Swagger 2.0 或 OpenAPI 3.0 规范的 JSON 文件
- 集成 Spring 生态，提供 Docket 配置类，支持自定义接口扫描范围（如包路径、URL 匹配规则）和文档信息（如标题、版本、作者）

##### Swagger

- 可视化文档渲染：将 SpringFox 生成的 JSON 文件解析为交互式网页，通过浏览器访问（如  `http://localhost:8080/swagger-ui.html`  ）
- 提供接口列表、参数说明、请求示例，并支持在线测试 API（可直接发送请求并查看响应）
- 标准化规范支持：Swagger 定义 OpenAPI 规范（原 Swagger 规范），为 API 描述提供统一标准（如接口路径、请求方法、数据类型），SpringFox 生成的 JSON 文件完全遵循此规范，确保与其他 Swagger 工具（如  `Swagger Editor`  ）兼容

##### 协作流程

- 开发阶段：开发者在 Spring 控制器中添加 Swagger 注解（如  `@Api`  、  `@ApiParam`  ），描述接口细节
- 运行时：SpringFox 扫描代码并生成 JSON 文档
- 展示阶段：Swagger UI 读取 JSON 文件，渲染为可视化界面供团队使用

在 2020 时，由于 SpringFox 官方基本停止维护，不再发布新版本或修复问题，再加上他无法适配 Spring Boot 2.6+ 及 3.x 版本，导致与新版本 Spring 生态冲突（如路径匹配失效、注解不兼容）。以及配置的复杂性导致他逐渐退出市场

转而由更新的技术–SpringDoc 接过接力棒，SpringDoc 完美支持 Spring Boot 2.6+ 及 3.x（含 JDK 17+），并且原生支持 OpenAPI 3 规范，除此之外，如果不需要特殊的复杂配置，甚至可以零配置，仅需引入一个依赖，即可实现开箱即用，还有他直接使用 JSR-303 规范注解（如  `@Schema` 、 `@Parameter` ），替代 SpringFox 的专属注解（如  `@ApiModel` ），降低了开发人员的学习成本

## 正式开始

**最小化配置使用**

不多说废话了，下面我们正式开始，首先我们先介绍最简单，最小化的引入以及使用方式

**第一步：引入 Jar 包**

```
<dependency>
    <groupId>org.springdoc</groupId>
    <artifactId>springdoc-openapi-starter-webmvc-ui</artifactId>
    <version>2.5.0</version> <!-- 建议使用最新版本 -->
</dependency>
```

**第二步：配置配置文件**

正常使用 SpringDoc，或多或少都会进行一些配置文件的配置，但是由于这里是进行最小化配置，所以这里不进行配置文件配置，仅仅介绍几个重要配置的默认项，给大家一个基础印象，方便大家理解后面运行时为什么要这样做，当然，如果不感兴趣的小伙伴也可以直接跳过，跟着步骤走，并不影响使用

```
# application.yml
springdoc:
# SpringDoc的API包扫描路径，如果不配置，SpringDoc 自动扫描整个项目类路径，它会自动识别所有 @RestController、@RequestMapping 等注解，生成 API 文档
packages-to-scan: com.example.controller
swagger-ui:
    # 是否开启swagger界面，依赖OpenApi，默认为true，如果要开启需要OpenApi同时开启
    enabled: true
    # 内置 Swagger UI 的访问路径，默认值为/swagger-ui/index.html
    path: /swagger-ui/index.html
    # 指定OpenAPI文档的URL（注意这里一定要与api-docs.path保持一致，否则会请求失败）
    url: /v3/api-docs
    # 是否禁用Swagger UI自带的示例接口（如 Petstore 等默认接口），默认值为false，仅展示当前项目的 API
    disable-swagger-default-url: false
api-docs:
    # 是否启用OpenAPI文档端点，默认为true
    enabled: true
    # OpenAPI 3规范的文档访问路径，默认值为/v3/api-docs
    path: /api-docs
```

**第三步：添加一个配置类，用于设置 Swagger-UI 页面的一些基础信息的展示**

```
@Configuration
@OpenAPIDefinition(info = @Info(
    title = "项目API文档",
    version = "1.0",
    description = "SpringBoot项目接口文档"
))
public class SpringDocConfig {
    // 无需额外配置，注解已定义基本信息
}
```

到这一步：其实已经可以访问页面，观看效果了（访问链接为： `http://localhost:8080/swagger-ui/index.html` ，注意如果上方配置文件修改了，这里要替换为对应的链接，我这里没有修改所以使用默认链接），只是项目如果没有任何 controller，这里会展示空页面，如下：

![在这里插入图片描述](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/696b840eb3fe71da861cd6150c5160b7_MD5.png)

空页面效果**第四步：在需要显示的 Controller 方法上加上注解，用于给方法添加备注，如下会展示不加注解与加注解的区别**

不加注解：

```
@RestController
@RequestMapping("/main")
public class MainController {
    @GetMapping("/index")
    public String index(String str1) {
        return "请求成功";
    }
}
```

![](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/112abff503bd93b5928206ba71636ad2_MD5.png)

不加注解的展示效果添加注解

```
@RestController
@RequestMapping("/main")
@Tag(name = "演示controller", description = "演示controller")
public class MainController {

    @GetMapping("/index")
    @Operation(summary = "演示方法", description = "演示方法的注释")
    public String index(
            @Parameter(description = "参数1", required = true) String str1) {
        return "请求成功";
    }

}
```

![在这里插入图片描述](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/44f189e6722aa18a53a82ca5dde817af_MD5.png)

添加注解后的展示效果至此为止，SpringDoc 的最小化使用已经全部完成（请注意，以上所有配置生效的前提是，当前 Spring 项目未添加任何过滤器、拦截器，以及未使用 SpringSecurity 等安全框架，否则，仅仅进行最小化配置是无法运行的，因为一些默认配置可能会被拦截，如果需要更复杂配置，请继续往下看）

**SpringDoc 中简单分组配置（包含编程式配置与声明式配置）**

上方仅仅只是展示了 SpringDoc 的最基础用法，接下来，我们展示 SpringDoc 的一种常用用法：分组，先上效果图，让大家了解是个什么功能

![在这里插入图片描述](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/5be855a6ca309a61b24a718f2e049ad1_MD5.png)

分组效果图接下来开始进行详细配置：

**方式一：编程式配置（灵活性高、扩展性强、调试友好）**

```
@Configuration
@OpenAPIDefinition(info = @Info(
        title = "项目API文档",
        version = "1.0",
        description = "SpringBoot项目接口文档"
))
public class SpringDocConfig {
    /**
     * 商品分组的配置（使用请求路径扫描的方式进行配置）
     * @return org.springdoc.core.models.GroupedOpenApi
     * @author ren
     * @date 2025/07/06 17:17
     */
    @Bean
    public GroupedOpenApi userGroup() {
        // 使用路径匹配方式：仅包含 /api/product/** 下的接口
        return GroupedOpenApi.builder()
                .group("商品模块")
                .pathsToMatch("/api/product/**")   // 路径匹配
                .build();
    }

    /**
     * 会员分组的配置（使用包扫描的方式进行配置）
     * @return org.springdoc.core.models.GroupedOpenApi
     * @author ren
     * @date 2025/07/06 17:17
     */
    @Bean
    public GroupedOpenApi productGroup() {
        // 使用包扫描方式：扫描 com.ren.main.controller.member 包下的所有接口
        return GroupedOpenApi.builder()
                .group("用户模块")
                .packagesToScan("com.ren.main.controller.member") // 包扫描
                .build();
    }

}
```

这种配置方式的原理是通过添加  `GroupedOpenApi`  类型的 Bean，项目启动时，SpringDoc 会寻找环境中是否存在  `GroupedOpenApi`  类型的 Bean，如果存在，则会创建分组进行展示

注意：

- 一旦这里配置了分组方式展示，那么在  `application.yml`  配置文件中配置的  `springdoc.packages-to-scan`  就会失效，因为 SpringDoc 的扫描机制，分组配置的扫描路径优先级大于配置文件配置的扫描优先级
- 路径扫描有两种方式，一种是根据请求路径进行扫描，一种是根据包路径进行扫描，上方都有进行配置
- 如果多个分组中有重合的路径，也就是说一个接口在多个分组配置的路径中都能扫描到，那么这个接口会存在于多个分组中

以下展示我的代码结构，方便大家理解：

![在这里插入图片描述](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/a9efdff1b14a648a78c70e48a0447af3_MD5.png)

代码结构

![在这里插入图片描述](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/8ba86b5fbc1ad3813a37b4595a4ae56a_MD5.png)

代码结构

![在这里插入图片描述](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/742c933b5937919246e8e1499779b581_MD5.png)

代码结构

![在这里插入图片描述](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/b839070dee3cd68f0b2127a158dffd01_MD5.png)

代码结构大家会发现，我的目录中有一个 MainController 的内容，在页面中没有展示了，这是为什么呢？原因我上面提过了，因为分组的配置会覆盖默认配置与配置文件配置，而分组配置中由于没有包含  `MainController`  的内容，所以， `MainController`  的内容没有地方展示了

那么如果想要展示出这个文件中的接口该怎么办呢？很简单，在分组中再加一个默认分组，用于展示所有接口内容即可，如下

```
@Configuration
@OpenAPIDefinition(info = @Info(
        title = "项目API文档",
        version = "1.0",
        description = "SpringBoot项目接口文档"
))
public class SpringDocConfig {

    /**
     * 默认分组
     * @return org.springdoc.core.models.GroupedOpenApi
     * @author ren
     * @date 2025/07/06 17:38
     */
    @Bean
    public GroupedOpenApi defaultGroup() {
        return GroupedOpenApi.builder()
                .group("默认分组")
                .pathsToMatch("/**")   // 路径匹配
                .build();
    }

    /**
     * 商品分组的配置（使用请求路径扫描的方式进行配置）
     * @return org.springdoc.core.models.GroupedOpenApi
     * @author ren
     * @date 2025/07/06 17:17
     */
    @Bean
    public GroupedOpenApi userGroup() {
        // 使用路径匹配方式：仅包含 /api/product/** 下的接口
        return GroupedOpenApi.builder()
                .group("商品模块")
                .pathsToMatch("/api/product/**")   // 路径匹配
                .build();
    }

    /**
     * 会员分组的配置（使用包扫描的方式进行配置）
     * @return org.springdoc.core.models.GroupedOpenApi
     * @author ren
     * @date 2025/07/06 17:17
     */
    @Bean
    public GroupedOpenApi productGroup() {
        // 使用包扫描方式：扫描 com.ren.main.controller.member 包下的所有接口
        return GroupedOpenApi.builder()
                .group("用户模块")
                .packagesToScan("com.ren.main.controller.member") // 包扫描
                .build();
    }
}
```

配置后展示的内容

![在这里插入图片描述](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/f064c88837428fce45d8fca7761a36f3_MD5.png)

配置默认分组后展示的内容看上面的图， `MainController`  的内容展示在这里了，同时  `ProductController`  和  `MemberController`  的内容也展示在这里了，这是为什么呢，原因我上面说过了，如果一个请求被多个分组扫描到，那么他会展示在多个分组中

**方式二：声明式配置（配置集中管理、可使用多配置文件进行环境隔离）**

```
springdoc:
  group-configs:
    - group: '默认分组'
      paths-to-match: '/**'
    - group: '商品模块'
      paths-to-match: '/api/product/**'
    - group: '用户模块'
      packages-to-scan: 'com.ren.main.controller.member'
```

![在这里插入图片描述](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/e7120f0836be562b17c9864d11344613_MD5.png)

声明式配置效果如上：效果与方式一相同

**如果项目中重写了 WebMvcConfigurer 的 addResourceHandlers 方法，所需进行的处理**

WebMvcConfigurer

 `WebMvcConfigurer`  是 Spring MVC 的配置中枢，用于定制化 Spring MVC 的各种行为。它不是过滤器或拦截器，而是一个配置接口（类似汽车的仪表盘），让你调整 Spring MVC 的运行方式。

他所拥有的方法

-  `addInterceptors(registry)`  ：注册拦截器
-  `addCorsMappings(registry)`  ：配置跨域权限
-  `addResourceHandlers(registry)`  ：指定静态资源路径
-  `addViewControllers(registry)`  ：设置简易页面跳转
-  `configureMessageConverters(list)`  ：定制 JSON/XML 解析器
-  `configurePathMatch(configurer)`  ：调整 URL 匹配规则
-  `addArgumentResolvers(list)`  ：自定义请求参数处理器
-  `addReturnValueHandlers(list)`  ：自定义返回值处理器
-  `configureContentNegotiation(configurer)`  ：内容协商配置（响应格式协商）

如果我们重写了  `WebMvcConfigurer`  的  `addResourceHandlers`  方法，那么原本 Spring 自己默认配置的所有的静态资源的指向路径就全都会失效，于是就需要我们自己去配置指定

```
@Configuration
public class ResourcesConfig implements WebMvcConfigurer
{
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {

        registry.addResourceHandler("/swagger-ui/**")
            .addResourceLocations("classpath:/META-INF/resources/webjars/springdoc-openapi-ui/")
            .setCacheControl(CacheControl.maxAge(5, TimeUnit.HOURS).cachePublic());
    }
}
```

按照如上设置后，SpringDoc 将恢复正常（注意新版的 SpringDoc 和老版的 SpringFox 配置有所区别，这里只展示新版 SpringDoc 的配置方法）如果大家对老版配置有需要，可以留言，留言人多会单独出一期

**如果项目引入了 SpringSecurity 需要进行的处理**

由于项目引入了 SpringSecurity，导致如果项目不经过认证无法访问系统资源，我们就需要在 SpringSecurity 的配置文件中放开 SpringDoc 相关的静态资源的拦截，如下

```
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
public class SecurityConfig {
    /*
     * 配置过滤器链
     * @param http
     * @return org.springframework.security.web.SecurityFilterChain
     * @author ren
     * @date 2025/04/17 21:30
     */
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http.authorizeHttpRequests(auth -> auth
                // 允许 OPTIONS 方法通过
                .requestMatchers(HttpMethod.OPTIONS, "/**").permitAll()
                // 静态资源，可匿名访问
                .requestMatchers(request -> {
                    String path = request.getServletPath();
                    return (request.getMethod().equals("GET") && ( "/".equals(path) || path.endsWith(".html") || path.endsWith(".css") || path.endsWith(".js")));
                }).permitAll()
                .requestMatchers("/swagger-ui/**", "/*/api-docs/**", "/swagger-resources/**", "/webjars/**", "/druid/**")
                .permitAll()
                // 除上面外的所有请求全部需要鉴权认证
                .anyRequest().authenticated()
        );
        return http.build();
    }
}
```

添加如上配置后，即可放开 SpringSecurity 的认证限制

## 总结

以上就是今天要讲的内容，本文简单介绍了 SpringDoc 整合在 SpringBoot 项目中的步骤，如果有遗漏，请大家留言，看到后会进行补充

[加入小哈的星球](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / Java 学习路线 / **社群讨论 / **学习打卡 / 每月赠书**

- 《仿小红书（微服务架构 ）》 已完结，基于 Spring Cloud Alibaba + Spring Boot 3.x + JDK 17..., [点击查看项目介绍](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247538491&idx=1&sn=576995017721766d0fe15723fd135619&chksm=fd5787bdca200eab54d2fb8ca07fcc2bffdec3eaab4ab82ab5eaf949f0254c1683455e02010b&token=343952052&lang=zh_CN&scene=21#wechat_redirect) ； 演示地址： http://116.62.199.48:7070/
- 《 Spring AI 应用（RAG 智能客服） 》已完结, 基于 Spring AI 2.x + Spring Boot 4.x + JDK 21
- 《 秒杀系统设计 》正在更新中，单体到微服务高并发架构演进

- 《 前后端分离博客项目（全栈开发） 》 已完结,演示链接： http://116.62.199.48/
- 项目阅读地址： https://quanxiaoha.com/column

截止目前，**累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

![图片](assets/2026-11-01%20-%20%E5%91%8A%E5%88%ABSwagger%20UI%EF%BC%81%E4%B8%80%E6%AC%BE%E6%9B%B4%E9%80%82%E5%90%88%20SpringBoot%20%E7%9A%84API%E6%96%87%E6%A1%A3%E6%96%B0%E9%80%89%E6%8B%A9/b01fd91d58faf9455f8fbb5c64bb22f0_MD5.webp)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~
2. 国内互联网公司舒适度排行榜，第一名实至名归！
3. 面试官：如果要存ip地址，用什么数据类型比较好?
4. 面试官：为什么 Kafka 没办法 100% 保证消息不丢失？
```

```

```

```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。
获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。
```

```
PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。
点“在看”支持小哈呀，谢谢啦
```

---
原文链接：https://mp.weixin.qq.com/s/1XO9l0eFULUQ3ZVU3v30Sg
