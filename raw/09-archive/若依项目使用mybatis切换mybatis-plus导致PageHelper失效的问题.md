---
title: 若依项目使用mybatis切换mybatis-plus导致PageHelper失效的问题
tags:
  - mybatis-plus
categories:
  - mybatis-plus
date: 2025-01-02 09:36:32
---

今天在单位，经理给新来的新人出了一个小问题，来判断新人的能力，小问题不是很复杂，是用网上一直很火的开源项目若依，主要的问题是，在若依的项目将mybatis更换为mybatis-plus，由于plus的方便，所以现在对于单表查询大家都是不愿意去写xml的，我当时看感觉也不是很复杂，可能唯一复杂的地方就是在写mybatisplus的配置文件，可能比较困难，但是若依的官方网站有切换的方法，所以不是很难，当我弄完之后，经理说了一句这样会有问题，你看看分页是不是不好使了，一看果然如此，但是始终不知道问题出在哪里，

```java
package com.ruoyi.framework.config;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import javax.sql.DataSource;
import org.apache.ibatis.io.VFS;
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.boot.autoconfigure.SpringBootVFS;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;
import org.springframework.core.io.DefaultResourceLoader;
import org.springframework.core.io.Resource;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;
import org.springframework.core.io.support.ResourcePatternResolver;
import org.springframework.core.type.classreading.CachingMetadataReaderFactory;
import org.springframework.core.type.classreading.MetadataReader;
import org.springframework.core.type.classreading.MetadataReaderFactory;
import org.springframework.util.ClassUtils;
import com.ruoyi.common.utils.StringUtils;

/**
* Mybatis支持*匹配扫描包
*
* @author ruoyi
*/
@Configuration
public class MyBatisConfig
{
   @Autowired
   private Environment env;

   static final String DEFAULT_RESOURCE_PATTERN = "**/*.class";

   public static String setTypeAliasesPackage(String typeAliasesPackage)
   {
       ResourcePatternResolver resolver = (ResourcePatternResolver) new PathMatchingResourcePatternResolver();
       MetadataReaderFactory metadataReaderFactory = new CachingMetadataReaderFactory(resolver);
       List<String> allResult = new ArrayList<String>();
       try
       {
           for (String aliasesPackage : typeAliasesPackage.split(","))
           {
               List<String> result = new ArrayList<String>();
               aliasesPackage = ResourcePatternResolver.CLASSPATH_ALL_URL_PREFIX
                       + ClassUtils.convertClassNameToResourcePath(aliasesPackage.trim()) + "/" + DEFAULT_RESOURCE_PATTERN;
               Resource[] resources = resolver.getResources(aliasesPackage);
               if (resources != null && resources.length > 0)
               {
                   MetadataReader metadataReader = null;
                   for (Resource resource : resources)
                   {
                       if (resource.isReadable())
                       {
                           metadataReader = metadataReaderFactory.getMetadataReader(resource);
                           try
                           {
                               result.add(Class.forName(metadataReader.getClassMetadata().getClassName()).getPackage().getName());
                           }
                           catch (ClassNotFoundException e)
                           {
                               e.printStackTrace();
                           }
                       }
                   }
               }
               if (result.size() > 0)
               {
                   HashSet<String> hashResult = new HashSet<String>(result);
                   allResult.addAll(hashResult);
               }
           }
           if (allResult.size() > 0)
           {
               typeAliasesPackage = String.join(",", (String[]) allResult.toArray(new String[0]));
           }
           else
           {
               throw new RuntimeException("mybatis typeAliasesPackage 路径扫描错误,参数typeAliasesPackage:" + typeAliasesPackage + "未找到任何包");
           }
       }
       catch (IOException e)
       {
           e.printStackTrace();
       }
       return typeAliasesPackage;
   }

   public Resource[] resolveMapperLocations(String[] mapperLocations)
   {
       ResourcePatternResolver resourceResolver = new PathMatchingResourcePatternResolver();
       List<Resource> resources = new ArrayList<Resource>();
       if (mapperLocations != null)
       {
           for (String mapperLocation : mapperLocations)
           {
               try
               {
                   Resource[] mappers = resourceResolver.getResources(mapperLocation);
                   resources.addAll(Arrays.asList(mappers));
               }
               catch (IOException e)
               {
                   // ignore
               }
           }
       }
       return resources.toArray(new Resource[resources.size()]);
   }

   @Bean
   public SqlSessionFactory sqlSessionFactory(DataSource dataSource) throws Exception
   {
       String typeAliasesPackage = env.getProperty("mybatis.typeAliasesPackage");
       String mapperLocations = env.getProperty("mybatis.mapperLocations");
       String configLocation = env.getProperty("mybatis.configLocation");
       typeAliasesPackage = setTypeAliasesPackage(typeAliasesPackage);
       VFS.addImplClass(SpringBootVFS.class);

       final SqlSessionFactoryBean sessionFactory = new SqlSessionFactoryBean();
       sessionFactory.setDataSource(dataSource);
       sessionFactory.setTypeAliasesPackage(typeAliasesPackage);
       sessionFactory.setMapperLocations(resolveMapperLocations(StringUtils.split(mapperLocations, ",")));
       sessionFactory.setConfigLocation(new DefaultResourceLoader().getResource(configLocation));
       return sessionFactory.getObject();
   }
}
```

