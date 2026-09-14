---
title: "为什么阿里不推荐使用 keySet() 遍历 HashMap？"
type: source
tags: [Java, HashMap, keySet, entrySet, 遍历, 阿里巴巴开发手册, 源码分析]
sources: [raw/01-articles/2026-09-12 - 为什么阿里不推荐使用 keySet（） 遍历 HashMap？.md]
last_updated: 2026-09-14
---

# 为什么阿里不推荐使用 keySet() 遍历 HashMap？

## 核心摘要
《阿里巴巴开发手册》推荐使用 entrySet 而非 keySet 遍历 HashMap，理由是 keySet 需要两次遍历而 entrySet 只需一次。本文通过反编译和源码追踪，揭示 keySet 遍历"两次"的真正机制：增强 for 循环语法糖转换为 Iterator，而 HashIterator 构造方法中存在 do-while 循环遍历哈希表数组找到第一个非空 entry。

## 关键要点
- 阿里巴巴开发手册推荐使用 entrySet 遍历 HashMap，Java8 推荐使用 Map.forEach()
- keySet 遍历两次：一次转为 Iterator 对象，一次从 HashMap 中取出 key 对应的 value
- entrySet 遍历一次：直接获取键值对
- 增强 for 循环（for-each）是 Java 语法糖，反编译后显示实际调用 map.keySet().iterator()
- keySet() 返回 KeySet 对象，其 iterator() 方法返回 new KeyIterator()
- KeyIterator extends HashIterator，HashIterator 构造方法中有 do-while 循环遍历 table 数组
- HashIterator 构造方法中的遍历是"第一次遍历"的来源
- 调用链：keySet → iterator() → KeyIterator → HashIterator

## 详细内容

### 遍历方式对比
HashMap 常见遍历方式：
- 使用迭代器（Iterator）
- 使用 keySet() 获取键集合，通过增强 for 循环遍历键
- 使用 entrySet() 获取键值对集合，通过增强 for 循环遍历
- 使用 Java 8+ 的 Lambda 表达式和流

阿里巴巴开发手册推荐 entrySet，理由：
- keySet 遍历两次：一次转为 Iterator 对象，另一次从 hashMap 中取出 key 对应的 value
- entrySet 遍历一次

### keySet 两次遍历的源码追踪

**第一层：增强 for 循环的语法糖**
```java
for (String key : map.keySet()) {
    String value = map.get(key);
}
```
反编译后：
```java
Iterator var2 = map.keySet().iterator();
while(var2.hasNext()) {
    String key = (String)var2.next();
    String value = (String)map.get(key);
}
```

**第二层：KeySet.iterator()**
```java
final class KeySet extends AbstractSet<K> {
    public final Iterator<K> iterator() { return new KeyIterator(); }
}
```

**第三层：KeyIterator**
```java
final class KeyIterator extends HashIterator
    implements Iterator<K> {
    public final K next() { return nextNode().key; }
}
```

**第四层：HashIterator 构造方法中的遍历**
```java
HashIterator() {
    expectedModCount = modCount;
    Node<K,V>[] t = table;
    current = next = null;
    index = 0;
    if (t != null && size > 0) {
        do {} while (index < t.length && (next = t[index++]) == null);
    }
}
```
构造方法中的 do-while 循环遍历 table 数组找到第一个不为空的 entry，这就是"第一次遍历"的来源。KeyIterator 继承 HashIterator，创建 KeyIterator 对象时会执行父类构造方法。

### 总结
- keySet 遍历内部使用 iterator() 方法
- iterator() 创建 KeyIterator 对象
- KeyIterator extends HashIterator
- HashIterator 构造方法中遍历找到第一个不为空的 entry

调用链：keySet → iterator() → KeyIterator → HashIterator

## 关联连接
- [[HashMap]]
- [[JavaCollection]]
- [[AlibabaDevManual]]
- [[IteratorPattern]]
- [[JavaSyntaxSugar]]
