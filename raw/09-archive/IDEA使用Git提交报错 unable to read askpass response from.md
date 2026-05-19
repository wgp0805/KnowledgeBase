---
title: IDEA使用Git提交报错 unable to read askpass response from
tags:
  - IDEA 
  - Git
categories:
  - Git
date: 2023-08-22 14:03:24·
---

```java
error: unable to read askpass response from 'C:\Users\xxxx\AppData\Local\JetBrains\IntelliJIdea2023.2\tmp\intellij-git-askpass-local.sh'
bash: /dev/tty: No such device or address
error: failed to execute prompt script (exit code 1)
```

报错

![image-20230822143842064](image-20230822143842064.png)



![image-20230822143904779](image-20230822143904779.png)然后我们需要在地址中间插上自己git的用户名和密码 还有@，格式为[userName]:[password]@

具体位置在http://后面，直接插入就可以了

```
url = https://[userName]:[password]@****************.git
```

这样就可以啦，可以正常拉取推送代码
