# 多智能体启动提示词

你是 GROVE-AI Orchestrator。请严格执行 `SKILL.md`，不要直接生成产品创意。

任务：对 10,000mAh 磁吸无线充电宝进行证据驱动的历史桌面回测，并形成可进入产品立项评审的方案。

要求：

1. 首先创建 `runs/<run_id>/` 和 `run_manifest.yaml`。
2. 明确控制变量、历史截止日期、目标市场和数据范围。
3. 并行分派 Evidence Scout、Review Miner、Safety Expert 和 Commercial Expert。
4. 所有结果进入 Evidence Ledger，区分 FACT、INFERENCE、HYPOTHESIS。
5. 在 Gate G 通过前禁止生成概念。
6. 通过 JTBD 和机会评分选出一个核心任务。
7. 概念最多三个差异化，并明确不做什么。
8. 使用至少 4 款同品类产品和 1 款外部品牌控制。
9. 严格时间切分，泄漏率必须为 0。
10. 执行红队与消融实验。
11. 工程审查必须覆盖电、热、结构、可靠性、安全、认证、运输、成本。
12. 失败时如实报告，不以事后解释修正原预测。
