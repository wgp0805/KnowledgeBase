---
title: "为什么越来越多人用 OnlyOffice？"
source: "https://mp.weixin.qq.com/s/3M34_R5tKjePUStcz7rHqQ"
---
苏三 苏三说技术 *2026年9月27日 09:20*

大家好，我是苏三，又跟大家见面了。

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)

## 前言

2026年5月19日，OnlyOffice DocumentServer 9.4.0正式发布。

这次更新有一个标志性的变化—— **官方社区版从9.4.0开始强制使用轻量模式，不再提供原有的标准模式** 。

传统的分布式架构，合并成了单进程单体化架构。

这意味着部署一个在线文档编辑服务，从“docker-compose多容器编排”变成了“docker run一键启动”。

今天这篇文章，我就把OnlyOffice为什么越来越多人用的原因，从头到尾给你拆解一遍。

希望对你会有所帮助。

## 一、OnlyOffice到底是什么？

> 有些小伙伴可能会说：“OnlyOffice不就是个开源办公套件吗？跟LibreOffice有什么区别？”

**区别很大。**

LibreOffice是 **桌面软件** ，你装在自己电脑上，编辑本地文件。

它的在线版本是Collabora Online，基于LibreOffice核心。

OnlyOffice的核心是 **DocumentServer** ——一个独立的在线文档编辑后端服务。你可以把它理解成： **在服务器上跑了一个“云端的Office”** ，用户通过浏览器访问，文档存在你的服务器上，不经过任何第三方。

用人话说： **OnlyOffice是“文档编辑后端服务”，不是完整的网盘或办公套件** 。

它负责在浏览器里渲染和编辑文档，至于文档存哪里、谁有权限访问、怎么管理文件夹——这些需要你的系统来提供。

## 二、一张图看懂OnlyOffice的架构

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%EF%BC%9F/c86897f519585cebac7bfcf02f954345_MD5.jpg)

**文档管理器和文档存储服务由集成商提供** ——可以是OnlyOffice DocSpace，也可以是你自己服务器上的实现。DocumentServer负责文档编辑、转换、命令和构建服务。

## 三、底层原理

