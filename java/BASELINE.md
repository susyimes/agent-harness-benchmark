# BASELINE.md

## 基线项目描述

一个小型 Maven 项目，核心 4 类：

- `ConfigParser.java`
- `DagScheduler.java`
- `JobExecutor.java`
- `ReportBuilder.java`

总代码量建议 700~1000 行，测试 15 个，初始失败 5~7 个。

## 预埋问题建议

1. `CompletableFuture` timeout 后未取消底层任务
2. retry 逻辑错误地把 timeout 也纳入可重试异常
3. DAG 环检测只返回 true/false，错误信息不可读
4. `dryRun=true` 时仍触发 side-effect callback
5. 报告结果使用 `HashMap` 导致输出顺序不稳定
6. 多线程下失败统计与重试次数统计不一致
7. 大 DAG 下队列轮询实现低效

## 隐藏考点

- 线程池 shutdown 语义
- 被取消任务的状态聚合
- deterministic report
- 在 1000 task 下避免明显 O(n^2) 调度开销
