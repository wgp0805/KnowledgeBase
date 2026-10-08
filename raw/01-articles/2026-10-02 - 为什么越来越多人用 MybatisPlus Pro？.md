---
source_url: "https://mp.weixin.qq.com/s/3qPngax74IhPQQ-kbnic6g"
title: "为什么越来越多人用 MybatisPlus Pro？"
account: "苏三说技术"
published_at: "2026-10-02 09:20:00"
saved_at: "2026-10-02 09:56:37"
sync_id: "art_32868a1363844fe89817ec4640cbbf31"
parse_status: "ok"
---

# 为什么越来越多人用 MybatisPlus Pro？

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐14个牛逼的SpringBoot项目](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247536010&idx=1&sn=69cbb5fdfc59c9c636559fb556386b24&scene=21#wechat_redirect)

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

说到MyBatis，很多小伙伴都会用，但未必用得“惊艳”。

这个轻量级的持久层框架虽然灵活，但在日常的单表CRUD操作上，不得不面对**重复代码多、开发效率低**的现实问题。

我们来看一个典型的场景：

```
// 原生MyBatis：每个实体都要写XML，每个方法都要配SQL
<mapper namespace="com.example.UserMapper">
    <select id="selectById" resultType="User">
        SELECT * FROM user WHERE id = #{id}
    </select>
    <insert id="insert" useGeneratedKeys="true" keyProperty="id">
        INSERT INTO user(name, age) VALUES(#{name}, #{age})
    </insert>
    <update id="updateById">
        UPDATE user SET name = #{name}, age = #{age} WHERE id = #{id}
    </update>
    <delete id="deleteById">
        DELETE FROM user WHERE id = #{id}
    </delete>
    <!-- 还有分页、列表、批量... 无穷无尽 -->
</mapper>
```

最近有位小伙伴反馈说：“苏三哥，为什么一个简单的用户表，我要写一百多行的XML？单表操作不就是增删改查和分页吗，能不能一行代码搞定？”

说实话，听到这话我一点都不意外。

当年我们使用传统MyBatis时，第一反应也是一样的。

但用了MybatisPlus一段时间，发现它把我们从XML地狱里解救出来，确实爽。

不过日子久了，又开始觉得不够用了，每个接口还得写个Controller、Service、ServiceImpl……虽然比MyBatis强了不少，但还是有不少重复劳动。

直到最近，我深度体验了基于MybatisPlus抽取的 **MybatisPlus Pro**——只需继承一个BaseController，增删改查、分页、列表、排序、条件查询，全部开箱即用。

今天这篇文章就专门跟大家一起聊聊MybatisPlus Pro，希望对你会有所帮助。

## 一、为什么我们需要MybatisPlus Pro？

在深入讲解之前，我们先来盘点一下日常开发中那些“看似能忍、实则很烦”的场景。

**痛点1：MybatisPlus的BaseMapper已经很方便了，但Service层还得重复写。**

每个Service接口基本都是在定义findById、findAll、insert、update、delete等通用方法。

虽然MP提供了IService接口，但依然需要在每个ServiceImpl里调用BaseMapper的方法，没有从根本上解决**重复劳动的底层逻辑**。

**痛点2：Controller层还是得写。**

很多小伙伴在工作中可能有这样的经历：需求方说要加一个新模块，需要做一套完整的增删改查接口。

咱们开始复制粘贴，改类名、改路径、改参数……搞完一两个模块还没啥，等需求方一次性提了七八个模块的需求时，光写这些“复制-粘贴-微调”的代码就要一两个小时，而且极其容易出错。

**痛点3：代码质量参差不齐。**

同样的增删改查，张三这样写，李四那样写。

有的参数校验做得严丝合缝，有的漏了异常处理，线上直接报错。

**痛点4：条件查询代码重复率高。**

每个Controller里都要对QueryWrapper进行各种eq、like、orderBy的配置，逻辑极其相似，写多了就会看到大量的重复代码。

有一句话说得好：**最好的代码是没有代码。**

如果能把这些几乎一模一样的代码全部自动化生成，我们就能把90%的精力释放出来，投入到真正的业务逻辑里去。

## 二、MybatisPlus Pro是什么？

**MybatisPlus Pro是在MybatisPlus的基础上进行增强的工具**，它的核心理念是“站在巨人的肩膀上”，只做增强不做改变。

从项目结构上看，MybatisPlus Pro就是在MybatisPlus的基础上增加更多的模板功能，利用Spring Boot进行开发，将通用功能抽取出来，形成一套开箱即用的基类体系。

说白了，MybatisPlus Pro的核心思路就是：**在MybatisPlus已经“消灭”了Mapper层代码的基础上，继续“消灭”Service层和Controller层的重复代码**，让开发者只需要关注核心的业务逻辑。

> 这里需要说明一下，MybatisPlus Pro目前有两种理解：一种是社区基于MP二次封装的项目实现方案（就像富贵同学那个版本），另一种是MybatisPlus官方在不断迭代中新增的Pro级特性。本文重点围绕前者的设计思路和实战价值展开。

下面，我从架构师视角给大家画一张架构图，方便理解MyBatis、MybatisPlus和MybatisPlus Pro这三者之间的关系：

![](assets/2026-10-02%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20MybatisPlus%20Pro%EF%BC%9F/724bbd3ce087a03729ba3f8846ea58a8_MD5.jpg)

## 三、快速上手

说了这么多理论，咱们直接上代码，感受一下Pro版的威力。

### 第一步：引入依赖

MybatisPlus Pro建立在MybatisPlus基础上，所以首先要引入MybatisPlus的starter依赖：

```
<dependency>
    <groupId>com.baomidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>3.5.15</version>
</dependency>
```

> 官方在2025年11月30日发布了v3.5.15版本，支持SpringBoot 4.0.0和Jackson 3.0，推荐使用最新的稳定版本。

### 第二步：编写工具类

工具类是Pro版的核心基础设施，它提供了三个关键功能：

- 驼峰与下划线的互相转换 ——解决Java实体类字段名和数据库列名的自动映射问题
- 通过反射获取实体字段值 ——动态提取实体中各字段的值，为构建QueryWrapper做准备
- 基于实体类自动生成QueryWrapper ——零代码构建查询条件，大大简化条件查询的编写

这里的关键逻辑需要详细讲一下：当一个实体对象（比如User对象）传入getQueryWrapper方法时，这个方法会通过Java反射获取这个类的所有声明的字段（用entity.getClass().getDeclaredFields()获取）。

然后遍历每一个字段，跳过那些被final修饰的字段（因为这些字段不能动态修改），再通过field.setAccessible(true)突破Java的访问权限限制，获取被private修饰的字段值。

如果字段值不为null，就把Java的驼峰字段名（如userName）转换成数据库的下划线列名（user_name），然后向QueryWrapper添加一个eq（等值匹配）条件。

这样一来，我们传入的实体里有哪些非空字段，QueryWrapper就自动用这些字段作为查询条件，完全不需要手动编写。

```
public class ApprenticeUtil {
    privatestatic Pattern humpPattern = Pattern.compile("[A-Z]");
    privatestatic Pattern linePattern = Pattern.compile("_(\\w)");

    // 驼峰转下划线（userName -> user_name）
    public static String humpToLine(String str) {
        Matcher matcher = humpPattern.matcher(str);
        StringBuffer sb = new StringBuffer();
        while (matcher.find()) {
            matcher.appendReplacement(sb, "_" + matcher.group(0).toLowerCase());
        }
        matcher.appendTail(sb);
        return sb.toString();
    }

    // 下划线转驼峰（user_name -> userName）
    public static String lineToHump(String str) {
        str = str.toLowerCase();
        Matcher matcher = linePattern.matcher(str);
        StringBuffer sb = new StringBuffer();
        while (matcher.find()) {
            matcher.appendReplacement(sb, matcher.group(1).toUpperCase());
        }
        matcher.appendTail(sb);
        return sb.toString();
    }

    // 根据非空字段生成QueryWrapper——这里是核心
    publicstatic <E> QueryWrapper<E> getQueryWrapper(E entity) {
        Field[] fields = entity.getClass().getDeclaredFields();
        QueryWrapper<E> eQueryWrapper = new QueryWrapper<>();
        for (Field field : fields) {
            // 忽略final字段
            if (Modifier.isFinal(field.getModifiers())) {
                continue;
            }
            field.setAccessible(true);
            try {
                Object obj = field.get(entity);
                if (obj != null) {
                    String name = humpToLine(field.getName());
                    eQueryWrapper.eq(name, obj);
                }
            } catch (IllegalAccessException e) {
                returnnull;
            }
        }
        return eQueryWrapper;
    }
}
```

### 第三步：编写通用BaseController

BaseController是整个Pro版的“发动机”，它集成了最核心的CRUD操作逻辑：

```
public class BaseController<S extends IService<T>, T> {
    @Autowired
    protected S baseService;

    @PostMapping("add")
    public Result add(@RequestBody T entity) {
        return Result.success(baseService.save(entity));
    }

    @PostMapping("update")
    public Result update(@RequestBody T entity) {
        return Result.success(baseService.updateById(entity));
    }

    @GetMapping("delete")
    public Result delete(String id) {
        return Result.success(baseService.removeById(id));
    }

    @GetMapping("detail")
    public Result detail(String id) {
        return Result.success(baseService.getById(id));
    }

    @PostMapping("list")
    public Result list(@RequestBody T entity) {
        // 利用工具类自动构建查询条件
        QueryWrapper<T> wrapper = ApprenticeUtil.getQueryWrapper(entity);
        if (wrapper == null) {
            wrapper = new QueryWrapper<>();
        }
        return Result.success(baseService.list(wrapper));
    }

    @PostMapping("page")
    public Result page(@RequestBody PageDto<T> pageDto) {
        T entity = pageDto.getEntity();
        QueryWrapper<T> wrapper = ApprenticeUtil.getQueryWrapper(entity);
        if (wrapper == null) {
            wrapper = new QueryWrapper<>();
        }
        IPage<T> page = new Page<>(pageDto.getPageNo(), pageDto.getPageSize());
        return Result.success(baseService.page(page, wrapper));
    }
}
```

这段代码的底层执行逻辑值得详细剖析。

当客户端通过 `/add` 接口发送POST请求时，Spring框架自动将JSON格式的请求体解析为T类型的实体对象。

然后baseService.save(entity)被调用，baseService实际上是MybatisPlus的IService接口的实现类，它内部持有一个BaseMapper。

save方法会自动判断：如果主键为null，执行insert插入操作；如果主键不为null，执行updateById更新操作。

MybatisPlus在应用启动时就会自动向Mapper中注入这些基本的CRUD操作，所以不需要我们写一行SQL。

**这里特别说一下 `list` 方法**：参数是T类型实体，方法内部直接用ApprenticeUtil.getQueryWrapper(entity)自动构建QueryWrapper。

比如前端传入一个只有name为“张三”的User对象（其他字段为null），那么框架会自动生成 `WHERE name = '张三'` 的查询条件。

所有非空字段都会被纳入查询条件，自动取交集。

这就实现了一个强大的能力—— **给什么字段查什么字段，完全零代码**！

### 第四步：实际使用

搞定了BaseController，我们再来创建一个ProductController，看看代码量能减少多少：

```
// 实体类
@Data
@TableName("product")
publicclass Product {
    @TableId(type = IdType.AUTO)
    private Long id;
    private String name;
    private BigDecimal price;
    private Integer stock;
    private LocalDateTime createTime;
}

// Service接口
publicinterface ProductService extends IService<Product> {
}

// Service实现（按常规写法，也可以自动生成）
@Service
publicclass ProductServiceImpl extends ServiceImpl<ProductMapper, Product> implements ProductService {
}

// Controller——就这一行！
@RestController
@RequestMapping("/product")
publicclass ProductController extends BaseController<ProductService, Product> {
}
```

你没看错，**创建一个完整CRUD的Controller只需要继承BaseController**。

增删改查、分页、列表……这些接口全部自动生成，一条代码都不用写！

## 四、底层原理深度剖析

很多小伙伴可能会好奇：BaseController里的这些方法是如何知道要对哪张表操作的呢？

为什么我写一个方法，对应的SQL就自动生成了？

这个问题的答案藏在MybatisPlus的底层执行链路里。

### 4.1 完整的SQL执行链路

我们用一张清晰的流程图来展示从Controller调用到数据库返回结果的全过程：

![](assets/2026-10-02%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20MybatisPlus%20Pro%EF%BC%9F/17d9b73573d50eef18b70cdc42b1f6f3_MD5.jpg)

### 4.2 重点剖析：BaseMapper的注入机制

这里我来重点讲一下MybatisPlus的核心魔法是如何实现的。

很多小伙伴可能每天都在用BaseMapper，但从来没想过它是怎么生效的。

先回顾一下MyBatis的核心流程：MyBatis通过SqlSessionFactoryBuilder读取mybatis-config.xml配置文件，构建SqlSessionFactory，再由SqlSessionFactory创建SqlSession，每次操作数据库都通过SqlSession完成。

MyBatis底层自定义了Executor执行器接口来操作数据库，Executor有两个主要实现：一个是基本执行器（SimpleExecutor），一个是缓存执行器（CachingExecutor）。

MybatisPlus的强大之处在于它在这个基础上做了增强：

**1. 动态代理机制**：在Spring启动时，所有继承了BaseMapper的接口都会被MapperProxyFactory使用JDK动态代理创建代理对象。当你调用productMapper.selectById(1L)时，实际上调用的是MapperProxy的invoke方法，这个方法会拦截你的接口调用，分析出你要执行的是一个名为selectById的查询操作。

**2. MappedStatement的自动生成**：MybatisPlus的SQL注入器（SqlInjector）会在应用启动时，为BaseMapper中的所有通用方法生成对应的MappedStatement。

**MappedStatement是MyBatis的底层封装对象，它包含了SQL模板、参数类型、返回结果类型等完整的SQL执行信息**，mapper.xml文件中一个SQL操作就对应一个MappedStatement。

MP在启动时自动将这些SQL注入到MyBatis的Configuration中，这就是为什么我们不需要写任何XML就能执行SQL的原因。

**3. 拦截器链（Interceptor Chain）** ：MybatisPlus通过MybatisPlusInterceptor构建了一个拦截器链，在Executor执行前注入各种增强逻辑，比如分页、乐观锁、多租户等，这些功能都是通过拦截器和责任链模式来实现的。

**4. 完整的方法解析机制**：当你的Mapper接口调用通用方法时，MybatisPlus能知道这是一个通用方法还是自定义方法，并找到对应的MappedStatement来执行SQL。

### 4.3 条件构造器（Wrapper）的工作原理

以条件查询为例，下面是条件构造器内部执行的详细流程：

![](assets/2026-10-02%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20MybatisPlus%20Pro%EF%BC%9F/f145ccdf3c40d48dc4859de2ae62740d_MD5.jpg)

Lambda表达式的核心优势是类型安全——使用 `User::getName` 而不是字符串 `"name"` ，如果字段名写错了，编译器立刻就会报错，而传统的字符串写法只有到运行时才会发现SQL错误，这是技术上对“约定优于配置”理念的一种实现。

## 五、优缺点

### 5.1 优点

**1. 开发效率呈指数级提升**一个模块从接口定义到CRUD功能完整可用，只需要继承BaseController并注入Service，5行代码搞定。相比原生MyBatis要写XML、Mapper、Service、ServiceImpl、Controller，工作量减少80%以上。

**2. 代码风格统一，降低维护成本**所有模块的增删改查逻辑全部来自同一个BaseController，代码风格完全一致。新人接手项目时，不需要去研究每个Controller用了什么技巧——所有的结构和处理方式都一样。

**3. 零XML配置**MybatisPlus本身已经做到了不需要XML配置BaseCRUD，而Pro版进一步把Controller层的配置也省掉了。

**4. 功能完备，开箱即用**分页插件已经内置，只需要传pageNo和pageSize就可以获得完整的分页查询结果。条件构造器可以灵活构建复杂的查询条件，比如eq（等于）、like（模糊匹配）、between（范围查询）、orderBy（排序）等，可以满足绝大多数业务场景的需求。

**5. 非侵入式设计**MybatisPlus Pro是在MybatisPlus基础上做的增强，你仍然可以在需要复杂SQL的地方编写原生MyBatis的Mapper和XML，两者完全兼容。

### 5.2 缺点

**1. 复杂多表关联查询仍然是痛点**一旦涉及三张表以上的关联查询，条件构造器会让代码变得非常复杂和难以阅读。有经验的小伙伴应该能体会到：用Wrapper写三表关联，代码的逻辑可能比写SQL还要绕。原因在于Wrapper本身设计是用来构建单表查询条件的，它并不擅长处理多表JOIN的语义表达。

**2. 部分场景存在性能隐患**需要特别注意的是，BaseMapper自带的selectById、selectList等方法默认会查询所有字段——相当于SQL中的 `SELECT *` 。在MySQL性能优化中，有一条黄金法则：不要使用 `SELECT *` ，因为这会增加不必要的网络传输和内存开销，尤其是当表中包含TEXT、BLOB这类大字段时，性能问题更加明显。

官方在使用说明中也提醒：MP会对启动即自动注入基本CRUD操作，性能损耗虽然极小，但在极端场景下需要谨慎考量。

**3. 一些方法存在魔法值隐患**比如使用 `QueryWrapper<User>().eq("id", 1)` 这种方式，字段名是以字符串形式写死的。如果数据库字段名改了，编译阶段根本无法发现，只有运行到那一行代码时才会报错，排查起来非常耗时。这也是为什么官方越来越推崇LambdaWrapper的原因——用方法引用代替字符串，从根本上解决这个问题。

**4. 部分功能有过度封装之嫌**有开发者认为MP一定程度上“侵入”了Service层，当业务逻辑变得非常复杂时，这些封装好的通用方法反而可能成为限制。

**5. SQL可读性和调优难度增加**当使用复杂的条件构造器时，生成的SQL语句对调试来说不够直观。如果不熟悉MP的内部机制，定位慢查询的原因会比直接看XML配置的SQL更困难。

## 六、使用场景与选型建议

### 6.1 推荐使用MybatisPlus Pro的场景

**场景1：中小型项目、快速迭代项目**这类项目的特点是需求变化快，对开发速度要求高，但对极致性能要求相对较低。使用MybatisPlus Pro可以大幅提升开发效率。

**场景2：后台管理系统、管理后台类应用**这些应用的核心功能就是围绕数据的增删改查，模块数量多、业务逻辑相对简单。Pro版特别适合这类场景。

**场景3：基础CRUD操作占主导的项目**如果项目中80%以上都是单表增删改查操作（比如各种配置管理、字典管理、基础数据维护），Pro版能带来巨大的效率提升。

**场景4：开发团队规模较小，希望统一代码风格**小团队或者个人开发者，用Pro版可以快速搭建项目，同时保证代码结构清晰统一。

### 6.2 谨慎使用或不推荐的场景

**场景1：业务核心、对SQL执行效率要求极高的系统**比如交易系统、支付系统、高并发的订单系统等，需要对每一条SQL的性能做极致调优。MP的通用方法（尤其是 `SELECT *` ）可能会成为性能瓶颈。

**场景2：复杂报表系统、复杂数据统计系统**这类系统往往需要编写十几行甚至几十行的复杂SQL，多表关联、子查询、聚合函数比比皆是。这种情况下，直接编写原生SQL比使用条件构造器更清晰、更可控。

**场景3：对SQL需要精细审核的安全敏感系统**在一些金融、政务等对SQL语句需要逐条审查的场景下，框架自动生成的SQL可能不太符合审核要求。此时建议全部使用手写的XML SQL。

### 6.3 架构选型时的对比参考

下面这张表帮大家快速理清MyBatis、MybatisPlus和MybatisPlus Pro之间的差异，做到“选型有据”：

| 维度 | 原生MyBatis | MybatisPlus | MybatisPlus Pro |
| --- | --- | --- | --- |
| ** CRUD开发速度 ** | 慢（需手写SQL） | 快（BaseMapper） | 极快（全自动） |
| ** 代码量 ** | 多 | 较少 | 很少 |
| ** 多表SQL灵活性 ** | 高（完全可控） | 高（兼容原生） | 高（兼容原生） |
| ** 学习成本 ** | 低 | 中等 | 中等 |
| ** 定制化程度 ** | 高 | 高 | 中高 |
| ** 统一代码风格 ** | 差 | 一般 | 好 |
| ** 适用项目 ** | 所有 | 所有 | 中大型+快速开发 |
| ** 对数据库的掌控力 ** | 完全掌控 | 单表可封装 | 单表可封装 |

> 这个对比表帮大家在技术选型时做到心里有数——每个框架都有自己的优势和局限，关键是根据项目的实际情况来做选择。

## 七、避坑指南

作为过来人，我踩过不少坑，下面分享几点实战经验：

**坑1：不要过度使用通用查询方法**

有小伙伴在工作中喜欢“一个selectList走天下”，这样虽然方便，但遇到高频查询的接口时， `SELECT *` 查询所有字段会严重影响性能。建议重要的查询接口一定要用select()指定字段。

**坑2：Lambda版本优先于字符串版本**

使用LambdaQueryWrapper代替QueryWrapper，通过方法引用的方式避免硬编码字符串，既保证了类型安全，又避免了字段名变更时的隐式错误。

```
// ✅ 推荐写法（类型安全）
userMapper.selectList(Wrappers.<User>lambdaQuery()
    .eq(User::getStatus, 1)
    .like(User::getUsername, "zhang")
    .orderByDesc(User::getCreateTime));

// ❌ 不推荐写法（字符串容易拼错）
userMapper.selectList(Wrappers.<User>query()
    .eq("status", 1)
    .like("username", "zhang"));
```

**坑3：分页一定要用MybatisPlus的分页插件**

不要自己写LIMIT，MybatisPlus内置的分页插件基于物理分页，对不同数据库提供了良好的兼容性，不仅代码简洁，性能也好很多。

**坑4：复杂SQL果断放弃Wrapper，回归原生**

当查询涉及三张表以上的关联时，我的建议是：不要挣扎，直接在Mapper XML里写SQL。清晰、可控、易于调优，这才是真正的生产力。

**坑5：实体字段命名遵循驼峰规范**

MP的自动映射依赖驼峰命名规范，建议始终使用标准的驼峰命名，避免不必要的配置。

## 总结

写到这里，我们来简单总结一下。

**MybatisPlus Pro的出现，核心目标是解决一个根本问题：把开发者从海量的重复代码中解放出来。**

它继承了MybatisPlus无侵入、高效率的设计理念，通过BaseController这一层巧妙的设计，把Controller层、Service层的重复劳动全部自动化。

配合工具类的反射机制和Wrapper条件构造器，还可以实现基于实体非空字段的自动条件查询——开发体验可以说是质的飞跃。

当然，**没有银弹**。

Pro版在复杂多表关联、极致性能优化等场景下确实存在短板，但正如业界公认的：它解决了80%的简单CRUD重复工作，剩下的20%复杂场景依然能手写SQL，两者结合才是最佳实践。

MyBatis-Plus在MyBatis的基础上只做增强不做改变，既简化了开发，又保留了MyBatis的所有灵活性。

最后，用一句话与所有开发者共勉：**提高效率不是偷懒，而是把精力投入到更有价值的业务中去。**

如果觉得有用，点个在看支持一下！

> - MybatisPlus 官方文档：https://baomidou.com
> - MybatisPlusPro 项目地址：https://gitee.com/nirui-gitee/mybatis-plus-pro

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐14个牛逼的SpringBoot项目](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247536010&idx=1&sn=69cbb5fdfc59c9c636559fb556386b24&scene=21#wechat_redirect)

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

---
原文链接：https://mp.weixin.qq.com/s/3qPngax74IhPQQ-kbnic6g
