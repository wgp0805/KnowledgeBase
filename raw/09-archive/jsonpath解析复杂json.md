---
title: jsonpath解析复杂json
tags:
  - fastJson
categories:
  - JAVA
date: 2022-07-09 09:47:58
---

## 简单介绍


| JSONPath | 描述                                                       |
| :------: | :--------------------------------------------------------- |
|    $     | 根节点                                                     |
|    @     | 现行节点                                                   |
| . or [ ] | 取子节点                                                   |
|    ..    | 不管位置，选择所有符合条件的节点                           |
|    *     | 匹配所有元素节点                                           |
|   [ ]    | 迭代器标示（可以做简单的迭代操作，数字下标，根据美容选值） |
|  [ , ]   | 支持迭代器多选                                             |
|   ?()    | 支持过过滤操作                                             |
|   （）   | 支持表达式计算                                             |

## 实例


```java
 import cn.hutool.core.util.StrUtil;
import com.alibaba.fastjson.JSONPath;

public class FastjsonKit {

    public static <T> T get(String json, String path) {
        if (StrUtil.isBlank(json) || StrUtil.isBlank(path)) {
            return null;
        }
        try {
            return (T) JSONPath.extract(json, path);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
 
 
 
 @DisplayName("jsonpath使用方法   JSONPath()")
    @Test
    void JSONPath(){
        String jsonStr = "{ \"store\": {\n" +
                "    \"book\": [\n" +
                "      { \"category\": \"reference\",\n" +
                "        \"author\": \"张三\",\n" +
                "        \"title\": \"圆圈正义\",\n" +
                "        \"price\": 8.95\n" +
                "      },\n" +
                "      { \"category\": \"fiction\",\n" +
                "        \"author\": \"罗翔\",\n" +
                "        \"title\": \"法治的细节\",\n" +
                "        \"price\": 12.99,\n" +
                "        \"isbn\": \"0-553-21311-3\"\n" +
                "      }\n" +
                "    ],\n" +
                "    \"bicycle\": {\n" +
                "      \"color\": \"red\",\n" +
                "      \"price\": 19.95\n" +
                "    }\n" +
                "  }\n" +
                "}";
        //获取store节点下的Book[0]的author值
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$.store.book[0].author"));

        //输出全部author的值
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$.store.book[*].author"));

        //输出book[*]中category == 'reference'的book
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$.store.book[?(@.category == 'reference')]"));

        //输出book[*]中category == 'reference' 或者 price >10的book
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$.store.book[?(@.category == 'reference' || @.price>10)]"));

        //输出book[*]中category == 'reference'的book的author
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$.store.book[?(@.category == 'reference')].author"));

        //输出book[*]中price>10的book
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$.store.book[?(@.price>10)]"));

        //输出book[*]中含有isbn元素的book
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$.store.book[?(@.isbn)]"));

        //输出该json中所有price的值
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$..price"));

        //输出该json中所有title的值
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$..title"));

        //输出该json中book 0,1的值
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$..book[0,1]"));

        //可以提前编辑一个路径，并多次使用它
        System.out.println("结果为："+ FastjsonKit.get(jsonStr, "$.store.book[*]"));
    }
```

## 结果

```text
结果为：张三
结果为：["张三","罗翔"]
结果为：[{"category":"reference","author":"张三","title":"圆圈正义","price":8.95}]
结果为：[{"category":"reference","author":"张三","title":"圆圈正义","price":8.95},{"category":"fiction","author":"罗翔","title":"法治的细节","price":12.99,"isbn":"0-553-21311-3"}]
结果为：["张三"]
结果为：[{"category":"fiction","author":"罗翔","title":"法治的细节","price":12.99,"isbn":"0-553-21311-3"}]
结果为：[{"category":"fiction","author":"罗翔","title":"法治的细节","price":12.99,"isbn":"0-553-21311-3"}]
结果为：[8.95,12.99,19.95]
结果为：["圆圈正义","法治的细节"]
结果为：[{"category":"reference","author":"张三","title":"圆圈正义","price":8.95},{"category":"fiction","author":"罗翔","title":"法治的细节","price":12.99,"isbn":"0-553-21311-3"}]
结果为：[{"category":"reference","author":"张三","title":"圆圈正义","price":8.95},{"category":"fiction","author":"罗翔","title":"法治的细节","price":12.99,"isbn":"0-553-21311-3"}]
```

