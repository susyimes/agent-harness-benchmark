# Java 赛题：可重试 DAG Job Runner

## 题目定位

这是一个面向 agent 框架的 Java 工程修复题。重点是让 agent 在典型企业工程约束下处理：

- 多模块调用关系理解
- 并发与 Future/线程池行为修复
- 超时与取消语义
- 报告稳定性
- 回归测试补强

## 建议仓库结构

```text
java/
├─ README.md
├─ TASK.md
├─ BASELINE.md
├─ BENCHMARK.md
└─ repo-template/
   ├─ pom.xml
   ├─ src/main/java/benchmark/runner/
   │  ├─ ConfigParser.java
   │  ├─ DagScheduler.java
   │  ├─ JobExecutor.java
   │  └─ ReportBuilder.java
   └─ src/test/java/benchmark/runner/
      ├─ ConfigParserTest.java
      ├─ DagSchedulerTest.java
      ├─ JobExecutorTest.java
      └─ EndToEndTest.java
```

## 题目概述

baseline 是一个基于线程池的 DAG job runner，支持 JSON 配置、任务依赖、重试、超时和 dry-run。项目看起来完整，但实现里夹杂多处真实工程常见问题。

## 为什么这题能拉开差距

Java 题能明显测出 agent 框架在：

- 阅读稍啰嗦的工程代码时是否会迷路
- 修改并发逻辑时是否保守且可验证
- 面对 Maven/测试反馈时能否高效迭代
