---
title: 使用Docker在Windows上部署独立MySQL
tags:
  - mysql
categories:
  - mysql
date: 2026-04-02 14:22:48
---

# **使用 Docker 在 Windows 上部署独立 MySQL 8.0 容器（带持久化与自定义配置）**

> 发布时间：2026年4月2日
> 适用环境：Windows + Docker Desktop + PowerShell

在开发或测试环境中，我们常常需要一个轻量、可复用、数据持久化的 MySQL 数据库。使用 Docker 是实现这一目标的高效方式。本文将详细介绍如何在 **Windows 系统**上通过 **Docker** 部署一个**完全独立**的 MySQL 8.0 容器，并实现：

- 数据目录持久化到本地磁盘
- 配置文件可自定义并挂载
- 支持外部客户端连接（如 Navicat、MySQL Workbench）
- 兼容主流应用（避免认证插件问题）
- 自动重启保障服务可用性

------

## **一、准备工作**

### **1. 创建本地目录**

首先，在 `D:\` 盘创建用于存储数据和配置的目录：

powershell



```
mkdir D:\dockerDir\mysql\lib
mkdir D:\dockerDir\mysql\conf
```

- `lib`：用于存放 MySQL 的数据库文件（持久化核心）
- `conf`：用于存放自定义 `.cnf` 配置文件（可选）

### **2. 创建 Docker 自定义网络（推荐）**

为了便于未来容器间通信（例如 Web 应用容器连接此数据库），建议使用自定义网络：

powershell



```
docker network create docker-net
```

> 若你仅需本地访问 MySQL，此步可跳过，但保留更利于扩展。

### **3. 授权 Docker 访问 D 盘**

打开 **Docker Desktop → Settings → Resources → File Sharing**，确保 `D:\` 已加入共享路径列表，然后点击 **Apply & Restart**。

------

## **二、一键启动 MySQL 容器**

在 **PowerShell** 中执行以下单行命令：

powershell



```
docker run -d --name mysql --network docker-net -e MYSQL_ROOT_PASSWORD=123456 -p 3306:3306 -v D:\dockerDir\mysql\lib:/var/lib/mysql -v D:\dockerDir\mysql\conf:/etc/mysql/conf.d --restart unless-stopped mysql:8.0 --default-authentication-plugin=mysql_native_password --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

------

## **三、命令详解**

表格



| 参数                                    | 作用说明                                          |
| :-------------------------------------- | :------------------------------------------------ |
| `-d`                                    | 后台运行容器（detached 模式）                     |
| `--name mysql`                          | 容器命名为 `mysql`，便于管理                      |
| `--network docker-net`                  | 加入名为 `docker-net` 的自定义网络                |
| `-e MYSQL_ROOT_PASSWORD=123456`         | 设置 root 用户密码为 `123456`（必需）             |
| `-p 3306:3306`                          | 将宿主机 3306 端口映射到容器，允许本地客户端连接  |
| `-v D:\...\lib:/var/lib/mysql`          | 挂载数据目录，实现持久化                          |
| `-v D:\...\conf:/etc/mysql/conf.d`      | 挂载配置目录，支持自定义配置                      |
| `--restart unless-stopped`              | 容器自动重启（除非手动停止）                      |
| `mysql:8.0`                             | 使用官方 MySQL 8.0 镜像                           |
| `--default-authentication-plugin=...`   | 使用兼容性更好的 `mysql_native_password` 认证插件 |
| `--character-set-server=utf8mb4`        | 默认字符集设为 `utf8mb4`（支持 emoji）            |
| `--collation-server=utf8mb4_unicode_ci` | 使用更准确的 Unicode 排序规则                     |

------

## **四、验证部署是否成功**

### **1. 查看容器状态**

powershell



```
docker ps -f name=mysql
```

应看到 `mysql` 容器处于 `Up` 状态。

### **2. 测试数据库连接**

进入容器并登录 MySQL：

powershell



```
docker exec -it mysql mysql -uroot -p123456
```

若出现 `mysql>` 提示符，说明部署成功！

### **3. （可选）添加自定义配置**

在 `D:\dockerDir\mysql\conf` 下创建 `custom.cnf` 文件，例如：

ini



```
[mysqld]
default-time-zone = '+08:00'
max_connections = 500
innodb_buffer_pool_size = 256M
```

然后重启容器使配置生效：

powershell



```
docker restart mysql
```

------

## **五、常见问题与注意事项**

- **权限错误？** → 确保 Docker Desktop 已授权访问 `D:\`。
- **端口冲突？** → 如果本机已安装 MySQL，可将 `-p 3306:3306` 改为 `-p 3307:3306`，通过 `localhost:3307` 连接。
- **忘记密码？** → 删除容器（`docker rm -f mysql`）后重新运行命令即可重置（**注意：删除容器不会删除 `lib` 中的数据！** 若需彻底重置，请清空 `lib` 目录）。
- **仅容器间访问？** → 可省略 `-p 3306:3306`，提高安全性。

------

## **六、总结**

通过上述步骤，你已成功部署了一个 **生产级可用的 MySQL 开发环境**，具备：

✅ 数据持久化
✅ 配置灵活可调
✅ 外部工具友好
✅ 自动恢复能力

该方案适用于个人开发、团队测试、CI/CD 环境搭建等多种场景。后续如需部署其他服务（如 Redis、PostgreSQL、Web 应用等），只需将其加入同一 `docker-net` 网络，即可通过容器名直接通信，构建完整的微服务架构。

------

> 📌 **提示**：本文所有操作均基于 **独立 MySQL 服务**，不依赖任何第三方应用（如 Nacos），确保通用性和简洁性。

如有疑问，欢迎留言交流！
