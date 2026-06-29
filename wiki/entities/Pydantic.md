---
title: "Pydantic"
type: entity
tags: [Python, 数据校验, 类型安全]
sources: [raw/01-articles/FastAPI 入门教程.md]
last_updated: 2026-06-29
---

## 定义
Python 生态中高性能的数据校验库，基于 Python 类型提示实现声明式数据建模与运行时验证。是 [[FastAPI]] 三引擎之一（数据验证引擎）。

## 关键信息

### 核心能力
- **BaseModel**：通过继承定义数据结构，字段写法即类型注解
- **Field 约束**：`min_length`、`max_length`、`ge`、`le`、`description` 等
- **专用类型**：`EmailStr`（自动校验邮箱）、`HttpUrl`、`SecretStr` 等
- **嵌套模型**：支持模型互相嵌套
- **额外属性检查**：未声明字段会被拒绝（可配置）

### 校验流程（FastAPI 中）
1. 请求到达 → 解析 JSON
2. 字段类型检查（如 `username: str` 传入非字符串立即拒绝）
3. 约束条件验证（长度、范围）
4. 嵌套模型验证
5. 不合格请求返回 **422 错误**，明确指出哪个字段失败及原因

这种"在门口就把不合格请求拦住"的设计，大大减少业务代码中的防御性判断。

### 典型用法
```python
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20)
    email: EmailStr = Field(..., description="邮箱地址")
    password: str = Field(..., min_length=8)
    age: Optional[int] = Field(None, ge=0, le=150)
    tags: list[str] = []
```

### 声明式编程
开发者只需声明"我要什么"，框架自动处理"怎么校验"。这种范式与 Java 的 JSR-303（Bean Validation） + Lombok 体验类似，但更彻底——类型注解既是文档也是校验规则。

### 学习成本
初学者需要适应 Model 模式（先定义类再用），相比 Flask 直接处理 dict 多一层心智负担，但换来代码可读性、IDE 自动补全和运行时安全。

## 关联连接
- [[摘要-fastapi-入门教程]] — 来源
- [[FastAPI]] — 主要使用方
- [[ASGI]] — 同生态
- [[Java]] — Bean Validation 是类比方案
