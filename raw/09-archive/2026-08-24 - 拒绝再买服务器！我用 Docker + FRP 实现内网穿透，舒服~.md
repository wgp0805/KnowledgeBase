---
source_url: "https://mp.weixin.qq.com/s/EkWio5w9oLpudYhm-5HD2A"
title: "拒绝再买服务器！我用 Docker + FRP 实现内网穿透，舒服~"
account: "Java学习者社区"
published_at: "2026-08-24 15:34:28"
saved_at: "2026-08-25 06:05:38"
sync_id: "art_dd7a1c41e9264b8387095a03cae43bd9"
parse_status: "ok"
---

# 拒绝再买服务器！我用 Docker + FRP 实现内网穿透，舒服~

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/ac7c28bbd0652d9f5d649549d2ee2589_MD5.png)

****

最近不少星球小伙伴询问，小哈书项目演示环境：http://116.62.199.48:7070/，它的内网穿透效果，是使用哪个工具搞定的？具体要怎么弄？我也想搞一个！

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/1a18621f73b15846a92718bb5eb06ccc_MD5.jpg)

## 背景说明

小哈书很长一段时间内，是没有演示环境的，一方面是后端核心功能还没开发完，前端还没搞定；另一个原因就是，它是一个微服务项目，光是服务就拆分了 12 个，另外还有不少中间件，如 RocketMQ, Cassandra, Elascticsearch 等等，都是吃内存的大户，事实也证明，整体单机单节点部署下来，共吃掉了 14G 的内存，这还是我未部署数据对齐服务，以及 xxl-job 的情况：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/5dd0817e4137dde37cdafc35983a3133_MD5.jpg)

14G+ 内存的云服务器！不用多说，一年的费用成本太高了，而且每年都得交！有没有什么法子，部署在本地电脑上，就可以暴露到公网中，让其他小伙伴也能访问呢？

答案是肯定的，那就是 —— **内网穿透**。

## 什么是内网穿透？

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/35398669ffb29eabf7272f5fec4a52bb_MD5.jpg)

内网穿透是一种技术手段，允许外部网络通过公网访问局域网（内网）中的设备或服务。目的是**突破内网隔离**，解决因缺乏公网 IP 或防火墙限制导致的外部无法直接访问内网资源的问题。

内网穿透的核心原理是**中间服务器转发**。内网设备主动与公网上的代理服务器（如frp、ngrok）建立连接。当外部用户访问代理服务器时，代理将请求转发给内网设备，再将响应返回给用户。

## FRP 介绍

**FRP（Fast Reverse Proxy）** 是一款开源的内网穿透工具，通过反向代理技术将内网服务暴露到公网。其核心功能是**将外部请求转发到内网设备**，支持 TCP、UDP、HTTP、HTTPS 等多种协议，广泛用于开发调试、远程访问等场景。

其优势如下：

- 开源免费，高度可控 ：代码完全公开（GitHub地址：fatedier/frp），可自行部署和修改，避免依赖第三方服务。无流量或连接数限制（商业工具如花生壳可能收费或限速）。
- 配置灵活，支持多协议 ：可转发任意 TCP/UDP 端口（如 SSH、远程桌面、数据库），也支持 HTTP/HTTPS 的域名绑定和负载均衡。
- 跨平台，轻量易用 ：服务端（frps）和客户端（frpc）均支持 Windows、Linux、macOS，甚至树莓派等嵌入式设备。仅需简单配置文件即可运行，无需复杂网络知识。
- 自建服务器，数据更安全 ：用户可完全掌控中转服务器（如阿里云、腾讯云等公网服务器），避免第三方工具的数据泄露风险。支持 TLS 加密传输，保障通信安全。
- 性能高效，扩展性强 ：流量中转延迟低，尤其适合对实时性要求高的场景（如远程桌面）。支持多客户端、多端口映射，企业级场景可通过插件扩展功能。

## 相比较其他工具

以下是常见的内网穿透工具对比：

