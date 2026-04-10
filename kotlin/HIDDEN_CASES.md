# HIDDEN_CASES.md

本文件描述 Kotlin 语言 benchmark 的隐藏测试设计要点。

- 重点检查 structured concurrency、timeout/cancel/retry、dry-run 零副作用、并发上限、JSON 输出稳定性、benchmark 退化
- 隐藏测试建议 28~36 条
- 不进入公开 baseline 仓库

核心方向：
- 空任务图 / 多 root / 复杂环 / 重复依赖
- timeout 后子协程真实停止
- retry 不吞 CancellationException
- supervisor 语义正确
- dry-run 无副作用
- 多轮运行无状态污染
- tasks 输出顺序稳定
- 宽 DAG 不得被串行化
- 无协程泄露

详细版本以私有评测仓库为准。
