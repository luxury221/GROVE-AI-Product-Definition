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

| 对象 | 状态 | 说明 |
|---|---|---|
| GROVE-AI 方法与 Skill | `Completed` | 方法、模板、Schema 和脚本已形成并通过基础验证 |
| Compass 10K 概念 | `In Progress` | Design artifact: `Completed`；Empirical validation: `Planned` |
| Soundcore 微型适配 | `In Progress` | Design artifact: `Completed`；Empirical validation: `Planned` |
| 正式历史回测 | `Planned` | Protocol: `Completed`；Execution: `Planned` |
| 飞书工作台与 Compass MVP | `Planned` | 入围后搭建与验证 |
| RangeView、RouteCharge、DockCable、PowerPilot AI 效果 | `Hypothesis` | 需要用户、工程和基线实验验证 |

`Completed` 只用于已存在、可复现并通过对应 Gate 的对象。设计产物完成但实证未完成时，使用复合状态，不把产品效果、商业收益或实验指标写成结果。

## 入围后 14 天交付

计划采用两档范围。**必达交付**包括 10–15 个核心 SKU、300+ 去重反馈、1 个完整历史回测案例、1 个基线、1 个消融、Compass 10K 提案和飞书端到端工作台；**挑战目标**包括 20+ SKU、500+ 去重反馈、Soundcore 微型迁移及更多回测时间点与外部品牌控制。详见 [ROADMAP_14_DAYS.md](ROADMAP_14_DAYS.md)。

## 快速查看

- [两部分报名摘要](EXECUTIVE_SUMMARY.md)
- [安克业务价值](BUSINESS_VALUE.md)
- [14 天实施路线图](ROADMAP_14_DAYS.md)
- [完整开题报告（附件）](docs/GROVE-AI_Research_Proposal.md)
- [Compass 10K 示范概念](docs/COMPASS_10K_CONCEPT.md)
- [Soundcore 第二品类微型适配](docs/SOUNDCORE_MICRO_ADAPTER.md)
- [GROVE-AI Skill](grove-ai-product-definition/SKILL.md)

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

