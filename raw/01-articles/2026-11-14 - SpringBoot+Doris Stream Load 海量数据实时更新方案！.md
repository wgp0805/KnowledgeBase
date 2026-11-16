---
source_url: "https://mp.weixin.qq.com/s/rIkirRrhfQYfxqW1-lK39w"
title: "SpringBoot+Doris Stream Load 海量数据实时更新方案！"
account: "小哈学Java"
published_at: "2026-11-14 18:34:25"
saved_at: "2026-11-14 19:56:42"
sync_id: "art_48c5ec61642642b9a3c97048398447b2"
parse_status: "ok"
---

# SpringBoot+Doris Stream Load 海量数据实时更新方案！

将 **小哈学Java**** **设为“**星标****⭐**”

第一时间收到文章更新

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pUq1tpL9smoGRBrGxVIe44HRyniahtntKiapbod5x0CClVodTkJgxDFnEw1PNmj2WoQN21icDhr8XBZCTiaxWUVfI03aQea9VQaDUyrQNCBic4k0/640?wx_fmt=png&from=appmsg)

来源：https://blog.csdn.net/mouzeping123/article/details/149420654

**在线 Java 面试刷题（已更新362题，25个分类，图文并茂）**：https://www.quanxiaoha.com/java-interview

**目录**

- 整体架构
- 1.依赖配置 (pom.xml)
- 2.配置属性类
- 3.字段映射注解
- 4.自动映射工具类
- 5.Doris Stream Load 核心类
- 6.实体类示例
- 7.业务层实现
- 8.配置类
- 9.应用配置 (application.yml)
- 方案特点与优势
- 性能优化建议

## 整体架构

```
├── src
│   ├── main
│   │   ├── java
│   │   │   └── com
│   │   │       └── example
│   │   │           └── doris
│   │   │               ├── annotation
│   │   │               │   └── DorisField.java
│   │   │               ├── config
│   │   │               │   ├── DorisConfig.java
│   │   │               │   └── DorisStreamLoadProperties.java
│   │   │               ├── core
│   │   │               │   └── DorisStreamLoader.java
│   │   │               ├── entity
│   │   │               │   └── User.java
│   │   │               ├── service
│   │   │               │   └── UserService.java
│   │   │               └── util
│   │   │                   └── DorisMapper.java
│   │   └── resources
│   │       └── application.yml
```

## 1. 依赖配置 (pom.xml)

```
<dependencies>
    <!-- Spring Boot Starter -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- HTTP客户端 -->
    <dependency>
        <groupId>org.apache.httpcomponents</groupId>
        <artifactId>httpclient</artifactId>
        <version>4.5.13</version>
    </dependency>
    <!-- Jackson -->
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
    </dependency>
    <dependency>
        <groupId>com.fasterxml.jackson.datatype</groupId>
        <artifactId>jackson-datatype-jsr310</artifactId>
    </dependency>
    <!-- Lombok -->
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    <!-- Guava -->
    <dependency>
        <groupId>com.google.guava</groupId>
        <artifactId>guava</artifactId>
        <version>31.1-jre</version>
    </dependency>
    <!-- 反射工具 -->
    <dependency>
        <groupId>org.reflections</groupId>
        <artifactId>reflections</artifactId>
        <version>0.10.2</version>
    </dependency>
</dependencies>
```

## 2. 配置属性类

DorisStreamLoadProperties.java

```
package com.example.doris.config;

import lombok.Getter;
import lombok.Setter;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

@Getter
@Setter
@Configuration
@ConfigurationProperties(prefix = "doris.stream-load")
publicclass DorisStreamLoadProperties {
    private String url;
    private String username;
    private String password;
    privateint connectTimeout = 30000;
    privateint socketTimeout = 60000;
    privateint batchSize = 50000;
    privateint maxRetries = 3;
    private String compression = "none";
    privateint maxParallel = 4;
    private String columnSeparator = "\\x01";
    private String lineSeparator = "\\n";
}
```

## 3. 字段映射注解

DorisField.java

```
package com.example.doris.annotation;

import java.lang.annotation.ElementType;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.FIELD)
public@interface DorisField {
    /**
     * Doris表字段名（默认使用实体字段名）
     */
    String value() default "";

    /**
     * 字段顺序（数值越小越靠前）
     */
    int order() default Integer.MAX_VALUE;

    /**
     * 是否忽略该字段
     */
    boolean ignore() default false;
}
```

