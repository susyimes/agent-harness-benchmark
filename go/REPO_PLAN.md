# REPO_PLAN.md

> 目标：把 `go/` 目录变成可独立分发、可 benchmark 的 Go baseline 仓库方案。

## 一、仓库定位

题目名称建议：**Go 本地并发任务编排器修复与补强**。

核心考察：
- DAG 调度
- goroutine / channel / context 语义
- timeout / retry / dry-run
- report 稳定性
- race / 泄露 / benchmark 退化

---

## 二、建议目录结构

```text
go/
├─ README.md
├─ TASK.md
├─ BASELINE.md
├─ BENCHMARK.md
├─ HIDDEN_CASES.md
├─ REPO_PLAN.md
├─ repo-template/
│  ├─ go.mod
│  ├─ parser.go
│  ├─ scheduler.go
│  ├─ executor.go
│  ├─ reporter.go
│  ├─ cmd/taskrunner/main.go
│  ├─ testdata/
│  │  ├─ configs/
│  │  └─ expected/
│  ├─ scripts/
│  │  ├─ gen_benchmark_data.go
│  │  └─ run_benchmark.sh
│  └─ *_test.go
└─ private-eval/
   ├─ hidden-tests/
   └─ scorer/
```

---

## 三、基线规模建议

- 代码量：600~900 行
- 公开测试：16~20 个
- 初始失败：5~7 个
- hidden tests：18~24 个

---

## 四、核心模块职责

### parser.go
- 解析 JSON/YAML 配置
- 校验重复 id、缺失依赖、非法字段

### scheduler.go
- 拓扑推进
- ready 队列
- 环检测
- 防重复提交

### executor.go
- goroutine 执行
- context timeout / cancel
- retry
- dry-run
- 并发上限

### reporter.go
- 聚合结果
- 稳定排序
- JSON 输出

---

## 五、建议预埋问题

1. 复杂环漏判
2. send on closed channel 风险
3. timeout 后 goroutine 未退出
4. retry 与 cancel 语义混淆
5. dry-run 仍执行副作用
6. report 顺序不稳定
7. 汇总存在 data race 风险

---

## 六、benchmark 数据生成

通过脚本生成：
- 100 task 宽 DAG
- 1000 task 宽 DAG
- 1000 task 链 DAG
- 1000 task 混合 timeout/retry 场景

固定 seed，保证可复现。

---

## 七、公开发题方式

发布内容：
- repo-template
- 公开测试
- README/TASK/BASELINE/BENCHMARK

不发布：
- hidden tests
- race 阈值与性能阈值
- 参考输出 SHA

---

## 八、评分执行建议

1. `go test ./...`
2. `go test ./... -race`
3. CLI smoke：
   - `go run ./cmd/taskrunner validate ...`
   - `go run ./cmd/taskrunner run ...`
4. hidden tests
5. benchmark 脚本

---

## 九、隐藏测试保管

建议私有目录：

```text
private-eval/go-hidden/
├─ hidden_tests/
├─ fixtures/
└─ thresholds.json
```

---

## 十、完成标准

一个合格的 Go benchmark baseline 应满足：
- 本地 clone 即可跑
- 公开测试与 hidden tests 分层合理
- race / goroutine 泄露可被检测
- benchmark 可重复执行
- 输出稳定可比较
