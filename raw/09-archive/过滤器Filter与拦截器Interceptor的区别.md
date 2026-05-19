---
title: 过滤器Filter与拦截器Interceptor的区别
tags:
  - 过滤器
  - 拦截器
categories:
  - JAVA
date: 2024-11-25 15:44:28
---

## 结论

1. 底层原理不同：Filter 是 基于 函数回调 实现的； Interceptor 是基于 反射机制与动态代理 实现的。

2. 使用范围不同：Filter 是 Servlet规范 的接口，依赖web容器（Tomcat等），只能在web工程中使用；Interceptor 是 Spring的组件，不依赖web容器。

3. 触发时机不同：请求进入顺序： Tomcat ==> Filter ==> Servlet ==> Interceptor ==> Controller。

4. 拦截范围不同：Filter 对进入容器的所有请求进行拦截；Interceptor 只会对`Controller`中请求或访问`static`目录下的资源请求进行拦截。

5. 注入bean情况不同：Filter 中能正常注入其他bean; Interceptor 在 springcontext 之前加载，而 bean 由 Spring管理，所以注册 Interceptor 前需要先手动注入 Interceptor ；

6. 控制执行顺序不同：实际开发中，使用的通常是多个 Filter 或 Interceptor 组成的 链；Filter 中 拦截的核心方法是 doFilter(), Filter 直接按顺序执行；但是在 Interceptor 中存在 前置拦截方法 preHandle() 和 后置拦截方法 postHandle()，preHandle() 是顺序执行的，而 postHandle() 是反顺序执行的。

## Interceptor讲解

1. preHandle (HttpServletRequest request, HttpServletResponse response, Object handle) 方法，该方法将在请求处理之前进行调用。SpringMVC 中的Interceptor 是链式调用，在一个应用中或者说是在一个请求中可以同时存在多个Interceptor。每个Interceptor 的调用会依据它的声明顺序依次执行，而且最先执行的都是Interceptor 中的preHandle 方法，所以可以在这个方法中进行一些前置初始化操作或者是对当前请求的一个预处理，也可以在这个方法中进行一些判断来决定请求是否要继续进行下去。该方法的返回值是布尔值Boolean类型的，当它返回为false时，表示请求结束，后续的Interceptor和Controller都不会再执行；当返回值为true时就会继续调用下一个Interceptor的preHandle方法，如果已经是最后一个Interceptor的时候就会是调用当前请求的Controller方法。

2. postHandle (HttpServletRequest request, HttpServletResponse response, Object handle, ModelAndView modelAndView) 方法，由preHandle 方法的解释我们知道这个方法包括后面要说到的afterCompletion方法都只能是在当前所属的Interceptor的preHandle方法的返回值为true时才能被调用。postHandle方法，顾名思义就是在当前请求进行处理之后，也就是Controller方法调用之后执行，但是它会在DispatcherServlet进行视图返回渲染之前被调用，所以我们可以在这个方法中对Controller处理之后的ModelAndView对象进行操作。postHandle方法被调用的方向跟preHandle是相反的，也就是说先声明的Interceptor的postHandle方法反而会后执行。

3. afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handle, Exception ex) 方法，该方法也是需要当前对应的Interceptor 的preHandle 方法的返回值为true 时才会执行。顾名思义，该方法将在整个请求结束之后，也就是在DispatcherServlet 渲染了对应的视图之后执行。这个方法的主要作用是用于进行资源清理工作的。

## 执行顺序

### Interceptor

- preHandle() ：这个方法将在请求处理之前进行调用。注意：如果该方法的返回值为false ,将视为当前请求结束，不仅自身的拦截器会失效，还会导致其他的拦截器也不再执行。
- postHandle()：只有在 preHandle() 方法返回值为true 时才会执行。会在Controller 中的方法调用之后，DispatcherServlet 返回渲染视图之前被调用。 有意思的是：postHandle() 方法被调用的顺序跟 preHandle() 是相反的，先声明的拦截器 preHandle() 方法先执行，而postHandle()方法反而会后执行。
- afterCompletion()：只有在 preHandle() 方法返回值为true 时才会执行。在整个请求结束之后， DispatcherServlet 渲染了对应的视图之后执行。

### Filter

- init() ：该方法在容器启动初始化过滤器时被调用，它在 Filter 的整个生命周期只会被调用一次。注意：这个方法必须执行成功，否则过滤器会不起作用。
- doFilter() ：容器中的每一次请求都会调用该方法， FilterChain 用来调用下一个过滤器 Filter。
- destroy()： 当容器销毁 过滤器实例时调用该方法，一般在方法中销毁或关闭资源，在过滤器 Filter 的整个生命周期也只会被调用一次

## 代码示例

### Filter

```java
import javax.servlet.annotation.WebFilter;
import java.io.IOException;
//将Filter注入IOC容器中
@Component
@WebFilter(urlPatterns = "/*")
public class MyFilter implements Filter {

 	@Override 
    public void init(FilterConfig filterConfig) throws ServletException {
 		// Filter前置
    }

 	@Override 
     public void doFilter(ServletRequest servletRequest, ServletResponse servletResponse, FilterChain filterChain) throws IOException, ServletException {

 			// 调用后续过滤器或目标资源（这里就是放行，放行后response中才会有内容） 
         //Filter处理中
         filterChain.doFilter(servletRequest, servletResponse);

 
     }

 	@Override 
    public void destroy() {
 		//Filter后置
    }
}
```

### Interceptor

```java
@Component
public class PermissionInterceptor implements HandlerInterceptor {

	/**
	 * 执行方法前 
	 */
	@Override
	public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
		
		// if need login
		boolean needLogin = true;
        
        ...
            
		if (needLogin) {
			return false;
		}
		return true;
	}
    /**
	 * 执行方法后
	 */
	@Override
    public void postHandle(HttpServletRequest request, HttpServletResponse response, Object handler, @Nullable ModelAndView modelAndView) throws Exception {
        
        //业务代码
        
    }
	
    
    
    
    /**
	 * DispatcherServlet 渲染了对应的视图之后执行
	 */
	@Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, @Nullable Exception ex) throws Exception {
        
        //业务代码
        
    }
}

```

