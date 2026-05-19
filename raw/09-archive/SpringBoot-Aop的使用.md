---
title: SpringBoot-Aop的使用
tags:
  - SpringBoot
categories:
  - SpringBoot
date: 2023-06-13 16:50:40
---

# SpringBoot-AOP的使用

在了解springboot的aop之前要先了解java的自定义注解的相关内容

## 自定义注解

## `@Retention`: 表示该注解的生命周期，是RetentionPolicy类型的，该类型是一个枚举类型，可提供三个值选择，分别是：`CLASS`、`RUNTIME`、`SOURCE`

- - `RetentionPolicy.CLASS`: 注解被保留到class文件，但jvm加载class文件时候被遗弃，这是默认的生命周期；
  - `RetentionPolicy.RUNTIME`: 注解不仅被保存到class文件中，jvm加载class文件之后，仍然存在；
  - `RetentionPolicy.SOURCE`: 注解只保留在源文件，当Java文件编译成class文件的时候，注解被遗弃；
    由此可见生命周期关系：SOURCE < CLASS < RUNTIME，我们一般用RUNTIME

- `@Target`: 表示该注解的作用范围，是ElementType类型的，该类型是一个枚举类型，一共提供了10个值选择，我们最常用的几个：`FIELD`、`TYPE`、`PARAMETER`、`METHOD`
  - `ElementType.FIELD`:用于字段、枚举的常量
  - `ElementType.TYPE`:用于接口、类、枚举、注解
  - `ElementType.PARAMETER`:用于方法参数
  - `ElementType.METHOD`:用于方法

```java
/**
 * @Description:
 * @Name: TestLog
 * @Author: wgp
 * @DateTime: 2023/6/13 15:45
 */
@Target({ElementType.METHOD})
@Retention(RetentionPolicy.RUNTIME)
@Documented
public @interface TestLog {

    String value() default "";

    String messsge() default "aaaaaaaa";

}
```

## aop的定义

面向切面编程

## SpringBoot中使用AOP

### 一、引入aop

```xml
<!--springboot自带的aop引用这一个包即可-->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
</dependency>

<!--由于我在写代码的时候为了方便还引用了其他的包，如果自己写可以直接引用这个-->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-aop</artifactId>
    <version>2.2.1.RELEASE</version>
</dependency>
<dependency>
    <groupId>cn.hutool</groupId>
    <artifactId>hutool-all</artifactId>
    <version>5.8.11</version>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.47</version>
</dependency>
```

### 二、 定义切面类。

为什么使用AOP编程范式？
（1）分离功能需求和非功能需求；
（2）集中处理某一关注点；
（3）侵入性少，增强代码可读性及可维护性。

下边记录AOP切面在springboot中的使用。

AOP的应用场景
权限控制、缓存控制、事务控制、分布式追踪、异常处理等

**eg：**

如果需要在每一个方法上打印入参和出参的日志，如果在每个方法上去加上log很显然这是不现实的，这样会增加重复代码，会让代码变得冗余。

而使用AOP之后，你可以建一个切面类，对要进行权限验证的方法进行切入即可！

在程序运行时，动态的将代码切入到类的指定方法或者位置上的思想，就是面向切面编程。

我这里写了个简单的例子

```java
 * @Description: 切面类
 * @Name: TestAspect
 * @Author: wgp
 * @DateTime: 2023/6/13 16:11
 */
//Component 和 Aspect 配合使用声明为切面类
@Component
@Aspect
@Slf4j
public class TestAspect {
    
}
```

**注：这里的Aspect和Component这两个注解要一起使用，将此类声明为切面类，所有的通知将在此处理，还有一些注解在这里解释下**

1.  在类上使用 @Component 注解 把切面类加入到IOC容器中

2. 在类上使用 @Aspect 注解 使之成为切面类

### 三、 AOP的常用的几个术语

1. Target：目标类，要被代理的类，例如，UserController；

2. JoinPoint（连接点）：所谓的连接点，是指那些被拦截到的方法；
3. PointCut（切入点）：被增强的连接点（所谓的增强其实就是添加的新功能）；
4. Advice（通知、增强），增强代码；

5. Weaving（织入）：是指把增强的advice应用到目标对象target来创建新的代理对象proxy的 过程。

6. proxy：代理类；

7. Aspect（切面）：是切入点pointcut和通知advice的结合。

### 四、定义切入点

