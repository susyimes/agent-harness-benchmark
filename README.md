# agent-harness-benchmark

用于测试 agent 框架性能的多语言题库仓库。

## 目标

本仓库不测试纯算法能力，而重点测试 agent 框架在以下方面的综合表现：

- 代码理解与任务分解
- 多文件修改与局部重构
- 调试、回归修复与补测试
- 长链路执行稳定性
- benchmark 与结果总结
- 在统一约束下的跨语言工程能力

## 语言目录

- `python/`
- `java/`
- `go/`
- `kotlin/`
- `swift/`
- `node/`

每个语言目录应包含：

- `README.md`：该语言赛题说明
- `TASK.md`：给 agent 的执行任务说明
- `BASELINE.md`：初始基线项目与预埋问题说明
- `BENCHMARK.md`：benchmark 规则和评分建议

## 统一设计原则

1. 尽量零外部服务、零数据准备
2. 强调本地可运行
3. 难度中高，避免纯 CRUD
4. 强调调试、修复、测试补强与回归控制
5. 尽量让不同 agent 框架在过程质量和最终结果上拉开差距

## 推荐统一评分维度

- Correctness：功能与测试通过情况
- Robustness：边界处理、回归测试、隐藏问题覆盖
- Performance：benchmark 结果
- Process Quality：中间步骤、总结质量、可审查性
- Tool Efficiency：耗时、重复操作、无效改动
