---
title: SpringBoot接收参数的几种常用方式
tags:
  - SpringBoot
categories:
  - SpringBoot
date: 2022-05-28 18:57:06
---
# 第一类：请求路径参数

## 1、@PathVariable

获取路径参数。即*url/{id}*这种形式。

## 2、@RequestParam

获取查询参数。即*url?name=*这种形式

### 例子

GET
http://localhost:8080/demo/123?name=suki_rong
对应的java代码：

```
@GetMapping("/demo/{id}")
//使用@PathVariable下边必须要配合@RequestParam 去使用
public void demo(@PathVariable(name = "id") String id, @RequestParam(name = "name") String name) {
    System.out.println("id="+id);
    System.out.println("name="+name);
}
Copy
```

输出结果：
id=123
name=suki_rong

## 3、@RequestHeader(value="token")

在 Java 中，@RequestHeader 注解用于从 HTTP 请求头中获取指定名称的值，并将其绑定到方法参数上。当你在控制器方法的参数前使用 @RequestHeader 注解时，Spring MVC 会自动从请求头中读取对应的值，并将其传递给该参数。
例如，假设你有一个 RESTful API 方法，需要从请求头中获取名为 "token" 的值，你可以这样定义方法：

```java
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class MyController {

    @GetMapping("/api/data")
    public String getData(@RequestHeader(value = "token") String token) {
        // 在这里可以使用 token 值进行验证或其他操作
        return "Data for token: " + token;
    }
}
```



# 第二类：Body参数

因为是POST请求，这里用Postman的截图结合代码说明

## 1、@RequestBody

### 例子

对应的java代码：

```
@PostMapping(path = "/demo1")
public void demo1(@RequestBody Person person) {
    System.out.println(person.toString());
}
Copy
```

输出结果：
name:suki_rong;age=18;hobby:programing

也可以是这样

```
@PostMapping(path = "/demo1")
public void demo1(@RequestBody Map<String, String> person) {
    System.out.println(person.get("name"));
}
Copy
```

输出结果：
suki_rong

## 2、无注解

### 例子

对应的java代码：

```
@PostMapping(path = "/demo2")
public void demo2(Person person) {
    System.out.println(person.toString());
}
Copy
```

输出结果：
name:suki_rong;age=18;hobby:programing

## Person类

```
public class Person {

    private long id;
    private String name;
    private int age;
    private String hobby;

    @Override
    public String toString(){
        return "name:"+name+";age="+age+";hobby:"+hobby;
    }

    // getters and setters
}
Copy
```

# 第三类：请求头参数以及Cookie

## 1、@RequestHeader

## 2、@CookieValue

### 例子

java代码：

```
@GetMapping("/demo3")
public void demo3(@RequestHeader(name = "myHeader") String myHeader,
        @CookieValue(name = "myCookie") String myCookie) {
    System.out.println("myHeader=" + myHeader);
    System.out.println("myCookie=" + myCookie);
}
Copy
```

也可以这样

```
@GetMapping("/demo3")
public void demo3(HttpServletRequest request) {
    System.out.println(request.getHeader("myHeader"));
    for (Cookie cookie : request.getCookies()) {
        if ("myCookie".equals(cookie.getName())) {
            System.out.println(cookie.getValue());
        }
    }
}
```