定义方式：

execution：用于匹配方法执行的连接点；

within：用于匹配指定类型内的方法执行；

this：用于匹配当前AOP代理对象类型的执行方法；注意是AOP代理对象的类型匹配，这样就可能包括引入接口也类型匹配；    

target：用于匹配当前目标对象类型的执行方法；注意是目标对象的类型匹配，这样就不包括引入接口也类型匹配；

args：用于匹配当前执行的方法传入的参数为指定类型的执行方法；

@within：用于匹配所以持有指定注解类型内的方法；

@target：用于匹配当前目标对象类型的执行方法，其中目标对象持有指定的注解；

@args：用于匹配当前执行的方法传入的参数持有指定注解的执行；

@annotation：用于匹配当前执行方法持有指定注解的方法；

建议使用@annotation，配合自定义注解，实现拦截

### 五、切入点表达式

> 切入点表达式的格式：

```
execution([可见性] 返回类型 [声明类型].方法名(参数) [异常])
```

其中【】中的为可选，其他的还支持通配符的使用:

*：匹配所有字符
..：一般用于匹配多个包，多个参数
+：表示类及其子类
运算符有：&&、||、!

> 常用的表达式

- 包名切面
  对 com.app.controller 包中所有的类的所有方法切面

```java
@Pointcut("execution(public * com.app.controller.*.*(..))")
```

+ 包名及子包切面
  对 com.app.controller 及其子包中所有的类的所有方法切面

```java
@Pointcut("execution(public * com.app.controller..*.*(..))")
```

- 类名切面
  只针对 StudentController 类切面

```java
@Pointcut("execution(public * com.app.controller.StudentController.*(..))")
```

> 测试代码

```java
@Pointcut("execution (* com.example.aspectdemo.controller.*.*(..))")
public void test() {
}
```

这里加个图更方便理解

![6f061d950a7b0208f9798de68e7edfda562cc8b2](6f061d950a7b0208f9798de68e7edfda562cc8b2.png)

我在网上又找到了些其他的表达式，仅供参考

