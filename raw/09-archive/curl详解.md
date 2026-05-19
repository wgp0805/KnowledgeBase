---
title: curl详解
tags:
  - curl
categories:
  - liunx
date: 2025-07-29 09:52:02
---

`curl`（Client URL）是一个强大的命令行工具，用于在终端中传输数据（支持 HTTP、HTTPS、FTP、FTPS、SCP、SFTP 等协议）。它广泛应用于 API 测试、文件下载、自动化脚本等场景。以下从基础到高级功能详解：

---

### **一、基础用法**

#### 1. **下载文件**

```bash
curl -O http://example.com/file.zip      # 下载文件到当前目录（保留原名）
curl -o custom_name.zip http://example.com/file.zip  # 指定保存文件名
```

#### 2. **发送 GET 请求**

```bash
curl https://api.example.com/data        # 获取响应内容
curl -i https://api.example.com/data     # 包含响应头（-i）
```

#### 3. **发送 POST 请求**

```bash
# 表单数据
curl -d "name=John&age=30" -X POST https://api.example.com/users

# JSON 数据
curl -H "Content-Type: application/json" -d '{"name":"John"}' https://api.example.com/users
```

---

### **二、核心选项详解**

| 选项   | 作用                     | 示例                                                         |
| ------ | ------------------------ | ------------------------------------------------------------ |
| `-X`   | 指定 HTTP 方法           | `curl -X DELETE https://api.example.com/item/1`              |
| `-H`   | 添加请求头               | `curl -H "Authorization: Bearer token" https://api.example.com` |
| `-d`   | 发送 POST 数据           | `curl -d "param=value" https://example.com`                  |
| `-F`   | 上传文件/表单            | `curl -F "file=@photo.jpg" https://example.com/upload`       |
| `-L`   | 跟随重定向               | `curl -L http://example.com`                                 |
| `-v`   | 显示详细通信过程（调试） | `curl -v https://example.com`                                |
| `-u`   | 基本认证                 | `curl -u user:pass https://example.com`                      |
| `-x`   | 使用代理                 | `curl -x http://proxy:8080 https://example.com`              |
| `-k`   | 忽略 SSL 证书验证        | `curl -k https://self-signed-cert.com`                       |
| `-s`   | 静默模式（不显示进度）   | `curl -s https://example.com > output`                       |
| `-C -` | 断点续传                 | `curl -C - -O http://example.com/largefile.zip`              |

---

### **三、高级用法**

#### 1. **文件上传**

```bash
# 上传文件 (multipart/form-data)
curl -F "file=@localfile.png" https://example.com/upload

# 添加额外字段
curl -F "file=@img.jpg" -F "description=My Image" https://example.com/upload
```

#### 2. **Cookie 操作**

```bash
curl -b "session=abc123" https://example.com       # 发送 Cookie
curl -c cookies.txt https://example.com            # 保存响应 Cookie 到文件
curl -b cookies.txt https://example.com            # 从文件读取 Cookie
```

#### 3. **限速下载**

```bash
curl --limit-rate 200K -O http://example.com/largefile.iso  # 限制 200KB/s
```

#### 4. **输出到文件**

```bash
curl -o output.html http://example.com        # 保存为文件
curl http://example.com | jq .                # 通过管道处理 JSON
```

#### 5. **调试与日志**

```bash
curl -v https://example.com                     # 显示请求/响应详情
curl --trace output.txt https://example.com     # 记录完整通信过程
```

#### 6. **FTP 操作**

```bash
curl -u ftpuser:ftppass ftp://example.com/file.txt -O   # 下载 FTP 文件
curl -T localfile.txt ftp://example.com/upload/         # 上传文件到 FTP
```

---

### **四、实用场景示例**

#### 1. **测试 API**

```bash
# 带 JSON 头的 POST 请求
curl -H "Content-Type: application/json" \
     -H "X-API-Key: 12345" \
     -d '{"query": "hello"}' \
     https://api.example.com/endpoint
```

#### 2. **下载并解压**

```bash
curl -L https://example.com/archive.tar.gz | tar xz
```

#### 3. **模拟浏览器请求**

```bash
curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" \
     -e "https://google.com" \
     https://example.com
```

