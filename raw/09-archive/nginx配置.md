---
title: nginx配置
tags:
  - nginx
categories:
  - nginx
date: 2024-07-02 09:56:10
---



#### 目录

- - [1. Nginx 配置的三种方式](https://cloud.tencent.com/developer?from_column=20421&from=20421)
  - [2. location配置](https://cloud.tencent.com/developer?from_column=20421&from=20421)
  - [3. 针对 location 截取代理路径的例子](https://cloud.tencent.com/developer?from_column=20421&from=20421)
  - [4. 普通代理的例子](https://cloud.tencent.com/developer?from_column=20421&from=20421)
  - [5. 配置前端的例子](https://cloud.tencent.com/developer?from_column=20421&from=20421)

### 1. Nginx 配置的三种方式

-  第一种直接替换 `location` 匹配部分 
-  第二种 `proxy_pass` 的目标地址，默认不带 `/`，表示只代理[域名](https://cloud.tencent.com/act/pro/domain-sales?from_column=20065&from=20065)，`url` 和参数部分不会变（把请求的 `path` 拼接到 `proxy_pass` 目标域名之后作为代理的URL） 
-  第三种 `proxy_pass` 的目标地址后增加 `/`，则表示把 `path` 中 `location` 匹配成功的部分剪切掉之后再拼接到 `proxy_pass` 目标地址 

第二种对应标题 **4. 普通代理的例子**

第三种对应标题 **3. 针对 location 截取代理路径的例子**

### 2. location配置

代码语言：javascript

复制

```javascript
location [ = | ~ | ~* | ^~ ] uri { 
   ...}
```

uri前面的方括号中的内容是可选项，解释如下：

`"="`：用于标准uri前，要求请求字符串与uri严格匹配，一旦匹配成功则停止

`"~"`：用于正则uri前，并且区分大小写

`"~*"`：用于正则uri前，但不区分大小写

`"^~"`：用于标准uri前，要求Nginx找到标识uri和请求字符串匹配度最高的location后，立即使用此location处理请求，而不再使用location块中的正则uri和请求字符串做匹配

### 3. 针对 location 截取代理路径的例子

例如下面的配置演示第三种配置方案，当我们访问 `http://44.179.118.54:80/shop/xxx` 的时候

访问的时候 Nginx 会把 `/shop/` 截取掉然后把后面的 `path` 拼接到 `proxy_pass` 上

那么我们实际访问的就是： `http://44.179.118.54:8007/xxx` 这个服务。

第二个访问 `http://44.179.118.54:8007/addrdata/xxx` 实际就是访问 `http://44.179.118.54:8007/xxx` 这个服务。

这两种配置方式达到的效果都是一致的。

**主要就是 `proxy_pass` 地址后面加 `/` 和不加 `/` 处理逻辑完全不一样。**

代码语言：javascript

复制

```javascript
 # shop-service
 # 反向代理shop-service服务
location ^~ /shop/ {
       proxy_pass  http://44.179.118.54:8007/;
       proxy_http_version 1.1;
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "upgrade";
       proxy_read_timeout 300s;

       proxy_redirect    off;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header Host $http_host;
       proxy_next_upstream http_502 http_504 error timeout invalid_header;
}

# 这里的效果和上面配置的效果一致
location ~ ^/addrdata/(.*) {
       proxy_pass  http://44.179.118.54:8007/$1$is_args$args;
       proxy_http_version 1.1;
       proxy_set_header Upgrade $http_upgrade;
       proxy_set_header Connection "upgrade";
       proxy_read_timeout 300s;

       proxy_redirect    off;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header Host $http_host;
       proxy_next_upstream http_502 http_504 error timeout invalid_header;
}
```

### 4. 普通代理的例子

这样我们访问 `http://19.11.11.70:8888/test-api/xxx` 实际就是访问 `http://19.11.11.71:8088/test-api/xxx`，就是帮 `19.11.11.71:8088` 端口做了一层代理

代码语言：javascript

复制

```javascript
server { 
   
    listen       8888;
    server_name  19.11.11.70;
    client_max_body_size     10240m; #修改成自己的想要设置的å44;13Hclient_body_timeout 6000s;
    client_header_timeout 600;
    client_body_buffer_size 128m;
    send_timeout 300s;
    keepalive_timeout 300s;

    location /test-api { 
   
        proxy_pass  http://19.11.11.71:8088/test-api;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_read_timeout 300s;

        proxy_redirect    off;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header Host $http_host;
        proxy_next_upstream http_502 http_504 error timeout invalid_header;
    }
}
```

### 5. 配置前端的例子

代码语言：javascript

复制

```javascript
# 根目录配置前端
# 前端放置目录 /home/java/nginx/cn_abd-app/abd-app
location / { 
   
    root /home/java/nginx/cn_abd-app/abd-app/;
    index index.html index.htm;
    try_files $uri $uri/ /index.html;
}

# 非根目录配置前端
# 前端放置目录 /home/java/nginx/cn_bbd-app/bbd-app
location /bbd-app { 
   
    root   /home/java/nginx/cn_bbd-app/;
    index  index.html index.htm;
    try_files $uri $uri/ /bbd-app/index.html;
}

# 非根目录配置二级路由前端
# 前端放置目录 /home/java/nginx/cn_bbd-app/app/bbd-app
location /app/bbd-app { 
   
    root   /home/java/nginx/cn_bbd-app/;
    index  index.html index.htm;
    try_files $uri $uri/ /app/bbd-app/index.html;
}

# 非根目录配置hash路由前端
# 前端放置目录 /home/java/nginx/cn_bbd-app/share 
location /share { 
   
    root /home/java/nginx/cn_bbd-app/;
    index index.html index.htm;
 }
```

全栈程序员栈长，转载请注明出处：https://javaforall.cn/180278.html原文链接：https://javaforall.cn







# 以上的使用就够用了下面是详细的讲解

语法规则

location [=|~|~*|^~] /uri/ { … }

前缀匹配时，Nginx 不对 url 做编码，因此请求为 /static/20%/aa ，可以被规则 ^~ /static/ /aa 匹配到（注意是空格）

匹配成功后，url的 域名+port 替换为root指定的目录，

以请求https://www.cnblogs.com:8080/benwu/articles/2283622.html为例，
1: location配置如下

```
location /benwu {
　　root /home/files/;
}
```

匹配到/benwu，url中的域名+port替换为root指定的目录，即将请求地址中的https://www.cnblogs.com:8080被替换为了/home/files/，
所以在服务器端实际访问的路径是：/home/files/benwu/articles/2283622.html

2: location配置如下

```
location /benwu/articles {
　　root /home/files/;
}
```

匹配到 /benwu/articles，url的域名+port替换为root指定的目录，即url中的https://www.cnblogs.com:8080被替换为了/home/files，
所以实际访问的路径仍然是：/home/files/benwu/articles/2283622.html。
root在替换时不会替换匹配到的路径。

 

多个 location 配置的情况下匹配顺序为

首先精确匹配 = ，如果匹配成功，则停止其他匹配
其次前缀匹配 ^~
其次是按文件中顺序的正则匹配
然后匹配不带任何修饰的前缀匹配。
最后是交给 / 通用匹配
当有匹配成功时候，停止匹配，按当前匹配规则处理请

location匹配顺序
"="前缀指令匹配，如果匹配成功，则停止其他匹配
普通字符串指令匹配，顺序是从长到短，匹配成功的location如果使用^~，则停止其他匹配（正则匹配）
正则表达式指令匹配，按照配置文件里的顺序，成功就停止其他匹配
如果第三步中有匹配成功，则使用该结果，否则使用第二步结果
最后是交给 / 通用匹配

注意点
匹配的顺序是先匹配普通字符串，然后再匹配正则表达式。另外普通字符串匹配顺序是根据配置中字符长度从长到短，也就是说使用普通字符串配置的location顺序是无关紧要的，反正最后nginx会根据配置的长短来进行匹配，但是需要注意的是正则表达式按照配置文件里的顺序测试。找到第一个比配的正则表达式将停止搜索。

一般情况下，匹配成功了普通字符串location后还会进行正则表达式location匹配。有两种方法改变这种行为，其一就是使用“=”前缀，这时执行的是严格匹配，并且匹配成功后立即停止其他匹配，同时处理这个请求；另外一种就是使用“^~”前缀，如果把这个前缀用于一个常规字符串那么告诉nginx 如果路径匹配那么不测试正则表达式。

匹配模式及顺序

= 　　 #用于标准uri前，需要请求字串与uri完全匹配，如果匹配成功就停止向下匹配并立即处理请求。
~ 　　 #区分大小写
~* 　　 #不区分大写
!~ 　　 #区分大小写不匹配
!~* 　　#不区分大小写不匹配
^ 　　 #匹配正则开头
$ 　　 #匹配正则结尾
\ 　　 #转义字符。可以转. * ?等
\* 　　 #代表任意长度的任意字符

location = /uri　　　　 #开头表示精确匹配，只有完全匹配上才能生效。
location ^~ /uri　　　　#开头对URL路径进行前缀匹配，并且在正则之前。
location ~ pattern     #开头表示区分大小写的正则匹配。
location ~* pattern    #开头表示不区分大小写的正则匹配。
location /uri 　　     #不带任何修饰符，也表示前缀匹配，但是在正则匹配之后。
location /            #通用匹配，任何未匹配到其它location的请求都会匹配到，相当于switch中的default。



```
#不区分大小写匹配任何以gif、jpg、jpeg结尾的请求
location ~* .(gif|jpg|jpeg)$ ｛  
     
｝

#区分大小写匹配以.txt结尾的请求，并设置此location的路径是/usr/local/nginx/html/。也就是以.txt结尾的请求将访问/usr/local/nginx/html/ 路径下的txt文件
location ~ ^.+\.txt$ {
    root /usr/local/nginx/html/;
}

# ^~ 以 /admin/ 开头的请求，都会匹配上
location ^~ /admin/ {
   root /xvdb/mobai/
}

此时 /xvdb/mobai/目录中必须要有 admin 文件夹

#匹配成功: http://www.cnblogs.com/admin/index.jsp
#匹配成功: http://www.cnblogs.com/admin/login.jsp

#忽略大小写,包含/Images/
location ~* /Images/ {
}
#匹配成功: http://www.cnblogs.com/test/Images/     
#匹配成功: http://www.cnblogs.com/images/    


#不加任何规则则时，默认是大小写敏感，前缀匹配，相当于加了“^”与“~”
location /index/ {
}
#匹配成功: http://www.cnblogs.com/index
#匹配成功: http://www.cnblogs.com/index/index.html
#匹配失败: http://www.cnblogs.com/test/index
#匹配失败: http://www.cnblogs.com/Index

 
#精确匹配, 只匹配http://www.cnblogs.com
location = / {
}
#匹配成功: http://www.cnblogs.com 
#匹配失败: http://www.cnblogs.com/index

# 匹配到所有url
location / {

}
```



例子，有如下匹配规则：



```
location = / {
  echo "规则A";
}
location = /login {
  echo "规则B";
}
location^~ /static/ {
  echo "规则C";
}
location^~ /static/files {
  echo "规则X";
}
location ~ \.(gif|jpg|png|js|css)$ {
  echo "规则D";
}
location ~* \.png$ {
  echo "规则E";
}
location /img {
  echo "规则Y";
}
location / {
  echo "规则F";
}
```



那么产生的效果如下：

访问根目录 / ，比如 http://localhost/ 将匹配 规则A
访问 http://localhost/login 将匹配 规则B ， http://localhost/register 则匹配 规则F
访问 http://localhost/static/a.html 将匹配 规则C
访问 http://localhost/static/files/a.exe 将匹配 规则X ，虽然 规则C 也能匹配到，但因为最大匹配原则，最终选中了 规则X 。你可以测试下，去掉规则 X ，则当前 URL 会匹配上 规则C 。
访问 http://localhost/a.gif , http://localhost/b.jpg 将匹配 规则D 和 规则 E ，但是 规则 D 顺序优先， 规则 E 不起作用，而 http://localhost/static/c.png 则优先匹配到 规则 C
访问 http://localhost/a.PNG 则匹配 规则 E ，而不会匹配 规则 D ，因为 规则 E 不区分大小写。
访问 http://localhost/img/a.gif 会匹配上 规则D ,虽然 规则Y 也可以匹配上，但是因为正则匹配优先，而忽略了 规则Y 。
访问 http://localhost/img/a.tiff 会匹配上 规则Y 。
访问 http://localhost/category/id/1111 则最终匹配到规则 F ，因为以上规则都不匹配，这个时候应该是 Nginx 转发请求给后端应用服务器，比如 FastCGI（php），tomcat（jsp），Nginx 作为反向代理服务器存在。

 

# 详解nginx的root与alias 

以请求https://www.cnblogs.com:8080/benwu/articles/2283622.html为例，
测试1: location配置如下

```
location /benwu {
　　root /home/files/;
}
```

匹配到/benwu，将url中的 前缀(ip/域名)+port+匹配到的路径 替换为alias指定的目录，
即url中的https://www.cnblogs.com:8080/benwu 被替换为了/home/files/，所以实际访问的路径为/home/files/articles/2283622.html

测试2: location配置如下

```
location /benwu/articles {
　　root /home/files/;
}
```

匹配到/home/files，将url中的 前缀(ip/域名)+port+匹配到的路径 替换为alias指定的目录，
即url中的https://www.cnblogs.com:8080/benwu 被替换为了/home/files/，所以实际访问的路径为/home/files/2283622.html
alias在替换时会替换匹配到的路径。

alias其余特性，最左匹配、index、location解析url工作流程、末尾’/'与root一致。

 

所以实际使用中，笔者觉得至少有三个匹配规则定义，如下：

\# 直接匹配网站根，通过域名访问网站首页比较频繁，使用这个会加速处理，官网如是说。
\# 这里是直接转发给后端应用服务器了，也可以是一个静态首页
\# 第一个必选规则 

```
location = / {
  proxy_pass http://tomcat:8080/index
}
```

\# 第二个必选规则是处理静态文件请求，这是 nginx 作为 http 服务器的强项
\# 有两种配置模式，目录匹配或后缀匹配，任选其一或搭配使用 



```
location ^~ /static/ {
  root /webroot/static/;
}
location ~* \.(gif|jpg|jpeg|png|css|js|ico)$ {
  root /webroot/res/;
}
```



\# 第三个规则就是通用规则，用来转发动态请求到后端应用服务器
\# 非静态文件请求就默认是动态请求，自己根据实际把握
\# 毕竟目前的一些框架的流行，带.php、.jsp后缀的情况很少了 

```
location / {
  proxy_pass http://tomcat:8080/
}
```


rewrite 语法

last – 基本上都用这个 Flag
break – 中止 Rewirte，不再继续匹配
redirect – 返回临时重定向的 HTTP 状态 302
permanent – 返回永久重定向的 HTTP 状态 301


1、下面是可以用来判断的表达式：

-f 和 !-f 　　用来判断是否存在文件
-d 和 !-d 　　用来判断是否存在目录
-e 和 !-e 　　用来判断是否存在文件或目录
-x 和 !-x 　　用来判断文件是否可执行


2、下面是可以用作判断的全局变量

例：



```
http://localhost:88/test1/test2/test.php?k=v
$host：localhost
$server_port：88
$request_uri：/test1/test2/test.php?k=v
$document_uri：/test1/test2/test.php
$document_root：D:\nginx/html
$request_filename：D:\nginx/html/test1/test2/test.php
```



redirect 语法



```
server {
  listen 80;
  server_name start.igrow.cn;
  index index.html index.php;
  root html;
  if ($http_host !~ "^star\.igrow\.cn$") {
    rewrite ^(.*) http://star.igrow.cn$1 redirect;
  }
} 
```



防盗链 



```
location ~* \.(gif|jpg|swf)$ {
  valid_referers none blocked start.igrow.cn sta.igrow.cn;
  if ($invalid_referer) {
    rewrite ^/ http://$host/logo.png;
  }
}
```



根据文件类型设置过期时间 



```
location ~* \.(js|css|jpg|jpeg|gif|png|swf)$ {
  if (-f $request_filename) {
    expires 1h;
    break;
  }
}
```



 
