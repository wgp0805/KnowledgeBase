---
title: "一个 Token 就够了，JWT 续签为什么要搞 Access Token + Refresh Token 双 Token？"
source: "https://mp.weixin.qq.com/s/ckMV60RxAZnL91P1ILAAqQ"
---
胖虎 Java专栏 *2026年6月29日 12:20*

很多后端同学第一次做 JWT 登录，脑子里都会冒出一个很自然的问题。

登录成功发一个 JWT。前端每次请求带上。后端验签、校验过期时间、放行。

这不是挺好吗？

那为什么很多系统还要搞 Access Token 和 Refresh Token 两个 Token？

看起来像是把简单问题复杂化了。

说实话，如果只是做一个内部小后台，一个 Token 真的够用。用户少，风险低，过期了重新登录也不是什么天大的事。

但只要你的系统开始面向大量用户，尤其是 App、SaaS、开放平台这类产品，单 Token 很快就会撞上一堵墙。

这堵墙叫，过期时间怎么设。

![图片](assets/%E4%B8%80%E4%B8%AA%20Token%20%E5%B0%B1%E5%A4%9F%E4%BA%86%EF%BC%8CJWT%20%E7%BB%AD%E7%AD%BE%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E6%90%9E%20Access%20Token%20+%20Refresh%20Token%20%E5%8F%8C%20Token%EF%BC%9F/685814ef08ef1e9a53f228cc3935e0f1_MD5.webp)

一个 Token 如果要拿来访问业务接口，就必须有有效期。

设短一点，比如 15 分钟、30 分钟，安全性确实好一些。Token 真泄露了，攻击者能用的时间也有限。

问题是用户体验会变差。

你可以想象一个很常见的场景，用户在页面上填了半天表单，点提交的时候后端返回 401，前端跳登录页。

这不是安全设计。

这是制造血压。

那把时间设长一点呢，比如 7 天、30 天？

体验确实好了。用户几乎不会被打断。

但风险也跟着上来了。这个 JWT 一旦被偷，攻击者就可以在有效期内一直拿它访问接口。

更麻烦的是，JWT 最大的卖点之一是无状态。服务端不存 Session，每次只靠签名和过期时间判断它是不是有效。

这也带来一个副作用，服务端很难主动让一个已经签发出去的 JWT 失效。

当然，你可以加黑名单。

比如用户退出登录时，把这个 JWT 的 jti 放进 Redis 黑名单里。每次请求都查一遍黑名单，只要命中就拒绝。

能不能做？

能。

但你要想清楚，JWT 原本省掉的那次服务端状态查询，又被你加回来了。最后看起来像 JWT，跑起来像 Session，只是换了个名字。

单 Token 的根本矛盾就在这里。

短了，用户难受。

长了，安全难受。

加黑名单，架构又开始变重。

双 Token 不是为了炫技，它就是专门来拆这个矛盾的。

## 两个 Token，干两件完全不同的事

双 Token 里最重要的一点，不是「有两个字符串」。

而是职责分开。

Access Token 负责访问业务接口。

Refresh Token 负责换新的 Access Token。

这两句话一定要分清楚。

Access Token 的生命周期应该很短，常见是 10 到 30 分钟。前端请求业务接口时带它，后端验签后放行。

Refresh Token 的生命周期更长，常见是 7 天、14 天、30 天。它不应该拿去访问任何业务接口，只能调用刷新接口。

这就把问题拆开了。

高频传输、暴露面大的 Access Token，有效期做短。

低频使用、只出现在刷新接口里的 Refresh Token，有效期做长。

用户感知上，只要 Refresh Token 还没过期，前端就能在 Access Token 过期后自动换一个新的。用户不需要频繁登录。

安全上，业务接口里到处跑的是短命 Token。就算被截获，窗口也比较小。

![图片](assets/%E4%B8%80%E4%B8%AA%20Token%20%E5%B0%B1%E5%A4%9F%E4%BA%86%EF%BC%8CJWT%20%E7%BB%AD%E7%AD%BE%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E6%90%9E%20Access%20Token%20+%20Refresh%20Token%20%E5%8F%8C%20Token%EF%BC%9F/97b00e8ec9040d312d45d6a1de61a828_MD5.jpg)

