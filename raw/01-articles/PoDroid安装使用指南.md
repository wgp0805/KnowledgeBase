# PoDroid 安装使用指南：旧手机畅玩 Docker

> 来源：抖音视频「旧手机畅玩Docker！PoDroid安装使用指南！无需ROOT刷机！」+ 官方文档整理
> 视频作者：在下莫老师 | 发布时间：2026-09-30

---

## 一、什么是 PoDroid

**PoDroid** 是一款可以在 Android 手机上运行完整 Linux 容器环境的应用，**无需 ROOT、无需刷机**。

它通过 QEMU 软件虚拟化技术，在你的旧手机上启动一个真正的 Alpine Linux 虚拟机，预装了 **Podman、Docker、LXC** 三大容器引擎，开箱即用。

### 核心亮点

- **无需 Root**：完全在用户空间运行，任何原生 Android 8+ 手机都能用
- **三大容器引擎**：Podman + Docker + LXC 零配置启动
- **自定义内核**：Linux 7.1.5 内核，内置 overlay2、cgroup v2、netfilter 等
- **真实终端**：xterm-256color 终端，支持鼠标、122 种配色、13 种字体
- **端口转发**：一键将 VM 端口暴露到手机真实 IP
- **内置 SSH**：Dropbear SSH 服务，可从电脑远程连接
- **X11 桌面**：应用内 X11 查看器，可运行 Firefox 等 GUI 程序
- **持久化存储**：所有安装和配置重启后不丢失

### 与 Termux / Google Terminal 对比

| 功能 | PoDroid | Termux | Google Terminal |
|------|---------|--------|-----------------|
| 需要 Root | ❌ 不需要 | ❌ 不需要 | ❌ 不需要 |
| 真实容器运行时 | ✅ Podman+Docker+LXC | ❌ | 需手动配置 |
| VM 隔离 | ✅ QEMU + AVF | ❌ 共享内核 | ✅ AVF |
| Docker Hub 镜像 | ✅ 直接拉取 | ❌ | 需手动配置 |
| 自定义内核 | ✅ Linux 7.1.5 | ❌ 宿主内核 | ✅ |
| 适用设备 | 任意 ARM64 Android 8+ | 所有设备 | 仅 Pixel |
| 端口转发 | ✅ | 需 socat | ❌ |
| SSH 服务 | ✅ 内置 | 需安装 | 需手动配置 |

---

## 二、环境要求

### 设备要求

- **CPU 架构**：ARM64（arm64-v8a），不支持 32 位或 x86 设备
- **系统版本**：Android 8.0（API 26）或更高
- **存储**：APK 约 200MB，VM 磁盘可从 2GB 到 512GB 自定义
- **推荐配置**：至少 4GB 内存，闲置旧手机最佳

### 硬件加速（可选）

在 **Pixel 8 / 8a / 9 / 9 Pro / 9 Pro XL / 10** 系列设备上，可开启 AVF (pKVM) 硬件加速，实现接近原生的 CPU 速度。其他设备默认使用 QEMU TCG 软件模拟。

---

## 三、安装步骤

### 第 1 步：下载 APK

PoDroid 不在 Google Play 上架，需从 GitHub Releases 页面下载：

```
GitHub 搜索：ExTV/Podroid → Releases → 下载最新 Podroid-release-*.apk
```

### 第 2 步：安装 APK

1. 进入 Android **设置 → 应用 → 特殊应用权限 → 安装未知应用**
2. 为你的浏览器或文件管理器开启"允许安装未知应用"
3. 打开下载的 APK 文件，点击 **安装**

### 第 3 步：首次启动向导

首次打开 PoDroid 会进入四步设置向导：

#### Step 1：持久化存储大小

- 选择 VM 磁盘镜像大小：**2GB ~ 512GB**（受手机剩余空间限制）
- 该镜像保存在应用私有存储中，存放 VM 内安装的所有软件、容器镜像和配置
- **建议**：尽量选大一些，后续只能扩容不能缩容

#### Step 2：VM 配置

- **CPU 核心数**：建议 2~4 核
- **内存分配**：默认 512MB，建议 **1GB 以上**（运行桌面环境需 2GB+）
- **SSH 开关**：开启后自动启动 Dropbear SSH 服务

#### Step 3：下载文件夹共享（可选）

- 开启后，手机的 Downloads 文件夹会挂载到 VM 的 `/mnt/downloads`
- 双向同步：手机下载的文件自动出现在 VM 中，反之亦然
- **注意**：QEMU 后端在某些设备上可能不稳定，如遇异常请关闭

#### Step 4：权限授予

