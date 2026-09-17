---
title: "Java + Vue + SpringBoot 抽签系统技术方案"
type: synthesis
tags: [Java, Vue, SpringBoot, 抽签, 系统设计]
sources: [wiki/index.md]
last_updated: 2026-09-17
---

# Java + Vue + SpringBoot 抽签系统技术方案

## 1. 系统架构设计

- **前端**：Vue 3 + Element Plus UI 组件库
- **后端**：SpringBoot 4 (基于 JDK 21) + Spring Security 7 + MyBatis-Plus
- **持久层**：MySQL + Redis (抽签计数/缓存)
- **部署**：Docker Compose

**关联连接**：[[SpringBoot]]、[[Vue3]]、 [[ElementPlus]]、 [[SpringSecurity]]

## 2. 核心业务流程

```
用户请求抽签
    ↓
1. 前端 Token 鉴权 (JWT + 双Token机制)
    ↓
2. 后端校验用户今日抽签次数 (Redis INCR)
    ↓
3. 判断是否中奖 (基于权重配置表)
    ↓
4. 扣除抽签次数，生成抽签记录
    ↓
5. 返回中奖结果 + 前端动画展示
```

**关联连接**：[[dual-token-mechanism]]、 [[rbac]]

## 3. 关键技术实现

### 后端 (Java/SpringBoot)

- **统一响应体**：`ResponseResult<T>` 泛型封装 (参考摘要-springboot脚手架搭建)
- **全局异常处理**：`@RestControllerAdvice` + `@ExceptionHandler` (同上)
- **抽签幂等性**：通过数据库唯一索引 + Redis 计数器防重 (参考摘要-重复提交问题)
- **Redis 计数**：`INCR` 每日重置，超时自动清零
- **权重抽签算法**：基于累积权重随机算法

### 前端 (Vue 3)

- **Axios 拦截器**：Token 自动从 Redis 黑名单检测并无感刷新 (参考摘要-springboot4-security7-vue3-best-practice)
- **v-permission 指令**：控制按钮权限显隐
- **Element Plus**：抽签弹窗、 loading 动画
- **Pinia**：管理用户抽签剩余次数状态

**关联连接**：[[Pinia]]、[[Axios]]、 [[JWT]]

## 4. 目录结构建议

```
project/
├─ springboot/
│  ├─ controller/   # 抽签接口
│  ├─ service/      # 抽签业务逻辑
│  ├─ mapper/       # MyBatis-Plus Mapper
│  ├─ entity/       # Award, DrawRecord entities
│  ├─ config/       # Redis配置, Security配置
│  └─ utils/        # 权重算法工具类
└─ vue/
   ├─ components/   # AwardDialog, DrawButton
   ├─ stores/       # Pinia store用户抽签状态
   └─ views/       # 抽签页
```

## 5. 数据库设计 (关键表)

```sql
-- 抽签配置表：奖项权重配置
CREATE TABLE award_config (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    weight INT NOT NULL DEFAULT 1,    -- 权重
    count INT NOT NULL DEFAULT 0,     -- 剩余次数
    status TINYINT DEFAULT 1          -- 1:启用 0:禁用
);

-- 抽签记录表
CREATE TABLE draw_record (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    user_id BIGINT NOT NULL,
    award_id BIGINT,
    status TINYINT,   -- 1:中奖 2:未中奖
    create_time DATETIME,
    CONSTRAINT uk_user_day UNIQUE KEY (user_id, DATE(create_time))
);
```

**关联连接**：[[MyBatisPlus]]