这是原来的mybatis的配置按照官网的操作步骤，是要把这个都注释掉，然后加入新的，新的配置官网都有直接复制就行

```java
package com.ruoyi.framework.config;

import com.baomidou.mybatisplus.annotation.DbType;
import com.baomidou.mybatisplus.extension.plugins.MybatisPlusInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.BlockAttackInnerInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.OptimisticLockerInnerInterceptor;
import com.baomidou.mybatisplus.extension.plugins.inner.PaginationInnerInterceptor;
import com.github.pagehelper.PageInterceptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.transaction.annotation.EnableTransactionManagement;

/**
 * Mybatis Plus 配置
 *
 * @author ruoyi
 */
@EnableTransactionManagement(proxyTargetClass = true)
@Configuration
public class MybatisPlusConfig
{
    @Bean
    public MybatisPlusInterceptor mybatisPlusInterceptor()
    {
        MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
        // 分页插件
        interceptor.addInnerInterceptor(paginationInnerInterceptor());
        // 乐观锁插件
        interceptor.addInnerInterceptor(optimisticLockerInnerInterceptor());
        // 阻断插件
        interceptor.addInnerInterceptor(blockAttackInnerInterceptor());
        return interceptor;
    }

    /**
     * 分页插件，自动识别数据库类型 https://baomidou.com/guide/interceptor-pagination.html
     */
    public PaginationInnerInterceptor paginationInnerInterceptor()
    {
        PaginationInnerInterceptor paginationInnerInterceptor = new PaginationInnerInterceptor();
        // 设置数据库类型为mysql
        paginationInnerInterceptor.setDbType(DbType.MYSQL);
        // 设置最大单页限制数量，默认 500 条，-1 不受限制
        paginationInnerInterceptor.setMaxLimit(-1L);
        return paginationInnerInterceptor;
    }

    /**
     * 乐观锁插件 https://baomidou.com/guide/interceptor-optimistic-locker.html
     */
    public OptimisticLockerInnerInterceptor optimisticLockerInnerInterceptor()
    {
        return new OptimisticLockerInnerInterceptor();
    }

    /**
     * 如果是对全表的删除或更新操作，就会终止该操作 https://baomidou.com/guide/interceptor-block-attack.html
     */
    public BlockAttackInnerInterceptor blockAttackInnerInterceptor()
    {
        return new BlockAttackInnerInterceptor();
    }

}
```

然后我们这边经理指定了mybatisplus的版本`<mybatis-plus.version>3.5.9</mybatis-plus.version>`,pagehelper不用动。在总的`pom.xml`中加入配置信息

```xml
  <!-- mybatis-plus -->
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-spring-boot3-starter</artifactId>
        <version>${mybatis-plus.version}</version>
    </dependency>
```

到这里若依官网的修改建议就结束了，但是这时在启动的时候会报错

