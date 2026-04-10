# REPO_PLAN.md

> 目标：把 `python/` 目录完善成一个可独立分发、可公开测试、可私有隐藏评测的 Python benchmark baseline。

## 一、仓库定位

题目名称建议：**Python 本地事件账本任务队列修复与补强**。

核心考察：
- 文件账本恢复
- worker 执行一致性
- retry / 幂等 / 恢复
- CLI 与 metrics 契约
- 测试补强

不考察：
- 外部消息队列
- 数据库
- 分布式系统

---

## 二、建议目录结构

```text
python/
├─ README.md
├─ TASK.md
├─ BASELINE.md
├─ BENCHMARK.md
├─ HIDDEN_CASES.md
├─ REPO_PLAN.md
├─ repo-template/
│  ├─ pyproject.toml
│  ├─ app/
│  │  ├─ models.py
│  │  ├─ storage.py
│  │  ├─ queue.py
│  │  ├─ worker.py
│  │  ├─ retry.py
│  │  ├─ metrics.py
│  │  ├─ cli.py
│  │  └─ utils.py
│  ├─ data/
│  │  ├─ seed_jobs.json
│  │  └─ corrupted_events.log
│  ├─ tests/
│  │  ├─ test_storage.py
│  │  ├─ test_queue.py
│  │  ├─ test_worker.py
│  │  ├─ test_retry.py
│  │  ├─ test_metrics.py
│  │  ├─ test_cli.py
│  │  └─ test_regression.py
│  ├─ scripts/
│  │  ├─ run_demo.py
│  │  └─ gen_benchmark_data.py
│  └─ benchmark-output/
│     └─ .gitkeep
└─ private-eval/
   ├─ hidden-tests/
   └─ scorer/
```

---

## 三、基线规模建议

- 代码量：700~1100 行
- 测试：18~22 个公开测试
- 初始失败数：6~8 个
- hidden tests：18~24 个

---

## 四、核心模块职责

### storage.py
- 追加 JSON Lines 事件
- 回放事件恢复最终状态
- 容忍坏行

### queue.py
- 入队、去重、拉取待执行任务
- 防止重复消费

### worker.py
- 执行任务
- 处理成功 / 失败 / retry / 恢复

### retry.py
- 明确重试上限与等待策略
- 统一 attempt 计数语义

### metrics.py
- 统一统计口径
- 给 CLI 和 benchmark 共用

### cli.py
- `enqueue`
- `run-once`
- `run-until-empty`
- `status`
- `list`
- `show`
- `metrics`
- `rebuild-index`

---

## 五、建议预埋问题

1. 回放状态机错误
2. retry off-by-one
3. 重复 job_id 未拦截
4. 多 worker 重复消费风险
5. 坏日志直接崩溃
6. CLI 与 metrics 口径不一致
7. rebuild-index 非幂等

---

## 六、benchmark 数据生成

通过 `scripts/gen_benchmark_data.py` 生成：

- 100 jobs 基础队列
- 1000 jobs 基础队列
- 1000 jobs 混合失败/重试队列
- 1000 jobs 损坏日志恢复场景

固定随机种子，保证可复现。

---

## 七、公开发题方式

对外发布时提供：
- `repo-template/`
- 公开测试
- README / TASK / BASELINE / BENCHMARK

不提供：
- hidden tests
- scorer 阈值
- 参考 benchmark 结果

---

## 八、评分执行建议

1. 先跑公开测试：`pytest`
2. 再跑 CLI smoke：
   - `python -m app.cli status`
   - `python -m app.cli metrics`
3. 再跑 hidden tests
4. 再跑 benchmark 脚本

统一记录：
- time_to_green
- tests_added
- files_modified
- hidden_pass_rate
- benchmark_summary

---

## 九、隐藏测试保管

建议放在私有目录：

```text
private-eval/python-hidden/
├─ hidden_tests/
├─ fixtures/
└─ thresholds.json
```

---

## 十、完成标准

一个可独立发给其他 agent 框架的 Python benchmark baseline，至少应满足：

- clone 后本地可直接运行
- 公开任务边界清晰
- 初始有稳定可复现失败
- hidden tests 能拉开差距
- benchmark 可重复执行
- 输出可比较
