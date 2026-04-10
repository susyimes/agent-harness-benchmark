# Python Event Ledger Benchmark Baseline

这是一个用于测试 agent 框架能力的 Python baseline 项目。

## 目标

参测 agent 需要修复并补强这个本地事件账本任务队列系统，使其在：

- 事件回放恢复
- retry 边界
- 幂等消费
- CLI 一致性
- metrics 统计
- 回归测试补强

等方面达到可交付水平。

## 本地运行

```bash
python -m pytest -q
python -m app.cli status --seed data/seed_jobs.json --log data/events.log
python -m app.cli run-until-empty --seed data/seed_jobs.json --log data/events.log
```

## baseline 特征

- 初始版本可运行，但测试不会全绿
- 存在已知 bug 和缺失能力
- 不依赖数据库或外部服务
- 适合拿给其他 agent 框架做 benchmark
