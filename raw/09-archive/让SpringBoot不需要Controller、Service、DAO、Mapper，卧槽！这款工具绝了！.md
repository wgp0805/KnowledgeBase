---
title: "让SpringBoot不需要Controller、Service、DAO、Mapper，卧槽！这款工具绝了！"
source: "https://mp.weixin.qq.com/s/5WM_gsNtjQfEZ8k1KcTVFg"
---
点击关注 👉 IT码徒 *2026年7月21日 21:11*

点击“IT码徒”，关注，置顶公众号

每日技术干货，第一时间送达！

## Dataway介绍

Dataway 是基于 DataQL 服务聚合能力，为应用提供的一个接口配置工具。使得使用者无需开发任何代码就配置一个满足需求的接口。整个接口配置、测试、冒烟、发布。一站式都通过 Dataway 提供的 UI 界面完成。UI 会以 Jar 包方式提供并集成到应用中并和应用共享同一个 http 端口，应用无需单独为 Dataway 开辟新的管理端口。

这种内嵌集成方式模式的优点是，可以使得大部分老项目都可以在无侵入的情况下直接应用 Dataway。进而改进老项目的迭代效率，大大减少企业项目研发成本。

Dataway 工具化的提供 DataQL 配置能力。这种研发模式的变革使得，相当多的需求开发场景只需要配置即可完成交付。从而避免了从数据存取到前端接口之间的一系列开发任务，例如：Mapper、BO、VO、DO、DAO、Service、Controller 统统不在需要。

