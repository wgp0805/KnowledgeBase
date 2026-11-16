---
source_url: "https://mp.weixin.qq.com/s/-C9_fHFirHlQxkwEfxB90A"
title: "SpringBoot + SpringBatch + Quartz整合定时批量任务"
account: "小哈学Java"
published_at: "2026-11-15 20:36:33"
saved_at: "2026-11-16 06:30:00"
sync_id: "art_8e08039b98f344c88e393f60660169cc"
parse_status: "ok"
---

# SpringBoot + SpringBatch + Quartz整合定时批量任务

将 **小哈学Java**** **设为“**星标****⭐**”

第一时间收到文章更新

![](assets/2026-11-15%20-%20SpringBoot%20+%20SpringBatch%20+%20Quartz%E6%95%B4%E5%90%88%E5%AE%9A%E6%97%B6%E6%89%B9%E9%87%8F%E4%BB%BB%E5%8A%A1/7b885168936cbe11e0ac2207c9a95f0d_MD5.png)

来源：https://blog.csdn.net/zxd1435513775/article/details/99677223

**在线 Java 面试刷题（已更新362题，25个分类，图文并茂）**：https://www.quanxiaoha.com/java-interview

**目录**

- 一、引言
- 二、代码具体实现
- 三、小结

### 一、引言

最近一周，被借调到其他部门，赶一个紧急需求，需求内容如下：

PC 网页触发一条设备升级记录（下图），后台要定时批量设备更新。这里定时要用到 Quartz，批量数据处理要用到 SpringBatch，二者结合，可以完成该需求。

由于之前，没有用过 SpringBatch，于是上网查了下资料，发现可参考的不是很多，于是只能去慢慢的翻看官方文档。

> **“**https://docs.spring.io/spring-batch/4.1.x/reference/html/

遇到不少问题，就记录一下吧。

![PC 网页触发的设备升级记录](assets/2026-11-15%20-%20SpringBoot%20+%20SpringBatch%20+%20Quartz%E6%95%B4%E5%90%88%E5%AE%9A%E6%97%B6%E6%89%B9%E9%87%8F%E4%BB%BB%E5%8A%A1/1ca1b45041bb5a5eae593a363f376b99_MD5.png)

PC 网页触发的设备升级记录

### 二、代码具体实现

1、pom文件

```
  <dependencies>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
      <groupId>org.postgresql</groupId>
      <artifactId>postgresql</artifactId>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-jdbc</artifactId>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-batch</artifactId>
    </dependency>
    <dependency>
      <groupId>org.projectlombok</groupId>
      <artifactId>lombok</artifactId>
    </dependency>
    <dependency>
      <groupId>org.springframework.boot</groupId>
      <artifactId>spring-boot-starter-batch</artifactId>
    </dependency>
   </dependencies>
```

2、application.yaml文件

```
spring:
  datasource:
    username: thinklink
    password: thinklink
    url: jdbc:postgresql://172.16.205.54:5432/thinklink
    driver-class-name: org.postgresql.Driver
  batch:
    job:
      enabled: false
server:
  port: 8073

#upgrade-dispatch-base-url: http://172.16.205.125:8080/api/rpc/dispatch/command/
upgrade-dispatch-base-url: http://172.16.205.211:8080/api/noauth/rpc/dispatch/command/

# 每次批量处理的数据量，默认为5000
batch-size: 5000
```

3、Service实现类，触发批处理任务的入口，执行一个job

```
@Service("batchService")
public class BatchServiceImpl implements BatchService {

 // 框架自动注入
    @Autowired
    private JobLauncher jobLauncher;
    @Autowired
    private Job updateDeviceJob;
    /**
     * 根据 taskId 创建一个Job
     * @param taskId
     * @throws Exception
     */
    @Override
    public void createBatchJob(String taskId) throws Exception {
        JobParameters jobParameters = new JobParametersBuilder()
                .addString("taskId", taskId)
                .addString("uuid", UUID.randomUUID().toString().replace("-",""))
                .toJobParameters();
        // 传入一个Job任务和任务需要的参数
        jobLauncher.run(updateDeviceJob, jobParameters);
    }
}
```

