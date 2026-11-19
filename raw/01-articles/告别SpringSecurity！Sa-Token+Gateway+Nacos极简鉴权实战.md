---
title: "告别SpringSecurity！Sa-Token+Gateway+Nacos极简鉴权实战"
source: "https://mp.weixin.qq.com/s/bvNufU2xz--TmboWIbxXxw"
author:
  - "[[点击关注 👉]]"
published:
created: 2026-11-19
description:
tags:
  - "clippings"
---
点击关注 👉 IT码徒 *2026年11月16日 23:25*

点击“IT码徒”，关注，置顶公众号

```
每日技术干货，第一时间送达！
```

之前进行鉴权、授权都要写一大堆代码。如果使用像 `Spring Security` 这样的框架，又要花好多时间学习，拿过来一用，好多配置项也不知道是干嘛用的，又不想了解。要是不用 `Spring Security` ，token的生成、校验、刷新，权限的验证分配，又全要自己写，想想都头大。

`Spring Security` 太重而且配置繁琐。自己实现所有的点必须又要顾及到，更是麻烦。

最近看到一个权限认证框架，真是够简单高效。这里分享一个使用 `Sa-Token` 的gateway鉴权demo。

![图片](assets/%E5%91%8A%E5%88%ABSpringSecurity%EF%BC%81Sa-Token+Gateway+Nacos%E6%9E%81%E7%AE%80%E9%89%B4%E6%9D%83%E5%AE%9E%E6%88%98/cbcaaf22f406380157c49da576b866f9_MD5.webp)

01

需求分析

结构

认证

sa-token模块

我们首先编写sa-token模块进行token生成和权限分配。

在 `sa-token` 的session模式下生成token非常方便，只需要调用

```
StpUtil.login(Object
id);
```

就可以为账号生成 Token 凭证与 Session 会话了。

配置信息

```
server:
  # 端口
port:8081

spring:
application:
    name:weishuang-account
datasource:
    driver-class-name:
            com.mysql.cj.jdbc.Driver
          
    url:jdbc:mysql://127.0.0.1:3306/weishuang_account?useUnicode=true&characterEncoding=utf8&autoReconnect=true&allowMultiQueries=true&useSSL=false&serverTimezone=Asia/Shanghai&zeroDateTimeBehavior=CONVERT_TO_NULL
    username:root
    password:root
# redis配置
redis:
    # Redis数据库索引（默认为0）
    database:0
    # Redis服务器地址
    host:127.0.0.1
    # Redis服务器连接端口
    port:6379
    # Redis服务器连接密码（默认为空）
    # password:
    # 连接超时时间
    timeout:10s
    lettuce:
      pool:
        # 连接池最大连接数
        max-active:200
        # 连接池最大阻塞等待时间（使用负值表示没有限制）
        max-wait:-1ms
        # 连接池中的最大空闲连接
        max-idle:10
        # 连接池中的最小空闲连接
        min-idle:0

############## Sa-Token 配置 (文档: 
            https://sa-token.cc)
           ##############
sa-token:
# token名称 (同时也是cookie名称)
token-name:weishuang-token
# token有效期，单位s 默认30天, -1代表永不过期
timeout:2592000
# token临时有效期 (指定时间内无操作就视为token过期) 单位: 秒
activity-timeout:-1
# 是否允许同一账号并发登录 (为true时允许一起登录, 为false时新登录挤掉旧登录)
is-concurrent:true
# 在多人登录同一账号时，是否共用一个token (为true时所有登录共用一个token, 为false时每次登录新建一个token)
is-share:true
# token风格
token-style:uuid
# 是否输出操作日志
is-log:false
# token前缀
token-prefix:Bearer
```

在 `sa-token` 的配置中，我使用了 `token-name` 来指定token的名称，如果不指定那么就是默认的satoken。

使用 `token-prefix` 来指定token的前缀，这样前端在header里传入token的时候就要加上Bearer了(注意有个空格)，建议和前端商量一下需不需要这个前缀，如果不使用，直接传token就好了。

现在调用接口时传入的格式就是

