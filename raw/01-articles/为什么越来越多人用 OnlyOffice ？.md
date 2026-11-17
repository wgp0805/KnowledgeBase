---
title: "为什么越来越多人用 OnlyOffice ？"
source: "https://mp.weixin.qq.com/s/eLa-tr9rWNQKzQ-ljThrJw"
author:
  - "[[苏三]]"
published:
created: 2026-11-17
description:
tags:
  - "clippings"
---
苏三 苏三说技术 *2026年11月17日 08:20*

## 大家好，我是苏三，又跟大家见面了。

## 前言

做企业项目的小伙伴应该都遇到过这样的需求。

业务部门提需求说：系统需要有在线编辑 Word的功能，客户不想下载下来改完再传回去。

你一想这需求挺正常，然后开始找方案，发现怎么走都不顺。

绕不开的第一件事是私有化部署。

如果客户是国企或者金融机构，数据不能出内网，必须部署在自己的服务器或私有云上。

SaaS 方案第一步就卡死，数据出境这关过不去。

第二件事，业务系统要嵌入文档编辑能力。

不是让用户跳到某个独立平台去改文件，而是在自己的系统里直接打开、编辑、保存，改完还能回到业务流程里接着走。

第三件事，开发成本要可控。

买商业 SDK，按人头收费，五百个用户一年下来够养半个前端团队，预算会上根本没法交代。

自研呢，光把.docx 在浏览器里渲染得跟 Word 差不多，就够一个小组折腾大半年，更别提协同算法和格式兼容。

三条路都试过，都不太通。

那该怎么办呢？

今天这篇文章就专门跟大家一起聊聊OnlyOffice，它可以帮我们解决这些问题。

## 二、OnlyOffice 是什么？

OnlyOffice是一个可私有化部署的在线文档编辑引擎，支持 Word、Excel、PPT、PDF 和表单的查看与编辑，通过 API 嵌进你自己的系统。  

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/3fa7b628f739dc8ccf411ea8c9a85336_MD5.webp)

它不是网盘，也不是要替代你业务系统的协作平台。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/7c2f36e74dc5280fa178bca6c5f30b16_MD5.png)

你可以把它当成一块“文档编辑能力”的积木。

用户、权限、文件存储、业务流程，还是你自己的系统管，它只负责把那个.docx 在浏览器里打开、让人改、改完通知你存回去。

版本上分三条线：开源社区版、企业版、开发者版。

三者核心编辑功能基本一致，区别在授权方式和高级功能。

社区版免费，AGPL [v.3](http://v.3) 协议，适合小团队和测试。

企业版是商业授权，面向企业内部部署，多了管理面板、高级安全配置和技术支持。

开发者版同样商业授权，核心差异是白标——能换掉 Logo、改主题色、把“关于”页面换成你自己的品牌。

## 三、四个与开发者相关的能力

### 3.1 API 集成

这是 OnlyOffice 最核心的能力，也是开发者接触它的第一道门。

集成模型不复杂，就三件事： **后端生成 config、前端加载编辑器、文档服务回调你的接口保存** 。

**config 机制** 。

你的后端生成一个 JSON，里面描述这份文档的一切：文件类型、文档地址、权限、用户信息、界面语言、回调地址。这个 JSON 交给前端，前端拿它初始化编辑器。

config 里放什么、不放什么，完全由你控制。官方文档的集成示例里，config 就是编辑器的“说明书”。

**前端加载** 。

你的页面里放一个 div，引入 ONLYOFFICE 的 `              api.js            ` ，然后 `new              DocsAPI.DocEditor("div-id",            config)` ，编辑器就渲染在那个 div 里。

用户看到的是你系统里的一个页面，背后是 ONLYOFFICE 在渲染文档。

**回调保存** 。

用户在编辑器里改完，ONLYOFFICE 在保存时机向你的 `callbackUrl` 发 POST 请求，body 里带状态码和文档下载地址。

你的后端收到之后，下载新文件、覆盖存储、返回成功。整个闭环就完成了。

**50+ 连接器** 。

官方准备了 50 多个现成连接器，覆盖 Nextcloud、Moodle、Odoo、WordPress、SharePoint 这些常见系统。

如果你的系统正好是其中之一，接起来很快。

但更实用的是另一件事：你可以一个连接器都不用，直接拿 API 从零嵌进自己的业务系统。官方连接器本质上是这套 API 的现成用法示例，看懂一个，自己写就不难。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/460265bd3157032d6258bd82e0864c7e_MD5.png)

