# BENCHMARK.md

## benchmark 场景

- 100 task 宽 DAG
- 1000 task 宽 DAG
- 1000 task 链 DAG
- 1000 task 混合 timeout/retry DAG

## 指标

- 总耗时
- dry-run 耗时
- 报告生成耗时
- 输出稳定性

## 评分重点

- timeout/cancel 语义是否真实有效
- 是否新增针对异步时序和 abort 的测试
- 是否避免重复扫描导致的大 DAG 退化
