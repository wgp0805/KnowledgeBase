---
title: lambda表达式简单解析
tags:
  - lambda
categories:
  - JAVA
date: 2022-09-10 11:02:26
---

## 一、什么是lambda表达式

lambda是java8中的一个新特性，可以对一个接口的方法进行非常简洁的实现，但实际上lambda就是一个匿名函数

### Lambda对接口的要求

虽然可以使用Lambda表达式对某些接口进行简单的实现，但是并不是所有的接口都可以用Lambda表达式来实现，要求接口中定义的**必须要实现的抽象方法只能是一个**

> ```
> 在JAVA8中 ，对接口加了一个新特性：default
> 可以使用default对接口方法进行修饰，被修饰的方法在接口中可以默认实现
> ```

### @FunctionalInterface

修饰函数式接口的，接口中的抽象方法只有一个

二、Lambda的基础语法

#### 1.语法

Lambda表达式的基础语法
Lambda是一个匿名函数 一般关注的是以下两个重点：

- 参数列表
- 方法体

```
（）：用来描述参数列表
 {}：用来描述方法体 有时可以省略
->: Lambda运算符 读作goes to
 例 Test t=()->{System.out.println("hello word")}; 大括号可省略
```

#### 2、创建多个接口

```java
@FunctionalInterface
public interface LambdaNoneReturnNoneParmeter {
    void test();
}

 
//无返回值有单个参数
@FunctionalInterface
public interface LambdaNoneReturnSingleParmeter {
    void test(int n);
}

//无返回值 多个参数的接口
@FunctionalInterface
public interface LambdaNoneReturnMutipleParmeter {
    void test(int a,int b);
}

//有返回值 无参数接口
@FunctionalInterface
public interface LambdaSingleReturnNoneParmeter {
    int test();
}

//有返回值 有单个参数的接口
@FunctionalInterface
public interface LambdaSingleReturnSingleParmeter {
    int test(int n);
}

//有返回值 有多个参数的接口
@FunctionalInterface
public interface LambdaSingleReturnMutipleParmeter {
    int test(int a,int b);
}

```

#### 3、创建测试类

```java
public class Syntax1 {
    public static void main(String[] args) {
        // 无参无返回  
        LambdaNoneReturnNoneParmeter lambda1=()->{
            System.out.println("hello word");
        };
        lambda1.test();
        // 无返回值 单个参数 
        LambdaNoneReturnSingleParmeter lambda2=(int n)->{
            System.out.println("参数是："+n);
        };
        lambda2.test(10);
        // 无返回值 多个参数
        LambdaNoneReturnMutipleParmeter lambda3=(int a,int b)->{
            System.out.println("参数和是："+(a+b));
        };
        lambda3.test(10,12);
        // 有返回值 无参数
        LambdaSingleReturnNoneParmeter lambda4=()->{
            System.out.println("lambda4：");
            return 100;
        };
        int ret=lambda4.test();
        System.out.println("返回值是："+ret);
        // 有返回值 单个参数
        LambdaSingleReturnSingleParmeter lambda5=(int a)->{
            return a*2;
        };
        int ret2= lambda5.test(3);
        System.out.println("单个参数，lambda5返回值是:"+ret2);
        //有返回值 多个参数
        LambdaSingleReturnMutipleParmeter lambda6=(int a,int b)->{
            return a+b;
        };
        int ret3=lambda6.test(12,14);
        System.out.println("多个参数，lambda6返回值是："+ret3);
    }
}
```

## 三、语法精简

### 1.参数类型精简

由于在接口的抽象方法中，已经定义了参数的数量类型 所以在Lambda表达式中参数的类型可以省略
备注：如果需要省略类型，则每一个参数的类型都要省略，千万不要一个省略一个不省略

```java
LambdaNoneReturnMutipleParmeter lambda1=(int a,int b)-> {
    System.out.println("hello world"); 
};    
//可以精简为:
LambdaNoneReturnMutipleParmeter lambda1=(a,b)-> {
    System.out.println("hello world");
};
```

### 2.参数小括号精简