这里有个细节很多人会忽略。

Refresh Token 不一定要是 JWT。

甚至在大多数业务系统里，我更倾向于把 Refresh Token 做成随机字符串，然后把它存在服务端。

比如用一段安全随机数生成 refresh\_token，服务端把它的 hash 存进 Redis，关联 userId、设备信息、过期时间。

用户退出登录，就删掉这条记录。

发现风险设备，就删掉对应设备的 Refresh Token。

用户改密码，直接让这个用户所有 Refresh Token 失效。

这才是 Refresh Token 真正值钱的地方。

它给了服务端一个「可撤销的登录态」。

如果 Refresh Token 也做成完全无状态的 JWT，而且服务端什么都不存，那它只是一个更长寿的 JWT。单 Token 遇到的「无法主动失效」问题，又回到原点了。

## 一次正常登录和续签，大概是这样走的

先看登录。

用户输入账号密码，后端校验通过后，下发两样东西。

一个短期 Access Token。

一个长期 Refresh Token。

如果是 Web 项目，常见做法是 Access Token 放在内存里，Refresh Token 放在 HttpOnly、Secure、SameSite 合理配置的 Cookie 里。这样 JavaScript 读不到 Refresh Token，XSS 直接偷走它的概率会低很多。

但这里也别只看 XSS。

Refresh Token 如果走 Cookie，刷新接口也要按 Cookie 认证的方式防 CSRF。SameSite 是一层保护，不是免死金牌。严谨一点的系统，还会校验 Origin / Referer，或者配合 CSRF Token。

如果是移动端 App，就要放到系统提供的安全存储里，比如 iOS Keychain、Android Keystore 这类地方。不要随手塞普通本地文件。

再看业务请求。

前端访问接口时带 Access Token。后端验签，没过期就继续处理。

Access Token 过期后，业务接口返回 401。前端拦截到 401，拿 Refresh Token 去调用刷新接口。

刷新接口做几件事。

校验 Refresh Token 是否存在。

校验是否过期。

校验设备、客户端、IP 风险，至少做一些基础判断。

通过后，发一个新的 Access Token。

更稳一点的做法是，同时发一个新的 Refresh Token，并把旧的作废。

这就是 Refresh Token Rotation。

![图片](assets/%E4%B8%80%E4%B8%AA%20Token%20%E5%B0%B1%E5%A4%9F%E4%BA%86%EF%BC%8CJWT%20%E7%BB%AD%E7%AD%BE%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E6%90%9E%20Access%20Token%20+%20Refresh%20Token%20%E5%8F%8C%20Token%EF%BC%9F/a83962a0285daf81911c1a2f357abf5e_MD5.png)

Java 后端里，逻辑可以很简单。

登录时不要把重点放在「生成两个 JWT」上，重点应该放在「Access Token 短命，Refresh Token 可撤销」上。

伪代码大概是这样。

```
LoginResult login(String username, String password) {
    User user = checkPassword(username, password);

    String accessToken = 
            jwtService.createAccessToken(
          
            
            user.id(),
          
            
            Duration.ofMinutes(
          20)
    );

    String refreshToken = 
            tokenGenerator.secureRandom();
          
    String refreshHash = hash(refreshToken);

    
            refreshTokenStore.save(
          
            refreshHash,
            
            user.id(),
          
            currentDeviceId(),
            
            Duration.ofDays(
          14)
    );

    return new LoginResult(accessToken, refreshToken);
}
```

刷新时也一样。

```
TokenResult refresh(String refreshToken) {
    String oldHash = hash(refreshToken);
    RefreshSession session = 
            refreshTokenStore.find(oldHash);
          

    if (session == null || 
            session.expired())
           {
        throw new UnauthorizedException("请重新登录");
    }

    
            riskChecker.check(session);
          

    
            refreshTokenStore.delete(oldHash);
          

    String newRefreshToken = 
            tokenGenerator.secureRandom();
          
    
            refreshTokenStore.save(
          
            hash(newRefreshToken),
            
            session.userId(),
          
            
            session.deviceId(),
          
            
            Duration.ofDays(
          14)
    );

    String newAccessToken = 
            jwtService.createAccessToken(
          
            
            session.userId(),
          
            
            Duration.ofMinutes(
          20)
    );

    return new TokenResult(newAccessToken, newRefreshToken);
}
```

