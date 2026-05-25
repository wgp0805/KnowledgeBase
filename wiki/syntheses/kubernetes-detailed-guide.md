---
title: "kubernetes-detailed-guide"
type: synthesis
tags: [容器, 编排, DevOps, 微服务, K8s, 教程]
sources: []
last_updated: 2026-05-25
---

# Kubernetes 详细教程与注意事项

## 一、架构详解

### 1.1 整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                      Kubernetes 集群                         │
├─────────────────────────────────────────────────────────────┤
│  Master 节点 (控制平面)                                       │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌────────┐ │
│  │ API Server  │ │ Scheduler   │ │ Controller  │ │ etcd   │ │
│  │ (集群入口)   │ │ (调度器)    │ │ Manager     │ │ (存储)  │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └────────┘ │
├─────────────────────────────────────────────────────────────┤
│  Worker 节点 (工作节点)                                       │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│  │ kubelet     │ │ kube-proxy  │ │ Container   │            │
│  │ (节点代理)   │ │ (网络代理)  │ │ Runtime     │            │
│  └─────────────┘ └─────────────┘ └─────────────┘            │
│  ┌─────────────────────────────────────────────┐            │
│  │  Pod ┌──────────┐ ┌──────────┐              │            │
│  │      │Container1│ │Container2│   ...        │            │
│  │      └──────────┘ └──────────┘              │            │
│  └─────────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 核心组件说明

| 组件 | 位置 | 职责 |
|------|------|------|
| **API Server** | Master | 集群入口，所有操作的 REST 接口，认证授权 |
| **Scheduler** | Master | 监听未调度的 Pod，根据资源/亲和性选择节点 |
| **Controller Manager** | Master | 维持期望状态（副本数、节点监控） |
| **etcd** | Master | 分布式键值存储，保存集群所有状态数据 |
| **kubelet** | Worker | 管理 Pod 生命周期，汇报节点状态 |
| **kube-proxy** | Worker | 维护网络规则，实现 Service 负载均衡 |
| **Container Runtime** | Worker | 容器运行时（containerd/CRI-O） |

## 二、核心资源对象详解

### 2.1 Pod（最小调度单位）

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
    env: production
spec:
  containers:
  - name: myapp
    image: nginx:1.24
    ports:
    - containerPort: 80
    resources:
      requests:        # 最小资源需求（调度依据）
        cpu: "100m"    # 0.1 核
        memory: "128Mi"
      limits:          # 最大资源限制
        cpu: "500m"
        memory: "512Mi"
    livenessProbe:     # 存活探针
      httpGet:
        path: /health
        port: 80
      initialDelaySeconds: 30
      periodSeconds: 10
    readinessProbe:    # 就绪探针
      httpGet:
        path: /ready
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
  restartPolicy: Always
```

### 2.2 Deployment（无状态应用部署）

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp-deployment
spec:
  replicas: 3                    # 副本数
  selector:
    matchLabels:
      app: myapp
  strategy:
    type: RollingUpdate          # 滚动更新策略
    rollingUpdate:
      maxSurge: 1                # 最多多出 1 个 Pod
      maxUnavailable: 0          # 更新时不允许不可用
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:v1
        ports:
        - containerPort: 8080
```

### 2.3 Service（服务发现与负载均衡）

```yaml
# ClusterIP - 集群内部访问
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  type: ClusterIP
  selector:
    app: myapp
  ports:
  - port: 80           # Service 端口
    targetPort: 8080    # Pod 端口
    protocol: TCP
---
# NodePort - 外部可通过 NodeIP:NodePort 访问
apiVersion: v1
kind: Service
metadata:
  name: myapp-nodeport
spec:
  type: NodePort
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080     # 范围：30000-32767
---
# LoadBalancer - 云厂商负载均衡
apiVersion: v1
kind: Service
metadata:
  name: myapp-lb
spec:
  type: LoadBalancer
  selector:
    app: myapp
  ports:
  - port: 80
    targetPort: 8080
```

### 2.4 Ingress（域名路由）

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  ingressClassName: nginx
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: myapp-service
            port:
              number: 80
  - host: api.example.com
    http:
      paths:
      - path: /v1
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8080
  tls:
  - hosts:
    - myapp.example.com
    secretName: tls-secret