> 1）execution：用于匹配子表达式。
>
> ​      //匹配com.cjm.model包及其子包中所有类中的所有方法，返回类型任意，方法参数任意
> ​      @Pointcut("execution(* com.cjm.model..*.*(..))")
> ​      public void before(){}
>
>  
>
>    2）within：用于匹配连接点所在的Java类或者包。
>
> ​      //匹配Person类中的所有方法
> ​      @Pointcut("within(com.cjm.model.Person)")
> ​      public void before(){}
>
>  
>
> ​      //匹配com.cjm包及其子包中所有类中的所有方法
>
> ​      @Pointcut("within(com.cjm..*)")
> ​      public void before(){}
>
>  
>
>    3） this：用于向通知方法中传入代理对象的引用。
>       @Before("before() && this(proxy)")
>       public void beforeAdvide(JoinPoint point, Object proxy){
>          //处理逻辑
>       }
>
>  
>
>    4）target：用于向通知方法中传入目标对象的引用。
>       @Before("before() && target(target)
>       public void beforeAdvide(JoinPoint point, Object proxy){
>          //处理逻辑
>       }
>
>  
>
>    5）args：用于将参数传入到通知方法中。
>       @Before("before() && args(age,username)")
>       public void beforeAdvide(JoinPoint point, int age, String username){
>          //处理逻辑
>       }
>  
>    6）@within ：用于匹配在类一级使用了参数确定的注解的类，其所有方法都将被匹配。 
>
> ​      @Pointcut("@within(com.cjm.annotation.AdviceAnnotation)") － 所有被@AdviceAnnotation标注的类都将匹配
> ​      public void before(){}
>
> 　　
>
>    7）@target ：和@within的功能类似，但必须要指定注解接口的保留策略为RUNTIME。
>       @Pointcut("@target(com.cjm.annotation.AdviceAnnotation)")
>       public void before(){}
>
>  
>
>    8）@args ：传入连接点的对象对应的Java类必须被@args指定的Annotation注解标注。
>       @Before("@args(com.cjm.annotation.AdviceAnnotation)")
>       public void beforeAdvide(JoinPoint point){
>          //处理逻辑
>       }
>
> 　　
>
>    9）@annotation ：匹配连接点被它参数指定的Annotation注解的方法。也就是说，所有被指定注解标注的方法都将匹配。
>       @Pointcut("@annotation(com.cjm.annotation.AdviceAnnotation)")
>       public void before(){}
>
>    10）bean：通过受管Bean的名字来限定连接点所在的Bean。该关键词是Spring2.5新增的。
>       @Pointcut("bean(person)")
>       public void before(){}

### 六、常见的五种通知

**前置通知**（@Before）：在目标方法调用之前调用通知

**后置通知**（@After）：在目标方法完成之后调用通知

**环绕通知**（@Around）：在被通知的方法调用之前和调用之后执行自定义的方法

- *包围一个连接点的通知，如方法调用。这是最强大的一种通知类型。环绕通知可以在方法调用前后完成自定义的行为。它也会选择是否继续执行连接点或直接返回它自己的返回值或抛出异常来结束执行。*

- 环绕通知最麻烦，也最强大，其是一个对方法的环绕，具体方法会通过代理传递到切面中去，切面中可选择执行方法与否，执行方法几次等。

- 环绕通知使用一个代理`ProceedingJoinPoint`类型的对象来管理目标对象，所以此通知的第一个参数必须是`ProceedingJoinPoint`类型，在通知体内，调用`ProceedingJoinPoint`的`proceed()`方法会导致后台的连接点方法执行。`proceed` 方法也可能会被调用并且传入一个`Object[]`对象-该数组中的值将被作为方法执行时的参数。

**返回通知**（@AfterReturning）：在目标方法成功执行之后调用通知

**异常通知**（@AfterThrowing）：在目标方法抛出异常之后调用通知

{% note success %}
通过切入点执行通知
{% endnote %}

```java
@Component
@Aspect
@Slf4j //这里方便打印日志使用，如果不用可以不写
public class TestAspect {

    @Pointcut("execution (* com.example.aspectdemo.controller.*.*(..))")
    public void test() {
    }

    @Before("test()")
    public void beforeAdvice() {
        System.out.println("前置通知，进入方法前打印");
        System.out.println("beforeAdvice...");
    }
    
    @After("test()")
    public void afterAdvice() {
        System.out.println("方法调用完成后通知");
        System.out.println("afterAdvice...");
    }

    @Around("test()")
    public void aroundAdvice(ProceedingJoinPoint proceedingJoinPoint) {
        System.out.println("before");
        try {
            proceedingJoinPoint.proceed();
        } catch (Throwable t) {
            t.printStackTrace();
        }
        System.out.println("after");
    }
}
```

启动项目访问链接

```http
###
GET http://localhost:8080/test/index
```

打印结果

![image-20230613172430375](image-20230613172430375.png)

{% note success %}
通过识别注解的方式执行切面类
{% endnote %}

```java
@Component
@Aspect
@Slf4j
public class TestAspect {

//    @Pointcut("execution (* com.example.aspectdemo.controller.*.*(..))")
//    public void test() {
//        System.out.println("111111111111111");
//    }


    @Before("@annotation(testLog)")
    public void beforeAdvice(TestLog testLog) {
        System.out.println("前置通知，进入方法前打印");
        System.out.println("beforeAdvice...");
    }


    @After("@annotation(testLog)")
    public void afterAdvice(TestLog testLog) {
        System.out.println("方法调用完成后通知");
        System.out.println("afterAdvice...");
    }
    /**
     * 这里的方法指的是上述所有拦截的方法
     */

    @Around("@annotation(testLog)")
    public void aroundAdvice(ProceedingJoinPoint proceedingJoinPoint,TestLog testLog) {
        System.out.println("before");
        try {
            proceedingJoinPoint.proceed();
        } catch (Throwable t) {
            t.printStackTrace();
        }
        System.out.println("after");
    }


    @AfterReturning("@annotation(testLog)")
    public void AfterReturning(TestLog testLog) {
        System.out.println("方法调用完成后通知");
        System.out.println("afterAdvice...");
    }


    @AfterThrowing("@annotation(testLog)")
    public void AfterThrowing(TestLog testLog) {
        System.out.println("方法调用完成后通知");
        System.out.println("afterAdvice...");
    }


}

```

访问链接

```http
###
GET http://localhost:8080/test/index
```

执行结果

![image-20230614084108442](image-20230614084108442.png)

### 七、在通知中获取参数

> 任何通知方法可以将第一个参数定义为`org.aspectj.lang.JoinPoint`类型（环绕通知需要定义第一个参数为`ProceedingJoinPoint`类型，它是 `JoinPoint` 的一个子类）。`JoinPoint`接口提供了一系列有用的方法，比如 `getArgs()`（返回方法参数）、`getThis()`（返回代理对象）、`getTarget()`（返回目标）、`getSignature()`（返回正在被通知的方法相关信息）和 `toString()`（打印出正在被通知的方法的有用信息）

#### controller方法改造

```
/**
 * @Description: 自定义注解测试
 * @Name: TestController
 * @Author: wgp
 * @DateTime: 2023/6/13 15:22
 */
@RequestMapping("/test")
@RestController
public class TestController {

    @TestLog("测试测试")
    @GetMapping("/index/{id}")
    public Result getTest(@PathVariable String id){
        System.out.println("controller参数:"+ id);
        return null;
    }

}
```

#### JoinPoint

使用的通知中 ，除了环绕通知 其他四种通知都会拿到 JoinPoint joinPoint 这么一个参数，下边记录下该参数种的常用方法：

（1）**Signature joinPoint.getignature()** 获取封装课署名信息的对象，在该对象种，可以获取到 目标方法名、参数、所属class类等信息。
**joinPoint.getignature().getDeclaringType().getSimpleName()** 获取切入点方法对应的类名
**joinPoint.getSignature().getName()** 获取切入点方法名

（2）**Object[] getArgs()**
获取传入目标方法的参数。

（3）**Object getTarget()**
获取被代理的对象。

（4）**Object getThis()**
获取代理的对象。

#### @Before通知

```java
package com.example.aspectdemo.aspect;


import com.example.aspectdemo.annotation.TestLog;
import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Before;
import org.springframework.stereotype.Component;

import java.util.Arrays;

/**
 * 需要的依赖
 * <dependency>
 * <groupId>org.springframework.boot</groupId>
 * <artifactId>spring-boot-starter-aop</artifactId>
 * </dependency>
 *
 * @Description: 切面类
 * @Name: TestAspect
 * @Author: wgp
 * @DateTime: 2023/6/13 16:11
 */
//Component 和 Aspect 配合使用声明为切面类
@Component
@Aspect
public class TestAspect {


    @Before("@annotation(testLog)")
    public void beforeAdvice(JoinPoint joinPoint, TestLog testLog) {
        System.out.println("************** 获取切入点的相关信息 **************");
        // 获取切入点的方法
        System.out.println("【切入点方法为】" + joinPoint);
        // 获取切入点方法名对应的类名
        System.out.println("【切入点方法名的简单类名为】" + joinPoint.getSignature().getDeclaringType().getSimpleName());
        // 获取切入点方法名
        System.out.println("【切入点方法名为】" + joinPoint.getSignature().getName());
        // 获取切入点方法参数列表
        Object[] args = joinPoint.getArgs();
        System.out.println("【切入点方法参数列表】" + Arrays.toString(args));
        // 获取被代理的对象
        System.out.println("【被代理的对象】" + joinPoint.getTarget());
        // 获取代理的对象
        System.out.println("【代理的对象】" + joinPoint.getThis());

        System.out.println("----------------------------");
        System.out.println("对带有了@TestLog注解的方法，做check检查");
    }


}

```

**打印结果**

```text
************** 获取切入点的相关信息 **************
【切入点方法为】execution(Result com.example.aspectdemo.controller.TestController.getTest(String))
【切入点方法名的简单类名为】TestController
【切入点方法名为】getTest
【切入点方法参数列表】[10]
【被代理的对象】com.example.aspectdemo.controller.TestController@7807a3d8
【代理的对象】com.example.aspectdemo.controller.TestController@7807a3d8
----------------------------
对带有了@TestLog注解的方法，做check检查
```

#### **@After() 后置方法 参数 JoinPoint**

与前置通知的方法一样，这里不记录了，注意：后置通知获取不到目标方法返回的结果，在后置结果通知中才能获取到。

**注意：**

**无论结果正常返回还是抛出异常，后置通知都会执行！！！**

```java
@Component
@Aspect
public class TestAspect {


    // 定义一个切入点，关于切入点如何定义？
    @Pointcut("@annotation(com.example.aspectdemo.annotation.TestLog)")
    public void pointFn(){}

    // 定义一个通知,在执行pointFn这个方法之前（切入入进去之前），我们需要执行check方法
    @Before("pointFn()")
    public void check(JoinPoint joinPoint) {
        System.out.println("前置通知执行了");
    }
    // 在目标方法执行后，无论发生什么异常都会执行通知
    // 【注意】,在后置通知中还不能访问目标方法执行返回的结果，执行结果需要到
    //        返回通知里访问！！！
    @After("pointFn()")
    public void afterCheck(JoinPoint joinPoint) {
        System.out.println("后置通知执行了");
    }
}
```

controllert中的方法

```java
@RequestMapping("/test")
@RestController
public class TestController {

    @TestLog("测试测试")
    @GetMapping("/index/{id}")
    public Result getTest(@PathVariable String id){
        int a = 1;
        int b = 0;
        int i = a / b;
        System.out.println("controller参数:"+ id);
        return null;
    }
}
```

**执行的结果**

![image-20230614092515193](image-20230614092515193.png)

这里前置通知和后置通知都执行了，及时异常也执行方法

#### @AfterReturning 返回通知（后置结果通知）

@AfterReturning (value=“”, returning=“” ) 结果通知参数会有两个，
参数一：value 值就是切点方法；
参数二：returning 值的是结果参数，该值必须要跟下边方法中参数二 中的参数 一致才行。

```java
@Component
@Aspect
public class TestAspect {
    // 定义一个切入点，关于切入点如何定义？
    @Pointcut("@annotation(com.example.aspectdemo.annotation.TestLog)")
    public void pointFn(){}
    // 返回通知：在方法正常结束后，时可以拿到方法的返回值的！！！
    // returning 值是result，所以下边方法参数二 的参数也必须为result
    // 通过result我们可以获取到目标方法返回的结果！！！
    @AfterReturning(value = "pointFn()", returning = "result")
    public void afterRe(JoinPoint joinPoint, Object result) {
        System.out.println("==========结果通知执行了==========");
        // joinPoint参数与前置通知、后置通知一样，不记录了
        System.out.println("返回的参数为："+result);
        System.out.println("返回的JSON格式的参数为："+ JSON.toJSONString(result));
    }
}
```

**controller改造**

```java
@RequestMapping("/test")
@RestController
public class TestController {
    @TestLog("测试测试")
    @GetMapping("/index/{id}")
    public String getTest(@PathVariable String id) {
        System.out.println("controller参数:" + id);
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("code", "1");
        jsonObject.put("msg", "222222222222222");
        return jsonObject.toString();
    }
}
```

打印结果

```text
==========结果通知执行了==========
返回的参数为：{"msg":"222222222222222","code":"1"}
返回的JSON格式的参数为："{\"msg\":\"222222222222222\",\"code\":\"1\"}"
```

#### @AfterThrowing 异常通知（后置结果异常通知）

@AfterThrowing (value = “pointFn()”, throwing = “e”) 异常通知参数会有两个，
参数一：value 值就是切点方法；
参数二：throwing 值的是异常参数，该值必须要跟下边方法中参数二 中的参数 一致才行。

```java
@Component
@Aspect
public class TestAspect {
    // 定义一个切入点，关于切入点如何定义？
    @Pointcut("@annotation(com.example.aspectdemo.annotation.TestLog)")
    public void pointFn(){}

    // 在目标方法出现异常时会执行的代码，可以获取到异常对象、信息等
    @AfterThrowing(value = "pointFn()", throwing = "e")
    public void afterTh(JoinPoint joinPoint, Exception e) {
        // joinPoint参数与前置通知、后置通知一样，不记录了
        // 获取异常信息（这个异常信息是我们自定义的！）
        System.out.println("==========结果通知执行了==========");
        System.out.println(e.getMessage());
    }
}
```

**controller改造**

```
@RequestMapping("/test")
@RestController
public class TestController {

    @TestLog("测试测试")
    @GetMapping("/index/{id}")
    public void getTest(@PathVariable String id) throws Exception {
        System.out.println("controller参数:" + id);
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("code", "1");
        jsonObject.put("msg", "222222222222222");
        throw new Exception("故意抛出一个错误，让AfterThrowing通知");
    }
}
```

**执行结果**

```text
==========结果通知执行了==========
故意抛出一个错误，让AfterThrowing通知
2023-06-14T09:42:07.260+08:00 ERROR 25504 --- [nio-8080-exec-1] o.a.c.c.C.[.[.[/].[dispatcherServlet]    : Servlet.service() for servlet [dispatcherServlet] in context with path [] threw exception [Request processing failed: java.lang.Exception: 故意抛出一个错误，让AfterThrowing通知] with root cause

java.lang.Exception: 故意抛出一个错误，让AfterThrowing通知
```

#### @Around 环绕通知（等于前置通知 + 返回通知 + 异常通知 + 后置通知）

环绕通知是通知类行中功能最强大的，它是JoinPoint的子接口，环绕通知需要携带 ProceedingJoinPoint 类型的参数。

环绕通知的几个重点：

（1）环绕通知类似于动态代理的全过程，ProceedingJoinPoint pjp 类型的参数可以决定是否执行目标方法（也就是说必须要手动调用 pip.proceed() 方法，目标方法才能执行）， 如果忘记这样做就会导致通知被执行了 , 但目标方法没有被执行 ，且让环绕通知必须要有返回值，返回值即目标方法的返回值。

（2）如果环绕通知没有返回值，会出现空指针异常的情况。

```java
@Component
@Aspect
public class TestAspect {
    // 定义一个切入点，关于切入点如何定义？
    @Pointcut("@annotation(com.example.aspectdemo.annotation.TestLog)")
    public void pointFn(){}

    @Around("pointFn()")
    public void aroundFn(ProceedingJoinPoint pjp) {
        Object[] args = pjp.getArgs();
        System.out.println("入参----"+Arrays.toString(args));
        String methodName = pjp.getSignature().getName();
        System.out.println("==========环绕通知执行了==========");
        Object result = null;
        try{
            // == 前置通知
            System.out.println("【目标方法】"+methodName);
            // 执行目标方法
            result = pjp.proceed();
            // == 结果通知
            System.out.println("目标方法返回结果为："+result);
        }catch (Throwable e) {
            // == 异常通知
            System.out.println(e.getMessage());
        }
        // == 后置通知
        System.out.println("后置通知执行");
    }
}
```

打印结果

```text
入参----[10]
==========环绕通知执行了==========
【目标方法】getTest
controller参数:10
目标方法返回结果为：{"msg":"222222222222222","code":"1"}
后置通知执行
```

**除了环绕通知和异常通知，来看下 前置通知、结果通知和后置通知的执行顺序**

```java
@Component
@Aspect
public class TestAspect {
    // 定义一个切入点，关于切入点如何定义？
    @Pointcut("@annotation(com.example.aspectdemo.annotation.TestLog)")
    public void pointFn(){}

    @Before("@annotation(testLog)")
    public void beforeAdvice(JoinPoint joinPoint, TestLog testLog) {
        System.out.println("前置通知");
    }


    @After("@annotation(testLog)")
    public void after(JoinPoint joinPoint, TestLog testLog) {
        System.out.println("后置通知");
    }

    @AfterReturning ("@annotation(testLog)")
    public void AfterReturning (JoinPoint joinPoint, TestLog testLog) {
        System.out.println("结果通知");
    }
}
```

执行结果

```text
前置通知
结果通知
后置通知
```

#### **指定切面优先级问题**

• 在同一个目标方法上应用多个切面时，除非明确指定，否则他们的的优先级时不确定的。
• 切面的优先级可以通过实现Ordered接口或利用Order注解指定。
• 实现 Ordered 接口 , getOrder () 方法的返回值越小 , 优先级越高，切面出的越在前面。
• 若使用 @Order 注解 , 序号出现在注解中

新增一个切面类TestAspect1

```java
@Order(2)
@Component
@Aspect
public class TestAspect1 {

    @Before("@annotation(testLog)")
    public void beforeAdvice(JoinPoint joinPoint, TestLog testLog) {
        System.out.println("前置通知");
    }
}
```

老的切面类代码

```java
@Order(2)
@Component
@Aspect
public class TestAspect {

    @Before("@annotation(testLog)")
    public void beforeAdvice(JoinPoint joinPoint, TestLog testLog) {
        System.out.println("前置通知");
    }
}
```

执行结果

```tex
新的的切面通知1111111111111
老的切面通知
```

**最后，来看下同时使用拦截器和aop时，执行顺序**

很明显拦截器在最外层执行，而aop切面在里层执行（这里的代码找了个别人的贴图，这里暂时就不测试了）

![image-20230614095930485](image-20230614095930485.png)
