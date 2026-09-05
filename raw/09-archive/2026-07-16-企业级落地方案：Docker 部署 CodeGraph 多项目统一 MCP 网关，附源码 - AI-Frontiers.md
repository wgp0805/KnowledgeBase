---
title: "企业级落地方案：Docker 部署 CodeGraph 多项目统一 MCP 网关，附源码 - AI-Frontiers"
source: "博客园"
url: "https://www.cnblogs.com/aifrontiers/p/21546653"
date: "2026-07-16T08:06:00Z"
score: 0.6
tags: ["编程", "中文", "技术"]
auto_captured: true
---

# 企业级落地方案：Docker 部署 CodeGraph 多项目统一 MCP 网关，附源码 - AI-Frontiers

> **来源**: 博客园  
> **链接**: https://www.cnblogs.com/aifrontiers/p/21546653  
> **抓取日期**: 2026-07-16  
> **相关性评分**: 0.6

原文：<https://mp.weixin.qq.com/s/9hZHi9F4Kscou8CaHhFNEg>

很多人研发、产品会有这样的需求，需要频繁在多个代码仓库间切换以检索函数定义、类继承关系等语义信息。现有工具缺乏统一的知识库接入层，每个项目需独立部署 CodeGraph MCP 服务，端口管理混乱且难以维护。