- **通知权限**：VM 以前台服务运行，需通知权限显示运行状态
- **后台运行权限**：防止 Android 在应用切后台时杀死 VM
- 两项都建议授予，也可跳过后续再补

---

## 四、启动与首次运行

### 启动 VM

1. 点击主页 **Start VM** 按钮
2. 首次启动约需 **50~60 秒**（后续启动仅需 10~15 秒）
3. 首次启动会执行两个一次性任务：
   - **SSH 主机密钥生成**：约 25~35 秒（只执行一次）
   - **ext4 文件系统格式化**：按你选择的大小格式化磁盘镜像
4. 通知栏会显示启动进度："Starting SSH..." → "Almost ready..." → "Ready!"

### 打开终端

启动完成后，点击 **Open Terminal** 即可进入 Alpine Linux shell。

### 默认登录凭证

- **用户名**：`root`
- **密码**：`podroid`

> 终端每次启动都会显示该默认密码提示。

创建普通用户：

```bash
# 添加用户并加入 wheel 组（可使用 doas/sudo）
adduser -G wheel <用户名>
```

---

## 五、容器使用指南

PoDroid 启动后，**Podman、Docker、LXC 均已预配置并自动启动**，无需额外设置。

### 快速验证

```bash
# Podman：rootless 模式，开箱即用
podman run --rm alpine echo "Hello from Podroid!"

# Docker：已预安装并自动启动
docker run -d -p 8080:80 nginx

# LXC：网桥已就绪
lxc-create -t alpine -n test && lxc-start -n test
```

### 常用容器示例

#### 1. 运行 Nginx 网页服务

```bash
# 1. 创建测试页面
mkdir -p ~/site && echo '<h1>Hello from Podroid!</h1>' > ~/site/index.html

# 2. 启动 Nginx 容器
podman run -d --name hello \
  -p 8080:80 \
  -v ~/site:/usr/share/nginx/html:ro \
  docker.io/library/nginx:alpine

# 3. 验证（VM 内部）
wget -qO- http://localhost:8080
```

> 如需从手机浏览器或其他设备访问，需在 Settings → Port forwards 中添加 8080 → 8080 的端口转发规则。

#### 2. 自托管 Pi-hole（广告过滤 DNS）

```bash
podman run -d --name pihole \
  -p 8080:80 -p 5353:53/tcp \
  -e TZ=Asia/Shanghai \
  docker.io/pihole/pihole:latest
```

#### 3. 自托管 Gitea（Git 服务）

```bash
podman run -d --name gitea \
  -p 3000:3000 -p 2222:22 \
  -v gitea-data:/data \
  docker.io/gitea/gitea:latest-linux-arm64
```

#### 4. 自托管 Vaultwarden（密码管理）

```bash
podman run -d --name vaultwarden \
  -p 8888:80 \
  -v vaultwarden-data:/data \
  docker.io/vaultwarden/server:latest
```

#### 5. code-server（浏览器中的 VS Code）

```bash
podman run -d --name code-server \
  -p 8443:8443 \
  -v "$HOME/.config:/home/coder/.config" \
  -v "$PWD:/home/coder/project" \
  ghcr.io/coder/code-server:latest \
  --bind-addr 0.0.0.0:8443 /home/coder/project
```

### 镜像选择建议

- **必须使用 ARM64 镜像**：标签通常为 `:latest-linux-arm64` 或 `:arm64`
- **避免 x86/amd64 镜像**：会双重模拟，性能下降 50~100 倍
- **轻量镜像优先**：如 `nginx:alpine` 比 `nginx` 基础版小得多

---

## 六、SSH 远程连接

### 开启 SSH

在首次设置向导或 **Settings** 中开启 SSH 选项，Dropbear 会自动启动。

### 从电脑连接

确保手机和电脑在同一 Wi-Fi 网络下：

```bash
# 查看手机 IP：在 PoDroid 主页或 Status 页面查看
ssh root@<手机IP> -p 9922
# 密码：podroid
```

> **注意**：SSH 端口是 **9922** 而非 22，因为 Android 应用无法绑定 1024 以下的特权端口。

### VS Code Remote 连接

1. 确保 SSH 已开启
2. 在 VS Code 安装 **Remote - SSH** 扩展
3. 配置 SSH 连接：`ssh root@<手机IP> -p 9922`
4. 连接后即可像远程 Linux 服务器一样开发

### 文件传输（SFTP）

```bash
# 命令行方式
sftp -P 9922 root@<手机IP>

# 或使用 WinSCP / FileZilla 等图形化工具
# 协议：SFTP，端口：9922，用户：root，密码：podroid
```

---

## 七、端口转发

