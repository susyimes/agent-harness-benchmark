# TRACKS.md

## 目标

将 6 门语言的 benchmark 题库完善到可以单独拿出去测试其他 agent 框架。

## 设计原则

1. 零外部服务
2. 尽量零数据准备
3. 本地可运行
4. 中高难度，强调调试、修复、测试补强
5. 每门语言可独立发题和评分

## 两大题型家族

### Runner 家族
- python
- go
- kotlin
- node

共性：
- DAG / pipeline / workflow / task runner
- 并发 / retry / timeout / cancel / dry-run / report
- 重点测执行链路与状态一致性

### Log / Query 家族
- java
- swift

共性：
- 本地日志查询 / 检索 / 统计 / 脱敏
- parser / filter / sort / stats / CLI/API
- 重点测代码理解、边界修复、输出稳定性

## 下一阶段产物要求

每门语言目录需要进一步补齐：

- benchmark 可执行方案说明
- baseline 仓库蓝图
- 隐藏测试设计
- 公开评测流程
- benchmark 结果模板
