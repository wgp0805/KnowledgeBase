---
title: SpringBoot整合SpringSecurity及框架的简单使用
tags:
  - SpringSecurity
categories:
  - SpringSecurity
date: 2023-06-20 09:41:20
---

之前本来想自己写一个security的博客了，但是这个框架一直也没用过，配置这块网上也是千奇百怪，本来用了个最新版，但是写法上变化太多，所以这里转载一个放在这里，然后在文章里进行补充，转载自：https://www.jianshu.com/p/5f78a11259cb

#### 1、Spring Security介绍

> **Spring security**，是一个强大的和高度可定制的身份验证和访问控制框架。它是确保基于Spring的应用程序的标准             ——来自官方参考手册

**Spring security** 和 **shiro** 一样，具有认证、授权、加密等用于权限管理的功能。和 **shiro** 不同的是，**Spring security**拥有比**shiro**更丰富的功能，并且，对于**Springboot**而言，**Spring Security**比**Shiro**更合适一些，因为都是**Spring**家族成员。今天，我们来为**SpringBoot**项目集成**Spring Security**。

本文所使用的版本：

​       **SpringBoot ： 2.2.6.RELEASE**
 ​       **Spring Security ： 5.2.2.RELEASE**

#### 2、配置Spring Security

在**SpringBoot**中集成**Spring Security**很简单，只需要在pom.xml中添加下面代码就行：



```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-security</artifactId>
</dependency>
```

这里可以不指定**Spring Security**的版本号，它会根据**SpringBoot**的版本来匹配对应的版本，**SpringBoot**版本是 **2.2.6.RELEASE**，对应**Spring Security**的版本是**5.2.2.RELEASE**。

然后，我们就可以将springboot启动了。

当我们尝试访问项目时，它会跳转到这个界面来：

![image-20230620140713667](image-20230620140713667.png)

   对！在此之前，你什么也不用做。这就是**Spring Security**的优雅之处。你只需要引入**Spring Security**的包，它就能在你的项目中工作。因为它已经帮你实现了一个简单的登陆界面。根据官方介绍，登录使用的账号是user，密码是随机密码，这个随机密码可以在控制台中找到，类似这样的一句话：

```tex
    Using generated security password: 1cb77bc5-8d74-4846-9b6c-4813389ce096
```

   Using generated security password后面的的就是系统给的随机密码，我们可以使用这个密码进行登录。随机密码在每一次启动服务后生成（如果你配置了热部署**devtools**，你得随时留意控制台了，因为每当你修改了代码，系统会自动重启，那时随机密码就会重新生成）。

   当然，这样的功能一定不是你想要的，也一定不会就这样拿给你的用户使用。那么，接下来，让我们把它配置成我们想要的样子。

   要实现自定义配置，首先要创建一个继承于**WebSecurityConfigurerAdapter**的配置类：

```java
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

}
```

   这里使用了**@EnableWebSecurity**注解，这个注解是**Spring Security**用于启用web安全的注解。具体实现，这里就不深入了。

   要实现自定义拦截配置，首先得告诉Spring Security，用户信息从哪里获取，以及用户对应的角色等信息。这里就需要重写**WebSecurityConfigurerAdapter**的**configure(AuthenticationManagerBuilder auth)**方法了。这个方法将指使**Spring Security**去找到用户列表，然后再与想要通过拦截器的用户进行比对，再进行下面的步骤。

   **Spring Security**的用户存储配置有多个方案可以选择，包括：

- **内存用户存储**
- **数据库用户存储**
- **LDAP用户存储**
- **自定义用户存储**

   我们分别来看看这几种用户存储的配置方法：

##### 1.内存用户存储

   此配置方式是直接将用户信息存储在内存中，这种方式在速度上无疑是最快的。但只适用于有限个用户数量，且这些用户几乎不会发生改变。我们来看看配置方法：