4、SpringBatch配置类，此部分最重要（☆☆☆☆☆）

```
@Configuration
public class BatchConfiguration {

    private static final Logger log = LoggerFactory.getLogger(BatchConfiguration.class);

    @Value("${batch-size:5000}")
    private int batchSize;

 // 框架自动注入
    @Autowired
    public JobBuilderFactory jobBuilderFactory;

 // 框架自动注入
    @Autowired
    public StepBuilderFactory stepBuilderFactory;

 // 数据过滤器，对从数据库读出来的数据，注意进行操作
    @Autowired
    public TaskItemProcessor taskItemProcessor;

    // 接收job参数
    public Map<String, JobParameter> parameters;

    public Object taskId;

    @Autowired
    private JdbcTemplate jdbcTemplate;

 // 读取数据库操作
    @Bean
    @StepScope
    public JdbcCursorItemReader<DispatchRequest> itemReader(DataSource dataSource) {

        String querySql = " SELECT " +
                " e. ID AS taskId, " +
                " e.user_id AS userId, " +
                " e.timing_startup AS startTime, " +
                " u.device_id AS deviceId, " +
                " d.app_name AS appName, " +
                " d.compose_file AS composeFile, " +
                " e.failure_retry AS failureRetry, " +
                " e.tetry_times AS retryTimes, " +
                " e.device_managered AS deviceManagered " +
                " FROM " +
                " eiot_upgrade_task e " +
                " LEFT JOIN eiot_upgrade_device u ON e. ID = u.upgrade_task_id " +
                " LEFT JOIN eiot_app_detail d ON e.app_id = d. ID " +
                " WHERE " +
                " ( " +
                " u.device_upgrade_status = 0 " +
                " OR u.device_upgrade_status = 2" +
                " )" +
                " AND e.tetry_times > u.retry_times " +
                " AND e. ID = ?";

        return new JdbcCursorItemReaderBuilder<DispatchRequest>()
                .name("itemReader")
                .sql(querySql)
                .dataSource(dataSource)
                .queryArguments(new Object[]{parameters.get("taskId").getValue()})
                .rowMapper(new DispatchRequest.DispatchRequestRowMapper())
                .build();
    }

 // 将结果写回数据库
    @Bean
    @StepScope
    public ItemWriter<ProcessResult> itemWriter() {
        return new ItemWriter<ProcessResult>() {

            private int updateTaskStatus(DispatchRequest dispatchRequest, int status) {
                log.info("update taskId: {}, deviceId: {} to status {}", dispatchRequest.getTaskId(), dispatchRequest.getDeviceId(), status);

                Integer retryTimes = jdbcTemplate.queryForObject(
                        "select retry_times from eiot_upgrade_device where device_id = ? and upgrade_task_id = ?",
                        new Object[]{ dispatchRequest.getDeviceId(), dispatchRequest.getTaskId()}, Integer.class
                );
                retryTimes += 1;
                int updateCount = jdbcTemplate.update("update eiot_upgrade_device set device_upgrade_status = ?, retry_times = ? " +
                        "where device_id = ? and upgrade_task_id = ?", status, retryTimes, dispatchRequest.getDeviceId(), dispatchRequest.getTaskId());
                if (updateCount <= 0) {
                    log.warn("no task updated");
                } else {
                    log.info("count of {} task updated", updateCount);
                }

                // 最后一次重试
                if (status == STATUS_DISPATCH_FAILED && retryTimes == dispatchRequest.getRetryTimes()) {
                    log.info("the last retry of {} failed, inc deviceManagered", dispatchRequest.getTaskId());
                    return 1;
                } else {
                    return 0;
                }
            }

            @Override
            @Transactional
            public void write(List<? extends ProcessResult> list) throws Exception {
                Map taskMap = jdbcTemplate.queryForMap(
                        "select device_managered, device_count, task_status from eiot_upgrade_task where id = ?",
                        list.get(0).getDispatchRequest().getTaskId() // 我们认定一个批量里面，taskId都是一样的
                        );
                int deviceManagered = (int)taskMap.get("device_managered");
                Integer deviceCount = (Integer) taskMap.get("device_count");
                if (deviceCount == null) {
                    log.warn("deviceCount of task {} is null", list.get(0).getDispatchRequest().getTaskId());
                }
                int taskStatus = (int)taskMap.get("task_status");
                for (ProcessResult result: list) {
                    deviceManagered += updateTaskStatus(result.getDispatchRequest(), result.getStatus());
                }
                if (deviceCount != null && deviceManagered == deviceCount) {
                    taskStatus = 2; //任务状态 0:待升级，1:升级中，2:已完成
                }
                jdbcTemplate.update("update eiot_upgrade_task  set device_managered = ?, task_status = ? " +
                        "where id = ?", deviceManagered, taskStatus, list.get(0).getDispatchRequest().getTaskId());
            }
        };
    }

    /**
     * 定义一个下发更新的 job
     * @return
     */
    @Bean
    public Job updateDeviceJob(Step updateDeviceStep) {
        return jobBuilderFactory.get(UUID.randomUUID().toString().replace("-", ""))
                .listener(new JobListener()) // 设置Job的监听器
                .flow(updateDeviceStep)// 执行下发更新的Step
                .end()
                .build();
    }

    /**
     * 定义一个下发更新的 step
     * @return
     */
    @Bean
    public Step updateDeviceStep(JdbcCursorItemReader<DispatchRequest> itemReader,ItemWriter<ProcessResult> itemWriter) {
        return stepBuilderFactory.get(UUID.randomUUID().toString().replace("-", ""))
                .<DispatchRequest, ProcessResult> chunk(batchSize)
                .reader(itemReader) //根据taskId从数据库读取更新设备信息
                .processor(taskItemProcessor) // 每条更新信息，执行下发更新接口
                .writer(itemWriter)
                .build();
    }

    // job 监听器
    public class JobListener implements JobExecutionListener {

        @Override
        public void beforeJob(JobExecution jobExecution) {
            log.info(jobExecution.getJobInstance().getJobName() + " before... ");
            parameters = jobExecution.getJobParameters().getParameters();
            taskId = parameters.get("taskId").getValue();
            log.info("job param taskId : " + parameters.get("taskId"));
        }

        @Override
        public void afterJob(JobExecution jobExecution) {

            log.info(jobExecution.getJobInstance().getJobName() + " after... ");
            // 当所有job执行完之后，查询设备更新状态，如果有失败，则要定时重新执行job
            String sql = " SELECT " +
                    " count(*) " +
                    " FROM " +
                    " eiot_upgrade_device d " +
                    " LEFT JOIN eiot_upgrade_task u ON d.upgrade_task_id = u. ID " +
                    " WHERE " +
                    " u. ID = ? " +
                    " AND d.retry_times < u.tetry_times " +
                    " AND ( " +
                    " d.device_upgrade_status = 0 " +
                    " OR d.device_upgrade_status = 2 " +
                    " ) ";

            // 获取更新失败的设备个数
            Integer count = jdbcTemplate.queryForObject(sql, new Object[]{taskId}, Integer.class);

            log.info("update device failure count : " + count);

            // 下面是使用Quartz触发定时任务
            // 获取任务时间,单位秒
//            String time = jdbcTemplate.queryForObject(sql, new Object[]{taskId}, Integer.class);
            // 此处方便测试，应该从数据库中取taskId对应的重试间隔，单位秒
            Integer millSecond = 10;

            if(count != null && count > 0){
                String jobName = "UpgradeTask_" + taskId;
                String reTaskId = taskId.toString();
                Map<String,Object> params = new HashMap<>();
                params.put("jobName",jobName);
                params.put("taskId",reTaskId);
                if (QuartzManager.checkNameNotExist(jobName))
                {
                    QuartzManager.scheduleRunOnceJob(jobName, RunOnceJobLogic.class,params,millSecond);
                }
            }

        }
    }
}
```