```txt
C:\Java\jdk17\bin\java.exe -agentlib:jdwp=transport=dt_socket,address=127.0.0.1:11595,suspend=y,server=n -agentpath:C:\Users\w1217\AppData\Local\Temp\idea_libasyncProfiler_dll_temp_folder7618\libasyncProfiler.dll=version,jfr,event=wall,interval=10ms,cstack=no,file=C:\Users\w1217\IdeaSnapshots\RuoYiApplication_2025_01_02_094531.jfr,dbghelppath=C:\Users\w1217\AppData\Local\Temp\idea_dbghelp_dll_temp_folder1\dbghelp.dll,log=C:\Users\w1217\AppData\Local\Temp\RuoYiApplication_2025_01_02_094531.jfr.log.txt,logLevel=DEBUG -XX:TieredStopAtLevel=1 -Dspring.output.ansi.enabled=always -Dcom.sun.management.jmxremote -Dspring.jmx.enabled=true -Dspring.liveBeansView.mbeanDomain -Dspring.application.admin.enabled=true "-Dmanagement.endpoints.jmx.exposure.include=*" -javaagent:C:\Users\w1217\AppData\Local\JetBrains\IntelliJIdea2024.3\captureAgent\debugger-agent.jar -Dkotlinx.coroutines.debug.enable.creation.stack.trace=false -Ddebugger.agent.enable.coroutines=true -Dkotlinx.coroutines.debug.enable.flows.stack.trace=true -Dkotlinx.coroutines.debug.enable.mutable.state.flows.stack.trace=true -Dfile.encoding=UTF-8 -classpath "D:\java\IDEA\Project-gs\RuoYi-Vue-springboot3\ruoyi-admin\target\classes;D:\java\apache-maven-3.2.2\repository\org\springdoc\springdoc-openapi-starter-webmvc-ui\2.5.0\springdoc-openapi-starter-webmvc-ui-2.5.0.jar;D:\java\apache-maven-3.2.2\repository\org\springdoc\springdoc-openapi-starter-webmvc-api\2.5.0\springdoc-openapi-starter-webmvc-api-2.5.0.jar;D:\java\apache-maven-3.2.2\repository\org\springdoc\springdoc-openapi-starter-common\2.5.0\springdoc-openapi-starter-common-2.5.0.jar;D:\java\apache-maven-3.2.2\repository\io\swagger\core\v3\swagger-core-jakarta\2.2.21\swagger-core-jakarta-2.2.21.jar;D:\java\apache-maven-3.2.2\repository\io\swagger\core\v3\swagger-annotations-jakarta\2.2.21\swagger-annotations-jakarta-2.2.21.jar;D:\java\apache-maven-3.2.2\repository\io\swagger\core\v3\swagger-models-jakarta\2.2.21\swagger-models-jakarta-2.2.21.jar;D:\java\apache-maven-3.2.2\repository\jakarta\xml\bind\jakarta.xml.bind-api\4.0.2\jakarta.xml.bind-api-4.0.2.jar;D:\java\apache-maven-3.2.2\repository\jakarta\activation\jakarta.activation-api\2.1.3\jakarta.activation-api-2.1.3.jar;D:\java\apache-maven-3.2.2\repository\jakarta\validation\jakarta.validation-api\3.0.2\jakarta.validation-api-3.0.2.jar;D:\java\apache-maven-3.2.2\repository\com\fasterxml\jackson\dataformat\jackson-dataformat-yaml\2.17.1\jackson-dataformat-yaml-2.17.1.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-webmvc\6.1.8\spring-webmvc-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-beans\6.1.8\spring-beans-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-context\6.1.8\spring-context-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-core\6.1.8\spring-core-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-jcl\6.1.8\spring-jcl-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-expression\6.1.8\spring-expression-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\webjars\swagger-ui\5.13.0\swagger-ui-5.13.0.jar;D:\java\apache-maven-3.2.2\repository\com\mysql\mysql-connector-j\8.2.0\mysql-connector-j-8.2.0.jar;D:\java\apache-maven-3.2.2\repository\com\google\protobuf\protobuf-java\3.21.9\protobuf-java-3.21.9.jar;D:\java\IDEA\Project-gs\RuoYi-Vue-springboot3\ruoyi-framework\target\classes;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter-web\3.3.0\spring-boot-starter-web-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter\3.3.0\spring-boot-starter-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot\3.3.0\spring-boot-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter-logging\3.3.0\spring-boot-starter-logging-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\ch\qos\logback\logback-classic\1.5.6\logback-classic-1.5.6.jar;D:\java\apache-maven-3.2.2\repository\ch\qos\logback\logback-core\1.5.6\logback-core-1.5.6.jar;D:\java\apache-maven-3.2.2\repository\org\apache\logging\log4j\log4j-to-slf4j\2.23.1\log4j-to-slf4j-2.23.1.jar;D:\java\apache-maven-3.2.2\repository\org\apache\logging\log4j\log4j-api\2.23.1\log4j-api-2.23.1.jar;D:\java\apache-maven-3.2.2\repository\org\slf4j\jul-to-slf4j\2.0.13\jul-to-slf4j-2.0.13.jar;D:\java\apache-maven-3.2.2\repository\jakarta\annotation\jakarta.annotation-api\2.1.1\jakarta.annotation-api-2.1.1.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter-json\3.3.0\spring-boot-starter-json-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\com\fasterxml\jackson\datatype\jackson-datatype-jdk8\2.17.1\jackson-datatype-jdk8-2.17.1.jar;D:\java\apache-maven-3.2.2\repository\com\fasterxml\jackson\datatype\jackson-datatype-jsr310\2.17.1\jackson-datatype-jsr310-2.17.1.jar;D:\java\apache-maven-3.2.2\repository\com\fasterxml\jackson\module\jackson-module-parameter-names\2.17.1\jackson-module-parameter-names-2.17.1.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter-tomcat\3.3.0\spring-boot-starter-tomcat-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\apache\tomcat\embed\tomcat-embed-core\10.1.24\tomcat-embed-core-10.1.24.jar;D:\java\apache-maven-3.2.2\repository\org\apache\tomcat\embed\tomcat-embed-el\10.1.24\tomcat-embed-el-10.1.24.jar;D:\java\apache-maven-3.2.2\repository\org\apache\tomcat\embed\tomcat-embed-websocket\10.1.24\tomcat-embed-websocket-10.1.24.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-web\6.1.8\spring-web-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\io\micrometer\micrometer-observation\1.13.0\micrometer-observation-1.13.0.jar;D:\java\apache-maven-3.2.2\repository\io\micrometer\micrometer-commons\1.13.0\micrometer-commons-1.13.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter-aop\3.3.0\spring-boot-starter-aop-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-aop\6.1.8\spring-aop-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\aspectj\aspectjweaver\1.9.22\aspectjweaver-1.9.22.jar;D:\java\apache-maven-3.2.2\repository\com\alibaba\druid-spring-boot-3-starter\1.2.23\druid-spring-boot-3-starter-1.2.23.jar;D:\java\apache-maven-3.2.2\repository\com\alibaba\druid\1.2.23\druid-1.2.23.jar;D:\java\apache-maven-3.2.2\repository\org\slf4j\slf4j-api\2.0.13\slf4j-api-2.0.13.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-autoconfigure\3.3.0\spring-boot-autoconfigure-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\pro\fessional\kaptcha\2.3.3\kaptcha-2.3.3.jar;D:\java\apache-maven-3.2.2\repository\com\jhlabs\filters\2.0.235-1\filters-2.0.235-1.jar;D:\java\apache-maven-3.2.2\repository\com\github\oshi\oshi-core\6.6.3\oshi-core-6.6.3.jar;D:\java\apache-maven-3.2.2\repository\net\java\dev\jna\jna\5.14.0\jna-5.14.0.jar;D:\java\apache-maven-3.2.2\repository\net\java\dev\jna\jna-platform\5.14.0\jna-platform-5.14.0.jar;D:\java\IDEA\Project-gs\RuoYi-Vue-springboot3\ruoyi-system\target\classes;D:\java\IDEA\Project-gs\RuoYi-Vue-springboot3\ruoyi-quartz\target\classes;D:\java\apache-maven-3.2.2\repository\org\quartz-scheduler\quartz\2.3.2\quartz-2.3.2.jar;D:\java\apache-maven-3.2.2\repository\com\mchange\mchange-commons-java\0.2.15\mchange-commons-java-0.2.15.jar;D:\java\IDEA\Project-gs\RuoYi-Vue-springboot3\ruoyi-common\target\classes;D:\java\apache-maven-3.2.2\repository\com\baomidou\mybatis-plus-spring-boot3-starter\3.5.9\mybatis-plus-spring-boot3-starter-3.5.9.jar;D:\java\apache-maven-3.2.2\repository\com\baomidou\mybatis-plus\3.5.9\mybatis-plus-3.5.9.jar;D:\java\apache-maven-3.2.2\repository\com\baomidou\mybatis-plus-core\3.5.9\mybatis-plus-core-3.5.9.jar;D:\java\apache-maven-3.2.2\repository\com\baomidou\mybatis-plus-annotation\3.5.9\mybatis-plus-annotation-3.5.9.jar;D:\java\apache-maven-3.2.2\repository\com\baomidou\mybatis-plus-spring\3.5.9\mybatis-plus-spring-3.5.9.jar;D:\java\apache-maven-3.2.2\repository\org\mybatis\mybatis\3.5.16\mybatis-3.5.16.jar;D:\java\apache-maven-3.2.2\repository\org\mybatis\mybatis-spring\3.0.4\mybatis-spring-3.0.4.jar;D:\java\apache-maven-3.2.2\repository\com\baomidou\mybatis-plus-spring-boot-autoconfigure\3.5.9\mybatis-plus-spring-boot-autoconfigure-3.5.9.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter-jdbc\3.3.0\spring-boot-starter-jdbc-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\com\zaxxer\HikariCP\5.1.0\HikariCP-5.1.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-jdbc\6.1.8\spring-jdbc-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\com\baomidou\mybatis-plus-jsqlparser\3.5.9\mybatis-plus-jsqlparser-3.5.9.jar;D:\java\apache-maven-3.2.2\repository\com\github\jsqlparser\jsqlparser\5.0\jsqlparser-5.0.jar;D:\java\apache-maven-3.2.2\repository\com\baomidou\mybatis-plus-jsqlparser-common\3.5.9\mybatis-plus-jsqlparser-common-3.5.9.jar;D:\java\apache-maven-3.2.2\repository\com\baomidou\mybatis-plus-extension\3.5.9\mybatis-plus-extension-3.5.9.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-context-support\6.1.8\spring-context-support-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter-security\3.3.0\spring-boot-starter-security-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\security\spring-security-config\6.3.0\spring-security-config-6.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\security\spring-security-core\6.3.0\spring-security-core-6.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\security\spring-security-crypto\6.3.0\spring-security-crypto-6.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\security\spring-security-web\6.3.0\spring-security-web-6.3.0.jar;D:\java\apache-maven-3.2.2\repository\com\github\pagehelper\pagehelper-spring-boot-starter\2.1.0\pagehelper-spring-boot-starter-2.1.0.jar;D:\java\apache-maven-3.2.2\repository\com\github\pagehelper\pagehelper-spring-boot-autoconfigure\2.1.0\pagehelper-spring-boot-autoconfigure-2.1.0.jar;D:\java\apache-maven-3.2.2\repository\com\github\pagehelper\pagehelper\6.1.0\pagehelper-6.1.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter-validation\3.3.0\spring-boot-starter-validation-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\hibernate\validator\hibernate-validator\8.0.1.Final\hibernate-validator-8.0.1.Final.jar;D:\java\apache-maven-3.2.2\repository\org\jboss\logging\jboss-logging\3.5.3.Final\jboss-logging-3.5.3.Final.jar;D:\java\apache-maven-3.2.2\repository\com\fasterxml\classmate\1.7.0\classmate-1.7.0.jar;D:\java\apache-maven-3.2.2\repository\org\apache\commons\commons-lang3\3.14.0\commons-lang3-3.14.0.jar;D:\java\apache-maven-3.2.2\repository\com\fasterxml\jackson\core\jackson-databind\2.17.1\jackson-databind-2.17.1.jar;D:\java\apache-maven-3.2.2\repository\com\fasterxml\jackson\core\jackson-annotations\2.17.1\jackson-annotations-2.17.1.jar;D:\java\apache-maven-3.2.2\repository\com\fasterxml\jackson\core\jackson-core\2.17.1\jackson-core-2.17.1.jar;D:\java\apache-maven-3.2.2\repository\com\alibaba\fastjson2\fastjson2\2.0.53\fastjson2-2.0.53.jar;D:\java\apache-maven-3.2.2\repository\commons-io\commons-io\2.13.0\commons-io-2.13.0.jar;D:\java\apache-maven-3.2.2\repository\org\apache\poi\poi-ooxml\4.1.2\poi-ooxml-4.1.2.jar;D:\java\apache-maven-3.2.2\repository\org\apache\poi\poi\4.1.2\poi-4.1.2.jar;D:\java\apache-maven-3.2.2\repository\commons-codec\commons-codec\1.16.1\commons-codec-1.16.1.jar;D:\java\apache-maven-3.2.2\repository\org\apache\commons\commons-collections4\4.4\commons-collections4-4.4.jar;D:\java\apache-maven-3.2.2\repository\org\apache\commons\commons-math3\3.6.1\commons-math3-3.6.1.jar;D:\java\apache-maven-3.2.2\repository\com\zaxxer\SparseBitSet\1.2\SparseBitSet-1.2.jar;D:\java\apache-maven-3.2.2\repository\org\apache\poi\poi-ooxml-schemas\4.1.2\poi-ooxml-schemas-4.1.2.jar;D:\java\apache-maven-3.2.2\repository\org\apache\xmlbeans\xmlbeans\3.1.0\xmlbeans-3.1.0.jar;D:\java\apache-maven-3.2.2\repository\org\apache\commons\commons-compress\1.19\commons-compress-1.19.jar;D:\java\apache-maven-3.2.2\repository\com\github\virtuald\curvesapi\1.06\curvesapi-1.06.jar;D:\java\apache-maven-3.2.2\repository\org\yaml\snakeyaml\2.2\snakeyaml-2.2.jar;D:\java\apache-maven-3.2.2\repository\io\jsonwebtoken\jjwt\0.9.1\jjwt-0.9.1.jar;D:\java\apache-maven-3.2.2\repository\javax\xml\bind\jaxb-api\2.3.1\jaxb-api-2.3.1.jar;D:\java\apache-maven-3.2.2\repository\javax\activation\javax.activation-api\1.2.0\javax.activation-api-1.2.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\boot\spring-boot-starter-data-redis\3.3.0\spring-boot-starter-data-redis-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\io\lettuce\lettuce-core\6.3.2.RELEASE\lettuce-core-6.3.2.RELEASE.jar;D:\java\apache-maven-3.2.2\repository\io\netty\netty-common\4.1.110.Final\netty-common-4.1.110.Final.jar;D:\java\apache-maven-3.2.2\repository\io\netty\netty-handler\4.1.110.Final\netty-handler-4.1.110.Final.jar;D:\java\apache-maven-3.2.2\repository\io\netty\netty-resolver\4.1.110.Final\netty-resolver-4.1.110.Final.jar;D:\java\apache-maven-3.2.2\repository\io\netty\netty-buffer\4.1.110.Final\netty-buffer-4.1.110.Final.jar;D:\java\apache-maven-3.2.2\repository\io\netty\netty-transport-native-unix-common\4.1.110.Final\netty-transport-native-unix-common-4.1.110.Final.jar;D:\java\apache-maven-3.2.2\repository\io\netty\netty-codec\4.1.110.Final\netty-codec-4.1.110.Final.jar;D:\java\apache-maven-3.2.2\repository\io\netty\netty-transport\4.1.110.Final\netty-transport-4.1.110.Final.jar;D:\java\apache-maven-3.2.2\repository\io\projectreactor\reactor-core\3.6.6\reactor-core-3.6.6.jar;D:\java\apache-maven-3.2.2\repository\org\reactivestreams\reactive-streams\1.0.4\reactive-streams-1.0.4.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\data\spring-data-redis\3.3.0\spring-data-redis-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\data\spring-data-keyvalue\3.3.0\spring-data-keyvalue-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\data\spring-data-commons\3.3.0\spring-data-commons-3.3.0.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-tx\6.1.8\spring-tx-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\springframework\spring-oxm\6.1.8\spring-oxm-6.1.8.jar;D:\java\apache-maven-3.2.2\repository\org\apache\commons\commons-pool2\2.12.0\commons-pool2-2.12.0.jar;D:\java\apache-maven-3.2.2\repository\eu\bitwalker\UserAgentUtils\1.21\UserAgentUtils-1.21.jar;D:\java\apache-maven-3.2.2\repository\jakarta\servlet\jakarta.servlet-api\6.0.0\jakarta.servlet-api-6.0.0.jar;D:\java\IDEA\Project-gs\RuoYi-Vue-springboot3\ruoyi-generator\target\classes;D:\java\apache-maven-3.2.2\repository\org\apache\velocity\velocity-engine-core\2.3\velocity-engine-core-2.3.jar;D:\java\IDEA\Project-gs\RuoYi-Vue-springboot3\ruoyi-mes\target\classes;D:\java\IDEA\IntelliJ IDEA 2024.3\lib\idea_rt.jar" com.ruoyi.RuoYiApplication
Connected to the target VM, address: '127.0.0.1:11595', transport: 'socket'
Application Version: 3.8.8
Spring Boot Version: 3.3.0
////////////////////////////////////////////////////////////////////
//                          _ooOoo_                               //
//                         o8888888o                              //
//                         88" . "88                              //
//                         (| ^_^ |)                              //
//                         O\  =  /O                              //
//                      ____/`---'\____                           //
//                    .'  \\|     |//  `.                         //
//                   /  \\|||  :  |||//  \                        //
//                  /  _||||| -:- |||||-  \                       //
//                  |   | \\\  -  /// |   |                       //
//                  | \_|  ''\---/''  |   |                       //
//                  \  .-\__  `-`  ___/-. /                       //
//                ___`. .'  /--.--\  `. . ___                     //
//              ."" '<  `.___\_<|>_/___.'  >'"".                  //
//            | | :  `- \`.;`\ _ /`;.`/ - ` : | |                 //
//            \  \ `-.   \_ __\ /__ _/   .-` /  /                 //
//      ========`-.____`-.___\_____/___.-`____.-'========         //
//                           `=---='                              //
//      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^        //
//             佛祖保佑       永不宕机      永无BUG               //
////////////////////////////////////////////////////////////////////
09:45:32.524 [background-preinit] INFO  o.h.v.i.util.Version - [<clinit>,21] - HV000001: Hibernate Validator 8.0.1.Final
09:45:32.560 [main] INFO  c.r.RuoYiApplication - [logStarting,50] - Starting RuoYiApplication using Java 17 with PID 23124 (D:\java\IDEA\Project-gs\RuoYi-Vue-springboot3\ruoyi-admin\target\classes started by w1217 in D:\java\IDEA\Project-gs\RuoYi-Vue-springboot3)
09:45:32.561 [main] DEBUG c.r.RuoYiApplication - [logStarting,51] - Running with Spring Boot v3.3.0, Spring v6.1.8
09:45:32.562 [main] INFO  c.r.RuoYiApplication - [logStartupProfileInfo,660] - The following 1 profile is active: "druid"
09:45:33.308 [main] WARN  o.s.b.w.s.c.AnnotationConfigServletWebServerApplicationContext - [refresh,632] - Exception encountered during context initialization - cancelling refresh attempt: java.lang.IllegalArgumentException: Could not find class [org.mybatis.spring.boot.autoconfigure.MybatisAutoConfiguration]
09:45:33.329 [main] ERROR o.s.b.SpringApplication - [reportFailure,859] - Application run failed
java.lang.IllegalArgumentException: Could not find class [org.mybatis.spring.boot.autoconfigure.MybatisAutoConfiguration]
	at org.springframework.util.ClassUtils.resolveClassName(ClassUtils.java:355)
	at org.springframework.core.annotation.TypeMappedAnnotation.adapt(TypeMappedAnnotation.java:466)
	at org.springframework.core.annotation.TypeMappedAnnotation.getValue(TypeMappedAnnotation.java:391)
	at org.springframework.core.annotation.TypeMappedAnnotation.asMap(TypeMappedAnnotation.java:278)
	at org.springframework.core.annotation.AbstractMergedAnnotation.asAnnotationAttributes(AbstractMergedAnnotation.java:191)
	at org.springframework.context.annotation.AnnotationBeanNameGenerator.determineBeanNameFromAnnotation(AnnotationBeanNameGenerator.java:144)
	at org.springframework.context.annotation.AnnotationBeanNameGenerator.generateBeanName(AnnotationBeanNameGenerator.java:110)
	at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.registerBeanDefinitionForImportedConfigurationClass(ConfigurationClassBeanDefinitionReader.java:160)
	at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitionsForConfigurationClass(ConfigurationClassBeanDefinitionReader.java:141)
	at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitions(ConfigurationClassBeanDefinitionReader.java:120)
	at org.springframework.context.annotation.ConfigurationClassPostProcessor.processConfigBeanDefinitions(ConfigurationClassPostProcessor.java:429)
	at org.springframework.context.annotation.ConfigurationClassPostProcessor.postProcessBeanDefinitionRegistry(ConfigurationClassPostProcessor.java:290)
	at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanDefinitionRegistryPostProcessors(PostProcessorRegistrationDelegate.java:349)
	at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanFactoryPostProcessors(PostProcessorRegistrationDelegate.java:118)
	at org.springframework.context.support.AbstractApplicationContext.invokeBeanFactoryPostProcessors(AbstractApplicationContext.java:788)
	at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:606)
	at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146)
	at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:754)
	at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:456)
	at org.springframework.boot.SpringApplication.run(SpringApplication.java:335)
	at org.springframework.boot.SpringApplication.run(SpringApplication.java:1363)
	at org.springframework.boot.SpringApplication.run(SpringApplication.java:1352)
	at com.ruoyi.RuoYiApplication.main(RuoYiApplication.java:19)
