---
title: "面试官：你掌握哪些 Linux 常用命令？"
source: "https://mp.weixin.qq.com/s/AC2LR_N4BiFWDlIOU8jdog"
---
犬小哈 小哈学Java *2026年8月27日 09:00*

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E4%BD%A0%E6%8E%8C%E6%8F%A1%E5%93%AA%E4%BA%9B%20Linux%20%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%9F/be3dc3f3c15aa988193e523b8466bbfe_MD5.webp)

**在线 Java 面试刷题（已更新334题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

## 面试考察点

1. **实际开发经验** ：面试官想看你是否真的在 Linux 环境下写过代码、部署过服务、排查过线上问题。一开口就是 `ls` 、 `cd` 、 `pwd` 三件套，基本就是学生党；一开口就是 `tail -f` 、 `grep -A 20` 、 `jstack` 、 `netstat -anp` ，那是有过实战的老哥。
2. **问题排查能力** ：服务上线后 CPU 飙高、内存泄漏、磁盘打满、端口冲突，这些场景你能用哪些命令快速定位？这才是面试官真正关心的。
3. **知识面广度** ：除了基础命令，是否掌握文本处理三剑客（ `grep` / `awk` / `sed` ）、性能监控工具、Java 诊断工具，这些直接体现你的技术深度。

## 核心答案

我把日常开发常用的命令按场景分了类，这样记起来更有条理。

![Linux 常用命令按场景排查示意图](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E4%BD%A0%E6%8E%8C%E6%8F%A1%E5%93%AA%E4%BA%9B%20Linux%20%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%9F/396f81b12b6c5a862f2736aa15d76759_MD5.webp)

Linux 常用命令按场景排查示意图

### 一、文件与目录操作（日常高频）

| 命令 | 作用 | 常用示例 |
| --- | --- | --- |
| `ls` | 列出目录内容 | `ls -lh`  （人类可读大小）、 `ls -lt` （按时间排序） |
| `cd` | 切换目录 | `cd -`  回到上次目录、 `cd ~` 回家目录 |
| `pwd` | 显示当前路径 | `pwd` |
| `cp` | 复制 | `cp -r dir1 dir2`  （递归复制目录） |
| `mv` | 移动/重命名 | `mv              old.txt                         new.txt           ` |
| `rm` | 删除 | `rm -rf dir`  （ **慎用！生产环境别瞎敲** ） |
| `mkdir` | 创建目录 | `mkdir -p a/b/c`  （递归创建） |
| `find` | 查找文件 | `find / -name "*.log" -mtime +7` |
| `tree` | 树状显示目录 | `tree -L 2`  （只显示 2 层） |

### 二、文件查看与编辑（看日志必备）

| 命令 | 作用 | 常用示例 |
| --- | --- | --- |
| `cat` | 查看整个文件 | `cat file` |
| `less` | 分页查看 | `less +F file`  （类似 `tail -f` ，还能往上翻） |
| `head`  / `tail` | 看头/尾 | `tail -f              app.log           `  、 `tail -n 100              app.log           ` 、 `head -n 50 file` |
| `echo` | 输出 | `echo $JAVA_HOME` |
| `vi`  / `vim` | 编辑 | 生产排查日志时偶尔要改配置 |

> “
> 
> 看日志我最常用的就是 `tail -f              xxx.log           ` ，配合 `grep` 过滤关键信息，下面会讲。

### 三、文本处理三剑客（排查神器）

这三个命令是 Java 程序员排查问题的核武器，必须掌握。

#### 1\. grep —— 文本搜索

```
# 在日志里搜关键词，显示匹配行的后 20 行（排查异常堆栈特别有用）
grep -A 20 "NullPointerException" 
            app.log
          

# 递归搜索某个目录下所有 java 文件中的关键字
grep -rn "public class" --include="*.java" .

# 反向匹配 + 忽略大小写
grep -vi "debug" 
            app.log
          

# 统计匹配行数
grep -c "ERROR" 
            app.log
```

#### 2\. awk —— 文本分析

```
# 查看 CPU 使用率前 5 的进程
ps aux | sort -rnk 3 | head -5

# 统计每个 IP 出现的次数（分析访问日志）
awk '{print $1}' 
            access.log
           | sort | uniq -c | sort -rn | head

# 按 ":" 分隔，打印第 1 列和第 3 列（比如分析 /etc/passwd）
awk -F':' '{print $1, $3}' /etc/passwd
```

