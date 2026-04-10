# HIDDEN_CASES.md

> 本文件供评测方内部使用，不对参测 agent 公开。
> 目标：把 Python 赛题推进到可独立对外做 benchmark 的程度，并防止只针对公开测试做表面修补。

## 设计原则

隐藏测试重点不是刁难，而是验证：

1. 状态机语义是否真的正确
2. 事件账本恢复是否稳健
3. CLI / 内部状态 / metrics 口径是否一致
4. 输出是否稳定可比较
5. 修复后是否引入明显性能退化

建议隐藏测试总数：18~24 条。

---

## 一、边界类隐藏测试

### HC-01 空 seed 输入
- 输入：空任务列表
- 期望：
  - 不崩溃
  - 可输出空状态
  - metrics / status 口径一致

### HC-02 重复 job_id
- 输入：重复 job_id 的 seed 数据
- 期望：
  - enqueue 阶段即报错或拒绝
  - 不允许进入执行后再混乱覆盖

### HC-03 坏日志尾部
- 输入：JSON Lines 最后一行被截断
- 期望：
  - 恢复时跳过坏尾行
  - 其他历史事件仍可正确回放

### HC-04 未知事件类型
- 输入：混入未知 event type
- 期望：
  - 系统降级处理
  - 不整体崩溃
  - metrics 中可计入 warning / malformed

---

## 二、回归类隐藏测试

### HC-05 RUNNING->FAILED->RETRY_SCHEDULED->RUNNING->SUCCESS 回放正确
- 期望最终状态为 SUCCESS
- 防止恢复逻辑只看“最近一次失败”

### HC-06 retry 边界 off-by-one
- `max_retries=2` 时总尝试次数必须与定义一致
- 不允许只跑 2 次或多跑到 4 次

### HC-07 同一 job 不得重复成功提交
- 多 worker 场景下同一 job 最多成功一次
- 不允许重复消费导致双 success

### HC-08 rebuild-index 幂等
- 连续多次执行 rebuild-index
- 结果一致，不重复膨胀索引或计数

### HC-09 metrics 与 list/show/status 口径一致
- 同一批任务下多种 CLI 命令结果互相校验
- 防止各命令各算各的

---

## 三、稳定性类隐藏测试

### HC-10 连续运行 20 次结果一致
- 固定 seed、固定日志
- 状态汇总和输出顺序完全一致

### HC-11 崩溃恢复后再次运行不受污染
- 第一次中途失败
- 第二次恢复运行
- 不受上次临时状态污染

### HC-12 坏数据混杂合法数据
- 空行、坏 JSON、重复事件、顺序轻微错乱混在一起
- 系统仍能恢复大部分合法状态

### HC-13 CLI 错误码稳定
- 参数错误、文件不存在、内部恢复失败
- exit code 与 stderr 行为稳定

---

## 四、输出一致性类隐藏测试

### HC-14 JSON / 文本输出顺序稳定
- list / show / metrics 输出字段顺序稳定
- 不依赖 dict 遍历顺序

### HC-15 错误信息模板稳定
- 至少包含错误类别关键词
- 不输出随机地址、堆栈噪音作为主信息

### HC-16 metrics 字段定义稳定
- total / queued / running / success / failed / retrying 等字段固定
- 不允许一次叫 failed，一次叫 errorCount

---

## 五、性能 / benchmark 退化测试

### HC-17 1000 job 回放不得明显 O(n^2)
- 回放时间与 100 job 比较不能异常恶化

### HC-18 1000 job enqueue + run-until-empty 总耗时合理
- 防止为求正确性引入极重全量扫描

### HC-19 大日志恢复不应整文件多轮重复 parse
- 同一恢复流程中不应反复全量读日志多次

### HC-20 metrics/report 构建不应成为主要瓶颈
- 状态已恢复时，统计输出应近似线性

---

## 隐藏测试保管建议

- 不放入公开仓库
- 存于私有评测目录：`private-eval/python-hidden/`
- 失败时仅回传类别，不回传具体断言