```

### 2.5 ConfigMap & Secret

```yaml
# ConfigMap - 配置数据
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production
  APP_DEBUG: "false"
  application.yml: |
    server:
      port: 8080
    spring:
      datasource:
        url: jdbc:mysql://db:3306/mydb
---
# Secret - 敏感数据（base64 编码）
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
type: Opaque
data:
  DB_PASSWORD: cGFzc3dvcmQxMjM=    # echo -n 'password123' | base64
  API_KEY: c2VjcmV0a2V5
---
# 在 Pod 中使用
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  containers:
  - name: myapp
    image: myapp:v1
    envFrom:                    # 环境变量方式
    - configMapRef:
        name: app-config
    - secretRef:
        name: app-secret
    volumeMounts:               # 文件挂载方式
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: app-config
```

### 2.6 持久化存储（PV/PVC）

```yaml
# PersistentVolume - 持久卷（管理员创建）
apiVersion: v1
kind: PersistentVolume
metadata:
  name: nfs-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  nfs:
    server: 192.168.1.100
    path: /data/nfs
---
# PersistentVolumeClaim - 持久卷声明（用户申请）
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: myapp-pvc
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 5Gi
---
# 在 Pod 中使用
apiVersion: v1
kind: Pod
metadata:
  name: myapp
spec:
  containers:
  - name: myapp
    image: myapp:v1
    volumeMounts:
    - name: data
      mountPath: /data
  volumes:
  - name: data
    persistentVolumeClaim:
      claimName: myapp-pvc
```

## 三、常用命令速查

### 3.1 集群信息

```bash
# 查看集群信息
kubectl cluster-info

# 查看节点
kubectl get nodes
kubectl get nodes -o wide

# 查看节点详情
kubectl describe node <node-name>
```

### 3.2 资源操作

```bash
# 创建资源
kubectl apply -f deployment.yaml

# 查看资源
kubectl get pods
kubectl get pods -A                    # 所有命名空间
kubectl get pods -o wide               # 显示更多信息
kubectl get pods -l app=myapp          # 按标签过滤
kubectl get pods --field-selector status.phase=Running

# 查看详情
kubectl describe pod <pod-name>

# 查看日志
kubectl logs <pod-name>
kubectl logs <pod-name> -f             # 实时跟踪
kubectl logs <pod-name> --previous     # 上次崩溃的日志
kubectl logs <pod-name> -c <container> # 多容器 Pod 指定容器

# 进入容器
kubectl exec -it <pod-name> -- /bin/bash
kubectl exec -it <pod-name> -c <container> -- /bin/sh

# 删除资源
kubectl delete pod <pod-name>
kubectl delete -f deployment.yaml
kubectl delete pods --all              # 删除所有 Pod
```

### 3.3 扩缩容

```bash
# 手动扩缩容
kubectl scale deployment myapp --replicas=5

# 查看 HPA（自动扩缩容）
kubectl get hpa
kubectl autoscale deployment myapp --min=2 --max=10 --cpu-percent=80
```

### 3.4 滚动更新与回滚

```bash
# 更新镜像
kubectl set image deployment/myapp myapp=myapp:v2

# 查看更新状态
kubectl rollout status deployment/myapp

# 查看更新历史
kubectl rollout history deployment/myapp

# 回滚到上一版本
kubectl rollout undo deployment/myapp

# 回滚到指定版本
kubectl rollout undo deployment/myapp --to-revision=2
```

### 3.5 命名空间

```bash
# 查看命名空间
kubectl get namespaces

# 创建命名空间
kubectl create namespace my-namespace

# 在指定命名空间操作
kubectl get pods -n my-namespace
kubectl apply -f deployment.yaml -n my-namespace
```

## 四、Spring Boot 应用部署实战

### 4.1 项目结构

```
k8s-deploy/
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   └── secret.yaml
└── pom.xml
```

### 4.2 Dockerfile

```dockerfile
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
COPY target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### 4.3 完整部署配置

