---
source_url: "https://mp.weixin.qq.com/s/fWfdWPFgY5x5793JayK6Yw"
title: "为什么阿里不推荐使用 keySet（） 遍历 HashMap？"
account: "小哈学Java"
published_at: "2026-09-12 22:27:03"
saved_at: "2026-09-14 07:28:08"
sync_id: "art_4bfdd706b2124ccf80484f83719a5dc4"
parse_status: "ok"
---

# 为什么阿里不推荐使用 keySet（） 遍历 HashMap？

![图片 1](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/20079d804ac9a9ff19e44f9968be4404_MD5.png)

![图片 2](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/ed1ba0b764c0983a2eb74d526e681912_MD5.jpg)

![图片 3](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/05f62117df802c8c8146484c4d968427_MD5.jpg)

![图片 4](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/6d159e9009614deb8d2741cbb35311e4_MD5.jpg)

![图片 5](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/7e7c3530dc827fb73b67cf6f1e7418e0_MD5.jpg)

![图片 6](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/6fa16197f64a5f90c73f55c0bdcffa5e_MD5.jpg)

![图片 7](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/5f0f367f6ede829005092de9047b62ac_MD5.jpg)

![图片 8](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/f6c1b3d33681ad2267a063b2b6291736_MD5.jpg)

![图片 9](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/40a9cbf51c237c1c70d30723980e9a4a_MD5.jpg)

![图片 10](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

![图片 11](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/b01fd91d58faf9455f8fbb5c64bb22f0_MD5.webp)

![图片 12](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/7df57b5574ec2ec178922933af126d15_MD5.gif)

![图片 13](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/b0ee5bffad568537e70580143316fb61_MD5.gif)

将 **小哈学Java**** **设为“**星标****⭐**”

第一时间收到文章更新

![](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/761cadfeb5cb3f8d3dea8dee1e80878e_MD5.png)

来源：juejin.cn/post/7295353579002396726

**在线 Java 面试刷题（已更新334题，图文并茂）**：https://www.quanxiaoha.com/java-interview

来源：juejin.cn/post/7295353579002396726

**目录**

- Part1 引言
- Part2 keySet 如何遍历了两次
- 1 iterator()
- 2 HashMap.KeySet#iterator()
- 3 HashMap.KeyIterator
- 4 HashMap.HashIterator

- Part3 总结

## Part1 引言

HashMap 相信所有学 Java 的都一定不会感到陌生，作为一个非常重用且非常实用的 Java 提供的容器，它在我们的代码里面随处可见。因此遍历操作也是我们经常会使用到的。HashMap 的遍历方式现如今有非常多种：

- 使用迭代器（Iterator)。
- 使用  `keySet()`  获取键的集合，然后通过增强的 for 循环遍历键。
- 使用  `entrySet()`  获取键值对的集合，然后通过增强的 for 循环遍历键值对。
- 使用 Java 8+ 的 Lambda 表达式和流。

以上遍历方式的孰优孰劣，在《阿里巴巴开发手册》中写道：

![阿里巴巴开发手册关于 HashMap 遍历的推荐](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/ed1ba0b764c0983a2eb74d526e681912_MD5.jpg)

阿里巴巴开发手册关于 HashMap 遍历的推荐这里推荐使用的是  `entrySet`  进行遍历，在 Java8 中推荐使用  `Map.forEach()` 。给出的理由是遍历次数上的不同。

- keySet 遍历，需要经过两次遍历。
- entrySet 遍历，只需要一次遍历。

> **“**其中 keySet 遍历了两次，一次是转为 Iterator 对象，另一次是从 hashMap 中取出 key 所对应的 value。

其中后面一段话很好理解，但是前面这句话却有点绕，为什么转换成了 Iterator 遍历了一次？

我查阅了各个平台对 HashMap 的遍历，其中都没有或者原封不动的照搬上句话。（当然也可能是我没有查阅到靠谱的文章，欢迎指正）

## Part2 keySet 如何遍历了两次

我们首先写一段代码，使用 keySet 遍历 Map。

```
public class Test {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<>();
        map.put("k1", "v1");
        map.put("k2", "v2");
        map.put("k3", "v3");
        for (String key : map.keySet()) {
            String value = map.get(key);
            System.out.println(key + ":" + value);
        }
    }
}
```

运行结果显而易见的是

```
k1:v1
k2:v2
k3:v3
```

