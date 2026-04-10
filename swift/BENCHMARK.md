# BENCHMARK.md

## benchmark 场景

- 100 task 宽 DAG
- 1000 task 宽 DAG
- 1000 task 链 DAG
- 1000 task 混合失败/timeout/retry DAG

## 指标

- 总耗时
- 报告生成耗时
- 输出稳定性
- 状态统计正确率

## 评分重点

- timeout/cancel/retry 语义是否正确
- 是否为 Swift Concurrency 特有问题补测试
- 是否避免大规模任务下明显资源浪费
