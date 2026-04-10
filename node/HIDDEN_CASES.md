# HIDDEN_CASES.md

> 本文件供评测方内部使用，不对参测 agent 公开。
> 目标：确保 Node.js 赛题能真正测试 agent 框架在异步状态管理、子进程清理、artifact 传递和输出稳定性上的能力。

## 设计原则

隐藏测试重点覆盖：
1. Promise / callback 状态竞争
2. timeout 后子进程清理
3. retry / timeout 交互
4. artifact 链稳定性
5. CLI 退出码与日志一致性
6. benchmark 退化点

建议隐藏测试：18~24 条。

---

## 一、边界类

### HC-01 空 pipeline
- 不崩溃
- 输出合法空结果

### HC-02 单任务成功
- 最小闭环正确

### HC-03 重复 task id
- 配置校验阶段报错

### HC-04 缺失依赖
- 运行前失败，不进入执行

### HC-05 复杂环依赖
- 非简单环也能检出

---

## 二、回归类

### HC-06 retries 边界 off-by-one
- `retries:2` 的尝试次数必须与定义一致

### HC-07 timeout 后子进程必须真正退出
- 不允许 test 结束后仍挂住

### HC-08 timeout 不得被错误重试
- abort / timeout 应区别于普通失败

### HC-09 同一依赖子任务不得重复执行
- 多上游同时完成时只触发一次

### HC-10 artifact 相对路径在不同 cwd 下仍稳定
- 不得依赖调用目录偶然正确

---

## 三、稳定性类

### HC-11 连续运行 20 次结果一致
- 固定 seed
- 输出与状态稳定

### HC-12 无悬挂子进程
- benchmark 或测试结束后无遗留 node 子进程

### HC-13 flaky 任务重试成功后状态正确
- 不保留第一次失败污染

### HC-14 invalid config 错误信息稳定
- 提前失败、stderr 清晰、exit code 正确

---

## 四、输出一致性类

### HC-15 report 顺序稳定
- 不依赖 Promise 完成顺序

### HC-16 stdout/stderr 分流稳定
- 错误输出不混到正常结构化结果中

### HC-17 CLI 成功/失败退出码稳定
- success=0, failure!=0

---

## 五、性能 / benchmark 类

### HC-18 1000 task 宽 pipeline 不被偷偷串行化
- 防止全局 await 串行

### HC-19 1000 task 链 pipeline 调度开销合理
- 防止重复全量扫描 ready 集合

### HC-20 timeout 风暴下快速收敛
- 不残留超时子进程

### HC-21 report 构建近似线性
- 不做重复深拷贝 / 拼接

---

## 保管建议

- 私有目录：`private-eval/node-hidden/`
- hidden fixtures / thresholds 不进公开仓库