```java
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.inMemoryAuthentication().passwordEncoder(passwordEncoder())
            .withUser("zhangsan").password(passwordEncoder().encode("123456")).authorities("ADMIN")
            .and()
            .withUser("lisi").password(passwordEncoder().encode("123456")).authorities("ORDINARY");
    }
    
    private PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
```

   可以看到，**AuthenticationManagerBuilder**使用构造者方式来构建的。在上面方法中，先调用了**inMemoryAuthentication()**方法，它来指定用户存储在内存中。接下来又调用了passwordEncoder()方法，这个方法的作用是告诉**Spring Security**认证密码的加密方式。因为在**Spring security5**过后，必须指定某种加密方式，不然程序会报错。接下来调用的**withUser()、password()、authorities()**方法，分别是在指定用户的账号、密码以及权限名。在添加完一个用户后，要使用and()方法来连接下一个用户的添加。

   如果使用这种配置方法，你会发现，在修改用户时，就必须修改代码。对于绝大多数项目来说，这种方式是满足不了需求的，至少我们需要一个注册功能。

##### 2.数据库用户存储

   将用户信息存储在数据库中，让我们可以很方便地对用户信息进行增删改查。并且还可以为用户添加除认证信息外的附加信息，这样的设计也是我们很多小心应用所采取的方式。让我们来实现以下：

```java
    @Autowired
    private DataSource dataSource;
    
    
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.jdbcAuthentication().dataSource(dataSource).passwordEncoder(passwordEncoder())
            .usersByUsernameQuery(
                    "select username, password, status from Users where username = ?")
            .authoritiesByUsernameQuery(
                    "select username, authority from Authority where username = ?");
        
    }
    
    private PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
```

   调用**jdbcAuthentication()**来告诉Spring Security使用jdbc的方式来查询用户和权限，**dataSource()**方法指定数据库连接信息，**passwordEncoder()**指定密码加密规则，用户的密码数据应该以同样的方式进行加密存储，不然，两个加密方式不同的密码，匹配补上。**usersByUsernameQuery()**和**authoritiesByUsernameQuery()**方法分别定义了查询用户和权限信息的sql语句。其实，**Spring security**为我们默认了查询用户、权限甚至还有群组用户授权的sql，这三条默认的sql存放在**org.springframework.security.core.userdetails.jdbc.JdbcDaoImpl**中，有兴趣的小伙伴可以点进去看看。如果你要使用默认的，那你的表中关键性的字段必须和语句中的一致。

   使用数据库来存储用户和权限等信息已经可以满足大部分的需求。但是**Spring security**还为我们提供了另外一种配置方式，让我们来看一下。

##### 3.LDAP用户存储

   **LDAP**：轻型目录访问协议，是一个开放的，中立的，工业标准的应用协议，通过IP协议提供访问控制和维护分布式信息的目录信息。简单来说，就是将用户信息存放在另外一台服务器中（当然，也可以在同一台服务器，但我们一般不这么做），通过网络来进行访问的技术。

   我们来简单配置一下：

```java
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        LdapAuthenticationProviderConfigurer<AuthenticationManagerBuilder> configurer =                     auth.ldapAuthentication()
            .userSearchBase("ou=people")
            .userSearchFilter("(uid={0})")
            .groupSearchBase("ou=groups")
            .groupSearchFilter("member={0}");
            
        configurer.passwordCompare()
            .passwordEncoder(passwordEncoder())
            .passwordAttribute("passcode");
        configurer.contextSource().url("ldap://xxxxx.com:33389/dc=xxxxxx,dc=com");
    }
    
    private PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
```

   **userSearchFilter()**和**groupSearchFilter()**设置的是用户和群组的过滤条件，而**userSearchBase()**和**groupSearchBase()**设置了搜索起始位置，**contextSource().url()**设置**LDAP**服务器的地址。如果没有远程的服务器可以使用**contextSource().root()**来使用嵌入式**LDAP**服务器，此方式将使用项目中的用户数据文件来提供认证服务。

   如果以上几种方式还不能满足我们的需求，我们可以用自定义的方式来配置。

##### 4.自定义用户存储

   自定义用户存储，就是自行使用认证名称来查找对应的用户数据，然后交给Spring Security使用。我们需要定义一个实现**UserDetailsService**的**service**类：