本篇给大家分享近期的项目实战经验，实现开箱即用的多项目知识库统一访问能力。即，将一个父级目录下的多个项目批量构建 CodeGraph 知识库，并通过一个 Docker 容器、一个对外端口提供远程 MCP 访问。最终访问形态

  * [http://远程机器:8000/project-a/mcp](<http://xn--m7r540b49njsu:8000/project-a/mcp>)
  * [http://远程机器:8000/project-b/mcp](<http://xn--m7r540b49njsu:8000/project-b/mcp>)
  * [http://远程机器:8000/project-c/mcp](<http://xn--m7r540b49njsu:8000/project-c/mcp>)



话不多说，开整。

  * github地址： <https://github.com/dora-wang-x/codegraph-mcp-gateway>



# 安装 CodeGraph CLI

  * **去官网地址下载离线安装包**



<https://github.com/colbymchenry/codegraph/releases#release-v1.4.0>

  * **从本地拷贝下载文件到服务器**


    
    
    scp codegraph-linux-x64.tar.gz username@ip_address:/home/.../Projects/codegraph_ide
    

  * **Linux系统下执行操作**  
新建 `install-codegraph.sh`


    
    
    #!/bin/bash
    VERSION=v1.4.0
    INSTALL_DIR="$HOME/.codegraph"
    BIN_DIR="$HOME/.local/bin"
    
    # 创建目录
    mkdir -p "$INSTALL_DIR/versions/$VERSION"
    mkdir -p "$BIN_DIR"
    
    # 解压
    tar -xzf codegraph-linux-x64-v1.4.0.tar.gz \
      -C "$INSTALL_DIR/versions/$VERSION" \
      --strip-components=1
    
    # 创建版本软链接 + 全局命令
    ln -sfn "$INSTALL_DIR/versions/$VERSION" "$INSTALL_DIR/current"
    ln -sf "$INSTALL_DIR/current/bin/codegraph" "$BIN_DIR/codegraph"
    
    # 检查并添加PATH（不存在才写入bashrc）
    if ! echo "$PATH" | grep -q "$HOME/.local/bin"; then
      echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
      echo "已向 ~/.bashrc 添加 PATH"
    fi
    
    echo "安装完成！执行 source ~/.bashrc 或重启终端后运行 codegraph"
    

执行以下指令
    
    
    chmod +x install-codegraph.sh
    ./install-codegraph.sh
    

验证安装
    
    
    source ~/.bashrc
    codegraph --version
    

  * **验证**


    
    
    which codegraph
    codegraph --version
    codegraph --help
    

# 构建docker离线镜像

现在使用的 `@colbymchenry/codegraph`（npm 版本）**原生只有 stdio 模式** ，**不自带 HTTP / SSE / TCP 远程监听参数** ，这里采用 **mcp-remote 桥接（stdio → HTTP）** 方式，更适合生成环境。这里默认系统已安装npm包。

项目github地址 <https://github.com/dora-wang-x/codegraph-mcp-gateway>

构建docker离线镜像的目录结构
    
    
    docker/
      .env
      batch_codegraph_init.sh
      codegraph.Dockerfile
      multi_project_gateway.js
    codegraph-linux-x64-v1.4.0.tar.gz
    install-codegraph.sh
    README.md
    

**说明：**

  * `docker/.env`：保存构建和运行变量。
  * `docker/batch_codegraph_init.sh`：扫描项目集合目录下一级子目录，逐个执行 `codegraph init`。
  * `docker/codegraph.Dockerfile`：构建 CodeGraph MCP 远程服务镜像。
  * `docker/multi_project_gateway.js`：扫描已初始化项目，为每个项目启动内部 `supergateway`，并暴露统一 HTTP 入口。
  * `codegraph-linux-x64-v1.4.0.tar.gz`：CodeGraph Linux x64 离线包，放在仓库根目录作为 Docker build context 的一部分。
  * `install-codegraph.sh`：在服务端安装 codegraph-linux-x64-v1.4.0.tar.gz 脚本
  * `README.md`：介绍项目目标，安装步骤



## 工作方式

  * **服务端项目集合目录** ：


    
    
    /srv/projects/
      project-a/
      project-b/
      project-c/
    

  * **容器内挂载为** ：


    
    
    /workspace/projects/
      project-a/
      project-b/
      project-c/
    

  * **批量初始化后** ：



通过batch_codegraph_init.sh脚本批量构建代码知识库
    
    
    /workspace/projects/project-a/.codegraph/codegraph.db
    /workspace/projects/project-b/.codegraph/codegraph.db
    /workspace/projects/project-c/.codegraph/codegraph.db
    

  * **容器启动时，`docker/multi_project_gateway.js` 会**： 
    * 扫描 `CONTAINER_PROJECTS_PATH` 下一级子目录。
    * 默认只服务存在 `.codegraph/codegraph.db` 的项目。
    * 为每个项目分配内部端口，例如 `9100`、`9101`、`9102`。
    * 启动内部 `supergateway`。
    * 在 `MCP_PORT` 上暴露统一入口。
  * **实际部署前`.env` 文件通常只需要改**： 
    * `HOST_PROJECTS_PATH`：离线服务器上的项目集合目录。
    * `HOST_PORT`：对外暴露端口。



# 在线环境构建镜像

  * **在仓库根目录执行:**

Linux/macOS shell：



    
    
    set -a
    . docker/.env
    set +a
    
    docker build \
      -f docker/codegraph.Dockerfile \
      --build-arg NODE_IMAGE="${NODE_IMAGE}" \
      --build-arg APT_MIRROR_BASE="${APT_MIRROR_BASE}" \
      --build-arg CODEGRAPH_VERSION="${CODEGRAPH_VERSION}" \
      --build-arg CODEGRAPH_ARCHIVE="${CODEGRAPH_ARCHIVE}" \
      --build-arg SUPERGATEWAY_VERSION="${SUPERGATEWAY_VERSION}" \
      -t "${IMAGE_NAME}:${IMAGE_TAG}" \
      .
    

Windows PowerShell：
    
    
    Get-Content .\docker\.env | Where-Object { $_ -and $_ -notmatch '^#' } | ForEach-Object {
      $k, $v = $_ -split '=', 2
      Set-Item -Path "Env:$k" -Value $v
    }
    
    docker build `
      -f .\docker\codegraph.Dockerfile `
      --build-arg NODE_IMAGE="$env:NODE_IMAGE" `
      --build-arg APT_MIRROR_BASE="$env:APT_MIRROR_BASE" `
      --build-arg CODEGRAPH_VERSION="$env:CODEGRAPH_VERSION" `
      --build-arg CODEGRAPH_ARCHIVE="$env:CODEGRAPH_ARCHIVE" `
      --build-arg SUPERGATEWAY_VERSION="$env:SUPERGATEWAY_VERSION" `
      -t "$env:IMAGE_NAME`:$env:IMAGE_TAG" `
      .
    

  * **导出镜像** ：

Linux/macOS shell：



    
    
    docker save "${IMAGE_NAME}:${IMAGE_TAG}" -o "${IMAGE_TAR}"
    

Windows PowerShell：
    
    
    docker save "$env:IMAGE_NAME`:$env:IMAGE_TAG" -o "$env:IMAGE_TAR"
    

# 离线环境加载并运行

  * **加载镜像** ：



在执行以下指令之前，需要将 .env文件中的`HOST_PROJECTS_PATH`变量改为真实的项目路径
    
    
    set -a
    . docker/.env
    set +a
    
    docker load -i "${IMAGE_TAR}"
    

  * **运行容器** ：


    
    
    docker run -d \
      --name "${CONTAINER_NAME}" \
      --env-file docker/.env \
      -p "${HOST_PORT}:${MCP_PORT}" \
      -v "${HOST_PROJECTS_PATH}:${CONTAINER_PROJECTS_PATH}" \
      --restart unless-stopped \
      "${IMAGE_NAME}:${IMAGE_TAG}"
    

## 初始化 CodeGraph 索引

容器启动后，对所有一级子项目批量初始化：
    
    
    docker exec -it "${CONTAINER_NAME}" batch_codegraph_init.sh "${CONTAINER_PROJECTS_PATH}"
    

初始化完成后重启容器，让前置网关重新扫描已初始化项目，**一定要执行这步** ：
    
    
    docker restart "${CONTAINER_NAME}"
    

单个项目也可以手动初始化：
    
    
    docker exec -it "${CONTAINER_NAME}" codegraph init "${CONTAINER_PROJECTS_PATH}/project-a"
    

检查状态：
    
    
    docker exec -it "${CONTAINER_NAME}" codegraph status "${CONTAINER_PROJECTS_PATH}/project-a"
    

测试查询：
    
    
    docker exec -it "${CONTAINER_NAME}" codegraph explore "某个函数名或你的问题" --path "${CONTAINER_PROJECTS_PATH}/project-a"
    

## 远程访问验证

检查统一网关：
    
    
    curl "http://远程机器:${HOST_PORT}${HEALTH_ENDPOINT}"
    

查看项目映射：
    
    
    curl "http://远程机器:${HOST_PORT}/projects"
    

检查某个项目后端：
    
    
    curl "http://远程机器:${HOST_PORT}/project-a/healthz"
    

# **OpenClaud/Opencode远程MCP配置**

假设远程服务端有以下几个项目
    
    
    /home/dora/Desktop/Projects/git_rep/
    ├── ragflow/         
    ├── openclaude/       
    ├── codegraph-mcp-gateway/    
    

下面分别给出OpenClaud/Opencode MCP配置示例

OpenClaud：
    
    
    {
      "permissions": {
        "allow": [     
          "mcp__codegraph-codegraph-mcp-gateway__codegraph_explore",
          "mcp__codegraph-codegraph-mcp-gateway__*",
          "mcp__codegraph-openclaude__codegraph_explore",
          "mcp__codegraph-openclaude__*",
          "mcp__codegraph-ragflow__codegraph_explore",
          "mcp__codegraph-ragflow__*"
        ]
      },
      "hooks": {
        "UserPromptSubmit": [
          {
            "hooks": [
              {
                "type": "command",
                "command": "codegraph prompt-hook"
              }
            ]
          }
        ]
      },
      "mcpServers": {
        "codegraph-ragflow": {
          "type": "http",
          "url": "http://192.168.220.128:8000/ragflow/mcp",
          "enabled": true
        },
        "codegraph-openclaude": {
          "type": "http",
          "url": "http://192.168.220.128:8000/openclaude/mcp",
          "enabled": true
        },
        "codegraph-codegraph-mcp-gateway": {
          "type": "http",
          "url": "http://192.168.220.128:8000/codegraph-mcp-gateway/mcp",
          "enabled": true
        }
      }
    }
    
    

Opencode：
    
    
    {
      "$schema": "https://opencode.ai/config.json",
      "model": "deepseek-ai/DeepSeek-V4-Pro",
      "provider": {
        ......
      },
      "mcp": {
        "codegraph-openclaude": {
          "type": "remote",
          "url": "http://192.168.220.128:8000/openclaude/mcp",
          "enabled": true
        },
        "codegraph-ragflow": {
          "type": "remote",
          "url": "http://192.168.220.128:8000/ragflow/mcp",
          "enabled": true
        },
        "codegraph-codegraph-mcp-gateway": {
          "type": "remote",
          "url": "http://192.168.220.128:8000/codegraph-mcp-gateway/mcp",
          "enabled": true
        }
      },
      "tools": {
        "mcp__codegraph-codegraph-mcp-gateway*": true,
        "mcp__codegraph-openclaude__*": true,
        "mcp__codegraph-ragflow__*": true
      }
    }
    
    

OpenClaud CLAUDE.md 和 Opencode AGENTS.md路由规则，这里两个文件内容配置的完全相同
    
    
    # CodeGraph 强制使用规则
    
    当用户问题涉及以下任一场景时，必须先使用 CodeGraph，再回答, 优先使用远程 MCP 工具：
    - 查找函数、类、变量、接口、配置项的定义
    - 分析调用链、依赖关系、数据流
    - 解释某个项目/模块/功能的实现
    - 定位 bug、修改代码、评审代码
    - 询问“在哪里实现”“怎么调用”“谁调用了它”
    
    禁止在完成 CodeGraph 初查前使用 grep、read、逐文件扫描来寻找符号或调用关系。
    
    ## 查询规则：
    1. 先用较小范围查询，不要一次塞入大量关键词。
    2. 每次 `codegraph_explore` 优先聚焦一个模块、文件或功能点。
    3. `maxFiles` 优先使用 3 到 6，只有结果不足时再提高。
    4. 如果 MCP 返回超时，缩小查询范围后重试。
    
    ## 项目索引映射
    
    | 项目 | 路径 | CodeGraph 索引名 | 触发词 |
    |---|---|---|---|
    | codegraph-mcp-gateway | http://192.168.220.128:8000/codegraph-mcp-gateway/mcp | codegraph-mcp-gateway | codegraph-mcp-gateway, 项目规划 |
    | openclaude | http://192.168.220.128:8000/openclaude/mcp | openclaude | openclaude |
    | ragflow | http://192.168.220.128:8000/ragflow/mcp | ragflow | ragflow |
    
    ## 路由优先级
    
    1. 如果用户给出了文件路径或当前工作目录，按路径选择索引。
    2. 如果用户明确提到项目名，按项目名选择索引。
    3. 如果只出现通用词，例如 RAG、检索、agent、工具调用，不要仅凭该词选择索引；应根据上下文判断，无法判断时先询问用户。
    4. 不要把 `rag` 作为 openclaude 和 ragflow 的共同触发词。
    
    ## 执行流程
    
    1. 先判断是否是代码理解/定位/调用链类问题。
    2. 选择唯一 CodeGraph 索引。
    3. 调用 `codegraph_search` 查找相关符号或文件。
    4. 只有在搜索结果需要展开时，才调用 `codegraph_explore` 或委托 Explore 子代理。
    5. 如果 CodeGraph 无结果，说明已检索失败，再使用 grep/read 作为兜底。
    6. 回答时说明使用了哪个索引。
    

**参考资料**

**CodeGraph + Claude Code 图知识库实战，让 AI 编程效率翻倍**


---
> 原文链接: https://www.cnblogs.com/aifrontiers/p/21546653