| ** 工具 ** | ** 优势 ** | ** 劣势 ** |
| --- | --- | --- |
| ** FRP ** | 开源免费、自建服务器、协议支持全面 | 需自行维护公网服务器 |
| ** Ngrok ** | 无需自建服务器，快速启动 | 免费版限制多（域名随机、限速） |
| ** ZeroTier ** | P2P 直连，延迟低 | 依赖客户端软件，需组网配置 |
| ** 花生壳 ** | 简单易用，适合小白用户 | 免费版带宽低，商业版价格高 |

## 部署流程

FRP 的部署流程如下：

- 准备一台普通配置的云服务器 ，比如 2核2G ，2M 带宽的，在上面部署 FRP 服务端（frps）, 填写相关配置；
- 准备一台本地电脑 ，里面运行着你想要内网穿透的应用，如小哈书；并安装 FRP 客户端 (frpc)，并填写相关配置；

下图是小哈书演示环境的部署图，由于需要部署前端工程，所以内网穿透到的是 Nginx 端口上，本小节中，我们将演示的是，穿透到 Gataway 网关，步骤都是差不多的：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/e083eeb1ef018fda2d04e7f37e5741fc_MD5.jpg)

## 服务器安装 frps

废话不多说，上手实操一波。

### 下载镜像

登录到云服务器中，拉取  `frps`  的 Docker 镜像：

```
docker pull fatedier/frps:v0.61.2
```

如果你配置了 Docker 镜像加速，依然无法下载镜像。可以先在本地电脑上，执行上述命令，将镜像下载到本地：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/12a05bff47a32f0676d341325a862027_MD5.jpg)

然后，打开 cmd 命令行工具，进入到某个文件夹下，我这里是  `D:/`  根目录下：

```
cd D:/
```

执行如下命令，将下载好的本地镜像，导出为一个  `tar`  包：

```
docker save -o frps.tar fatedier/frps:v0.61.2
```

> **“**解释一下上述命令的参数：
> - **  `docker save`  **：Docker 的子命令，用于将镜像导出为 tar 文件；
> -  `-o frps.tar`  ：  `-o`  指定输出文件名（此处为  `frps.tar`  ）；
> -  `fatedier/frps:v0.61.2`  ： 要保存的镜像名称及标签（即  `镜像名:标签`  ）；

导出成功后，就可以在当前目录中看到这个  `tar`  包了。接着，我们将  `tar`  包上传到云服务器中，执行命令如下，导入此  `tar`  包，就可以完成镜像的离线安装了：

```
docker load -i frps.tar
```

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/f5025b7dc6efe719c500d429506dbf7c_MD5.jpg)

### 创建配置文件

frps 镜像下载完成后，我们在云服务的  `/docker`  目录下，创建一个  `/frps`  文件夹，用于放置  `frps`  的配置文件，命令如下：

```
cd /docker

mkdir frps
```

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/09cb374d88655cfdde5c40b9855e4e3f_MD5.jpg)

进入到  `/docker/frps`  文件夹中，创建一个名为  `frps.toml`  的配置文件：

```
 vim frps.toml
```

内容如下：

```
# FRPS 配置文件

# 服务端基础绑定配置
bindAddr = "0.0.0.0"  # 监听所有网络接口（0.0.0.0 表示接受任意来源连接）
bindPort = 7000       # FRP 核心服务端口，用于和客户端建立连接使用

# 管理控制台配置
webServer.addr = "0.0.0.0"    # 管理后台监听地址（开放给所有IP访问）
webServer.port = 7500         # 管理后台访问端口（通过浏览器访问此端口）
webServer.user = "admin"       # 管理后台登录用户名
webServer.password = "123456"  # 管理后台登录密码（建议使用高强度密码）

# 安全认证配置
auth.method = "token"  # 认证方式（token 为密钥验证）
auth.token = "5bk6QH80Annl9U1jdVa9T0RpUkU4bOKOpshZSe1ImuD7V2Jp8k5Dgxf5vFNRAOvuirhjaSnGDLIWWG6M0S5r3A=="  # 客户端连接必须携带此密钥

# 日志配置
log.level = "warn"     # 日志级别（trace/debug/info/warn/error）
log.to = "/opt/frps/frps.log"  # 日志文件存储路径（需确保写入权限）
```

### 运行容器

执行如下命令，将  `frps`  运行起来：