config 进入、文件被拉取、保存时回调，三步闭环。

### 3.2 私有化部署

这个能力是很多人第一次试 OnlyOffice 的直接原因。

**部署形态** 。

OnlyOffice 文档支持部署在本地服务器、私有云、完全离线的内网环境。

官方下载页提供 Windows、Linux 安装包，也提供 Docker 镜像。

企业版产品页写得很明确：自托管部署，数据保留在你自己的基础设施内，无第三方数据访问。

**Docker 一行跑起来** 。最快的方式就是 Docker：

```
docker run -i -t -d -p 8080:80 onlyoffice/documentserver
```

挂载数据目录、配好 JWT，服务就在你机器上跑起来了。

本地、私有云、离线内网，用的都是这套。

**为什么这件事重要** 。

数据在自己手里，金融、医疗、政府这类客户的合规门槛才谈得上满足。

文档、用户数据、审计日志全在你的基础设施里，OnlyOffice 官方碰不到你的数据。

SaaS 方案给不了这个保证，自研又扛不住成本，私有化部署恰好卡在中间那个位置。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/f6ed7fe3236d656ff95a7c6040907fd5_MD5.png)

文档服务、文件存储、日志全在你自己的基础设施内，官方不接触数据。

### 3.3 协作能力

协作是内置的，不是外挂插件。

**实时编辑** 。

多人同时打开同一份文档，能看到彼此的光标、选区和在线状态。

协同有两种模式：快速模式实时显示所有人的改动，严格模式锁定段落，让你专注写自己的部分不受干扰。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/1da5bdd8371c2d122771b4b2db32d88b_MD5.jpg)

**评论** 。

选中一段文字加评论，可以 @ 提及协作者。

评论和修订可以并存，适合审阅流程。

**版本历史** 。

编辑器里能查看文档的历史版本，对比差异、回滚到某个版本。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/32ddf9471665ffe80776f17c5d16e62b_MD5.png)

对于需要留痕的业务场景（合同、报告、审批稿），这个能力是刚需。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/1e606a34ee77de5ac53eb832cc30bb81_MD5.png)

多个浏览器窗口并排，不同账号编辑同一文档，能看到对方彩色光标和头像。

### 3.4 白标能力

白标是开发者版的核心差异，也是做 SaaS 的人最在意的一点。

**换什么** 。

通过 `              editorConfig.customization            ` ，可以换掉编辑器界面里的 Logo、深色主题 Logo、点击 Logo 跳转的 URL、关于页面里的公司名称、地址、邮箱等信息。

主题色也能改。

客户看到的是你的品牌，不是“由 OnlyOffice 提供技术支持”。

**为什么重要** 。

做 SaaS 产品卖给客户，品牌一致性是产品体验的一部分。

如果你的产品里突然冒出一个第三方 Logo，客户会问“这是谁”，信任感会打折。

白标能力让 OnlyOffice 变成你产品里“看不见的引擎”。

**补充一句** ：OnlyOffice 支持离线 AI，但不是自托管后开箱就能用的。需要额外部署本地模型、做配置，是另一套工程。

## 四、实战演示：Spring Boot 接入

流程就四步：Docker 部署、后端生成 config、前端加载编辑器、处理保存回调。

这里先把示例工程的结构交代清楚。

后面的代码都来自 `onlyoffice-springboot` ，项目使用 Spring Boot 3.4.5 和 Java 17，不额外引入 JWT 框架，签名和验签直接用 JDK 的 `HmacSHA256` 完成：

```
onlyoffice-springboot/
├── config/
            OnlyOfficeProperties.java
          
├── controller/
│   ├── 
            DocumentController.java
          
│   ├── 
            FileController.java
          
│   └── 
            OnlyOfficeController.java
          
├── service/
│   ├── 
            DocumentStorageService.java
          
│   ├── 
            FileAccessService.java
          
│   ├── 
            JwtService.java
          
│   └── 
            OnlyOfficeCallbackService.java
          
└── resources/static/
    ├── 
            index.html
          
    └── 
            editor.html
```

**第一步，Docker 部署，带上 JWT 配置。**

```
docker run -i -t -d -p 8080:80 \
  -e JWT_ENABLED=true \
  -e JWT_SECRET=susantest123456 \
  -v /data/onlyoffice/data:/var/www/onlyoffice/Data \
  onlyoffice/documentserver
```