5、Processor，处理每条数据，可以在此对数据进行过滤操作

```
@Component("taskItemProcessor")
public class TaskItemProcessor implements ItemProcessor<DispatchRequest, ProcessResult> {

    public static final int STATUS_DISPATCH_FAILED = 2;
    public static final int STATUS_DISPATCH_SUCC = 1;

    private static final Logger log = LoggerFactory.getLogger(TaskItemProcessor.class);

    @Value("${upgrade-dispatch-base-url:http://localhost/api/v2/rpc/dispatch/command/}")
    private String dispatchUrl;

    @Autowired
    JdbcTemplate jdbcTemplate;

    /**
     * 在这里，执行 下发更新指令 的操作
     * @param dispatchRequest
     * @return
     * @throws Exception
     */
    @Override
    public ProcessResult process(final DispatchRequest dispatchRequest) {
        // 调用接口，下发指令
        String url = dispatchUrl + dispatchRequest.getDeviceId()+"/"+dispatchRequest.getUserId();

        log.info("request url:" + url);
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON_UTF8);

        MultiValueMap<String, String> params = new LinkedMultiValueMap<String, String>();

        JSONObject jsonOuter = new JSONObject();
        JSONObject jsonInner = new JSONObject();
        try {
            jsonInner.put("jobId",dispatchRequest.getTaskId());
            jsonInner.put("name",dispatchRequest.getName());
            jsonInner.put("composeFile", Base64Util.bytesToBase64Str(dispatchRequest.getComposeFile()));
            jsonInner.put("policy",new JSONObject().put("startTime",dispatchRequest.getPolicy()));
            jsonInner.put("timestamp",dispatchRequest.getTimestamp());

            jsonOuter.put("method","updateApp");
            jsonOuter.put("params",jsonInner);
        } catch (JSONException e) {
            log.info("JSON convert Exception :" + e);
        }catch (IOException e) {
            log.info("Base64Util bytesToBase64Str :" + e);
        }

        log.info("request body json :" + jsonOuter);
        HttpEntity<String> requestEntity = new HttpEntity<String>(jsonOuter.toString(),headers);
        int status;
        try {
            ResponseEntity<String> response = restTemplate.postForEntity(url,requestEntity,String.class);
            log.info("response :" + response);
            if (response.getStatusCode() == HttpStatus.OK) {
                status = STATUS_DISPATCH_SUCC;
            } else {
                status = STATUS_DISPATCH_FAILED;
            }

        }catch (Exception e){
            status = STATUS_DISPATCH_FAILED;
        }

        return new ProcessResult(dispatchRequest, status);
    }
}
```

