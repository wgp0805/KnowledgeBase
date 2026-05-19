---
title: Docker部署Redis全攻略：持久化、自定义网络与配置详解
tags:
  - redis
categories:
  - redis
date: 2026-04-02 14:35:09
---

## 一、准备工作：目录与配置文件

首先，我们需要在宿主机上准备好配置文件和数据存储目录。

### 1. 创建目录结构

在本地创建一个目录用于存放配置和数据，例如：`D:\dockerDir\redis\conf`。

### 2. 创建配置文件

在上述`conf`目录下新建一个`redis.conf`文件。

### 3. 编辑配置

用文本编辑器打开`redis.conf`，填入以下基础配置：

```
# 允许所有IP访问，方便局域网内其他服务连接
bind 0.0.0.0
# 关闭保护模式，配合密码认证使用
protected-mode no
# Redis服务端口
port 6379
# 开启AOF持久化，确保数据安全
appendonly yes
# 设置访问密码，生产环境请务必修改为强密码
requirepass 123456
```

---

## 二、创建Docker网络

为了让Redis容器与其他容器在同一个网络内通过容器名通信，我们先创建一个专属的Docker网络。

**可复制的一行命令**

```
docker network create docker-net
```

---

## 三、拉取Redis镜像

从Docker Hub拉取官方最新的Redis镜像。

**可复制的一行命令**

```
docker pull redis
```

---

## 四、启动Redis容器

这是最关键的一步。我们将使用`docker run`命令，把之前准备好的配置文件、数据目录以及网络设置全部挂载和指定进去。

**可复制的一行命令**

```
docker run -d --name redis --network docker-net -p 6379:6379 -v D:/dockerDir/redis/conf/redis.conf:/usr/local/etc/redis/redis.conf -v D:/dockerDir/redis/data:/data redis redis-server /usr/local/etc/redis/redis.conf
```

---

## 五、验证部署

容器启动后，我们需要确认它是否正常运行。

### 1. 检查容器状态

执行以下命令，查看容器状态是否为`Up`。

```
docker ps
```

### 2. 连接Redis测试

进入容器内部，使用`redis-cli`连接并测试。

```
docker exec -it redis redis-cli -a 123456
```

连接成功后，尝试写入和读取数据：

```
127.0.0.1:6379> SET test "hello"
OK
127.0.0.1:6379> GET test
"hello"
```

如果返回正常，说明部署成功！此时，你可以去`D:\dockerDir\redis\data`目录下查看，应该能看到生成的`appendonly.aof`持久化文件。

---

## 六、命令参数详解

| 参数                                                   | 说明                                       |
| ------------------------------------------------------ | ------------------------------------------ |
| `-d`                                                   | 后台运行容器（守护进程模式）               |
| `--name redis`                                         | 将容器命名为`redis`，方便后续管理和记忆    |
| `--network docker-net`                                 | 将容器连接到创建的`docker-net`网络中       |
| `-p 6379:6379`                                         | 将宿主机的6379端口映射到容器的6379端口     |
| `-v D:/.../redis.conf:/usr/local/etc/redis/redis.conf` | 将本地的配置文件挂载到容器内的默认配置路径 |
| `-v D:/.../data:/data`                                 | 将本地的数据目录挂载到容器内的`/data`目录  |
| `redis`                                                | 指定使用的镜像名称                         |
| `redis-server /usr/local/etc/redis/redis.conf`         | 告诉容器启动时使用自定义配置文件           |

---

## 七、注意事项

1. **配置文件格式**：Redis配置文件必须使用`指令 值`的格式，不支持XML标签格式。
2. **目录存在**：确保`D:\dockerDir\redis\data`文件夹已存在，否则Docker可能会创建失败。
3. **密码安全**：生产环境中请务必修改默认密码`123456`为强密码。
4. **网络通信**：其他容器加入`docker-net`网络后，可以通过`redis:6379`直接访问Redis服务。

---

## 八、常见问题排查

### 启动失败

- 检查配置文件格式是否正确
- 确认挂载路径是否存在
- 查看容器日志：`docker logs redis`

### 连接问题

- 确认端口映射是否正确
- 检查防火墙设置
- 验证密码是否正确

---

通过以上步骤，您已经成功在Docker中部署了Redis，并实现了数据持久化和自定义网络配置。这个方案既适合开发环境，也适合生产环境的基础部署需求。