```
server:
  port:9000
spring:
application:
    name:weishuang-gateway
cloud:
    loadbalancer:
      ribbon:
        enabled:false
    nacos:
      discovery:
        username:nacos
        password:nacos
        server-addr:localhost:8848
    gateway:
      routes:
        -id:account
          uri:lb://weishuang-account
          order:1
          predicates:
            -Path=/account/**
# redis配置
redis:
    # Redis数据库索引（默认为0）
    database:0
    # Redis服务器地址
    host:127.0.0.1
    # Redis服务器连接端口
    port:6379
    # Redis服务器连接密码（默认为空）
    # password:
    # 连接超时时间
    timeout:10s
    lettuce:
      pool:
        # 连接池最大连接数
        max-active:200
        # 连接池最大阻塞等待时间（使用负值表示没有限制）
        max-wait:-1ms
        # 连接池中的最大空闲连接
        max-idle:10
        # 连接池中的最小空闲连接
        min-idle:0

############## Sa-Token 配置 (文档: 
            https://sa-token.cc)
           ##############
sa-token:
# token名称 (同时也是cookie名称)
token-name:weishuang-token
# token有效期，单位s 默认30天, -1代表永不过期
timeout:2592000
# token临时有效期 (指定时间内无操作就视为token过期) 单位: 秒
activity-timeout:-1
# 是否允许同一账号并发登录 (为true时允许一起登录, 为false时新登录挤掉旧登录)
is-concurrent:true
# 在多人登录同一账号时，是否共用一个token (为true时所有登录共用一个token, 为false时每次登录新建一个token)
is-share:true
# token风格
token-style:uuid
# 是否输出操作日志
is-log:false
# token前缀
token-prefix:Bearer
```

`sa-token`

现在调用接口时传入的格式就是

```
weishuang-token = Bearer token123456
```

`sa-token` 的session模式需要redis来存储session，在微服务中，各个服务的session也需要redis来同步。

当然 `sa-token` 也支持jwt来生成无状态的token，这样就不需要在服务中引入redis了。本文使用session模式（jwt的刷新token等机制还要自己实现，session的刷新 `sa-token` 都帮我们做好了，使用默认的模式更加方便，而且功能更多）

我们来编写一个登录接口

User

```
@Data
publicclassUser {

    /**
     * id
     */
    private String id;

    /**
     * 账号
     */
    private String userName;

    /**
     * 密码
     */
    private String password;

}
```

UserController

```
@RestController
@RequestMapping("/account/user/")
publicclassUserController {

    @Autowired
    private UserManager userManager;

    @PostMapping("doLogin")
    public SaResult doLogin(@RequestBody AccountUserLoginDTO req) {
        
            userManager.login(req);
          

        return 
            SaResult.ok(
          "登录成功");
    }
}
```

UserManager

```
@Component
publicclassUserManagerImplimplementsUserManager {

    @Autowired
    private UserService userService;

    @Override
    publicvoidlogin(AccountUserLoginDTO req) {
        //生成密码
        Stringpassword= 
            PasswordUtil.generatePassword(req.getPassword());
          
        //调用数据库校验是否存在用户
        Useruser= 
            userService.getOne(req.getUserName(),
           password);
        if (user == null) {
            thrownewRuntimeException("账号或密码错误");
        }
        
        //为账号生成Token凭证与Session会话
        
            StpUtil.login(user.getId());
          
        //为该用户的session存储更多信息
        //这里为了方便直接把user实体存进去了，也包括了密码，自己实现时不建议这样做。
        
            StpUtil.getSession().set(
          "USER_DATA", user);
    }

}
```

UserService

```
@Service
publicclassUserServiceImplextendsServiceImpl<UserMapper, User> implementsUserService {

    @Autowired
    private UserMapper userMapper;

    public User getOne(String username, String password){
        LambdaQueryWrapper<User> queryWrapper = newLambdaQueryWrapper<>();
        
            queryWrapper.eq(User::getUserName,username)
          
                .eq(User::getPassword,password);

        return 
            userMapper.selectOne(queryWrapper);
          
    }
}
```

gateway模块

依赖