6、封装数据库返回数据的实体Bean，注意静态内部类

```
public class DispatchRequest {

    private String taskId;
    private String deviceId;
    private String userId;
    private String name;
    private byte[] composeFile;
    private String policy;
    private String timestamp;
    private String md5;
    private int failureRetry;
    private int retryTimes;
    private int deviceManagered;

   // 省略构造函数，setter/getter/tostring方法
   //......

    public static class DispatchRequestRowMapper implements RowMapper<DispatchRequest> {
        @Override
        public DispatchRequest mapRow(ResultSet resultSet, int i) throws SQLException {

            DispatchRequest dispatchRequest = new DispatchRequest();
            dispatchRequest.setTaskId(resultSet.getString("taskId"));
            dispatchRequest.setUserId(resultSet.getString("userId"));
            dispatchRequest.setPolicy(resultSet.getString("startTime"));
            dispatchRequest.setDeviceId(resultSet.getString("deviceId"));
            dispatchRequest.setName(resultSet.getString("appName"));
            dispatchRequest.setComposeFile(resultSet.getBytes("composeFile"));
            dispatchRequest.setTimestamp(DateUtil.DateToString(new Date()));
            dispatchRequest.setRetryTimes(resultSet.getInt("retryTimes"));
            dispatchRequest.setFailureRetry(resultSet.getInt("failureRetry"));
            dispatchRequest.setDeviceManagered(resultSet.getInt("deviceManagered"));
            return dispatchRequest;
        }
    }
}
```