## 4. 自动映射工具类

DorisMapper.java

```
package com.example.doris.util;

import cn.hutool.core.date.DateUtil;
import com.fantaibao.constants.DorisField;
import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.lang.reflect.Field;
import java.util.*;
import java.util.stream.Collectors;

publicclass DorisMapper {
    privatestaticfinal ObjectMapper objectMapper = new ObjectMapper();

    /**
     * 将实体列表转换为Doris需要的Map列表（保持字段顺序）
     */
    publicstatic <T> List<Map<String, Object>> convertToDorisData(List<T> entities, Map<String, Object> additionalFields) {
        if (entities == null || entities.isEmpty()) {
            return Collections.emptyList();
        }
        // 获取第一个实体类获取字段顺序
        Class<?> clazz = entities.get(0).getClass();
        List<Field> orderedFields = getOrderedFields(clazz);
        return entities.stream().map(entity -> {
            Map<String, Object> map = new LinkedHashMap<>();
            // 添加额外字段
            if (additionalFields != null) {
                map.putAll(additionalFields);
            }
            // 添加实体字段
            for (Field field : orderedFields) {
                try {
                    field.setAccessible(true);
                    DorisField annotation = field.getAnnotation(DorisField.class);
                    String fieldName = annotation.value().isEmpty() ?
                            field.getName() : annotation.value();
                    Object value = field.get(entity);
                    //如果数据库字段类型是datetime 类型，则格式化为yyyy-MM-dd HH:mm:ss。不然会存入空值
                    map.put(fieldName, field.getType() == Date.class ? DateUtil.format((Date) value, "yyyy-MM-dd HH:mm:ss") : value);
                } catch (IllegalAccessException e) {
                    thrownew RuntimeException("字段访问失败: " + field.getName(), e);
                }
            }
            return map;
        }).collect(Collectors.toList());
    }

    /**
     * 将实体列表转换为Doris需要的Map列表（使用Jackson序列化）
     */
    publicstatic <T> List<Map<String, Object>> convertWithJackson(List<T> entities, Map<String, Object> additionalFields) {
        return entities.stream().map(entity -> {
            // 使用Jackson将实体转为Map
            Map<String, Object> map = objectMapper.convertValue(entity,
                    new TypeReference<LinkedHashMap<String, Object>>() {
                    });
            // 添加额外字段
            if (additionalFields != null) {
                map.putAll(additionalFields);
            }
            return map;
        }).collect(Collectors.toList());
    }

    /**
     * 获取带注解的字段并按顺序排序
     */
    private static List<Field> getOrderedFields(Class<?> clazz) {
        return Arrays.stream(clazz.getDeclaredFields())
                .filter(f -> f.isAnnotationPresent(DorisField.class))
                .filter(f -> !f.getAnnotation(DorisField.class).ignore())
                .sorted(Comparator.comparingInt(
                        f -> f.getAnnotation(DorisField.class).order()
                ))
                .collect(Collectors.toList());
    }
}
```

## 5. Doris Stream Load 核心类

DorisStreamLoader.java

