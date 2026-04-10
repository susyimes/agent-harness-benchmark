# AGENT_FRAMEWORK_USAGE.md

本文件面向**其他 agent 框架的使用者 / 评测者**。

它说明如何使用本仓库中的多语言 baseline 题目，对不同 agent 框架进行工程能力 benchmark。

---

## 1. 仓库定位

`agent-harness-benchmark` 不是算法题仓库，也不是语言教程仓库。

它的目标是测试 agent 框架在真实工程任务中的表现，包括：

- 阅读已有代码
- 理解多文件结构
- 运行测试并定位问题
- 修复 bug
- 补回归测试
- 保持输出和文档一致
- 在长链路任务中稳定收敛

更直接地说：

> 这个仓库测的是 **agent framework 的工程执行能力**，而不是模型单次生成代码的表面能力。

---

## 2. 适用对象

本仓库适用于以下类型的 agent / agent framework：

- coding agent
- IDE agent
- CLI agent
- multi-step orchestration agent
- thread/session based coding assistant
- research / benchmark harness

如果一个系统支持：

1. 读取本地代码仓库
2. 修改文件
3. 运行命令
4. 反复调试测试

那么它就适合使用本仓库进行 benchmark。

---

## 3. Benchmark 关注的能力

建议重点观察以下维度：

### 3.1 Correctness
- 能否修复失败测试
- 能否满足题面要求
- 能否处理边界情况

### 3.2 Robustness
- 是否会补回归测试
- 是否会处理脏数据 / timeout / cancel / malformed 输入
- 是否会保持输出稳定

### 3.3 Process Quality
- 是否先跑测试再改代码
- 是否能分阶段推进
- 是否会在最后做回归验证

### 3.4 Delivery Quality
- 是否更新 README / 说明
- 是否能输出清晰总结
- 是否交付了可复现结果

### 3.5 Performance
- 是否在 benchmark 场景下明显退化
- 是否靠过度串行化换正确性
- 是否留下悬挂进程 / 协程 / goroutine / 线程

---

## 4. 仓库结构说明

### 顶层文件

- `SCORING.md`：统一评分维度
- `TRACKS.md`：赛道分类（runner / log-query）
- `ROADMAP.md`：仓库推进路线
- `AGENT_FRAMEWORK_USAGE.md`：本文件

### 每门语言目录

每个语言目录通常包含：

- `README.md`：语言题目简介
- `TASK.md`：给 agent 的任务说明
- `BASELINE.md`：基线项目与预埋问题
- `BENCHMARK.md`：benchmark 规则
- `HIDDEN_CASES.md`：评测方内部用的隐藏测试设计
- `REPO_PLAN.md`：该语言 baseline 仓库规划
- `repo-template/`：真实 baseline 样板仓库

---

## 5. 赛道说明

本仓库大致分成两类题型。

### 5.1 Runner 家族
适合测试：
- DAG / pipeline / workflow / task runner
- 并发
- retry
- timeout / cancel
- dry-run
- report 输出

当前语言：
- Python
- Go
- Kotlin
- Node

### 5.2 Log / Query 家族
适合测试：
- parser 容错
- 搜索 / 过滤 / 排序
- 统计逻辑
- 脱敏
- CLI / API 一致性
- 输出稳定性

当前语言：
- Java
- Swift

---

## 6. 当前成熟度状态

### 6.1 当前最适合直接拿来跑 agent 验证的

#### Python
位置：`python/repo-template/`

特点：
- 已本地运行验证
- 有稳定失败测试
- 适合作为第一门 benchmark 题

#### Node
位置：`node/repo-template/`

特点：
- 已本地运行验证
- timeout / retry / DAG 调度缺陷明显
- 很适合测试 agent 框架的工程闭环能力

### 6.2 已有 baseline 样板，但建议补环境后再正式 benchmark 的

#### Java
位置：`java/repo-template/`

状态：
- baseline 结构已成型
- 当前仓库作者环境缺 Maven，未完成本地验证

#### Go
位置：`go/repo-template/`

状态：
- baseline 结构已成型
- 当前仓库作者环境缺 Go toolchain，未完成本地验证

#### Kotlin
位置：`kotlin/repo-template/`

状态：
- baseline 结构已成型
- 仍需进一步增强运行便利性（如 wrapper / 验证）

#### Swift
位置：`swift/repo-template/`

状态：
- baseline 结构已成型
- 当前仓库作者环境缺 Swift toolchain，未完成本地验证