```
docker run --name frps \
   --restart unless-stopped \
   --network host \
   -e TZ=Asia/Shanghai \
   -v /docker/frps:/opt/frps \
   -d fatedier/frps:v0.61.2 -c /opt/frps/frps.toml
```

> **“**解释上述命令核心的参数：
> - **  `--restart unless-stopped`  **：容器退出时自动重启（除非手动停止）；
> - **  `--network host`  **：容器直接复用主机IP和端口；
> - **  `-v /docker/frps:/opt/frps`  **：将宿主机的  `/docker/frps`  目录映射到容器的  `/opt/frps`  目录；
> - **  `-c /opt/frps/frps.toml`  **：指定配置文件路径为容器内的  `/opt/frps/frps.toml`  ；

再通过  `docker ps`  命令，确认一下  `frps`  服务端是否正在运行中：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/04a3584fb5253931ff8536be6d217f5b_MD5.jpg)

### 添加安全组

接下来，我们需要配置一下云服务器的安全组。首先是，添加 7000 端口，此端口用于和 frpc 客户端进行通信。访问来源设置为 0.0.0.0/0, 表示所有人均可访问，这么配置，主要是考虑到家庭 IP 经常变动，开放给所有人，就不用频繁修改授权 IP 了：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/d15c28e212385605ea63127ac5b6606b_MD5.jpg)

然后，再添加一下 7500 端口，frps 的管理控制台需要使用此端口。访问来源仅授权给你的 IP:

> **“****TIP**: 如何获取当前网络的 IP, 可访问这个网站获得：https://www.ip138.com/。

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/d1b6e91f31d5aee92a6aef1a3224e9f4_MD5.jpg)

以上端口在安全组添加完毕后，打开浏览器，访问 frps 的管理控制台链接： `http://云服务公网IP:7500`  , 输入配置文件中配置的用户名与密码：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/7158ec391a81f3a6eeab0bf434d68e80_MD5.jpg)

即可登录到后台中，如下图所示：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/785ee6372e9c3e7f932f921a5bcd3318_MD5.jpg)

## 本地电脑安装 frpc

云服务器端搞定后，开始在本地电脑中安装 frpc 客户端。

### 下载镜像

打开 cmd 命令行，执行如下命令，拉取 frpc 的 Docker 镜像：

```
docker pull fatedier/frpc:v0.61.2
```

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/1780c45d012873848fe7236cde897f51_MD5.jpg)

### 创建配置文件

进入  `E:/docker`  目录下，创建一个  `/frpc`  文件夹：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/35c666633f1d861e78fc620c25637322_MD5.jpg)

进入到该文件夹下，准备开始编写 frpc 的配置文件  `frpc.toml` , 内容如下：

```
# FRPC 客户端配置文件

# 连接服务端配置
serverAddr = "116.0.120.57" # FRPS 服务端公网IP地址（需确保可访问性）
serverPort = 7000            # 对应服务端 bindPort 配置（默认7000）

# 认证配置（必须与服务端的保持一致）
auth.method = "token"
auth.token = "5bk6QH80Annl9U1jdVa9T0RpUkU4bOKOpshZSe1ImuD7V2Jp8k5Dgxf5vFNRAOvuirhjaSnGDLIWWG6M0S5r3A=="

# 日志配置
log.level = "warn"            # 日志级别（trace/debug/info/warn/error）
log.to = "/opt/frpc/frpc.log" # 日志文件路径（需确保目录存在且有写入权限）

# 代理规则配置（可配置多个 [[proxies]] 块）
[[proxies]]
name = "xiaohashu-gateway"  # 代理规则名称（需唯一）
type = "tcp"                # 代理类型（tcp/http/https/udp等）
localIP = "192.168.0.101"   # 本地需要穿透的内网服务IP地址
localPort = 8000            # 本地服务端口（如本机运行的 Spring Boot 应用端口，这里配置的是 Gateway 网关端口）
remotePort = 8000           # 服务端监听的远程端口
```

以上配置文件中，代理规则的  `localIP`  表示需要穿透的局域网 IP，可通过  `ipconfig`  命令来获取，如下图所示：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/e0f7f86c76341168a396686fc2a226ef_MD5.jpg)

