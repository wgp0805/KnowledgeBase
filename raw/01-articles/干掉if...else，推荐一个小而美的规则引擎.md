---
title: "干掉if...else，推荐一个小而美的规则引擎"
source: "https://mp.weixin.qq.com/s/7JzJL1CTnTNGVNF2Tlf_Yg"
---
苏三 苏三说技术 *2026年7月2日 08:20*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)

## 前言

最近在做代码Review的时候，发现了一个非常普遍的问题—— **一个业务方法里，if...else叠了七八层，代码行数直接飙到300多行** 。

**业务规则的复杂度，天然就是不断增长的** 。

今天加一个规则，明天改一个规则，后天删一个规则——用if...else硬编码，就是在给自己挖坑。

那有没有什么办法，能把业务规则从代码里 **抽离** 出来，让代码变得干净、可维护、可动态调整？

有。

今天我要介绍的这个工具，就是专门干这个事的—— **Easy Rules** 。

希望对你会有所帮助。

## 一、先看看if...else的“七宗罪”

在正式介绍Easy Rules之前，我们先看一个典型的“if...else地狱”案例：

```
public class DiscountService {
    
    public double calculateDiscount(User user, Order order) {
        double discount = 0.0;
        
        // 规则1：VIP用户打9折
        if (
            user.isVip())
           {
            discount = 0.9;
        }
        
        // 规则2：订单金额超过1000，再打95折
        if (
            order.getAmount()
           > 1000) {
            discount = discount * 0.95;
        }
        
        // 规则3：新用户首单打8折
        if (
            user.isNewUser()
           && 
            user.getOrderCount()
           == 0) {
            discount = 0.8;
        }
        
        // 规则4：双11期间全场9折
        if (isDoubleEleven()) {
            discount = discount * 0.9;
        }
        
        // 规则5：老用户且订单金额超过5000，打85折
        if (!
            user.isNewUser()
           && 
            order.getAmount()
           > 5000) {
            discount = 0.85;
        }
        
        // 规则6：规则7：规则8...
        // 越加越多，代码越来越长
        
        return discount;
    }
}
```

这段代码有什么问题？

**第一，可读性差。** 规则越多，方法越长，谁接手谁想骂人。

**第二，可维护性差。** 改一个规则，要找到对应的if分支，小心翼翼地改，生怕影响到别的逻辑。

**第三，可测试性差。** 要覆盖所有规则组合的测试用例，数量呈指数级增长。

**第四，扩展性差。** 每加一个新规则，就要修改源代码、重新编译、重新部署。

**第五，业务和代码耦合。** 业务人员想调整规则，得求着开发改代码。

**第六，重复逻辑遍地都是。** 同样的条件判断，可能在好几个地方出现。

**第七，** **修改后必须重启服务。** 线上规则调整零活度几乎为零。

> 有些小伙伴可能会说：“这些规则我写个配置表，从数据库里查不就行了？”没错，配置化确实能解决一部分问题。但真正的规则引擎，不只是“把规则存到数据库里”——它还要解决规则的 **组合、优先级、条件评估、自动执行** 等一系列问题。把if...else搬到数据库里，if...else还是if...else，只是换了个地方而已。

那怎么办？

**规则引擎** 就是干这个的。

## 二、Easy Rules是什么？

Easy Rules是一个简单而强大的 **Java规则引擎** ，由 **j-easy** 团队开源维护。

它的设计灵感来源于Martin Fowler提出的“规则引擎”概念。

Martin Fowler在一篇非常经典的文章里说过：

> **“你可以自己构建一个简单的规则引擎。你只需要创建一组具有条件和操作的对象，将它们存储在一个集合中，并运行它们来评估条件并执行操作。”**

Easy Rules做的就是这件事——它提供了 `Rule` 抽象来创建带有条件和操作的规则，以及 `RulesEngine` API来运行一系列规则。

### 2.1 一句话说清Easy Rules

**Easy Rules就是一个“把if...else从代码里搬出来、用规则对象来管理”的工具。**

它让你可以这样定义规则：

```
@Rule(name = "VIP折扣规则", priority = 1)
public class VipDiscountRule {
    @Condition
    public boolean isVip(@Fact("user") User user) {
        return 
            user.isVip();
          
    }
    @Action
    public void applyDiscount(@Fact("order") Order order) {
        
            order.setDiscount(
          0.9);
    }
}
```

然后这样执行：

```
RulesEngine engine = new DefaultRulesEngine();

            engine.fire(rules,
           facts);
```

是不是清爽多了？

### 2.2 核心特点

Easy Rules有以下几个核心特点：