```java
@Service
public class MyUserDetailsService implements UserDetailsService{

    @Autowired
    private UserMapper userMapper;
    
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userMapper.getUserByUsername(username);
        return user == null ? new User() : user;
    }
}

public class User implements UserDetails {
    ...
}
```

   该类只需要实现一个方法：**loadUserByUsername()**。该方法需要做的是使用传过来的**username**来匹配一个带有密码等信息的用户实体。需要注意的是这里的User类需要实现UserDetails，也就是说，查到的信息里，必须得有**Spring** **Security**所需要的信息。

   下面，让我们来继续配置：

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Autowired
    private MyUserDetailsService userDetailsService;
    
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
        auth.userDetailsService(userDetailsService)
            .passwordEncoder(passwordEncoder());
    }
    
    @Bean
    private PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

   这样的配置方法就很简单了，只需要告诉**Spring Security**你的**UserDetailsService**实现类是哪个就可以了，它会去调用**loadUserByUsername()**来查找用户。

   以上就是**Spring Security**所提供的4种用户存储方式，接下来，需要考虑的是，怎么拦截请求。

#### 3、请求拦截

##### 1.安全规则

   **Spring Security**的请求拦截配置方法是用户存储配置方法的重载方法，我们先来简单配置一下：



```java
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/user", "/menu")
            .hasRole("ADMIN")
            .antMatchers("/", "/**").permitAll();
    }
}
```

   调用**authorizeRequests()**方法后，就可以添加自定义拦截路径了。**antMatchers()**方法配置了请求路径，**hasRole()**和**permitAll()**指定了访问规则，分别表示拥有“**ADMIN**”权限的用户才能访问、所有用户可以访问。

   需要注意的是：这里的配置需要成对出现，并且配置的顺序也很重要。声明在前面的规则拥有更高的优先级。也就是说，如果我们将**.antMatchers("/", "/**").permitAll()**放到了最前面，像这样：

```java
@Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/", "/**").permitAll()
             .antMatchers("/user", "/menu")
            .hasRole("ADMIN");
    }
```

   那么，下面的"/**user**"和 "/**menu**"的配置是徒劳，因为前面的规则已经指明所有路径能被所有人访问。当然权限的规则方法还有很多，我这里只列举了两个。以下为常见的内置表达式：

| 表达                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| hasRole(String role)                                         | 返回`true`当前委托人是否具有指定角色。例如， `hasRole('admin')`默认情况下，如果提供的角色不是以“ ROLE_”开头，则会添加该角色。可以通过修改`defaultRolePrefix`on来自定义`DefaultWebSecurityExpressionHandler`。 |
| `hasAnyRole(String… roles)`                                  | 返回`true`当前委托人是否具有提供的任何角色（以逗号分隔的字符串列表形式）。例如， `hasAnyRole('admin', 'user')`默认情况下，如果提供的角色不是以“ ROLE_”开头，则会添加该角色。可以通过修改`defaultRolePrefix`on来自定义`DefaultWebSecurityExpressionHandler`。 |
| `hasAuthority(String authority)`                             | 返回`true`当前委托人是否具有指定权限。例如， `hasAuthority('read')` |
| `hasAnyAuthority(String… authorities)`                       | 返回`true`如果当前主体具有任何所提供的当局的（给定为逗号分隔的字符串列表）例如， `hasAnyAuthority('read', 'write')` |
| `principal`                                                  | 允许直接访问代表当前用户的主体对象                           |
| `authentication`                                             | 允许直接访问`Authentication`从`SecurityContext`              |
| `permitAll`                                                  | 始终评估为 `true`                                            |
| `denyAll`                                                    | 始终评估为 `false`                                           |
| `isAnonymous()`                                              | 返回`true`当前委托人是否为匿名用户                           |
| `isRememberMe()`                                             | 返回`true`当前主体是否是“记住我”的用户                       |
| `isAuthenticated()`                                          | `true`如果用户不是匿名的，则返回                             |
| `isFullyAuthenticated()`                                     | 返回`true`如果用户不是匿名或记得，我的用户                   |
| `hasPermission(Object target, Object permission)`            | 返回`true`用户是否可以访问给定权限的给定目标。例如，`hasPermission(domainObject, 'read')` |
| `hasPermission(Object targetId, String targetType, Object permission)` | 返回`true`用户是否可以访问给定权限的给定目标。例如，`hasPermission(1, 'com.example.domain.Message', 'read')` |

