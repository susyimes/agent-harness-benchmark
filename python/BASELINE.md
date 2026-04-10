# BASELINE.md

## 基线项目描述

一个约 500~800 行的 Python 项目，包含 4 个核心模块：

- `parser.py`：解析 JSON 配置与默认值
- `scheduler.py`：构建 DAG、检测环、生成执行顺序
- `executor.py`：并发执行任务，处理 retry / timeout / dry-run
- `reporter.py`：聚合执行结果并输出 JSON 报告

## 预埋问题建议

1. 重复 task id 未正确报错
2. cycle detection 在某些交叉依赖下漏判
3. topo 顺序不稳定，导致输出偶发变化
4. dry-run 仍然调用了任务 action
5. timeout 只记录失败，未真正取消工作线程
6. retry 会吞掉最后一次异常
7. reporter 统计 duration 时忽略重试开销
8. 报告中任务顺序依赖并发完成顺序

## 测试建议

- 总测试数固定 15 个
- 初始失败数 5~7 个
- 包含单测 + 1~2 个 e2e 用例

## 隐含难点

- 一处修复可能引入另一处 nondeterminism
- timeout 与 retry 的交互容易写错
- 公开测试通过后仍可能在大 DAG benchmark 下出现性能退化
