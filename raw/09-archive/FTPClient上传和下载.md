---
title: FTPClient上传和下载
tags:
  - FTP
categories:
  - JAVA
date: 2022-05-28 18:52:51
---
### 1.需要的包

- org.apache.commons.net.ftp.FTPClient;

### 2.介绍

- 此处使用到了**递归**的算法，然后去执行下载整个文件夹或者下载单个文件
- 程序自动递归下载指定目录下的所有文件及子文件夹，上传时，自动递归创建服务器目录
- 此处执行的代码逻辑是先下载图片和xls文件，其他类型的文件不予下载，然后再上传到另一个服务器上，然后再把本地的缓存路径删除！

### 3. 代码

- 测试类

```
public static void main(String[] args) {
		String sysDate = "2021-02-23";
		//上传Ftp
		FTPClient uploadClient = null;
		//下载Ftp
		FTPClient downClient = null;
		
		try {
			downClient = FtpUtil.connectFtpServer("39.100.247.387", 21, "upolad", "srdJ5RaWzJbjtRpw",0);
			//获取下载上传路径
			String Dir = "/bhpsftp/e_photo/real-xiaobai/2021-02-23";
			String[] types = {".jpg",".xls",".xlsx"};
			String local = "D:\\temp\\real-xiaobai\\2021-02-23";
			FtpUtil.doDownload(downClient, Dir, local, types);
			
			
			
			uploadClient = FtpUtil.connectFtpServer("39.100.247.387", 21, "upolad", "srdJ5RaWzJbjtRpw",0);
			//获取文件上传路径
			String uploadDir = "/bhpsftp/e_photo/real-xiaobai/2021-02-23";
			File localFile = new File("D:\\temp\\real-xiaobai\\2021-02-23");
			boolean makeFtpDirs = FtpUtil.makeFtpDirs(uploadClient, uploadDir);
			System.out.println(makeFtpDirs);
			System.out.println(uploadDir);
			//上传所有文件
			FtpUtil.doUpload(uploadClient, uploadDir, localFile);
			
		} catch (Exception e) {
            e.printStackTrace();
        } finally {
        	try {
				FtpUtil.disconnectFtpServer(uploadClient);
				FtpUtil.delete(new File("D:\\temp\\/real-xinzhuang/2021-02-23"));
			} catch (Exception e) {
				e.printStackTrace();
			}
        }
//		
	}
Copy
```

- Ftp工具类

