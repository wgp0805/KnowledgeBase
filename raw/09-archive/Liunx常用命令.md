---
title: Liunx常用命令
tags:
  - liunx
categories:
  - Liunx
date: 2022-05-29 11:10:53
---
# Liunx命令

### 目录说明

```
bin  (binaries)存放二进制可执行文件 
sbin  (super user binaries)存放二进制可执行文件，只有root才能访问 
etc (etcetera)存放系统配置文件 
usr  (unix shared resources)用于存放共享的系统资源 
home 存放用户文件的根目录 
root  超级用户目录 
dev (devices)用于存放设备文件 
lib  (library)存放跟文件系统中的程序运行所需要的共享库及内核模块 
mnt  (mount)系统管理员安装临时文件系统的安装点 
boot 存放用于系统引导时使用的各种文件 
tmp  (temporary)用于存放各种临时文件 
var  (variable)用于存放运行时需要改变数据的文件 

```

### 常用命令

```
ls : 查看当前文件夹下的目录
pwd: 查看当前所处的目录
ip addr ：ip地址 
cd: 进入文件夹
touch: 创建文件
mkdir: 创建文件夹
clear : 清屏   快捷键 Ctrl+L

command  [-options]  [parameter1] ：命令格式
ls /: 显示根目录文件
ls  -a : 显示全部文件
	-l ：显示文件列表
	-h ：显示文件大小
	-a -l -h
	-alh
xx --help: 查看帮助	
tab: 自动补全
cat : 查看文件内容
history： 历史命令
ls 2*/?/[x,x,x,x,x] : 通配符
ls >/>> xxx.txt : 重定向保存内容，>覆盖  >>追加
more xx.txt : 分页     空格:下一页 B:上一页
ls -alh / | more ：管道
cd.. : 返回上级目录
cd - : 后退
cd ~ ：家目录
tree : 查看目录结构树
mkdir A/B/C/D -p : 层级创建目录
rmdir 目录：删除目录（空）
rm 文件：删除文件
rm 目录 -r : 删除目录（任意）
ln -s 源文件 新文件： 软连接
ln 源文件 新文件 ： 硬链接
grep [-选项] ‘搜索内容串’ 文件名 ：搜索
mv 源文件 新文件：重命名
mv 源文件 目录/：移动文件

cp 源文件 目录/ -r：拷贝文件

which ${java} 查看程序安装目录


```

## 压缩命令

```
tar -cvf 压缩包名称.tar *.txt   : 打包*.txt
tar -xvf 压缩包名称.tar         : 解包*.txt

tar -zcvf 压缩包名称.tar.gz *.txt : 打包并压缩*.txt
tar -zxvf 压缩包名称.tar.gz       : 解包*.txt

tar -jcvf 压缩包名称.tar.bz2 *.txt : 打包*.txt
tar -jxvf 压缩包名称.tar.bz2 	   : 解包*.txt
```

### 用户权限

```
用户：
whoami ：查看当前用户
sudo useradd zhangsan -m : 添加账户
sudo passwd zhangsan  : 添加账户密码
su 账户: 切换用户
exit : 切换回之前的账户
sudo userdel -r zhangsan ：删除账户
sudo usermod zhangsan -a -G adm   ：添加sudo权限

sudo usermod zhangsan -a -G sudo  ：添加sudo权限

权限：
chmod u/g/o/a +/-/=rwx ：修改文件的权限（字母法）
chmod 777 11.txt ： 修改文件的权限（数字法）
```

### 防火墙

```
防火墙操作
启动：systemctl start firewalld
停止：systemctl stop firewalld
重启：systemctl restart firewalld.service
查看状态：systemctl status firewalld
开机启动：systemctl enable firewalld.service
开机禁用：systemctl disable firewalld
查看服务是否开机启动：systemctl is-enabled firewalld.service
查看已启动的服务列表：systemctl list-unit-files|grep enabled
查看启动失败的服务列表：systemctl --failed
查看版本：firewall-cmd --version
查看帮助：firewall-cmd --help
显示状态：firewall-cmd --state
查看所有打开的端口：firewall-cmd --zone=public --list-ports
更新防火墙规则：firewall-cmd --reload
查看区域信息:firewall-cmd --get-active-zones
查看指定接口所属区域：firewall-cmd --get-zone-of-interface=eth0
拒绝所有包：firewall-cmd --panic-on
取消拒绝状态：firewall-cmd --panic-off
查看是否拒绝：firewall-cmd --query-panic
开放80端口：firewall-cmd --zone=public --add-port=80/tcp --permanent （--permanent永久生效，没有此参数重启后失效）
查看80端口：firewall-cmd --zone=public --query-port=80/tcp
删除80端口：firewall-cmd --zone=public --remove-port=80/tcp --permanent
开放端口区间：firewall-cmd --permanent --zone=public --add-port=8080-9999/tcp //永久
重新载入使配置立即生效：firewall-cmd --reload
```

## date命令

```
//将服务器时间设置为2023年6月6日 17时06分06秒
date s "20230606 17：06：06"
//查看系统当前时间
date
```



## zookeeper

```java
服务管理命令：
zkServer.sh start|stop|restart|status

客户端连接：
zkCli.sh -server ${ip}:${port}

客户端关闭：
quit 或者按 Ctrl + C
```