```
<dependencies>
        <dependency>
            <groupId>
            org.springframework.cloud
          </groupId>
            <artifactId>spring-cloud-starter-openfeign</artifactId>
            <scope>provided</scope>
        </dependency>

        <dependency>
            <groupId>
            com.alibaba.cloud
          </groupId>
            <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
        </dependency>

        <dependency>
            <groupId>
            org.springframework.cloud
          </groupId>
            <artifactId>spring-cloud-starter-loadbalancer</artifactId>
        </dependency>

        <!-- 引入gateway网关 -->
        <dependency>
            <groupId>
            org.springframework.cloud
          </groupId>
            <artifactId>spring-cloud-starter-gateway</artifactId>
            <exclusions>
                <exclusion>
                    <groupId>
            org.springframework.boot
          </groupId>
                    <artifactId>spring-boot-starter-web</artifactId>
                </exclusion>
            </exclusions>
        </dependency>

        <dependency>
            <groupId>
            org.projectlombok
          </groupId>
            <artifactId>lombok</artifactId>
        </dependency>

        
        <dependency>
            <groupId>
            cn.dev33
          </groupId>
            <artifactId>sa-token-reactor-spring-boot-starter</artifactId>
            <version>1.34.0</version>
        </dependency>

        <!-- Sa-Token 整合 Redis （使用 jackson 序列化方式） -->
        <dependency>
            <groupId>
            cn.dev33
          </groupId>
            <artifactId>sa-token-dao-redis-jackson</artifactId>
            <version>1.34.0</version>
        </dependency>
        <dependency>
            <groupId>
            org.apache.commons
          </groupId>
            <artifactId>commons-pool2</artifactId>
        </dependency>

    </dependencies>
```

配置

gateway我们也注册到nacos中。

拦截认证

```
package 
            com.weishuang.gateway.gateway.config;
          

import 
            cn.dev33.satoken.reactor.filter.SaReactorFilter;
          
import 
            cn.dev33.satoken.router.SaRouter;
          
import 
            cn.dev33.satoken.stp.StpUtil;
          
import 
            cn.dev33.satoken.util.SaResult;
          
import 
            org.springframework.beans.factory.ObjectProvider;
          
import 
            org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
          
import 
            org.springframework.boot.autoconfigure.http.HttpMessageConverters;
          
import 
            org.springframework.context.annotation.Bean;
          
import 
            org.springframework.context.annotation.Configuration;
          
import 
            org.springframework.http.converter.HttpMessageConverter;
          

import 
            java.util.ArrayList;
          
import 
            java.util.List;
          
import 
            java.util.stream.Collectors;
          

@Configuration
publicclassSaTokenConfigure {

    // 注册 Sa-Token全局过滤器
    @Bean
    public SaReactorFilter getSaReactorFilter() {
        returnnewSaReactorFilter()
                // 拦截地址
                .addInclude("/**")    /* 拦截全部path */
                // 开放地址
                .addExclude("/
            favicon.ico"
          )
                // 鉴权方法：每次访问进入
                .setAuth(obj -> {
                    // 登录校验 -- 拦截所有路由，并排除/account/user/doLogin用于开放登录
                    
            SaRouter.match(
          "/**", "/account/user/doLogin", r -> 
            StpUtil.checkLogin());
          

//                    // 权限认证 -- 不同模块, 校验不同权限
//                    
            SaRouter.match("/account/**",
           r -> 
            StpUtil.checkRole("user"));
          
//                    
            SaRouter.match("/admin/**",
           r -> 
            StpUtil.checkRole("admin"));
          
//                    
            SaRouter.match("/goods/**",
           r -> 
            StpUtil.checkPermission("goods"));
          
//                    
            SaRouter.match("/orders/**",
           r -> 
            StpUtil.checkPermission("orders"));
          

                    // 更多匹配 ...  */
                })
                // 异常处理方法：每次setAuth函数出现异常时进入
                .setError(e -> {
                    return 
            SaResult.error(e.getMessage());
          
                })
                ;
    }
}
```

只需要在gateway中添加一个全局过滤器进行鉴权操作就可以实现认证/鉴权操作了。

这里我们对 `**` 全部路径进行拦截，但不要忘记把我们的登录接口释放出来，允许访问。

