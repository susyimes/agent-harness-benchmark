# BENCHMARK.md

## 数据规模

统一使用本地脚本自动生成 DAG：

- 100 tasks，宽 DAG
- 1000 tasks，宽 DAG
- 1000 tasks，链 DAG
- 1000 tasks，10% 任务首轮失败后重试成功

## 指标

- 全量执行耗时
- dry-run 耗时
- 报告生成耗时
- p50 / p95 单任务完成时间（可选）
- 结果是否 deterministic

## 评分建议

- Correctness 40
- Robustness 20
- Performance 15
- Process Quality 15
- Tool Efficiency 10

## 隐藏考点

- 1000 task 下 max_workers 是否真的生效
- timeout 后是否出现僵尸任务
- dry-run 是否完全无副作用
- JSON report 字段顺序与内容是否稳定