代码不复杂。

难的是边界。

你要清楚哪个 Token 能访问业务，哪个 Token 只能续签。你要清楚哪个 Token 可以无状态，哪个 Token 最好能撤销。你还要清楚退出登录、改密码、风险设备这些场景到底删什么。

## Refresh Token 为什么相对更安全

很多人会问，Refresh Token 有效期更长，那不是更危险吗？

对，它一旦被偷，确实危险。

所以双 Token 的安全性不是来自「Refresh Token 天生安全」。

它来自几件事叠在一起。

第一，Refresh Token 传输频率低。

Access Token 每个接口都带。首页接口、列表接口、详情接口、埋点接口，只要请求需要登录态，它就会出现。

Refresh Token 只在 Access Token 过期后刷新时使用。一天可能就几次。

暴露次数少，风险面就小。

第二，Refresh Token 可以放在更难被脚本读取的位置。

Web 里常见做法是 HttpOnly Cookie。它不是万能药，但至少能挡住一类直接通过 JavaScript 读取 token 的 XSS。

第三，刷新接口可以做重校验。

业务接口每次都校验设备指纹、IP 异常、客户端版本，成本不低，也容易误伤。

刷新接口调用频率低，就适合加更重的检查。

比如同一个 Refresh Token 突然从陌生地区、陌生设备、异常客户端过来，就可以拒绝刷新，或者要求重新登录。

第四，Refresh Token 可以轮换。

每次刷新都换一个新的 Refresh Token，旧的立刻失效。

这样做有一个好处，如果旧 Token 被重复使用，服务端就能发现异常。

正常情况下，旧 Token 用过一次就不该再出现。

如果它又出现了，说明要么客户端并发处理有问题，要么 Token 泄露了。

这时更谨慎的策略是，直接吊销这一整组 Refresh Token，也就是把这个设备会话或者 token family 都废掉，让用户重新登录。

OAuth 2.0 Security Best Current Practice 里也提到，对公开客户端来说，Refresh Token 要么做发送方约束，要么做轮换。原因就是公开客户端很难安全保存长期凭据，只能通过轮换和重放检测把风险压低。

## 前端最容易踩的坑，401 并发刷新

后端同学讲双 Token，经常讲到刷新接口就停了。

但前端那里还有一个坑。

Access Token 过期的一瞬间，页面上可能不是一个请求失败，而是一堆请求同时失败。

列表接口 401。

用户信息接口 401。

通知接口 401。

权限接口也 401。

如果每个 401 都去刷新一次，就会出事。

尤其你做了 Refresh Token Rotation。

第一个刷新请求成功后，旧 Refresh Token 已经作废，新 Refresh Token 已经下发。

第二个刷新请求如果还拿旧 Refresh Token 去换，就会失败。第三个、第四个也可能乱套。

最后用户明明只是 Access Token 过期，却被你踢回登录页。

所以前端要保证一件事。

同一时间，只能有一个刷新请求在路上。

其他失败请求排队等。

等第一个刷新拿到新 Access Token，再统一重放。

![图片](assets/%E4%B8%80%E4%B8%AA%20Token%20%E5%B0%B1%E5%A4%9F%E4%BA%86%EF%BC%8CJWT%20%E7%BB%AD%E7%AD%BE%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E6%90%9E%20Access%20Token%20+%20Refresh%20Token%20%E5%8F%8C%20Token%EF%BC%9F/b50bb48dfc8ec0f3bd06e7482217eb9b_MD5.png)

伪代码不展开太长，大概就是这个结构。

```
let refreshing = false;
let queue = [];

async function handle401(originalRequest) {
  if (refreshing) {
    return new Promise(resolve => {
      queue.push(token => {
        originalRequest.headers.Authorization = \`Bearer ${token}\`;
        resolve(api(originalRequest));
      });
    });
  }

  refreshing = true;

  try {
    const tokens = await refreshToken();
    saveTokens(tokens);

    queue.forEach(retry => retry(tokens.accessToken));
    queue = [];

    originalRequest.headers.Authorization = \`Bearer ${
            tokens.accessToken}
          \`;
    return api(originalRequest);
  } finally {
    refreshing = false;
  }
}
```

