# Go TaskRunner Benchmark Baseline

这是一个用于测试 agent 框架能力的 Go baseline 项目。

## 目标

参测 agent 需要修复并补强这个本地 DAG task runner，使其在：

- 配置解析
- DAG 调度
- context timeout / cancel
- retry
- dry-run
- report 稳定性

等方面达到可交付水平。

## 本地运行

```bash
go test ./...
go run ./cmd/taskrunner
```

## baseline 特征

- 可运行，但测试不会全绿
- 本地零外部服务
- 适合拿给其他 agent 框架做 benchmark
