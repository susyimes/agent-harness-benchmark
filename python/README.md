# Python 赛题：可恢复 Mini Runner

## 题目定位

这是一个面向 agent 框架性能评估的 Python 工程题。重点不在于算法竞赛，而在于：

- 理解已有代码
- 定位并修复多处缺陷
- 在新增约束下补全功能
- 编写回归测试
- 运行 benchmark 并输出总结

## 建议仓库结构

```text
python/
├─ README.md
├─ TASK.md
├─ BASELINE.md
├─ BENCHMARK.md
└─ repo-template/
   ├─ pyproject.toml
   ├─ src/mini_runner/
   │  ├─ parser.py
   │  ├─ scheduler.py
   │  ├─ executor.py
   │  └─ reporter.py
   └─ tests/
      ├─ test_parser.py
      ├─ test_scheduler.py
      ├─ test_executor.py
      ├─ test_reporter.py
      └─ test_e2e.py
```

## 题目概述

参测 agent 将接手一个小型任务执行器项目。它支持：

- 从 JSON 读取任务 DAG
- 进行依赖调度
- 并发执行无依赖任务
- 支持 timeout 和 retry
- 提供 dry-run
- 输出执行报告

但 baseline 版本故意带有多处缺陷，并且测试不完整。agent 需要在有限上下文和多步操作中完成闭环修复。

## 为什么这题适合拉开差距

Python 环境门槛低，便于让不同 agent 框架在同一机器上直接开跑。真正拉开差距的点在于：

- 是否会先建立问题地图，再分阶段推进
- 是否能识别 nondeterministic 问题
- 是否会主动补测试而不是只修公开用例
- 是否能在 benchmark 前做必要的轻量优化
