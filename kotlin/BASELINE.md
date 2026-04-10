# BASELINE.md

## 基线项目描述

4 个核心文件：

- `ConfigParser.kt`
- `DagScheduler.kt`
- `TaskExecutor.kt`
- `ReportFormatter.kt`

测试数 15，初始失败 5~7。

## 预埋问题建议

1. 使用 `GlobalScope` 造成结构化并发失效
2. `withTimeout` 后子协程未被正确取消
3. retry 错误地捕获 `CancellationException`
4. dry-run 仍触发任务副作用
5. cycle detection 仅检测简单环
6. 报告 JSON 中任务顺序不稳定
7. 统计中把 cancelled 与 failed 混淆

## 隐藏考点

- 是否能避免将所有逻辑包进一个大 `runBlocking`
- 是否正确处理 supervisorScope 语义
- 大 DAG 下协程调度是否存在明显资源浪费