7、启动类上要加上注解

```
@SpringBootApplication
@EnableBatchProcessing
public class Application {

    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

### 三、小结

其实 SpringBatch 并没有想象中那么好用，当从数据库中每次取 5000 条数据后，进入 processor 中是逐条处理的，这个时候不能不行操作，等 5000 条数据处理完之后，再一次性执行 ItemWriter 方法。

在使用的过程中，最坑的地方是 ItemReader 和 ItemWriter 这两个地方，如何执行自定义的 Sql，参考文中代码就行。

至于 Quartz 定时功能，很简单，只要定时创建 SpringBatch 里面的 Job，让这个 job 启动就好了，此处就不在给出了，贴的代码太多了。由于公司一些原因，代码不能放到 GitHub 上。

[加入小哈的星球](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)，你将获得: **专属的项目实战（4个项目） / 1v1 提问 / 简历修改 / Java 学习路线 / **社群讨论 / **学习打卡 / 每月赠书**

- 《仿小红书（微服务架构 ）》 已完结，基于 Spring Cloud Alibaba + Spring Boot 3.x + JDK 17..., [点击查看项目介绍](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247538491&idx=1&sn=576995017721766d0fe15723fd135619&chksm=fd5787bdca200eab54d2fb8ca07fcc2bffdec3eaab4ab82ab5eaf949f0254c1683455e02010b&token=343952052&lang=zh_CN&scene=21#wechat_redirect) ； 演示地址： http://116.62.199.48:7070/
- 《 Spring AI 应用（RAG 智能客服） 》已完结, 基于 Spring AI 2.x + Spring Boot 4.x + JDK 21
- 《 秒杀系统设计 》正在更新中，单体到微服务高并发架构演进

- 《 前后端分离博客项目（全栈开发） 》 已完结,演示链接： http://116.62.199.48/
- 项目阅读地址： https://quanxiaoha.com/column

截止目前，**累计输出 150w+ 字，讲解图 4013+ 张，还在持续爆肝中..** [戳我加入学习，解锁全部项目，已有4900+小伙伴加入](https://mp.weixin.qq.com/s?__biz=MzU4MDUyMDQyNQ==&mid=2247566317&idx=1&sn=ede64496766addace122dd32f6cfbdcf&scene=21#wechat_redirect)

![图片](assets/2026-11-15%20-%20SpringBoot%20+%20SpringBatch%20+%20Quartz%E6%95%B4%E5%90%88%E5%AE%9A%E6%97%B6%E6%89%B9%E9%87%8F%E4%BB%BB%E5%8A%A1/df95f03fcf108bf41e98f713f22df8c0_MD5.gif)

![图片](assets/2026-11-15%20-%20SpringBoot%20+%20SpringBatch%20+%20Quartz%E6%95%B4%E5%90%88%E5%AE%9A%E6%97%B6%E6%89%B9%E9%87%8F%E4%BB%BB%E5%8A%A1/b01fd91d58faf9455f8fbb5c64bb22f0_MD5.webp)

```
1. 我的私密学习小圈子，从0到1手撸企业实战项目~
2. SpringBoot+Doris Stream Load 海量数据实时更新方案！
3. 比 Xshell 还好用的 SSH 客户端神器，MobaXterm 太爱了！
4. 面试官：介绍一下 Kafka 的 ISR 机制？
```

```

```

```
最近面试BAT，整理一份面试资料《Java面试BATJ通关手册》，覆盖了Java核心技术、JVM、Java并发、SSM、微服务、数据库、数据结构等等。
获取方式：点“在看”，关注公众号并回复 Java 领取，更多内容陆续奉上。
```

```
PS：因公众号平台更改了推送规则，如果不想错过内容，记得读完点一下“在看”，加个“星标”，这样每次新文章推送才会第一时间出现在你的订阅列表里。
点“在看”支持小哈呀，谢谢啦
```

---
原文链接：https://mp.weixin.qq.com/s/-C9_fHFirHlQxkwEfxB90A
