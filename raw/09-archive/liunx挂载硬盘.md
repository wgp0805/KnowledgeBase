---
title: liunx挂载硬盘
tags:
  - liunx
categories:
  - liunx
date: 2023-07-07 15:42:50
---

我要挂载的硬盘为`sdb`，首先将硬盘插上。

# **1 查看硬盘**

使用检测硬盘命令：

```
lsblk
```

看到 `sdb` 存在,并且没有进行挂载

![image-20230707154343897](image-20230707154343897.png)

可以使用命令查询硬盘的实际位置

```shell
fdisk -l
```

![image-20230707154513737](image-20230707154513737.png)

然后使用查看硬盘命令：

```
df -h
```

如果只是插上硬盘而无其他操作，则看不到要挂载的硬盘`sdb`。

# 2 挂载

格式化硬盘 `sdb` ：

```
mkfs -t ext4 /dev/sdb
```

如果不格式化可能会报错

![image-20230707154621497](image-20230707154621497.png)

导致挂载失败

创建挂载目录 `data`：

```
mkdir /data
```

把空间挂在 `/data` ：

```
mount /dev/sdb /data
```

再次使用 `df -h` 可以看到硬盘已存在：

![image-20230707154657924](image-20230707154657924.png)

# 3 添加信息

将以下信息添加到 `/etc/fstab` 中

```
/dev/sdb   /data   ext4   defaults    0    0
```

若无法添加，则需要修改文件权限。（这步不是必须要执行的，可以忽略）

立即执行 `fstab` 的内容：

```
mount -a
```

不报错则挂载成功。

# **4 修改权限**

如访问硬盘 `sdb`出现报错：

> permission denied

同样修改 `sdb`的权限即可：

```
chmod 777 /media/sdb
```

# **5 解除挂载**

若需要解除挂载：

```
umount /dev/sdb
```

# **6 解除挂载**

若只是把硬盘`sdb`插上，开机时可能会自动挂载硬盘，但是这样硬盘无法使用，需要先解除挂载：

```
umount /dev/sdb
```

重新挂载到`data`目录：

```
mount /dev/sdb /data
```
