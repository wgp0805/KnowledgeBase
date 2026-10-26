---
title: "Spring AI Alibaba -- 文生图、文生音及向量化 - NE_STOP"
source: "博客园"
url: "https://www.cnblogs.com/alineverstop/p/23413567"
date: "2026-10-23T06:29:00Z"
score: 0.9
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# Spring AI Alibaba -- 文生图、文生音及向量化 - NE_STOP

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/alineverstop/p/23413567  
> **抓取日期**: 2026-10-23  
> **相关性评分**: 0.9

# ChatMemory对话记忆

ChatMemory（Spring AI 里的聊天记忆接口）。

LLM 本身是**无状态** 的，你单独发一句消息，它不知道上一轮聊了啥。`ChatMemory` 就是 Spring AI 提供的**会话上下文管理器** ，用来保存当前对话的消息列表，每次请求自动把历史消息塞给大模型，实现连续对话。

由于大模型本身不存储数据，服务一重启，记忆的信息就丢失了，所以必须持久化。

## 四种记忆类型

  1. 内存存储

用于开发和测试的简单内存存储。

  2. 持久化存储

用于生产环境的数据库支持存储。

  3. 分布式存储

用于可扩展应用程序的分布式存储。

  4. 自定义存储

用于特定需求的自定义存储实现。




## 记忆持久化案例

