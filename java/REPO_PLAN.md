# REPO_PLAN.md

本文件是 Java 语言 baseline 仓库的落地规划摘要。

目标：将 `java/` 目录发展为可独立分发、可公开测试、可私有隐藏评测的 benchmark baseline。

建议内容：
- repo-template/ 下使用 Maven + JDK 17+
- 核心主类：ConfigParser / DagScheduler / JobExecutor / ReportBuilder
- 公开测试：16~22 个
- 初始失败：6~8 个
- hidden tests：18~24 个
- benchmark 数据：wide-1000 / chain-1000 / mixed-retry-timeout / cancel-storm
- 对外发布公开题面与公开测试，不发布 hidden tests / scorer / thresholds

详细版本以私有评测规划文档为准。