```
package com.example.doris.core;

import com.alibaba.fastjson.JSONObject;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.google.common.collect.Lists;
import lombok.extern.slf4j.Slf4j;
import org.apache.http.Header;
import org.apache.http.HttpEntity;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPut;
import org.apache.http.entity.ByteArrayEntity;
import org.apache.http.entity.HttpEntityWrapper;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicHeader;
import org.apache.http.util.EntityUtils;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.List;
import java.util.Map;
import java.util.concurrent.*;
import java.util.stream.Collectors;
import java.util.zip.GZIPOutputStream;

@Slf4j
@Component
publicclass DorisStreamLoader {
    privatefinal ScheduledExecutorService scheduler = Executors.newScheduledThreadPool(1);
    privatefinal DorisStreamLoadProperties properties;
    privatefinal String authEncoding;
    privatefinal CloseableHttpClient httpClient;
    privatefinal ExecutorService executorService;

    public DorisStreamLoader(@Qualifier("dorisStreamLoadProperties") DorisStreamLoadProperties properties) {
        this.properties = properties;

        // 基本认证编码
        this.authEncoding = Base64.getEncoder().encodeToString(
                (properties.getUsername() + ":" + properties.getPassword()).getBytes(StandardCharsets.UTF_8));

        // 创建带连接池的HTTP客户端
        this.httpClient = HttpClients.custom()
                .setConnectionTimeToLive(60, TimeUnit.SECONDS)
                .setMaxConnTotal(properties.getMaxParallel() * 2)
                .setMaxConnPerRoute(properties.getMaxParallel())
                .build();

        // 创建并行加载线程池
        this.executorService = Executors.newFixedThreadPool(properties.getMaxParallel());
    }

    /**
     * 并行流式加载数据
     *
     * @param data      数据列表
     * @param format    数据格式 (json/csv)
     * @param dbName    数据库名称
     * @param tableName 表名
     */
    public void parallelStreamLoad(List<Map<String, Object>> data, String format, String dbName, String tableName) {
        if (data.isEmpty()) return;
        // 分批处理
        List<List<Map<String, Object>>> batches = Lists.partition(data, properties.getBatchSize());
        // 等待所有任务完成
        CompletableFuture.allOf(batches.stream()
                .map(batch -> CompletableFuture.runAsync(() -> {
                    try {
                        sendBatch(batch, format, dbName, tableName);
                    } catch (Exception e) {
                        log.error("Stream Load 批次处理失败", e);
                        thrownew RuntimeException(e);
                    }
                }, executorService)).toArray(CompletableFuture[]::new)).join();
    }

    private void sendBatch(List<Map<String, Object>> batch, String format, String dbName, String tableName) {
        String data;
        if ("csv".equalsIgnoreCase(format)) {
            data = convertToCsv(batch);
        } else {
            data = convertToJson(batch);
        }
        attemptSendWithRetry(data, format, 0, dbName, tableName);
    }

    private void attemptSendWithRetry(String data, String format, int retryCount, String dbName, String tableName) {
        try {
            sendToDoris(data, format, dbName, tableName);
            log.info("Stream Load 成功");
        } catch (Exception e) {
            if (retryCount < properties.getMaxRetries()) {
                long delay = 1000 * (long) Math.pow(2, retryCount);
                log.warn("Stream Load 失败，第 {} 次重试，{}ms 后重试", retryCount + 1, delay, e);
                scheduler.schedule(() -> attemptSendWithRetry(data, format, retryCount + 1, dbName, tableName), delay, TimeUnit.MILLISECONDS);
            } else {
                log.error("Stream Load 达到最大重试次数失败", e);
                thrownew RuntimeException("Stream Load 批次失败: " + e.getMessage(), e);
            }
        }
    }

    private String convertToJson(List<Map<String, Object>> batch) {
        try {
            returnnew ObjectMapper().writeValueAsString(batch);
        } catch (JsonProcessingException e) {
            thrownew RuntimeException("JSON转换失败", e);
        }
    }

    private String convertToCsv(List<Map<String, Object>> batch) {
        return batch.stream()
                .map(row -> row.values().stream()
                        .map(value -> value == null ? "\\N" : value.toString())
                        .collect(Collectors.joining(properties.getColumnSeparator())))
                .collect(Collectors.joining(properties.getLineSeparator()));
    }

    private void sendToDoris(String data, String format, String dbName, String tableName) throws IOException {
        HttpPut httpPut = new HttpPut(String.format(properties.getUrl(), dbName, tableName));
        httpPut.setHeader("Authorization", "Basic " + authEncoding);

        // 设置超时
        RequestConfig config = RequestConfig.custom()
                .setConnectTimeout(properties.getConnectTimeout())
                .setSocketTimeout(properties.getSocketTimeout())
                .build();
        httpPut.setConfig(config);
        // 设置格式相关header
        if ("csv".equalsIgnoreCase(format)) {
            httpPut.setHeader("Content-Type", "text/plain");
            httpPut.setHeader("format", "csv");
            httpPut.setHeader("column_separator", properties.getColumnSeparator());
            httpPut.setHeader("line_delimiter", properties.getLineSeparator());
        } else {
            httpPut.setHeader("Content-Type", "application/json");
            httpPut.setHeader("format", "json");
            httpPut.setHeader("strip_outer_array", "true");
        }
        // 压缩处理
        HttpEntity entity;
        if ("gzip".equals(properties.getCompression())) {
            httpPut.setHeader("compress_type", "gz");
            entity = new GzipCompressingEntity(data);
        } else {
            entity = new StringEntity(data, StandardCharsets.UTF_8);
        }
        httpPut.setEntity(entity);
        try (CloseableHttpResponse response = httpClient.execute(httpPut)) {
            int statusCode = response.getStatusLine().getStatusCode();
            LoadResponse result = JSONObject.parseObject(EntityUtils.toString(response.getEntity()), LoadResponse.class);
            if (!result.getStatus().equals("Success")) {
                log.error("Stream Load失败: HTTP {} - {}", statusCode, result);
                thrownew IOException("Doris Stream Load失败: " + result);
            }
            // 解析导入结果
            log.info("成功导入{}条数据, 耗时: {}ms",result.getNumberLoadedRows(),result.getLoadTimeMs());
        }
    }

    // GZIP压缩实体
    staticclass GzipCompressingEntity extends HttpEntityWrapper {
        public GzipCompressingEntity(String data) throws IOException {
            super(createEntity(data));
        }

        private static HttpEntity createEntity(String data) throws IOException {
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            try (GZIPOutputStream gzip = new GZIPOutputStream(bos)) {
                gzip.write(data.getBytes(StandardCharsets.UTF_8));
            }
            returnnew ByteArrayEntity(bos.toByteArray());
        }

        @Override
        public Header getContentEncoding() {
            returnnew BasicHeader("Content-Encoding", "gzip");
        }
    }
}
```