到这里简单的认证操作就实现了。我们仅仅使用了sa-token的一个 `             StpUtil.login(Object            id)` 方法，其他事情sa-token都帮我们完成了，更无需复杂的配置和多到爆炸的Bean。

鉴权

有时候一个token认证并不能让我们区分用户能不能访问这个资源，使用那个菜单，我们需要更细粒度的鉴权。

在经典的RBAC模型里，用户会拥有多个角色，不同的角色又会有不同的权限。

这里我们使用五个表来表示用户、角色、权限之间的关系。

很显然，我们想判断用户有没有权限访问一个path，需要判断用户是否还有该权限。

在sa-token中想要实现这个功能，只需要实现 `StpInterface` 接口即可。

```
/**
 * 自定义权限验证接口扩展 
 */
@Component   
publicclassStpInterfaceImplimplementsStpInterface {

    @Override
    public List<String> getPermissionList(Object loginId, String loginType) {
        // 返回此 loginId 拥有的权限列表 
        return ...;
    }

    @Override
    public List<String> getRoleList(Object loginId, String loginType) {
        // 返回此 loginId 拥有的角色列表
        return ...;
    }

}
```

我们在gateway实现这个接口，为用户赋予权限，再进行权限校验，就可以精确到path了。

我们使用先从Redis中获取缓存数据，获取不到时走RPC调用account服务获取。

为了更方便的使用gateway调用account服务，我们使用nacos进行服务发现，用feign调用。

在account和gateway服务中配置nacos

配置nacos

在两个服务中加入nacos的配置

```
spring:
  cloud:
    nacos:
      discovery:
        username:nacos
        password:nacos
        server-addr:localhost:8848
datasource:
    driver-class-name:
            com.mysql.cj.jdbc.Driver
          
    url:jdbc:mysql://127.0.0.1:3306/weishuang_account?useUnicode=true&characterEncoding=utf8&autoReconnect=true&allowMultiQueries=true&useSSL=false&serverTimezone=Asia/Shanghai&zeroDateTimeBehavior=CONVERT_TO_NULL
    username:root
    password:root
```

```
<dependency>
    <groupId>
            com.alibaba.cloud
          </groupId>
    <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId>
</dependency>
```

配置gateway

需要注意的是，gateway是基于WebFlux的一个响应式组件， `HttpMessageConverters` 不会像Spring Mvc一样自动注入，需要我们手动配置。

```
package 
            com.weishuang.gateway.gateway.config;
          

import 
            org.springframework.beans.factory.ObjectProvider;
          
import 
            org.springframework.boot.autoconfigure.condition.ConditionalOnMissingBean;
          
import 
            org.springframework.boot.autoconfigure.http.HttpMessageConverters;
          
import 
            org.springframework.context.annotation.Bean;
          
import 
            org.springframework.context.annotation.Configuration;
          
import 
            org.springframework.http.converter.HttpMessageConverter;
          

import 
            java.util.stream.Collectors;
          

@Configuration
publicclassHttpMessageConvertersConfigure {
    @Bean
    @ConditionalOnMissingBean
    public HttpMessageConverters messageConverters(ObjectProvider<HttpMessageConverter<?>> converters) {
        returnnewHttpMessageConverters(
            converters.orderedStream().collect(Collectors.toList()));
          
    }
}
```

实现获取角色、权限接口

在account中实现通过用户获取角色、获取权限的接口

RoleController、PermissionController

```
@RestController
@RequestMapping("/account/role/")
publicclassRoleController {

    @Autowired
    private RoleManager roleManager;

    @PostMapping("/getRoles")
    public List<RoleDTO> getRoles(@RequestParam String userId) {
        return 
            roleManager.getRoles(userId);
          
    }
}

@RestController
@RequestMapping("/account/permission/")
publicclassPermissionController {

    @Autowired
    private PermissionManager permissionManager;

    @PostMapping("/getPermissions")
    public List<PermissionDTO> getPermissions(@RequestParam String userId) {
        return 
            permissionManager.getPermissions(userId);
          
    }

}
```

RoleManager