#### 3\. sed —— 文本替换

```
# 把文件里的 "old" 替换成 "new"（原地修改）
sed -i 's/old/new/g' 
            file.txt
          

# 只显示第 10 到 20 行
sed -n '10,20p' 
            file.txt
          

# 删除空行
sed '/^$/d' 
            file.txt
```

### 四、进程与端口管理（线上排查必备）

这块是 **Java 程序员面试的核心得分区** ，线上服务有问题，基本都从这里开始查。

![Linux 线上问题排查流程图](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E4%BD%A0%E6%8E%8C%E6%8F%A1%E5%93%AA%E4%BA%9B%20Linux%20%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%9F/ec734d976b994106970b5640b05cfee5_MD5.jpg)

Linux 线上问题排查流程图

上图是线上问题排查的典型路径，下面把对应的命令展开讲。

```
# 1. 查看系统资源占用（CPU、内存）
top                          # 实时查看，按 1 看各 CPU 核心
htop                         # 更友好的版本（需要安装）

# 2. 查看进程
ps aux | grep java           # 找 Java 进程
ps -ef | grep java           # 另一种写法
jps                          # 专门看 Java 进程（JDK 自带）

# 3. 查看端口占用（部署服务时报 "端口被占用" 必用）
netstat -anp | grep 8080     # 看 8080 端口被谁占了
netstat -tunlp               # 查看所有监听端口（推荐）
ss -tunlp                    # 新一代工具，比 netstat 快
lsof -i:8080                 # 看哪个进程占用了 8080

# 4. 杀进程
kill -9 12345                # 强杀 PID 为 12345 的进程
killall java                 # 按名字杀（**慎用**）

# 5. 后台运行
nohup java -jar 
            app.jar
           > /dev/null 2>&1 &
```

### 五、Java 诊断工具（JDK 自带，加分项）

这块很多候选人答不上来，说出来就是加分项。

| 工具 | 作用 | 典型场景 |
| --- | --- | --- |
| `jps` | 列出 Java 进程 | 类似 `ps` ，但只看 Java |
| `jstack` | 打印线程堆栈 | CPU 飙高、死锁排查 |
| `jmap` | 打印内存快照 | OOM 分析、内存泄漏 |
| `jstat` | 查看 GC 情况 | 监控 GC 频率 |
| `jinfo` | 查看/修改 JVM 参数 | 线上动态调整参数 |
| `jhat` | 分析 heap dump | 配合 `jmap` 使用 |
| `arthas` | 阿里开源诊断工具 | **强烈推荐！线上排查神器** |

举个 CPU 飙高的排查流程：

```
# 1. 用 top 找到 CPU 飙高的 Java 进程 PID
top

# 2. 用 top -Hp 看哪个线程飙高（把 PID 转成十六进制）
top -Hp 12345

# 3. 用 jstack 打印堆栈，grep 那个十六进制线程 ID
printf "%x\n" 12367       # 十进制转十六进制（比如得到 304f）
jstack 12345 | grep -A 30 "304f"
```

这一套流程面试官特别爱听，能答出来基本就稳了。

### 六、系统性能监控

```
# 内存
free -h                     # 查看内存使用（人类可读）

# 磁盘
df -h                       # 查看磁盘使用情况
du -sh /var/log             # 查看某目录大小
du -sh *                    # 查看当前目录所有文件夹大小

# 系统负载
uptime                      # 看系统负载（1/5/15 分钟）

# IO 性能
iostat -x 1                 # 每秒查看磁盘 IO（1 表示间隔 1 秒）

# 虚拟内存统计
vmstat 1                    # 每秒看一次，关注 r（运行队列）、si/so（swap）

# 查看内核日志
dmesg | tail -50
```

### 七、网络相关

```
# 测试网络连通性
ping 
            www.baidu.com
          

# 测试端口连通性（服务连不上必用）
telnet 192.168.1.100 8080

# 请求接口
curl http://localhost:8080/api/user
curl -X POST -H "Content-Type: application/json" -d '{"name":"tom"}' http://localhost:8080/api/user

# 下载文件
wget 
            https://example.com/file.tar.gz
          

# 查看 DNS 解析
nslookup 
            www.baidu.com
          

# 查看本机网卡
ifconfig                    # 老命令
ip addr                     # 新命令
```

### 八、权限与用户

