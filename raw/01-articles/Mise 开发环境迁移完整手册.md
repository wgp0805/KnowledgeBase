

> 适用系统：Windows 统一安装根目录：`D:\java\mise-software` npm 固定配置：prefix=`D:\java\npm-global`，cache=`D:\java\node_cache` 目标：使用 mise 统一管理 Java、Node、Maven、PHP 多版本，实现多项目环境隔离、自动切换，配套 IDEA 开发环境

## 目录

1. 项目背景与目标
2. 环境现状与目标工具清单
3. 核心概念澄清
4. 迁移前目录与环境变量规划
5. 迁移前置准备（保护 npm 全局包）
6. 旧环境清理（PATH、旧 SDK）
7. Mise 安装与环境变量配置
8. 工具安装实操 & 踩坑处理记录
9. Mise 基础使用教程
10. 多项目独立版本隔离方案（核心：项目自动切换）
11. PowerShell 自动激活配置（cd 进入目录自动加载 mise.toml）
12. IDEA 配置 JDK
13. IDEA 配置 Node & Npm
14. IDEA 配置 Maven
15. Mise 管理 PHP
16. Mise 管理 Maven
17. 保留 / 删除目录清单
18. Mise 高频命令速查表
19. 硬性避坑清单

---

## 1. 项目背景与目标

目标：淘汰 nvm、手动 JDK 切换等零散工具，**使用 mise 统一管理后端 Java、前端 Node、构建工具 Maven、脚本 PHP**。 实现效果：

- 项目 1：Java8 (Temurin8) + Node20.18.0
- 项目 2：Java17 + Node24.19.0 进入项目目录自动切换对应工具版本，退出目录自动恢复全局版本；IDEA 与终端环境保持同步。

## 2. 环境现状与目标工具清单

### 目标安装版本

- Java：`java@temurin-8.0.422`、`java@17`、`java@21.0.5`
- Node：`node@20.18.0`、`node@24.19.0`
- Maven：`maven@3.9.9`
- PHP：`vfox:version-fox/vfox-php@8.3`（需第三方插件）

### 目录规划

