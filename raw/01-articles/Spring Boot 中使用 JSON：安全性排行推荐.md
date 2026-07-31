---
title: "Spring Boot 中使用 JSON：安全性排行推荐"
source: "https://mp.weixin.qq.com/s/peD6lEzQCjetOshbLQA7ew"
---
程序汪 我是程序汪 *2026年7月30日 10:15*

![图片](assets/Spring%20Boot%20%E4%B8%AD%E4%BD%BF%E7%94%A8%20JSON%EF%BC%9A%E5%AE%89%E5%85%A8%E6%80%A7%E6%8E%92%E8%A1%8C%E6%8E%A8%E8%8D%90/f690bedb0d289bddc48069f97c54919f_MD5.webp)

大家好，我是程序汪最近大家都知道FastJson爆雷不断，于是给大家总结下

先说结论：不存在“零漏洞”的 JSON 库。与其统计历史 CVE 数量，不如看默认配置、Spring Boot 兼容度和误用概率。

## 第一名：Jackson（很推荐）

Spring Boot 默认方案，综合最稳。自动配置、版本管理和生态都比较成熟，项目不需要额外替换转换器。注意不要随意开启全局多态反序列化，也不要让外部 JSON 决定 Java 类型。Spring Boot 4 已将 Jackson 3 作为首选默认库。官方文档

## 第二名：Gson（推荐）

功能简单，攻击面相对容易控制，适合普通 JSON 转换和小型项目。Gson 还主动禁止反序列化 `              java.lang.Class            ` 。缺点是已进入维护模式，在 Spring Boot 中的扩展能力不如 Jackson。官方说明

## 第三名：JSON-B（一般）

Jakarta 标准方案，规则清晰，适合偏规范化的企业项目。但国内资料、组件生态和排错经验都少一些。

## 第四名：FastJson2（不推荐）

性能不错，AutoType 默认关闭，也支持 SafeMode。但近期类型解析路径仍在持续加固。存量项目可以继续用，新项目没有特殊性能需求，不建议主动替换 Jackson。确需使用时，禁止全局 AutoType，并开启：

```
-
            Dfastjson2.parser.safeMode=
          true
```

安全配置说明

真正安全的组合不是“选对库”这么简单，而是：固定 DTO、限制请求大小、关闭自动类型、及时升级依赖。普通 Spring Boot 项目直接用默认 Jackson，通常最省心。

## Spring Boot 中使用 JSON：安全性与重大漏洞排行

先定口径：截至 2026 年 7 月，只统计公开 CVE 或官方公告中涉及远程代码执行、危险反序列化的高危问题。历史漏洞少，不一定代表今天更安全，用户量和审计力度也会影响数量。

| 推荐 | JSON 库 | 代表性重大记录 |
| --- | --- | --- |
| 1 | Jackson | 2017—2020 年集中出现 20 余个多态反序列化相关高危 CVE；2026 年又披露两项类型校验绕过 |
| 2 | Gson | 2022 年 1 项高危反序列化问题，主要影响是 DoS |
| 3 | JSON-B/Yasson | 暂未查到同等级公开 RCE 记录，但使用量和生态明显小于 Jackson |
| 4 | FastJson2 | 暂无正式公开 CVE；2026 年出现 AutoType 风险讨论，官方已合并校验加固 |
| 5 | FastJson [1.x](http://1.x/) | 2017、2020、2022、2026 多轮反序列化/RCE 风险，不建议新项目继续使用 |

## 为什么仍推荐 Jackson

Jackson 历史漏洞数量不少，但大部分需要主动开启多态类型、存在特定 gadget 类，并允许外部 JSON 控制类型。正常使用固定 DTO，并不会自动进入这些危险路径。

它还是 Spring Boot 默认方案，版本由 Boot 统一管理，升级、测试和兼容成本最低。Spring Boot 4 已将 Jackson 3 作为首选默认库。Spring Boot 文档

## 最实用的选择

普通 Spring Boot 项目直接使用 Jackson；简单工具可选 Gson；Jakarta 项目可考虑 JSON-B。FastJson2 存量项目应关闭 AutoType或开启 SafeMode。FastJson [1.x](http://1.x/) 则应尽快退出。

真正安全的配置只有几条：固定 DTO、禁止全局多态、限制请求大小、及时升级依赖。JSON 库选得再好，把外部类型名直接交给反序列化器，也照样会出事。

数据参考：Jackson 2026 高危漏洞、Gson 2022 漏洞、FastJson 2026 漏洞。