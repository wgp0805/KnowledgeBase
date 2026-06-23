在docker上执行命令
```
docker run -d --restart unless-stopped --name omnibox -p 7023:7023 -v D:/dockerDir/omnibox/data:/app/data lampon/omnibox:latest
```
然后访问
localhost:7023/admin 进入管理界面，在爬虫管理选择github导入链接
https://github.com/Silent1566/OmniBox-Spider
然后勾选自己喜欢的源就行了