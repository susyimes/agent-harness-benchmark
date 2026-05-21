# agent-harness-benchmark

**Dual-Track Agent Harness Benchmark：标准评测兼容 + 工程实战验证。**

本项目用于评估 agent framework / harness 的真实工程执行能力。它测的不是模型单次回答能力，而是 **模型 + harness + 工具 + 执行环境** 在完整任务链路里的系统级效果。

我们关心一个 agent 系统能否读懂已有工程、定位问题、运行测试、修复回归、补充测试，并稳定交付一个可审查、可复现、可比较的结果。

更多项目理念见：

- [VISION.md](./VISION.md)

## 项目定位

本项目不想做一个“大杂烩 benchmark 集合”。

最合适的路线是：

> **标准 harness 框架做可信背书，实战工程题做核心差异化。**

因此，项目分成两部分：

1. **流行 Harness 框架测试法**：用主流评测框架作为标准化外壳，证明评测协议不是闭门造车。
2. **实战测试法**：保留并强化多语言真实工程任务，测试 agent 的工程闭环能力。

## 第一部分：流行 Harness 框架测试法

这一部分对应 `standard-harness track`。

目标是用主流评测框架包一层标准协议，让本项目可以和现有评测生态对齐，同时仍然保留 agent/harness 系统级任务的特色。

### 首选：Inspect AI