如果参数列表中，参数的数量只有一个 此时小括号可以省略

```java
LambdaNoneReturnSingleParmeter lambda2=(a)->{
    System.out.println("hello world");
};
//可以精简为:
LambdaNoneReturnSingleParmeter lambda2= a->{
    System.out.println("hello world");
};
```

### 3.方法大括号精简

如果方法体中只有一条语句，此时大括号可以省略

```java
LambdaNoneReturnSingleParmeter lambda3=a->{
    System.out.println("hello world");
};
//可以精简为:
LambdaNoneReturnSingleParmeter lambda3=a->System.out.println("hello world");
```

### 4.大括号精简补充

如果方法体中唯一的一条语句是一个返回语句，则省略大括号的同时 也必须省略return

```java
LambdaSingleReturnNoneParmeter lambda4=()->{
    return 10;
};
//可以精简为:
LambdaSingleReturnNoneParmeter lambda4=()->10;
```

### 5.多参数，有返回值 精简

```java
LambdaSingleReturnNoneParmeter lambda4=(a,b)->{
    return a+b;
};
//可以精简为:
LambdaSingleReturnMutipleParmeter lambda5=(a,b)->a+b;
```

## 四、Lambda语法进阶

### 1.方法引用(普通方法与静态方法)

在实际应用过程中，一个接口在很多地方都会调用同一个实现，例如：

```
LambdaSingleReturnMutipleParmeter lambda1=(a,b)->a+b;
LambdaSingleReturnMutipleParmeter lambda2=(a,b)->a+b;
```

这样一来每次都要写上具体的实现方法 a+b，如果需求变更，则每一处实现都需要更改，基于这种情况，可以将后续的是实现更改为已定义的 方法，需要时直接调用就行

**语法：**

方法引用： 可以快速的将一个Lambda表达式的实现指向一个已经实现的方法

方法的隶属者如果是静态方法，隶属的就是一个类，其他的话就是隶属对象

语法：方法的隶属者::方法名

注意：

1. 引用的方法中，参数数量和类型一定要和接口中定义的方法一致
2. 返回值的类型也一定要和接口中的方法一致

例：

```java
public class Syntax3 {
    public static void main(String[] args) {
        
        LambdaSingleReturnSingleParmeter lambda1=a->a*2;
        LambdaSingleReturnSingleParmeter lambda2=a->a*2;
        LambdaSingleReturnSingleParmeter lambda3=a->a*2;
        //简化
        LambdaSingleReturnSingleParmeter lambda4=a->change(a);
        //方法引用
        LambdaSingleReturnSingleParmeter lambda5=Syntax3::change;
    }
 
    //自定义的实现方法
    private static int change(int a){
        return a*2;
    }
}
```

### 2.方法引用(构造方法)

目前有一个实体类

```java
public class Person {
    public String name;
    public int age;

    public Person() {
        System.out.println("Person的无参构造方法执行");
    }

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
        System.out.println("Person的有参构造方法执行");
    }
}
```

两个接口，各有一个方法，一个接口的方法需要引用Person的无参构造，一个接口的方法需要引用Person的有参构造 用于返回两个Person对象，例：

```java
interface PersonCreater{
    //通过Person的无参构造实现
    Person getPerson();
}

interface PersonCreater2{
    //通过Person的有参构造实现
    Person getPerson(String name,int age);
}
```

那么可以写作：

```java
public class Syntax4 {
    public static void main(String[] args) {

        PersonCreater creater=()->new Person();

        //引用的是Person的无参构造
         //PersonCreater接口的方法指向的是Person的方法
        PersonCreater creater1=Person::new; //等价于上面的()->new Person()
        //实际调用的是Person的无参构造 相当于把接口里的getPerson()重写成new Person()。
        Person a=creater1.getPerson(); 
​
        //引用的是Person的有参构造
        PersonCreater2 creater2=Person::new;
        Person b=creater2.getPerson("张三",18);
    }
}
```

**注意：是引用无参构造还是引用有参构造 在于接口定义的方法参数**

转载至：https://blog.csdn.net/m0_51212267/article/details/123946067