代理规则中  `localPort`  配置项，表示你想内网穿透的本地端口，这里填写的 8000，即 Gataway 网关端口。 `remotePort`  表示需要访问云服务的 8000 端口，才能内网穿透到本地电脑的 8000 端口。

所以，还需要将 8000 端口也添加到安全组中，访问来源设置为  `0.0.0.0/0`  , 表示所有人都能访问。后续，我们就可以访问  `http://云服务器公网IP:8000`  ， 来访问到本地电脑的网关服务了：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/bbfa6539e9748ac290389fbbeec11f47_MD5.jpg)

### 运行容器

在 cmd 命令行中，执行如下命令，将 frpc 客户端运行起来：

```
docker run --name frpc \
   --restart=unless-stopped \
   -e TZ=Asia/Shanghai \
   -v E:\docker\frpc:/opt/frpc \
   -d fatedier/frpc:v0.61.2 -c /opt/frpc/frpc.toml
```

Windows 电脑需要转换为一行命令来执行，不然会报错：

```
docker run --name frpc --restart=unless-stopped -e TZ=Asia/Shanghai -v E:\docker\frpc:/opt/frpc -d fatedier/frpc:v0.61.2 -c /opt/frpc/frpc.toml
```

执行完成后，通过  `docker ps`  命令确认一下 frpc 容器正在运行中：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/b9fa8c99b85e488f24c95ed2e87c2821_MD5.jpg)

接着，登录到 frps 的管理后台，点击左侧栏的 “TCP” 协议菜单，如果看到客户端配置的内网穿透规则出现了，并且状态为  `online`  在线 , 说明内网穿透已经配置成功了：

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/2b440c4a7b2f8cb6be513c26960302cc_MD5.jpg)

## 测试一下效果

最后，我们通过 Apipost 工具，来测试一下是否真的生效了。调用 “获取笔记详情接口”，将之前的  `localhost`  地址，修改为云服务器的公网 IP 地址, 如果能够成功响应，说明大功告成啦！

![](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/abd2810cb6254b019abde59e9903c820_MD5.jpg)

[加入小哈的星球](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / Java 学习路线 / **社群讨论 / **学习打卡 / 每月赠书**

- 《仿小红书（微服务架构 ）》 已完结，基于 Spring Cloud Alibaba + Spring Boot 3.x + JDK 17..., [点击查看项目介绍](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247538491&idx=1&sn=576995017721766d0fe15723fd135619&chksm=fd5787bdca200eab54d2fb8ca07fcc2bffdec3eaab4ab82ab5eaf949f0254c1683455e02010b&token=343952052&lang=zh_CN&scene=21#wechat_redirect) ； 演示地址： http://116.62.199.48:7070/
- 《 Spring AI 应用（RAG 智能客服） 》已完结, 基于 Spring AI + Spring Boot 3.x + JDK 21
- 《 秒杀系统设计 》正在更新中，单体到微服务高并发架构演进

- 《 前后端分离博客项目（全栈开发） 》 已完结,演示链接： http://116.62.199.48/
- 项目阅读地址： https://quanxiaoha.com/column

截止目前，**累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

![图片](assets/2026-08-24%20-%20%E6%8B%92%E7%BB%9D%E5%86%8D%E4%B9%B0%E6%9C%8D%E5%8A%A1%E5%99%A8%EF%BC%81%E6%88%91%E7%94%A8%20Docker%20+%20FRP%20%E5%AE%9E%E7%8E%B0%E5%86%85%E7%BD%91%E7%A9%BF%E9%80%8F%EF%BC%8C%E8%88%92%E6%9C%8D~/b01fd91d58faf9455f8fbb5c64bb22f0_MD5.webp)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~
2. 面试官: 什么是用户态、内核态？如何切换的？
3. 滴滴一面：GPU 和 CPU 的区别是什么？为什么挖矿、大模型都用 GPU？
4. 面试官：什么是冷备、热备，暖备？
```

```

```

```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。
获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。
```

```
PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。
点“在看”支持小哈呀，谢谢
```

---
原文链接：https://mp.weixin.qq.com/s/EkWio5w9oLpudYhm-5HD2A
