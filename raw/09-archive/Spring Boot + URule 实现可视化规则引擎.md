# Spring Boot + URule 实现可视化规则引擎，太优雅了！



**目录**

* 一、背景
  
* 二、介绍
  
* 三、安装使用
  
* 四、基础概念
  
* 3.3.1 向导式规则集
  
* 3.3.2 脚本式规则集
  
* 3.2.1 变量库文件
  
* 3.2.2 常量库文件
  
* 3.2.3 参数库文件
  
* 3.2.4 动作库文件
  
* 3.1 整体介绍
  
* 3.2 库文件
  
* 3.3 规则集
  
* 3.4 决策表
  
* 3.5 其他
  
* 四、运用场景
  
* 五、总结
  

* * *

## 一、背景

前段时间，在做项目重构的时候，遇到很多地方需要做很多的条件判断。当然可以用很多的 if-else 判断去解决，但是当时也不清楚怎么回事，就想玩点别的。于是乎，就去调研了规则引擎。

当然，市面上有很多成熟的规则引擎，功能很多，性能很好。但是，就是想玩点不一样的（大家做技术选型别这样，这个是反面教材）。最终一款 URule 的规则引擎吸引了我，主要还是采用浏览器可直接配置，不需要过多安装，可视化规则也做的不错。经过一系列调研，后面就把它接入了项目中，顺便记录下调研的结果。

## 二、介绍

规则引擎其实是一种组件，它可以嵌入到程序当中。将程序复杂的判断规则从业务代码中剥离出来，使得程序只需要关心自己的业务，而不需要去进行复杂的逻辑判断；简单的理解是规则接受一组输入的数据，通过预定好的规则配置，再输出一组结果。

当然，市面上有很多成熟的规则引擎，如：Drools、Aviator、EasyRules 等等。但是 URule，它可以运行在 Windows、Linux、Unix 等各种类型的操作系统之上，采用纯浏览器的编辑模式，不需要安装工具，直接在浏览器上编辑规则和测试规则。

当然这款规则引擎有开源和 pro 版本的区别，至于 pro 版是啥，懂的都懂，下面放个表格，了解下具体的区别

| 特性  | PRO 版 | 开源版 |
| --- | --- | --- |
| 向导式决策集 | 有   | 有   |
| 脚本式决策集 | 有   | 有   |
| 决策树 | 有   | 有   |
| 决策流 | 有   | 有   |
| 决策表 | 有   | 有   |
| 交叉决策表 | 有   | 无   |
| 复杂评分卡 | 有   | 无   |
| 文件名、项目名重构 | 有   | 无   |
| 参数名、变量常量名重构 | 有   | 无   |
| Excel 决策表导入 | 有   | 无   |
| 规则集模版保存与加载 | 有   | 无   |
| 中文项目名和文件名支持 | 有   | 无   |
| 服务器推送知识包到客户端功能的支持 | 有   | 无   |
| 知识包优化与压缩的支持 | 有   | 无   |
| 客户端服务器模式下大知识包的推拉支持 | 有   | 无   |
| 规则集中执行组的支持 | 有   | 无   |
| 规则流中所有节点向导式条件与动作配置的支持 | 有   | 无   |
| 循环规则多循环单元支持 | 有   | 无   |
| 循环规则中无条件执行的支持 | 有   | 无   |
| 导入项目自动重命名功能 | 有   | 无   |
| 规则树构建优化 | 有   | 无   |
| 对象查找索引支持 | 有   | 无   |
| 规则树中短路计算的支持 | 有   | 无   |
| 规则条件冗余计算缓存支持 | 有   | 无   |
| 基于方案的批量场景测试功能 | 有   | 无   |
| 知识包调用监控 | 有   | 无   |
| 更为完善的文件读写权限控制 | 有   | 无   |
| 知识包版本控制 | 有   | 无   |
| SpringBean 及 Java 类的热部署 | 有   | 无   |
| 技术支持 | 有   | 无   |