Caused by: java.lang.ClassNotFoundException: org.mybatis.spring.boot.autoconfigure.MybatisAutoConfiguration
	at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641)
	at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188)
	at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:520)
	at java.base/java.lang.Class.forName0(Native Method)
	at java.base/java.lang.Class.forName(Class.java:467)
	at org.springframework.util.ClassUtils.forName(ClassUtils.java:304)
	at org.springframework.util.ClassUtils.resolveClassName(ClassUtils.java:345)
	... 22 common frames omitted
Disconnected from the target VM, address: '127.0.0.1:11595', transport: 'socket'

Process finished with exit code 1

```

造成这个错误的主要原因是jsqlparser这个东西被mybatis-plus提前接管了，所以在pagehelper就不应该再去接管了，所以这时要再启动类里边将pagehelper的自动配置排除掉。

```java
package com.ruoyi;

import com.github.pagehelper.autoconfigure.PageHelperAutoConfiguration;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

/**
 * 启动程序
 * 
 * @author ruoyi
 */
@SpringBootApplication(exclude = { DataSourceAutoConfiguration.class, PageHelperAutoConfiguration.class })
public class RuoYiApplication
{
    public static void main(String[] args)
    {
        // System.setProperty("spring.devtools.restart.enabled", "false");
        SpringApplication.run(RuoYiApplication.class, args);
        System.out.println("(♥◠‿◠)ﾉﾞ  若依启动成功   ლ(´ڡ`ლ)ﾞ  \n" +
                " .-------.       ____     __        \n" +
                " |  _ _   \\      \\   \\   /  /    \n" +
                " | ( ' )  |       \\  _. /  '       \n" +
                " |(_ o _) /        _( )_ .'         \n" +
                " | (_,_).' __  ___(_ o _)'          \n" +
                " |  |\\ \\  |  ||   |(_,_)'         \n" +
                " |  | \\ `'   /|   `-'  /           \n" +
                " |  |  \\    /  \\      /           \n" +
                " ''-'   `'-'    `-..-'              ");
    }
}
```

这时就可以启动项目了，然后尽情的CRUD了，但是本文的最终问题出现了，若依以前的分页就不好用了，因为将pagehelper的自动配置排除掉了，所以不好使也是再情理之中，但是问题也大概能猜到，就是再处理sql的时候并没有把预先应该拼接的分页sql拼上，但是项目中也并没有关于pagehelper的配置类，所以这个时我就想是不是再处理分页的时候就有问题，然后看BaseController里边处理了分页，但是由于使用mybatis-plus分页自带，所以以后的分页代码就不能是用pagehelper了，不管咋说还是人家自己的好用，所以这里做了个兼容，顺手的事情，在BaseController中增加这两个方法，这样就可以和pageHelper兼容了

```java
 public Page getPage() {
        PageDomain pageDomain = TableSupport.buildPageRequest();
        Page page = new Page();
        page.setCurrent(pageDomain.getPageNum());
        page.setSize(pageDomain.getPageSize());
        return page;
    }


    public TableDataInfo getDataTable(IPage iPage) {
        TableDataInfo rspData = new TableDataInfo();
        rspData.setCode(HttpStatus.SUCCESS);
        rspData.setRows(iPage.getRecords());
        rspData.setTotal(iPage.getTotal());
        return rspData;
    }
```

但是依旧不好使，这时我就找了经理问了这块应该咋办，网上也没有多少关于这块的问题的解答（PS：主要是我水平不行没查明白。。。）然后经理告诉我在mybatisplus的配置类里，将pagehelper的拦截器注入进来就行了，这时我才恍然大明白，既然项目里边没有分页的拦截器那就是自带了呀，注入进来就行了呀，这顿找啊

```java

    /**
     * 分页插件，自动识别数据库类型
     */
    @Bean
    public PageInterceptor pageInterceptor() {
        return new PageInterceptor();
    }
```

在mybatis-puls的配置类上加上这段，轻松秒杀，还是年轻，的学啊！！！！
