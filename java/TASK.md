# TASK.md

你将修复并增强一个 Java DAG job runner。

## 目标

1. 运行测试并定位失败。
2. 修复并发、超时、重试、环检测和 dry-run 相关问题。
3. 保持现有整体架构，不做无必要重写。
4. 至少新增 5 条回归测试。
5. 输出 benchmark 结果与修复总结。

## 功能要求

- JSON 配置解析
- DAG 调度
- 线程池并发执行
- timeout + cancel
- retry
- dry-run
- 稳定的 JSON 报告

## 输出要求

- 问题根因列表
- 修复策略
- 新增测试列表
- benchmark 结果
- 剩余风险
