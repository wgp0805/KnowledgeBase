---
title: "SpringBoot 实现电子文件签字+合同系统！"
source: "https://mp.weixin.qq.com/s/ZOc9ip43S-75EsSt0bQwmw"
---
小哈学Java *2026年7月14日 15:21*

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/ad6d58d7d9d617facd72a90aab4ae589_MD5.webp)

**在线 Java 面试刷题（已更新271题，图文并茂）： [https://www.quanxiaoha.com/java-interview](https://www.quanxiaoha.com/java-interview)**

- 一、前言
- 二、项目源码及部署
- 1、项目结构及使用框架
	- 2、项目下载及部署
- 三、功能展示

## 一、前言

今天公司领导提出一个功能，说实现一个文件的签字+盖章功能，然后自己进行了简单的学习，对文档进行数字签名与签署纸质文档的原因大致相同，数字签名通过使用计算机加密来验证 （身份验证：验证人员和产品所声明的身份是否属实的过程。例如，通过验证用于签名代码的数字签名来确认软件发行商的代码来源和完整性。）数字信息，如文档、电子邮件和宏。数字签名有助于确保：真实性，完整性，不可否认性。目前市面上的电子签章产品也是多样化，但是不管是哪个厂家的产品，在线签章简单易用，同时也能保证签章的有效性，防篡改，防伪造，稳定，可靠就是好产品。

此次开源的系统模拟演示了文件在OA系统中的流转，主要为办公系统跨平台在线处理Office文档提供了完美的解决方案。Word文档在线处理的核心环节，包括：起草文档、领导审批、核稿、领导盖章、正式发文。PageOffice产品支持PC端Word文档在线处理的所有环节；MobOffice产品支持了移动端领导审批和领导盖章的功能。支持PC端和移动端对文档审批和盖章的互认。然后此次博客中使用的卓正软件的电子签章采用自主知识产权的核心智能识别验证技术，确保文档安全可靠。采用 COM、ActiveX嵌入式技术开发，确保软件能够支持多种应用。遵循《中华人民共和国电子签名法》关于电子签名的规范，同时支持国际通用的 RSA算法，符合国家安全标准。

PageOffice和MobOffice产品结合使用为跨平台处理Office文件提供了完美的解决方案，主要功能有word在线编辑保存和留痕，word和pdf文件在线盖章(电子印章）。

## 二、项目源码及部署

### 1、项目结构及使用框架

该签字+盖章流程系统使用了SpringBoot+thymeleaf实现的，然后jar包依赖使用了maven

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/3e83fbf8dc752fa83b1a203688c77ac4_MD5.webp)

- 控制层
```
@Controller
@RequestMapping("/mobile")
public class MobileOfficeController {

    @Value("${docpath}")
    private  String docPath;

    @Value("${moblicpath}")
    private  String moblicpath;

    @Autowired
    DocService m_docService;

    /**
     * 添加MobOffice的服务器端授权程序Servlet（必须）
     *
     */
    @RequestMapping("/opendoc")
    public void opendoc(HttpServletRequest request, HttpServletResponse response, HttpSession session,String type,String userName)throws  Exception {
        String fileName = "";
        userName= 
            URLDecoder.decode(userName,
          "utf-8");

        Doc doc=
            m_docService.getDocById(1);
          
        if(
            type.equals(
          "word")){
            fileName = 
            doc.getDocName();
          
        }else{
            fileName = 
            doc.getPdfName();
          
        }
        OpenModeType openModeType = 
            OpenModeType.docNormalEdit;
          

        if (
            fileName.endsWith(
          ".doc")) {
            openModeType = 
            OpenModeType.docNormalEdit;
          
        } elseif (
            fileName.endsWith(
          ".pdf")) {
            String mode = 
            request.getParameter(
          "mode");
            if (
            mode.equals(
          "normal")) {
                openModeType = 
            OpenModeType.pdfNormal;
          
            } else {
                openModeType = 
            OpenModeType.pdfReadOnly;
          
            }
        }

        MobOfficeCtrl mobCtrl = new MobOfficeCtrl(request,response);
        
            mobCtrl.setSysPath(moblicpath);
          
        
            mobCtrl.setServerPage(
          "/
            mobserver.zz"
          );
        //
            mobCtrl.setZoomSealServer(
          "
            http://xxx.xxx.xxx.xxx:8080/ZoomSealEnt/enserver.zz"
          );
        
            mobCtrl.setSaveFilePage(
          "/mobile/savedoc?testid="+
            Math.random());
          
        
            mobCtrl.webOpen(
          "file://"+docPath+fileName,  openModeType , userName);
    }

    @RequestMapping("/savedoc")
    public  void  savedoc(HttpServletRequest request,  HttpServletResponse response){
        FileSaver fs = new FileSaver(request, response);
        
            fs.saveToFile(docPath+fs.getFileName());
          
        
            fs.close();
          
    }
}
```
- 项目业务层源码
```
@Service
public class DocServiceImpl implements DocService {
    @Autowired
    DocMapper docMapper;
    @Override
    public Doc getDocById(int id) throws Exception {
        Doc  doc=
            docMapper.getDocById(id);
          
        //如果doc为null的话，页面所有doc.属性都报错
        if(doc==null) {
            doc=new Doc();
        }
        return doc;
    }

    @Override
    public Integer addDoc(Doc doc) throws Exception {
       int id=
            docMapper.addDoc(doc);
          
        return id;
    }

    @Override
    public Integer updateStatusForDocById(Doc doc) throws Exception {
        int id=
            docMapper.updateStatusForDocById(doc);
          
        return id;
    }

    @Override
    public Integer updateDocNameForDocById(Doc doc) throws Exception {
        int id=
            docMapper.updateDocNameForDocById(doc);
          
        return id;
    }

    @Override
    public Integer updatePdfNameForDocById(Doc doc) throws Exception {
        int id=
            docMapper.updatePdfNameForDocById(doc);
          
        return id;
    }
}
```
- 拷贝文件
```
public class CopyFileUtil {
  //拷贝文件
  public static boolean copyFile(String oldPath, String newPath) throws Exception {
      boolean copyStatus=false;

      int bytesum = 0;
      int byteread = 0;
      File oldfile = new File(oldPath);
      if (
            oldfile.exists())
           { //文件存在时
          InputStream inStream = new FileInputStream(oldPath); //读入原文件
          FileOutputStream fs = new FileOutputStream(newPath);

          byte[] buffer = new byte[1444];
          int length;
          while ((byteread = 
            inStream.read(buffer))
           != -1) {
              bytesum += byteread; //字节数 文件大小
              //
            System.out.println(bytesum);
          
              
            fs.write(buffer,
           0, byteread);
          }
          
            fs.close();
          
          
            inStream.close();
          
          copyStatus=true;
      }else{
          copyStatus=false;
      }
      return copyStatus;
  }
}
```
- 二维码源码
```
public class QRCodeUtil {
    private String codeText;//二维码内容
    private BarcodeFormat barcodeFormat;//二维码类型
    private int width;//图片宽度
    private int height;//图片高度
    private String imageformat;//图片格式
    private int backColorRGB;//背景色，颜色RGB的数值既可以用十进制表示，也可以用十六进制表示
    private int codeColorRGB;//二维码颜色
    private ErrorCorrectionLevel errorCorrectionLevel;//二维码纠错能力
    private String encodeType;

    public QRCodeUtil() {
        codeText = "
            www.zhuozhengsoft.com"
          ;
        barcodeFormat = 
            BarcodeFormat.PDF_417;
          
        width = 400;
        height = 400;
        imageformat = "png";
        backColorRGB = 0xFFFFFFFF;
        codeColorRGB = 0xFF000000;
        errorCorrectionLevel = 
            ErrorCorrectionLevel.H;
          
        encodeType = "UTF-8";
    }
    public QRCodeUtil(String text) {
        codeText = text;
        barcodeFormat = 
            BarcodeFormat.PDF_417;
          
        width = 400;
        height = 400;
        imageformat = "png";
        backColorRGB = 0xFFFFFFFF;
        codeColorRGB = 0xFF000000;
        errorCorrectionLevel = 
            ErrorCorrectionLevel.H;
          
        encodeType = "UTF-8";
    }

    public String getCodeText() {
        return codeText;
    }

    public void setCodeText(String codeText) {
        
            this.codeText
           = codeText;
    }

    public BarcodeFormat getBarcodeFormat() {
        return barcodeFormat;
    }

    public void setBarcodeFormat(BarcodeFormat barcodeFormat) {
        
            this.barcodeFormat
           = barcodeFormat;
    }

    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        
            this.width
           = width;
    }

    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        
            this.height
           = height;
    }

    public String getImageformat() {
        return imageformat;
    }

    public void setImageformat(String imageformat) {
        
            this.imageformat
           = imageformat;
    }

    public int getBackColorRGB() {
        return backColorRGB;
    }

    public void setBackColorRGB(int backColorRGB) {
        
            this.backColorRGB
           = backColorRGB;
    }

    public int getCodeColorRGB() {
        return codeColorRGB;
    }

    public void setCodeColorRGB(int codeColorRGB) {
        
            this.codeColorRGB
           = codeColorRGB;
    }

    public ErrorCorrectionLevel getErrorCorrectionLevel() {
        return errorCorrectionLevel;
    }

    public void setErrorCorrectionLevel(ErrorCorrectionLevel errorCorrectionLevel) {
        
            this.errorCorrectionLevel
           = errorCorrectionLevel;
    }

    private BufferedImage toBufferedImage(BitMatrix bitMatrix) {
        int width = 
            bitMatrix.getWidth();
          
        int height = 
            bitMatrix.getHeight();
          
        BufferedImage image = new BufferedImage(width, height, 
            BufferedImage.TYPE_INT_RGB);
          
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                
            image.setRGB(x,
           y, 
            bitMatrix.get(x,
           y) ? 
            this.codeColorRGB:
           
            this.backColorRGB);
          
            }
        }
        return image;
    }

    private byte[] writeToBytes(BitMatrix bitMatrix)
            throws IOException {

        try {
            BufferedImage bufferedimage = toBufferedImage(bitMatrix);

            //将图片保存到临时路径中
            File file = 
            java.io.File.createTempFile(
          "~pic","."+ 
            this.imageformat);
          
            //
            System.out.println(
          "临时图片路径："+
            file.getPath());
          
            
            ImageIO.write(bufferedimage,this.imageformat,file);
          

            //获取图片转换成的二进制数组
            FileInputStream fis = new FileInputStream(file);
            int fileSize = 
            fis.available();
          
            byte[] imageBytes = new byte[fileSize];
            
            fis.read(imageBytes);
          
            
            fis.close();
          

            //删除临时文件
            if (
            file.exists())
           {
                
            file.delete();
          
            }

            return imageBytes;
        } catch (Exception e) {
            
            System.out.println(
          " Image err :" + 
            e.getMessage());
          
            return null;
        }

    }

    //获取二维码图片的字节数组
    public byte[] getQRCodeBytes()
            throws IOException {

        try {
            MultiFormatWriter multiFormatWriter = new MultiFormatWriter();

            //设置二维码参数
            Map hints = new HashMap();
            if (
            this.errorCorrectionLevel
           != null) {
                //设置二维码的纠错级别
                
            hints.put(EncodeHintType.ERROR_CORRECTION,
           
            this.errorCorrectionLevel);
          
            }

            if (
            this.encodeType!=null
           && 
            this.encodeType.trim().length()
           > 0) {
                //设置编码方式
                
            hints.put(EncodeHintType.CHARACTER_SET,
           
            this.encodeType);
          
            }

            BitMatrix bitMatrix = 
            multiFormatWriter.encode(this.codeText,
           
            BarcodeFormat.QR_CODE,
           
            this.width,
           
            this.height,
           hints);
            byte[] bytes = writeToBytes(bitMatrix);

            return bytes;
        } catch (Exception e) {
            
            e.printStackTrace();
          
            return null;
        }
    }
}
```

### 2、项目下载及部署

- 项目源码下载地址： [https://download.csdn.net/download/weixin\_44385486/86427996](https://download.csdn.net/download/weixin_44385486/86427996)
- 下载项目源码后，使用idea导入slndemo项目并运行

![8253f903324d947563eb85a31193f0f9.jpeg](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/cd0ae0d296b4af02572c1f947efa8982_MD5.webp)

- 将项目slndemo下的 [slndemodata.zip压缩包拷贝到本地D盘根目录下并解压](http://slndemodata.xn--zipd-894fn3tuqbv4aea144gjzuomclvs3yomzdcr1fzka177jbv6byqn/)

![820141840466bacdc9c63c96f3853cd3.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/711dcd741c46fdf36858a8b398bccec2_MD5.webp)

- 点击启动项目

![25445bec83c9d962a365ba7f0a6898e3.jpeg](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/1285804a150cc6a255ccce282d819d4d_MD5.webp)

## 三、功能展示

### 1、项目启动后登录首页

- 账户：张三 密码：123456

![d28bae984f03cdac864ce09d93ac870f.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/2927c5d6437f3bbcbedf6c3028c0d83a_MD5.webp)

### 2、系统首页功能简介

这是一个简单的Demo项目，模拟Word文件在办公系统中的主要流转环节，并不意味着PageOffice产品只能支持这样的文档处理流程。PageOffice产品只提供文档在线处理的功能，包括：打开、编辑、保存、动态填充、文档合并、套红、留痕、盖章等上百项功能（详细请参考PageOffice产品开发包中的示例），不提供流程控制功能，所以不管开发什么样的Web系统，只要是需要在线处理Office文档，都可以根据自己的项目需要，调用PageOffice产品相应的功能即可。 **「注意：为了简化代码逻辑，此演示程序只能创建一个文档进行流转。」**

![35d9fb4f7317d6574932baab51efb9c7.jpeg](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/87d0d5e9f1a53dc2049f07d2caca6841_MD5.webp)

### 3、点击起草文档

- 点击起草文档，点击提交

![ee5855af0df64de59b1abd3ff862c1c3.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/78be9fc4c544d26cd687c924ed4a0ca5_MD5.webp)

- 点击代办文档，然后点击编辑，当你点击编辑时你没有下载PageOffice，他会提醒你安装，你点击安装之后，关闭浏览器，重新打开浏览器就能编辑了！

![9448ab05ee580e7f3d521f795dfc03aa.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/e899c2f8c4b0a2adbcd676721fae0c6f_MD5.webp)

- 我们使用了PageOffice企业版，必须要注册序列化
- 版 本：PageOffice企业版5(试用)
- 序列号：35N8V-2YUC-LY77-W14XL

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/72e9c2417a929f5009d6508996eac62f_MD5.webp)

- 当我们注册成功以后，就可以编辑发布的文件或者公告了

![1f835881e264f898fa2c51dc8adcd167.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/e6b5a167d8462a5d4a3e2c9e91dbcc4d_MD5.webp)

- 编辑好以后点击保存

![104c2e6b94b7aba0f317332657e49fb4.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/c4c615a3778ac784ef8c2d81abcd3716_MD5.webp)

- 点击审批

![5ecffc8270e5e781b085f1334cbbd661.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/3b32e8aca1c93496b06bd9dc8c83a27d_MD5.webp)

### 4、审批

- 登录李总审批

![c656cb0fe7414cd9649583ad9a91cde9.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/19885f488aff5e1da0debaaed1541c9a_MD5.webp)

- 退出系统，然后输入李总

![043f20665741a8e7b8359ebd5f410a06.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/fca913ad7832c4eb80dfd2b3de1dac20_MD5.webp)

- ![dada4e9e5e1c24e8f6f0c9df818e5a54.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/07fbc056afb5e9a17d3b175715ee88a4_MD5.webp)
- 登录赵六进行审核稿子

![a20cfe1c9658172d05e02de2effe45ca.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/e0e6fcd80cc3faf926fb3c8eacb1fa61_MD5.webp)

### 5、审稿

- ![a3097590d041df2ad5a0581034b20ce1.jpeg](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/eab18ad87d1b37f94a538a2d654f2a13_MD5.webp)
- 审核然后到盖章环节

![6ac15701758d2987aee8e29bbe9d72dc.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/29696b8d87eb1b555baaac55a7597973_MD5.webp)

- 使用王总登录进行盖章

![d092f95c07754fcbd2b349fef9be3c7b.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/12c517d9668a1c6cb33286ed1c71ccf2_MD5.webp)

### 6、盖章和签字的实现

- 王总登录

![e1c1b9168b1e1728e3a6ff27b9c2d99a.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/74ae1c707bbbec1ce6e11f754632a5ef_MD5.webp)

- 点击盖章

![d915decd1396d3837f26217907bc88cb.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/75757579b6885d90bfe0a2c9402d1f84_MD5.webp)

- 点击加盖印章

![4ef62dd3b83751382b1783537f315ace.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/13987250b4ee06b18b0f48e8e03150cd_MD5.webp)

- 我们盖章前需要输入姓名+密码，需要输入错误报错

![4d09b489898b1913bc9850a3a3b1eb87.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/0fa35012232f97dd4a7341a98731835a_MD5.webp)

- 正确的账户密码是：
- 账户：王五
- 密码：123456

![789717f225bc936d5cc39fc87ccec38b.png](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/9f58e575d2e37ef553be09c7f330f20a_MD5.webp)

- 登录成功后有选择王五的个人章进行签字

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/23ea1683b4c1ae6f1914d063dfc95255_MD5.webp)

- 签字成功

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/db66feea25a9efb1cf711bb7055d9a18_MD5.webp)

