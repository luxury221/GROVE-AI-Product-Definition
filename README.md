# GROVE-AI

> 面向安克多产品线的证据驱动 AI 产品定义决策系统：把分散的用户、市场与工程证据，转化为可追溯、可验证、可进入人工决策 Gate 的产品机会。

**项目状态：入围遴选前优化。** 本仓库公开展示方法、模板和开题阶段样例；正式历史回测、硬件实验和商业效果仍为 `Planned`，不得视为已完成结果。

## 安克面对的问题

安克面向多国家、多渠道、多语言和多产品线。问题并非缺少信息，而是证据分散、口径不一、工程约束进入决策过晚，一次项目形成的知识也难以复用。传统人工整理容易造成证据损耗、重复沟通、功能堆叠和风险后置。

## GROVE-AI 解决什么

GROVE-AI 将 Evidence Ledger、JTBD、多角色审查、工程红队和历史时间切分回测组织为一套产品决策流程：

1. 统一编码用户反馈、竞品规格、独立评测、标准与工程约束；
2. 只在证据 Gate 通过后生成产品机会；
3. 分离提案者、工程/商业审查者、红队与审计者；
4. 用历史时点之后的真实观察检验预测，避免事后合理化；
5. 保留产品负责人的最终决策权，并沉淀可复用的品牌知识资产。

## 与普通 AI 工具的差异

| 方案 | 主要输出 | 证据约束 | 独立审查 | 可回测 | 人工 Gate |
|---|---|---:|---:|---:|---:|
| 评论总结工具 | 主题摘要 | 弱 | 否 | 否 | 否 |
| 单模型产品生成 | 概念清单 | 可选 | 否 | 否 | 可选 |
| 通用多智能体框架 | 角色协作结果 | 可选 | 部分 | 可选 | 可选 |
| **GROVE-AI** | 可审计的机会、约束与决策记录 | **强制** | **生成/审查分离** | **历史时间切分** | **强制** |

普通工具帮助产品经理更快生成答案；GROVE-AI 首先判断证据是否足以支持决策，再验证答案是否可靠。

## 项目层级

```text
GROVE-AI                     主方案：企业产品定义决策系统
└── 10,000mAh 磁吸充电宝     首个验证品类
    └── Compass 10K          示范产品（Hypothesis）
        └── PowerPilot AI    产品内部能力（Hypothesis）

飞书工作台                  入围后的协作与治理载体（Planned）
```

磁吸充电宝之所以被选为首个案例，是因为功率、温升、结构、容量、认证和用户反馈都可量化；它不是 GROVE-AI 的能力边界。仓库同时提供 [Soundcore 真无线耳机微型适配](docs/SOUNDCORE_MICRO_ADAPTER.md)，展示跨品类迁移方式。

## 企业价值闭环

![GROVE-AI 安克产品定义价值闭环：从外部证据输入，经 AI 分析、人工决策、新品定义与 MVP，最终沉淀为可复用的企业知识资产](assets/grove-ai-anker-product-definition-value-loop.png)

价值覆盖信息处理效率、决策质量、工程风险前置、跨团队协作和品牌知识资产沉淀。详见 [BUSINESS_VALUE.md](BUSINESS_VALUE.md)。

## 当前完成状态

| 状态 | 内容 |
|---|---|
| `Completed` | GROVE-AI 方法框架、Skill、模板、Schema、基础验证脚本、小规模公开资料样例 |
| `Completed` | Compass 10K 概念假设、Soundcore 微型适配设计、正式回测协议 |
| `In Progress` | 比赛表达优化、报名材料收敛、样本和数据规则冻结 |
| `Planned` | 20+ 同品类 SKU、500+ 去重反馈的正式历史回测与消融 |
| `Planned` | 飞书治理工作台、Compass 10K MVP 与热/功率/结构实验 |
| `Hypothesis` | RangeView、RouteCharge、DockCable、PowerPilot AI 的产品与工程效果 |

`Completed` 表示文档、方法或样例已形成，不表示产品效果、商业收益或实验指标已经得到验证。

## 入围后 14 天交付

交付分为证据底座、机会排序、工程/商业审查、历史回测、产品收敛、第二品类适配和工作台演示。每一天都有可检查的产物和人工 Gate，详见 [ROADMAP_14_DAYS.md](ROADMAP_14_DAYS.md)。

## 快速查看

- [两部分报名摘要](EXECUTIVE_SUMMARY.md)
- [安克业务价值](BUSINESS_VALUE.md)
- [14 天实施路线图](ROADMAP_14_DAYS.md)
- [完整开题报告（附件）](docs/GROVE-AI_Research_Proposal.md)
- [Compass 10K 示范概念](docs/COMPASS_10K_CONCEPT.md)
- [被 GROVE-AI 否决的功能堆叠反例](docs/COMPASS_10K_CONCEPT.md#被否决的反例maggo-all-in-one-max)
- [Soundcore 第二品类微型适配](docs/SOUNDCORE_MICRO_ADAPTER.md)
- [正式回测协议](docs/BACKTEST_PROTOCOL.md)
- [GROVE-AI Skill](grove-ai-product-definition/SKILL.md)
- [Issue #1 优化路线图](ISSUE_1_OPTIMIZATION_ROADMAP.md)

## 使用 Skill

将整个 `grove-ai-product-definition/` 文件夹安装到支持 Agent Skills 的环境，或直接让智能体读取其中的 `SKILL.md`。示例指令：

```text
使用 GROVE-AI，对目标消费电子品类建立可追溯 Evidence Ledger，
在 Gate G 通过后形成一个核心 JTBD，并设计严格时间切分的历史回测。
所有结论区分 FACT、INFERENCE、HYPOTHESIS，所有交付标记状态。
```

基础脚本：

```bash
python grove-ai-product-definition/scripts/score_opportunities.py <input.csv> <output.csv>
python grove-ai-product-definition/scripts/validate_run.py <runs/run_id>
python grove-ai-product-definition/scripts/backtest_metrics.py <predictions.csv> <observations.csv> <metrics.json>
```

## 许可证

Copyright © 2026 GROVE-AI Project Contributors. All rights reserved.

本仓库是 2026 AI 先锋未来人才大赛安克创新赛道的参赛项目，仅授权赛事主办方、安克创新及评审人员为赛事评审和验证目的使用。未经书面许可，不得复制、修改、传播、用于其他比赛、制作衍生项目或用于商业用途。具体条款参见 [LICENSE](LICENSE)。