两次遍历，第一次遍历所描述的是转为 Iterator 对象我们好像没有从代码中看见，我们看到的后面所描述的遍历，也就是遍历  `map,keySet()`  所返回的  `Set`  集合中的 key，然后去 HashMap 中拿取 value 的。

Iterator 对象呢？如何遍历转换为 Iterator 对象的呢？

![](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/05f62117df802c8c8146484c4d968427_MD5.jpg)

首先我们这种遍历方式大家都应该知道是叫： `增强for循环，for-each`

这是一种 Java 的语法糖~。

我们可以通过反编译，或者直接通过 Idea 在 class 文件中查看对应的 Class 文件

![IDEA 中查看反编译后的 Class 文件](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/6d159e9009614deb8d2741cbb35311e4_MD5.jpg)

IDEA 中查看反编译后的 Class 文件

```
public class Test {
    public Test() {
    }

    public static void main(String[] args) {
        Map<String, String> map = new HashMap();
        map.put("k1", "v1");
        map.put("k2", "v2");
        map.put("k3", "v3");
        Iterator var2 = map.keySet().iterator();

        while(var2.hasNext()) {
            String key = (String)var2.next();
            String value = (String)map.get(key);
            System.out.println(key + ":" + value);
        }

    }
}
```

和我们编写的是存在差异的，其中我们可以看到其中通过  `map.keySet().iterator()`  获取到了我们所需要看见的  `Iterator`  对象。

那么它又是怎么转换成的呢？为什么需要遍历呢？我们查看  `iterator()`  方法

### 1 iterator()

![Set 接口的 iterator() 方法定义](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/7e7c3530dc827fb73b67cf6f1e7418e0_MD5.jpg)

Set 接口的 iterator() 方法定义发现是 Set 定义的一个接口。返回此集合中元素的迭代器

### 2 HashMap.KeySet#iterator()

我们查看 HashMap 中 keySet 类对该方法的实现。

![KeySet 类在 HashMap 中的定义](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/6fa16197f64a5f90c73f55c0bdcffa5e_MD5.jpg)

KeySet 类在 HashMap 中的定义

