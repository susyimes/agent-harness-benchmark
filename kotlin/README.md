# Kotlin 赛题：协程任务编排器

## 题目定位

Kotlin 题目聚焦在 coroutine、structured concurrency、timeout/cancel 语义，以及 JSON 报告稳定输出。它很适合测试 agent 框架是否真的能处理现代并发抽象，而不是只做表面修补。

## 建议仓库结构

```text
kotlin/
├─ README.md
├─ TASK.md
├─ BASELINE.md
├─ BENCHMARK.md
└─ repo-template/
   ├─ build.gradle.kts
   ├─ src/main/kotlin/benchmark/
   │  ├─ ConfigParser.kt
   │  ├─ DagScheduler.kt
   │  ├─ TaskExecutor.kt
   │  └─ ReportFormatter.kt
   └─ src/test/kotlin/benchmark/
```

## 题目概述

一个使用 Kotlin 协程实现的 DAG runner，支持 timeout、retry、dry-run、JSON 报告。基线实现刻意引入结构化并发违规、取消传播异常和输出不稳定问题。

## 为什么这题能拉开差距

很多 agent 会写 Kotlin，但未必真正理解 coroutine scope、supervisor、timeout 和 cancel 的组合语义。这类题能很快分出层次。