```
@Component
publicclassRoleManagerImplimplementsRoleManager {

    @Autowired
    private RoleService roleService;

    @Autowired
    private UserRoleService userRoleService;

    @Autowired
    private Role2RoleDTOCovert role2RoleDTOCovert;

    @Override
    public List<RoleDTO> getRoles(String userId) {
        List userRoles = 
            userRoleService.getByUserId(userId);
          
        Set roleIds = 
            userRoles.stream().map(UserRole::getRoleId).collect(Collectors.toSet());
          
        List roleDTOS = 
            role2RoleDTOCovert.covertTargetList2SourceList(roleService.getByIds(roleIds));
          

        //服务不对外暴露，网关不传token到子服务，这里通过userId获取session，并设置角色。
        StringtokenValue= 
            StpUtil.getTokenValueByLoginId(userId);
          
        
        //为这个token在redis中设置角色，使网关获取更方便
        if(
            StringUtils.isNotEmpty(tokenValue)){
          
            if(
            CollectionUtils.isEmpty(roleDTOS)){
          
                
            StpUtil.getTokenSessionByToken(tokenValue).set(
          "ROLES", "");
            }else{
                List roleNames = 
            roleDTOS.stream().map(RoleDTO::getRoleName).collect(Collectors.toList());
          
                
            StpUtil.getTokenSessionByToken(tokenValue).set(
          "ROLES", 
            ListUtil.list2String(roleNames));
          
            }
        }
        return roleDTOS;
    }
}
```

PermissionManager

```
@Component
publicclassPermissionManagerImplimplementsPermissionManager {

    @Autowired
    private PermissionService permissionService;

    @Autowired
    private RolePermService rolePermService;

    @Autowired
    private UserRoleService userRoleService;

    @Autowired
    private Permission2PermissionDTOCovert permissionDTOCovert;

    @Override
    public List<PermissionDTO> getPermissions(String userId) {

        //获取用户的角色
        List roles = 
            userRoleService.getByUserId(userId);
          
        if (
            CollectionUtils.isEmpty(roles))
           {
            handleUserPermSession(userId, null);
        }

        Set roleIds = 
            roles.stream().map(UserRole::getRoleId).collect(Collectors.toSet());
          

        List rolePerms = 
            rolePermService.getByRoleIds(roleIds);
          

        if (
            CollectionUtils.isEmpty(rolePerms))
           {
            handleUserPermSession(userId, null);
        }

        Set permIds = 
            rolePerms.stream().map(RolePerm::getPermId).collect(Collectors.toSet());
          
        List perms = 
            permissionDTOCovert.covertTargetList2SourceList(permissionService.getByIds(permIds));
          

        handleUserPermSession(userId, perms);
        return perms;
    }

    privatevoidhandleUserPermSession(String userId, List<PermissionDTO> perms) {
        //通过userId获取session，并设置权限
        StringtokenValue= 
            StpUtil.getTokenValueByLoginId(userId);
          

        if (
            StringUtils.isNotEmpty(tokenValue))
           {
            //为了防止没有权限的用户多次进入到该接口，没权限的用户在redis中存入空字符串
            if (
            CollectionUtils.isEmpty(perms))
           {
                
            StpUtil.getTokenSessionByToken(tokenValue).set(
          "PERMS", "");
            } else {
                List paths = 
            perms.stream().map(PermissionDTO::getPath).collect(Collectors.toList());
          
                
            StpUtil.getTokenSessionByToken(tokenValue).set(
          "PERMS", 
            ListUtil.list2String(paths));
          
            }
        }
    }
}
```

gateway获取角色、权限

方式一：

官方写的实现StpInterfaceImpl中的方法

作为一个异步组件，gateway中不允许使用引起阻塞的同步调用，若使用feign进行调用就会发生错误，我们使用 `CompletableFuture` 来将同步调用转换成异步操作，但使用 `CompletableFuture` 我们需要指定线程池，否则将会使用默认的 `ForkJoinPool`