`JWT_SECRET` 记下来，后端生成 config 和校验回调都得用它。

不设或者设个弱密钥，等于把文档服务裸奔在公网上，别这么干。

Docker 跑起来之后，别急着写代码，先花两分钟确认服务是真的就绪了。

先查一下实际容器名或 ID：

```
docker ps
```
![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/04c90ac297b1d991eda54b3e75340f4a_MD5.png)

更严谨一点的做法是在容器内查一下版本信息：

```
docker exec 3eff4ef3b2b6 curl -s http://127.0.0.1:8000/info/
            info.json
           | grep buildVersion
```

正常会返回类似 `"buildVersion":"10.0.0"` 的输出。

注意别在宿主机上直接 curl 容器的 8000 端口，那个端口没映射出来，查不到是正常的。

最直接的办法是浏览器访问 `http://你的服务器IP:8080/welcome/` ，看到 “ONLYOFFICE Docs Community Edition installed” 的欢迎页，就说明主体服务起来了。

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/ccc990a737f037478f5a079c09d7636e_MD5.png)

如果页面打不开，先 `docker ps` 看容器状态是不是 Up，再 `docker logs` 看有没有报错。

JWT 配置有没有生效，也顺手确认一下：

```
docker exec 3eff4ef3b2b6 
            documentserver-jwt-status.sh
```

这个命令会显示当前 JWT 的启用状态和密钥，你拿它跟 `docker run` 里设的 `JWT_SECRET` 对一下，一致就说明配置没问题。

后面后端生成 config 和校验回调时用的就是这个密钥，对不上编辑器会白屏报“文档安全令牌格式不正确”。

项目里的配置入口如下，下面是 `              application.yml            ` 的配置片段：

```
server:
  port: ${SERVER_PORT:8081}
 address: 0.0.0.0

onlyoffice:
 docs-url: ${ONLYOFFICE_DOCS_URL:http://localhost:8080}
 public-app-url: ${APP_PUBLIC_URL:
            https://your-app.example.com}
          
 jwt-secret: ${ONLYOFFICE_JWT_SECRET:}
 storage:
    directory: ${DOCUMENT_STORAGE_DIR:./data/documents}
```

这里要特别提醒一句： `docs-url` 是浏览器加载 `              api.js            ` 使用的地址， `public-app-url` 是 ONLYOFFICE 服务端下载文件和发送回调使用的地址。

本地调试时， `public-app-url` 不能随手写成 `http://localhost:8081` 。

远程文档服务访问不到你电脑上的 localhost，最后还是会在保存时提示“这份文件无法保存”。

下面是 `JwtService` 的核心源码片段，负责给 config 和文件下载地址签发 HS256 令牌，同时校验回调请求：

