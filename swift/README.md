# Swift 赛题：结构化并发任务执行器

## 题目定位

Swift 题面向 Swift Concurrency（Task、TaskGroup、Cancellation）设计，用于测试 agent 框架在 Apple 生态并发语义、测试修复与结果聚合上的能力。

## 建议仓库结构

```text
swift/
├─ README.md
├─ TASK.md
├─ BASELINE.md
├─ BENCHMARK.md
└─ repo-template/
   ├─ Package.swift
   ├─ Sources/MiniRunner/
   │  ├─ ConfigParser.swift
   │  ├─ DagScheduler.swift
   │  ├─ TaskExecutor.swift
   │  └─ ReportBuilder.swift
   └─ Tests/MiniRunnerTests/
```

## 题目概述

baseline 是一个 Swift Package，提供 JSON 配置解析、任务依赖调度、并发执行、timeout、retry、dry-run 和报告输出。初始实现存在取消传播、顺序稳定性和状态统计错误。

## 为什么这题能拉开差距

Swift 对很多 agent 来说不是最舒适区，特别是并发与测试组合，更能测出框架在“陌生生态下”的稳健程度。