---

## 7. 推荐使用流程

### Step 1：选择一门语言题

如果你想先低成本验证 agent 框架，建议优先：

- `python/repo-template/`
- `node/repo-template/`

### Step 2：进入 baseline 仓库

例如：

```bash
cd python/repo-template
```

或：

```bash
cd node/repo-template
```

### Step 3：记录 baseline 初始状态

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

### Step 4：将任务交给目标 agent framework

建议给 agent 的目标至少包括：

1. 修复当前失败测试
2. 满足 `TASK.md` 描述的能力要求
3. 新增回归测试
4. 保持项目结构清晰
5. 输出修改总结

### Step 5：记录交付结果

至少记录：

- 最终测试结果
- 总耗时
- 修改文件数
- 新增测试数
- 是否更新文档
- 是否引入新回归

---

## 8. 推荐记录模板

建议使用统一 JSON 或 markdown 模板记录一次 benchmark。

### JSON 示例

```json
{
  "language": "python",
  "framework": "your-agent-framework",
  "baseline_commit": "HEAD",
  "initial_result": "11/13 passed",
  "final_result": "13/13 passed",
  "time_minutes": 24,
  "files_modified": 6,
  "tests_added": 4,
  "notes": [
    "fixed corrupted log tolerance",
    "fixed run_until_empty progression"
  ]
}
```

### Markdown 示例

```markdown
## Benchmark Record

- Language: python
- Framework: your-agent-framework
- Baseline commit: HEAD
- Initial tests: 11/13 passed
- Final tests: 13/13 passed
- Time spent: 24 minutes
- Files modified: 6
- Tests added: 4
- Notes:
  - fixed corrupted log tolerance
  - fixed run_until_empty progression
```

---

## 9. 评分建议

统一评分请参考：

- `SCORING.md`

建议至少从以下几个维度打分：

- Correctness
- Robustness
- Performance
- Process Quality
- Delivery Quality

如果你只做轻量比较，至少记录：

1. 是否修复公开测试
2. 是否补测试
3. 是否引入新问题
4. 是否有稳定、清晰的交付说明

---

## 10. 公平测试建议

为了避免不同 agent 框架的 benchmark 结果失真，建议遵守以下原则：

### 10.1 固定起点
- 所有 agent 使用同一个 baseline commit
- 不允许一个框架拿到更“干净”的起始仓库

### 10.2 固定环境
- 尽量在相同机器 / 相同语言版本下运行
- 至少记录 Python / Node / Java / Go / Kotlin / Swift 版本

### 10.3 固定权限边界
- 是否允许联网
- 是否允许安装依赖
- 是否允许人工中途提示
- 是否允许修改测试

这些都要在 benchmark 记录中明确写清。

### 10.4 不提前泄露 hidden cases
- `HIDDEN_CASES.md` 是评测方资产
- 不应直接发给参测 agent
- agent 只应看到 README / TASK / BASELINE / BENCHMARK / repo-template

### 10.5 不要只看最终是否全绿
很多 agent 会通过：
- 过度重构
- 删除测试
- 放宽断言
- 硬编码输出

来“做绿”测试。

因此建议同时检查：
- 修改范围是否合理
- 是否补了高质量测试
- 是否保持了项目结构可维护
- 是否引入了新的回归风险

---

## 11. 当前局限

请注意：本仓库当前已经具备多语言 baseline 雏形，但成熟度并不完全一致。

### 当前最成熟
- Python
- Node

### 当前仍在提升可运行性
- Java
- Go
- Kotlin
- Swift

因此，如果你今天就要开始 benchmark，建议优先从 Python / Node 开始。

---

## 12. 推荐起步方案

如果你是第一次使用本仓库，推荐这样开始：

### 第一轮
- 使用 `python/repo-template/`
- 使用 `node/repo-template/`

这两门语言已经足够用于：
- 测试 agent 是否会跑测试
- 是否会定位关键 bug
- 是否会补测试
- 是否能稳定完成修复闭环

### 第二轮
在环境完善后，再加入：
- Java
- Go
- Kotlin
- Swift

这样能够形成更完整的跨语言 benchmark 矩阵。

---

## 13. 一句话总结

如果你想把这个仓库直接用于测试 agent 框架，请记住两点：

1. **先从 Python / Node 开始，它们目前最可直接用。**
2. **不要只看是否测过，要看修复过程、测试补强和交付质量。**

这才是这个仓库真正要测的东西。