#### 4. **批量下载**

```bash
# 下载多个文件 (URL1, URL2, URL3)
curl -O https://example.com/file1.jpg -O https://example.com/file2.jpg
```

---

### **五、注意事项**

1. **敏感数据**：避免在命令中直接暴露密码（用 `-u user:pass` 时会被 `ps` 命令看到），建议使用 `--netrc` 或环境变量。

2. **编码问题**：  

   - 使用 `--data-urlencode` 对 POST 数据编码：  

     ```bash
     curl --data-urlencode "name=John Doe" http://example.com
     ```

3. **大文件下载**：  

   - 用 `-C -` 断点续传，避免网络中断重头开始。

---

### 六. 认证与权限

curl 支持多种认证方式，适用于需要权限验证的接口或服务。

- **基本认证（Basic Auth）**
  用 `-u` 参数指定用户名和密码（格式：`username:password`）。
  示例：

  ```bash
  curl -u admin:123456 https://example.com/protected  # 用户名 admin，密码 123456
  ```

- **Bearer Token 认证**
  常用于 OAuth2 授权，Token 通过 `Authorization` 头传递。
  示例：

  ```bash
  curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." https://api.example.com/data
  ```

- **Digest 认证**
  用 `--digest` 参数启用 Digest 认证（比基本认证更安全）。
  示例：

  ```bash
  curl --digest -u username:password https://example.com/digest-protected
  ```

#### 5. 其他实用功能

- **跟随重定向**
  用 `-L` 参数自动跟随 HTTP 重定向（3xx 状态码）。
  示例：

  ```bash
  curl -L https://example.com/redirect  # 自动跳转至最终 URL
  ```

- **断点续传**
  用 `-C -` 从上次中断的位置继续下载（需服务器支持）。
  示例：

  ```bash
  curl -C - -O https://example.com/large-file.zip  # 续传大文件
  ```

- **使用代理**
  用 `-x` 参数指定代理服务器（支持 HTTP、SOCKS 等代理类型）。
  示例：

  ```bash
  # HTTP 代理
  curl -x http://proxy_ip:port https://example.com
  
  # SOCKS5 代理
  curl -x socks5://proxy_ip:port https://example.com
  ```

- **超时设置**

  - `-m <秒数>`：设置总超时（连接 + 传输）；
  - `--connect-timeout <秒数>`：单独设置连接超时；
    示例：

  ```bash
  curl -m 10 --connect-timeout 5 https://example.com  # 总超时 10 秒，连接超时 5 秒
  ```

- **显示详细过程**
  用 `-v`（verbose）参数输出传输过程的详细日志（包括 DNS 解析、TCP 连接、SSL 握手等），适合调试。
  示例：

  ```bash
  curl -v https://httpbin.org/get  # 显示完整请求/响应细节
  ```

### 七、高级特性

- **Cookie 处理**

  - `-c <文件>`：将服务器返回的 Cookie 保存到文件；
  - `-b <文件>`：从文件加载 Cookie 并发送到服务器；
    示例：

  ```bash
  curl -c cookies.txt https://example.com/login  # 保存登录 Cookie
  curl -b cookies.txt https://example.com/user   # 使用 Cookie 访问需要登录的页面
  ```

- **SSL/TLS 选项**

  - `--insecure`：忽略 SSL 证书验证（测试环境用，生产环境不推荐）；
  - `--cacert <文件>`：指定自定义 CA 证书；
    示例：

  ```bash
  curl --insecure https://self-signed.example.com  # 访问自签名证书的网站
  ```

- **配置文件**
  可通过 `~/.curlrc`（Linux/macOS）或 `%APPDATA%\curl\.curlrc`（Windows）设置默认参数，避免重复输入。例如：

  ```bash
  # ~/.curlrc 内容
  -H "User-Agent: MyCurl/1.0"  # 默认 User-Agent
  --connect-timeout 10          # 默认连接超时 10 秒
  ```

### **八、帮助与文档**

- 查看所有选项：`curl --help`
- 详细文档：`man curl`
- 官方指南：[curl.se/docs/](https://curl.se/docs/)

掌握 `curl` 能高效处理网络任务，是开发者和运维的必备工具！
