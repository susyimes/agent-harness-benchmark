# Node.js 赛题：异步 DAG Task Runner

## 题目定位

这是一个 Node.js 工程 benchmark 题，重点测试 agent 框架对 Promise、AbortController、并发队列、结果聚合与测试补强的处理能力。

## 建议仓库结构

```text
node/
├─ README.md
├─ TASK.md
├─ BASELINE.md
├─ BENCHMARK.md
└─ repo-template/
   ├─ package.json
   ├─ src/
   │  ├─ parser.js
   │  ├─ scheduler.js
   │  ├─ executor.js
   │  └─ reporter.js
   └─ test/
```

## 题目概述

baseline 是一个基于 Promise 的 DAG task runner，支持 JSON 配置、依赖调度、并发执行、timeout、retry、dry-run 和 JSON 报告。基线实现存在 timeout 只 reject 不 cancel、retry 语义不清、输出顺序不稳定等常见缺陷。

## 为什么这题能拉开差距

Node 题看似简单，但实际很容易在 abort/cancel、event loop 时序和 deterministic report 上出问题，非常适合比较 agent 框架的工程调试能力。
