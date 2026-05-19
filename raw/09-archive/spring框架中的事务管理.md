---
title: spring框架中的事务管理
tags:
  - 事务
categories:
  - Spring
date: 2024-03-20 08:56:42
---

事务管理是应用系统开发中必不可少的一部分。Spring 为事务管理提供了丰富的功能支持。Spring 事务管理分为编码式和声明式的两种方式。编程式事务指的是通过编码方式实现事务；声明式事务基于 AOP,将具体业务逻辑与事务处理解耦。声明式事务管理使业务代码逻辑不受污染, 因此在实际使用中声明式事务用的比较多。声明式事务有两种方式，一种是在配置文件（xml）中做相关的事务规则声明，另一种是基于@Transactional 注解的方式。注释配置是目前流行的使用方式，

> ### @Transactional 注解的属性信息

| 属性名          | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| name            | 当在配置文件中有多个 TransactionManager,可以用该属性指定选择哪个事务管理器 |
| propagation     | 事务的传播行为，默认值为 REQUIRED。                          |
| isolation       | 事务的隔离度，默认值采用 DEFAULT.                            |
| timeout         | 事务的超时时间，默认值为-1。如果超过该时间限制但事务还没有完成，则自动回滚事务。 |
| read-only       | 指定事务是否为只读事务，默认值为false;为了忽略那些不需要事务的方法，比如读取数据，可以设置 read-only为true。 |
| rollback-for    | 用于指定能够触发事务回滚的异常类型，如果有多个异常类型需要指定，各类型之间可以通过逗号分隔。 |
| no-rollback-for | 抛出 no-rollback-for 指定的异常类型，不回滚事务。            |

除此以外，@Transactional 注解也可以添加到类级别上。当把@Transactional 注解放在类级别时，表示所有该类的公共方法都配置相同的事务属性信息。见清单 2，EmployeeService 的所有方法都支持事务并且是只读。当类级别配置了@Transactional，方法级别也配置了@Transactional，应用程序会以方法级别的事务属性信息来管理事务，换言之，方法级别的事务属性信息会覆盖类级别的相关配置信息。

**1 .添加位置**

