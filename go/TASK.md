# TASK.md

你将修复一个 Go DAG task runner。

## 目标

1. 运行测试并分析失败。
2. 修复 parser、scheduler、executor、reporter 中的问题。
3. 补充回归测试，尤其针对并发和取消语义。
4. 运行 benchmark 并总结结果。

## 必须支持

- JSON 配置读取
- DAG 调度
- goroutine 并发执行
- context timeout
- retry
- dry-run
- 稳定的 JSON 报告

## 交付

- 修复说明
- 新增测试说明
- benchmark 结果
- 已知限制
