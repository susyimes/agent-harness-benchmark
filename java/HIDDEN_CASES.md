# HIDDEN_CASES.md

本文件描述 Java 语言 benchmark 的隐藏测试设计要点。

- 关注并发语义、timeout/cancel、retry、DAG 调度、报告稳定性和性能退化
- 隐藏测试应保存在私有评测仓库，不进入公开 baseline
- 推荐最小集合：22 条

核心方向：
- 空任务与极端 timeout 边界
- 多父依赖严格等待全部完成
- 复杂环可读输出
- dry-run 零副作用
- timeout 不重试
- cancel 后不得回写 success
- retry/failure 统计一致
- 同任务不重复提交
- 重复运行稳定
- shutdown 后无线程泄漏
- JSON 字段顺序稳定
- 宽 DAG / 链 DAG / cancel 风暴性能退化守卫

详细版本以私有评测仓库为准。
