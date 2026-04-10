# BASELINE.md

## 基线项目描述

4 个核心文件：

- `parser.go`
- `scheduler.go`
- `executor.go`
- `reporter.go`

建议配 15 个测试，初始失败 5~7 个。

## 预埋问题建议

1. cycle detection 对复杂交叉环漏判
2. goroutine 退出时 channel close 时机错误，偶发 panic
3. context timeout 后 worker 未及时退出
4. retry 与 timeout 组合时状态不一致
5. dry-run 仍执行真实回调
6. report map 遍历顺序导致输出不稳定
7. 统计汇总存在 data race 风险

## 隐藏考点

- `go test -race` 下是否暴露问题
- 取消后 goroutine 是否泄露
- 1000 task 下 channel / queue 设计是否有明显阻塞