- 公司盖章，重复以上步骤

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/7fdb29ededbd937f772536cc3d327d72_MD5.webp)

- 签字盖章成功

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/d9914358fd6d98652ec9e3c82a252adb_MD5.webp)

### 7、完整签字盖章文件

- 保存之后发布文件

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/d7b2ca0bf0558053d0a8a23a9304b772_MD5.webp)

- 公司文件展示

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/8a9645bc3d6c5bdbb0f962aaed4f314d_MD5.webp)

- 盖章签字后的文件
![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/4676f8ac361856ae60cafd7fb3e7091f_MD5.webp)

图片

，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / **Java 学习路线 /** 社群讨论 / **学习打卡 / 每月赠书****

- 《仿小红书（微服务架构）》 已完结，基于 Spring Cloud Alibaba + Spring Boot [3.x](http://3.x/) + JDK 17..., ；演示地址：http://116.62.199.48:7070/
- 《Spring AI 应用（RAG 智能客服）》已完结, 基于 Spring AI + Spring Boot [3.x](http://3.x/) + JDK 21
- 《秒杀系统设计》正在更新中，单体到微服务高并发架构演进
- **《前后端分离博客项目（全栈开发）》** 已完结,演示链接：http://116.62.199.48/
- 项目阅读地址： [https://quanxiaoha.com/column](https://quanxiaoha.com/column)

截止目前， **累计输出 120w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4500+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/SpringBoot%20%E5%AE%9E%E7%8E%B0%E7%94%B5%E5%AD%90%E6%96%87%E4%BB%B6%E7%AD%BE%E5%AD%97+%E5%90%88%E5%90%8C%E7%B3%BB%E7%BB%9F%EF%BC%81/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~2. 面试官：BeanFactory 和 FactroyBean 的关系？3. 使用 Shadcn UI 构建 Java 桌面应用4. 大模型时代最讽刺的职业出现了：“大模型善后工程师”
```
```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。点“在看”支持小哈呀，谢谢
```

阅读原文