[Inspect AI](https://inspect.aisi.org.uk/) 是本项目优先接入的标准 harness 框架。

原因是本项目测的是 agent framework / harness 系统能力，而 Inspect AI 本身支持：

- coding / agentic tasks
- tool calling
- multi-agent
- sandbox
- 外部 agent 接入
- 日志查看与评测结果分析

这和本项目的目标最贴合：不是只问模型一道题，而是观察一个 agent 系统如何使用工具、运行环境、测试反馈和多轮修复来完成任务。

### 可选校准层：lm-evaluation-harness

[EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) 更适合做模型能力校准，例如 GSM8K、MMLU、BBH、MBPP 等传统 benchmark。

它很成熟，也广泛用于标准学术任务，但它不是本项目的主轴。

在本项目里，它更适合作为可选校准层：

- 跑少量 GSM8K / MBPP / MMLU 子集
- 记录裸模型的基础能力
- 帮助解释 agent harness 提升来自哪里

### 可选兼容层：OpenAI Evals

[OpenAI Evals](https://github.com/openai/evals) 可作为自定义 eval 格式和评测记录方式的参考。

它适合帮助项目形成更规范的数据格式、运行记录和结果输出，但不承担核心工程任务评测。

### 标准 Harness Track 定位

```text
standard-harness track
- Inspect AI：主入口，跑 agent/harness 系统级任务
- lm-evaluation-harness：可选校准层，跑少量 GSM8K / MBPP / MMLU 子集
- OpenAI Evals：可选兼容层，用于自定义 eval 格式参考
```

## 第二部分：实战测试法

这一部分对应 `practical-engineering track`。

这是本项目的核心卖点：多语言真实工程任务。

当前仓库已经天然接近“轻量 SWE-bench 风格”的实战 benchmark：

- 本地 repo
- 失败测试
- 隐藏用例
- 修复闭环
- 补测试要求
- 交付总结
- 可记录的过程指标

[SWE-bench](https://github.com/swe-bench/SWE-bench) 用真实 GitHub issue 测 AI 系统修复能力。本项目采用类似精神，但控制在更轻量、更本地、更适合 harness 对照实验的范围内。

### Practical Engineering Track 定位

```text
practical-engineering track
- Python / Node：第一批主赛道，最成熟，优先跑通
- Java / Swift：第二批，偏 log-query / parser / CLI
- Go / Kotlin：第三批，偏 runner / DAG / timeout / retry
```

## 目标工程结构

后续工程会逐步收敛到以下结构：

```text
agent-harness-benchmark/
  standard-harness/
    inspect-ai/
      tasks/
      solvers/
      scorers/
    lm-eval/
      task-configs/
  practical/
    python/
    node/
    java/
    swift/
    go/
    kotlin/
  shared/
    run_record_schema.json
    scoring.md
    answer_extractors/
    telemetry/
  reports/
    examples/
```

当前仓库仍保留顶层语言目录：

- `python/`
- `node/`
- `java/`
- `swift/`
- `go/`
- `kotlin/`

每个语言目录应包含：

- `README.md`：该语言赛题说明
- `TASK.md`：给 agent 的执行任务说明
- `BASELINE.md`：初始基线项目与预埋问题说明
- `BENCHMARK.md`：benchmark 规则和评分建议
- `HIDDEN_CASES.md`：隐藏测试设计
- `REPO_PLAN.md`：baseline 仓库规划
- `repo-template/`：真实 baseline 样板仓库

## 统一评测协议

最关键的协议是：**同一题目跑两组对照实验**。

```text
A. bare_model
   裸 API / 单轮 / 无工具 / 无调试循环

B. harness_agent
   harness 编排 / 多轮 / 工具 / 反思 / 多 agent / 测试反馈
```

统一记录：

- `pass_rate`
- `hidden_pass_rate`
- `time_to_first_green`
- `time_to_full_green`
- `total_tokens`
- `tool_calls`
- `retries`
- `files_modified`
- `tests_added`
- `final_summary_quality`

最终报告不只回答“分数有没有变高”，还要回答：

- 正确率提升了多少？
- 成本增加了多少？
- 多轮修复是否真的有价值？
- 工具调用是否减少了无效尝试？
- harness 是否比裸模型更稳定？

## 自导向测试发现协议

实战测试法不建议直接把测试命令完整喂给 agent。

更贴近真实工程工作的方式是：让 agent 先读项目，自己判断应该运行哪些测试，然后执行并汇报结果。

这可以作为本项目的核心执行方式之一：

```text
Self-Directed Test Discovery Protocol

1. 给 agent 一个 repo-template
2. 不直接告诉它完整测试命令
3. 要求 agent 先阅读项目结构和文档
4. agent 判断应该运行哪些测试或验证命令
5. agent 汇报：
   - 发现了哪些测试入口
   - 准备执行哪个命令
   - 为什么选择这个命令
6. agent 执行测试并汇报观察到的结果
7. agent 根据失败信息修复代码
8. agent 再次运行测试并汇报最终结果
9. evaluator 独立运行 canonical public tests + hidden tests 复核
```

这一协议测试的不只是代码修改能力，还测试 agent 是否能像真实工程师一样先搞明白：

- 这个项目怎么运行？
- 哪些测试才是有效验证？
- 当前失败是否被准确复现？
- 最终汇报是否和真实测试结果一致？

需要注意：**agent 的汇报不能直接当最终成绩**。

最终成绩必须由 evaluator 独立复核。原因是 agent 可能：

- 只跑了部分测试
- 漏掉集成测试或 benchmark 测试
- 误读测试输出
- 报告“通过”，但实际命令失败
- 只修公开测试，没有覆盖隐藏问题

因此本项目推荐把测试执行拆成两层：

```text
Agent 侧：
- 自己发现测试
- 自己执行测试
- 自己汇报结果

Evaluator 侧：
- 固定 public check
- 固定 hidden check
- 独立复核 agent 的汇报是否准确
```

这一协议可以沉淀为额外评分维度：

- `test_discovery_score`：是否找到正确测试入口
- `report_accuracy_score`：汇报结果是否和真实执行一致
- `debug_loop_score`：是否根据失败信息有效收敛
- `final_correctness_score`：评测方复跑 public / hidden tests 是否通过

## 重点测试能力

本仓库不测试纯算法能力，而重点测试 agent 框架在以下方面的综合表现：

- 代码理解与任务分解
- 多文件修改与局部重构
- 调试、回归修复与补测试
- 长链路执行稳定性
- benchmark 与结果总结
- 工具调用效率
- 在统一约束下的跨语言工程能力

## 统一设计原则

1. 尽量零外部服务、零数据准备
2. 强调本地可运行
3. 难度中高，避免纯 CRUD
4. 强调调试、修复、测试补强与回归控制
5. 尽量让不同 agent 框架在过程质量和最终结果上拉开差距
6. 先做少数高质量任务，再扩展更多语言和框架

## 推荐统一评分维度

- Correctness：功能与测试通过情况
- Robustness：边界处理、回归测试、隐藏问题覆盖
- Performance：benchmark 结果
- Process Quality：中间步骤、总结质量、可审查性
- Tool Efficiency：耗时、重复操作、无效改动

详细评分建议见：

- [SCORING.md](./SCORING.md)

## 推荐起步顺序

### Step 1：先跑通 Python / Node

优先把以下两个目录改造成 practical 第一批正式题：

- `python/repo-template/`
- `node/repo-template/`

这两门语言目前最适合低成本验证 agent 框架。

### Step 2：用 Inspect AI 包一层

为 practical 任务增加 Inspect AI 入口，形成：

- dataset
- solver
- scorer
- run log
- report output

然后跑 `bare_model` vs `harness_agent` 对照。

### Step 3：增加小规模校准集

再接入一个很小的 lm-evaluation-harness 校准集，例如：

- GSM8K 50 题
- MBPP 小样本
- MMLU 小子集

校准集只用于解释模型基础能力，不替代 practical engineering track。

### Step 4：输出统一报告

最终报告应强调：

- 正确率提升多少
- 成本增加多少
- 是否值得使用 harness
- 哪些任务最能体现 harness 价值

## 当前直接使用流程

如果你今天就要跑一次实战 benchmark，可以先从现有目录开始。

### 1. 选择一门语言题

建议优先：

- `python/repo-template/`
- `node/repo-template/`

### 2. 进入 baseline 仓库

```bash
cd python/repo-template
```

或：

```bash
cd node/repo-template
```

### 3. 记录 baseline 初始状态

在把任务交给 agent 之前，先记录：

- 当前 commit hash
- 当前测试命令
- 初始测试结果
- 当前已知失败数

例如：

```bash
python -m pytest -q
npm test
```

### 4. 将任务交给目标 agent framework

建议给 agent 的目标至少包括：

1. 修复当前失败测试
2. 满足 `TASK.md` 描述的能力要求
3. 新增回归测试
4. 保持项目结构清晰
5. 输出修改总结

### 5. 记录交付结果

至少记录：

- 最终测试结果
- 总耗时
- 修改文件数
- 新增测试数
- 是否更新文档
- 是否引入新回归

## 贡献方向

欢迎贡献：

- 完善某个语言的 `repo-template`
- 固定公开测试、隐藏测试和 benchmark 输入规模
- 增加 Inspect AI task / solver / scorer
- 增加 lm-evaluation-harness 小规模校准配置
- 补充统一 run record schema
- 增加 telemetry、token、latency、tool call 统计
- 提交一次真实 agent framework 的运行记录
- 改进文档，让更多人能快速参与