### 自动转发的端口

| 服务 | 手机端口 | VM 端口 | 协议 | 说明 |
|------|---------|---------|------|------|
| SSH | 9922 | 22 | TCP | 开启 SSH 时自动添加 |
| X11/VNC | 5900 | 5900 | TCP | 始终开启（应用内查看器用） |
| PulseAudio | 4713 | 4713 | TCP | 始终开启（音频流用） |

### 添加自定义转发

**方式一：应用设置**

1. 进入 **Settings → Port forwards → Add**
2. 输入手机端口（Host port）、VM 端口（VM port）
3. 选择协议：TCP / UDP / Both
4. QEMU 后端即时生效，无需重启 VM

**方式二：VM 内命令行**

```bash
# 添加转发：手机 8888 → VM 80
podroid-forward add 8888 80 tcp

# 简写形式
podroid-forward 8888 80

# 查看所有规则
podroid-forward list

# 删除规则
podroid-forward remove 8888 tcp

# 清除所有自定义规则
podroid-forward clean
```

### 端口限制说明

- **手机端端口必须 ≥ 1024**：Android 应用无特权端口绑定权限
- **建议使用 8080、8443、3000 等高位端口**
- 最多可保存 2048 条转发规则

---

## 八、X11 图形界面

### 打开 X11 查看器

在终端界面点击顶部栏的 **显示器图标**，即可打开应用内 X11 桌面查看器。

- 触摸 = 鼠标
- 软键盘 = 键盘输入
- 支持音频流（PulseAudio）

### 安装 GUI 应用

```bash
# 安装 XFCE 桌面环境
apk add xfce4 xfce4-terminal mousepad ristretto xfce4-taskmanager

# 安装 Firefox 浏览器
apk add firefox

# 安装 GIMP 图像编辑器
apk add gimp

# 安装后在终端启动
firefox &
```

### 注意事项

- **仅支持 X11 会话**：Wayland 桌面（GNOME Wayland、Plasma Wayland、sway、Hyprland）无法正常渲染
- **内存建议**：运行桌面环境至少分配 **1GB 以上 RAM**，否则会频繁交换到 ZRAM
- **性能预期**：TCG 软件模拟下 GUI 操作会有一定延迟，适合轻量使用

---

## 九、VM 内调用 Android 功能

PoDroid 内置了多个命令行工具，可在 VM 内直接操作 Android：

### 发送通知

```bash
# 基本用法
podroid-notify "构建完成！"

# 带标题和优先级
podroid-notify --title PoDroid --priority high "容器崩溃了"

# 更新同一通知（用 --id 复用）
podroid-notify --id 7 "进度 50%"
```

### 打开手机浏览器

```bash
podroid-open https://github.com/ExTV/Podroid
```

### 控制 VM

```bash
# 停止 VM
podroid-power stop

# 重启 VM
podroid-power restart

# 查看状态
podroid-power status
```

### 服务器模式（息屏运行）

```bash
# 开启服务器模式：屏幕全黑最低亮度，保持 VM 运行
podroid-server on

# 关闭服务器模式
podroid-server off

# 查看状态
podroid-server status
```

> 长按屏幕 3 秒可退出服务器模式。适合挂机跑脚本、跑服务。

---

## 十、开发环境配置

### 安装常用开发工具链

```bash
# 基础开发工具
apk add git nodejs npm python3 py3-pip go gcc musl-dev make

# 常用 CLI 工具
apk add curl jq rsync htop tmux vim ffmpeg yt-dlp
```

### 数据持久化

所有安装的软件、创建的文件、配置的服务都会保存在 ext4 持久化镜像中：

- `apk add` 安装的包 → 重启后仍在
- `rc-update add` 启用的服务 → 开机自动启动
- 容器镜像和数据 → 重启后完整保留

### 定时任务

```bash
# 编辑 crontab
echo "*/15 * * * * python3 /root/sync.py" | crontab -

# 启用并启动 cron 服务
rc-update add crond default && rc-service crond start
```

---

## 十一、备份与恢复

### 备份容器

在主页点击 **Backup** 按钮，应用会生成备份命令，复制到终端执行：

```bash
# 导出容器文件系统
podman export pihole -o /mnt/downloads/Podroid/backups/pihole.tar

# 保存镜像
podman save -o /mnt/downloads/Podroid/backups/myimage.tar myimage:latest
```

> 开启 Downloads 共享后，备份文件会出现在手机的 `Download/Podroid/backups/` 目录下。

---

## 十二、AVF 硬件加速（Pixel 设备专属）

### 支持设备

