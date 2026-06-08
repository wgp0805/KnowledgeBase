### 什么是 MinIO？能干什么？

**MinIO** 是一款基于 Go 语言开发的高性能、分布式开源对象存储系统。它完全兼容 Amazon S3 API，这意味着你可以像使用 AWS S3 一样使用 MinIO，现有的 S3 生态工具链可以无缝迁移。

**主要用途：**

1. **非结构化数据存储**：非常适合存储海量图片、视频、音频、日志文件、备份数据和容器/虚拟机镜像等。
2. **私有云存储构建**：企业需要独立掌控数据主权时，可快速搭建私有对象存储服务，避免依赖公有云。
3. **AI与大数据基础设施**：作为数据湖的存储后端，无缝对接 Hadoop、Spark 等大数据组件，以及作为 AI/ML 训练数据集的存储。
4. **混合云架构**：可作为私有云与公有云之间的数据桥梁。

---

### 使用 Docker 安装 MinIO 详细教程

MinIO 完全支持使用 Docker 进行安装部署。根据你的需求，以下是将配置文件存储在 `D:\dockerDir\minIO\conf`，数据持久化在 `D:\dockerDir\minIO\data` 的完整操作指南。

#### 1. 准备工作

确保你的 Windows 系统已经安装并启动了 Docker Desktop。  
在本地创建好对应的文件夹，用于挂载配置和数据：

powershell

编辑

```
mkdir D:\dockerDir\minIO\conf
mkdir D:\dockerDir\minIO\data
```

#### 2. 拉取 MinIO 官方镜像

打开终端（CMD 或 PowerShell），执行以下命令拉取最新版镜像：

powershell

编辑

```
docker pull minio/minio
```

#### 3. 启动 MinIO 容器

执行以下命令启动 MinIO 服务。这里我们映射了 **9000**（API 服务端口）和 **9001**（Web 控制台端口）：

powershell

编辑

```
docker run -d ^
  --name minio ^
  -p 9000:9000 ^
  -p 9001:9001 ^
  -e "MINIO_ROOT_USER=admin" ^
  -e "MINIO_ROOT_PASSWORD=123456" ^
  -v D:\dockerDir\minIO\data:/data ^
  -v D:\dockerDir\minIO\conf:/root/.minio ^
  minio/minio server /data --console-address ":9001"
```

**关键参数说明：**

- `-e "MINIO_ROOT_USER=admin"` 和 `-e "MINIO_ROOT_PASSWORD=admin123456"`：设置管理员账号和密码。MinIO 没有传统的配置文件，而是通过环境变量驱动配置。密码要求长度至少 8 位。
- `-v D:\dockerDir\minIO\data:/data`：将宿主机的数据目录映射到容器内的 `/data`，实现**数据持久化**。
- `-v D:\dockerDir\minIO\conf:/root/.minio`：将宿主机的配置目录映射到容器内的 `/root/.minio`。MinIO 运行时的配置（如加密的凭证、IAM 策略、TLS 证书等）会保存在此目录，防止容器重启或销毁后配置丢失。
- `--console-address ":9001"`：指定 Web 管理控制台监听的端口。

#### 4. 验证与使用

1. **访问控制台**：打开浏览器，访问 `http://localhost:9001`。
2. **登录**：输入刚才设置的账号（`admin`）和密码（`admin123456`）进行登录。
3. **创建存储桶（Bucket）**：在左侧菜单点击 **Buckets** -> **Create Bucket**，输入一个名称（如 `test-bucket`）并创建。
4. **上传文件**：进入刚创建的 Bucket，点击 **Upload** 按钮，上传任意图片或文本文件进行测试。上传成功后，说明存储读写功能完全正常。

#### 5. 进阶：使用命令行客户端 (mc) 管理

除了网页端，你还可以使用 MinIO 官方提供的命令行工具 `mc` 进行高效管理：

powershell

编辑

```
# 配置连接你的本地 MinIO
mc alias set myminio http://localhost:9000 admin admin123456

# 列出所有存储桶
mc ls myminio

# 将本地文件上传到存储桶
mc cp D:\test.txt myminio/test-bucket/
```

#### ⚠️ 注意事项

- **密码安全**：上述教程中的 `admin123456` 仅为演示使用。在生产环境中，请务必设置包含大小写字母、数字和符号的高强度密码（建议长度 ≥12 位）。
- **权限问题**：在 Windows Docker 环境下，通常会自动处理挂载目录的权限。但如果遇到“Permission denied”错误，请确保 `D:\dockerDir\minIO\data` 和 `conf` 目录具有读写权限。