1）接口实现类或接口实现方法上，而不是接口类中。
2）访问权限：public 的方法才起作用。@Transactional 注解应该只被应用到 public 方法上，这是由 Spring [AOP](https://so.csdn.net/so/search?q=AOP&spm=1001.2101.3001.7020) 的本质决定的。
系统设计：将标签放置在需要进行事务管理的方法上，而不是放在所有接口实现类上：只读的接口就不需要事务管理，由于配置了@Transactional就需要AOP拦截及事务的处理，可能影响系统性能。

```
1.接口中A、B两个方法，A无@Transactional标签，B有，上层通过A间接调用B，此时事务不生效。
 
2.接口中异常（运行时异常）被捕获而没有被抛出。
  默认配置下，spring 只有在抛出的异常为运行时 unchecked 异常时才回滚该事务，
  也就是抛出的异常为RuntimeException 的子类(Errors也会导致事务回滚)，
  而抛出 checked 异常则不会导致事务回滚 。可通过 @Transactional rollbackFor进行配置。
 
3.多线程下事务管理因为线程不属于 spring 托管，故线程不能够默认使用 spring 的事务,
  也不能获取spring 注入的 bean 。
  在被 spring 声明式事务管理的方法内开启多线程，多线程内的方法不被事务控制。
  一个使用了@Transactional 的方法，如果方法内包含多线程的使用，方法内部出现异常，
  不会回滚线程中调用方法的事务。

```



![image-20240320091039636](\img\spring框架中的事务管理\image-20240320091039636.png)

![image-20240320091047795](\img\spring框架中的事务管理\image-20240320091047795.png)

```
1. 事务方法的嵌套调用会产生事务传播。
2. spring 的事务管理是线程安全的
3. 父类的声明的 @Transactional 会对子类的所有方法进行事务增强；
   子类覆盖重写父类方式可覆盖其 @Transactional 中的声明配置。
 
4. 类名上方使用 @Transactional，类中方法可通过属性配置来覆盖类上的 @Transactional 配置；
   比如：类上配置全局是可读写，可在某个方法上改为只读。
```

### 自调用问题

> 避免 Spring 的 AOP 的自调用问题

在 Spring 的 AOP 代理下，只有目标方法由外部调用，目标方法才由 Spring 生成的代理对象来管理，这会造成自调用问题。若同一类中的其他没有@Transactional 注解的方法内部调用有@Transactional 注解的方法，有@Transactional 注解的方法的事务被忽略，不会发生回滚。见清单 5 举例代码展示。

> 自调用问题举例

```java
@Service
-->public class OrderService {
    private void insert() {
insertOrder();
}
@Transactional
    public void insertOrder() {
        //insert log info
        //insertOrder
        //updateAccount
       }
}
```

### 注解失效问题

正常情况下，只要在方法上添加@Transactional注解就完事了，但是需要注意的是，虽然使用简单，但是如果不合理地使用注解，还是会存在注解失效的问题。

**@Transactional 应用在非 public 修饰的方法上**

事务拦截器在目标方法执行前后进行拦截，内部会调用方法来获取Transactional 注解的事务配置信息，调用前会检查目标方法的修饰符是否为 public，不是 public则不会获取@Transactional 的属性配置信息。

**@Transactional 注解属性 rollbackFor 设置错误**

rollbackFor 可以指定能够触发事务回滚的异常类型。Spring默认抛出了未检查unchecked异常（继承自 RuntimeException 的异常）或者 Error才回滚事务；其他异常不会触发回滚事务。如果在事务中抛出其他类型的异常，但却期望 Spring 能够回滚事务，就需要指定rollbackFor属性。

**同一个类中方法调用，导致@Transactional失效**

开发中避免不了会对同一个类里面的方法调用，比如有一个类Test，它的一个方法A，A再调用本类的方法B（不论方法B是用public还是private修饰），但方法A没有声明注解事务，而B方法有。则外部调用方法A之后，方法B的事务是不会起作用的。这也是经常犯错误的一个地方。
那为啥会出现这种情况？其实这还是由于使用Spring AOP代理造成的，因为只有当事务方法被当前类以外的代码调用时，才会由Spring生成的代理对象来管理。

**异常被你的 catch“吃了”导致@Transactional失效**

如果你手动的catch捕获这个异常并进行处理，事务管理器会认为当前事务应该正常commit，就会导致注解失效，如果非要捕获且不失效，就必须在代码块内throw new Exception抛出异常。

**数据库引擎不支持事务**

开启事务的前提就是需要数据库的支持，我们一般使用的Mysql引擎时支持事务的，所以一般不会出现这种问题。

**开启多线程任务时，事务管理会受到影响**

因为线程不属于spring托管，故线程不能够默认使用spring的事务,也不能获取spring注入的bean在被spring声明式事务管理的方法内开启多线程，多线程内的方法不被事务控制。
如下代码，线程内调用insert方法，spring不会把insert方法加入事务就算在insert方法上加入@Transactional注解，也不起作用。

```java
@Service  
public class ServiceA {  
   
    @Transactional  
    public void threadMethod(){  
        this.insert();  
         System.out.println("main insert is over");  
        for(int a=0 ;a<3;a++){  
            ThreadOperation threadOperation= new ThreadOperation();  
            Thread innerThread = new Thread(threadOperation);  
            innerThread.start();  
        }  
    }  
   
    public  class ThreadOperation implements Runnable {  
        public ThreadOperation(){  
        }  
        @Override  
        public void run(){  
            insert();  
            System.out.println("thread insert is over");  
        }  
    }  
   
    public void insert(){  
   
    //do insert......  
   
    }  
}  
```

如果把上面insert方法提出到新的类中，加入事务注解，就能成功的把insert方法加入到事务管理当中

```java
@Service  
public class ServiceA {  
   
@Autowired  
private ServiceB serviceB;  
   
    @Transactional  
    public void threadMethod(){  
        this.insert();  
        System.out.println("main insert is over");  
        for(int a=0 ;a<3;a++){  
            ThreadOperation threadOperation= new ThreadOperation();  
            Thread innerThread = new Thread(threadOperation);  
            innerThread.start();  
        }  
    }  
   
    public  class ThreadOperation implements Runnable {  
        public ThreadOperation(){  
        }  
        @Override  
        public void run(){  
            serviceB.insert();  
            System.out.println("thread insert is over");  
        }  
    }  
   
    public void insert(){  
   
        //do insert......  
   
    }  
}  
   
@Service  
public class ServiceB {  
   
    @Transactional  
    public void insert(){  
   
        //do insert......  
   
    }  
   
}  
```

另外，使用多线程事务的情况下，进行回滚，比较麻烦。thread的run方法，有个特别之处，它不会抛出异常，但异常会导致线程终止运行。

最麻烦的是，在线程中抛出的异常即使在主线程中使用try…catch也无法截获这非常糟糕，我们必须要“感知”到异常的发生。比如某个线程在处理重要的事务，当thread异常终止，我必须要收到异常的报告，才能回滚事务。这时可以使用线程的UncaughtExceptionHandler进行异常处理，UncaughtExceptionHandler名字意味着处理未捕获的异常。更明确的说，它处理未捕获的运行时异常。

如下代码
线程出要使用
①处要抛出异常
②处要捕捉异常，并且要抛出RuntimeException
③处手动处理回滚逻辑

```java
@Service  
public class ServiceA {  
   
@Autowired  
private ServiceB serviceB;  
   
    @Transactional  
    public void threadMethod(){  
        this.insert();  
        System.out.println("main insert is over");  
        for(int a=0 ;a<3;a++){  
            ThreadOperation threadOperation= new ThreadOperation();  
            Thread innerThread = new Thread(threadOperation);  
            innerThread.setUncaughtExceptionHandler(new Thread.UncaughtExceptionHandler() {  
               public void uncaughtException(Thread t, Throwable e) {  
                   try {  
                        serviceB.delete();③  
                   } catch (Exception e1) {  
                       e1.printStackTrace();  
                   }  
               }  
            });  
            innerThread.start();  
        }  
    }  
   
    public  class ThreadOperation implements Runnable {  
        public ThreadOperation(){  
        }  
        @Override  
        public void run(){  
            try {  
               serviceB.insert();  
           }catch (Exception ex){ ②  
            System.out.println(" Exception in run ");  
               throw new RuntimeException();  
           }  
            System.out.println("thread insert is over");  
        }  
    }  
   
    public void insert(){  
   
        //do insert......  
   
    }  
}  
   
@Service  
public class ServiceB {  
   
    @Transactional  
    public void insert() throws Exception{ ①  
   
    //do insert......  
   
    }  
   
    @Transactional  
    public void delete() throws Exception{   
   
        //do delete......  
   
    }  
   
}  
```