```
# 修改权限
chmod 755 
            script.sh
                   # rwxr-xr-x
chmod +x 
            deploy.sh
                    # 加执行权限

# 修改文件所有者
chown user:group file

# 切换用户
su - deploy                 # 切换到 deploy 用户
sudo command                # 以 root 权限执行
```

### 九、压缩解压

```
# tar 包（最常用）
tar -zcvf 
            app.tar.gz
           app/   # 压缩
tar -zxvf 
            app.tar.gz
                  # 解压
tar -zxvf 
            app.tar.gz
           -C /opt  # 解压到指定目录

# zip
zip -r 
            app.zip
           app/
unzip 
            app.zip
```

### 十、其他高频命令

```
# 服务管理（CentOS 7+）
systemctl status nginx
systemctl start nginx
systemctl enable nginx      # 设置开机自启

# 定时任务
crontab -e                  # 编辑定时任务
crontab -l                  # 查看定时任务
# 示例：每天凌晨 2 点备份
0 2 * * * /home/
            backup.sh
          

# 历史命令
history | grep "mysql"

# 查看时间
date
date +"%Y-%m-%d %H:%M:%S"

# 管道与重定向（组合使用威力巨大）
cat 
            app.log
           | grep "ERROR" | wc -l
echo "hello" > 
            file.txt
               # 覆盖
echo "hello" >> 
            file.txt
              # 追加
command > /dev/null 2>&1    # 丢弃所有输出
```

## 面试高频追问

1. **追问一：线上 CPU 飙高怎么排查？**
- 答题套路： `top` 找进程 → `top -Hp` 找线程 → `jstack` 看堆栈 → 定位代码。这是标准答案，要能完整说出来。
3. **追问二：怎么查看某个端口的占用情况？**
- 三种方式： `netstat -anp | grep 端口` 、 `lsof -i:端口` 、 `ss -tunlp | grep 端口` 。答出两种以上加分。
5. **追问三： `grep` 、 `awk` 、 `sed` 有什么区别？**
- `grep` ：文本搜索（找）
	- `awk` ：文本分析（按列处理）
	- `sed` ：文本编辑（改）
7. **追问四： `rm -rf` 误删了怎么办？**
- 有备份走备份（ `extundelete` 工具有时能恢复 ext4 文件系统的删除文件），但绝大多数情况下 **恢复不了** 。生产环境 **禁用** `rm -rf /` ，推荐用 `mv` 到 `/tmp` 替代删除，或者用 `trash-cli` 这类工具。
9. **追问五： `kill -9` 和 `kill -15` 有什么区别？**
- `kill -15` （SIGTERM）是优雅终止，给应用收尾的机会（执行 hook、释放资源）。
	- `kill -9` （SIGKILL）是强杀，进程立即终止，可能丢数据。
	- \*\*Java 应用优先用 `kill -15` \*\*，让 Spring 等框架走优雅关闭流程。

## 常见面试变体

- "你平时在 Linux 下主要用哪些命令排查问题？"
- "如何用 Linux 命令定位线上 Java 进程 CPU 100%？"
- " `grep` 、 `awk` 、 `sed` 各自的使用场景？"
- "说说你常用的性能监控命令"

## 记忆口诀

**按场景记忆** ：

- 看 **日志** ： `tail -f` + `grep`
- 看 **进程** ： `ps aux` + `top`
- 看 **端口** ： `netstat` + `lsof`
- 看 **磁盘** ： `df -h` + `du -sh`
- 看 **内存** ： `free -h` + `top`
- 排 **Java 问题** ： `jps` + `jstack` + `jmap`

## 总结

答这道题别傻乎乎地从 `ls` 开始背， **按场景分类答** 才显专业。重点突出你在线上排查问题时的实战经验—— `top` → `jstack` → `grep` 这套组合拳，能直接把你的技术深度打在面试官脸上。再提一句 `arthas` 这种现代化诊断工具，加分不少。

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/%E9%9D%A2%E8%AF%95%E5%AE%98%EF%BC%9A%E4%BD%A0%E6%8E%8C%E6%8F%A1%E5%93%AA%E4%BA%9B%20Linux%20%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%EF%BC%9F/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 拼多多二面：为什么要使用 ElasticSearch？和传统关系数据库 MySQL 有什么不同？3. 终于找到一个好用的 Nginx 日志分析工具了4. 面试官：什么是时间片？
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

Java 面试题 | 八股文汇总 · 目录

阅读原文