接口响应类 LoadResponse

```
package com.fantaibao.application.config;

import lombok.Data;

@Data
publicclass LoadResponse {

    /**
     * 事务ID
     * 类型：long
     */
    privatelong TxnId;

    /**
     * 加载任务的唯一标识
     * 类型：String
     */
    private String Label;

    /**
     * 用户对本次加载的描述信息
     * 类型：String
     */
    private String Comment;

    /**
     * 是否启用两阶段提交协议
     * 类型：boolean
     */
    privateboolean TwoPhaseCommit;

    /**
     * 当前加载任务的状态
     * 类型：String
     */
    private String Status;

    /**
     * 加载结果的详细描述信息
     * 类型：String
     */
    private String Message;

    /**
     * 总共处理的数据行数
     * 类型：int
     */
    privateint NumberTotalRows;

    /**
     * 成功加载的数据行数
     * 类型：int
     */
    privateint NumberLoadedRows;

    /**
     * 被过滤（格式错误或校验失败）的数据行数
     * 类型：int
     */
    privateint NumberFilteredRows;

    /**
     * 未被选中的数据行数（例如因条件不满足而跳过）
     * 类型：int
     */
    privateint NumberUnselectedRows;

    /**
     * 加载数据的总字节数
     * 类型：int
     */
    privateint LoadBytes;

    /**
     * 整个加载过程所耗时间（单位：毫秒）
     * 类型：int
     */
    privateint LoadTimeMs;

    /**
     * 开启事务所耗时间（单位：毫秒）
     * 类型：int
     */
    privateint BeginTxnTimeMs;

    /**
     * 接收StreamLoad请求并写入内存所耗时间（单位：毫秒）
     * 类型：int
     */
    privateint StreamLoadPutTimeMs;

    /**
     * 读取数据所耗时间（单位：毫秒）
     * 类型：int
     */
    privateint ReadDataTimeMs;

    /**
     * 写入数据到存储引擎所耗时间（单位：毫秒）
     * 类型：int
     */
    privateint WriteDataTimeMs;

    /**
     * 接收数据所耗时间（单位：毫秒）
     * 类型：int
     */
    privateint ReceiveDataTimeMs;

    /**
     * 提交事务和发布版本所耗时间（单位：毫秒）
     * 类型：int
     */
    privateint CommitAndPublishTimeMs;
}
```

获取实体映射的数据库表工具类 TableUtils

```
package com.fantaibao.util;

import com.baomidou.mybatisplus.annotation.TableName;

publicclass TableUtils {
    publicstatic <T> String getTableName(Class<T> entityClass) {
        TableName tableNameAnnotation = entityClass.getAnnotation(TableName.class);
        if (tableNameAnnotation != null) {
            return tableNameAnnotation.value();
        }
        // 默认命名规则：驼峰转下划线
        return entityClass.getSimpleName()
                .replaceAll("([A-Z])", "_$1")
                .toLowerCase()
                .substring(1); // 去掉开头的下划线（如 User → user）
    }
}
```

