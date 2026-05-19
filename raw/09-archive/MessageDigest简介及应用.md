---
title: MessageDigest简介及应用
tags:
  - 加密
categories:
  - JAVA
date: 2022-05-28 18:58:41
---
### 1. 简介

java.security. MessageDigest 类用于为应用程序提供信息摘要算法的功能，如 MD5 或 SHA 算法。简单点说就是用于生成 散列码。 信息摘要是安全的单向哈希函数，它接收任意大小的数据，输出固定长度的哈希值。关于信息摘要和散列码请参照《 [数字证书简介](http://hubingforever.blog.163.com/blog/static/17104057920118981219705/) 》

MessageDigest 通过其getInstance系列静态函数来进行实例化和初始化。MessageDigest 对象通过使用`update` 方法处理数据。任何时候都可以调用 `reset`方法重置摘要。一旦所有需要更新的数据都已经被更新了，应该调用 `digest`方法之一完成哈希计算并返回结果。

对于给定数量的更新数据，`digest` 方法只能被调用一次。`digest` 方法被调用后，MessageDigest 对象被重新设置成其初始状态。

MessageDigest 的实现可随意选择是否实现 Cloneable 接口。客户端应用程可以通过尝试复制和捕获 CloneNotSupportedException 测试可复制性：

```
MessageDigest md = MessageDigest.getInstance("SHA-256");
 
  try {
      md.update(toChapter1);
      MessageDigest tc1 = md.clone();
      byte[] toChapter1Digest = tc1.digest();
      md.update(toChapter2);
      ...etc.
  } catch (CloneNotSupportedException cnse) {
      throw new DigestException("couldn't make digest of partial content");
  }
Copy
```

> 注意：
>
> 1. 如果给定的实现是不可克隆的，那么仍然可以通过实例化几个实例来计算中间摘要(如果摘要的数量事先知道的话)。
> 2. 由于历史原因，这个类是抽象的，从MessageDigestSpi继承而来。应用程序开发人员应该只注意这个MessageDigest类中定义的方法;超类中的所有方法都是为希望提供自己的消息摘要算法实现的加密服务提供者提供的。
> 3. MessageDigest并不是单实例的。如下代码所示：

```
try{

    MessageDigest mdTemp1 = MessageDigest.getInstance("MD5");

    MessageDigest mdTemp2= MessageDigest.getInstance("MD5");

    MessageDigest mdTemp3= MessageDigest.getInstance("MD5");

    System.out.println("mdTemp1==mdTemp2?:"+(mdTemp1==mdTemp2));

    System.out.println("mdTemp2==mdTemp3?:"+(mdTemp2==mdTemp3));

} catch (NoSuchAlgorithmException e){

    // TODO Auto-generated catch block

    e.printStackTrace();

}
Copy
```

运行结果

```
mdTemp1==mdTemp2?:false
mdTemp2==mdTemp3?:false
Copy
```

以上为jdk中的翻译和网上找来的翻译结果。

### 2. 使用MD5方法进行加密

```
/**
 * 密码MD5
 * @author wgp
 * @date 2021/7/13 14:17
 */

public class Md5Utils {

    private static Logger log = LoggerFactory.getLogger(Md5Utils.class);

    /**
     * TODO base64EncodeMD5 使用MD5方法加密
     *
     * 最终解码字符串的时候使用了base64去处理和直接转成String的方式没有什么区别
     *
     * @author wgp
     * @date 2021/7/13 14:50
     *
     * @param str
     * @return java.lang.String
     */
    public static String base64EncodeMD5(String str) {
        String md5Str = null;
        try {
            MessageDigest md5 = MessageDigest.getInstance("MD5");
            BASE64Encoder base64 = new BASE64Encoder();
            md5Str = base64.encode(md5.digest(str.getBytes()));
            log.info("【加密后的字符串："+md5Str+"】");
        } catch (NoSuchAlgorithmException e) {
            log.error("加密失败！");
            e.printStackTrace();
        }
        return md5Str;
    }

    /**
     * TODO getMD5Str
     * @author wgp
     * @date 2021/7/13 15:33
     *
     * @param str
     * @return java.lang.String
     */
    public static String getMD5Str(String str) {
        byte[] digest = null;
        try {
            //获取md5 为基础的加密算法 jdk中提供的加密算法有三种 “md5”，“sha - 1”，“sha - 256”
            MessageDigest md5 = MessageDigest.getInstance("md5");
            //入参为一个byte数组，所以按照utf-8的编码区转码
            //由于返回的结果也是一个byte[]所以经由base64做解码处理
            digest  = md5.digest(str.getBytes("utf-8"));
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
        // digest()最后确定返回md5 hash值，返回值为8位字符串。因为md5 hash值是16位的hex值，实际上就是8位的字符
        // BigInteger函数则将8位的字符串转换成16位hex值，用字符串来表示；得到字符串形式的hash值
        //一个byte是八位二进制，也就是2位十六进制字符（2的8次方等于16的2次方）
        String md5Str = new BigInteger(1, digest).toString(16);
        log.info("【加密后的字符串："+md5Str+"】");
        return md5Str;
    }

    public static void main(String[] args) {
        String s = "汪广平";
        String s1 = getMD5Str(s);
        //
        DigestUtils.md5DigestAsHex("1234".getBytes());
        System.out.println(s1.length());
    }
}

Copy
```

- `md5.reset()` 此方法是清除之前的摘要，但是个人感觉能用到的机会应该回很少。
- `md5.update()`此方法是将想要进行加密的内容加入摘要，其实就是将加密的内容更新进去，一会再调用机密算法的时候回调用它
- `md5.digest()`此方法是将摘要中的内容按照指定算法进行加密
- 在实际项目应用中spring有封装好的类直接可以使用

```
DigestUtils.md5DigestAsHex("1234".getBytes());
Copy
```

### 3.使用SHA-1加密

```
/**
    * TODO shaEncode  SHA-1实现
    * @author wgp
    * @date 2021/7/13 15:46
    *
    * @param inStr
    * @return java.lang.String
    */
   public static String shaEncode(String inStr){
       MessageDigest sha = null;
       StringBuffer hexValue = null;
       try {
           sha = MessageDigest.getInstance("SHA");
           byte[] byteArray = inStr.getBytes("UTF-8");
           byte[] md5Bytes = sha.digest(byteArray);
           hexValue = new StringBuffer();
           //new BigInteger(1,md5Bytes).toString(16); 此处也可以用这个方法处理然后直接返回字符串
           for (int i = 0; i < md5Bytes.length; i++) {
               int val = ((int) md5Bytes[i]) & 0xff;
               if (val < 16) {
                   hexValue.append("0");
               }
               hexValue.append(Integer.toHexString(val));
           }
       } catch (Exception e) {
           log.info(e.toString());
           e.printStackTrace();
           return "";
       }
       return hexValue.toString();
   }
Copy
```

- 也可以引用org.apache.commons.codec.digest.DigestUtils，然后按照如下方法调用加密即可。

```
public static String encodePassword(String psw) {
    if(StringUtils.isEmpty(psw)){
        return null;
    }else{
        return DigestUtils.sha1Hex(psw);
    }
} 
Copy
```

### 3. SHA-256 加密

代码基本和sha-1的一致，但是这些都是最简单的写法，只是学习用的一个实现，后续复杂操作，大多都是通过第三方的包去完成的，但是我还没有学习到，后续在考虑去出一篇博客！