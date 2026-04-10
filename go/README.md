# Go 赛题：并发流水线任务执行器

## 题目定位

这是一个 Go 工程题，目标是测试 agent 框架在 goroutine / channel / context 语义下的调试与修复能力。

## 建议仓库结构

```text
go/
├─ README.md
├─ TASK.md
├─ BASELINE.md
├─ BENCHMARK.md
└─ repo-template/
   ├─ go.mod
   ├─ parser.go
   ├─ scheduler.go
   ├─ executor.go
   ├─ reporter.go
   └─ *_test.go
```

## 题目概述

baseline 项目是一个 DAG task runner，使用 goroutine 并发执行，支持 context timeout、retry、dry-run 和 JSON 报告。代码表面上很 idiomatic，但隐藏了竞态、取消语义和结果聚合稳定性问题。

## 为什么这题能拉开差距

Go 的难点不在语法，而在并发语义是否被 agent 真正理解。很多 agent 会写出“能跑”的修复，但在 race、cancel、report 稳定性上翻车。