需求：将客户和大模型的对话问答保存进Redis进行持久化存储。

  1. 新建一个module ，pom文件为
         
         <?xml version="1.0" encoding="UTF-8"?>
         <project xmlns="http://maven.apache.org/POM/4.0.0"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
             <modelVersion>4.0.0</modelVersion>
             <parent>
                 <groupId>com.ali</groupId>
                 <artifactId>springAiAlibaba-workV1</artifactId>
                 <version>1.0-SNAPSHOT</version>
             </parent>
         
             <artifactId>saa08-persistent</artifactId>
         
             <properties>
                 <maven.compiler.source>17</maven.compiler.source>
                 <maven.compiler.target>17</maven.compiler.target>
                 <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
             </properties>
             <dependencies>
                 <dependency>
                     <groupId>org.springframework.boot</groupId>
                     <artifactId>spring-boot-starter-web</artifactId>
                 </dependency>
                 <dependency>
                     <groupId>com.alibaba.cloud.ai</groupId>
                     <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
                 </dependency>
                 <dependency>
                     <groupId>org.projectlombok</groupId>
                     <artifactId>lombok</artifactId>
                     <optional>true</optional>
                 </dependency>
                 <dependency>
                     <groupId>com.alibaba.cloud.ai</groupId>
                     <artifactId>spring-ai-alibaba-starter-memory-redis</artifactId>
                 </dependency>
                 <dependency>
                     <groupId>redis.clients</groupId>
                     <artifactId>jedis</artifactId>
                 </dependency>
                 <dependency>
                     <groupId>org.projectlombok</groupId>
                     <artifactId>lombok</artifactId>
                 </dependency>
             </dependencies>
         </project>
         

  2. 配置文件内容
         
         server.port=8008
         # ?????????
         server.servlet.encoding.charset=UTF-8
         server.servlet.encoding.enabled=true
         server.servlet.encoding.force=true
         
         spring.application.name=saa08-persistent
         
         #springai ????config
         spring.ai.dashscope.api-key=${aliQwen-apikey}
         
         #redis config
         spring.data.redis.host=localhost
         spring.data.redis.port=6379
         spring.data.redis.connect-timeout=3
         spring.data.redis.database=0
         spring.data.redis.timeout=2
         

  3. 配置类（2个）
         
         @Configuration
         public class RedisMemoryConfig {
         
             @Value("${spring.data.redis.host}")
             private String host;
         
             @Value("${spring.data.redis.port}")
             private int port;
         
             @Bean
             public RedisChatMemoryRepository getRedisChatMemoryRepository() {
                 return RedisChatMemoryRepository.builder()
                         .host(host).port(port).build();
             }
         }
         



    
    
    @Configuration
    public class SaaLLMConfig {
    
        private final String DEEPSEEk_MODEL="deepseek-v3";
        private final String QWEN_MODEL="qwen-max";
    
        // 方式一
        @Value("${spring.ai.dashscope.api-key}")
        private String apiKey;
    
        // 配置大模型对外暴露的api
        @Bean(name = "deepseekChatModel")
        public ChatModel deepseekChatModel() {
        return DashScopeChatModel.builder()
                // 配置apikey
                .dashScopeApi(DashScopeApi.builder().apiKey(apiKey).build())
                // 配置模型
                .defaultOptions(DashScopeChatOptions.builder().withModel(DEEPSEEk_MODEL).build())
                .build();
        }
    
        @Bean(name = "qwenChatModel")
        public ChatModel qwenChatModel() {
            return DashScopeChatModel.builder()
                    // 配置apikey
                    .dashScopeApi(DashScopeApi.builder().apiKey(apiKey).build())
                    // 配置模型
                    .defaultOptions(DashScopeChatOptions.builder().withModel(QWEN_MODEL).build())
                    .build();
        }
    
        @Bean(name = "deepseekChatClient")
        public ChatClient deepseekChatClient(@Qualifier("deepseekChatModel") ChatModel deepseekChatModel,
                                             RedisChatMemoryRepository redisChatMemoryRepository) {
            // 配置消息窗口记忆，最多保留10条消息
            MessageWindowChatMemory messageWindowChatMemory = MessageWindowChatMemory.builder()
                    .chatMemoryRepository(redisChatMemoryRepository)
                    .maxMessages(10)
                    .build();
            return ChatClient.builder(deepseekChatModel)
                    .defaultAdvisors(MessageChatMemoryAdvisor.builder(messageWindowChatMemory).build())
                    .build();
        }
    
        @Bean("qwenChatClient")
        public ChatClient qwenChatClient(@Qualifier("qwenChatModel") ChatModel qwenChatModel,
                                         RedisChatMemoryRepository redisChatMemoryRepository)  {
            // 配置消息窗口记忆，最多保留10条消息
            MessageWindowChatMemory messageWindowChatMemory = MessageWindowChatMemory.builder()
                    .chatMemoryRepository(redisChatMemoryRepository)
                    .maxMessages(10)
                    .build();
            return ChatClient.builder(qwenChatModel)
                    .defaultAdvisors(MessageChatMemoryAdvisor.builder(messageWindowChatMemory).build())
                    .build();
        }
    }
    

  4. 控制类
         
         @RestController
         public class ChatMemoryController {
         
             @Resource(name = "deepseekChatClient")
             private ChatClient deepseekChatClient;
         
             @Resource(name = "qwenChatClient")
             private ChatClient qwenChatClient;
         
             /**
              * 对话记忆
              *
              * @param
              * @return
              */
             @GetMapping("/chatmemory/chat")
             public String chat(@RequestParam("msg") String msg,
                                @RequestParam("userId") String userId) {
         
                return qwenChatClient.prompt(msg).advisors(new Consumer<ChatClient.AdvisorSpec>() {
                     // 顾问增强器
                     @Override
                     public void accept(ChatClient.AdvisorSpec advisorSpec) {
                         advisorSpec.param("conversationId", userId);
                     }
                 }).call().content();
             }
         
         
             /**
              * 对话记忆
              *
              * @param
              * @return
              */
             @GetMapping("/chatmemory/chat2")
             public String chat2(@RequestParam("msg") String msg,
                                @RequestParam("userId") String userId) {
         
                 // 顾问增强器
                 return qwenChatClient.prompt(msg).advisors(advisorSpec -> advisorSpec.param("conversationId", userId))
                         .call().content();
             }
         




此时对话内容就保存到Redis中。

# 文生图

大模型一般使用阿里的Qwen-Image 或者Wan系列（通义万相）。

## 代码示例

这里的pom文件和配置文件使用上一篇的基础配置。

控制类如下：
    
    
    @RestController
    public class Text2ImageController {
    
        public static final String IMAGE_MODEL = "wanx2.1-t2i-turbo";
    
        @Resource
        private ImageModel imageModel;
    
    
    
        /**
         * 文生图
         * @param
         * @return
         */
        @GetMapping("/test2image/image")
        public String image(@RequestParam(name="msg",defaultValue = "刺猬") String msg) {
    
            return imageModel.call(
                            new ImagePrompt(msg, DashScopeImageOptions.builder().withModel(IMAGE_MODEL).build())
                    )
                    .getResult()
                    .getOutput()
                    .getUrl();
    
        }
    
    }
    

# 文生音

使用语音合成模型CosyVoice；音色使用longyingcui

直接给出控制类
    
    
    @RestController
    public class Text2VoiceController {
    
        // 文生音模型
        public static final String VOICE_MODEL = "cosyvoice-v2";
        // 音色选择
        public static final String VOICE_TIMBER = "longyingcui";
    
        @Resource
        private SpeechSynthesisModel speechSynthesisModel;
    
    
    
        /**
         * 文生音
         * @param
         * @return
         */
        @GetMapping("/test2voice/voice")
        public String voice(@RequestParam(name="msg",defaultValue = "您的美团外卖已自动为您接单了！") String msg) {
            String filePath = "d:/"+ UUID.randomUUID().toString()+".mp3";
            // 语音参数设置
            DashScopeSpeechSynthesisOptions options = DashScopeSpeechSynthesisOptions.builder()
                    .voice(VOICE_TIMBER)
                    .model(VOICE_MODEL)
                    .build();
            // 调用文生音接口
           SpeechSynthesisResponse response = speechSynthesisModel.call(new SpeechSynthesisPrompt(msg, options));
           // 字节流语音转换
            ByteBuffer audioData = response.getResult().getOutput().getAudio();
            // 将字节流写入文件
            FileOutputStream fos = null;
            try {
                fos = new FileOutputStream(filePath);
                fos.write(audioData.array());
                fos.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
            return filePath;
    
        }
    
    }
    

# 向量化

向量：表示具有大小和方向的量。

## 文本向量化

嵌入模型：Embedding Model

**嵌入模型就是专门用来做文本向量化的 AI 模型** ，输入文本，输出一组向量（嵌入向量 /embedding），核心目标是把语义信息编码进向量里。

嵌入的工作原理就是将文本、图形、视频转换为向量的浮点数数组。

## 向量数据库

专门用于存储、管理和检索向量的数据库系统。

向量数据库维度越高，查询精准度也越高，查询效果越好。

常用的向量数据库有Elasticsearch、Neo4j、OceanBase、PGvector、Redis Stack等

**Redis Stack = 原生 Redis + 一套官方扩展模块打包在一起的发行版** ，除了普通 Redis 的缓存能力，自带**RediSearch（检索 + 向量搜索）** 。

Redis 8.0 之后官方已经把这些模块内置进原版 Redis，Redis Stack 这个独立包标记为弃用了，新项目直接用 Redis 8+ 即可。

作用：

将文本 、图像、视频转换为向量，存储在数据库中。他们执行相似性搜索，而不是精确匹配。当给定一个向量做为查询时，VectorStore 返回与查询向量“相似”的向量。

  1. 捕捉复杂词汇关系（语义相似性、同义词、多义词）

  2. 向量嵌入为检索增强生成（RAG）应用程序提供支持




## 代码示例

  1. 新建一个module，pom为：
         
         <?xml version="1.0" encoding="UTF-8"?>
         <project xmlns="http://maven.apache.org/POM/4.0.0"
                  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
             <modelVersion>4.0.0</modelVersion>
             <parent>
                 <groupId>com.ali</groupId>
                 <artifactId>springAiAlibaba-workV1</artifactId>
                 <version>1.0-SNAPSHOT</version>
             </parent>
         
             <artifactId>saa11-Embed2vector</artifactId>
         
             <properties>
                 <maven.compiler.source>17</maven.compiler.source>
                 <maven.compiler.target>17</maven.compiler.target>
                 <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
             </properties>
             <dependencies>
                 <dependency>
                     <groupId>org.springframework.boot</groupId>
                     <artifactId>spring-boot-starter-web</artifactId>
                 </dependency>
                 <dependency>
                     <groupId>com.alibaba.cloud.ai</groupId>
                     <artifactId>spring-ai-alibaba-starter-dashscope</artifactId>
                 </dependency>
         <!--        Redis向量数据库-->
                 <dependency>
                     <groupId>org.springframework.ai</groupId>
                     <artifactId>spring-ai-starter-vector-store-redis</artifactId>
                 </dependency>
                 <dependency>
                     <groupId>org.projectlombok</groupId>
                     <artifactId>lombok</artifactId>
                     <optional>true</optional>
                 </dependency>
             </dependencies>
         </project>
         

  2. 配置文件为：
         
         server.port=8011
         # ?????????
         server.servlet.encoding.charset=UTF-8
         server.servlet.encoding.enabled=true
         server.servlet.encoding.force=true
         
         spring.application.name=saa11-Embed2vector
         
         #springai ????config
         spring.ai.dashscope.api-key=${aliQwen-apikey}
         spring.ai.dashscope.chat.options.model=qwen-plus
         spring.ai.dashscope.embedding.options.model=text-embedding-v3
         
         # Redis Stack
         spring.data.redis.host=192.168.220.128
         spring.data.redis.port=6379
         spring.data.redis.password=redis-stack
         spring.data.redis.username=default
         spring.ai.vectorstore.redis.initialize-schema=true
         spring.ai.vectorstore.redis.index-name=custom-index
         spring.ai.vectorstore.redis.prefix=custom-prefix
         

  3. 控制类
         
         @RestController
         public class Embed2VectorController {
         
             @Resource
             private EmbeddingModel embeddingModel;
         
             @Resource
             private VectorStore vectorStore;
         
             // 文本向量化
             @GetMapping("/embed2vector/text2embed")
             public EmbeddingResponse text2embed(@RequestParam("msg") String msg){
         
                 // 使用全局模型配置
                 //EmbeddingResponse embeddingResponse = embeddingModel.call(new EmbeddingRequest(List.of(msg),null);
                 // 使用特定模型
                 EmbeddingResponse embeddingResponse = embeddingModel.call(new EmbeddingRequest(List.of(msg),
                         DashScopeEmbeddingOptions.builder().withModel("text-embedding-v3").build()));
                 System.out.println(Arrays.toString(embeddingResponse.getResult().getOutput()));
                 return embeddingResponse;
             }
         
             // 文本向量化后存入向量数据库RedisStack
             @GetMapping("/embed2vector/add")
             public void add(){
                 List<Document> documents = List.of(
                         new Document("i study LLM"),
                         new Document("i love java")
                 );
                 vectorStore.add(documents);
             }
         
             // 从向量数据库RedisStack中查找。进行相似度查找
             @GetMapping("/embed2vector/get")
             public List getAll(@RequestParam("msg") String msg){
                 SearchRequest searchRequest = SearchRequest.builder()
                         .query(msg)
                         .topK(10)
                         .build();
                 List<Document> documents = vectorStore.similaritySearch(searchRequest);
                 System.out.println(documents);
                 return documents;
             }
         }
         





---
> 原文链接: https://www.cnblogs.com/alineverstop/p/23413567