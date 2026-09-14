---
title: "从零搭建ELK日志采集系统：Filebeat + Logstash + ES + Kibana 保姆级教程 - 佛祖让我来巡山"
source: "博客园"
url: "https://www.cnblogs.com/sun-10387834/p/22908497"
date: "2026-09-09T08:32:00Z"
score: 0.9
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 从零搭建ELK日志采集系统：Filebeat + Logstash + ES + Kibana 保姆级教程 - 佛祖让我来巡山

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/sun-10387834/p/22908497  
> **抓取日期**: 2026-09-09  
> **相关性评分**: 0.9

> 轻量级架构，一份配置全搞定

## 一、前言

你是不是还在用 `tail -f` 和 `grep` 在多台服务器上翻日志？系统一出问题，就要登录三五台机器，来回切换窗口，定位一个Bug耗时半小时。

ELK 是业界最成熟的日志集中管理方案。本文将带你用 **Docker Compose** 一键部署 **Filebeat + Logstash + Elasticsearch + Kibana** 四件套，所有服务容器化运行，配置完整注释，你只需要复制、修改路径、启动即可。

**架构特点** ：

  * 轻量级，无需Kafka中间件
  * Filebeat直接发送给Logstash，Logstash处理后存入ES
  * 适合中小规模项目（日日志量 < 500GB）



**前提条件** ：

  * Linux/macOS 或 Windows（WSL2）
  * 已安装 Docker 和 Docker Compose（版本 20.10+）
  * 至少 4GB 可用内存（推荐 8GB）
  * 你有一个正在运行的 Spring Boot 或其他 Java 应用，日志输出到某个目录



* * *

## 二、整体架构（数据流向）

