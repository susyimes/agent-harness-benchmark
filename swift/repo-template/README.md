# Swift LogInspector Benchmark Baseline

这是一个用于测试 agent 框架能力的 Swift baseline 项目。

## 目标

参测 agent 需要修复并补强这个本地日志检索工具，使其在：

- parser 容错
- search 语义
- stats 统计
- redact 脱敏
- CLI 退出码与输出稳定性

等方面达到可交付水平。

## 本地运行

```bash
swift test
swift run loginspect search Fixtures/app.log error
```

## baseline 特征

- 可运行，但测试不会全绿
- 本地零外部服务
- 适合拿给其他 agent 框架做 benchmark