```
@Component
publicclassStpInterfaceImplimplementsStpInterface {

    @Autowired
    private RoleFacade roleFacade;

    @Autowired
    private PermissionFacade permissionFacade;

    @Autowired
    private ThreadPollConfig threadPollConfig;

    @Override
    public List<String> getPermissionList(Object loginId, String loginType) {
        Objectres= 
            StpUtil.getTokenSession().get(
          "PERMS");
        if (res == null) {
            CompletableFuture> permFuture = 
            CompletableFuture.supplyAsync(()
           -> {
                // 返回此 loginId 拥有的权限列表
                List permissions = 
            permissionFacade.getPermissions((String)
           loginId);

                return 
            permissions.stream().map(PermissionDTO::getPath).collect(Collectors.toList());
          
            }, 
            threadPollConfig.USER_ROLE_PERM_THREAD_POOL);
          
            try {
                return 
            permFuture.get();
          
            } catch (InterruptedException | ExecutionException e) {
                thrownewRuntimeException(e);
            }
        }
        Stringpaths= (String) res;
        
            System.out.println(paths);
          
        return 
            ListUtil.string2List(paths);
          
    }

    @Override
    public List<String> getRoleList(Object loginId, String loginType) {
        Objectres= 
            StpUtil.getTokenSession().get(
          "ROLES");
        if (res == null) {
            CompletableFuture> roleFuture = 
            CompletableFuture.supplyAsync(()
           -> {
                // 返回此 loginId 拥有的权限列表
                List roles = 
            roleFacade.getRoles((String)
           loginId);

                return 
            roles.stream().map(RoleDTO::getRoleName).collect(Collectors.toList());
          
            }, 
            threadPollConfig.USER_ROLE_PERM_THREAD_POOL);
          
            try {
                return 
            roleFuture.get();
          
            } catch (InterruptedException | ExecutionException e) {
                thrownewRuntimeException(e);
            }
        }
        StringroleNames= (String) res;
        
            System.out.println(roleNames);
          
        return 
            ListUtil.string2List(roleNames);
          
    }

}
```

这里我们创建一个线程池，用于权限获取使用

```
package 
            com.weishuang.gateway.gateway.config;
          

import 
            org.springframework.context.annotation.Configuration;
          

import 
            java.util.concurrent.*;
          
import 
            java.util.concurrent.atomic.AtomicInteger;
          

@Configuration
publicclassThreadPollConfig {

    privatefinal BlockingQueue<Runnable> asyncSenderThreadPoolQueue = newLinkedBlockingQueue<Runnable>(50000);

    publicfinalExecutorServiceUSER_ROLE_PERM_THREAD_POOL=newThreadPoolExecutor(
            
            Runtime.getRuntime().availableProcessors(),
          
            
            Runtime.getRuntime().availableProcessors(),
          
            1000 * 60,
            
            TimeUnit.MILLISECONDS,
          
            this.asyncSenderThreadPoolQueue,
            newThreadFactory() {
                privatefinalAtomicIntegerthreadIndex=newAtomicInteger(0);

                @Override
                public Thread newThread(Runnable r) {
                    returnnewThread(r, "RolePermExecutor_" + this.
            threadIndex.incrementAndGet());
          
                }
            });

}
```

StpInterfaceImpl

gateway配置过滤器，实现鉴权

```
@Component
publicclassForwardAuthFilterimplementsWebFilter {
    static Set<String> whitePaths = newHashSet<>();

    static {
        
            whitePaths.add(
          "/account/user/doLogin");
        
            whitePaths.add(
          "/account/user/logout");
        
            whitePaths.add(
          "/account/user/register");
    }

    @Override
    public Mono<Void> filter(ServerWebExchange serverWebExchange, WebFilterChain webFilterChain) {

        ServerHttpRequestserverHttpRequest= 
            serverWebExchange.getRequest();
          

        Stringpath= 
            serverHttpRequest.getPath().toString();
          

        //需要校验权限
        if(!
            whitePaths.contains(path)){
          

            //判断用户是否有该权限
            if(!
            StpUtil.hasPermission(path)){
          
                thrownewNotPermissionException(path);
            }
        }

        return 
            webFilterChain.filter(serverWebExchange);
          
    }
}
```

方式二：

如果您觉得一定要使用响应式才行，那么无需实现 `StpInterfaceImpl`