flowchart LR App[Spring Boot应用] -->|"写入"| LogFile[/var/log/myapp/*.log/] LogFile -->|"tail读取"| FB[Filebeat] FB -->|"Beats协议:5044"| LS[Logstash] LS -->|"解析/过滤"| LS2[Logstash Filter] LS2 -->|"Bulk API:9200"| ES[Elasticsearch] ES -->|"查询"| Kibana[Kibana:5601] Kibana --> User[👤 开发者/运维] 

**每个环节的职责** ：

组件 | 角色 | 一句话功能  
---|---|---  
**Filebeat** | 采集器 | 监控日志文件变化，读取新行，发送给Logstash  
**Logstash** | 处理器 | 接收日志，用正则或JSON解析成结构化数据，输出到ES  
**Elasticsearch** | 存储&检索引擎 | 存储日志，建立倒排索引，支持全文检索  
**Kibana** | 可视化界面 | Web界面，搜索日志、制作图表  
  
* * *

## 三、准备工作：目录结构

我们将在当前目录下创建所有配置文件，整体结构如下：
    
    
    elk-demo/
    ├── docker-compose.yml          # 主编排文件
    ├── filebeat/
    │   └── filebeat.yml            # Filebeat 配置
    ├── logstash/
    │   └── pipeline/
    │       └── logstash.conf       # Logstash 管道配置
    └── elasticsearch/
        └── data/                   # ES数据目录（挂载卷，由docker自动创建）
    

执行以下命令创建目录：
    
    
    mkdir -p elk-demo/{filebeat,logstash/pipeline,elasticsearch/data}
    cd elk-demo
    

* * *

## 四、Docker Compose 完整配置

创建 `docker-compose.yml` 文件，内容如下（每行都有详细注释）：
    
    
    version: '3.8'
    
    # 定义网络，方便容器间通过服务名通信
    networks:
      elk-net:
        driver: bridge
    
    services:
      # =============================================
      # 1. Elasticsearch：存储与检索引擎
      # =============================================
      elasticsearch:
        image: docker.elastic.co/elasticsearch/elasticsearch:7.17.14
        container_name: elasticsearch
        environment:
          # 单节点模式
          - discovery.type=single-node
          # 关闭安全认证（简化演示，生产环境应开启）
          - xpack.security.enabled=false
          # JVM堆内存，建议物理内存的50%，但不超过32GB，这里给1GB
          - ES_JAVA_OPTS=-Xms1g -Xmx1g
        ports:
          - "9200:9200"   # REST API端口
          - "9300:9300"   # 节点间通信端口
        networks:
          - elk-net
        volumes:
          # 持久化ES数据，防止重启丢失
          - ./elasticsearch/data:/usr/share/elasticsearch/data
        # 生产环境需设置 ulimits
        ulimits:
          memlock:
            soft: -1
            hard: -1
          nofile:
            soft: 65536
            hard: 65536
    
      # =============================================
      # 2. Logstash：数据处理管道
      # =============================================
      logstash:
        image: docker.elastic.co/logstash/logstash:7.17.14
        container_name: logstash
        ports:
          # 暴露5044端口接收来自Filebeat的Beats协议数据
          - "5044:5044"
        networks:
          - elk-net
        volumes:
          # 挂载pipeline配置目录（里面放logstash.conf）
          - ./logstash/pipeline:/usr/share/logstash/pipeline
        depends_on:
          - elasticsearch   # 确保ES先启动
        environment:
          - LS_JAVA_OPTS=-Xmx512m   # Logstash JVM内存限制
    
      # =============================================
      # 3. Kibana：可视化前端
      # =============================================
      kibana:
        image: docker.elastic.co/kibana/kibana:7.17.14
        container_name: kibana
        environment:
          # 告诉Kibana ES的访问地址（服务名就是容器名）
          - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
          # 界面语言设为中文
          - I18N_LOCALE=zh-CN
        ports:
          - "5601:5601"
        networks:
          - elk-net
        depends_on:
          - elasticsearch
    
      # =============================================
      # 4. Filebeat：轻量级日志采集器
      # =============================================
      filebeat:
        image: docker.elastic.co/beats/filebeat:7.17.14
        container_name: filebeat
        # 以root身份运行，以便读取宿主机日志文件（生产环境可指定用户）
        user: root
        networks:
          - elk-net
        volumes:
          # 挂载Filebeat配置文件（只读）
          - ./filebeat/filebeat.yml:/usr/share/filebeat/filebeat.yml:ro
          # ========== 【重要】挂载应用日志目录 ==========
          # 将宿主机的日志路径映射到容器内，让Filebeat能读取
          # 请将 /path/to/your/app/logs 替换为你的实际日志目录
          - /path/to/your/app/logs:/var/log/myapp:ro
          # 挂载Filebeat数据目录（存放registry，记录读取位置，防止重启重复采集）
          - ./filebeat/data:/usr/share/filebeat/data
        depends_on:
          - logstash
        # 如果日志目录有权限问题，可添加以下环境变量
        environment:
          - TZ=Asia/Shanghai
    

**⚠️ 需要你替换的内容** ：

  * **`/path/to/your/app/logs`** ：改为你的Spring Boot应用实际输出日志的目录，例如 `/home/ubuntu/app/logs` 或 `/var/log/myapp`。



* * *

## 五、Filebeat 配置（`filebeat/filebeat.yml`）

创建 `filebeat/filebeat.yml`，内容如下：
    
    
    # ==============================================
    # Filebeat 配置文件
    # ==============================================
    
    # ---------- 输入（从哪里读日志） ----------
    filebeat.inputs:
    - type: log                    # 日志类型
      enabled: true                # 启用该输入
      paths:
        # 容器内路径，对应于宿主机挂载的日志目录
        - /var/log/myapp/*.log     # 请确保这里与docker-compose中的挂载路径一致
      
      # ---------- 多行处理（Java异常堆栈） ----------
      # 如果日志以日期时间开头，认为是一条新日志的开始
      multiline.pattern: '^\d{4}-\d{2}-\d{2}'
      multiline.negate: true       # 不匹配时合并到上一行
      multiline.match: after       # 合并在上一行之后
    
      # ---------- 添加自定义字段（便于日志分类） ----------
      fields:
        app_name: "my-springboot-app"    # 应用名称，可自定义
        env: "prod"                      # 环境标识
      fields_under_root: true            # 使fields成为顶级字段
    
    # ---------- 内部队列（调整吞吐性能） ----------
    queue.mem:
      events: 4096                 # 内存队列最大事件数
      flush.min_events: 1024      # 达到该数量即发送
      flush.timeout: 5s           # 超时强制发送
    
    # ---------- 输出（发往哪里） ----------
    output.logstash:
      # Logstash的服务名和端口（在docker-compose中定义为logstash）
      hosts: ["logstash:5044"]
    
    # ---------- 日志记录（Filebeat自身的日志） ----------
    logging.level: info
    logging.to_files: true
    logging.files:
      path: /var/log/filebeat
      name: filebeat
      keepfiles: 7
    

**配置要点说明** ：

  * `multiline` 配置处理 Java 异常堆栈，确保一个完整的异常作为一条事件发送。
  * `fields` 中可添加任何你想要的标签，后续在 Kibana 中可作为过滤条件。
  * `queue.mem` 调整攒批行为，适当调大 `flush.min_events` 可减少网络请求，提升吞吐。



* * *

## 六、Logstash 配置（`logstash/pipeline/logstash.conf`）

Logstash 的管道配置分为三个阶段：**input → filter → output** 。

创建 `logstash/pipeline/logstash.conf`：
    
    
    # ==============================================
    # Logstash 管道配置
    # ==============================================
    
    input {
      # 接收来自Filebeat的Beats协议数据
      beats {
        port => 5044
        # 可设置客户端IP白名单等，此处省略
      }
    }
    
    # ==============================================
    # 过滤器（数据解析与转换）
    # ==============================================
    filter {
      # ----- 情况1：如果你的日志已经是JSON格式（推荐） -----
      # 例如通过logback的logstash-encoder输出
      # 则直接解析JSON，无需Grok
      json {
        source => "message"
        # 如果解析失败，会标记 _jsonparsefailure，可忽略或处理
        skip_on_invalid_json => true
      }
    
      # ----- 情况2：如果是纯文本日志，使用Grok解析 -----
      # 取消下面注释，并注释掉上面的json块
      # grok {
      #   match => { 
      #     "message" => "%{TIMESTAMP_ISO8601:timestamp} \[%{LOGLEVEL:level}\] %{GREEDYDATA:message_content}" 
      #   }
      #   overwrite => [ "message" ]   # 将原始message替换为解析后的内容
      # }
    
      # ----- 通用处理：添加/修改字段 -----
      # 将时间字符串转为ES中的@timestamp字段（用于时间轴排序）
      if [timestamp] {
        date {
          match => [ "timestamp", "ISO8601" ]
          target => "@timestamp"
        }
      }
    
      # 删除原始message字段（如果已经解析成结构化数据，可减少存储量）
      # mutate { remove_field => [ "message" ] }
    
      # 添加一个静态字段标识数据来源
      mutate {
        add_field => { "data_source" => "filebeat" }
      }
    }
    
    # ==============================================
    # 输出（发往Elasticsearch）
    # ==============================================
    output {
      elasticsearch {
        # ES服务地址（docker-compose中的服务名）
        hosts => ["elasticsearch:9200"]
        # 索引名称模式：按天切分，便于管理
        index => "app-logs-%{+YYYY.MM.dd}"
        # 批量写入大小
        bulk_size => 5000
        # 超时时间
        bulk_timeout => "60s"
        # 如果不想使用默认的模板，可自定义
        # template => "/usr/share/logstash/templates/my-template.json"
        # template_name => "my-app-logs"
      }
    
      # 调试时输出到控制台（查看容器日志可见）
      stdout {
        codec => rubydebug
      }
    }
    

**注意** ：如果你的应用日志已经输出为 JSON 格式（通过 Logback 的 `logstash-logback-encoder`），则使用 `json` 过滤器效率最高，无需 Grok 正则。如果应用输出的是纯文本，请注释掉 `json` 块，启用 `grok` 块，并根据你的日志格式调整正则表达式。

* * *

## 七、启动服务

所有配置就绪后，在 `elk-demo` 目录下执行：
    
    
    # 启动所有容器（后台运行）
    docker-compose up -d
    
    # 查看容器状态
    docker-compose ps
    
    # 查看实时日志
    docker-compose logs -f
    

如果启动成功，你应该能看到四个容器都在运行。如果 Filebeat 挂载的日志目录存在且有日志文件，Filebeat 会立即开始读取并发送。

* * *

## 八、验证日志链路

### 1\. 检查 Elasticsearch 是否正常

访问 `http://localhost:9200`，应返回 JSON 信息。

### 2\. 检查索引是否创建
    
    
    curl -X GET "localhost:9200/_cat/indices?v"
    

如果看到 `app-logs-2026.09.09` 类似的索引，说明日志已写入。

### 3\. 在 Kibana 中查看日志

  1. 访问 `http://localhost:5601`
  2. 左侧菜单 → **Stack Management → Index Patterns**
  3. 点击 **Create index pattern**
  4. 输入 `app-logs-*`，点击 Next step
  5. 选择 **@timestamp** 作为时间字段，点击 Create
  6. 左侧菜单 → **Discover** ，选择刚创建的索引模式，即可看到日志列表



在搜索框中可以输入条件过滤，例如：

  * `level: "ERROR"` → 只查错误日志
  * `app_name: "my-springboot-app"` → 查特定应用
  * `message: "超时"` → 包含关键词



![image](https://img2024.cnblogs.com/blog/1465907/202609/1465907-20260909162947190-195439361.png)

* * *

## 九、常见问题与避坑指南

### 9.1 Filebeat 无法读取日志文件（权限问题）

**现象** ：容器日志显示 `permission denied`。  
**解决** ：在 `docker-compose.yml` 中 Filebeat 服务添加 `user: root`（已添加），或确保宿主机日志目录对 other 有读权限（`chmod o+r`）。

### 9.2 Logstash 无法连接 Elasticsearch

**现象** ：Logstash 日志报错 `Connection refused`。  
**解决** ：确保 Elasticsearch 容器已完全启动，且环境变量 `ELASTICSEARCH_HOSTS` 配置正确。可以进入 Logstash 容器用 `curl elasticsearch:9200` 测试连通性。

### 9.3 Kibana 中看不到日志

  * 检查索引模式是否创建正确（名称与 Logstash 输出的索引一致）。
  * 检查 Discover 页面的时间选择器是否正确（例如选择 “Last 15 minutes”）。
  * 检查 Elasticsearch 中是否有数据（用 `_cat/indices` 命令查看）。



### 9.4 日志重复或丢失

Filebeat 维护一个 registry 记录读取位置，如果挂载了 `data` 目录，重启后不会重复读取。如果发现重复，可以删除 `./filebeat/data` 目录（会丢失进度），但生产环境不建议。

### 9.5 容器启动顺序问题

Docker Compose 的 `depends_on` 仅保证启动顺序，不保证服务完全就绪。如果 Logstash 启动时 ES 还未就绪，会重试，最终会连接成功。

### 9.6 磁盘空间不足

ES 默认不限制索引保留时间，建议配置 ILM（索引生命周期管理）自动删除过期数据。简单方式：在 Kibana 中创建 ILM 策略，或定期执行 curl 删除旧索引。

* * *

## 十、进阶优化建议

优化点 | 建议  
---|---  
**日志格式** | 在 Spring Boot 中配置 Logback 输出 JSON 格式（使用 `logstash-logback-encoder`），可避免 Logstash 的 Grok 解析，极大提升性能。  
**Filebeat 多行合并** | 根据你的日志格式调整 `multiline.pattern`，确保异常堆栈完整采集。  
**Logstash 性能** | 调整 `pipeline.workers` 和 `pipeline.batch.size`（在 `logstash.yml` 中配置），适应日志量。  
**ES 内存** | 根据物理内存调整 `ES_JAVA_OPTS`，至少分配 2GB。  
**索引生命周期** | 配置 ILM 自动将超过 7 天的索引转为只读或删除，保持集群健康。  
**监控告警** | 为 ELK 组件添加监控（如 Prometheus + Grafana），及时发现问题。  
  
* * *

## 十一、总结

通过本教程，你已经拥有了一套完整的 ELK 日志采集系统：

  * **Filebeat** 实时采集日志文件，通过 Beats 协议发送给 **Logstash**
  * **Logstash** 解析并结构化日志，存入 **Elasticsearch**
  * **Kibana** 提供强大的搜索和可视化界面



所有服务运行在 Docker 容器中，配置完全透明，你可以随时调整。这种架构适合大多数中小企业及开发测试环境，足够稳定且易于维护。

现在，当线上出现问题时，你只需打开 Kibana，输入关键词，就能在几秒内定位到具体日志，排查效率提升 10 倍以上。

**下一步行动** ：

  1. 将你的应用日志目录挂载到 Filebeat 容器中
  2. 根据你的日志格式，调整 Logstash 的解析规则
  3. 在 Kibana 中创建仪表盘，监控关键指标



如果在实践中遇到问题，欢迎在评论区留言交流！


---
> 原文链接: https://www.cnblogs.com/sun-10387834/p/22908497