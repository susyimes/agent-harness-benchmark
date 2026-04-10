# HIDDEN_CASES.md

本文件描述 Swift 语言 benchmark 的隐藏测试设计要点。

- 重点检查 Task / TaskGroup 取消传播、timeout 真取消、retry 语义、dry-run 零副作用、报告顺序稳定性、性能退化
- 隐藏测试建议 18~25 条
- 不进入公开 baseline 仓库

核心方向：
- 空配置 / 深链 DAG / 宽 DAG / 复杂环
- timeout 后底层任务真实停止
- retry 不重试 CancellationError
- 上游失败后的下游状态传播
- 多轮执行无状态污染
- 并发上限生效
- JSON 报告顺序稳定
- 1000 级 DAG benchmark 退化守卫

详细版本以私有评测仓库为准。
