# BENCHMARK.md

## benchmark 输入

由本地生成器构造：

- 100 task 宽 DAG
- 1000 task 宽 DAG
- 1000 task 链 DAG
- 1000 task 混合失败/重试 DAG

## 指标

- 总耗时
- 平均任务完成耗时
- 报告生成耗时
- 任务状态正确率
- 输出结果稳定性

## 评分关注点

- 并发修复是否真的正确
- 是否引入 synchronized 过度导致性能崩坏
- 是否主动新增针对取消语义和报告稳定性的测试
