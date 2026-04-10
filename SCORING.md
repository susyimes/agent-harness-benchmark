# SCORING.md

本仓库用于评估 agent 框架在真实工程修复任务中的表现。

## 通用评分维度（100 分）

- Correctness（40）
  - 公开测试通过率
  - 隐藏测试通过率
  - 功能完成度
- Robustness（20）
  - 边界处理
  - 回归测试补强
  - 输出稳定性
- Performance（10）
  - benchmark 场景表现
  - 明显低效实现惩罚
- Process Quality（20）
  - 是否先复现问题再修复
  - 是否分阶段推进
  - 是否做最终回归验证
- Delivery Quality（10）
  - README / TASK / benchmark 说明是否一致
  - 交付是否可独立运行

## 通用采集指标

- time_to_first_green
- time_to_full_green
- tests_added
- files_modified
- total_tool_calls
- repeated_failed_loops
- hidden_tests_passed

## 统一交付要求

每个语言题目目录应至少包含：

- README.md
- TASK.md
- BASELINE.md
- BENCHMARK.md
- HIDDEN_CASES.md
- REPO_PLAN.md

并明确：

- baseline 仓库结构
- 初始失败测试规模
- 公开/隐藏考点
- benchmark 输入规模
- 对外发题方式