这段逻辑看起来是前端细节，其实和后端设计强相关。

只要后端做 Refresh Token Rotation，前端就必须处理并发刷新。不然你会得到一个非常诡异的 bug，用户偶尔自动退出，复现又不好复现。

## 退出登录、改密码、封禁用户，到底删什么

再聊一个工程里经常漏掉的点。

双 Token 做完后，很多人以为退出登录就是前端把 token 清掉。

不够。

前端清掉，只能保证这个浏览器不再主动带 Token。

真正要做的是，服务端删除对应的 Refresh Token。

因为 Access Token 本来就短命，通常可以等它自然过期。Refresh Token 才是长期登录态，它必须能被服务端撤销。

几个常见场景可以这么处理。

用户点击退出登录，删除当前设备的 Refresh Token。

用户修改密码，删除这个用户所有设备的 Refresh Token。

管理员封禁用户，删除所有 Refresh Token，并且业务接口校验用户状态。

发现 Refresh Token 重放，删除这一组 token family，让该设备重新登录。

高风险系统里，如果你不能接受 Access Token 还残留十几分钟，就再额外加 Access Token 黑名单或者版本号校验。

但普通系统里，通常没必要把所有请求都拖进黑名单查询。Access Token TTL 设短一点，Refresh Token 做可撤销，已经能覆盖绝大多数场景。

![图片](assets/%E4%B8%80%E4%B8%AA%20Token%20%E5%B0%B1%E5%A4%9F%E4%BA%86%EF%BC%8CJWT%20%E7%BB%AD%E7%AD%BE%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E6%90%9E%20Access%20Token%20+%20Refresh%20Token%20%E5%8F%8C%20Token%EF%BC%9F/d1463b80f26e2b1da5df82ea0a3765f9_MD5.png)

## 什么时候没必要上双 Token

双 Token 是好东西，但不是所有系统都需要。

内部管理后台，几十个运营或财务在用，Token 两小时过期，重新登录一次也能接受。工程复杂度没必要上来就拉满。

短期活动页，生命周期就几天，用户也不是长期登录，单 Token 或 Session 可能更省事。

本来就是 Session 架构的系统，也不用硬改成双 Token。

Session 天然是服务端有状态。你想让用户失效，删 Session 就行。双 Token 解决的很多问题，在 Session 里本来就存在成熟答案。

双 Token 更适合这些场景。

用户量比较大。

登录状态要保持很多天。

业务接口又希望保持 JWT 的无状态校验。

安全风险不能完全忽略。

用户体验还不能动不动跳登录。

移动端 App、SaaS、开放平台、面向 C 端的 Web 应用，通常就会落到这个区间。

## 最后用一句话收住

Access Token 是短命通行证。

Refresh Token 是可撤销的续签凭据。

双 Token 不是为了让登录系统看起来高级，而是为了把三个问题拆开。

业务接口要快，所以 Access Token 短期、轻量、适合高频校验。

用户体验要稳，所以 Refresh Token 长期、低频、负责续签。

安全风险要能兜住，所以 Refresh Token 最好可存储、可轮换、可撤销、可检测重放。

把这三件事想清楚，你再看双 Token，就不会觉得它是在把一个 Token 拆成两个。

它其实是在把「登录态」拆成两层。

一层负责日常通行。

一层负责长期续命。

平时互不打扰。

出事时，也知道该切哪一层。

参考资料：

- • RFC 9700，Best Current Practice for OAuth 2.0 Security： [https://www.rfc-editor.org/rfc/rfc9700.html](https://www.rfc-editor.org/rfc/rfc9700.html)
- • OWASP JSON Web Token for Java Cheat Sheet： [https://cheatsheetseries.owasp.org/cheatsheets/JSON\\\_Web\\\_Token\\\_for\\\_Java\\\_Cheat\\\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/JSON/_Web/_Token/_for/_Java/_Cheat/_Sheet.html)
- • OWASP OAuth2 Cheat Sheet： [https://cheatsheetseries.owasp.org/cheatsheets/OAuth2\\\_Cheat\\\_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2/_Cheat/_Sheet.html)