```
/**
 * 全局过滤器
 */
@Component
publicclassForwardAuthFilterimplementsWebFilter {

    @Autowired
    private 
            WebClient.Builder
           webClientBuilder;

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, WebFilterChain chain) {
        ServerHttpRequestserverHttpRequest= 
            exchange.getRequest();
          
        Stringpath= 
            serverHttpRequest.getPath().toString();
          

        // /api开头的都要鉴权
        if (
            StringUtils.isNotEmpty(path)
           && 
            path.startsWith(
          "/api")) {
            Mono<List<String>> permissionList = getPermissionList();

            return 
            permissionList.flatMap(list
           -> {
                if (!
            StpUtil.stpLogic.hasElement(list,
           path)) {
                    return 
            Mono.error(
          newNotPermissionException(path));
                }
                return 
            chain.filter(exchange);
          
            });
        }
        return 
            chain.filter(exchange);
          
    }

    @Bean
    @LoadBalanced
    public 
            WebClient.Builder
           loadBalancedWebClientBuilder() {
        return 
            WebClient.builder();
          
    }

    private Mono<List<String>> getPermissionList() {
        StringuserId= (String) 
            StpUtil.getLoginId();
          

        Mono> listMono = 
            webClientBuilder.build()
          
                .post()
                .uri("http://weishuang-account/account/permission/getPermissions")
                .contentType(
            MediaType.APPLICATION_FORM_URLENCODED)
          
                .body(
            BodyInserters.fromFormData(
          "userId", userId))
                .retrieve()
                .bodyToFlux(
            PermissionDTO.class)
          
                .collectList();

        return 
            listMono.map(permissions
           -> 
            permissions.stream().map(PermissionDTO::getPath).collect(Collectors.toList()));
          
    }

}
```

修改sa-token的配置

```
@Configuration
publicclassSaTokenConfigure {

    // 注册 Sa-Token全局过滤器
    @Bean
    public SaReactorFilter getSaReactorFilter() {
        returnnewSaReactorFilter()
                // 拦截地址
                .addInclude("/**")    /* 拦截全部path */
                // 开放地址
                .addExclude("/
            favicon.ico"
          )
                // 鉴权方法：每次访问进入
                .setAuth(obj -> {
                    // 登录校验 -- 拦截所有路由，排除白名单
                    
            SaRouter.match(
          "/**")
                            .notMatch(newArrayList<>(
            WhitePath.whitePaths))
          
                            .check(r -> 
            StpUtil.checkLogin());
          
                })
                // 异常处理方法：每次setAuth函数出现异常时进入
                .setError(e -> {
                    return 
            SaResult.error(e.getMessage());
          
                });
    }
}
```

白名单

```
publicclassWhitePath {

    static Set<String> whitePaths = newHashSet<>();

    static {
        
            whitePaths.add(
          "/account/user/doLogin");
        
            whitePaths.add(
          "/account/user/logout");
        
            whitePaths.add(
          "/account/user/register");
    }
}
```

来源： [juejin.cn/post/7217360688263200825](http://juejin.cn/post/7217360688263200825)

—END—

**PS：防止找不到本篇文章，可以收藏点赞，方便翻阅查找哦。**

往期推荐[Java+iTextPDF，实时生成与预览PDF文件的最佳实践！](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514945&idx=1&sn=e7a2db7aec13074fe31de9bb8e3519f9&scene=21#wechat_redirect)[开源项目｜鹅厂开源的智能运维平台，非常强大！](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514945&idx=2&sn=5bd67407eb4179bf36cb73ff67bc294d&scene=21#wechat_redirect)[一个注解完美实现分布式锁](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514930&idx=2&sn=cbfd7b61668b9489870bf5357b390c39&scene=21#wechat_redirect)[开源项目｜100k+Star！GitHub爆火的多智能体神器，一条命令搭起AI一人公司](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514918&idx=1&sn=c67467ac5685731f0cbf01ac5d967763&scene=21#wechat_redirect)[网易二面：CPU狂飙900%，该怎么处理？](https://mp.weixin.qq.com/s?__biz=MzI3MDM0MzAyMg==&mid=2247514918&idx=2&sn=afa4c8d158eb916158ada7d62e97b690&scene=21#wechat_redirect)

java · 目录

阅读原文