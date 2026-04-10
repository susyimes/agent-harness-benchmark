# REPO_PLAN.md

> 目标：把 `node/` 目录完善成可独立分发、可 benchmark 的 Node.js baseline 仓库方案。

## 一、仓库定位

题目名称建议：**Node.js mini-ci-runner 修复与补强**。

核心考察：
- pipeline 调度
- Promise / 子进程状态管理
- retry / timeout / artifact
- CLI 契约
- 测试补强与稳定性

---

## 二、建议目录结构

```text
node/
├─ README.md
├─ TASK.md
├─ BASELINE.md
├─ BENCHMARK.md
├─ HIDDEN_CASES.md
├─ REPO_PLAN.md
├─ repo-template/
│  ├─ package.json
│  ├─ src/
│  │  ├─ cli.js
│  │  ├─ runner.js
│  │  ├─ scheduler.js
│  │  ├─ task-loader.js
│  │  ├─ logger.js
│  │  └─ utils/
│  ├─ fixtures/
│  │  ├─ pipelines/
│  │  └─ workspace/
│  ├─ tests/
│  │  ├─ cli.test.js
│  │  ├─ runner.test.js
│  │  ├─ scheduler.test.js
│  │  ├─ retry.test.js
│  │  ├─ timeout.test.js
│  │  ├─ artifact.test.js
│  │  └─ integration/
│  ├─ scripts/
│  │  ├─ gen_benchmark_data.js
│  │  └─ run_benchmark.sh
│  └─ benchmark-output/
│     └─ .gitkeep
└─ private-eval/
   ├─ hidden-tests/
   └─ scorer/
```

---

## 三、基线规模建议

- 代码量：700~1000 行
- 公开测试：16~22 个
- 初始失败：6~8 个
- hidden tests：18~24 个

---

## 四、核心模块职责

### scheduler.js
- DAG 调度
- ready 队列
- 防重复提交

### runner.js
- 任务执行主流程
- retry / timeout / artifact / 状态流转

### cli.js
- run / validate / inspect（可选）
- exit code / stdout / stderr 契约

### task-loader.js
- 解析 pipeline 配置
- 校验重复 task、缺失依赖、非法字段

### logger.js
- 结构化日志与 benchmark 输出分离

---

## 五、建议预埋问题

1. 依赖任务提前执行
2. retries off-by-one
3. timeout 后子进程未清理
4. CLI 退出码与结果不一致
5. artifact 路径不稳定
6. Promise / callback 竞争导致状态污染
7. report 顺序不稳定

---

## 六、benchmark 数据生成

脚本生成：
- 100 task 基础 pipeline
- 1000 task 宽 pipeline
- 1000 task 链 pipeline
- 1000 task 混合 flaky / timeout / artifact pipeline

固定 seed，保证可复现。

---

## 七、公开发题方式

公开提供：
- repo-template
- 公开测试
- README/TASK/BASELINE/BENCHMARK

不公开：
- hidden tests
- 私有 scorer
- 参考 benchmark 输出

---

## 八、评分执行建议

1. `npm test`
2. CLI smoke：
   - `node src/cli.js run ...`
3. hidden tests
4. benchmark 脚本
5. 检查是否有残留子进程

---

## 九、隐藏测试保管

建议私有目录：

```text
private-eval/node-hidden/
├─ hidden_tests/
├─ fixtures/
└─ thresholds.json
```

---

## 十、完成标准

一个合格的 Node.js benchmark baseline 应满足：
- 本地 clone 后可直接跑
- timeout / retry / artifact / CLI 契约可测
- hidden tests 能区分真假修复
- benchmark 可重复执行
- 无悬挂子进程和明显输出漂移