Pixel 8、Pixel 8a、Pixel 9、Pixel 9 Pro、Pixel 9 Pro XL、Pixel 10 系列（及其他厂商启用 pKVM 的设备）。

### 设置步骤

**第 1 步：确认设备支持**

```bash
adb shell pm list features | grep virtualization_framework
```

输出包含 `android.software.virtualization_framework` 即支持。

**第 2 步：授予权限**

```bash
adb shell pm grant com.excp.podroid android.permission.MANAGE_VIRTUAL_MACHINE
adb shell pm grant com.excp.podroid android.permission.USE_CUSTOM_VIRTUAL_MACHINE
```

> 没有电脑？可安装 Shizuku，通过无线调试激活后在 rish 中执行上述命令。

**第 3 步：运行诊断**

进入 **Settings → About → AVF (pKVM) diagnostic**，全部通过后将 Backend 设为 Auto 或 AVF。

### QEMU vs AVF 对比

| 特性 | QEMU (TCG) | AVF (pKVM) |
|------|-----------|------------|
| 设备要求 | 任意 ARM64 Android 8+ | 需支持 pKVM 的设备 |
| CPU 速度 | 软件模拟，慢 2~5 倍 | 接近原生 |
| 设置 | 零配置 | 需一次性授权 |
| USB 直通 | ✅ 支持 | ❌ 不支持 |
| 端口转发 | TCP + UDP | TCP + UDP |

---

## 十三、性能说明与优化

### TCG 软件模拟性能预期

- **IO 密集型任务**（Web 服务、数据库、脚本运行）：非常流畅
- **CPU 密集型任务**（编译、JVM 启动）：较慢，JVM 启动可能需 10~30 秒
- **长编译任务**（LLVM、Linux 内核、大型 Rust 项目）：非常慢，建议交叉编译后拷贝

### 优化建议

1. **增加内存**：分配 2GB+ RAM 可显著减少交换
2. **开启 AVF**：Pixel 设备切换到 AVF 后端，CPU 性能提升数倍
3. **使用 ARM64 镜像**：避免双重模拟
4. **选择轻量镜像**：alpine 版镜像体积小、启动快

---

## 十四、常见问题

### Q: 需要 Root 吗？需要刷机吗？

**完全不需要。** PoDroid 完全在用户空间运行，使用 QEMU TCG 软件模拟，任何原生 Android 8+ ARM64 设备都能直接安装使用。

### Q: 和 Termux 有什么区别？

Termux 运行在 Android 宿主内核上，该内核缺少容器所需的命名空间、cgroup 和 netfilter 支持。Proot 只是 chroot 模拟，无法真正运行 Docker 镜像。PoDroid 运行完整虚拟机和自定义内核，所有 OCI 镜像直接可用。

### Q: 后台运行时 VM 被杀了怎么办？

这是 Android 的幻影进程杀手导致的。解决方法：
1. 授予 PoDroid **无限制后台运行权限**
2. 在最近任务列表中锁定 PoDroid 应用
3. 关闭电池优化中对 PoDroid 的限制

### Q: 能挂载手机文件吗？

可以。在设置中开启 **Downloads folder sharing**，手机的 Downloads 文件夹会挂载到 VM 的 `/mnt/downloads`，双向同步。

### Q: 支持 USB 设备直通吗？

QEMU 后端支持。在设置中开启 USB passthrough 后，通过 OTG 接入的 USB 设备（无线网卡、存储、串口等）可直通到 VM 内。AVF 后端不支持。

### Q: 存储占用多大？

APK 约 200MB。首次启动时选择的 VM 磁盘大小是稀疏镜像，实际占用随安装内容增长，不会一次性占满。

---

## 十五、实用命令速查表

```bash
# ===== 容器操作 =====
podman run -d -p 8080:80 nginx          # 运行 Nginx
docker ps                                # 查看运行中的容器
docker images                            # 查看本地镜像
podman stop <容器名>                      # 停止容器

# ===== 服务管理 =====
rc-status                                # 查看服务状态
rc-update add docker default             # 开机自启 Docker
rc-service docker start                  # 启动 Docker

# ===== 网络相关 =====
podroid-forward list                     # 查看端口转发规则
podroid-forward add 8888 80 tcp          # 添加端口转发

# ===== 通知与控制 =====
podroid-notify "任务完成"                # 发送 Android 通知
podroid-power stop                       # 停止 VM
podroid-server on                        # 开启服务器模式

# ===== 包管理 =====
apk update && apk upgrade                # 升级系统
apk add <包名>                           # 安装软件
```

---

> **官方文档**：https://extv.github.io/Podroid/
> **GitHub 仓库**：https://github.com/ExTV/Podroid
