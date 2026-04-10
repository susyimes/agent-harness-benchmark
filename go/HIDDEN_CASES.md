# HIDDEN_CASES.md

> 本文件供评测方内部使用，不对参测 agent 公开。
> 目标：确保 Go 题目不仅能过公开测试，还能在 goroutine / channel / context / report 稳定性上拉开 agent 框架差距。

## 设计原则

隐藏测试重点覆盖：
1. context cancel 是否真实传播
2. channel close / queue 管理是否安全
3. race / goroutine 泄露
4. report 顺序稳定
5. 大 DAG 下性能退化

建议隐藏测试：18~24 条。

---

## 一、边界类

### HC-01 空 DAG
- 不崩溃
- 输出合法空报告

### HC-02 单节点成功
- 最小可运行闭环正确

### HC-03 重复 task id
- 解析阶段报错

### HC-04 缺失依赖
- validate 阶段报错

### HC-05 复杂交叉环
- 非简单环也能检出
- 不应卡死等待

---

## 二、回归类

### HC-06 channel close 时机错误不得 panic
- 高并发完成后不得出现 send on closed channel

### HC-07 timeout 后 goroutine 必须退出
- context 取消后不能后台继续跑

### HC-08 retry 不得把 cancel 当普通失败
- context canceled 不允许进入 retry

### HC-09 dry-run 零副作用
- 不执行真实回调，不写产物

### HC-10 同一任务只执行一次
- 多上游同时完成时不重复入队

---

## 三、稳定性类

### HC-11 go test -race 下无 data race
- 尤其是汇总、状态表、结果 map

### HC-12 连续运行 20 次结果一致
- 固定 seed，状态和顺序稳定

### HC-13 失败后再次运行无状态污染
- 前一轮失败不影响后一轮成功场景

### HC-14 cancel 后无 goroutine 泄露
- 执行后 goroutine 数恢复到合理水平

---

## 四、输出一致性类

### HC-15 report 顺序稳定
- 不依赖 map 遍历顺序

### HC-16 错误类型稳定
- cycle / timeout / dependency blocked / parse error 可区分

### HC-17 dry-run 与 real-run schema 一致
- 仅字段值不同，不是两套结构

---

## 五、性能 / benchmark 类

### HC-18 1000 宽 DAG 不应明显 O(n^2)
- ready 队列推进合理

### HC-19 1000 链 DAG 不应过多阻塞/轮询
- 线性开销可接受

### HC-20 timeout 风暴场景快速收敛
- 不残留大量后台 goroutine

### HC-21 report 生成近似线性
- 不反复全量扫描 / 深拷贝

---

## 保管建议

- 私有目录：`private-eval/go-hidden/`
- 隐藏 fixtures 与 thresholds 不进公开仓库