## 6. 实体类示例

User.java

```
package com.example.doris.entity;

import com.baomidou.mybatisplus.annotation.FieldStrategy;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableName;
import com.fantaibao.constants.DorisField;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;
import java.util.Date;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
@TableName("user ")
publicclass User {
    @DorisField(order = 1)
    private Long id;

    @DorisField(value = "user_name", order = 2)
    private String name;

    @DorisField(order = 3)
    private Integer age;

    @DorisField(value = "account_status", order = 4)
    private Integer status;

    @DorisField(ignore = true)
    private String password;  // 忽略字段，不会映射到Doris

    private String email;     // 无注解字段，不会映射到Doris

    @DorisField(order = 5)
    private LocalDateTime createTime;
}
```

## 7. 业务层实现

UserService.java

```
package com.example.doris.service;

import com.example.doris.core.DorisStreamLoader;
import com.example.doris.entity.User;
import com.example.doris.util.DorisMapper;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
@RequiredArgsConstructor
publicclass UserService {
    privatefinal DorisStreamLoader dorisStreamLoader;

    /**
     * 批量更新用户状态
     */
    public void batchUpdateUserStatus(List<User> users) {
        // 添加额外字段（如更新时间）
        Map<String, Object> additionalFields = new HashMap<>();
        additionalFields.put("update_time",
            LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));

        // 自动映射字段（使用注解方式）
        List<Map<String, Object>> dorisData =
            DorisMapper.convertToDorisData(users, additionalFields);

        // 执行并行Stream Load（数据库名和表名作为参数传递拼接到HttpURL链接上）
        dorisStreamLoader.parallelStreamLoad(dorisData, "json",
                        UserProvider.getUser().getTenantDbConnectionString(), TableUtils.getTableName(DishAppManagementMapping.class));
    }

    /**
     * 批量创建用户
     */
    public void batchCreateUsers(List<User> users) {
        // 添加额外字段
        Map<String, Object> additionalFields = new HashMap<>();
        additionalFields.put("create_time",
            LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));

        // 自动映射字段
        List<Map<String, Object>> dorisData =
            DorisMapper.convertToDorisData(users, additionalFields);

         // 执行并行Stream Load（数据库名和表名作为参数传递拼接到HttpURL链接上）
        dorisStreamLoader.parallelStreamLoad(dorisData, "json",
                        UserProvider.getUser().getTenantDbConnectionString(), TableUtils.getTableName(DishAppManagementMapping.class));
    }
}
```

## 8. 配置类

DorisConfig.java

```
package com.example.doris.config;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@EnableConfigurationProperties(DorisStreamLoadProperties.class)
public class DorisConfig {

    @Bean
    public DorisStreamLoader dorisStreamLoader(@Qualifier("dorisStreamLoadProperties") DorisStreamLoadProperties properties) {
        returnnew DorisStreamLoader(properties);
    }
}
```

## 9. 应用配置 (application.yml)

```
doris:
  stream-load:
    url:http://doris-fe:8030/api/user_db/user_table/_stream_load
    username:admin
    password:"secure_password"
    connect-timeout:60000       # 连接超时60秒
    socket-timeout:300000       # 传输超时5分钟
    batch-size:100000           # 每批10万条
    max-retries:5               # 最大重试5次
    compression:gzip            # 启用GZIP压缩
    max-parallel:8              # 并行度8线程

# 可选：Jackson日期格式配置
spring:
jackson:
    date-format:yyyy-MM-ddHH:mm:ss
    time-zone:GMT+8
```

## 方案特点与优势

#### 1. 自动化字段映射

通过  `@DorisField`  注解自动完成实体到 Doris 字段的映射

- 支持字段重命名：  `@DorisField(value = "user_name")`
- 支持字段排序：  `@DorisField(order = 1)`
- 支持忽略字段：  `@DorisField(ignore = true)`

#### 2. 高性能处理

- 分批处理： 每批 10 万条数据
- 并行加载： 8 线程并行处理
- GZIP 压缩： 减少网络传输量
- 指数退避重试： 提高系统容错性

#### 3. 智能缓存优化

