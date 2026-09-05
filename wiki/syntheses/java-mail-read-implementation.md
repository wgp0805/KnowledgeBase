---
title: "Java 项目实现读取邮件功能"
type: synthesis
tags: [Java, 邮件, IMAP, Jakarta-Mail, Spring-Boot, 通用知识]
sources: []
last_updated: 2026-08-19
---

# Java 项目实现读取邮件功能

> **来源说明**：本地知识库中无 Java 读取邮件（IMAP/POP3/JavaMail）的专门记录，本页为通用知识回答，结合知识库中相关的异步处理、定时任务、模板引擎等条目综合整理。

## 一、技术选型

| 方案 | 协议 | 适用场景 |
|------|------|---------|
| **IMAP**（推荐） | IMAP | 需要远程管理邮件（标记已读、分类、不删除服务器邮件），适合长期运行的邮件处理系统 |
| **POP3** | POP3 | 只需下载邮件到本地，简单场景 |
| **Exchange Web Services** | EWS | 企业用 Microsoft Exchange Server 时 |

Java 生态标准方案是 **Jakarta Mail**（原 JavaMail），Spring Boot 通过 `spring-boot-starter-mail` 封装。

## 二、Spring Boot 实现步骤

### 1. 引入依赖

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-mail</artifactId>
</dependency>
```

### 2. 配置 application.yml

```yaml
spring:
  mail:
    host: imap.exmail.qq.com        # 各邮箱服务商 IMAP 服务器地址
    port: 993
    username: your@email.com
    password: your-password-or-auth-code
    properties:
      mail:
        store:
          protocol: imaps
        imap:
          ssl:
            enable: true
        imap.timeout: 10000
```

> **注意**：QQ/163/Gmail 等邮箱需开启 IMAP 服务并使用**授权码**而非登录密码。Gmail 还需关闭"安全登录"或使用 App Password。

### 3. 读取邮件的核心代码

```java
import jakarta.mail.*;
import jakarta.mail.search.*;
import org.springframework.stereotype.Service;

import java.util.Properties;

@Service
public class MailReadService {

    @org.springframework.beans.factory.annotation.Value("${spring.mail.host}")
    private String host;
    @org.springframework.beans.factory.annotation.Value("${spring.mail.username}")
    private String username;
    @org.springframework.beans.factory.annotation.Value("${spring.mail.password}")
    private String password;

    public void readUnreadMails() throws Exception {
        Properties props = new Properties();
        props.put("mail.store.protocol", "imaps");
        props.put("mail.imaps.host", host);
        props.put("mail.imaps.ssl.enable", "true");

        Session session = Session.getInstance(props);
        Store store = session.getStore("imaps");
        store.connect(host, username, password);

        Folder inbox = store.getFolder("INBOX");
        inbox.open(Folder.READ_WRITE);

        // 只读未读邮件
        FlagTerm unreadFlag = new FlagTerm(new Flags(Flags.Flag.SEEN), false);
        Message[] messages = inbox.search(unreadFlag);

        for (Message msg : messages) {
            System.out.println("主题: " + msg.getSubject());
            System.out.println("发件人: " + msg.getFrom()[0]);
            System.out.println("时间: " + msg.getSentDate());
            System.out.println("内容: " + getTextFromMessage(msg));
            // 处理完后标记为已读
            msg.setFlag(Flags.Flag.SEEN, true);
        }

        inbox.close(false);
        store.close();
    }

    // 处理 multipart 邮件（纯文本 + HTML + 附件）
    private String getTextFromMessage(Message message) throws Exception {
        if (message.isMimeType("text/plain")) {
            return (String) message.getContent();
        }
        if (message.isMimeType("multipart/*")) {
            Multipart multipart = (Multipart) message.getContent();
            for (int i = 0; i < multipart.getCount(); i++) {
                BodyPart part = multipart.getBodyPart(i);
                if (part.isMimeType("text/plain")) {
                    return (String) part.getContent();
                }
            }
        }
        return "";
    }
}
```

## 三、常见邮箱 IMAP 服务器

| 邮箱 | IMAP 服务器 | 端口 |
|------|------------|------|
| QQ 企业邮箱 | imap.exmail.qq.com | 993 |
| QQ 个人邮箱 | imap.qq.com | 993 |
| 163 邮箱 | imap.163.com | 993 |
| Gmail | imap.gmail.com | 993 |
| Outlook | outlook.office365.com | 993 |

## 四、生产环境注意事项

1. **授权码**：QQ/163/Gmail 需在邮箱设置开启 IMAP 并生成授权码，配置里用授权码替代密码
2. **附件处理**：multipart 邮件需遍历 `BodyPart`，`part.getDisposition()` 为 `Part.ATTACHMENT` 时是附件，用 `part.getInputStream()` 读取
3. **定时拉取**：配合 [[PowerJob]] 或 [[XXL-JOB]] 定时任务，每 N 分钟拉取一次未读邮件
4. **连接复用**：不要每次都新建 Store，建议保持长连接或用连接池，避免被邮箱服务器限流
5. **HTML 邮件**：若需解析 HTML 内容，可用 Jsoup 提取纯文本
6. **异步处理**：邮件解析是 IO 密集型，可用 [[CompletableFuture]] 或 [[虚拟线程]] 异步处理，避免阻塞主线程

## 五、典型业务场景

- **工单系统**：用户回复邮件自动更新工单（参考 [[SolonAI-ReActAgent智能客服]] 的工单处理思路）
- **订单通知**：监听支付平台邮件通知，自动对账
- **告警聚合**：汇总多系统告警邮件，统一推送

## 关联连接

- [[SpringBoot]] - 承载框架
- [[FreeMarker]] - 邮件模板生成
- [[CompletableFuture]] - 异步处理
- [[虚拟线程]] - 高 IO 场景异步处理
- [[PowerJob]] - 定时拉取任务调度
- [[XXL-JOB]] - 定时拉取任务调度
- [[ApplicationEvent]] - 邮件事件解耦
- [[SolonAI-ReActAgent智能客服]] - 工单处理思路参考
