---
title: Orcale创建用户和表空间授权过程
tags:
  - Orcale
categories:
  - Orcale
date: 2022-05-28 17:37:51
---
### Orcale创建用户之前要先创建表空间
```sql
//创建表空间
create tablespace 表空间名 datafile '表空间路径\表空间名.dbf'' size 1000m;

//创建用户
create user 用户名 identified by 密码 default tablespace 表空间名 quota 500m on users;

//给用户授权
grant all privileges to 用户名;
```
除了上方还有分别授权的方法
```sql
授权
grant create session to 用户名;
grant create table to  用户名;
grant create tablespace to  用户名;
grant create view to  用户名;
```
### Oralce的特殊权限
1. 系统权限unlimited tablespace是隐含在dba, resource角色中的一个系统权限. 当用户得到dba或resource的角色时, unlimited tablespace系统权限也隐式受权给用户.

2. 系统权限unlimited tablespace不能被授予role, 可以被授予用户.

3. 系统权限unlimited tablespace不会随着resource, dba被授予role而授予给用户
### 特殊角色
1. DBA角色，是授权数据库管理员的权限

2. CONNECT角色， 是授予最终用户的典型权利，最基本的 一个（CREATE SESSION）

3. RESOURCE角色，是授予开发人员的 默认有八个权限（CREATE SEQUENCE,CREATE TRIGGER,CREATE CLUSTER,CREATE PROCEDURE,CREATE TYPE,CREATE OPERATOR,CREATE TABLE,CREATE INDEXTYPE）

4. exp_full_database角色，拥有导出数据库的权限

5. imp_full_database角色，拥有导入数据库的权限
### 用户授权示
```sql
--授权
GRANT
CONNECT,                
RESOURCE,               
--DBA,                  
--unlimited tablespace,
CREATE  SESSION,         
CREATE ANY SEQUENCE,     
CREATE ANY TABLE,        
CREATE ANY VIEW ,        
CREATE ANY INDEX,        
CREATE ANY PROCEDURE,    
CREATE ANY DIRECTORY,    
ALTER  SESSION, 
ALTER ANY SEQUENCE,     
ALTER ANY TABLE,        
--ALTER ANY VIEW ,        --不能修改视图
ALTER ANY INDEX,        
ALTER ANY PROCEDURE,    
--ALTER ANY DIRECTORY,    --不能修改目录
--DROP  SESSION,       --不能删除Session
DROP ANY SEQUENCE,     
DROP ANY TABLE,        
DROP ANY VIEW ,        
DROP ANY INDEX,        
DROP ANY PROCEDURE,    
DROP ANY DIRECTORY,    
SELECT ANY TABLE, 
SELECT ANY DICTIONARY,
INSERT ANY TABLE, 
UPDATE ANY TABLE, 
DELETE ANY TABLE,
DEBUG ANY PROCEDURE,
DEBUG CONNECT SESSION,
exp_full_database,  
imp_full_database     
TO xcj01;
```
#### 修改密码：
```sql
alter user xcj01
identified by xcj01;
```
#### 删除用户以及跟用户关联的对象：
```sql
drop user xcj01 CASCADE;
```
#### 查询用户权限和角色
```sql
select * from dba_role_privs a where a.grantee='XCJ01';
--或
select * from dba_sys_privs a where a.grantee='XCJ01';
```
#### 查看用户拥有哪些权限

```sql
select ROLE, PRIVILEGE from role_sys_privs where role='RESOURCE';   --RESOURCE，CONNECT，DBA
--或 
select grantee,privilege from dba_sys_privs where grantee='RESOURCE';
```
#### 为用户取消角色
```sql 
revoke resource from XCJ01;
```
#### 为用户取消权限

```sql
revoke unlimited tablespace from XCJ01;
```
#### 最后附加一个非常有用的技巧：查看Oracle的版本号。
```sql
select * from v$version where rownum <=1; 
```
#### orcale更改表空间名称
```sql
alter tablespace 原空间名 rename to 新空间名;


-- 查询全部表空间名
select name from v$tablespace;
```
#### 查看表空间路径
```sql 
select file_name , tablespace_name from dba_data_files;
select * from dba_data_files;
```