## 三、安装使用

实际使用时，有四种使用 URule Pro 的方式，分别是嵌入式模式、本地模式、分布式计算模式以及独立服务模式。

但是我们这里不考虑 URule Pro，咱自己整个开源版，在开源版集成 springboot 的基础上做一个二次开发，搜了一圈，其实就有解决方案。

大致的项目模块如下：

![项目模块结构](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/513240756ff760830c907bc7841370b1_MD5.webp)

项目模块结构

自己创建个空数据库，只需要在 edas-rule-server 服务中修改下数据库的配置，然后启动服务即可。第一次启动完成，数据库中会创建表。

```
            spring.datasource.type=com.alibaba.druid.pool.DruidDataSource
          

            spring.datasource.driver-class-name=com.mysql.jdbc.Driver
          

            spring.datasource.url=jdbc:mysql://localhost:3306/urule-data?serverTimezone=Asia/Shanghai&useUnicode=
          true&characterEncoding=utf-8&allowMultiQueries=true&useSSL=false

            spring.datasource.username=root](http://spring.datasource.username=root
          

            spring.datasource.password=mysql
```

上面说过，它是纯用浏览器进行编辑，配置规则的，只需要打开浏览器，输入地址：http://localhost:8090/urule/frame，看到这个界面，就说明启动成功了。

![URule 启动成功界面](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/8627f54186dddd0d05109ccbc1941795_MD5.webp)

URule 启动成功界面

  

## 四、基础概念

### 3.1 整体介绍

先说下 URule 它的构成部分，主要是两部分：1、设计器部分 2、规则执行引擎。设计器部分主要是库文件和规则文件构成。下面看下整体的结构图

![URule 整体结构图](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/897ef9f0f404dc64241632244e77c0a6_MD5.webp)

URule 整体结构图

### 3.2 库文件

如上图介绍的，库文件有 4 种，包括变量库，参数库，常量库和动作库。其实类似于 Java 开发的系统中的实体对象，枚举，常量以及方法。

上面说过，规则都是可视化配置的。在配置规则的过程中，就需要引入各种已经定义好的库文件，再结合业务需求，从而配置出符合业务场景的业务规则，所以哪里都有库文件的身影。



#### 3.2.1 变量库文件

在业务开发中，我们会创建很多 Getter 和 Setter 的 Java 类，比如 PO、VO、BO、DTO、POJO 等等，其实这些类 new 对象后主要起到的作用就是数据的载体，用来传输数据。

在 URule 中，变量库就是用来映射这些对象，然后可以在规则中使用，最终完成业务和规则的互动。最后上一张图，用来创建变量库

![创建变量库](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/d6d9a0d2db596c0b22629d426dd8898d_MD5.webp)

创建变量库

对了，上面废话了这么多可视化配置，这才是第一次展示配置界面，惭愧惭愧。

上图一目了然，在"库"这个菜单底下右键，然后点击添加变量库即可，最后定义自己喜欢的变量库名，当然名字只支持中文或者英文，其他字符不可用。

![变量库命名](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/70ee15bfb290554eddff322a95aeb1b3_MD5.webp)

变量库命名

创建完变量库后，就可以对变量库进行编辑，可以认为就是给 POJO 添加属性

![编辑变量库属性](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/96d14b991c732bc82a469a6659a47274_MD5.webp)

编辑变量库属性

也不弯弯绕绕讲什么术语，就个人理解。图左边是创建类，其中名称是它的别名，配置规则用它代替这个类。图右边是类的属性，我这里随便写了几个，估计看了懂得都懂。

最后在业务系统中创建对应的类，注意全限定名和配置变量库的类路径一致。