```yaml
# configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: springboot-config
  namespace: default
data:
  SPRING_PROFILES_ACTIVE: "prod"
  SERVER_PORT: "8080"
  LOGGING_LEVEL_ROOT: "INFO"
---
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: springboot-secret
  namespace: default
type: Opaque
data:
  DB_USERNAME: cm9vdA==           # root
  DB_PASSWORD: cGFzc3dvcmQxMjM=   # password123
---
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: springboot-app
  namespace: default
spec:
  replicas: 3
  selector:
    matchLabels:
      app: springboot-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: springboot-app
    spec:
      containers:
      - name: springboot-app
        image: myregistry.com/springboot-app:v1.0.0
        ports:
        - containerPort: 8080
        envFrom:
        - configMapRef:
            name: springboot-config
        - secretRef:
            name: springboot-secret
        resources:
          requests:
            cpu: "250m"
            memory: "256Mi"
          limits:
            cpu: "1000m"
            memory: "512Mi"
        livenessProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          initialDelaySeconds: 60
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        readinessProbe:
          httpGet:
            path: /actuator/health/readiness
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 5
          timeoutSeconds: 3
          failureThreshold: 3
        startupProbe:
          httpGet:
            path: /actuator/health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
          failureThreshold: 30
---
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: springboot-service
  namespace: default
spec:
  type: ClusterIP
  selector:
    app: springboot-app
  ports:
  - port: 80
    targetPort: 8080
    protocol: TCP
---
# ingress.yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: springboot-ingress
  namespace: default
  annotations:
    nginx.ingress.kubernetes.io/proxy-body-size: "10m"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "60"
spec:
  ingressClassName: nginx
  rules:
  - host: api.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: springboot-service
            port:
              number: 80
  tls:
  - hosts:
    - api.example.com
    secretName: api-tls-secret
```

### 4.4 部署步骤

```bash
# 1. 构建镜像
docker build -t myregistry.com/springboot-app:v1.0.0 .
docker push myregistry.com/springboot-app:v1.0.0

# 2. 创建配置
kubectl apply -f configmap.yaml
kubectl apply -f secret.yaml

# 3. 部署应用
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml

# 4. 验证部署
kubectl get pods -l app=springboot-app
kubectl get svc springboot-service
kubectl get ingress springboot-ingress

# 5. 查看日志
kubectl logs -l app=springboot-app -f
```

## 五、注意事项与最佳实践

### 5.1 资源配置

| 要点 | 说明 |
|------|------|
| **必须设置 requests/limits** | 防止单个 Pod 耗尽节点资源 |
| **requests ≠ limits** | requests 是调度依据，limits 是运行上限 |
| **JVM 堆内存** | limits.memory 应大于 JVM -Xmx，留 20-30% 给非堆 |
| **CPU limits** | 可以不设，允许突发；设了会被限流 |

```yaml
# Spring Boot 推荐配置
resources:
  requests:
    cpu: "250m"
    memory: "512Mi"
  limits:
    cpu: "1000m"      # 或不设
    memory: "1024Mi"  # JVM -Xmx768m + 非堆
```

### 5.2 健康检查

```yaml
# Spring Boot Actuator 端点
livenessProbe:      # 存活：应用是否还活着
  httpGet:
    path: /actuator/health/liveness
    port: 8080
  initialDelaySeconds: 60   # Spring Boot 启动慢，给足时间
  periodSeconds: 10

readinessProbe:     # 就绪：能否接收流量
  httpGet:
    path: /actuator/health/readiness
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 5

startupProbe:       # 启动：给慢启动应用更多时间
  httpGet:
    path: /actuator/health
    port: 8080
  failureThreshold: 30      # 30*5=150 秒启动窗口
  periodSeconds: 5
```

### 5.3 优雅停机

```yaml
# application.yml
server:
  shutdown: graceful

spring:
  lifecycle:
    timeout-per-shutdown-phase: 30s
```

```yaml
# Pod 配置
spec:
  terminationGracePeriodSeconds: 60   # 默认 30s，Spring Boot 建议 60s
  containers:
  - name: myapp
    lifecycle:
      preStop:
        exec:
          command: ["/bin/sh", "-c", "sleep 5"]  # 等待 endpoint 移除
```

