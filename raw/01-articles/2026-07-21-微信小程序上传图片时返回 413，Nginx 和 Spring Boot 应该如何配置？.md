---
title: "微信小程序上传图片时返回 413，Nginx 和 Spring Boot 应该如何配置？"
source: "SegmentFault"
url: "https://segmentfault.com/q/1010000048058934"
date: "2026-07-21T17:36:50+08:00"
score: 0.9
tags: ["中文", "编程", "问答", "技术"]
auto_captured: true
---

# 微信小程序上传图片时返回 413，Nginx 和 Spring Boot 应该如何配置？

> **来源**: SegmentFault  
> **链接**: https://segmentfault.com/q/1010000048058934  
> **抓取日期**: 2026-07-21  
> **相关性评分**: 0.9

最近在开发一个微信小程序的图片上传功能，小程序通过 `wx.uploadFile` 将图片上传到后端接口。

开发者工具中上传较小的图片可以成功，但在真机环境中上传体积较大的图片时，接口返回以下错误：
    
    
    413 Request Entity Too Large
    
    目前的项目环境如下：
    
    微信小程序原生开发
    Nginx 1.24
    Spring Boot 3
    Linux 服务器
    HTTPS 接口
    
    小程序端上传代码如下：
    
    wx.chooseMedia({
      count: 1,
      mediaType: ['image'],
      sourceType: ['album', 'camera'],
    
      success(res) {
        const filePath = res.tempFiles[0].tempFilePath
    
        wx.uploadFile({
          url: 'https://example.com/api/upload/image',
          filePath,
          name: 'file',
    
          success(uploadRes) {
            console.log('上传结果：', uploadRes)
          },
    
          fail(error) {
            console.error('上传失败：', error)
          }
        })
      }
    })
    
    Nginx 当前的接口代理配置如下：
    
    server {
        listen 443 ssl;
        server_name example.com;
    
        location /api/ {
            proxy_pass http://127.0.0.1:8080/;
    
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
    
    Spring Boot 接口代码如下：
    
    @RestController
    @RequestMapping("/upload")
    public class UploadController {
    
        @PostMapping("/image")
        public Map<String, Object> uploadImage(
                @RequestParam("file") MultipartFile file) {
    
            Map<String, Object> result = new HashMap<>();
            result.put("fileName", file.getOriginalFilename());
            result.put("fileSize", file.getSize());
    
            return result;
        }
    }
    
    目前观察到的情况是：
    
    1MB 左右的图片通常可以上传；
    体积较大的图片容易返回 413；
    请求还没有进入 Spring Boot 控制器；
    Nginx 日志中能够看到请求被拒绝；
    开发者工具和真机选择的图片体积可能不同。
    
    想确认以下几个问题：
    
    这个 413 错误是否主要由 Nginx 的请求体限制引起？
    除了 Nginx，Spring Boot 是否也需要设置上传文件大小？
    client_max_body_size 应该配置在 http、server 还是 location 中？
    修改配置后，应该如何确认新的限制已经生效？
    小程序端是否有必要在上传前压缩图片或者限制图片大小？
    
    期望实现的效果是：允许上传一定大小范围内的图片，超过限制时返回明确的 JSON 错误信息，而不是直接显示 Nginx 的 413 页面。
    

目前已经进行了以下排查和尝试。

### 1\. 检查请求是否进入后端

我在 Spring Boot 上传接口中增加了日志：
    
    
    @PostMapping("/image")
    public Map<String, Object> uploadImage(
            @RequestParam("file") MultipartFile file) {
    
        System.out.println("进入上传接口");
        System.out.println("文件大小：" + file.getSize());
    
        Map<String, Object> result = new HashMap<>();
        result.put("success", true);
    
        return result;
    }
    
    上传小图片时能够看到日志，上传大图片时没有输出，初步判断请求在进入 Spring Boot 之前就被拦截了。
    
    2. 修改 Nginx 请求体限制
    
    尝试在接口代理中增加：
    
    location /api/ {
        client_max_body_size 20m;
    
        proxy_pass http://127.0.0.1:8080/;
    
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    修改后执行了：
    
    sudo nginx -t
    sudo systemctl reload nginx
    
    nginx -t 提示配置语法正常，但不确定当前访问的虚拟主机是否真正使用了这份配置。
    
    3. 修改 Spring Boot 上传限制
    
    在 application.yml 中增加了：
    
    spring:
      servlet:
        multipart:
          max-file-size: 10MB
          max-request-size: 20MB
    
    修改后重新启动了 Spring Boot 服务。
    
    但由于大文件请求之前没有进入控制器，目前无法确定是 Nginx 配置未生效，还是还有其他位置存在大小限制。
    
    4. 检查 Nginx 日志
    
    在错误日志中看到了类似信息：
    
    client intended to send too large body
    
    因此怀疑主要问题仍然来自 Nginx。
    
    5. 尝试在小程序端压缩图片
    
    在选择图片后增加了压缩处理：
    
    wx.compressImage({
      src: filePath,
      quality: 70,
    
      success(compressRes) {
        wx.uploadFile({
          url: 'https://example.com/api/upload/image',
          filePath: compressRes.tempFilePath,
          name: 'file'
        })
      }
    })
    
    压缩后部分图片能够上传成功，但这只能减小文件体积，不能确认服务器端的正确配置方式。
    
    希望得到一个比较完整的处理建议，包括：
    
    Nginx 中上传大小限制的合适配置位置；
    Spring Boot 的文件大小配置；
    如何验证 Nginx 新配置是否已经生效；
    超出限制时如何返回统一的 JSON 错误；
    小程序上传前是否应该同时进行文件体积检查和图片压缩。
    
    ## 推荐标签
    

微信小程序  
Nginx  
Spring Boot  
文件上传


---
> 原文链接: https://segmentfault.com/q/1010000048058934