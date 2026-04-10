# BASELINE.md

## 基线项目描述

4 个核心文件：

- `ConfigParser.swift`
- `DagScheduler.swift`
- `TaskExecutor.swift`
- `ReportBuilder.swift`

测试总数 15，初始失败 5~7。

## 预埋问题建议

1. `TaskGroup` 中错误传播导致部分任务状态丢失
2. timeout 后任务未正确取消
3. retry 把取消错误也作为普通失败重试
4. dry-run 仍执行真实闭包
5. cycle detection 仅覆盖简单场景
6. 报告任务顺序不稳定
7. 汇总统计把 skipped / cancelled / failed 混淆

## 隐藏考点

- structured concurrency 语义
- cancellation 是否真正传播
- 大 DAG 下任务创建与汇总开销
