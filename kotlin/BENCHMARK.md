# BENCHMARK.md

## benchmark 场景

- 100 task 宽 DAG
- 1000 task 宽 DAG
- 1000 task 链 DAG
- 1000 task 混合 timeout/retry DAG

## 指标

- 总耗时
- 协程执行峰值（可选）
- 报告生成耗时
- 输出稳定性

## 评分重点

- cancel / timeout / retry 语义是否正确
- 是否新增针对 coroutine 泄露和 cancel 传播的测试
- 是否避免过度串行化