```
@Service
public class JwtService {

    private static final Base64.Encoder BASE64_URL_ENCODER =
            
            Base64.getUrlEncoder().withoutPadding();
          
    private static final Base64.Decoder BASE64_URL_DECODER =
            
            Base64.getUrlDecoder();
          
    private static final TypeReference<Map<String, Object>> MAP_TYPE =
            new TypeReference<>() {};

    private final ObjectMapper objectMapper;
    private final OnlyOfficeProperties properties;

    public JwtService(ObjectMapper objectMapper, OnlyOfficeProperties properties) {
        this.objectMapper = objectMapper;
        this.properties = properties;
    }

    public String sign(Map<String, Object> claims) {
        if (!
            properties.jwtEnabled())
           {
            throw new IllegalStateException("
            onlyoffice.jwt-secret
           未配置");
        }

        try {
            Map<String, Object> payload = new LinkedHashMap<>(claims);
            long now = 
            Instant.now().getEpochSecond();
          
            
            payload.putIfAbsent(
          "iat", now);
            
            payload.putIfAbsent(
          "exp", now + 3600);

            String header = encodeJson(
            Map.of(
          "alg", "HS256", "typ", "JWT"));
            String body = encodeJson(payload);
            String signingInput = header + "." + body;
            return signingInput + "."
                    + 
            BASE64_URL_ENCODER.encodeToString(hmac(signingInput));
          
        } catch (Exception exception) {
            throw new IllegalStateException("生成 JWT 失败", exception);
        }
    }

    public Map<String, Object> verify(String token) {
        if (!
            properties.jwtEnabled())
           {
            return 
            Map.of();
          
        }
        if (token == null || 
            token.isBlank())
           {
            throw new IllegalArgumentException("请求缺少 JWT");
        }

        try {
            String[] parts = 
            token.split(
          "\\.");
            if (
            parts.length
           != 3) {
                throw new IllegalArgumentException("JWT 格式错误");
            }

            String signingInput = parts[0] + "." + parts[1];
            byte[] expected = hmac(signingInput);
            byte[] actual = 
            BASE64_URL_DECODER.decode(parts[
          2]);
            if (!
            MessageDigest.isEqual(expected,
           actual)) {
                throw new IllegalArgumentException("JWT 签名无效");
            }

            Map claims = 
            objectMapper.readValue(
          
                    
            BASE64_URL_DECODER.decode(parts[
          1]), MAP_TYPE);
            Number expiresAt = (Number) 
            claims.get(
          "exp");
            if (expiresAt != null
                    && 
            expiresAt.longValue()
           < 
            Instant.now().getEpochSecond())
           {
                throw new IllegalArgumentException("JWT 已过期");
            }
            return claims;
        } catch (IllegalArgumentException exception) {
            throw exception;
        } catch (Exception exception) {
            throw new IllegalArgumentException("JWT 校验失败", exception);
        }
    }

    private String encodeJson(Map<String, Object> value) throws Exception {
        return 
            BASE64_URL_ENCODER.encodeToString(
          
                
            objectMapper.writeValueAsBytes(value));
          
    }

    private byte[] hmac(String input) throws GeneralSecurityException {
        Mac mac = 
            Mac.getInstance(
          "HmacSHA256");
        
            mac.init(
          new SecretKeySpec(
                
            properties.jwtSecret().getBytes(StandardCharsets.UTF_8),
          
                "HmacSHA256"));
        return 
            mac.doFinal(input.getBytes(StandardCharsets.UTF_8));
          
    }
}
```

这段代码里有两个关键点。

第一，比较签名用 `              MessageDigest.isEqual            ` ，没有直接比较普通字符串。

第二，config 和文件下载各自使用独立令牌。config 令牌供 ONLYOFFICE 校验编辑器配置，下载令牌会额外带 `fileId` 和 `purpose` ，只允许文档服务拉取指定文件。两类权限不混用，后面排查也清楚。

**第二步，后端生成 config。**

