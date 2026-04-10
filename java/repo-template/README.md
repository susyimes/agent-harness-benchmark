# Java LogFlow Mini Benchmark Baseline

这是一个用于测试 agent 框架能力的 Java baseline 项目。

## 目标

参测 agent 需要修复并补强这个本地日志查询小服务，使其在：

- 日志解析
- 搜索与过滤
- 时间范围边界
- 滚动日志读取
- 统计口径一致性
- 输出稳定性
- 测试补强

等方面达到可交付水平。

## 本地运行

如果机器已安装 Maven：

```bash
mvn test
mvn -q exec:java -Dexec.args="search data/app.log error"
```

如果机器未安装 Maven，请先安装 Maven 3.9+，或后续补充 Maven Wrapper 后再运行。

## baseline 特征

- 可运行，但测试不会全绿
- 本地零外部服务
- 适合拿给其他 agent 框架做 benchmark