- mise 根目录：`D:\java\mise-software`
- 工具安装目录：`D:\java\mise-software\installs\`
- shims 代理目录：`D:\java\mise-software\shims\`
- npm 全局包：`D:\java\npm-global`
- npm 缓存目录：`D:\java\node_cache`

## 3. 核心概念澄清

1. **OpenJDK vs Eclipse Temurin** OpenJDK 是开源源码项目，不提供成品安装包。Eclipse Temurin 是 Eclipse Adoptium 组织，基于 OpenJDK 源码编译、测试、通过 Java 兼容性认证的发行版。本质就是 OpenJDK，免费商用，项目开发完全兼容。

> 其他 OpenJDK 发行版：Microsoft Build of OpenJDK、Amazon Corretto、RedHat OpenJDK。

2. **mise shims 代理机制** shims 是 mise 的代理程序，`D:\java\mise-software\shims\`下面的 java.exe/node.exe 不是真实程序，会转发到**当前 mise 激活的对应版本**。
    - 选`installs\xxx\node.exe`：固定版本，外部 mise 切换不影响
    - 选`shims\node.exe`：动态跟随 mise 当前激活版本
3. **版本优先级**：项目目录`mise.toml` > 全局 mise 版本

## 4. 迁移前目录与环境变量规划

1. 环境变量：`MISE_DATA_DIR=D:\java\mise-software`，所有下载的 SDK 全部存放在此目录
2. PATH 环境变量：只保留 mise 的 shims 目录 `D:\java\mise-software\shims`，**删除旧 JDK、nvm、手动 maven 等路径**，避免冲突。
3. npm 全局目录固定为`D:\java\npm-global`，切换 node 版本不改变这个路径。

## 5. 迁移前置准备（保护 npm 全局包）

> 重点：保留已安装的 npm 全局包，迁移后不用重装

```
# 导出当前全局包清单
npm ls -g --depth=0 > npm-global-list.txt
# 固定npm全局目录
npm config set prefix "D:\java\npm-global"
npm config set cache "D:\java\node_cache"
```

> ⚠️ 跨 Node 大版本切换：原生编译类全局包（node-gyp 等）需要重装，纯 JS 包不受影响。

## 6. 旧环境清理（PATH、旧 SDK）

1. Windows 系统环境变量 PATH 中，删除：旧 JDK、nvm、旧 node、旧 maven 的路径。
2. 保留：mise shims 路径。
3. 旧 nvm 目录：确认 mise 全部安装成功、验证正常后，再删除 nvm 文件夹。

> 清理原则：**先验证新环境可用，再删除旧环境**。

## 7. Mise 安装与环境变量配置

1. Windows 安装 mise，设置环境变量`MISE_DATA_DIR=D:\java\mise-software`
2. 将`D:\java\mise-software\shims`加入系统 PATH，放在靠前位置
3. 新开终端，验证：

```
mise --version
```

## 8. 工具安装实操 & 踩坑处理记录

### 8.1 Java 安装

> 踩坑：最初尝试`temurin@8.0.212`报错，mise 工具注册表里 java 格式为`java@temurin-版本`，不能单独写 temurin。

```
# 查询可用temurin8版本
mise ls-remote java@temurin-8
# 安装
mise install java@temurin-8.0.422
mise install java@17
mise install java@21.0.5
# 全局切换示例
mise use -g java@17
```

> IDEA 识别：Eclipse Temurin 就是 OpenJDK 发行版。

### 8.2 Node 安装

```
mise install node@20.18.0
mise install node@24.19.0
mise use -g node@20.18.0
```

### 8.3 Maven 安装

```
# 查询版本
mise ls-remote maven
# 安装
mise install maven@3.9.9
# 全局激活
mise use -g maven@3.9.9
```

### 8.4 PHP 安装（Windows 需要第三方 vfox 插件）

> Windows mise 原生不自带 PHP 注册表，需要安装 vfox 插件

```
# 仅执行一次，安装php插件
mise plugins install vfox:version-fox/vfox-php
# 查询版本
mise ls-remote vfox:version-fox/vfox-php
# 安装php8.3
mise install vfox:version-fox/vfox-php@8.3
# 全局激活
mise use -g vfox:version-fox/vfox-php@8.3
# 当前shell临时使用，关闭窗口失效
mise shell vfox:version-fox/vfox-php@8.3
```

> 注意：Windows 运行 PHP 需要 VC++ 运行库，缺少`vcruntime140.dll`需要安装微软 VC Redist x64。 安装 composer：`mise install composer`

### 8.5 手动导入已有 SDK（备用）

如果你本地已经解压好 SDK，可以交给 mise 托管

```
mise link java@8.0.211 D:\java\oracle-jdk8u211
mise link maven@3.8.8 D:\java\apache-maven-3.8.8
```

## 9. Mise 基础使用教程

### 查看命令

```
# 查看所有已安装工具
mise ls
# 查看某个工具可安装版本
mise ls-remote node
mise ls-remote java
mise ls-remote maven
# 查看当前激活版本
mise current
# 环境自检，排查问题
mise doctor
# 更新mise本体
mise self-update
```

### 版本切换

```
# 全局切换（所有终端生效）
mise use -g java@17
mise use -g node@20.18.0

# 项目本地切换（项目目录执行，写入mise.toml）
mise use java@17 node@24.19.0

# 仅当前终端临时生效，关闭窗口恢复
mise shell java@temurin-8.0.422
```

### 安装 / 卸载

```
mise install node@20.18.0
mise uninstall node@24.19.0
```

## 10. 多项目独立版本隔离方案（核心：项目自动切换）

> 需求：项目 1 使用 java8+node20；项目 2 使用 java17+node24 原理：项目根目录放置`mise.toml`，进入目录 mise 自动读取配置，离开目录恢复全局版本。

### 10.1 项目 1 配置（D:\java\project1）

```
cd D:\java\project1
mise use java@temurin-8.0.422 node@20.18.0
```

生成`mise.toml`：

```
[tools]
java = "temurin-8.0.422"
node = "20.18.0"
maven = "3.9.9"
# "vfox:version-fox/vfox-php" = "8.3"
```

### 10.2 项目 2 配置（D:\java\project2）

```
cd D:\java\project2
mise use java@17 node@24.19.0
```

生成`mise.toml`：

```
[tools]
java = "17"
node = "24.19.0"
maven = "3.9.9"
```

### 10.3 使用效果

1. `cd D:\java\project1` → java=temurin8，node=20.18.0
2. `cd D:\java\project2` → java=17，node=24.19.0
3. `cd D:\java` → 恢复全局 mise 版本

### 10.4 团队协作

`mise.toml`可以提交 Git。其他团队成员安装 mise，拉代码后进入项目目录执行`mise install`，自动安装所有依赖工具版本。

### 10.5 IDEA 配套两种方案

- **方案 A（固定版本，稳定，不自动切换）**：IDEA 解释器写死`installs`目录下的 exe。外部 mise 切换版本，**不会影响 IDEA**；更换项目版本需要手动修改 IDEA 设置。
- **方案 B（shim 动态联动，推荐自动切换场景）**：IDEA 解释器选择 shims 目录，进入项目 IDEA 自动跟随 mise.toml 切换版本。
    - JDK：`D:\java\mise-software\shims\java.exe`
    - Node：`D:\java\mise-software\shims\node.exe`
    - Maven Home：`D:\java\mise-software\shims`

> ⚠️ 坑：如果 IDEA 解释器固定版本，但是内置终端用 mise 自动切换，**会出现版本不一致**，编译和运行环境冲突。推荐两种选择：全部固定，或者全部使用 shim。

## 11. PowerShell 自动激活配置（cd 进入目录自动加载 mise.toml）

> 效果：cd 进入项目文件夹，自动读取 mise.toml 切换版本，无需手动执行任何 mise 命令。

### 11.1 打开 PowerShell 配置文件

```
# 查看profile路径
$PROFILE
# 文件不存在则新建
New-Item -ItemType File -Path $PROFILE -Force
# 使用记事本打开
notepad $PROFILE
```

### 11.2 脚本（二选一）

#### 方案 A：官方最简推荐（PowerShell5.1 / PowerShell7 都支持）

粘贴到 profile 文件：

```
# mise 自动激活：cd进入目录自动加载mise.toml
if ($env:MISE_SHELL -eq $null) {
    # 初始化mise
    & D:\java\mise-software\shims\mise activate powershell | Out-String | Invoke-Expression
}

