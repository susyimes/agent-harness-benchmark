# Node mini-ci-runner Benchmark Baseline

本项目是一个用于测试 agent 框架能力的 Node.js baseline。

## 目标

参测 agent 需要修复并补强这个本地 pipeline runner，使其在：

- 依赖调度
- retry
- timeout
- 子进程清理
- artifact 传递
- CLI 退出码

等方面达到可交付水平。

## 运行

```bash
npm test
node src/cli.js run --config fixtures/pipelines/basic.json
```

## baseline 特征

- 可运行，但不会全绿
- 本地零外部服务
- 适合拿给其他 agent 框架做 benchmark