两个地方要留意： [document.key](http://document.key/) 怎么生成，文件怎么访问。

```
@GetMapping("/config/{fileId}")
public Map<String, Object> getConfig(@PathVariable Long fileId) {
    StoredFile file = 
            fileRepository.mustFind(fileId);
          
    // key 用 文件ID + 版本号
    String documentKey = 
            file.getId()
           + "_" + 
            file.getVersion();
          

    Map<String, Object> document = new LinkedHashMap<>();
    
            document.put(
          "fileType", "docx");
    
            document.put(
          "key", documentKey);
    
            document.put(
          "title", 
            file.getOriginalName());
          
    // 这个 url 是 ONLYOFFICE 服务端去拉的，不是浏览器
    
            document.put(
          "url", "
            https://your-app.com/api/files/"
           + fileId + "/download");

    Map<String, Object> editorConfig = new LinkedHashMap<>();
    
            editorConfig.put(
          "callbackUrl", "
            https://your-app.com/api/office/callback/"
           + fileId);
    
            editorConfig.put(
          "lang", "zh-CN");
    
            editorConfig.put(
          "user", 
            Map.of(
          "id", currentUserId(), "name", currentUserName()));

    Map<String, Object> config = new LinkedHashMap<>();
    
            config.put(
          "document", document);
    
            config.put(
          "editorConfig", editorConfig);
    
            config.put(
          "token", 
            jwtSigner.sign(config));
          
    return config;
}
```

`              document.key            ` 用“文件 ID + 版本号”，保存成功后版本号加一，下次打开自然就是新 key。

别拿文件名或者时间戳随手拼，容易出问题。

项目里把上面的 config 生成逻辑补成了下面这样。

下面是 `OnlyOfficeController` 的核心源码片段，权限、用户、回调和配置签名都在这里收口：

```
@GetMapping("/config/{id}")
public Map<String, Object> config(
        @PathVariable String id,
        @RequestParam(defaultValue = "demo-user") String userId,
        @RequestParam(defaultValue = "演示用户") String userName,
        @RequestParam(defaultValue = "edit") String mode) {

    DocumentInfo file = 
            storageService.get(id);
          
    String normalizedMode = "view".equalsIgnoreCase(mode) ? "view" : "edit";

    Map<String, Object> document = new LinkedHashMap<>();
    
            document.put(
          "fileType", 
            file.fileType());
          
    
            document.put(
          "key", 
            file.documentKey());
          
    
            document.put(
          "title", 
            file.name());
          
    
            document.put(
          "url", 
            fileAccessService.createDownloadUrl(file.id()));
          
    
            document.put(
          "permissions", 
            Map.of(
          
            "edit", "edit".equals(normalizedMode),
            "download", true,
            "print", true
    ));

    Map<String, Object> customization = new LinkedHashMap<>();
    
            customization.put(
          "autosave", true);
    
            customization.put(
          "compactHeader", false);
    
            customization.put(
          "comments", true);
    
            customization.put(
          "feedback", false);
    
            customization.put(
          "forcesave", false);
    
            customization.put(
          "help", false);
    
            customization.put(
          "hideRightMenu", false);

    Map<String, Object> editorConfig = new LinkedHashMap<>();
    
            editorConfig.put(
          "mode", normalizedMode);
    
            editorConfig.put(
          "lang", "zh-CN");
    
            editorConfig.put(
          "callbackUrl", 
            properties.publicUrl(
          
            "/api/office/callback/" + 
            file.id()));
          
    
            editorConfig.put(
          "user", 
            Map.of(
          
            "id", safeUserValue(userId, "demo-user"),
            "name", safeUserValue(userName, "演示用户")
    ));
    
            editorConfig.put(
          "customization", customization);
    
            editorConfig.put(
          "coEditing", 
            Map.of(
          "mode", "fast", "change", true));

    Map<String, Object> config = new LinkedHashMap<>();
    
            config.put(
          "type", "desktop");
    
            config.put(
          "documentType", documentType(
            file.fileType()));
          
    
            config.put(
          "document", document);
    
            config.put(
          "editorConfig", editorConfig);
    
            config.put(
          "width", "100%");
    
            config.put(
          "height", "100%");
    if (
            properties.jwtEnabled())
           {
        
            config.put(
          "token", 
            jwtService.sign(config));
          
    }

    Map<String, Object> response = new LinkedHashMap<>(config);
    
            response.put(
          "docsApiUrl", 
            properties.docsApiUrl());
          
    
            response.put(
          "documentInfo", file);
    return response;
}

private String documentType(String fileType) {
    return switch (fileType) {
        case "xls", "xlsx", "csv" -> "cell";
        case "ppt", "pptx" -> "slide";
        case "pdf" -> "pdf";
        default -> "word";
    };
}
```

这里有一个顺序不能弄反：先把 `document` 和 `editorConfig` 填完整，再对整份 config 签名。

签名内容必须与前端实际拿到的配置一致。

文件访问方式这块，url 是 ONLYOFFICE 服务端去请求的，不是浏览器直接请求。

文件如果在内网，得确保文档服务容器能访问到那个地址，不然浏览器能下载、编辑器却一直转圈报下载失败。

项目里没有直接把 `/api/files/{id}/download` 裸奔出去，而是给文档服务签发一枚 15 分钟有效的下载令牌。

下面是 `FileAccessService` 的源码实现：

```
@Service
public class FileAccessService {

    private final JwtService jwtService;
    private final OnlyOfficeProperties properties;

    public FileAccessService(
            JwtService jwtService,
            OnlyOfficeProperties properties) {
        this.jwtService = jwtService;
        this.properties = properties;
    }

    public String createDownloadUrl(String documentId) {
        String path = "/api/files/" + documentId + "/download";
        if (!
            properties.jwtEnabled())
           {
            return 
            properties.publicUrl(path);
          
        }

        Map<String, Object> claims = new LinkedHashMap<>();
        
            claims.put(
          "fileId", documentId);
        
            claims.put(
          "purpose", "document-download");
        
            claims.put(
          "iat", 
            Instant.now().getEpochSecond());
          
        
            claims.put(
          "exp", 
            Instant.now().plusSeconds(
          900).getEpochSecond());

        String token = 
            jwtService.sign(claims);
          
        return 
            UriComponentsBuilder.fromUriString(properties.publicUrl(path))
          
                .queryParam("access_token", token)
                .build(true)
                .toUriString();
    }

    public void verifyDownload(String documentId, String token) {
        if (!
            properties.jwtEnabled())
           {
            return;
        }

        Map claims = 
            jwtService.verify(token);
          
        if (!
            documentId.equals(claims.get(
          "fileId"))
                || !"document-download".equals(
            claims.get(
          "purpose"))) {
            throw new IllegalArgumentException("下载令牌与文档不匹配");
        }
    }
}
```

文档服务真正拉取文件时，会请求类似下面的地址：

```
https://your-app.example.com/api/files/welcome-word/download?access_token=eyJ...
```

下载接口先验令牌，再从存储读取文件：

```
@GetMapping("/{id}/download")
public ResponseEntity<byte[]> download(
        @PathVariable String id,
        @RequestParam(name = "access_token", required = false)
        String accessToken) {

    
            fileAccessService.verifyDownload(id,
           accessToken);
    DocumentInfo document = 
            storageService.get(id);
          
    byte[] content = 
            storageService.read(id);
          

    HttpHeaders headers = new HttpHeaders();
    
            headers.setContentType(mediaType(document.fileType()));
          
    
            headers.setContentDisposition(ContentDisposition.attachment()
          
            .filename(
            document.name(),
           
            StandardCharsets.UTF_8)
          
            .build());
    
            headers.setCacheControl(CacheControl.noStore().cachePrivate()
          
            .maxAge(
            Duration.ZERO));
          
    return 
            ResponseEntity.ok().headers(headers).body(content);
          
}
```

不带 `access_token` 请求这个接口时，项目会直接返回 `400` 。

这样浏览器知道文件 ID，也拿不到文档内容；只有拿到后端签发的短效令牌，文档服务才能完成拉取。

**第三步，前端加载编辑器。**

```
<div id="office-editor" style="width:100%; height:100vh;"></div>
<script src="https://your-docserver/web-apps/apps/api/documents/
            api.js"
          ></script>
<script>
const config = await fetch(\`/api/office/config/${fileId}\`).then(r => r.json());
new DocsAPI.DocEditor("office-editor", config);
</script>
```

项目里没有把 `              api.js            ` 写死在页面中，而是先请求 config，再从 config 返回的 `docsApiUrl` 动态加载脚本。

下面是 `              editor.js            ` 的核心源码片段：

```
async function startEditor() {
 const query = new URLSearchParams({ userId, userName, mode });
 const response = await fetch(
    \`/api/office/config/${encodeURIComponent(documentId)}?${query}\`,
    { cache: "no-store" }
  );
 const config = await response.json();
 if (!response.ok) {
    throw new Error(config.message || "无法获取编辑器配置");
  }

 await loadDocsApi(config.docsApiUrl);
  config.events = {
    onAppReady: () => {
      loadingPanel.hidden = true;
    },
    onDocumentReady: () => {
      setStatus("saved", "文档已加载");
    },
    onDocumentStateChange: event => {
      const changed = Boolean(event?.data);
      setStatus(
        changed ? "changed" : "idle",
        changed ? "有未保存修改" : "编辑器内已同步"
      );
    },
    onError: event => {
      const code = event?.data?.errorCode ?? "unknown";
      const description =
        event?.data?.errorDescription || "ONLYOFFICE 返回未知错误";
      showError(\`错误码 ${code}：${description}\`);
    },
    onRequestClose: () => {
      window.location.href = "/";
    }
  };

 new DocsAPI.DocEditor("office-editor", config);
}

function loadDocsApi(url) {
 return new Promise((resolve, reject) => {
    const script = document.createElement("script");
    script.src = url;
    script.async = true;
    script.onload = resolve;
    script.onerror = () => reject(
      new Error("无法加载 ONLYOFFICE 
            api.js，请检查文档服务地址。"
          )
    );
    document.head.appendChild(script);
  });
}
```

要注意， `onDocumentStateChange(false)` 只能说明编辑器内部状态已经同步，不代表 Spring Boot 已经收到 `status=2` 并把文件落盘。真正的保存结果，还得看服务端回调日志。

**第四步，处理保存回调**

status=2 或 6 时下载新文件、更新存储、刷新 key。

```
@PostMapping("/callback/{fileId}")
public Map<String, Integer> callback(@PathVariable Long fileId,
                                      @RequestBody Map<String, Object> body) {
    if (!
            jwtVerifier.verify(body))
           return 
            Map.of(
          "error", 1);

    int status = (int) 
            body.get(
          "status");
    if (status == 2 || status == 6) {
        String downloadUrl = (String) 
            body.get(
          "url");
        byte[] newContent = 
            restTemplate.getForObject(downloadUrl,
           byte[].class);
        
            fileStorage.update(fileId,
           newContent);
        
            fileRepository.incrementVersion(fileId);
           // 刷新 key
    }
    return 
            Map.of(
          "error", 0);
}
```

上面的代码保留了回调主流程。项目里把“验签、下载、写文件、升版本”拆到了 `OnlyOfficeCallbackService` 和 `DocumentStorageService` 中，下面是 `OnlyOfficeCallbackService` 的核心源码片段：

```
public Map<String, Integer> receive(
        String documentId,
        Map<String, Object> body) {
    try {
        Object token = 
            body.get(
          "token");
        
            jwtService.verify(token
           == null ? null : 
            token.toString());
          

        int status = statusOf(body);
        
            log.info(
          "OnlyOffice callback: document={}, status={}, key={}",
                documentId, status, 
            body.get(
          "key"));

        if (status == 2 || status == 6) {
            Object downloadUrl = 
            body.get(
          "url");
            if (!(downloadUrl instanceof String url) || 
            url.isBlank())
           {
                throw new IllegalArgumentException(
                        "OnlyOffice 回调缺少保存地址");
            }

            byte[] content = 
            restClient.get()
          
                    .uri(url)
                    .accept(
            MediaType.APPLICATION_OCTET_STREAM)
          
                    .exchange((request, response) -> {
                        if (!
            response.getStatusCode().is2xxSuccessful())
           {
                            throw new IllegalStateException(
                                    "下载 OnlyOffice 文件失败: "
                                            + 
            response.getStatusCode());
          
                        }

                        byte[] bytes = 
            response.getBody()
          
                                .readNBytes(MAX_DOWNLOAD_BYTES + 1);
                        if (
            bytes.length
           > MAX_DOWNLOAD_BYTES) {
                            throw new IllegalArgumentException(
                                    "OnlyOffice 文件超过 50 MB");
                        }
                        return bytes;
                    });

            var updated = 
            storageService.updateContent(documentId,
           content);
            
            log.info(
          
                    "OnlyOffice document saved: document={}, version={}, size={}",
                    documentId, 
            updated.version(),
           
            updated.size());
          
        }

        return 
            Map.of(
          "error", 0);
    } catch (Exception exception) {
        
            log.error(
          
                "OnlyOffice callback failed: document={}",
                documentId, exception);
        return 
            Map.of(
          "error", 1);
    }
}

private int statusOf(Map<String, Object> body) {
    Object value = 
            body.get(
          "status");
    if (value instanceof Number number) {
        return 
            number.intValue();
          
    }
    if (value instanceof String text) {
        return 
            Integer.parseInt(text);
          
    }
    throw new IllegalArgumentException("OnlyOffice 回调缺少 status");
}
```

这里的 `RestClient` 设置了 10 秒连接超时、60 秒读取超时，并限制下载文件最大为 50 MB，避免回调线程被异常地址拖住。

状态码只需要先盯住下面几个：

| 状态 | 含义 | 处理方式 |
| --- | --- | --- |
| `1` | 文档正在编辑 | 记录日志 |
| `2` | 文档关闭，需要保存 | 下载文件并更新版本 |
| `4` | 没有修改就关闭 | 返回成功 |
| `6` | 强制保存 | 下载文件并更新版本 |
| `7` | 强制保存出错 | 记录日志，不覆盖原文件 |

最后落盘时，项目没有直接往目标文件里写，而是先写临时文件，再原子替换：

```
public synchronized DocumentInfo updateContent(
        String id,
        byte[] content) {
    if (content == null || 
            content.length
           == 0) {
        throw new IllegalArgumentException("OnlyOffice 返回了空文件");
    }

    DocumentInfo current = get(id);
    DocumentInfo updated = 
            current.withContent(content.length);
          

    try {
        writeContent(updated, content);
        
            documents.put(id,
           updated);
        persistMetadata();
        return updated;
    } catch (IOException exception) {
        throw new IllegalStateException("更新文档内容失败", exception);
    }
}

private void writeContent(
        DocumentInfo document,
        byte[] content) throws IOException {
    Path target = contentPath(document);
    Path temporary = 
            storageDirectory.resolve(document.id()
           + ".tmp");

    
            Files.write(temporary,
           content);
    
            Files.move(
          
            temporary,
            target,
            
            StandardCopyOption.REPLACE_EXISTING,
          
            
            StandardCopyOption.ATOMIC_MOVE
          
    );
}
```

`withContent` 会生成新的版本号：

```
public DocumentInfo withContent(long newSize) {
    return new DocumentInfo(
            id,
            name,
            fileType,
            version + 1,
            newSize,
            
            Instant.now()
          
    );
}
```

下一次打开会使用 `id + "_" + version` 组成新的 `              document.key            ` ，不会继续复用旧缓存。

**踩坑提醒，提前说。**

key 不更新，会导致协同错乱。

文件已经变了还用旧 key，用户打开看到缓存旧版本，或者协同状态乱套。

回调不保存，用户会觉得“内容丢了”。

回调返回非零或者超时，ONLYOFFICE 就当保存失败，用户下次打开看到的是改之前的版本。

JWT 不一致，编辑器直接加载失败。

后端配了 JWT，Docker 环境变量没配或者配了别的值，编辑器白屏，报“文档安全令牌格式不正确”。

项目实际运行时效果：

![文档中心，展示上传入口和文档版本列表](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/ff835d965ae9ff9a753c7ddd79d06899_MD5.png)

在线编辑 Word文件的效果：

![ONLYOFFICE 在线编辑 Word，顶部工具栏和文档画布均已正常加载](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/fcb0842985df9ac27cb1a4afe564ff31_MD5.png)

在线编辑 Excel文件的效果：

![ONLYOFFICE 在线编辑 Excel，工作表与公式工具栏正常显示](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%20%EF%BC%9F/5fb1d211ad01f213cbdd06cb9e1696b4_MD5.png)

## 五、适用场景速查

四个能力和项目实战讲完，落到选型就一个问题：你的场景决定版本。

功能三档差别不大，差的是授权、并发和品牌控制权。

下面这张表格总结了版本选型：

| 场景 | 选什么 | 关键约束 |
| --- | --- | --- |
| 小团队、测试 | 社区版 | AGPL [v.3](http://v.3) 传染性；并发上限 20 |
| 企业内部部署、保留品牌 | 企业版 | ≥50 并发；按年或永久许可 |
| 提供 SaaS 服务、需要白标 | 开发者版 | 白标；仅按年许可 |
| 为每位客户单独部署 | 看品牌需求 | 要白标选开发者版，保留品牌选企业版 |

## 六、写在最后

回头看开头那三个问题：SaaS 数据出不了内网，商业 SDK 按人头收费扛不住，自研的隐性成本又太高。三条路走不通，大家才开始找“第三条路”。

OnlyOffice 给出的答案，是把“文档编辑”这件事从一项服务变成一块可以装进自己系统里的组件。

数据在你自己服务器上，能力通过 API 嵌进你的业务流程，授权按场景选、预算可控。

它不完美——社区版有 AGPL 的约束和并发上限，白标只有开发者版才有，离线 AI 还得自己额外部署模型。但在“私有化、可集成、成本可控”这个坐标系里，它确实把那条堵死的路走通了。

所以文档协作的“第三选择”，不是更便宜的 SaaS，也不是又一个自研轮子。

是数据在自己手里、能力能嵌进自己系统的编辑引擎。

选型时先想清楚两件事：数据要不要留在自己手里，品牌要不要换成自己的。

这两个问题的答案，基本就决定了你该看社区版、企业版还是开发者版。

剩下的，交给 Docker 一行命令和一份 config。

## 七、获取链接

- 本地部署： [https://www.onlyoffice.com/zh/download](https://www.onlyoffice.com/zh/download)
- 开源地址： [https://github.com/ONLYOFFICE/DocumentServer](https://github.com/ONLYOFFICE/DocumentServer)

了解更多：

- 企业版介绍： [https://www.onlyoffice.com/zh/docs-enterprise](https://www.onlyoffice.com/zh/docs-enterprise)
- 开发者版介绍： [https://www.onlyoffice.com/zh/for-developers](https://www.onlyoffice.com/zh/for-developers)
- 价格和版本对比： [https://www.onlyoffice.com/zh/pricing](https://www.onlyoffice.com/zh/pricing)
- 帮助中心： [https://helpcenter.onlyoffice.com/zh/](https://helpcenter.onlyoffice.com/zh/)
- API 文档： [https://api.onlyoffice.com/zh-CN/](https://api.onlyoffice.com/zh-CN/)

阅读原文