除此之外，还有一个支持SpEL表达式计算的方法，它的使用方法如下：

```java
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/user", "/menu")
            .access("hasRole('ADMIN')")
            .antMatchers("/", "/**").permitAll();
    }
```

   它所实现的规则和上面的方法一样。**Spring Security**还提供了其他丰富的SpEL表达式，如：

| 表达                                                         | 描述                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **`hasRole(String role)`**                                   | **返回`true`当前委托人是否具有指定角色。例如， `hasRole('admin')`默认情况下，如果提供的角色不是以“ ROLE_”开头，则会添加该角色。可以通过修改`defaultRolePrefix`on来自定义`DefaultWebSecurityExpressionHandler`。** |
| **`hasAnyRole(String… roles)`**                              | **返回`true`当前委托人是否具有提供的任何角色（以逗号分隔的字符串列表形式）。例如， `hasAnyRole('admin', 'user')`默认情况下，如果提供的角色不是以“ ROLE_”开头，则会添加该角色。可以通过修改`defaultRolePrefix`on来自定义`DefaultWebSecurityExpressionHandler`。** |
| **`hasAuthority(String authority)`**                         | **返回`true`当前委托人是否具有指定权限。例如， `hasAuthority('read')`** |
| **`hasAnyAuthority(String… authorities)`**                   | **返回`true`如果当前主体具有任何所提供的当局的（给定为逗号分隔的字符串列表）例如， `hasAnyAuthority('read', 'write')`** |
| **`principal`**                                              | **允许直接访问代表当前用户的主体对象**                       |
| **`authentication`**                                         | **允许直接访问`Authentication`从`SecurityContext`**          |
| **`permitAll`**                                              | **始终评估为 `true`**                                        |
| **`denyAll`**                                                | **始终评估为 `false`**                                       |
| **`isAnonymous()`**                                          | **返回`true`当前委托人是否为匿名用户**                       |
| **`isRememberMe()`**                                         | **返回`true`当前主体是否是“记住我”的用户**                   |
| **`isAuthenticated()`**                                      | **`true`如果用户不是匿名的，则返回**                         |
| **`isFullyAuthenticated()`**                                 | **返回`true`如果用户不是匿名或记得，我的用户**               |
| **`hasPermission(Object target, Object permission)`**        | **返回`true`用户是否可以访问给定权限的给定目标。例如，`hasPermission(domainObject, 'read')`** |
| **`hasPermission(Object targetId, String targetType, Object permission)`** | **返回`true`用户是否可以访问给定权限的给定目标。例如，`hasPermission(1, 'com.example.domain.Message', 'read')`** |

##### 2.登录

   如果此时，我们有自己的登录界面，需要替换掉**Spring Security**所提供的默认的界面，这时可以用**fromLogin()**和**loginPage()**方法来实现：

```java
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
            .antMatchers("/user", "/menu")
            .access("hasRole('ADMIN')")
            .antMatchers("/", "/**").permitAll()
            .and()
            .formLogin()
            .loginPage("/login");
    }
```

   这便将登录地址指向了“/**login**”。如果需要指定登录成功时，跳转的地址，可以使用**defaultSuccessUrl()**方法：

```java
           .and()
            .formLogin()
            .loginPage("/login")
            .defaultSuccessUrl("/home")
```

   此时用户登录过后，将跳转到主页来。

   下面，我们来看看登出。

##### 3.登出

   和登录类似的，可以使用**logout()**和**logoutSuccessUrl()**方法来实现：

```java
            .and()
            .logout()
            .logoutSuccessUrl("/login")
```

   上面例子中，用户登出后将跳转到登录界面。

#### 4、小结

   **至此，我们已基本了解了Spring Security配置，可以将它配置成我们想要的样子（基本）。其实Spring Security能做的事还有很多，光看我这篇文章是不够的。学习它最有效的方法就是阅读官方文档。里面有关于Spring Security最全最新的知识！（官网地址：[https://spring.io/projects/spring-security](https://links.jianshu.com/go?to=https%3A%2F%2Fspring.io%2Fprojects%2Fspring-security)）**