# 目录切换钩子，每次cd之后自动重新检测mise.toml
function prompt {
    # 执行mise目录自动切换
    & mise hook-env -s powershell | Out-String | Invoke-Expression
    # 保留原有提示符（默认PS路径提示符，不要删除）
    "PS $($executionContext.SessionState.Path.GetLocation())> "
}
```

#### 方案 B：增强提示版（切换版本终端打印青色提示）

```
if ($env:MISE_SHELL -eq $null) {
    & D:\java\mise-software\shims\mise activate powershell | Out-String | Invoke-Expression
}

$global:LAST_MISE_ENV = $null
function prompt {
    $envOutput = & mise hook-env -s powershell 2>&1
    if ($LASTEXITCODE -eq 0 -and $envOutput) {
        Invoke-Expression $envOutput
        $currentMise = mise current
        if ($currentMise -ne $global:LAST_MISE_ENV) {
            Write-Host "`n✅ Mise 版本已切换：`n$currentMise`n" -ForegroundColor Cyan
            $global:LAST_MISE_ENV = $currentMise
        }
    }
    "PS $($executionContext.SessionState.Path.GetLocation())> "
}
```

### 11.3 Windows 执行策略（管理员 PowerShell 执行，必做）

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

输入`Y`确认。

### 11.4 测试

1. **全部关闭 PowerShell 窗口，重新新开终端**
2. cd 进入项目目录，自动切换版本，执行`java -version / node -v`验证。

### 11.5 IDEA 内置终端联动

1. `Ctrl+Alt+S` → Tools → Terminal
2. Shell path 保持`powershell.exe`
3. 勾选 **Shell integration**
4. 重启 IDEA。内置终端 cd 切换目录，同样自动触发 mise 版本切换。

### 11.6 故障排查

1. 禁止运行脚本：管理员 PowerShell 执行执行策略命令。
2. cd 不自动切换：关闭所有终端重开；确认`mise.toml`文件名正确（不是`mise.toml.txt`）；手动执行`mise hook-env -s powershell`测试。
3. IDEA 终端不生效：重启 IDEA，开启 Shell integration。

### 11.7 关闭自动激活

`notepad $PROFILE`，删除脚本内容，保存，重启 PowerShell。

## 12. IDEA 配置 JDK

打开 IDEA，File → Project Structure → Project SDK，点击`Add JDK from disk...`

> 截图中大量重复条目是 mise 创建的软链接，**不要选择 global/latest/xxx.0 后缀**，选择主目录。

表格

|项目 JDK 版本|选择文件夹路径|
|---|---|
|JDK8|`D:\java\mise-software\installs\java\temurin-8`|
|JDK17|`D:\java\mise-software\installs\java\17`|
|JDK21|`D:\java\mise-software\installs\java\21`|

- 固定版本模式：直接选上面 installs 目录。
- 自动跟随 mise 模式：`D:\java\mise-software\shims\java.exe`

> 注意：IDEA 的 SDK 是独立配置，**和终端的 java 环境是两套东西**，需要手动保持版本一致。

## 13. IDEA 配置 Node & Npm

快捷键`Ctrl+Alt+S` → Languages & Frameworks → Node.js and NPM 点击 Node interpreter 右侧`...` → Add Local，选中 node.exe

表格

|模式|node.exe 路径|说明|
|---|---|---|
|固定 node20|`D:\java\mise-software\installs\node\20.18.0\node.exe`|外部 mise 切换版本不影响 IDEA|
|固定 node24|`D:\java\mise-software\installs\node\24.19.0\node.exe`|外部 mise 切换版本不影响 IDEA|
|跟随 mise 自动切换|`D:\java\mise-software\shims\node.exe`|终端切换 mise 版本，IDEA 同步变化|

- Package manager：IDEA 自动识别同目录 npm.cmd，无需手动修改。
- 建议勾选`Coding assistance for Node.js`开启代码提示。
- npm 全局配置命令（切换 node 版本后执行一次）：

```
npm config set prefix "D:\java\npm-global"
npm config set cache "D:\java\node_cache"
```

> 坑点：IDEA 图形界面 Node 解释器 和 IDEA 内置终端是两套独立环境，版本可能不一致。想统一推荐 shim 模式。

## 14. IDEA 配置 Maven

IDEA 设置：Build, Execution, Deployment → Build Tools → Maven

- **固定版本**：Maven home path 填写`D:\java\mise-software\installs\maven\3.9.9`
- **shim 联动模式**：Maven home path 填写`D:\java\mise-software\shims`

> Maven Runner 的 JRE 需要单独配置，建议和项目 JDK 保持一致。 maven 本地仓库默认`C:\Users\w1217\.m2\repository`，不受 mise 管理，在 settings.xml 自定义仓库。

## 15. Mise 管理 PHP

```
# 安装插件（一次性）
mise plugins install vfox:version-fox/vfox-php
# 查询版本
mise ls-remote vfox:version-fox/vfox-php
# 安装php8.3
mise install vfox:version-fox/vfox-php@8.3
# 全局激活
mise use -g vfox:version-fox/vfox-php@8.3
# 项目mise.toml
[tools]
"vfox:version-fox/vfox-php" = "8.3"
```

IDEA PHP 解释器两种模式：

- 固定版本：`D:\java\mise-software\installs\vfox-version-fox-vfox-php\8.3\php.exe`
- shim 跟随模式：`D:\java\mise-software\shims\php.exe`

## 16. Mise 管理 Maven

```
# 查看可安装版本
mise ls-remote maven
# 安装
mise install maven@3.9.9
# 全局激活
mise use -g maven@3.9.9
# 项目目录激活，写入mise.toml
mise use maven@3.9.9
# 当前shell临时使用
mise shell maven@3.9.9
```

> maven 会自动继承 mise 当前激活的 JAVA_HOME，和 JDK 完美联动。

## 17. 保留 / 删除目录清单

✅ **保留，禁止删除**

1. `D:\java\mise-software` mise 所有工具存放目录
2. `D:\java\npm-global` npm 全局包目录
3. `D:\java\node_cache` npm 缓存目录

⚠️ 旧 nvm 目录：验证 mise 完全稳定后，再删除。

## 18. Mise 高频命令速查表

表格

|功能|命令|
|---|---|
|查看已安装工具|`mise ls`|
|查询可安装版本|`mise ls-remote 工具名`|
|安装工具|`mise install 工具@版本`|
|卸载工具|`mise uninstall 工具@版本`|
|全局切换版本|`mise use -g 工具@版本`|
|项目本地版本（写入 mise.toml）|`mise use 工具@版本`（项目目录执行）|
|当前终端临时使用版本|`mise shell 工具@版本`|
|查看当前生效版本|`mise current`|
|一键安装项目 mise.toml 里全部工具|`mise install`|
|环境诊断排查|`mise doctor`|
|更新 mise 本体|`mise self-update`|

## 19. 硬性避坑清单

1. **不要手动修改系统 PATH 来切换 JDK/Node**，全部交给 mise shims 管理。
2. `MISE_DATA_DIR`一旦确定，**不要后期修改**，修改后所有已下载 SDK 失效，需要全部重装。
3. 项目`mise.toml`优先级高于全局，进入项目目录自动覆盖全局版本。
4. Node 跨大版本切换，原生编译类 npm 全局包必须重装；纯 JS 包不受影响。
5. IDEA 解释器和终端环境是两套独立配置，要么全部固定版本，要么全部使用 shim，防止版本不一致。
6. Windows PHP 依赖 VC++ 运行库，缺少 dll 会无法启动 php。
7. PowerShell 自动激活脚本修改后，**必须完全关闭所有终端窗口**才会生效，仅新开 tab 不生效。
8. 不要同时启用 nvm、sdkman 等其他版本管理工具，会造成 PATH 冲突。