![HashMap.KeySet#iterator() 源码](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/5f0f367f6ede829005092de9047b62ac_MD5.jpg)

HashMap.KeySet#iterator() 源码

```
final class KeySet extends AbstractSet<K> {
    public final int size()                 { return size; }
    public final void clear()               { HashMap.this.clear(); }
    public final Iterator<K> iterator()     { return new KeyIterator(); }
    public final boolean contains(Object o) { return containsKey(o); }
    public final boolean remove(Object key) {
        return removeNode(hash(key), key, null, false, true) != null;
    }
    public final Spliterator<K> spliterator() {
        return new KeySpliterator<>(HashMap.this, 0, -1, 0, 0);
    }
    public final void forEach(Consumer<? super K> action) {
        Node<K,V>[] tab;
        if (action == null)
            throw new NullPointerException();
        if (size > 0 && (tab = table) != null) {
            int mc = modCount;
            for (int i = 0; i < tab.length; ++i) {
                for (Node<K,V> e = tab[i]; e != null; e = e.next)
                    action.accept(e.key);
            }
            if (modCount != mc)
                throw new ConcurrentModificationException();
        }
    }
}
```

其中的 iterator() 方法返回的是一个  `KeyIterator`  对象，那么究竟是在哪里进行了遍历呢？我们接着往下看去。

### 3 HashMap.KeyIterator

![HashMap.KeyIterator 源码](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/f6c1b3d33681ad2267a063b2b6291736_MD5.jpg)

HashMap.KeyIterator 源码

```
final class KeyIterator extends HashIterator
    implements Iterator<K> {
    public final K next() { return nextNode().key; }
}
```

这个类也很简单：

- 继承了  `HashIterator`  类。
- 实现了  `Iterator`  接口。
- 一个  `next()`  方法。

还是没有看见哪里进行了遍历，那么我们继续查看  `HashIterator`  类

### 4 HashMap.HashIterator

![HashMap.HashIterator 源码](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/40a9cbf51c237c1c70d30723980e9a4a_MD5.jpg)

HashMap.HashIterator 源码

```
abstract class HashIterator {
    Node<K,V> next;        // next entry to return
    Node<K,V> current;     // current entry
    int expectedModCount;  // for fast-fail
    int index;             // current slot

    HashIterator() {
        expectedModCount = modCount;
        Node<K,V>[] t = table;
        current = next = null;
        index = 0;
        if (t != null && size > 0) { // advance to first entry
            do {} while (index < t.length && (next = t[index++]) == null);
        }
    }

    public final boolean hasNext() {
        return next != null;
    }

    final Node<K,V> nextNode() {
        Node<K,V>[] t;
        Node<K,V> e = next;
        if (modCount != expectedModCount)
            throw new ConcurrentModificationException();
        if (e == null)
            throw new NoSuchElementException();
        if ((next = (current = e).next) == null && (t = table) != null) {
            do {} while (index < t.length && (next = t[index++]) == null);
        }
        return e;
    }

    public final void remove() {
        Node<K,V> p = current;
        if (p == null)
            throw new IllegalStateException();
        if (modCount != expectedModCount)
            throw new ConcurrentModificationException();
        current = null;
        K key = p.key;
        removeNode(hash(key), key, null, false, false);
        expectedModCount = modCount;
    }
}
```

我们可以发现这个构造器中存在了一个  `do-while`  循环操作，目的是找到一个第一个不为空的  `entry` 。

```
HashIterator() {
    expectedModCount = modCount;
    Node<K,V>[] t = table;
    current = next = null;
    index = 0;
    if (t != null && size > 0) { // advance to first entry
        do {} while (index < t.length && (next = t[index++]) == null);
    }
}
```

而  `KeyIterator`  是 extend  `HashIterator`  对象的。这里涉及到了继承的相关概念，大家忘记的可以找相关的文章看看，或者我也可以写一篇~~dog。

例如两个类

```
public class Father {

    public Father(){
        System.out.println("father");
    }
}
public class Son extends Father{

    public static void main(String[] args) {
        Son son = new Son();
    }
}
```

创建 Son 对象的同时，会执行 Father 构造器。也就会打印出  `father`  这句话。

那么这个循环操作就是我们要找的循环操作了。

## Part3 总结

- 使用 keySet 遍历，其实内部是使用了对应的  `iterator()`  方法。
-  `iterator()`  方法是创建了一个  `KeyIterator`  对象。
-  `KeyIterator`  对象 extend  `HashIterator`  对象。
-  `HashIterator`  对象的构造方法中，会遍历找到第一个不为空的  `entry`  。

> **“**keySet->iterator()->KeyIterator->HashIterator

[加入小哈的星球](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / Java 学习路线 / **社群讨论 / **学习打卡 / 每月赠书**

- 《仿小红书（微服务架构 ）》 已完结，基于 Spring Cloud Alibaba + Spring Boot 3.x + JDK 17..., [点击查看项目介绍](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247538491&idx=1&sn=576995017721766d0fe15723fd135619&chksm=fd5787bdca200eab54d2fb8ca07fcc2bffdec3eaab4ab82ab5eaf949f0254c1683455e02010b&token=343952052&lang=zh_CN&scene=21#wechat_redirect) ； 演示地址： http://116.62.199.48:7070/
- 《 Spring AI 应用（RAG 智能客服） 》已完结, 基于 Spring AI + Spring Boot 3.x + JDK 21
- 《 秒杀系统设计 》正在更新中，单体到微服务高并发架构演进

- 《 前后端分离博客项目（全栈开发） 》 已完结,演示链接： http://116.62.199.48/
- 项目阅读地址： https://quanxiaoha.com/column

截止目前，**累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

![图片](assets/2026-09-12%20-%20%E4%B8%BA%E4%BB%80%E4%B9%88%E9%98%BF%E9%87%8C%E4%B8%8D%E6%8E%A8%E8%8D%90%E4%BD%BF%E7%94%A8%20keySet%EF%BC%88%EF%BC%89%20%E9%81%8D%E5%8E%86%20HashMap%EF%BC%9F/b01fd91d58faf9455f8fbb5c64bb22f0_MD5.webp)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~
2. 使用 Shadcn UI 构建 Java 桌面应用
3. 面试题：ES 不支持 decimal，如何避免丢失精度？
4. 四大软件外包公司
```

```

```

```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。
获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。
```

```
PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。
点“在看”支持小哈呀，谢谢
```


---
原文链接：https://mp.weixin.qq.com/s/fWfdWPFgY5x5793JayK6Yw
