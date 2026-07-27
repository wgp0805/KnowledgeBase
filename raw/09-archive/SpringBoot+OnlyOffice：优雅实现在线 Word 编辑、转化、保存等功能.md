---
title: "SpringBoot+OnlyOffice：优雅实现在线 Word 编辑、转化、保存等功能"
source: "https://mp.weixin.qq.com/s/iyk15xnxQ9_Lq0sTrPClPA"
---
小哈学Java *2026年7月26日 22:07*

![图片](assets/SpringBoot+OnlyOffice%EF%BC%9A%E4%BC%98%E9%9B%85%E5%AE%9E%E7%8E%B0%E5%9C%A8%E7%BA%BF%20Word%20%E7%BC%96%E8%BE%91%E3%80%81%E8%BD%AC%E5%8C%96%E3%80%81%E4%BF%9D%E5%AD%98%E7%AD%89%E5%8A%9F%E8%83%BD/cce9543f98f05f091f32c4c9979758c0_MD5.webp)

来源： [https://blog.csdn.net/qq\_40834643](https://blog.csdn.net/qq_40834643)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

**目录**

- 前言
- 1、onlyoffice 的部署
- 2、代码逻辑开发
- 2.1、前端代码
	- 2.2、后端代码
- 3、问题总结
- 3.1、访问案例失败
	- 3.2、加载 word 文档失败
	- 3.3、系统后端有 token 验证问题
	- 3.4、使用文档地址访问问题
- 4、后记

---

## 前言

最近有个项目需求是实现前端页面可以对 word 文档进行编辑，并且可以进行保存，于是一顿搜索，找到开源第三方 onlyoffice，实际上 onlyOffice 有很多功能，例如文档转化、多人协同编辑文档、文档打印等，我们只用到了文档编辑功能。

## 1、onlyoffice 的部署

部署分为 docker 部署方式和本地直接安装的方式，比较两种部署方式，docker 是比较简单的一种，因为只要拉取相关镜像，然后启动时配置好对应的配置文件即可。

由于搜索的时候先看到的是 linux 本地部署，所以采用了第二种方式，下面我将给出两个参考博客：

**docker 的方式：** （我未进行尝试，对于是否能成功是不知的）

[https://blog.csdn.net/wangchange/article/details/140185623](https://blog.csdn.net/wangchange/article/details/140185623)

**ubuntu 部署方式：** （我按照这个方式走下来是可以走通的）

[https://blog.csdn.net/qq\_36437991/article/details/139859247](https://blog.csdn.net/qq_36437991/article/details/139859247)

## 2、代码逻辑开发

前端使用的 element 框架 vue 版本，后端采用 springboot

### 2.1、前端代码

**参考官方文档 API**

[https://api.onlyoffice.com/docs/docs-api/get-started/basic-concepts/](https://api.onlyoffice.com/docs/docs-api/get-started/basic-concepts/)

**参考文档**

[https://api.onlyoffice.com/docs/docs-api/usage-api/advanced-parameters/](https://api.onlyoffice.com/docs/docs-api/usage-api/advanced-parameters/)

记得添加下面的 js 文件

```
<div id="placeholder"></div>
<script type="text/javascript" src="https://documentserver/web-apps/apps/api/documents/
            api.js"
          ></script>
```

记得将 documentserver 替换为部署 onlyoffice 的地址。

```
const config = {
    document: {
        mode: 'edit',
        fileType: 'docx',
        key: String( 
            Math.floor(Math.random()
           * 10000)),
        title: 
            route.query.name
           + '.docx',
        url: 
            import.meta.env.VITE_APP_API_URL+\`/getFile/
          ${
            route.query.id}
          \`,
        permissions: {
            comment: true,
            download: true,
            modifyContentControl: true,
            modifyFilter: true,
            edit: true,
            fillForms: true,
            review: true,
        },
    },
    documentType: 'word',
    editorConfig: {
        user: {
            id: 'liu',
            name: 'liu',
        },
        // 隐藏插件菜单
        customization: {
            plugins: false,
            forcesave: true,
        },
        lang: 'zh',
        // callbackUrl: \`${
            import.meta.env.VITE_APP_API_URL}
           +'/callback' \`,
        callbackUrl: 
            import.meta.env.VITE_APP_API_URL+\`/callback\`,
          
    },
    height: '100%',
    width: '100%',
}

new 
            window.DocsAPI.DocEditor(
          'onlyoffice', config)
```

其中 `              import.meta.env.VITE_APP_API_URL            ` 为你实际的后端地址， `http：ip：端口号/访问路径` ，例如我们就是： `http:192.168.123.123:8089/getFile/12` ，其中 12 为会议号，用于得到文件地址。

其中 `              import.meta.env.VITE_APP_API_URL+/callback            ` 为回调函数，即文档有什么操作后，都会通过这个函数进行回调，例如：编辑保存操作。

### 2.2、后端代码

pom 依赖

```
<!-- httpclient start -->
<dependency>
    
            org.apache.httpcomponents
          
    <artifactId>httpclient</artifactId>
</dependency>
<dependency>
    
            org.apache.httpcomponents
          
    <artifactId>httpmime</artifactId>
</dependency>
```
```
package 
            com.ruoyi.web.controller.meetingminutes.onlyoffice;
          

/**
 * @Author 不要有情绪的  ljy
 * @Date 2024/10/31 20:26
 * @Description:
 */

import 
            com.ruoyi.system.domain.MeetingTable;
          
import 
            com.ruoyi.system.service.IMeetingTableService;
          
import 
            com.ruoyi.web.controller.meetingminutes.utils.HttpsKitWithProxyAuth;
          
import 
            io.swagger.annotations.Api;
          
import 
            io.swagger.annotations.ApiOperation;
          
import 
            lombok.Getter;
          
import 
            lombok.Setter;
          
import 
            org.springframework.beans.factory.annotation.Autowired;
          
import 
            org.springframework.http.HttpHeaders;
          
import 
            org.springframework.http.HttpStatus;
          
import 
            org.springframework.http.MediaType;
          
import 
            org.springframework.http.ResponseEntity;
          
import 
            org.springframework.web.bind.annotation.*;
          

import 
            javax.servlet.http.HttpServletResponse;
          
import 
            java.io.*;
          
import 
            java.net.URISyntaxException;
          
import 
            java.net.URLEncoder;
          
import 
            java.util.Collections;
          

/**
 *
 */
@Api(value = "OnlyOfficeController")
@RestController
public class OnlyOfficeController {
    @Autowired
    private IMeetingTableService meetingTableService;

    //这里仅写死路径测试
    //    private String meetingMinutesFilePath = "C:\\Users\\qrs-ljy\\Desktop\\王勋\\c1f15837-d8b4-4380-8161-b85e970ad174\\123435_会议纪要（公开）.docx"; //这里仅写死路径测试
    private String meetingMinutesFilePath;

    /**
     * 传入参数 会议id，得到会议纪要文件流，并进行打开
     *
     * @param response
     * @param meeting_id
     * @return
     * @throws IOException
     */
    @ApiOperation(value = "OnlyOffice")
    @GetMapping("/getFile/{meeting_id}")
    public ResponseEntity<byte[]> getFile(HttpServletResponse response, @PathVariable Long meeting_id) throws IOException {
        MeetingTable meetingTable = 
            meetingTableService.selectMeetingTableById(meeting_id);
          
        meetingMinutesFilePath = 
            meetingTable.getMeetingMinutesFilePath();
          
        if (meetingMinutesFilePath == null || "".equals(meetingMinutesFilePath)) {
            return null;   //当会议纪要文件为空的时候，就返回null
        }
        File file = new File(meetingMinutesFilePath);
        FileInputStream fileInputStream = null;
        InputStream fis = null;
        try {
            fileInputStream = new FileInputStream(file);
            fis = new BufferedInputStream(fileInputStream);
            byte[] buffer = new byte[
            fis.available()];
          
            
            fis.read(buffer);
          
            
            fis.close();
          
            HttpHeaders headers = new HttpHeaders();
            
            headers.setContentType(MediaType.APPLICATION_OCTET_STREAM);
          
            // 替换为实际的文档名称
            
            headers.setContentDispositionFormData(
          "attachment", 
            URLEncoder.encode(file.getName(),
           "UTF-8"));
            return new ResponseEntity<>(buffer, headers, 
            HttpStatus.OK);
          
        } catch (Exception e) {
            throw new RuntimeException("e -> ", e);
        } finally {
            try {
                if (fis != null) 
            fis.close();
          
            } catch (Exception e) {

            }
            try {
                if (fileInputStream != null) 
            fileInputStream.close();
          
            } catch (Exception e) {

            }
        }

    }

    @CrossOrigin(origins = "*", methods = {
            RequestMethod.GET,
           
            RequestMethod.POST,
           
            RequestMethod.OPTIONS})
          
    @PostMapping("/callback")
    public ResponseEntity<Object> handleCallback(@RequestBody CallbackData callbackData) {

        //状态监听
        //参见
            https://api.onlyoffice.com/editors/callback
          
        Integer status = 
            callbackData.getStatus();
          
        switch (status) {
            case 1: {
                //document is being edited  文档已经被编辑
                break;
            }
            case 2: {
                //document is ready for saving,文档已准备好保存
                
            System.out.println(
          "document is ready for saving");
                String url = 
            callbackData.getUrl();
          
                try {
                    saveFile(url); //保存文件
                } catch (Exception e) {
                    
            System.out.println(
          "保存文件异常");
                }
                
            System.out.println(
          "save success.");
                break;
            }
            case 3: {
                //document saving error has occurred,保存出错
                
            System.out.println(
          "document saving error has occurred,保存出错");
                break;
            }
            case 4: {
                //document is closed with no changes,未保存退出
                
            System.out.println(
          "document is closed with no changes,未保存退出");
                break;
            }
            case 6: {
                //document is being edited, but the current document state is saved,编辑保存
                String url = 
            callbackData.getUrl();
          
                try {
                    saveFile(url); //保存文件
                } catch (Exception e) {
                    
            System.out.println(
          "保存文件异常");
                }
                
            System.out.println(
          "save success.");
            }
            case 7: {
                //error has occurred while force saving the document. 强制保存文档出错
                
            System.out.println(
          "error has occurred while force saving the document. 强制保存文档出错");
            }
            default: {

            }
        }
        // 返回响应
        return ResponseEntity.ok(
            Collections.singletonMap(
          "error", 0));

    }

    public void saveFile(String downloadUrl) throws URISyntaxException, IOException {

        
            HttpsKitWithProxyAuth.downloadFile(downloadUrl,
           meetingMinutesFilePath);

    }

    @Setter
    @Getter
    public static class CallbackData {
        /**
         * 用户与文档的交互状态。0：用户断开与文档共同编辑的连接；1：新用户连接到文档共同编辑；2：用户单击强制保存按钮
         */
//        @IsArray()
//        actions?:IActions[] =null;

        /**
         * 字段已在 4.2 后版本废弃，请使用 history 代替
         */
        Object changeshistory;

        /**
         * 文档变更的历史记录，仅当 status 等于 2 或者 3 时该字段才有值。其中的 serverVersion 字段也是 refreshHistory 方法的入参
         */
        Object history;

        /**
         * 文档编辑的元数据信息，用来跟踪显示文档更改记录，仅当 status 等于 2 或者 2 时该字段才有值。该字段也是 setHistoryData（显示与特定文档版本对应的更改，类似 Git 历史记录）方法的入参
         */
        String changesurl;

        /**
         * url 字段下载的文档扩展名，文件类型默认为 OOXML 格式，如果启用了 assemblyFormatAsOrigin（
            https://api.onlyoffice.com/editors/save
          #assemblyFormatAsOrigin） 服务器设置则文件以原始格式保存
         */
        String filetype;

        /**
         * 文档强制保存类型。0：对命令服务（
            https://api.onlyoffice.com/editors/
          command/forcesave）执行强制保存；1：每次保存完成时都会执行强制保存请求，仅设置 forcesave 等于 true 时生效；2：强制保存请求由计时器使用服务器中的设置执行。该字段仅 status 等于 7 或者 7 时才有值
         */
        Integer forcesavetype;

        /**
         * 文档标识符，类似 id，在 Onlyoffice 服务内部唯一
         */
        String key;

        /**
         * 文档状态。1：文档编辑中；2：文档已准备好保存；3：文档保存出错；4：文档没有变化无需保存；6：正在编辑文档，但保存了当前文档状态；7：强制保存文档出错
         */
        Integer status;

        /**
         * 已编辑文档的链接，可以通过它下载到最新的文档，仅当 status 等于 2、3、6 或 7 时该字段才有值
         */
        String url;

        /**
         * 自定义参数，对应指令服务的 userdata 字段
         */
        Object userdata;

        /**
         * 打开文档进行编辑的用户标识列表，当文档被修改时，该字段将返回最后编辑文档的用户标识符，当 status 字段等于 2 或者 6 时有值
         */
        String[] users;

        /**
         * 最近保存时间
         */
        String lastsave;

        /**
         * 加密令牌
         */
        String token;
    }
}
```

代码中使用了其他类，这儿贴出（我也是参考的别人的博客，后面会给出参考链接）

```
package 
            com.ruoyi.web.controller.meetingminutes.utils;
          

/**
 * @Author 不要有情绪的  ljy
 * @Date 2024/10/31 20:34
 * @Description:
 */

import 
            java.io.File;
          
import 
            java.io.FileOutputStream;
          
import 
            java.io.IOException;
          
import 
            java.io.InputStream;
          
import 
            java.io.InterruptedIOException;
          
import 
            java.net.Authenticator;
          
import 
            java.net.InetSocketAddress;
          
import 
            java.net.MalformedURLException;
          
import 
            java.net.PasswordAuthentication;
          
import 
            java.net.Proxy;
          
import 
            java.net.Socket;
          
import 
            java.net.UnknownHostException;
          
import 
            java.security.KeyManagementException;
          
import 
            java.security.KeyStoreException;
          
import 
            java.security.NoSuchAlgorithmException;
          
import 
            java.security.cert.CertificateException;
          
import 
            java.security.cert.X509Certificate;
          
import 
            java.util.ArrayList;
          
import 
            java.util.HashMap;
          
import 
            java.util.List;
          
import 
            java.util.Map;
          
import 
            java.util.TimerTask;
          
import 
            java.util.concurrent.Executors;
          
import 
            java.util.concurrent.ScheduledExecutorService;
          
import 
            java.util.concurrent.TimeUnit;
          

import 
            javax.net.ssl.SSLContext;
          
import 
            javax.net.ssl.SSLException;
          
import 
            javax.net.ssl.SSLHandshakeException;
          

import 
            org.apache.commons.codec.CharEncoding;
          
import 
            org.apache.commons.io.IOUtils;
          
import 
            org.apache.http.Consts;
          
import 
            org.apache.http.HttpEntity;
          
import 
            org.apache.http.HttpEntityEnclosingRequest;
          
import 
            org.apache.http.HttpHost;
          
import 
            org.apache.http.HttpRequest;
          
import 
            org.apache.http.NameValuePair;
          
import 
            org.apache.http.NoHttpResponseException;
          
import 
            org.apache.http.auth.AUTH;
          
import 
            org.apache.http.auth.AuthState;
          
import 
            org.apache.http.auth.MalformedChallengeException;
          
import 
            org.apache.http.auth.UsernamePasswordCredentials;
          
import 
            org.apache.http.client.HttpRequestRetryHandler;
          
import 
            org.apache.http.client.config.RequestConfig;
          
import 
            org.apache.http.client.entity.UrlEncodedFormEntity;
          
import 
            org.apache.http.client.methods.CloseableHttpResponse;
          
import 
            org.apache.http.client.methods.HttpGet;
          
import 
            org.apache.http.client.methods.HttpPost;
          
import 
            org.apache.http.client.methods.HttpPut;
          
import 
            org.apache.http.client.protocol.HttpClientContext;
          
import 
            org.apache.http.config.Registry;
          
import 
            org.apache.http.config.RegistryBuilder;
          
import 
            org.apache.http.conn.ConnectTimeoutException;
          
import 
            org.apache.http.conn.socket.ConnectionSocketFactory;
          
import 
            org.apache.http.conn.socket.LayeredConnectionSocketFactory;
          
import 
            org.apache.http.conn.socket.PlainConnectionSocketFactory;
          
import 
            org.apache.http.conn.ssl.NoopHostnameVerifier;
          
import 
            org.apache.http.conn.ssl.SSLConnectionSocketFactory;
          
import 
            org.apache.http.conn.ssl.TrustStrategy;
          
import 
            org.apache.http.entity.ContentType;
          
import 
            org.apache.http.entity.StringEntity;
          
import 
            org.apache.http.entity.mime.MultipartEntityBuilder;
          
import 
            org.apache.http.entity.mime.content.InputStreamBody;
          
import 
            org.apache.http.entity.mime.content.StringBody;
          
import 
            org.apache.http.impl.auth.BasicScheme;
          
import 
            org.apache.http.impl.client.CloseableHttpClient;
          
import 
            org.apache.http.impl.client.HttpClients;
          
import 
            org.apache.http.impl.conn.PoolingHttpClientConnectionManager;
          
import 
            org.apache.http.message.BasicHeader;
          
import 
            org.apache.http.message.BasicNameValuePair;
          
import 
            org.apache.http.protocol.HttpContext;
          
import 
            org.apache.http.ssl.SSLContextBuilder;
          
import 
            org.slf4j.Logger;
          
import 
            org.slf4j.LoggerFactory;
          

/**
 * httpclient Sock5支持参考：
            https://blog.csdn.net/weixin_34075268/article/details/92040047
          
 * @author liujh
 *
 */
public class HttpsKitWithProxyAuth {

    private static Logger logger = 
            LoggerFactory.getLogger(HttpsKitWithProxyAuth.class);
          
    private static final int CONNECT_TIMEOUT = 10000;// 设置连接建立的超时时间为10000ms
    private static final int SOCKET_TIMEOUT = 30000; // 多少时间没有数据传输
    private static final int HttpIdelTimeout = 30000;//空闲时间
    private static final int HttpMonitorInterval = 10000;//多久检查一次
    private static final int MAX_CONN = 200; // 最大连接数
    private static final int Max_PRE_ROUTE = 200; //设置到路由的最大连接数,
    private static CloseableHttpClient httpClient; // 发送请求的客户端单例
    private static PoolingHttpClientConnectionManager manager; // 连接池管理类
    private static ScheduledExecutorService monitorExecutor;

    private static final String APPLICATION_FORM_URLENCODED = "application/x-www-form-urlencoded";
    private static final String APPLICATION_JSON = "application/json";
    private static final String USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36";
    private static final Object syncLock = new Object(); // 相当于线程锁,用于线程安全

    /**
     * 代理相关的变量,
     */
    public static final String HTTP = "http";//proxyType的取值之一http
    public static final String SOCKS = "socks";//proxyType的取值之一socks
    private static boolean needProxy = false; //是否需要代理连接
    private static boolean needLogin = false;//代理连接是否需要账号和密码，为true时填上proxyUsername和proxyPassword
    private static String proxyType = HTTP; //代理类型,http,socks分别为http代理和sock5代理
    private static String proxyHost = "127.0.0.1"; //代理IP
    private static int proxyPort = 1080; //代理端口
    private static String proxyUsername = "sendi";//代理账号，needLogin为true时不能为空
    private static String proxyPassword = "123456";//代理密码，needLogin为true时不能为空

    private static RequestConfig requestConfig = 
            RequestConfig.custom()
          
            .setConnectionRequestTimeout(CONNECT_TIMEOUT)
            .setConnectTimeout(CONNECT_TIMEOUT)
            //.setCookieSpec(
            CookieSpecs.IGNORE_COOKIES)
          
            .setSocketTimeout(SOCKET_TIMEOUT).build();

    static {
        /**
         * Sock5代理账号和密码设置
         * 如果账号和密码都不为空表示需要账号密码认证,因为这个是全局生效，因此在这里直接设置
         * 可通过
            Authenticator.setDefault(null)取消全局配置
          
         * 
            Authenticator.setDefault(Authenticator
           a)关于a参数的说明如下：
         * (The authenticator to be set. If a is {@code null} then any previously set authenticator is removed.)
         */
        if(needProxy && 
            SOCKS.equals(proxyType)
           && needLogin){
            //用户名和密码验证
            
            Authenticator.setDefault(new
           Authenticator(){
                protected  PasswordAuthentication  getPasswordAuthentication(){
                    PasswordAuthentication p = new PasswordAuthentication(proxyUsername, 
            proxyPassword.toCharArray());
          
                    return p;
                }
            });
        }
    }

    /**
     * 设置代理信息，可以在发请求前进行调用，用于替换此类中的代理相关的变量,全局设置一次就可
     * needProxy 是否需要代理连接
     * needLogin 代理连接是否需要账号和密码，为true时填上proxyUsername和proxyPassword
     * proxyType 代理类型,http,socks分别为http代理和sock5代理
     * proxyHost 代理IP
     * proxyPort 代理端口
     * proxyUsername 代理账号，needLogin为true时不能为空
     * proxyPassword 代理密码，needLogin为true时不能为空
     */
    public static void setProxy(boolean needProxy,boolean needLogin,String proxyType,String proxyHost,int proxyPort,String proxyUserName,String proxyPassword){

        
            HttpsKitWithProxyAuth.needProxy
           = needProxy;
        
            HttpsKitWithProxyAuth.needLogin
           = needLogin;
        
            HttpsKitWithProxyAuth.proxyType
           = proxyType;
        
            HttpsKitWithProxyAuth.proxyHost
           = proxyHost;
        
            HttpsKitWithProxyAuth.proxyPort
           = proxyPort;
        
            HttpsKitWithProxyAuth.proxyUsername
           = proxyUserName;
        
            HttpsKitWithProxyAuth.proxyPassword
           = proxyPassword;

    }

    private static CloseableHttpClient getHttpClient() {

        if (httpClient == null) {
            // 多线程下多个线程同时调用getHttpClient容易导致重复创建httpClient对象的问题,所以加上了同步锁
            synchronized (syncLock) {
                if (httpClient == null) {

                    try {
                        httpClient = createHttpClient();
                    } catch (KeyManagementException e) {
                        
            logger.error(
          "error",e);
                    } catch (NoSuchAlgorithmException e) {
                        
            logger.error(
          "error",e);
                    } catch (KeyStoreException e) {
                        
            logger.error(
          "error",e);
                    }

                    // 开启监控线程,对异常和空闲线程进行关闭
                    monitorExecutor = 
            Executors.newScheduledThreadPool(1);
          
                    
            monitorExecutor.scheduleAtFixedRate(new
           TimerTask() {
                        @Override
                        public void run() {

                            // 关闭异常连接
                            
            manager.closeExpiredConnections();
          

                            // 关闭5s空闲的连接
                            
            manager.closeIdleConnections(HttpIdelTimeout,TimeUnit.MILLISECONDS);
          

                            //
            logger.info(manager.getTotalStats().toString());
          
                            //
            logger.info(
          "close expired and idle for over "+HttpIdelTimeout+"ms connection");
                        }

                    }, HttpMonitorInterval, HttpMonitorInterval, 
            TimeUnit.MILLISECONDS);
          
                }
            }
        }
        return httpClient;
    }

    /**
     * 构建httpclient实例
     * @return
     * @throws KeyStoreException
     * @throws NoSuchAlgorithmException
     * @throws KeyManagementException
     */
    private static CloseableHttpClient createHttpClient() throws NoSuchAlgorithmException, KeyStoreException, KeyManagementException {

        SSLContextBuilder builder = new SSLContextBuilder();
        // 全部信任 不做身份鉴定
        
            builder.loadTrustMaterial(null,
           new TrustStrategy() {
            @Override
            public boolean isTrusted(X509Certificate[] x509Certificates, String s) throws CertificateException {
                return true;
            }
        });

        ConnectionSocketFactory plainSocketFactory = null;
        LayeredConnectionSocketFactory sslSocketFactory = null;

        /**
         * 如果需要进行Sock5代理访问开放如下代码
         * */
        if(needProxy && 
            SOCKS.endsWith(proxyType)){
          

            plainSocketFactory = new MyConnectionSocketFactory();
            sslSocketFactory = new MySSLConnectionSocketFactory(
            builder.build());
          

        }else {

            plainSocketFactory = 
            PlainConnectionSocketFactory.getSocketFactory();
          
            sslSocketFactory = new SSLConnectionSocketFactory(
            builder.build(),
           
            NoopHostnameVerifier.INSTANCE);
          

        }

        Registry<ConnectionSocketFactory> registry = RegistryBuilder
                .<ConnectionSocketFactory> create()
                .register("http", plainSocketFactory)
                .register("https", sslSocketFactory).build();

        manager = new PoolingHttpClientConnectionManager(registry);
        // 设置连接参数
        
            manager.setMaxTotal(MAX_CONN);
           // 最大连接数
        
            manager.setDefaultMaxPerRoute(Max_PRE_ROUTE);
           // 路由最大连接数

        // 请求失败时,进行请求重试
        HttpRequestRetryHandler handler = new HttpRequestRetryHandler() {

            @Override
            public boolean retryRequest(IOException e, int i, HttpContext httpContext) {

                if (i > 3) {
                    // 重试超过3次,放弃请求
                    
            logger.error(
          "retry has more than 3 time, give up request");
                    return false;
                }
                if (e instanceof NoHttpResponseException) {
                    // 服务器没有响应,可能是服务器断开了连接,应该重试
                    
            logger.error(
          "receive no response from server, retry");
                    return true;
                }
                if (e instanceof SSLHandshakeException) {
                    // SSL握手异常
                    
            logger.error(
          "SSL hand shake exception");
                    return false;
                }
                if (e instanceof InterruptedIOException) {
                    // 超时
                    
            logger.error(
          "InterruptedIOException");
                    return false;
                }
                if (e instanceof UnknownHostException) {
                    // 服务器不可达
                    
            logger.error(
          "server host unknown");
                    return false;
                }
                if (e instanceof ConnectTimeoutException) {
                    // 连接超时
                    
            logger.error(
          "Connection Time out");
                    return false;
                }
                if (e instanceof SSLException) {
                    
            logger.error(
          "SSLException");
                    return false;
                }

                HttpClientContext context = 
            HttpClientContext.adapt(httpContext);
          
                HttpRequest request = 
            context.getRequest();
          

                if (!(request instanceof HttpEntityEnclosingRequest)) {
                    // 如果请求不是关闭连接的请求
                    return true;
                }
                return false;
            }
        };

        CloseableHttpClient client = null;
        /**
         * 如果需要进行HTTPS代理访问开放如下代码
         * */
        if(needProxy && 
            HTTP.endsWith(proxyType)){
          

            client = 
            HttpClients.custom()
          
                    .setConnectionManager(manager)
                    .setProxy(new HttpHost(proxyHost, proxyPort))
                    .setRetryHandler(handler).build();

        }else {

            client = 
            HttpClients.custom()
          
                    .setConnectionManager(manager)
                    .setRetryHandler(handler).build();

        }

        return client;
    }

    public static String get(String url) {
        return get(url, null);
    }

    public static String get(String url,Map<String,Object> headerParams) {

        HttpGet httpGet = new HttpGet(url);
        
            httpGet.setHeader(
          "User-Agent",USER_AGENT);
        
            httpGet.setConfig(requestConfig);
          

        if(headerParams != null && 
            headerParams.size()>0){
          
            for(String headerName : 
            headerParams.keySet())
           {
                
            httpGet.setHeader(headerName,headerParams.get(headerName)+
          "");
            }
        }

        CloseableHttpResponse response = null;
        InputStream in = null;

        String result = null;

        try {

            HttpClientContext ctx  = createContext();
            response = getHttpClient().execute(httpGet,ctx);

            HttpEntity entity = 
            response.getEntity();
          
            if (entity != null) {
                in = 
            entity.getContent();
          
                result = 
            IOUtils.toString(
          in, "utf-8");
            }

        } catch (Exception e) {
            
            logger.error(
          "error",e);
        } finally {
            try {
                if (in != null) 
            in.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }

            try {
                if (response != null) 
            response.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }
        }

        return result;
    }

    public static String postJson(String url,Map<String,Object> requestParams) {
        return postJson(url, 
            JsonUtil.toJSONString(requestParams));
          
    }

    public static String postJson(String url,Map<String,Object> requestParams,Map<String,String> headerParams) {
        return postJson(url, 
            JsonUtil.toJSONString(requestParams),headerParams);
          
    }

    public static String postJson(String url,String requestParamStr) {
        return postJson(url, requestParamStr, null);
    }

    /**
     * PUT方式调用http请求方法
     * @param url
     * @param requestParamStr
     * @param headerParams
     * @return
     */
    public static String put(String url,String requestParamStr,Map<String,String> headerParams) {

        HttpPut httpput = new HttpPut(url);
        
            httpput.setHeader(
          "Content-Type", APPLICATION_JSON+";charset=" + 
            CharEncoding.UTF_8);
          
        
            httpput.setHeader(
          "Accept",APPLICATION_JSON+";charset="+
            CharEncoding.UTF_8);
          
        
            httpput.setHeader(
          "User-Agent",USER_AGENT);

        if(headerParams != null && 
            headerParams.size()>0){
          
            for(String headerName : 
            headerParams.keySet())
           {
                
            httpput.setHeader(headerName,headerParams.get(headerName)+
          "");
            }
        }

        StringEntity se = new StringEntity(requestParamStr,
            CharEncoding.UTF_8);
          
        
            se.setContentType(APPLICATION_JSON+
          ";charset=" +
            CharEncoding.UTF_8);
          
        
            httpput.setEntity(se);
          
        
            httpput.setConfig(requestConfig);
          

        CloseableHttpResponse response = null;
        InputStream in = null;

        String result = null;

        try {

            HttpClientContext ctx  = createContext();
            response = getHttpClient().execute(httpput,ctx);

            HttpEntity entity = 
            response.getEntity();
          
            if (entity != null) {
                in = 
            entity.getContent();
          
                result = 
            IOUtils.toString(
          in, "utf-8");
            }

        } catch (Exception e) {
            
            logger.error(
          "error",e);
        } finally {
            try {
                if (in != null) 
            in.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }

            try {
                if (response != null) 
            response.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }
        }

        return result;

    }

    /**
     * 创建一个HttpClientContext
     * @return
     * @throws MalformedChallengeException
     */
    public static HttpClientContext createContext() throws MalformedChallengeException{

        HttpClientContext ctx  = 
            HttpClientContext.create();
          

        /**
         * 如果需要进行Sock5代理访问
         */
        if(needProxy && 
            SOCKS.endsWith(proxyType)){
          
            InetSocketAddress socksaddr = new InetSocketAddress(proxyHost,proxyPort);
            
            ctx.setAttribute(
          "
            socks.address"
          , socksaddr);
        }else{

            /**
             * 如果需要进行HTTPS代理访问开放如下代码
             */
            if(needProxy && 
            HTTP.endsWith(proxyType)){
          

                /**
                 * 代理连接认证如果需要认证账号和密码时处理
                 */
                if(needLogin){

                    AuthState authState = new AuthState();
                    BasicScheme basicScheme = new BasicScheme();
                    
            basicScheme.processChallenge(new
           BasicHeader(
            AUTH.PROXY_AUTH,
           "BASIC realm=default"));
                    
            authState.update(basicScheme,
           new UsernamePasswordCredentials(proxyUsername, proxyPassword));
                    
            ctx.setAttribute(HttpClientContext.PROXY_AUTH_STATE,
           authState);

                }

            }

        }
        return ctx;
    }

    public static String postJson(String url,String requestParamStr,Map<String,String> headerParams) {

        HttpPost httppost = new HttpPost(url);

        
            httppost.setHeader(
          "Content-Type", APPLICATION_JSON+";charset=" + 
            CharEncoding.UTF_8);
          
        
            httppost.setHeader(
          "Accept",APPLICATION_JSON+";charset="+
            CharEncoding.UTF_8);
          
        
            httppost.setHeader(
          "User-Agent",USER_AGENT);

        if(headerParams != null && 
            headerParams.size()>0){
          
            for(String headerName : 
            headerParams.keySet())
           {
                
            httppost.setHeader(headerName,headerParams.get(headerName)+
          "");
            }
        }

        StringEntity se = new StringEntity(requestParamStr,
            CharEncoding.UTF_8);
          
        
            se.setContentType(APPLICATION_JSON+
          ";charset=" +
            CharEncoding.UTF_8);
          
        
            httppost.setEntity(se);
          

        
            httppost.setConfig(requestConfig);
          

        CloseableHttpResponse response = null;
        InputStream in = null;

        String result = null;

        try {

            HttpClientContext ctx  = createContext();
            response = getHttpClient().execute(httppost,ctx);

            HttpEntity entity = 
            response.getEntity();
          
            if (entity != null) {
                in = 
            entity.getContent();
          
                result = 
            IOUtils.toString(
          in, "utf-8");
            }

        } catch (Exception e) {
            
            logger.error(
          "error",e);
        } finally {
            try {
                if (in != null) 
            in.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }

            try {
                if (response != null) 
            response.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }
        }

        return result;
    }

    //requestParamStr---------->>> name=test&age=12
    public static String postFormUrlencoded(String url,String requestParamStr) {
        return postFormUrlencoded(url, requestParamStr ,null);

    }

    public static String postFormUrlencoded(String url,String requestParamStr,Map<String,Object> headerParams) {
        Map<String,String> requestParams = new HashMap<String,String>();

        String[] strs = 
            requestParamStr.split(
          "&");
        for(String str : strs) {
            String[] keyValues = 
            str.split(
          "=");
            if(
            keyValues.length
           == 2) {
                
            requestParams.put(keyValues[0],
           keyValues[1]);
            }
        }

        return postFormUrlencoded(url, requestParams,headerParams);

    }

    public static String postFormUrlencoded(String url,Map<String,String> requestParams) {
        return postFormUrlencoded(url,requestParams,null);
    }

    public static String postFormUrlencoded(String url,Map<String,String> requestParams,Map<String,Object> headerParams) {

        HttpPost httppost = new HttpPost(url);

        //application/json
        
            httppost.setHeader(
          "Content-Type", APPLICATION_FORM_URLENCODED+";charset=" + 
            CharEncoding.UTF_8);
          
        
            httppost.setHeader(
          "Accept",APPLICATION_JSON+";charset="+
            CharEncoding.UTF_8);
          
        
            httppost.setHeader(
          "User-Agent",USER_AGENT);

        if(headerParams != null && 
            headerParams.size()>0){
          
            for(String headerName : 
            headerParams.keySet())
           {
                
            httppost.setHeader(headerName,headerParams.get(headerName)+
          "");
            }
        }

        List<NameValuePair> formparams = new ArrayList<NameValuePair>();

        for(String keyStr : 
            requestParams.keySet())
           {
            
            formparams.add(new
           BasicNameValuePair(keyStr, 
            requestParams.get(keyStr)));
          
        }

        UrlEncodedFormEntity uefe = new UrlEncodedFormEntity(formparams, 
            Consts.UTF_8);
          
        
            httppost.setEntity(uefe);
          

        
            httppost.setConfig(requestConfig);
          

        CloseableHttpResponse response = null;
        InputStream in = null;

        String result = null;

        try {

            HttpClientContext ctx  = createContext();
            response = getHttpClient().execute(httppost,ctx);

            HttpEntity entity = 
            response.getEntity();
          
            if (entity != null) {
                in = 
            entity.getContent();
          
                result = 
            IOUtils.toString(
          in, "utf-8");
            }

        } catch (Exception e) {
            
            logger.error(
          "error",e);
        } finally {
            try {
                if (in != null) 
            in.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }

            try {
                if (response != null) 
            response.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }
        }

        return result;

    }

    //文件上传的通用方法例子测试, 除了file部分参数外，写死了格外的字段参数如scene,output，后台将接收到file,scene,output三个参数，可以根据需求修改
    public static String postFormMultipart(String url,InputStream fin,String originalFilename) {

        HttpPost httppost = new HttpPost(url);

        
            httppost.setConfig(requestConfig);
          
        InputStreamBody bin = new InputStreamBody(fin, originalFilename);

        MultipartEntityBuilder multipartEntityBuilder = 
            MultipartEntityBuilder.create();
          
        
            multipartEntityBuilder.addPart(
          "file",bin);
        
            multipartEntityBuilder.addPart(
          "fileName",new StringBody(originalFilename,
            ContentType.TEXT_PLAIN));
          
        
            multipartEntityBuilder.addPart(
          "fileSize",new StringBody("1024",
            ContentType.TEXT_PLAIN));
          
        
            multipartEntityBuilder.addPart(
          "scene", new StringBody("default",
            ContentType.TEXT_PLAIN));
          
        
            multipartEntityBuilder.addPart(
          "output", new StringBody("json2",
            ContentType.TEXT_PLAIN));
          
        HttpEntity reqEntity = 
            multipartEntityBuilder.build();
          

        
            httppost.setEntity(reqEntity);
          

        CloseableHttpResponse response = null;
        InputStream in = null;
        String result = null;
        try {

            HttpClientContext ctx  = createContext();
            response = getHttpClient().execute(httppost,ctx);

            HttpEntity entity = 
            response.getEntity();
          
            if (entity != null) {
                in = 
            entity.getContent();
          
                result = 
            IOUtils.toString(
          in, "utf-8");
            }

        } catch (Exception e) {
            
            logger.error(
          "error",e);
        } finally {
            try {
                if (in != null) 
            in.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }

            try {
                if (response != null) 
            response.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }
        }

        return result;

    }

    /**
     * 下载文件到本地
     * @param downloadUrl
     * @param savePathAndName
     */
    public static void downloadFile(String downloadUrl,String savePathAndName){
        HttpGet httpGet = new HttpGet(downloadUrl);
        
            httpGet.setHeader(
          "User-Agent",USER_AGENT);
        
            httpGet.setConfig(requestConfig);
          

        CloseableHttpResponse response = null;
        InputStream in = null;

        try {

            response = getHttpClient().execute(httpGet,
            HttpClientContext.create());
          

            HttpEntity entity = 
            response.getEntity();
          
            if (entity != null) {
                in = 
            entity.getContent();
          

                //如果path传进来是/结束的话处理一下，先去掉。
                FileOutputStream out = new FileOutputStream(new File(savePathAndName));
                
            IOUtils.copy(
          in, out);
                
            out.close();
          

            }

        } catch (IOException e) {
            
            logger.error(
          "error",e);
        } finally {
            try {
                if (in != null) 
            in.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }

            try {
                if (response != null) 
            response.close();
          
            } catch (IOException e) {
                
            logger.error(
          "error",e);
            }
        }
    }

    /**
     * 下载文件到本地
     * @param downloadUrl
     * @param saveFileName
     * @param savePath
     */
    public static void downloadFile(String downloadUrl,String saveFileName,String savePath){

        //如果path传进来是/结束的话处理一下，先去掉。
        String savePathAndName = 
            savePath.endsWith(
          "/") ? 
            savePath.substring(0,savePath.lastIndexOf(
          "/")) : savePath;
        downloadFile(downloadUrl, savePathAndName);

    }

    /**
     * 关闭连接池
     */
    public static void closeConnectionPool() {

        if(manager != null) 
            manager.close();
          
        if(monitorExecutor != null) 
            monitorExecutor.shutdown();
          
        try {if(httpClient != null) 
            httpClient.close();}
           catch (IOException e) {
            logger.error(
          "error",e);}

        manager = null;
        monitorExecutor = null;
        httpClient = null;

    }

    private static class MyConnectionSocketFactory extends PlainConnectionSocketFactory {

        @Override
        public Socket createSocket(final HttpContext context) throws IOException {
            InetSocketAddress socksaddr = (InetSocketAddress) 
            context.getAttribute(
          "
            socks.address"
          );
            Proxy proxy = new Proxy(
            Proxy.Type.SOCKS,
           socksaddr);
            return new Socket(proxy);
        }

        @Override
        public Socket connectSocket(int connectTimeout, Socket socket, HttpHost host, InetSocketAddress remoteAddress,
                                    InetSocketAddress localAddress, HttpContext context) throws IOException {
            // Convert address to unresolved
            InetSocketAddress unresolvedRemote = InetSocketAddress
                    .createUnresolved(
            host.getHostName(),
           
            remoteAddress.getPort());
          
            return 
            super.connectSocket(connectTimeout,
           socket, host, unresolvedRemote, localAddress, context);
        }

    }

    private static class MySSLConnectionSocketFactory extends SSLConnectionSocketFactory {

        public MySSLConnectionSocketFactory(final SSLContext sslContext) {
            // You may need this verifier if target site's certificate is not secure
            super(sslContext, 
            NoopHostnameVerifier.INSTANCE);
          

        }

        @Override
        public Socket createSocket(final HttpContext context) throws IOException {
            InetSocketAddress socksaddr = (InetSocketAddress) 
            context.getAttribute("socks.address");
          
            Proxy proxy = new Proxy(
            Proxy.Type.SOCKS,
           socksaddr);
            return new Socket(proxy);
        }

        @Override
        public Socket connectSocket(int connectTimeout, Socket socket, HttpHost host, InetSocketAddress remoteAddress,
                                    InetSocketAddress localAddress, HttpContext context) throws IOException {
            // Convert address to unresolved
            InetSocketAddress unresolvedRemote = InetSocketAddress
                    .createUnresolved(
            host.getHostName(),
           
            remoteAddress.getPort());
          
            return 
            super.connectSocket(connectTimeout,
           socket, host, unresolvedRemote, localAddress, context);
        }

    }

    public static void main(String[] args) throws InterruptedException, MalformedURLException {

        String url = "
            https://api.openai.com/v1/chat/completions";
          
        url = "
            https://www.baidu.com";
          
        
            System.out.println(HttpsKitWithProxyAuth.get(url));
          

        //关闭连接池，正式环境中这个不要关闭
        
            HttpsKitWithProxyAuth.closeConnectionPool();
          

    }

}
```
```
package 
            com.ruoyi.web.controller.meetingminutes.utils;
          

/**
 * @Author 不要有情绪的  ljy
 * @Date 2024/10/31 20:35
 * @Description:
 */

import 
            java.io.IOException;
          
import 
            java.text.SimpleDateFormat;
          
import 
            java.time.LocalDate;
          
import 
            java.time.LocalDateTime;
          
import 
            java.time.format.DateTimeFormatter;
          
import 
            java.util.List;
          
import 
            java.util.Map;
          
import 
            java.util.TimeZone;
          

import 
            org.slf4j.Logger;
          
import 
            org.slf4j.LoggerFactory;
          

import 
            com.fasterxml.jackson.annotation.JsonAutoDetect.Visibility;
          
import 
            com.fasterxml.jackson.annotation.JsonInclude;
          
import 
            com.fasterxml.jackson.annotation.PropertyAccessor;
          
import 
            com.fasterxml.jackson.core.JsonProcessingException;
          
import 
            com.fasterxml.jackson.core.type.TypeReference;
          
import 
            com.fasterxml.jackson.databind.DeserializationFeature;
          
import 
            com.fasterxml.jackson.databind.JavaType;
          
import 
            com.fasterxml.jackson.databind.ObjectMapper;
          
import 
            com.fasterxml.jackson.databind.SerializationFeature;
          
import 
            com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
          
import 
            com.fasterxml.jackson.datatype.jsr310.deser.LocalDateDeserializer;
          
import 
            com.fasterxml.jackson.datatype.jsr310.deser.LocalDateTimeDeserializer;
          
import 
            com.fasterxml.jackson.datatype.jsr310.ser.LocalDateSerializer;
          
import 
            com.fasterxml.jackson.datatype.jsr310.ser.LocalDateTimeSerializer;
          

//
            https://www.cnblogs.com/christopherchan/p/11071098.html
          
public class JsonUtil {

    private final static Logger logger = 
            LoggerFactory.getLogger(JsonUtil.class);
          

    //日期格式化
    private static final String STANDARD_FORMAT = "yyyy-MM-dd HH:mm:ss";

    private static ObjectMapper objectMapper;

    static{

        /**
         * ObjectobjectMapper是JSON操作的核心，Jackson的所有JSON操作都是在ObjectobjectMapper中实现。
         * ObjectobjectMapper有多个JSON序列化的方法，可以把JSON字符串保存File、OutputStream等不同的介质中。
         * writeValue(File arg0, Object arg1)把arg1转成json序列，并保存到arg0文件中。
         * writeValue(OutputStream arg0, Object arg1)把arg1转成json序列，并保存到arg0输出流中。
         * writeValueAsBytes(Object arg0)把arg0转成json序列，并把结果输出成字节数组。
         * writeValueAsString(Object arg0)把arg0转成json序列，并把结果输出成字符串。
         */
        objectMapper = new ObjectMapper();

        //对象的所有字段全部列入
        
            objectMapper.setSerializationInclusion(JsonInclude.Include.ALWAYS);
          

        //取消默认转换timestamps形式
        
            objectMapper.configure(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS,
          false);

        //忽略空Bean转json的错误
        
            objectMapper.configure(SerializationFeature.FAIL_ON_EMPTY_BEANS,
          false);

        //所有的日期格式都统一为以下的样式，即yyyy-MM-dd HH:mm:ss
        
            objectMapper.setDateFormat(new
           SimpleDateFormat(STANDARD_FORMAT));

        //忽略 在json字符串中存在，但是在java对象中不存在对应属性的情况。防止错误
        
            objectMapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES,
          false);

        
            objectMapper.setTimeZone(TimeZone.getTimeZone(
          "GMT+8"));
        
            objectMapper.setVisibility(PropertyAccessor.ALL,
           
            Visibility.ANY);
          

        //开启美化功能
        //
            objectMapper.enable(SerializationFeature.INDENT_OUTPUT);
          

        //解决Java8 LocalDate,LocalDateTime等序列化问题
        JavaTimeModule module=new JavaTimeModule();
        
            module.addSerializer(LocalDateTime.class,new
           LocalDateTimeSerializer(
            DateTimeFormatter.ofPattern(
          "yyyy-MM-dd HH:mm:ss")));
        
            module.addDeserializer(LocalDateTime.class,new
           LocalDateTimeDeserializer(
            DateTimeFormatter.ofPattern(
          "yyyy-MM-dd HH:mm:ss")));
        
            module.addSerializer(LocalDate.class,new
           LocalDateSerializer(
            DateTimeFormatter.ofPattern(
          "yyyy-MM-dd")));
        
            module.addDeserializer(LocalDate.class,new
           LocalDateDeserializer(
            DateTimeFormatter.ofPattern(
          "yyyy-MM-dd")));
        
            objectMapper.registerModule(module);
          

    }

    /**
     * 对象转Json格式字符串
     * @param obj 对象
     * @return Json格式字符串
     */
    public static String toJSONString(Object s) {

        if (s == null) {
            return null;
        }

        if (s instanceof String)
            return (String) s;

        String jsonValue = null;
        try {
            jsonValue = 
            objectMapper.writeValueAsString(s);
          
        } catch (JsonProcessingException e) {
            
            logger.error(
          "Parse Object to String error",e);
        }

        return jsonValue;

    }

    @SuppressWarnings("unchecked")
    public static Map<String,Object> castToObject(String fromValue){
        if(fromValue == null || "".equals(fromValue) ){
            return null;
        }

        try {
            return 
            objectMapper.readValue(fromValue,
           
            Map.class);
          
        } catch (Exception e) {
            
            logger.error(
          "Parse String to Object error:", e);
            return null;
        }

    }

    /**
     * 字符串转换为自定义对象
     * @param str 要转换的字符串
     * @param clazz 自定义对象的class对象
     * @return 自定义对象
     */
    @SuppressWarnings("unchecked")
    public static <T> T castToObject(String fromValue, Class<T> clazz){
        if(fromValue == null || "".equals(fromValue) || clazz == null){
            return null;
        }

        try {
            return 
            clazz.equals(String.class)
           ? (T) fromValue : 
            objectMapper.readValue(fromValue,
           clazz);
        } catch (Exception e) {
            
            logger.error(
          "Parse String to Object error:", e);
            return null;
        }

    }

    @SuppressWarnings("unchecked")
    public static <T> T castToObject(String fromValue, TypeReference<T> typeReference) {
        if (fromValue == null || "".equals(fromValue) || typeReference == null) {
            return null;
        }
        try {
            return (T) (
            typeReference.getType().equals(String.class)
           ? fromValue : 
            objectMapper.readValue(fromValue,
           typeReference));
        } catch (IOException e) {
            
            logger.error(
          "Parse String to Object error:", e);
            return null;
        }
    }

    public static <T> T castToObject(String fromValue, Class<?> collectionClazz, Class<?>... elementClazzes) {
        JavaType javaType = 
            objectMapper.getTypeFactory().constructParametricType(collectionClazz,
           elementClazzes);
        try {
            return 
            objectMapper.readValue(fromValue,
           javaType);
        } catch (IOException e) {
            
            logger.error(
          "Parse String to Object error : ", 
            e.getMessage());
          
            return null;
        }
    }

    public static <T> T getValue(String fromValue, Class<T> clazz){
        return castToObject(fromValue,clazz);
    }

    public static <T> T getValue(String fromValue, TypeReference<T> toValueTypeRef){
        return castToObject(fromValue, toValueTypeRef);
    }

    public static <T> T getValue(String fromValue, Class<?> collectionClazz, Class<?>... elementClazzes){
        return castToObject(fromValue, collectionClazz, elementClazzes);
    }

    //可通过点语法获取数据，如getValue("
            data.list"
          ,"xxxxxxxx",
            List.class);
          
    public static <T> T getValue(String key, String fromValue, Class<T> clazz){
        Map<String,Object> infoMap = castToObject(fromValue);
        if(infoMap == null) return null;

        return getValue(key, infoMap, clazz);
    }

    //可通过点语法获取数据，如getValue("
            data.list"
          ,"xxxxxxxx",new TypeReference<List<User>>(){});
    public static <T> T getValue(String key, String fromValue, TypeReference<T> toValueTypeRef){
        Map<String,Object> infoMap = castToObject(fromValue);
        if(infoMap == null) return null;

        return getValue(key, infoMap, toValueTypeRef);
    }

    public static <T> T getValue(String key, String fromValue, Class<?> collectionClazz, Class<?>... elementClazzes){
        Map<String,Object> infoMap = castToObject(fromValue);
        if(infoMap == null) return null;
        return getValue(key, infoMap, collectionClazz, elementClazzes);
    }

    //可通过点语法获取数据，如getValue("
            data.list"
          ,new TypeReference<List<User>>(){});
    @SuppressWarnings("rawtypes")
    public static <T> T getValue(String key, Map fromMap, Class<T> clazz) {

        try {

            // 首先将key进行拆分
            String[] keys = 
            key.split(
          "[.]");

            for (int i = 0; i < 
            keys.length;
           i++) {

                Object value = 
            fromMap.get(keys[i]);
          
                if(value == null) return null;

                if (i < 
            keys.length
           - 1) {
                    fromMap = (Map) value;
                }else {
                    return 
            objectMapper.convertValue(value,
           clazz);
                }
            }

        } catch (Exception e) {
            
            logger.error(
          "getValue error : ", 
            e.getMessage());
          
            return null;
        }

        return null;

    }

    @SuppressWarnings("rawtypes")
    public static <T> T getValue(String key, Map fromMap, Class<?> collectionClazz, Class<?>... elementClazzes){
        try {

            // 首先将key进行拆分
            String[] keys = 
            key.split(
          "[.]");

            for (int i = 0; i < 
            keys.length;
           i++) {

                Object value = 
            fromMap.get(keys[i]);
          
                if(value == null) return null;

                if (i < 
            keys.length
           - 1) {
                    fromMap = (Map) value;
                }else {
                    JavaType javaType = 
            objectMapper.getTypeFactory().constructParametricType(collectionClazz,
           elementClazzes);
                    return 
            objectMapper.convertValue(value,
           javaType);
                }

            }

        } catch (Exception e) {
            
            logger.error(
          "getValue error : ", 
            e.getMessage());
          
            return null;
        }

        return null;
    }

    @SuppressWarnings("rawtypes")
    public static <T> T getValue(String key, Map fromMap, TypeReference<T> toValueTypeRef) {

        try {

            // 首先将key进行拆分
            String[] keys = 
            key.split(
          "[.]");

            for (int i = 0; i < 
            keys.length;
           i++) {

                Object value = 
            fromMap.get(keys[i]);
          
                if(value == null) return null;

                if (i < 
            keys.length
           - 1) {
                    fromMap = (Map) value;
                }else {
                    return 
            objectMapper.convertValue(value,
           toValueTypeRef);
                }

            }

        } catch (Exception e) {
            
            logger.error(
          "getValue error : ", 
            e.getMessage());
          
            return null;
        }

        return null;

    }

    /**
     * 将对像转换成具体的其他Bean对像
     * @param fromValue
     * @param toValueTypeRef
     * @return
     */
    public static <T> T convertValue(Object fromValue, TypeReference<T> toValueTypeRef){

        try {
            return 
            objectMapper.convertValue(fromValue,
           toValueTypeRef);
        } catch (Exception e) {
            
            logger.error(
          "convertValue error : ", 
            e.getMessage());
          
            return null;
        }

    }

    public static <T> T convertValue(Object fromValue, Class<T> toValueType){

        try {
            return 
            objectMapper.convertValue(fromValue,
           toValueType);
        } catch (Exception e) {
            
            logger.error(
          "convertValue error : ", 
            e.getMessage());
          
            return null;
        }

    }

    public static String getString(Map<String,Object> fromMap, String fieldName){
        return 
            fromMap.get(fieldName)==null
           ? null : 
            fromMap.get(fieldName).toString();
          
    }

    //根据filedName的key查找map为空时，使用对应的defaultValue默认值替换返回
    public static String getString(Map<String,Object> jsonObject, String fieldName,String defaultValue){
        return 
            jsonObject.get(fieldName)==null
           ? defaultValue : 
            jsonObject.get(fieldName).toString();
          
    }

    public static Integer getInteger(Map<String,Object> jsonObject, String fieldName){
        return 
            jsonObject.get(fieldName)==null
           ? null : (Integer)
            jsonObject.get(fieldName);
          
    }

    public static Double getDouble(Map<String,Object> jsonObject, String fieldName){
        return 
            jsonObject.get(fieldName)==null
           ? null : (Double)
            jsonObject.get(fieldName);
          
    }

    public static Boolean getBoolean(Map<String,Object> jsonObject, String fieldName){
        return 
            jsonObject.get(fieldName)==null
           ? false : (Boolean)
            jsonObject.get(fieldName);
          
    }

    public static Long getLong(Map<String,Object> jsonObject, String fieldName){
        return 
            jsonObject.get(fieldName)==null
           ? null : (Long)
            jsonObject.get(fieldName);
          
    }

    public static <T> List<T> getList(Map<String,Object> jsonObject, String fieldName,Class<T> clazz){
        return 
            jsonObject.get(fieldName)==null
           ? null : 
            JsonUtil.getValue(fieldName,
           jsonObject, 
            List.class,clazz);
          
    }

}
```

## 3、问题总结

开始敲黑板了

### 3.1、访问案例失败

部署完成后，可能存在很多问题，例如：访问 example 访问失败，那么使用

```
systemctl status ds*
```

查看有没有启动对应的服务

### 3.2、加载 word 文档失败

修改启动的配置文件，将 token 去除，更改配置文件 [local.json](http://local.json/) 和 [default.json，配置文件位置](http://default.xn--json,-qn2hjuo63ldzycda4341c/)

```
/etc/onlyoffice/documentserver
```

`              local.json            ` 中将参数 token 都改为 false，去除 token

```
"token": {
   "enable": {
     "request": {
       "inbox": false,
       "outbox": false
     },
     "browser": false
   },
```

`              default.json            ` 中将参数 `request-filtering-agent` 改为 true，token 也改为 false， `rejectUnauthorized` 改为 false

```
"request-filtering-agent" : {
     "allowPrivateIPAddress": true,
     "allowMetaIPAddress": true
    },
"token": {
     "enable": {
      "browser": false,
      "request": {
       "inbox": false,
       "outbox": false
      }
   },
"rejectUnauthorized": false
```

修改了以上配置参数后，重启服务，再次测试。

以上更基本能解决报错文档权限问题，文档保存失败问题，文档下载问题等报错信息。

### 3.3、系统后端有 token 验证问题

如果你访问的地址需要携带 token，进行 token 验证（自己的系统后台，并非 onlyoffice 的 token），那么可以通过配置下面代码的形式进行解决，例如：我的访问路径为 `http:192.168.123.123:8089/getFile/12` ，去除 token 验证（ `             requests.antMatchers("/callback",            "/getFile/*", "/login", "/register", "/captchaImage").permitAll()` ）

```
@Bean
protected SecurityFilterChain filterChain(HttpSecurity httpSecurity) throws Exception {
    return httpSecurity
            // CSRF禁用，因为不使用session
            .csrf(csrf -> 
            csrf.disable())
          
            // 禁用HTTP响应标头
            .headers((headersCustomizer) -> {
                
            headersCustomizer.cacheControl(cache
           -> 
            cache.disable()).frameOptions(options
           -> 
            options.sameOrigin());
          
            })
            // 认证失败处理类
            .exceptionHandling(exception -> 
            exception.authenticationEntryPoint(unauthorizedHandler))
          
            // 基于token，所以不需要session
            .sessionManagement(session -> 
            session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
          
            // 注解标记允许匿名访问的url
            .authorizeHttpRequests((requests) -> {
                
            permitAllUrl.getUrls().forEach(url
           -> 
            requests.antMatchers(url).permitAll());
          
                // 对于登录login 注册register 验证码captchaImage 允许匿名访问
                
            requests.antMatchers(
          "/callback", "/getFile/*", "/login", "/register", "/captchaImage").permitAll()
                        // 静态资源，可匿名访问
                        .antMatchers(
            HttpMethod.GET,
           "/", "/*.html", "/**/*.html", "/**/*.css", "/**/*.js", "/profile/**").permitAll()
                        .antMatchers("/
            swagger-ui.html"
          , "/swagger-resources/**", "/webjars/**", "/*/api-docs", "/druid/**").permitAll()
                        // 除上面外的所有请求全部需要鉴权认证
                        .anyRequest().authenticated();
            })
            // 添加Logout filter
            .logout(logout -> 
            logout.logoutUrl(
          "/logout").logoutSuccessHandler(logoutSuccessHandler))
            // 添加JWT filter
            .addFilterBefore(authenticationTokenFilter, 
            UsernamePasswordAuthenticationFilter.class)
          
           //添加CORS filter
            .addFilterBefore(corsFilter, 
            JwtAuthenticationTokenFilter.class)
          
            .addFilterBefore(corsFilter, 
            LogoutFilter.class)
          
            .build();
}
```

### 3.4、使用文档地址访问问题

如果你不采用上面的方式，即 `http:192.168.123.123:8089/getFile/12` 的方式，你想采用 `http:192.168.123.123:8089/word/             1234.docx           ` 的方式，也是可以的，但是你需要将文档挂到一个服务上，例如使用 ngnix 作为代理，进行 `/word/             1234.docx           ` 的重定向。

下面你可以直接使用一个在线的 docx 链接来测试你是否部署成功，在线链接：

[https://d2nlctn12v279m.cloudfront.net/assets/docs/samples/zh/demo.docx](https://d2nlctn12v279m.cloudfront.net/assets/docs/samples/zh/demo.docx)

即将前端代码中的 url 替换为上面的链接。

## 4、后记

如果你看到这里，那么代表你将要成功了，整个过程比较艰难，前后弄了两三天，还好最后结果是好的，所以简单总结一下，勉励自己。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/SpringBoot+OnlyOffice%EF%BC%9A%E4%BC%98%E9%9B%85%E5%AE%9E%E7%8E%B0%E5%9C%A8%E7%BA%BF%20Word%20%E7%BC%96%E8%BE%91%E3%80%81%E8%BD%AC%E5%8C%96%E3%80%81%E4%BF%9D%E5%AD%98%E7%AD%89%E5%8A%9F%E8%83%BD/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. Druid 崩了，线上直接炸锅！3. 面试官：分库分表后会带来哪些问题？你能答上来几个？4. 蚂蚁又开源了一个顶级 Java 项目！
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文