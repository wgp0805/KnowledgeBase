---
title: windows系统释放休眠文件和保留空间占用的硬盘空间
tags:
  - win
categories:
  - win
date: 2023-11-21 15:45:39
---

windows powershell 以管理员身份运行  释放  休眠文件

```
DISM.exe /Online /Set-ReservedStorageState /State:Disabled
```

cmd管理员身份运行    释放  保留空间  

```
powercfg -h off
```