```
package com.cicada;

import com.bstek.urule.model.Label;
          
import lombok.Data;
          

/**
  *  @author  往事如风
  *  @version  1.0
  *  @date  2023/3/3 15:38
  *  @description
  */
@Data
publicclassStu{

        @Label("姓名")
        private  String name;

        @Label("年龄")
        privateint  age;

        @Label("班级")
        private  String classes;
}
```

最后说下这个 `@Label` 注解，这个是由 URule 提供的注解，主要是描述字段的属性，跟变量库的标题一栏一致就行。听官方介绍可以通过这个注解，实现 POJO 属性和变量库属性映射。就是 POJO 写好，然后对应规则的变量库就不需要重新写，可以直接生成。反正就有这个功能，这里就直接一笔带过了。

#### 3.2.2 常量库文件

说到常量库，这个就可以认为是我们 Java 系统中的常量，枚举。比如性别，要定义枚举吧；比如对接的机构，也可以定义一个枚举吧。

当然，类似于变量库，常量库也可以实现和系统中的枚举相互映射，这样做的好处可以避免我们手动输入，防止输入错误。创建常量库也比较简单，直接在"库"这个菜单下右键，"添加常量库"。

创建好常量库文件后，也会出现如下页面：

![常量库编辑页面](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/2c8d4a674e731d8d2ab4baa7852a83ec_MD5.webp)

常量库编辑页面

#### 3.2.3 参数库文件

参数库，就是 URule 规则中的临时变量，变量的类型和数量不固定。可以认为类似于 Map，实际上存储参数库的也就是个 Map。

同样的套路，直接在"库"这个菜单下右键，"添加参数库"。

![参数库编辑页面](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/dd25fb83869ae04cb18e40f9851cc258_MD5.webp)

参数库编辑页面

可以看到，参数库已经少了左边分类这一项，直接添加参数，选择类型就是干，相对简单了很多。"名称"这列我这里用了英文，就是 Map 中的 key，而"标题"这列就是在配置规则时候显示用的，中文看着比较直观。

> “
> 
> 当然还需要注意的点是，定义的名称要保证唯一，因为 Map 中的 key 是唯一的，不然就会存在覆盖的情况。

#### 3.2.4 动作库文件

动作库可以对配置在 spring 中的 bean 方法进行映射，然后可以在规则中直接调用这批方法。惯用套路，还是在"库"菜单下右键，点击"添加动作库"。

![动作库编辑页面](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/24a4941fb2f87533343a318f424399f0_MD5.webp)

动作库编辑页面

然后我在系统中添加了一个类 `Action`，然后在类上标记 `@Component` 注解，将该类交给 spring 的 bean 容器管理。该类中添加一些方法，在方法上标记 `@ExposeAction` 注解，该注解是 URule 定义的，说明被标记的方法都会被动作库读取到。

```
package com.bstek.urule.cicada;

import com.bstek.urule.action.ActionId;
import com.bstek.urule.model.ExposeAction;
import org.springframework.stereotype.Component;

import java.text.SimpleDateFormat;
import java.util.Date;

/**
 * @author 往事如风
 * @version 1.0
 * @date 2023/3/10 13:59
 * @description
 */
@Component("action")
public class Action {

    @ActionId("Hello")
    public String hello() {
        return "hello";
    }

    @ExposeAction(value = "方法1")
    public boolean evalTest(String username) {
        if (username == null) {
            return false;
        } else if (username.equals("张三")) {
            return true;
        }
        return false;
    }

    @ExposeAction(value = "测试Int")
    public int testInt(int a, int b) {
        return a + b;
    }

    @ExposeAction(value = "打印内容")
    public void printContent(String username, Date birthday) {
        SimpleDateFormat sd = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        if (birthday != null) {
            System.out.println(username + "今年已经" + sd.format(birthday) + "岁了!");
        } else {
            System.out.println("Hello " + username);
        }
    }

    @ExposeAction(value = "打印Stu")
    public void printUser(Stu m) {
        System.out.println("Hello " + m.getName() + ", is age:" + m.getAge());
    }
}
```