- **轻量级** ：没有复杂的依赖和配置，JAR包仅 **100KB** 左右
- **POJO开发** ：用普通的Java类加注解就能定义规则
- **多种定义方式** ：支持注解、流式API、表达式语言（MVEL/SpEL/JEXL）、YAML/JSON配置
- **复合规则** ：支持将多个简单规则组合成复杂规则
- **易于集成** ：可以轻松集成到Spring Boot等框架中

## 三、核心概念

Easy Rules围绕 **四个核心抽象** 构建：

![图片](https://mmbiz.qpic.cn/mmbiz_png/3SCLUkuu2IFTJNPGafBjr5quGb06Ja6HibMPsZXib9pRJ6Jrp2b4dBvAb4Z6NeVgDwSTqWQbKGwENXW96T21QNvMolIL6g71GG4mpIcNlFl64/640?wx_fmt=png&from=appmsg#imgIndex=0)

### 3.1 Rule（规则）

`Rule` 接口是Easy Rules最核心的抽象。一个规则包含：

- **name** ：规则的唯一名称
- **description** ：规则的简要说明
- **priority** ：规则的优先级（数字越小优先级越高）
- **condition** ：条件——返回 `true` 时触发规则
- **action** ：动作——条件满足时执行的操作
```
public interface Rule {
    boolean evaluate(Facts facts);  // 评估条件
    void execute(Facts facts) throws Exception;  // 执行动作
    // getters for name, description, priority...
}
```

### 3.2 Facts（事实）

`Facts` 是规则执行时的 **数据上下文** ，本质是一个 **键值对容器** 。你把数据放进去，规则从中取数据：

```
Facts facts = new Facts();

            facts.put(
          "user", user);

            facts.put(
          "order", order);

            facts.put(
          "rain", true);
```

### 3.3 Rules（规则集合）

`Rules` 是规则的 **有序容器** ，负责管理一组规则。规则按照 `priority` 自动排序：

```
Rules rules = new Rules();

            rules.register(
          new VipDiscountRule());

            rules.register(
          new NewUserDiscountRule());

            rules.register(
          new DoubleElevenRule());
```

### 3.4 RulesEngine（规则引擎）

`RulesEngine` 是 **执行规则的核心引擎** 。Easy Rules提供了两种实现：

| 引擎类型 | 执行策略 | 适用场景 |
| --- | --- | --- |
| **DefaultRulesEngine** | 按优先级顺序执行，条件满足就执行 | 大多数常规场景 |
| **InferenceRulesEngine** | 前向链推理，反复执行直到没有规则可触发 | 规则之间存在依赖和连锁反应 |

```
// 默认引擎
RulesEngine engine = new DefaultRulesEngine();

            engine.fire(rules,
           facts);
```

## 四、四种规则定义方式

Easy Rules提供了 **四种** 定义规则的方式，你可以根据实际场景灵活选择。

### 4.1 方式一：注解方式（最常用）

**适用场景** ：规则固定、逻辑清晰、大部分常规业务场景。

用 `@Rule` 、 `@Condition` 、 `@Action` 、 `@Fact` 注解来定义规则：

```
@Rule(name = "天气规则", description = "如果下雨就带伞", priority = 1)
public class WeatherRule {
    
    @Condition
    public boolean isRaining(@Fact("rain") boolean rain) {
        return rain;
    }
    
    @Action
    public void takeUmbrella() {
        
            System.out.println(
          "下雨了，记得带伞！");
    }
}
```

**注解说明** ：

- `@Rule` ：标记类为规则，可指定 `name` 、 `description` 和 `priority`
- `@Condition` ：标记条件方法，必须返回 `boolean` ，只能有一个
- `@Action` ：标记动作方法，可以有多个，通过 `order` 指定执行顺序
- `@Fact` ：标记参数，从 `Facts` 容器中按名称取值

执行代码：

```
public class Application {
    public static void main(String[] args) {
        // 1. 准备事实
        Facts facts = new Facts();
        
            facts.put(
          "rain", true);
        
        // 2. 注册规则
        Rules rules = new Rules();
        
            rules.register(
          new WeatherRule());
        
        // 3. 执行引擎
        RulesEngine engine = new DefaultRulesEngine();
        
            engine.fire(rules,
           facts);
        // 输出：下雨了，记得带伞！
    }
}
```

### 4.2 方式二：流式API（动态规则）

**适用场景** ：规则需要动态生成、规则条件在运行时才能确定。

使用 `RuleBuilder` 流式API构建规则：

```
Rule dynamicRule = new RuleBuilder()
    .name("高温预警规则")
    .description("温度超过30度时提醒防暑")
    .priority(2)
    .when(facts -> 
            facts.get(
          "temperature") > 30)
    .then(facts -> 
            System.out.println(
          "天气炎热，注意防暑！"))
    .build();
```

`when()` 方法接收一个 `Predicate<Facts>` ， `then()` 方法接收一个 `Consumer<Facts>` 。这种方式非常适合 **运行时动态生成规则** 的场景。

### 4.3 方式三：表达式语言（最灵活）

**适用场景** ：规则频繁变更、希望非开发人员也能修改规则。

Easy Rules支持 **MVEL、SpEL、JEXL** 三种表达式语言：

```
// 使用MVEL表达式
Rule mvelRule = new MVELRule()
    .name("会员折扣规则")
    .description("会员且订单金额大于100享受9折")
    .when("
            user.vip
           == true && 
            order.amount
           > 100")
    .then("
            order.discount
           = 0.9");
```

表达式语言最大的优势是： **规则可以以字符串形式存储** （数据库、配置文件、管理后台），修改规则 **不需要重新编译和部署** 。

### 4.4 方式四：YAML/JSON配置（配置化）

**适用场景** ：希望把规则完全抽离到配置文件、由业务人员维护。

通过YAML或JSON文件定义规则：

```
# 
            rules.yml
          
-name:"新用户首单折扣"
description:"新用户第一笔订单打8折"
priority:3
condition:"
            user.newUser
           == true && 
            user.orderCount
           == 0"
actions:
    -"
            order.discount
           = 0.8"
```

通过 `MVELRuleFactory` 或 `SpELRuleFactory` 加载配置文件：

```
MVELRuleFactory ruleFactory = new MVELRuleFactory(new YamlRuleDefinitionReader());
Rule rule = 
            ruleFactory.createRule(
          new FileReader("
            rules.yml"
          ));
```

## 五、底层原理

### 5.1 整体架构

Easy Rules的架构可以分为四个层次：

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3SCLUkuu2IGeuzXXMQuxxTcQw0iaSbHk9M6QeJzC8ibHgrpWiarEPzGPpY8QGjRJ0x5MzZf551faWPTj2rx8GsghjuUdkoU1fwLQA9gTmnZj7k/640?wx_fmt=jpeg&from=appmsg#imgIndex=1)

### 5.2 DefaultRulesEngine：执行流程

`DefaultRulesEngine` 是最常用的引擎实现，它的执行流程如下：

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/3SCLUkuu2IFKumHZQrg11po0pXuJsKORtZcaianBxWjx6Zp8535iaIuJXdq2pYJ4tWKeaxyFFKFsp61jlCBdhIVrfoQv04icyYSnj7CzwVNla0/640?wx_fmt=jpeg&from=appmsg#imgIndex=2)

### 5.3 InferenceRulesEngine：前向链推理

`InferenceRulesEngine` 实现了 **前向链推理** 算法。它的核心逻辑是：

1. 进入推理循环
2. 在当前 `Facts` 下，找出所有条件为 `true` 的规则（候选规则）
3. 如果没有候选规则，退出循环
4. 否则，执行所有候选规则（可能修改 `Facts` ）
5. 回到步骤2，继续循环
![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3SCLUkuu2IGndfwHnia1w8KFq7rDeAdbh21TbUmJQkNWWT5gzFb87dIq4QAia8nfvibQvdnSpxAkay7f6Bg47cGUn0eRpKCpm0vEdkIaSlrCck/640?wx_fmt=png&from=appmsg#imgIndex=3)

这种模式特别适合 **规则之间存在依赖关系** 的场景——一个规则的执行结果可能成为另一个规则的触发条件。

### 5.4 引擎参数配置

可以通过 `RulesEngineParameters` 精细控制引擎行为：

```
RulesEngineParameters parameters = new RulesEngineParameters()
    .skipOnFirstAppliedRule(true)    // 第一个规则执行后跳过后续
    .skipOnFirstFailedRule(true)     // 第一个规则失败后跳过后续
    .skipOnFirstNonTriggeredRule(false) // 第一个规则未触发时是否跳过
    .priorityThreshold(10);          // 只执行优先级<=10的规则

RulesEngine engine = new DefaultRulesEngine(parameters);
```

### 5.5 监听器机制

Easy Rules提供了 **监听器** 机制，可以在规则执行的各个阶段插入自定义逻辑：

```
public class LoggingRuleListener implements RuleListener {
    
    @Override
    public boolean beforeEvaluate(Rule rule, Facts facts) {
        
            System.out.println(
          "开始评估规则：" + 
            rule.getName());
          
        returntrue; // 返回false可跳过该规则
    }
    
    @Override
    public void afterEvaluate(Rule rule, Facts facts, boolean evaluationResult) {
        
            System.out.println(
          "规则 " + 
            rule.getName()
           + " 评估结果：" + evaluationResult);
    }
    
    @Override
    public void onSuccess(Rule rule, Facts facts) {
        
            System.out.println(
          "规则 " + 
            rule.getName()
           + " 执行成功");
    }
    
    @Override
    public void onFailure(Rule rule, Facts facts, Exception exception) {
        
            System.err.println(
          "规则 " + 
            rule.getName()
           + " 执行失败：" + 
            exception.getMessage());
          
    }
}
```

监听器可以用于 **日志记录、性能监控、统计规则命中率、调试** 等多种场景。

## 六、复合规则

> 有些小伙伴可能会问：单个规则只能处理一个条件，那复杂的业务逻辑怎么办？

Easy Rules提供了 **复合规则** 机制，可以把多个简单规则组合成复杂的规则。它提供了三种复合规则类型：

### 6.1 UnitRuleGroup（与逻辑）

**“所有规则都满足，才执行”**

![图片](https://mmbiz.qpic.cn/mmbiz_png/3SCLUkuu2IHorQOYZyFX1BCCWzI9RUF5X9sibuyFcjXc64fEibvhAloVnQodicDicx7kRvcE9iaaQQzbOEGmXQicTwGWFwsOrwSBy1fokWG0wE5IY/640?wx_fmt=png&from=appmsg#imgIndex=4)

**使用场景** ：需要多个前置条件全部满足才能执行某个操作。比如“用户是VIP且订单金额超过1000且商品有库存”，三个条件缺一不可。

```
UnitRuleGroup unitGroup = new UnitRuleGroup("全部满足规则组");

            unitGroup.addRule(
          new VipRule());

            unitGroup.addRule(
          new AmountRule());

            unitGroup.addRule(
          new StockRule());
// 只有三个规则全部满足，group才会执行
```

### 6.2 ActivationRuleGroup

**“只要有一个满足，就执行第一个”**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/3SCLUkuu2IFTrSwoiaaib4riaq5xyxKJzEbwoxtO53WdJoaOXBWuGQ7Ll0CpxtlZmPWVvEia9zVoGPgrhIoM6frgiaKO8NPzxYHuDj9zAFgPOaZI/640?wx_fmt=png&from=appmsg#imgIndex=5)

**使用场景** ：多个互斥的折扣规则，只能选一个生效。比如“新用户首单8折”和“VIP用户9折”同时满足时，只执行优先级高的那个。

```
ActivationRuleGroup activationGroup = new ActivationRuleGroup("折扣规则组");

            activationGroup.addRule(
          new NewUserDiscountRule());  // priority=3

            activationGroup.addRule(
          new VipDiscountRule());      // priority=1
// 只会执行优先级最高的那个（VIP折扣）
```

### 6.3 ConditionalRuleGroup（条件逻辑）

**“第一个满足的规则决定是否执行后续规则”**

**使用场景** ：根据第一个规则的结果决定是否执行后续规则链。

```
ConditionalRuleGroup conditionalGroup = new ConditionalRuleGroup("条件规则组");

            conditionalGroup.addRule(
          new CheckUserTypeRule());   // 第一个规则：判断用户类型

            conditionalGroup.addRule(
          new VipDiscountRule());     // 后续规则：根据类型执行

            conditionalGroup.addRule(
          new NormalDiscountRule());
// 只有第一个规则满足，才会继续执行后续规则
```

## 七、Maven依赖

在项目中引入Easy Rules非常简单：

```
<!-- Easy Rules 核心库 -->
<dependency>
    <groupId>
            org.jeasy
          </groupId>
    <artifactId>easy-rules-core</artifactId>
    <version>4.1.0</version>
</dependency>

<!-- 支持YAML/JSON规则定义 -->
<dependency>
    <groupId>
            org.jeasy
          </groupId>
    <artifactId>easy-rules-support</artifactId>
    <version>4.1.0</version>
</dependency>

<!-- 支持MVEL表达式语言 -->
<dependency>
    <groupId>
            org.jeasy
          </groupId>
    <artifactId>easy-rules-mvel</artifactId>
    <version>4.1.0</version>
</dependency>
```

> **注意** ：Easy Rules项目自2020年12月起进入维护模式， **最新稳定版本为4. [1.x](http://1.x/)** ，建议所有用户升级到此版本。

## 八、优缺点

### 优点

**1\. 极轻量级** JAR包仅 **100KB** 左右，没有任何复杂的依赖和配置。启动速度从秒级降至 **毫秒级** ，非常适合Kubernetes环境中的Pod快速启动。

**2\. 学习成本极低** 基于POJO和注解的编程模型，Java开发者几乎零门槛上手。不需要学习复杂的DSL（领域特定语言）。

**3\. 多种规则定义方式** 支持注解、流式API、表达式语言（MVEL/SpEL/JEXL）、YAML/JSON四种方式，覆盖从“代码硬编码”到“完全配置化”的全谱系需求。

**4\. 复合规则支持** 支持与逻辑、排他或逻辑、条件逻辑三种复合规则，可以从简单规则组合出复杂业务逻辑。

**5\. 监听器机制** 提供了完整的规则执行生命周期监听，方便日志记录、性能监控和调试。

**6\. 零配置开箱即用** 不需要任何外部配置文件，引入依赖即可开始使用。

**7\. 与Spring Boot无缝集成** 可以轻松集成到Spring Boot项目中，通过 `@Bean` 注册规则和引擎。

### 缺点

**1\. 规则修改仍需重启** 业务规则变更后， **仍然需要修改Java代码并重启服务** ，除非结合动态类加载或表达式语言方案。

**2\. 不支持复杂规则链和决策表** 相比Drools等重量级规则引擎，Easy Rules在复杂规则链、决策表等高级场景上能力有限。

**3\. 项目进入维护模式** Easy Rules自2020年12月起进入维护模式，目前仅支持版本4. [1.x。新功能开发基本停止，但现有功能足够稳定。](http://1.x.xn--,-n66aq8af0eda64p96mdnck1imxj97srzd5m100chl4af1v2l0ala0492d./)

**4\. 不适用于超大规模规则集** 当规则数量达到数千条时，性能可能不如采用Rete算法的Drools。

**5\. 无可视化管理界面** Easy Rules本身不提供可视化规则管理界面，需要自行开发。

## 九、适用场景

### 强烈推荐使用的场景

| 场景 | 典型应用 |
| --- | --- |
| **电商促销规则** | 满减、折扣、优惠券、会员特权 |
| **风控系统** | 用户评分、异常检测、反欺诈 |
| **数据验证** | 表单校验、数据完整性检查 |
| **条件判断** | 用户注册、登录等场景的条件分支 |
| **动态决策** | 智能推荐、个性化服务 |
| **游戏AI** | NPC行为规则、智能决策 |
| **配置化管理** | 通过YAML/JSON文件管理业务规则 |

### 不太适合的场景

| 场景 | 原因 |
| --- | --- |
| **超大规模规则集（数千条）** | 性能不如Drools等专业引擎 |
| **需要可视化规则管理** | Easy Rules不提供可视化界面 |
| **需要实时热更新规则** | 需要结合动态类加载或表达式语言自行实现 |
| **非常复杂的决策表** | Easy Rules能力有限 |

**一个实用的选型建议** ：如果你不确定未来规则的复杂度会发展到什么程度，可以从Easy Rules开始，待规则变复杂后再平滑迁移到Drools。

## 十、写在最后

回到最初的问题： **为什么要干掉if...else？**

不是if...else本身有问题——它是编程语言最基本的控制结构，没有任何问题。

**问题在于，当业务规则不断增长时，if...else会变成一座“代码垃圾山”** ——越堆越高、越堆越乱、越堆越没人敢动。

Easy Rules做的事情，就是 **把if...else从代码里“搬”出来，变成一个个独立的、可组合的、可管理的规则对象** 。

它不是一个“万能银弹”——它解决不了所有问题，它只是把“规则管理”这件事，从“写死在代码里”变成了“用对象来管理”。

但就这一步，已经能让你的代码从“if...else地狱”变成“规则清晰、可维护、可扩展”的优雅架构。

如果你正在维护一个被if...else撑爆的老系统，或者正在设计一个规则频繁变更的新系统， **不妨花10分钟把Easy Rules的官方示例跑一遍** 。

体会一下“规则即对象”的感觉——你会发现，代码可以如此清爽。

**开源地址与官方资源** ：

- **GitHub** ： [https://github.com/j-easy/easy-rules](https://github.com/j-easy/easy-rules)
- **官方文档** ： [https://www.easyrules.org/](https://www.easyrules.org/)

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的企业智能知识库系统](https://mp.weixin.qq.com/s?__biz=MzkwNjMwMTgzMQ==&mid=2247539571&idx=1&sn=58c091f5f488a3c7e82bb18641f8db9a&scene=21#wechat_redirect)