[document.key——整个协同编辑的“身份证”。](http://document.xn--key-8n0aa2ch4245gktb74to4byx8grm7bucza7y3b8zjwyd./)

这是理解OnlyOffice最关键的一点。

**很多开发者第一次接触OnlyOffice时会以为：浏览器直接编辑服务器上的Word文件。实际上不是。**

真实的流程是：

![图片](assets/%E4%B8%BA%E4%BB%80%E4%B9%88%E8%B6%8A%E6%9D%A5%E8%B6%8A%E5%A4%9A%E4%BA%BA%E7%94%A8%20OnlyOffice%EF%BC%9F/191c615993c41b61cc2a8a6abbc90121_MD5.jpg)

浏览器编辑的是 **ONLYOFFICE内部缓存中的协同编辑文件（ [Editor.bin）](http://editor.bin\)/)** ，而不是原始Word文件。

**[document.key是当前文档内容版本的唯一身份标识。](http://document.xn--key-s18d78bb1h8rbzzlp4qmpiexrs0be4ey1diub938gtbp4i4ggrl./)**

它不是文件ID，是 **当前协同编辑版本ID** 。

它决定了五件事：多个用户是否进入同一个协同会话、是否复用已有的 [Editor.bin文件、是否认为文件已经变化、是否重新下载原始文件、是否属于同一个编辑版本。](http://editor.xn--bin-6y3baa7684cqcavnpfp2br9acac159my5bu1a70a2nfae1092afnmzgjjo3ceaj85i78hiai612fq92h288dtbcey7qw03adwat01e./)

**完整的编辑生命周期** ：

第一次打开文档（key = key0）→ 原始Word文件被下载 → 转换为 [Editor.bin缓存在](http://editor.xn--bin-op6el5qbs6d/) `/var/lib/onlyoffice/documentserver/App_Data` 中。

多人进入协同编辑 → 使用同一个key0 → 进入同一个协同编辑会话，大家编辑的是 [Editor.bin。](http://editor.bin./)

编辑过程中 → 所有修改都在缓存中，原始Word文件可能完全没有变化。

**真正生成新Word文件的时机是所有人退出编辑或强制保存之后** ，此时生成 [output.docx，callback收到status](http://output.xn--docx,callbackstatus-dp55a827x/) = 2或6。

**为什么会出现“内容丢失”？**

很多系统收到回调后没有下载 [output.docx，仍然保留旧的原始文件。](http://output.xn--docx,-pg2hrju7dnwpp5peo4a36ai49gwdmgie./)

下次重新打开时，ONLYOFFICE下载的仍然是旧文件。

**实际上不是内容丢失，而是根本没有保存新的 [output.docx](http://output.docx/)** 。

## 四、Java集成OnlyOffice

### 4.1 部署DocumentServer

```
docker run -i -t -d -p 8080:80 --restart=always \
  -e JWT_ENABLED=true \
  -e JWT_SECRET='your-secret-key' \
  onlyoffice/documentserver:9.4.0
```

访问 `http://localhost:8080` 验证是否成功。

### 4.2 Spring Boot后端：生成编辑器配置

```
@RestController
publicclass DocumentController {

    @Value("${
            onlyoffice.docserver.url}"
          )
    private String docServerUrl;

    @Value("${
            onlyoffice.callback.url}"
          )
    private String callbackUrl;

    @GetMapping("/edit/{docId}")
    public String editDocument(@PathVariable String docId, Model model) {
        Document doc = 
            documentService.findById(docId);
          
        
        // 构建编辑器配置
        Map config = 
            Map.of(
          
            "document", 
            Map.of(
          
                "fileType", 
            doc.getExtension(),
          
                "key", 
            doc.getVersionKey(),
            // 关键！每次内容变化要换key
                "title", 
            doc.getName(),
          
                "url", 
            doc.getDownloadUrl()
          
            ),
            "editorConfig", 
            Map.of(
          
                "callbackUrl", callbackUrl,
                "mode", "edit",
                "user", 
            Map.of(
          "id", "1", "name", "老张")
            )
        );
        
        
            model.addAttribute(
          "config", config);
        
            model.addAttribute(
          "docServerUrl", docServerUrl);
        return"editor";
    }
}
```

**关键点** ： `key` 每次文档内容变化后必须更新，否则OnlyOffice会认为文件没变，继续用缓存的 [Editor.bin。](http://editor.bin./)

### 4.3 处理保存回调

OnlyOffice在文档保存时会回调你的服务：

```
@PostMapping("/callback")
@ResponseBody
public String handleCallback(@RequestBody Map<String, Object> data) {
    // 状态2或6表示文档已准备好保存
    if ("2".equals(
            data.get(
          "status")) || "6".equals(
            data.get(
          "status"))) {
        String downloadUrl = (String) ((Map) 
            data.get(
          "url")).get("url");
        // 下载并保存文档
        saveDocument(downloadUrl, (String) 
            data.get(
          "key"));
        // 更新版本key，让下次打开时重新加载
        
            documentService.updateVersionKey((String)
           
            data.get(
          "key"));
    }
    return "{\"error\":0}";
}
```

### 4.4 前端页面

```
<script src="http://docserver-url/web-apps/apps/api/documents/
            api.js"
          ></script>
<div id="editor"></div>
<script>
    const docEditor = new 
            DocsAPI.DocEditor(
          "editor", {
        document: { fileType: "docx", key: "key0", title: "
            demo.docx"
          , url: "..." },
        editorConfig: { callbackUrl: "http://your-server/callback", mode: "edit" },
        width: "100%", height: "100%"
    });
</script>
```

## 五、轻量模式

这是9.4版本最重要的变化。

**传统标准模式** 依赖 **Nginx + PostgreSQL + RabbitMQ + 多Node进程协同** ，部署时需要处理服务依赖顺序、健康检查、MQ异常恢复。对中小企业私有化部署、Docker单容器/NAS/群晖/ARM低配机器、POC验证场景来说，这些依赖过于沉重。

**轻量模式** 将原本依赖消息队列和数据库的分布式架构， **合并为单进程单体化架构** 。

状态全部内存化，无需额外数据库维护；单机文件状态管理，不再依赖RabbitMQ。

| 对比维度 | 标准模式 | 轻量模式 |
| --- | --- | --- |
| **依赖组件** | Nginx + PostgreSQL + RabbitMQ + 多进程 | **单进程单体化** |
| **部署方式** | docker-compose多容器编排 | **docker run一键启动** |
| **资源占用** | 高（MQ + DB常驻内存） | **低** |
| **运维复杂度** | 高 | **低** |
| **适用场景** | 高并发大规模集群 | 中小企业/小团队/POC |

启动轻量模式只需要在环境变量中加上：

```
docker run -itd -p 8080:80 \
  -e MEMORY_MODE=true \
  onlyoffice/documentserver:9.4.0
```

**轻量模式特别适合** 中小企业/小团队文档协作、POC验证与开发测试、NAS/Docker单容器部署、ARM低配机器、离线内网环境。

如果你的业务需要集群、高可用、横向扩展，仍然建议使用标准模式。

## 六、各项对比

| 对比维度 | OnlyOffice | Collabora Online | Microsoft 365 |
| --- | --- | --- | --- |
| **核心引擎** | **自研OOXML引擎** | LibreOffice核心 | 微软原生 |
| **原生格式** | **OOXML (.docx/.xlsx/.pptx)** | ODF | OOXML |
| **Microsoft格式兼容性** | **最强** | 一般 | 原生 |
| **部署方式** | Docker/Linux/Windows | Docker/Linux | 仅云端 |
| **私有化部署** | ✅ | ✅ | ❌ |
| **空闲内存** | ~2GB | **~1GB** | N/A |
| **免费版限制** | 20并发连接 | 20文档/10连接 | 无免费版 |
| **协同编辑** | ✅ 实时协同 | ✅ 实时协同 | ✅ |
| **AI助手** | ✅ 内置 | ❌ | ✅ Copilot |

**核心差异可以概括为三句话** ：

- **OnlyOffice给的是“Microsoft格式兼容性”** ——如果你团队主要用.docx和.xlsx，OnlyOffice的round-trip fidelity最强
- **Collabora给的是“轻量+ODF生态”** ——如果你用户主要用ODF格式，Collabora的空闲内存只有1GB左右
- **Microsoft 365给的是“原生体验”** ——如果不需要私有化部署，微软云端仍是最省心的选择

## 七、优缺点

### 优点

**1\. Microsoft格式兼容性最强** 自研OOXML引擎，对.docx、.xlsx、.pptx的round-trip fidelity在开源方案中最好。界面和交互方式与Microsoft Office非常接近，迁移成本低。

**2\. 轻量模式部署极简** 9.4版本起社区版强制轻量模式，单进程架构，docker run一键启动。对2C4G的小机器和NAS环境非常友好。

**3\. 原生在线协作** 实时多人协同编辑、版本历史、评论批注、更改追踪。协同模式支持Fast和Strict两种。

**4\. 安全功能全内置** JWT双重校验、HTTPS强制、回调防伪造、字段脱敏。不需要额外付费购买安全模块。

**5\. 生态丰富** 构建了40多个连接器和50多个插件，可以嵌入Nextcloud、ownCloud、Seafile、Odoo、Moodle等系统，也兼容Office 365和SharePoint。

**6\. 官方社区版免费** 社区版采用AGPL v3协议，核心编辑功能完整。9.4版本取消了20个并发连接限制。

### 缺点

**1\. 资源占用比Collabora高** 空闲内存约2GB，而Collabora只有约1GB。对于2GB以下内存的VPS，OnlyOffice可能跑不起来。

**2\. 非OOXML格式兼容性一般** OnlyOffice主要优化了OOXML格式。如果你处理大量ODF或旧版.doc文件，可能不如Collabora。

**3\. [document.key机制容易踩坑](http://document.xn--key-zk2el7umlh99tmfcb43m/)** 很多开发者第一次接触时会把 [document.key当成文件ID，导致协同会话错乱、版本冲突、内容看似“丢失”。理解这个机制需要时间。](http://document.xn--keyid,-ui0ci4277aa8595f80ak3crorq251a2vag6uvyd360byem4lbz78byppunubzj6s9em41a97ul84cfhzdn03c.xn--ciq91hn8v8fb7z8a1m4artaq59acmnrqc./)

**4\. 社区版不支持集群** 轻量模式只适合单机小规模部署。需要高可用和横向扩展时，必须使用企业版。

## 八、适用场景

| 场景 | 推荐程度 | 理由 |
| --- | --- | --- |
| **企业OA系统集成** | ✅✅✅ 强烈推荐 | 自研OOXML引擎，格式兼容性最好 |
| **私有化文档协作** | ✅✅✅ 强烈推荐 | Docker一键部署，数据完全自控 |
| **与Nextcloud/ownCloud集成** | ✅✅✅ 强烈推荐 | 官方连接器成熟，部署简单 |
| **Microsoft格式为主的团队** | ✅✅✅ 强烈推荐 | Round-trip fidelity在开源方案中最好 |
| **中小企业/小团队** | ✅✅✅ 强烈推荐 | 轻量模式对2C4G机器友好 |
| **需要AI助手** | ✅✅ 推荐 | 内置AI助手，支持DeepSeek等模型 |
| **超大规模集群部署** | ⚠️ 需评估 | 社区版不支持集群，需企业版 |
| **纯ODF格式场景** | ⚠️ 需评估 | Collabora可能更合适 |

## 九、写在最后

回到最初的问题： **为什么越来越多人用OnlyOffice？**

答案不复杂—— **因为它把“在线文档编辑”这件事，从“买授权”变成了“自己部署”。**

商业文档SDK按年收费、按并发收费、多人协同要升级旗舰版。

而OnlyOffice把核心编辑能力开源出来，你用Docker就能跑，数据在自己服务器上，不经过任何第三方。

**更关键的是，9.4版本把部署复杂度砍了一大截。**

过去部署OnlyOffice要处理PostgreSQL、RabbitMQ、多Node进程，很多人卡在环境配置上就放弃了。

现在轻量模式单进程架构， `docker run -e MEMORY_MODE=true` 一条命令就能启动。

**[document.key机制是最大的坑，也是最大的价值。](http://document.xn--key,-8m5fn5a98dt4fd2ojseda1411bea530afa33gh51qga./)**

理解它需要时间，但理解之后你会发现，这套机制让协同编辑、版本管理、缓存复用都变得优雅。

当然，OnlyOffice不是银弹。

资源占用比Collabora高、社区版不支持集群、非OOXML格式兼容性一般。

但对于企业OA集成、私有化文档协作、Microsoft格式为主的团队来说，它已经是一个非常成熟的选项。

## 十、参考资源

- **OnlyOffice官网** ： [https://www.onlyoffice.com](https://www.onlyoffice.com/)
- **DocumentServer GitHub** ： [https://github.com/ONLYOFFICE/DocumentServer](https://github.com/ONLYOFFICE/DocumentServer)
- **API文档** ： [https://api.onlyoffice.com](https://api.onlyoffice.com/)
- **Docker镜像** ： `onlyoffice/documentserver:9.4.0`

最近缺项目经历想快速提升项目实战能力（包含多个AI项目），或者最近找工作，或者想学习AI的小伙伴，可以看看下面👇🏻的这个链接（或许真的能够帮到你）:

[推荐一个牛逼的RAG+KAG双引擎系统](https://mp.weixin.qq.com/s?__biz=MzkzNzg4MzI2MQ==&mid=2247535459&idx=1&sn=46cb5e406ec8dc7e6c61edab95ed321d&scene=21#wechat_redirect)