最后在动作库页面上添加 bean，"Bean Id"一列输入对应的 spring bean 的名称，这里输入 action。然后点击操作列中的小手按钮，就会弹出刚在 `Action` 类中标记了 ExposeAction 注解的方法。选择一个指定的方法添加进来，最后看到方法对应的参数也会被自动加载进去。

![动作库方法加载](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/cc813604866c62ffd21c2a35c7e20006_MD5.webp)

动作库方法加载

![动作库方法参数](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/739847a20322fba454e34ce239f9cc8e_MD5.webp)

动作库方法参数

最后，变量库、参数库、动作库、常量库这些库文件定义好后，各种规则文件配置的时候就可以导入他们。但是一旦这些库文件被某个规则文件使用，就不要随意修改库文件了。

### 3.3 规则集

说到规则集，顾名思义，就是配置规则了。前面定义的库文件就需要导入到规则集中去配置使用。它是使用频率最高的一个业务规则实现方式。

规则集说的是规则的集合，由三个部分规则组成：如果、那么、否则。

在规则集的定义的方式上，URule 由向导式和脚本式两种；

* **向导式规则集**：就是在页面上通过鼠标点点点，高度的可视化配置，不是开发都能懂，这也是这个规则引擎的亮点所在。
  
* **脚本式规则集**：听名字就知道了，这玩意要写脚本的。拉高配置门槛，需要懂点编码的人来编写。
  

#### 3.3.1 向导式规则集

还是一样，首先新建。这次是在"决策集"菜单上右键，点击"添加向导式决策集"，这样就创建好一个规则集了。

![添加向导式决策集](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/6731e9c83830ad3d8574801c70bcfd25_MD5.webp)

添加向导式决策集

在配置规则前，可以先导入前面定义好的库文件。我这里导入变量库文件，页面上点击"变量库"，然后选择指定的变量库文件即可。如图所示；

![导入变量库文件](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/b69c6b6c4372fb391237542e165a9706_MD5.webp)

导入变量库文件

最后，可以愉快的配置规则了，向导式没什么好讲的，都是可视化界面，点点点即可。下面是我配置的一个简单的规则集；

![向导式规则集配置](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/bdbbe2bfc47fc1e35fa96348eea345bd_MD5.webp)

向导式规则集配置

可以看到由三部分组成：如果、那么、否则；

1.  **如果**：配置规则的条件；
    
2.  **那么**：配置满足条件后执行的动作，一般配置变量赋值比较多
    
3.  **否则**：配置不满足条件执行的动作
    

最后，附上添加完规则后，通过代码去执行规则；

```
package com.cicada;

  import cn.hutool.core.bean.BeanUtil;
  import com.Result;
  import com.bstek.urule.Utils;
  import com.bstek.urule.runtime.KnowledgePackage;
  import com.bstek.urule.runtime.KnowledgeSession;
  import com.bstek.urule.runtime.KnowledgeSessionFactory;
  import com.bstek.urule.runtime.service.KnowledgeService;
  import com.cicada.req.StuReq;
  import org.springframework.web.bind.annotation.PostMapping;
  import org.springframework.web.bind.annotation.RequestBody;
  import org.springframework.web.bind.annotation.RequestMapping;
  import org.springframework.web.bind.annotation.RestController;

  import java.io.IOException;

  /**
   * @author 往事如风
   * @version 1.0
   * @date 2023/3/10 16:47
   * @description 规则引擎数据控制器
   */
  @RestController
  @RequestMapping("/rule")
  public class RuleDataController {

      @PostMapping("/stu")
      public Result rule(@RequestBody StuReq stuReq) throws IOException {
          KnowledgeService knowledgeService = (KnowledgeService)
  Utils.getApplicationContext().getBean(KnowledgeService.BEAN_ID);

          KnowledgePackage knowledgePackage = knowledgeService.getKnowledge("xxx/xxx");
          KnowledgeSession knowledgeSession =
  KnowledgeSessionFactory.newKnowledgeSession(knowledgePackage);

          Stu stu = BeanUtil.copyProperties(stuReq, Stu.class);

          knowledgeSession.insert(stu);
          knowledgeSession.fireRules();

          return Result.success(stu.getTeacher());
      }
  }
```