Dataway 是 Hasor 生态中的一员，因此在 Spring 中使用 Dataway 首先要做的就是打通两个生态。根据官方文档中推荐的方式我们将 Hasor 和 Spring Boot 整合起来。这里是原文： [https://www.hasor.net/web/extends/spring/for\_boot.html](https://www.hasor.net/web/extends/spring/for_boot.html)

## 第一步：引入相关依赖

```
<dependency>
    
            net.hasor
          
    <artifactId>hasor-spring</artifactId>
    <version>4.1.3</version>
</dependency>
<dependency>
    
            net.hasor
          
    <artifactId>hasor-dataway</artifactId>
    <version>4.1.3-fix20200414</version><!-- 4.1.3 包存在UI资源缺失问题 -->
</dependency>
```

hasor-spring 负责 Spring 和 Hasor 框架之间的整合。 hasor-dataway 是工作在 Hasor 之上，利用 hasor-spring 我们就可以使用 dataway了。

## 第二步：配置 Dataway，并初始化数据表

dataway 会提供一个界面让我们配置接口，这一点类似 Swagger 只要jar包集成就可以实现接口配置。找到我们 springboot 项目的配置文件 **[application.properties](http://application.properties/)**

```
# 是否启用 Dataway 功能（必选：默认false）
HASOR_DATAQL_DATAWAY=true

# 是否开启 Dataway 后台管理界面（必选：默认false）
HASOR_DATAQL_DATAWAY_ADMIN=true

# dataway  API工作路径（可选，默认：/api/）
HASOR_DATAQL_DATAWAY_API_URL=/api/

# dataway-ui 的工作路径（可选，默认：/interface-ui/）
HASOR_DATAQL_DATAWAY_UI_URL=/interface-ui/

# SQL执行器方言设置（可选，建议设置）
HASOR_DATAQL_FX_PAGE_DIALECT=mysql
```

Dataway 一共涉及到 5个可以配置的配置项，但不是所有配置都是必须的。

其中 **HASOR\_DATAQL\_DATAWAY** 、 **HASOR\_DATAQL\_DATAWAY\_ADMIN** 两个配置是必须要打开的，默认情况下 Datawaty 是不启用的。

Dataway 需要两个数据表才能工作，下面是这两个数据表的简表语句。下面这个 SQL 可以在 dataway的依赖 jar 包中 “META-INF/hasor-framework/mysql” 目录下面找到，建表语句是用 mysql 语法写的。

```
CREATE TABLE \`interface_info\` (
    \`api_id\`          int(11)      NOT NULL AUTO_INCREMENT   COMMENT 'ID',
    \`api_method\`      varchar(12)  NOT NULL                  COMMENT 'HttpMethod：GET、PUT、POST',
    \`api_path\`        varchar(512) NOT NULL                  COMMENT '拦截路径',
    \`api_status\`      int(2)       NOT NULL                  COMMENT '状态：0草稿，1发布，2有变更，3禁用',
    \`api_comment\`     varchar(255)     NULL                  COMMENT '注释',
    \`api_type\`        varchar(24)  NOT NULL                  COMMENT '脚本类型：SQL、DataQL',
    \`api_script\`      mediumtext   NOT NULL                  COMMENT '查询脚本：xxxxxxx',
    \`api_schema\`      mediumtext       NULL                  COMMENT '接口的请求/响应数据结构',
    \`api_sample\`      mediumtext       NULL                  COMMENT '请求/响应/请求头样本数据',
    \`api_create_time\` datetime     DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    \`api_gmt_time\`    datetime     DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
    PRIMARY KEY (\`api_id\`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='Dataway 中的API';

CREATE TABLE \`interface_release\` (
    \`pub_id\`          int(11)      NOT NULL AUTO_INCREMENT   COMMENT 'Publish ID',
    \`pub_api_id\`      int(11)      NOT NULL                  COMMENT '所属API ID',
    \`pub_method\`      varchar(12)  NOT NULL                  COMMENT 'HttpMethod：GET、PUT、POST',
    \`pub_path\`        varchar(512) NOT NULL                  COMMENT '拦截路径',
    \`pub_status\`      int(2)       NOT NULL                  COMMENT '状态：0有效，1无效（可能被下线）',
    \`pub_type\`        varchar(24)  NOT NULL                  COMMENT '脚本类型：SQL、DataQL',
    \`pub_script\`      mediumtext   NOT NULL                  COMMENT '查询脚本：xxxxxxx',
    \`pub_script_ori\`  mediumtext   NOT NULL                  COMMENT '原始查询脚本，仅当类型为SQL时不同',
    \`pub_schema\`      mediumtext       NULL                  COMMENT '接口的请求/响应数据结构',
    \`pub_sample\`      mediumtext       NULL                  COMMENT '请求/响应/请求头样本数据',
    \`pub_release_time\`datetime     DEFAULT CURRENT_TIMESTAMP COMMENT '发布时间（下线不更新）',
    PRIMARY KEY (\`pub_id\`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8mb4 COMMENT='Dataway API 发布历史。';

create index idx_interface_release on interface_release (pub_api_id);
```

## 第三步：配置数据源

作为 Spring Boot 项目有着自己完善的数据库方面工具支持。我们这次采用 druid + mysql + spring-boot-starter-jdbc 的方式。

首先引入依赖

```
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.30</version>
</dependency>
<dependency>
    
            com.alibaba
          
    <artifactId>druid</artifactId>
    <version>1.1.21</version>
</dependency>
<dependency>
    
            org.springframework.boot
          
    <artifactId>spring-boot-starter-jdbc</artifactId>
</dependency>
<dependency>
    
            com.alibaba
          
    <artifactId>druid-spring-boot-starter</artifactId>
    <version>1.1.10</version>
</dependency>
```

然后增加数据源的配置

```
# db

            spring.datasource.url=jdbc:mysql://xxxxxxx:3306/example
          

            spring.datasource.username=xxxxx
          

            spring.datasource.password=xxxxx
          

            spring.datasource.driver-class-name=com.mysql.jdbc.Driver
          

            spring.datasource.type:com.alibaba.druid.pool.DruidDataSource
          
# druid

            spring.datasource.druid.initial-size=3
          

            spring.datasource.druid.min-idle=3
          

            spring.datasource.druid.max-active=10
          

            spring.datasource.druid.max-wait=60000
          

            spring.datasource.druid.stat-view-servlet.login-username=admin
          

            spring.datasource.druid.stat-view-servlet.login-password=admin
          

            spring.datasource.druid.filter.stat.log-slow-sql=
          true

            spring.datasource.druid.filter.stat.slow-sql-millis=1
```

如果项目已经集成了自己的数据源，那么可以忽略第三步。

## 第四步：把数据源设置到 Hasor 容器中

Spring Boot 和 Hasor 本是两个独立的容器框架，我们做整合之后为了使用 Dataway 的能力需要把 Spring 中的数据源设置到 Hasor 中。

首先新建一个 Hasor 的 模块，并且将其交给 Spring 管理。然后把数据源通过 Spring 注入进来。

```
@DimModule
@Component
public class ExampleModule implements SpringModule {
    @Autowired
    private DataSource dataSource = null;

    @Override
    public void loadModule(ApiBinder apiBinder) throws Throwable {
        // .DataSource form Spring boot into Hasor
        
            apiBinder.installModule(new
           JdbcModule(
            Level.Full,
           
            this.dataSource));
          
    }
}
```

Hasor 启动的时候会调用 loadModule 方法，在这里再把 DataSource 设置到 Hasor 中。

## 第五步：在SprintBoot 中启用 Hasor

```
@EnableHasor()
@EnableHasorWeb()
@SpringBootApplication(scanBasePackages = { "
            net.example.hasor"
           })
public class ExampleApplication {
    public static void main(String[] args) {
        
            SpringApplication.run(ExampleApplication.class,
           args);
    }
}
```

这一步非常简单，只需要在 Spring 启动类上增加两个注解即可。

## 第六步：启动应用

应用在启动过程中会看到 Hasor Boot 的欢迎信息

```
_    _                        ____              _
| |  | |                      |  _ \            | |
| |__| | __ _ ___  ___  _ __  | |_) | ___   ___ | |_
|  __  |/ _\` / __|/ _ \| '__| |  _ < / _ \ / _ \| __|
| |  | | (_| \__ \ (_) | |    | |_) | (_) | (_) | |_
|_|  |_|\__,_|___/\___/|_|    |____/ \___/ \___/ \__|
```

在后面的日志中还可以看到类似下面这些日志。

```
2020-04-14 13:52:59.696 [main] INFO  
            n.h.core.context.TemplateAppContext
           - loadModule class 
            net.hasor.dataway.config.DatawayModule
          
2020-04-14 13:52:59.697 [main] INFO  
            n.hasor.dataway.config.DatawayModule
           - dataway api workAt /api/
2020-04-14 13:52:59.697 [main] INFO  
            n.h.c.e.AbstractEnvironment
           - var -> HASOR_DATAQL_DATAWAY_API_URL = /api/.
2020-04-14 13:52:59.704 [main] INFO  
            n.hasor.dataway.config.DatawayModule
           - dataway admin workAt /interface-ui/
2020-04-14 13:52:59.716 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[901d38f22faa419a8593bb349905ed0e] -> bindType ‘class 
            net.hasor.dataway.web.ApiDetailController’
           mappingTo: ‘[/interface-ui/api/api-detail]’.
2020-04-14 13:52:59.716 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[c6eb9f3b3d4c4c8d8a4f807435538172] -> bindType ‘class 
            net.hasor.dataway.web.ApiHistoryListController’
           mappingTo: ‘[/interface-ui/api/api-history]’.
2020-04-14 13:52:59.717 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[eb841dc72ad54023957233ef602c4327] -> bindType ‘class 
            net.hasor.dataway.web.ApiInfoController’
           mappingTo: ‘[/interface-ui/api/api-info]’.
2020-04-14 13:52:59.717 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[96aebb46265245459ae21d558e530921] -> bindType ‘class 
            net.hasor.dataway.web.ApiListController’
           mappingTo: ‘[/interface-ui/api/api-list]’.
2020-04-14 13:52:59.718 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[7467c07f160244df8f228321f6262d3d] -> bindType ‘class 
            net.hasor.dataway.web.ApiHistoryGetController’
           mappingTo: ‘[/interface-ui/api/get-history]’.
2020-04-14 13:52:59.719 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[97d8da5363c741ba99d87c073a344412] -> bindType ‘class 
            net.hasor.dataway.web.DisableController’
           mappingTo: ‘[/interface-ui/api/disable]’.
2020-04-14 13:52:59.720 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[8ddc3316ef2642dfa4395ca8ac0fff04] -> bindType ‘class 
            net.hasor.dataway.web.SmokeController’
           mappingTo: ‘[/interface-ui/api/smoke]’.
2020-04-14 13:52:59.720 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[cc06c5fb343b471aacedc58fb2fe7bf8] -> bindType ‘class 
            net.hasor.dataway.web.SaveApiController’
           mappingTo: ‘[/interface-ui/api/save-api]’.
2020-04-14 13:52:59.720 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[7915b2b1f89a4e73891edab0264c9bd4] -> bindType ‘class 
            net.hasor.dataway.web.PublishController’
           mappingTo: ‘[/interface-ui/api/publish]’.
2020-04-14 13:52:59.721 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[0cfa34586455414591bdc389bff23ccb] -> bindType ‘class 
            net.hasor.dataway.web.PerformController’
           mappingTo: ‘[/interface-ui/api/perform]’.
2020-04-14 13:52:59.721 [main] INFO  
            net.hasor.core.binder.ApiBinderWrap
           - mapingTo[37fe4af3e2994acb8deb72d21f02217c] -> bindType ‘class 
            net.hasor.dataway.web.DeleteController’
           mappingTo: ‘[/interface-ui/api/delete]’.
```

当看到 “dataway api workAt **/api/** ” 、 dataway admin workAt **/interface-ui/** 信息时，就可以确定 Dataway 的配置已经生效了。

## 第七步：访问接口管理页面进行接口配置

在浏览器中输入 “http://127.0.0.1:8080/interface-ui/” 就可以看到期待已久的界面了。

![图片](assets/%E8%AE%A9SpringBoot%E4%B8%8D%E9%9C%80%E8%A6%81Controller%E3%80%81Service%E3%80%81DAO%E3%80%81Mapper%EF%BC%8C%E5%8D%A7%E6%A7%BD%EF%BC%81%E8%BF%99%E6%AC%BE%E5%B7%A5%E5%85%B7%E7%BB%9D%E4%BA%86%EF%BC%81/c6752c4bf9f950c0a50c96ae3d7c910b_MD5.png)

图片

## 第八步：新建一个接口

Dataway 提供了2中语言模式，我们可以使用强大的 DataQL 查询语言，也可以直接使用 SQL 语言（在 Dataway 内部 SQL 语言也会被转换为 DataQL 的形式执行。）

![图片](assets/%E8%AE%A9SpringBoot%E4%B8%8D%E9%9C%80%E8%A6%81Controller%E3%80%81Service%E3%80%81DAO%E3%80%81Mapper%EF%BC%8C%E5%8D%A7%E6%A7%BD%EF%BC%81%E8%BF%99%E6%AC%BE%E5%B7%A5%E5%85%B7%E7%BB%9D%E4%BA%86%EF%BC%81/243fbd6de7b1bb7c959aed3e299ae0f6_MD5.png)

图片

首先我们在 SQL 模式下尝试执行一条 select 查询，立刻就可以看到这条 SQL 的查询结果。

![图片](assets/%E8%AE%A9SpringBoot%E4%B8%8D%E9%9C%80%E8%A6%81Controller%E3%80%81Service%E3%80%81DAO%E3%80%81Mapper%EF%BC%8C%E5%8D%A7%E6%A7%BD%EF%BC%81%E8%BF%99%E6%AC%BE%E5%B7%A5%E5%85%B7%E7%BB%9D%E4%BA%86%EF%BC%81/cf5a07916a0c2c04d3671bc25da43b79_MD5.png)

图片

同样的方式我们使用 DataQL 的方式需要这样写：

```
var query = @@sql()<%
    select * from interface_info
%>
return query()
```

其中 var query = **@@sql()<%... %>** 是用来定义SQL外部代码块，并将这个定义存入 query 变量名中。<% %> 中间的就是 SQL 语句。

最后在 DataQL 中调用这个代码块，并返回查询结果。

当接口写好之后就可以保存发布了，为了测试方便，我选用 GET 方式。

![图片](assets/%E8%AE%A9SpringBoot%E4%B8%8D%E9%9C%80%E8%A6%81Controller%E3%80%81Service%E3%80%81DAO%E3%80%81Mapper%EF%BC%8C%E5%8D%A7%E6%A7%BD%EF%BC%81%E8%BF%99%E6%AC%BE%E5%B7%A5%E5%85%B7%E7%BB%9D%E4%BA%86%EF%BC%81/ce630fd3d173d0cd05353e2434268af6_MD5.png)

图片

接口发布之后我们直接请求：http://127.0.0.1:8080/api/demos，就看到期待已久的接口返回值了。

![图片](assets/%E8%AE%A9SpringBoot%E4%B8%8D%E9%9C%80%E8%A6%81Controller%E3%80%81Service%E3%80%81DAO%E3%80%81Mapper%EF%BC%8C%E5%8D%A7%E6%A7%BD%EF%BC%81%E8%BF%99%E6%AC%BE%E5%B7%A5%E5%85%B7%E7%BB%9D%E4%BA%86%EF%BC%81/cd095fa8448a13cc36a0be4f9c1d2b9a_MD5.png)

图片

## 最后总结

经过上面的几个步骤我们介绍了如何基于 Spring Boot 项目使用 Dataway 来简单的配置接口。Dataway 的方式确实给人耳目一新，一个接口竟然可以如此简单的配置出来无需开发任何一行代码，也不需要做任何 Mapping 实体映射绑定。

最后放几个有用的连接：

- Dataway 官方手册： [https://www.hasor.net/web/dataway/about.html](https://www.hasor.net/web/dataway/about.html)
- Dataway 在 OSC 上的项目地址，欢迎收藏： [https://www.oschina.net/p/dataway](https://www.oschina.net/p/dataway)
- DataQL 手册地址： [https://www.hasor.net/web/dataql/what\_is\_dataql.html](https://www.hasor.net/web/dataql/what_is_dataql.html)
- Hasor 项目的首页： [https://www.hasor.net/web/index.html](https://www.hasor.net/web/index.html)

来源： [my.oschina.net/ta8210/blog/3234639](http://my.oschina.net/ta8210/blog/3234639)

—END—

**PS：防止找不到本篇文章，可以收藏点赞，方便翻阅查找哦。**

往期推荐[面试官：一台服务器最大能支持多少条TCP连接？问倒一大片。。。](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514257&idx=1&sn=f42885564d7a7e65dca24dc64cd4907f&scene=21#wechat_redirect)[面试官：Git如何撤回已Push的代码？问倒一大片。。。](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514241&idx=2&sn=b73288775b62054ddacef3f1b51faf10&scene=21#wechat_redirect)[Maven 4 要来了：15 年后，Java 构建工具迎来“彻底重构”](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514225&idx=1&sn=9a34ac9d93915f291a3599bf366ac7a4&scene=21#wechat_redirect)[3个完美替代 Navicat 的工具，香~](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514220&idx=1&sn=727261054a6b407d6481f09539a4b605&scene=21#wechat_redirect)[还在使用WebSocket实现实时消息推送吗？](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514189&idx=1&sn=f059d19982d281b0ca50699d2b23501c&scene=21#wechat_redirect)[MyBatisPlus封神玩法：这12个骚操作让开发效率直接起飞！](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514189&idx=2&sn=2ab55b7fcde87b294b29779c27b78aa8&scene=21#wechat_redirect)

Springboot · 目录

阅读原文