---
title: "用Qoder+SSE实现工作流实时推送"
source: "https://paicoding.com/column/14/5"
author:
published: 2026-02-08
created: 2026-05-19
description: "基于 Spring SseEmitter 和前端 EventSource 建立服务端推送通道，实现工作流执行过程的实时 SSE 状态推送。使用 CompletableFuture 实现长文本 TTS 并行处理，针对 TTS API 的输入长度限制（600 字节），设计文本智能分片算法"
tags:
  - "clippings"
---
大家好，我是二哥呀。

前面我们已经完成了 LLM 节点和超拟人音频节点的开发，意味着从输入→LLM 节点→超拟人音频节点→输出节点的，一整套 AI 播客的工作流已经雏形可见了。

接下来，我们就需要把四个节点编排起来，来看看实际的效果。

## 一、AI 播客完整工作流验证

先来看输出节点，它的输出引用超拟人音频节点的 audioUrl，呈现给用户的就是原生的 `{{output}}` ，前端页面我们会渲染成一个音频播放器，这一步没问题。

![](https://cdn.paicoding.com/paicoding/754fc83fc8969e7fc4a8f0b1dd6f0d8f.png)

输出节点的前一个节点是超拟人音频合成节点，它的输出就是 voice\_url，这是是我们自定义的，供下一个节点应用；它的输入是文本 text，引用的是通义千问 LLM 节点的 output。

![](https://cdn.paicoding.com/paicoding/27393a5e79646e8f39106f7d2ea922ae.png)

超拟人音频合成节点的前一个节点是通义千问节点，输入参数 input 引用的是用户的输入，输出我们定义为 output，通义千问节点会按照我们的提示词，将用户的输入转成一段符合播客风格的文本内容，供超拟人音频节点合成。

![](https://cdn.paicoding.com/paicoding/9f3edb8231b27581f421c91023749330.png)

那这样一个完成的 AI 播客工作流就算是编排完成了。接下来我们点击【调试】按钮，打开调试面板，输入一段文本，看看整体工作流的运行效果如何。

![](https://cdn.paicoding.com/paicoding/5fbcb37cb3064a42c247fb6b40cd3996.png)

点击【执行工作流】，执行状态，执行日志都开始动起来了。

很遗憾，出现 bug 了，千问 LLM 和 qwen3-tts API 调用都失败了，但节点状态竟然是运行成功的状态，并且 qwen 这里执行失败，就应该立马停止，不应该再继续执行 tts，对吧？

我们把问题直接扔给 Qoder CLI，让它修复。对于 Vibe Coding 来说，发现错误、调教 AI 是至关重要的能力，我们需要指出哪里出错了，应该如何修复，延后再验证，再继续测试，直到最终满足我们的预期效果。

错误其实很明显，我已经看到了 `调用 API 失败: Illegal character in scheme name at index 0: %20https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions\"` 也就是我们填写 API 地址的时候，多了一个空格。😄

Vibe Coding 时代，这种工程素养是非常重要的，否则 AI 改了，但可能改错了，我们没有发现，最终就是耗费大量的时间，拉扯，你会觉得 AI 很傻，AI 会觉得你很菜。

掐起架来了。

第一是我们填写的时候注意，第二是程序帮我们规避到这种问题。

来看看 Qoder CLI 的表现吧。

1. QwenNodeExecutor: 移除了 try-catch 吞掉异常的逻辑,API 调用失败时会直接抛出异常
2. TTSNodeExecutor: 已有正确的异常抛出机制(第31、41、62行)
3. WorkflowEngine: 第92行的 throw e 确保节点失败时立即停止后续节点执行

OK，这正是我们想要的。接着，我们继续让它修复多余空格的问题，直接 trim 掉，没问题。

再次测试，我们发现了另外一个问题，qwen 返回正常的文本，但 tts 执行失败了，从错误信息来看，似乎阿里百炼 TTS API 对输入文本的长度有限制，这一点我们可以访问阿里百炼 TTS 的官方 API 确认一下。

的确，通义千问3-TTS-Flash模型最长输入为600字符。这就对了，实际上，在日常的开发当中，我们一定要多去看官方的 doc，因为 AI Coding 是没办法做到非常准确的，一是我们在提示词中无法给他准确的信息，二是官方的 doc 也会更新，所以这种刨根问底的态度是非常关键的。

好，我们把错误直接扔给 Qoder CLI。但感觉这次反馈并不符合我们的预期（我们希望他能自动分块，然后按块去调用千问 TTS 的 API），那这个时候怎么办呢？可以键入 `/model` 选择一个更高质量的模型，比如说先调整到 Performance 来试试，如果不满意，可以再调高至 Ultimate。

如果还不满意，就不让它猜我们的意图了，直接告诉 Qoder CLI 我们想要的（可以依赖 AI，但也要有自己的技术功底做支撑，否则 AI 和你都会感觉束手无策）：需要切割文本，然后多次调用 tts API，分别把音频文件保存到 MinIO 后，再合并成一个返回回来。

OK，第一件事：将超过 600 字符的文本按标点符号智能分段；第二个件事：多次调用: 对每个分段调用 TTS API；第三件事：下载所有音频片段并合并为单个 WAV 文件；第四件事：将合并后的音频上传到 MinIO。

确认一下代码，整体上没什么问题。但其实还有一个更好的方案，我们以后再试，先看看目前的方案是否可以正常工作。

OK，确实搞定了，可以正常执行，多个音频文件和合并成了一个。

从后台的日志上，确实能看得出来，文本被切割成了 3 个片段。

但有一个细节需要提醒大家，前面看官方 doc 的时候，有说：“通义千问3-TTS-Flash模型最长输入为600字符。”

但实际测试下来，明显感觉不太对劲，这里的 600 字符更像是 600 字节，因为我们总的文本长度为 529，但仍然会提示：

> {"statusCode":400,"message":"<400> InternalError.Algo.InvalidParameter: Range of input length should be \[0, 600\]","code":"InvalidParameter","isJson":true,"requestId":"d98db78f-3802-4b27-a3f6-b7d78d91f9b3"}

类似的错误，当我按照字节去切割为 473、598、356 的时候，最终 API 调用成功了。😄

这就是前面我一再强调的，一定要去看官方 doc，一是指引 AI，二是抱着怀疑的态度，去质疑 AI，去质疑官方 doc。

很多时候，新手容易犯的错误就是，明明我是对的，为什么错了。代码是不会说谎的，错了就是错了，肯定是你哪里错了。只有这样的心态，你才不容易被程序逼疯。

。。。。。。

## 二、集成 SSE 完成节点的实时执行反馈

调通整个工作流后，我们还有一个需求要解决。现在的执行状态，是等所有节点都跑完之后，前端一次性展示结果。

这种方式在功能上是没问题的，但从用户体验上来说，状态流转应该是一个动态过程：

- LLM 节点开始执行 → 执行中 → 执行完成
- 接着切换到 TTS 节点 → 执行中 → 执行完成
- 最后到结束节点，整体流程结束

也就是说，\*\*工作流的执行状态，本质上是一个随时间不断演进的过程，而不是一个一次性结果。\*\*带着这个问题，我们直接把需求丢给了 Qoder CLI：

> 现在有个问题，我发现，执行状态、节点执行结果都是等所有节点都执行完后才显示出来的，实际上这应该是一个动态的过程，llm 节点开始执行的时候执行状态就切到 llm 节点开始执行、执行中、执行结束，然后到 tts 的开始执行、执行中、执行结束，最后到结束节点，这应该是实时响应的。前后端需要联调起来。

面对这个问题，Qoder 并没有一上来就写代码，而是先拆解问题，给出了一套非常工程化的解决步骤。

- 分析当前的工作流架构
- 设计实时更新的方案
- 通过 WebSocket 或者 SSE 来实现实时更新
- 更新工作流引擎以出发状态更新事件
- 前端监听状态变更
- 更新前端 DebugDrawer 的页面，以展示实时更新的效果
- 联调前后端的实时更新

非常严谨，如果让我来实现这个功能，基本上也是这个节奏，哈哈。

Qoder 这次选择了 SSE。原因很简单，整个执行过程是典型的 **服务端主动推送、单向流式更新** 场景，不需要复杂的双向通信，SSE 足够轻量，也更容易和现有 HTTP 体系集成。

### 01、SSE 接口源码分析

在实现层面，整体改动可以分为两部分。后端侧，引入事件执行模型 ExecutionEvent，用来统一描述工作流和节点的状态变化。在 ExecutionController 中新增一个 SSE 接口 executeWorkflowStream，将这些事件以流的形式持续推送给前端。

```java
@Operation(summary = "实时执行工作流(SSE)")
@GetMapping(value = "/{id}/execute/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
public SseEmitter executeWorkflowStream(@PathVariable Long id, @RequestParam String inputData) {
    SseEmitter emitter = new SseEmitter(300000L);
    String emitterId = id + "_" + System.currentTimeMillis();
    emitters.put(emitterId, emitter);
    
    emitter.onCompletion(() -> emitters.remove(emitterId));
    emitter.onTimeout(() -> emitters.remove(emitterId));
    emitter.onError((e) -> emitters.remove(emitterId));
    
    Consumer<ExecutionEvent> eventCallback = event -> {
        try {
            emitter.send(SseEmitter.event()
                    .name(event.getEventType())
                    .data(event));
        } catch (IOException e) {
            log.error("发送 SSE 事件失败", e);
            emitters.remove(emitterId);
        }
    };
    
    new Thread(() -> {
        try {
            Workflow workflow = workflowService.getById(id);
            if (workflow == null) {
                emitter.send(SseEmitter.event()
                        .name("ERROR")
                        .data(ExecutionEvent.workflowComplete("FAILED", "工作流不存在", 0)));
                emitter.complete();
                return;
            }
            
            workflowEngine.executeWithCallback(workflow, inputData, eventCallback);
            emitter.complete();
        } catch (Exception e) {
            log.error("工作流执行失败", e);
            try {
                emitter.send(SseEmitter.event()
                        .name("ERROR")
                        .data(ExecutionEvent.workflowComplete("FAILED", e.getMessage(), 0)));
            } catch (IOException ex) {
                log.error("发送错误事件失败", ex);
            }
            emitter.complete();
        }
    }).start();
    
    return emitter;
}
复制代码
```

这个接口返回的不是普通的 JSON，而是一个 SseEmitter。它代表的是一条 **可以持续向客户端发送事件的长连接** 。只要这个 emitter 不关闭，服务端就可以不断往前端推送执行状态，而前端不需要反复轮询。

在方法一开始，就创建了一个 SseEmitter，并且显式设置了超时时间。这里设置的是 300 秒，目的是给一次完整工作流执行预留足够的时间窗口，避免流程还没跑完，连接就被服务端提前回收。

接着，通过 workflowId + 时间戳生成一个 emitterId，并把 emitter 放进一个 Map 里统一管理。这一层设计很关键，它解决的是两个问题：一是支持同一个工作流被多次触发执行；二是当连接异常、超时或完成时，能够准确地清理对应的 emitter，避免资源泄漏。

紧接着，为 emitter 注册了三个回调：onCompletion、onTimeout 和 onError。这三个回调的处理逻辑非常统一，都是在连接生命周期结束时，把 emitter 从管理容器中移除。

真正把“实时”串起来的，是接下来的 eventCallback。这里定义了一个 Consumer，用来接收 WorkflowEngine 在执行过程中抛出的 ExecutionEvent。每当有新的执行事件产生，就通过 emitter.send 将事件推送给前端。

注意这里发送的不只是字符串，而是一个带有 eventType 的 SSE 事件。这意味着前端可以根据不同的事件类型，区分是工作流开始、节点开始、节点成功、节点失败，还是流程结束。

接下来这段 new Thread，是整个流程真正启动的地方。之所以单独起一个线程，是为了避免阻塞当前 HTTP 请求线程，让 SSE 连接可以保持打开状态，而工作流在后台独立执行。

在线程内部，首先会校验工作流是否存在。如果工作流不存在，会立即通过 SSE 向前端发送一个失败事件，然后结束连接。这一步的好处是，前端可以第一时间拿到明确的错误反馈，而不是无响应地等待。

如果工作流存在，就会调用 workflowEngine.executeWithCallback。这个方法和普通的 execute 最大的不同在于：它在每个节点执行前、执行成功、执行失败等关键时刻，都会通过 callback 抛出 ExecutionEvent。

也正是因为这一点，WorkflowEngine 不需要知道 SSE 的存在。它只负责“执行”和“通知状态变化”，而“怎么通知到前端”，由外层的 SSE 接口来完成。这是一个非常典型的解耦设计。

当整个工作流执行完成之后，会显式调用 emitter.complete，告诉前端：这条事件流已经结束。前端在收到 complete 信号后，可以做最终状态收敛，比如关闭加载动画、展示最终结果等。如果执行过程中抛出了未捕获的异常，代码也会兜底发送一个失败事件，并确保 emitter 被正确关闭。

详细分析源码也能证明一点： **Qoder 的代码能力真的无可挑剔** ！我们也要通过学习 Qoder，让自己具备这种代码能力，否则时间久了，你会发现自己被 AI 拉的差距越来越大。

### 02、后端发送 SSE 状态变化

如果说 SSE 解决的是“怎么把信息推给前端”，那 executeWithCallback 方法解决的就是： **在工作流执行的每一个关键时刻，准确地抛出状态变化。**

```java
public ExecutionResponse executeWithCallback(Workflow workflow, String inputData, Consumer<ExecutionEvent> eventCallback) {
    long startTime = System.currentTimeMillis();
    
    WorkflowConfig config = JSON.parseObject(workflow.getFlowData(), WorkflowConfig.class);
    List<WorkflowNode> sortedNodes = dagParser.parse(config);
    
    List<ExecutionResponse.NodeResult> nodeResults = new ArrayList<>();
    Map<String, Map<String, Object>> nodeOutputs = new HashMap<>();
    
    Map<String, Object> currentInput = new HashMap<>();
    currentInput.put("input", inputData);
    
    String status = "SUCCESS";
    String errorMessage = null;
    String outputData = null;
    
    ExecutionRecord record = new ExecutionRecord();
    
    try {
        if (eventCallback != null) {
            eventCallback.accept(ExecutionEvent.workflowStart(null));
        }
        
        for (WorkflowNode node : sortedNodes) {
            long nodeStartTime = System.currentTimeMillis();
            
            if (eventCallback != null) {
                eventCallback.accept(ExecutionEvent.nodeStart(node.getId(), node.getType()));
            }
            
            ExecutionResponse.NodeResult nodeResult = new ExecutionResponse.NodeResult();
            nodeResult.setNodeId(node.getId());
            nodeResult.setNodeName(node.getType());
            nodeResult.setInput(JSON.toJSONString(currentInput));
            
            try {
                NodeExecutor executor = executorFactory.getExecutor(node.getType());
                Map<String, Object> output = executor.execute(node, currentInput);
                
                nodeOutputs.put(node.getId(), output);
                currentInput = output;
                
                nodeResult.setStatus("SUCCESS");
                nodeResult.setOutput(JSON.toJSONString(output));
                
                long nodeEndTime = System.currentTimeMillis();
                int nodeDuration = (int) (nodeEndTime - nodeStartTime);
                nodeResult.setDuration(nodeDuration);
                
                if (eventCallback != null) {
                    eventCallback.accept(ExecutionEvent.nodeSuccess(node.getId(), node.getType(), output, nodeDuration));
                }
                
            } catch (Exception e) {
                log.error("节点执行失败: {}", node.getId(), e);
                nodeResult.setStatus("FAILED");
                nodeResult.setError(e.getMessage());
                status = "FAILED";
                errorMessage = "节点 " + node.getId() + " 执行失败: " + e.getMessage();
                
                if (eventCallback != null) {
                    eventCallback.accept(ExecutionEvent.nodeError(node.getId(), node.getType(), e.getMessage()));
                }
                
                throw e;
            } finally {
                long nodeEndTime = System.currentTimeMillis();
                nodeResult.setDuration((int) (nodeEndTime - nodeStartTime));
                nodeResults.add(nodeResult);
            }
        }
        
        outputData = JSON.toJSONString(currentInput);
        
    } catch (Exception e) {
        status = "FAILED";
        if (errorMessage == null) {
            errorMessage = e.getMessage();
        }
    }
    
    long endTime = System.currentTimeMillis();
    int duration = (int) (endTime - startTime);
    
    if (eventCallback != null) {
        eventCallback.accept(ExecutionEvent.workflowComplete(status, currentInput, duration));
    }
    
    record.setFlowId(workflow.getId());
    Map<String, Object> inputDataMap = new HashMap<>();
    inputDataMap.put("input", inputData);
    String inputDataJson = JSON.toJSONString(inputDataMap);
    log.info("保存执行记录 - inputData: {}", inputDataJson);
    log.info("保存执行记录 - outputData: {}", outputData);
    record.setInputData(inputDataJson);
    record.setOutputData(outputData);
    record.setStatus(status);
    record.setNodeResults(JSON.toJSONString(nodeResults));
    record.setErrorMessage(errorMessage);
    record.setDuration(duration);
    executionRecordMapper.insert(record);
    
    ExecutionResponse response = new ExecutionResponse();
    response.setExecutionId(record.getId());
    response.setStatus(status);
    response.setNodeResults(nodeResults);
    response.setOutputData(outputData);
    response.setDuration(duration);
    
    return response;
}
复制代码
```

方法一开始，先记录整体执行的 startTime，然后把 workflow 中存储的 flowData 反序列化成 WorkflowConfig。从这一刻开始，执行逻辑完全基于 DSL 描述，而不是数据库模型本身。

接下来通过 dagParser.parse，把 DSL 转换成一个已经排好序的节点列表。这里拿到的 sortedNodes，并不是简单的节点集合，而是 **已经满足依赖关系的执行顺序** 。

每执行一个节点，都会先记录 nodeStartTime，然后立刻发送 nodeStart 事件。注意这里发送事件的时机非常讲究：是在节点真正开始执行之前，而不是执行完成之后。这样前端才能准确地展示“某个节点正在运行中”的状态。

接着构建 NodeResult，对当前节点的输入进行序列化并保存。这一点在调试和问题排查时非常有价值，因为可以完整看到每个节点在当时“拿到了什么输入”。

如果节点执行成功，会把输出写入 nodeOutputs，并同步更新 currentInput，供后续节点使用。紧接着发送 nodeSuccess 事件，告诉外部：这个节点已经顺利跑完。

当所有节点执行完成，或者流程被中途终止之后，方法会统一整理 ExecutionRecord，计算整体耗时、最终状态和输出结果。

如果整个流程正常结束，会发送 workflowSuccess 事件；如果过程中出现异常，则发送 workflowFail 事件。

### 03、前端监听 SSE 事件更新

前端新增 executeWorkflowStream 监听 SSE 事件更新、实时显示节点执行状态、动态更新进度条、实时追加执行日志、支持执行过程中查看中间结果等。

```typescript
executeWorkflowStream(
  currentWorkflowId,
  inputData,
  (event: ExecutionEvent) => {
    console.log('收到事件:', event);

    switch (event.eventType) {
      case 'WORKFLOW_START':
        addLog('🚀 工作流开始执行');
        break;

      case 'NODE_START':
        addLog(\`📍 节点 [${event.nodeName}] 开始执行...\`);
        if (event.nodeId && event.nodeName) {
          const nodeResult: NodeResult = {
            nodeId: event.nodeId,
            nodeName: event.nodeName,
            status: 'RUNNING',
            input: {},
            output: {},
            duration: 0
          };
          tempNodeStatusMap.set(event.nodeId, nodeResult);
          setNodeStatusMap(new Map(tempNodeStatusMap));
        }
        break;

      case 'NODE_SUCCESS':
        if (event.nodeId && event.nodeName) {
          const duration = event.message?.match(/耗时 (\d+)ms/)?.[1] || '0';
          addLog(\`✅ 节点 [${event.nodeName}] 执行成功,耗时 ${duration}ms\`);

          const nodeResult: NodeResult = {
            nodeId: event.nodeId,
            nodeName: event.nodeName,
            status: 'SUCCESS',
            input: {},
            output: event.data || {},
            duration: parseInt(duration)
          };
          tempNodeStatusMap.set(event.nodeId, nodeResult);
          nodeResults.push(nodeResult);
          setNodeStatusMap(new Map(tempNodeStatusMap));
        }
        break;

      case 'NODE_ERROR':
        if (event.nodeId && event.nodeName) {
          addLog(\`❌ 节点 [${event.nodeName}] 执行失败: ${event.message}\`);
          const nodeResult: NodeResult = {
            nodeId: event.nodeId,
            nodeName: event.nodeName,
            status: 'FAILED',
            input: {},
            output: {},
            duration: 0,
            error: event.message
          };
          tempNodeStatusMap.set(event.nodeId, nodeResult);
          nodeResults.push(nodeResult);
          setNodeStatusMap(new Map(tempNodeStatusMap));
        }
        break;

      case 'WORKFLOW_COMPLETE':
        const totalDuration = event.message?.match(/总耗时 (\d+)ms/)?.[1] || '0';
        addLog(\`${event.status === 'SUCCESS' ? '✅' : '❌'} 工作流执行${event.status === 'SUCCESS' ? '成功' : '失败'},总耗时 ${totalDuration}ms\`);

        setExecutionResult({
          executionId: 0,
          status: event.status as 'SUCCESS' | 'FAILED',
          nodeResults: Array.from(tempNodeStatusMap.values()),
          outputData: event.data || {},
          duration: parseInt(totalDuration),
          errorMessage: event.status === 'FAILED' ? event.message : undefined
        });
        break;
    }
  },
  () => {
    setExecuting(false);
  },
  (error: Error) => {
    addLog(\`❌ 执行异常: ${error.message}\`);
    setExecuting(false);
  }
);
复制代码
```

OK，我们来体验一下，看看效果，有了，有了！

并且捎带把节点执行结果中的 JSON 字符串也格式化了，只不过有一点点小问题，就是 qwen 没有把上一步中的输入数据显示出来，tts 中的输入数据也没有把上一步的显示出来。

直接把问题发给 Qoder CLI，让它帮我们解决。

好，现在没问题了，文章结尾我会录一个视频给大家。

## 三、优化 TTS 的实时反馈

由于 TTS 需要分块，所以导致进度比较慢，那我们希望每次分片的进度也能够实时显示出来，这样对用户就会更友好一点，对吧？

直接把这个需求扔给 Qoder CLI，然后我们来看都有哪些改动。

- 后端在每个分片的前后处理发送进度事件
- 前端增加对 NODE\_PROGRESS 的处理

来看一下效果。执行日志里可以看到分片的进度了。

看了一下源码，目前是分片后同步方式请求千问 TTS API 的，那能不能在分片后并发请求呢？这样可以进一步加快 tts 节点的处理速度，对吧？

Qoder CLI 明确告诉我们可以，并且很快就搞定了。

看一下源码，主要是用到了 CompletableFuture，不错。

这其实也是面试中非常容易考察的点，尤其是问并发编程相关的八股时。

```java
MultiModalConversation conv = new MultiModalConversation();
        
List<CompletableFuture<byte[]>> futures = new ArrayList<>();

for (int i = 0; i < textChunks.size(); i++) {
    final int chunkIndex = i;
    final String chunk = textChunks.get(i);
    
    CompletableFuture<byte[]> future = CompletableFuture.supplyAsync(() -> {
        try {
            int utf8ByteLength = chunk.getBytes(java.nio.charset.StandardCharsets.UTF_8).length;
            log.info("处理第 {}/{} 个片段, 字符数: {}, UTF-8 字节数: {}", 
                    chunkIndex + 1, textChunks.size(), chunk.length(), utf8ByteLength);
            
            if (progressCallback != null) {
                Map<String, Object> progressData = new HashMap<>();
                progressData.put("totalChunks", textChunks.size());
                progressData.put("currentChunk", chunkIndex + 1);
                progressData.put("chunkText", chunk.substring(0, Math.min(50, chunk.length())) + "...");
                progressCallback.accept(ExecutionEvent.nodeProgress(
                    node.getId(), 
                    node.getType(), 
                    "正在处理第 " + (chunkIndex + 1) + "/" + textChunks.size() + " 个片段", 
                    progressData
                ));
            }
            
            MultiModalConversationParam param = MultiModalConversationParam.builder()
                    .apiKey(apiKey)
                    .model(model)
                    .text(chunk)
                    .voice(voice)
                    .languageType(languageType)
                    .build();
            
            MultiModalConversationResult result = conv.call(param);
            String audioUrl = result.getOutput().getAudio().getUrl();
            
            if (!StringUtils.hasText(audioUrl)) {
                throw new RuntimeException("阿里百炼 TTS 返回的音频URL为空 (片段 " + (chunkIndex + 1) + ")");
            }
            
            log.info("第 {}/{} 个片段音频URL: {}", chunkIndex + 1, textChunks.size(), audioUrl);
            
            byte[] audioData = downloadAudio(audioUrl);
            
            if (progressCallback != null) {
                Map<String, Object> progressData = new HashMap<>();
                progressData.put("totalChunks", textChunks.size());
                progressData.put("currentChunk", chunkIndex + 1);
                progressData.put("completedChunks", chunkIndex + 1);
                progressCallback.accept(ExecutionEvent.nodeProgress(
                    node.getId(), 
                    node.getType(), 
                    "已完成第 " + (chunkIndex + 1) + "/" + textChunks.size() + " 个片段", 
                    progressData
                ));
            }
            
            return audioData;
        } catch (Exception e) {
            throw new RuntimeException("处理第 " + (chunkIndex + 1) + " 个片段失败: " + e.getMessage(), e);
        }
    });
    
    futures.add(future);
}

CompletableFuture.allOf(futures.toArray(new CompletableFuture[0])).join();

for (CompletableFuture<byte[]> future : futures) {
    audioChunks.add(future.get());
}
复制代码
```

这一段 TTS 的实现，是整个实时反馈体验里最容易被低估的一块。这是我们遇到的问题：一段较长的文本被拆成多个片段后，如果按照同步方式逐个调用 TTS 接口、下载音频，再拼接，整个过程会明显变慢，而且前端只能看到“卡住不动”的状态。

于是我们引入了 CompletableFuture，把 **原本串行的 TTS 处理过程，改造成并发执行** 。每一个 CompletableFuture，都代表着一个文本片段对应的音频数据，在未来某个时间点会准备好。

接着进入 for 循环，对 textChunks 里的每一个文本片段分别创建一个异步任务。这里使用的是 `CompletableFuture.supplyAsync` 。每个异步任务里做的事情都是一样的：先记录当前处理的是第几个片段，同时通过 progressCallback 把“正在处理第 N 个片段”的进度事件推送出去；然后构造 TTS 请求参数，调用阿里百炼的 TTS 接口；拿到音频 URL 之后，再下载音频数据，最终返回一个 `byte` 数组。

异常处理采用的是 fail fast 策略，如果某一个片段在 TTS 调用或音频下载过程中失败，会直接抛出 RuntimeException。当所有 CompletableFuture 都创建完成之后，代码通过 `CompletableFuture.allOf(...).join()` 进入统一等待阶段。等 allOf 返回之后，说明所有音频分片要么全部成功，要么已经有异常抛出。

由于 futures 的插入顺序，和文本片段的顺序是一一对应的，这就保证了：TTS 处理是并发执行的，但最终音频的合并顺序是可控的。

OK，我们来看一下最终的效果。

从我的直观感受来看，快了，快了很多，对比并发之前的 33698ms，时间缩短了 2/3，这就是并发的优势啊！

## 四、小结

好，用 Qoder 的智能聊天模块，总结一下本次我们通过 Qoder CLI 完成的 PaiAgent 工作流新需求，看看如何写到简历上。

- 基于 Spring SseEmitter 和前端 EventSource 建立服务端推送通道，实现工作流执行过程的实时 SSE 状态推送。
- 在 NodeExecutor 接口中扩展 Consumer 回调参数，通过 default 方法保证向下兼容。
- 使用 CompletableFuture 实现长文本 TTS 并行处理，针对 TTS API 的输入长度限制（600 字节），设计文本智能分片算法，通过 CompletableFuture.supplyAsync() 并行提交分片任务，使用 allOf().join() 等待所有任务完成后按序合并，该节点执行时间由 33 秒缩短至 10 秒左右。
- 实现 WAV 音频文件合并算法，解析 WAV 文件结构（44 字节头 + PCM 数据），合并多个音频片段时保留首个文件头，拼接所有数据块，并使用小端序修正头部的文件大小和数据块大小字段，确保合并后音频可正常播放。
- 开发前端实时调试面板，使用 React + Ant Design 构建 DebugDrawer 组件，通过 EventSource 订阅 SSE 事件流，实现节点执行状态实时更新、动态进度条、Timeline 日志追加等功能。

这些也是面试中我们可以和面试官掰扯的关键点。

从工作流能不能跑，到节点执行过程是否可感知；从一次性返回结果，到基于 SSE 的实时状态流；再到 TTS 这种典型长耗时 IO 场景下，通过 CompletableFuture 把性能硬生生拉起来——这一整条链路，本质上都在回答同一个问题： **在 AI 应用里，工程能力到底值不值钱。**

Qoder 在这个过程里扮演的角色，并不是“帮我写几行代码的工具”，而是一个非常克制、但极其工程化的搭档。它不会替你做设计决策，但会逼着你把问题拆清楚；它不会帮你绕过复杂度，但会在关键节点给出合理、可落地的实现路径。

你会发现，真正让系统“好用起来”的，从来不是某个模型参数，也不是一句 Prompt，而是这些真真实实能帮我们完成开发任务的能力：执行链路、并发控制、异常传播、实时反馈。

代码我已经提交到了： [https://github.com/itwanger/PaiAgent-one/tree/PaiAgent-Five](https://github.com/itwanger/PaiAgent-one/tree/PaiAgent-Five)