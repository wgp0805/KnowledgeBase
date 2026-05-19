---
title: freemaker常用语法
tags:
  - freemaker
categories:
  - JAVA
date: 2022-05-28 18:59:42
---
在公司新接到一个模块的开发需求，当时睡页面用的freemaker，当时也是头顶一蒙啊，同事说和jstl的用法差不多，但是在常用的东西上的写法确实还是不会，所以在这总结些常用的语法！望指正！

```html
<!-- 此时name的值就是后台传过来的值直接填写就可以-->
<#if name = 0>
	<input type="text" name ="idCard">
</#if>
=================================================================
<!--接收参数采用${}的方式去接收-->
<!--这里的??表示可以为空-->
<input type="text" name ="idCard" value="${user??}">
=================================================================
<!--list就等同于for循环，userlist表示为后台传过来的集合，as 后的user表示遍历时的临时变量-->
<#list userlist as user>
        <ul class="u-list-box"> 
            <li class="u-list">
                <label for="">机主姓名:</label>
                <span>${user.userName}</span>
            </li>
        </ul>
  </#list>
=================================================================
<#list userlist as user>
        <ul class="u-list-box"> 
            <li class="u-list">
                <label for="">机主姓名:</label>
                <span>${user.userName}</span>
            </li>
        </ul>
  </#list>
  <!--这里的user——index是下标序号-->
  <#if user_index = 0>
  	checked="checked"
  </#if>
=================================================================
<!--遍历map-->
<#list map.keySet() as k>
    <option value="${k}">${map[k]}</option>
</#list>
=================================================================
<!--取LIST中第i个元素的值-->
${list[i]} 
<!--嵌套时前面要有括号，如下，将字符串变成list，然后取第i个元素的值-->
${(str?split(","))[i]} 
=================================================================
<!--list排序：-->
升序 .sort_by()
<#list list?sort_by("字段") as x>
</#list>
降序 .sort_by()?reverse
<#list list?sort_by("字段")?reverse as x> 
</#list>
=================================================================
<!--item_has_next,size使用：-->
<#list userList as user>
  <#if !user_has_next>
   共有${userList?size}最后一个用户是:${user.userName}
  </#if>
</#list>
```