```
// 字段映射缓存（避免重复反射）
private static final Map<Class<?>, List<Field>> FIELD_CACHE = new ConcurrentHashMap<>();

public static List<Field> getAnnotatedFields(Class<?> clazz) {
    return FIELD_CACHE.computeIfAbsent(clazz, key -> {
        // 反射获取带注解字段并排序
    });
}
```

#### 4. 结果监控

```
try (CloseableHttpResponse response = httpClient.execute(httpPut)) {
     int statusCode = response.getStatusLine().getStatusCode();
     LoadResponse result = JSONObject.parseObject(EntityUtils.toString(response.getEntity()), LoadResponse.class);
     if (!result.getStatus().equals("Success")) {
         log.error("Stream Load失败: HTTP {} - {}", statusCode, result);
         throw new IOException("Doris Stream Load失败: " + result);
     }
     // 解析导入结果
     log.info("成功导入{}条数据, 耗时: {}ms",result.getNumberLoadedRows(),result.getLoadTimeMs());
}
```

#### 5. 运行效果

![运行效果](https://mmbiz.qpic.cn/mmbiz_png/JdLkEI9sZfc2n4bepmbGRXIl9oxxw5G198iazQTa2D3GmmxyexPvwVvCImSZ3NgXHI1dicfBZWkiaocUrTP9Gw53A/640?wx_fmt=png&from=appmsg)

运行效果

## 性能优化建议

调整批次大小：

```
doris:
  stream-load:
    batch-size: 50000  # 根据Doris集群性能调整
```

增加并行度：

```
max-parallel: ${CPU_CORES * 2}  # 通常为CPU核数的2倍
```

启用压缩：

```
compression: gzip  # 减少网络传输量
```

调整超时设置：

```
connect-timeout: 120000    # 大数据量场景增加超时
socket-timeout: 600000
```

Doris 集群优化：

```
-- 增加BE内存限制
SET GLOBAL streaming_load_max_mb = 4096;

-- 增加并行任务数
SET GLOBAL max_running_txn_num_per_db = 1024;
```

此方案完全避免了手动字段映射，通过注解方式自动完成实体到 Doris 字段的映射，同时保持字段顺序一致性。相比 JDBC 批量更新，性能可提升 20-50 倍，特别适合海量数据更新场景。

[加入小哈的星球](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / Java 学习路线 / **社群讨论 / **学习打卡 / 每月赠书**

- 《仿小红书（微服务架构 ）》 已完结，基于 Spring Cloud Alibaba + Spring Boot 3.x + JDK 17..., [点击查看项目介绍](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247538491&idx=1&sn=576995017721766d0fe15723fd135619&chksm=fd5787bdca200eab54d2fb8ca07fcc2bffdec3eaab4ab82ab5eaf949f0254c1683455e02010b&token=343952052&lang=zh_CN&scene=21#wechat_redirect) ； 演示地址： http://116.62.199.48:7070/
- 《 Spring AI 应用（RAG 智能客服） 》已完结, 基于 Spring AI 2.x + Spring Boot 4.x + JDK 21
- 《 秒杀系统设计 》正在更新中，单体到微服务高并发架构演进

- 《 前后端分离博客项目（全栈开发） 》 已完结,演示链接： http://116.62.199.48/
- 项目阅读地址： https://quanxiaoha.com/column

截止目前，**累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/sTnayibHfVq6k58yrsWFU0zS4MhOFVPH9ib8lFF40iahdfmiaz8IicbvIfia8icp3F3Y5OG1BJAKthCic72w2IiboDVBicYA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&randomid=65h7dnft&retryload=1&tp=webp#imgIndex=1)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/knmrNHnmCLEdM2gtRgy5eLztKXrUhee76MZ9wAicNPicsnAHPibicaSHUVqFkkibxWlrGO0acUxQmycZpqCNGcibaicxA/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&retryload=1&tp=webp#imgIndex=6)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~
2. 比 Xshell 还好用的 SSH 客户端神器，MobaXterm 太爱了！
3. 面试官：介绍一下 Kafka 的 ISR 机制？
4. 在 IDEA 里斗个地主不过分吧！
```

```

```

```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。
获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。
```

```
PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。
点“在看”支持小哈呀，谢谢啦
```

---
原文链接：https://mp.weixin.qq.com/s/rIkirRrhfQYfxqW1-lK39w