![规则执行结果](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/8cc3204d8106c17a3d31d84e9abcc8b0_MD5.webp)

规则执行结果

请求接口，最终参数符合配置的条件，返回"那么"中配置的输出结果。

#### 3.3.2 脚本式规则集

脚本式的规则集，各种原理都是和向导式一模一样，无非就是拉高门槛，用写脚本的方式去实现配置的规则。这里不做过多的介绍了。

### 3.4 决策表

再聊下决策表，其实它就是规则集的另一种展示形式，比较相对规则集，我更喜欢用决策表去配置规则，应为它呈现的更加直观，更便于理解。但是本质和规则集没啥区别。

也不展开过多的赘述，这里我就放一张配置过的决策表；

![决策表配置示例](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/a17c881393fc1e6cb83212bbb028c0a0_MD5.webp)

决策表配置示例

### 3.5 其他

当然，还有其他的概念和功能，这里也不一一介绍了，因为上面说的已经是最常用的了，想了解的可以自行去了解。其他功能包括：交叉决策表、评分卡、复杂评分卡、决策树、规则流；当然，其中有些是 Pro 版的功能。

## 四、运用场景

最近在开发一期大版本的需求，其中就有个场景，具体如下；参与购买订单的用户都会有自己的一个职级，也可以说是角色。每个用户都会有三个职位：普通用户、会员、精英会员。

然后，每个月初都会对用户进行一次晋升处理，普通用户达到要求，就会晋升为会员，会员达到要求就会晋升为精英会员。

当然，普通用户晋升会员，会员晋升精英会员，都会有不同的规则；

1.  普通用户->会员：3 个月内帮注册人数达到 3 人；3 个月内自己和底下团队的人，下单金额超过 1 万；个人的订单继续率超过 80%。
    
2.  会员->精英会员：3 个月内帮注册人数达到 6 人；3 个月内自己和底下团队的人，下单金额超过 5 万；个人的订单继续率超过 90%。
    
3.  不能跨级晋升，普通用户最多只能到会员，达到会员了才能晋升到精英会员。
    

> “
> 
> 当然，这只是做过简化的一部分需求，我做过稍许的改动，真实的需求场景并没有这么简单。

下面，我对这个需求做一个规则的配置，这里用一个决策表进行配置；在配置规则前，我添加一个变量库文件和常量库；

![运用场景-变量库配置](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/fa723c8370c6a9076554e37453a7d8e5_MD5.webp)

运用场景-变量库配置

![运用场景-常量库配置](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/0545ab3698253815a8e3004108fd83b7_MD5.webp)

运用场景-常量库配置

最后，添加一个决策表，并进行规则配置；

![运用场景-决策表配置](assets/Spring%20Boot%20+%20URule%20%E5%AE%9E%E7%8E%B0%E5%8F%AF%E8%A7%86%E5%8C%96%E8%A7%84%E5%88%99%E5%BC%95%E6%93%8E/f674b14e753d21ca8206a4ad2f2405e9_MD5.webp)

运用场景-决策表配置

可以看到，表格一共五列，其中前四列是规则，最后一列是满足规则后输出的信息。这样看着就很清晰，即使并不是技术人员，也可以轻松看懂其中的规则。

## 五、总结

规则引擎对于我们的系统而言可用可不用，它可以锦上添花，帮助我们剥离出业务中需要进行大量判断的场景。但是，这种规则的剥离，需要我们开发人员对需求进行理解，在理解的基础上进行抽象概念的具化。这，也是整个编程的**必经之路**。

