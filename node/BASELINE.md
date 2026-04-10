# BASELINE.md

## 基线项目描述

4 个核心文件：

- `parser.js`
- `scheduler.js`
- `executor.js`
- `reporter.js`

测试固定 15 个，初始失败 5~7 个。

## 预埋问题建议

1. cycle detection 对复杂环漏判
2. timeout 仅 `Promise.race` reject，没有真正中断任务
3. retry 会错误重试被 abort 的任务
4. dry-run 仍执行副作用函数
5. 报告输出顺序依赖异步完成先后
6. 统计中把 retried success 记成 failed
7. 大 DAG 下调度实现存在重复扫描

## 隐藏考点

- 是否使用 `AbortController` 正确传播取消
- 是否避免用 `setTimeout` + race 做出伪取消
- benchmark 下 event loop 阻塞情况
