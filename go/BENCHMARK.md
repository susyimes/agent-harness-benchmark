# BENCHMARK.md

## benchmark 场景

- 100 task 宽 DAG
- 1000 task 宽 DAG
- 1000 task 链 DAG
- 1000 task，10% 首次失败重试成功

## 指标

- 总耗时
- goroutine 峰值（可选）
- 报告生成耗时
- 结果稳定性
- race 检查结果

## 评分重点

- 是否正确处理 cancel / close / retry 交互
- 是否主动使用 race 检查
- 是否避免用粗暴锁把并发性能抹平