```
public static Logger log = LoggerFactory.getLogger(FtpUtil.class);

	public static FTPClient connectFtpServer(String host, int port,
			String username, String password) throws Exception {
		return connectFtpServer(host, port, username, password, 1);
	}

	/**
	 * @param mode
	 *            0,主动模式；1，被动模式
	 * @return ftp客户端
	 */
	public static FTPClient connectFtpServer(String host, int port,
			String username, String password, int mode) throws Exception {
		log.info("ftp连接信息：ip[" + host + "],port[" + port + "],ftpUser["
				+ username + "],ftpPasswd[" + password + "]");
		FTPClient ftpClient = null;

		ftpClient = new FTPClient();
		ftpClient.connect(host, port);
		ftpClient.setControlEncoding("GBK");
		if (ftpClient.login(username, password)) {
			ftpClient.setFileType(FTPClient.BINARY_FILE_TYPE);

			// 判断是否连接成功
			int reply = ftpClient.getReplyCode();
			if (!FTPReply.isPositiveCompletion(reply)) {
				ftpClient.disconnect();
				log.error("ftp连接失败[服务器拒绝连接]");
				return null;
			} else {
				if (mode == 0) {
					ftpClient.enterLocalActiveMode();
				} else {
					ftpClient.enterLocalPassiveMode();
				}
			}
		} else {
			log.error("ftp连接失败[登录失败]");
			return null;
		}

		return ftpClient;
	}

	/**
	 * 判断是否连接
	 */
	public static boolean isConnected(FTPClient ftpClient) {
		if (ftpClient.isConnected()) {
			return true;
		}
		return false;
	}

	/**
	 * 断开与对方ftp服务的连接。
	 */
	public static void disconnectFtpServer(FTPClient ftpClient)
			throws Exception {
		if (ftpClient != null) {
			ftpClient.logout();
			ftpClient.disconnect();
		}
	}

	/**
	 * 判断给定的路径是文件还是文件夹
	 * 
	 * @param path
	 * @return
	 * @throws IOException
	 */
	public static boolean isDirectory(FTPClient ftpClient, String path)
			throws IOException {
		if (path.endsWith(".")) {
			return false;
		}
		// 如果是文件，就会返回false
		// 如果文件夹或文件名中含有中文，这里要转换一下，不然会返回false
		return ftpClient.changeWorkingDirectory(new String(path.getBytes(),
				"ISO-8859-1"));
	}

/**
	 * 判断本地路径是否存在，不存在就创建路径
	 * 
	 * @param path
	 */
	public static void makeLocalDirs(String path) {
		File localFile = new File(path);
		if (!localFile.exists()) {
			localFile.mkdirs();
		}
	}

	/**
	 * 对比路径下照片是否存在
	 * 
	 * @param path
	 * @return
	 */
	public static String hasLocalFile(String path) {
		File localFile = new File(path);
		return localFile.exists() ? "1" : "0";
	}

	/**
	 * 下载单个文件
	 * 
	 * @param dir
	 * @throws IOException
	 */
	public static boolean downloadFile(FTPClient ftpClient, String dir,
			String localPath) {
		boolean boo = false;
		try {
			if (!dir.endsWith(".")) {
				File file = new File(localPath);
				OutputStream os = new FileOutputStream(file);
				ftpClient.setControlEncoding("UTF-8");
				ftpClient.setFileType(FTPClient.BINARY_FILE_TYPE);
				// ftpClient.enterLocalPassiveMode();
				boo = ftpClient.retrieveFile(new String(dir.getBytes(),
						"ISO-8859-1"), os);
				os.flush();
				os.close();
			}
			return boo;
		} catch (Exception e) {
			e.printStackTrace();
			return boo;
		}
	}

	/**
	 * 下载任务，递归调用，循环下载所有目录下的文件
	 * 
	 * @param path
	 * @throws IOException
	 */
	public static void doDownload(FTPClient ftpClient, String path,
			String localPath, String[] types) throws IOException {
		if (!path.endsWith(".") && types != null && types.length > 0) {
			// 创建本地目录
			makeLocalDirs(localPath);
			// 切换工作目录
			ftpClient.changeWorkingDirectory(new String(path.getBytes(),
					"ISO-8859-1"));
			// 获取目录下的文件列表
			String[] fileNames = ftpClient.listNames();
			// 循环下载FTP目录下的文件
			for (String fname : fileNames) {
				if (isDirectory(ftpClient, path + "/" + fname)) {
					// 递归调用
					doDownload(ftpClient, path + "/" + fname, localPath + "/"
							+ fname, types);
				} else {
					for (String type : types) {
						if (fname.endsWith(type)) {
							downloadFile(ftpClient, path + "/" + fname,
									localPath + "/" + fname);
						}
					}
				}
			}
		}
	}

	/**
	 * 判断ftp文件夹是否存在 不存在就创建
	 * 
	 * @param ftpClient
	 * @param path
	 * @return
	 * @throws IOException
	 */
	public static boolean makeFtpDirs(FTPClient ftpClient, String path)
			throws IOException {
 		if (!ftpClient.changeWorkingDirectory(path)) {
			return ftpClient.makeDirectory(path);
		}
		return false;
	}

	/**
	 * 上传任务，递归调用，循环上传所有目录下的文件
	 * 
	 * @param ftpClient
	 *            ftp对象
	 * @param path
	 *            ftp服务器上的路径
	 * @param localPath
	 *            本地存储路径
	 * @param types
	 *            文件类型
	 * @throws IOException
	 */
	public static void doUpload(FTPClient ftpClient, String path, File localFile)
			throws IOException {
		if (localFile.isDirectory()) {
			for (File ff : localFile.listFiles()) {
				if (ff.isDirectory()) {
					ftpClient.changeWorkingDirectory(path);
					if (!ftpClient.changeWorkingDirectory(path + "/"
							+ ff.getName())) {
						ftpClient.makeDirectory(ff.getName());
					}
					doUpload(ftpClient, path + "/" + ff.getName(), ff);// 递归调用，传文件夹
				} else {
					uploadFile(ftpClient, path, ff);
				}
			}
		} else {
			uploadFile(ftpClient, path, localFile);
		}
	}

	/**
	 * 单个文件上传
	 * 
	 * @param ftp
	 *            ftp对象
	 * @param remotePath
	 *            目录
	 * @param localFile
	 *            文件对象
	 * @return
	 * @throws IOException
	 */
	private static boolean uploadFile(FTPClient ftp, String remotePath,
			File localFile){
		InputStream input = null; // 输入流
		try {
			ftp.changeWorkingDirectory(remotePath);
			input = new FileInputStream(localFile);
			return ftp.storeFile(localFile.getName(),input);
		} catch (IOException e) {
			e.printStackTrace();
			return false;
		} finally {
			try {
				if(input != null){
					input.close();
				}
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}

	/**
	 * 删除文件夹及文件夹下的文件
	 * @param dir
	 * @return
	 */
	public static void delete(File dirFile) {
		if (dirFile != null && dirFile.exists()) {
			 if(dirFile.isDirectory()){
				// 删除文件夹中的所有文件包括子文件夹
				File[] files = dirFile.listFiles();
				for (int i = 0; i < files.length; i++) {
					if (files[i].isDirectory()) {
						delete(files[i]);
					}else{
						files[i].delete();
					}
				}
			 }
			 dirFile.delete();
		}
	}
```