### 5.4 镜像最佳实践

```dockerfile
# ❌ 错误：使用 latest 标签
FROM openjdk:17

# ✅ 正确：使用具体版本
FROM eclipse-temurin:17.0.8_7-jre-alpine

# ❌ 错误：以 root 运行
ENTRYPOINT ["java", "-jar", "app.jar"]

# ✅ 正确：使用非 root 用户
RUN addgroup -S app && adduser -S app -G app
USER app
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### 5.5 配置管理

| 场景 | 推荐方式 |
|------|----------|
| 非敏感配置 | ConfigMap |
| 敏感配置（密码/密钥） | Secret + 外部密钥管理（Vault） |
| 配置热更新 | ConfigMap + volumeMounts（文件方式） |
| 环境特定配置 | 不同 namespace 的 ConfigMap |

### 5.6 网络策略

```yaml
# 限制 Pod 只能访问特定服务
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: myapp-network-policy
spec:
  podSelector:
    matchLabels:
      app: myapp
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - port: 3306
```

### 5.7 常见问题排查

| 问题 | 排查命令 | 常见原因 |
|------|----------|----------|
| Pod Pending | `kubectl describe pod <name>` | 资源不足、PVC 未绑定、节点亲和性 |
| Pod CrashLoopBackOff | `kubectl logs <name> --previous` | 应用启动失败、OOM、配置错误 |
| Pod ImagePullBackOff | `kubectl describe pod <name>` | 镜像不存在、仓库认证失败、网络问题 |
| Service 无法访问 | `kubectl get endpoints <svc>` | Pod 未就绪、selector 不匹配、端口错误 |
| Node NotReady | `kubectl describe node <name>` | kubelet 挂了、资源耗尽、网络不通 |

```bash
# 调试流程
kubectl get pods                          # 查看 Pod 状态
kubectl describe pod <name>               # 查看事件
kubectl logs <name> --previous            # 查看崩溃日志
kubectl exec -it <name> -- /bin/sh        # 进入容器调试
kubectl get events --sort-by=.lastTimestamp # 查看集群事件
```

## 六、生产环境建议

### 6.1 集群规划

| 环境 | Master 节点 | Worker 节点 | 说明 |
|------|-------------|-------------|------|
| 开发/测试 | 1 | 2-3 | minikube 或单节点 |
| 预发布 | 3 | 3+ | 与生产同配置 |
| 生产 | 3 (HA) | 5+ | 跨可用区部署 |

### 6.2 安全加固

```yaml
# Pod 安全上下文
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
  containers:
  - name: myapp
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
          - ALL
```

### 6.3 监控告警

| 工具 | 用途 |
|------|------|
| Prometheus + Grafana | 指标监控、可视化 |
| Loki + Promtail | 日志聚合 |
| Jaeger | 链路追踪 |
| kube-state-metrics | K8s 资源指标 |

### 6.4 备份策略

- **etcd 定期备份**：`etcdctl snapshot save`
- **配置版本控制**：所有 YAML 文件 Git 管理
- **Velero**：集群备份与恢复工具

## 七、学习路径建议

```
Week 1-2: Docker 基础 → 镜像构建 → Docker Compose
    ↓
Week 3-4: K8s 核心概念 → Pod/Deployment/Service
    ↓
Week 5-6: ConfigMap/Secret/PV → 命名空间 → RBAC
    ↓
Week 7-8: Ingress → HPA → 网络策略
    ↓
Week 9-10: Helm 包管理 → CI/CD 集成
    ↓
Week 11-12: 监控日志 → 生产部署 → 故障排查
```

## 关联连接

- [[kubernetes-introduction]] — K8s 基础介绍与 Docker 对比
- [[Docker]] — 容器引擎，K8s 的管理对象
- [[microservices]] — 微服务架构，K8s 主要应用场景
- [[SpringBoot]] — Java 应用容器化部署
- [[CI-CD]] — 持续集成/交付，K8s 部署场景
- [[Jenkins]] — CI/CD 自动化服务器
- [[Nginx]] — Ingress Controller 底层实现
