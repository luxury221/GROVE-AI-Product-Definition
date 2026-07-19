---
name: grove-ai-product-definition
description: 面向消费电子与安克多产品线执行证据驱动的 AI 产品定义决策，包括竞品与用户证据编码、JTBD 机会排序、生成与审查分离、工程和商业红队、人工决策 Gate、严格历史时间切分回测、概念收敛与品类适配。用于研究产品品类、比较竞品、分析真实用户反馈、定义或否决产品概念、验证产品机会、规划 MVP，或适配 10,000mAh 磁吸无线充电宝和 Soundcore 真无线耳机时。
---

# GROVE-AI 产品定义决策 Skill

## 定位

把分散的用户、市场、竞品、标准和工程证据，转化为可追溯、可验证、可进入人工决策 Gate 的产品机会。优先输出决策质量与企业价值，不把方法术语、模型数量或产品概念本身当作最终价值。

统一以下层级：

```text
GROVE-AI                     企业产品定义决策系统
└── 目标品类                 验证对象
    └── 产品概念             通过 Gate 后的示范结果
        └── 产品内部 AI 能力 需要单独证明的能力

协作平台                    证据、责任和 Gate 的治理载体
```

对安克案例，使用以下映射：GROVE-AI 为主方案；10,000mAh 磁吸无线充电宝为首个验证品类；Compass 10K 为示范概念；PowerPilot AI 为产品内部能力；飞书为计划中的协作载体。

## 强制纪律

### 证据纪律

- 为每个重要结论绑定 `evidence_id`。
- 区分 `FACT`、`INFERENCE` 与 `HYPOTHESIS`。
- 记录来源、发布日期、访问日期、地区、产品版本和置信度。
- 用官方或标准机构来源确认规格、安全、认证和法规。
- 用至少两类独立来源支持关键用户痛点；证据不足时标为弱证据。
- 不虚构销量、退货率、投诉率、用户比例、实验结果或商业收益。
- 不用单条评论、单个评测、合成用户或模型置信度代表市场事实。

### 决策纪律

- 在 Gate G 通过前禁止生成产品概念。
- 为机会同时保留支持证据、反证和未决冲突。
- 分离提案者、工程审查者、商业审查者、红队与审计者。
- 不用模型投票代替证据裁决。
- 只保留一个核心 JTBD 和不超过三个核心差异化。
- 把工程、安全、认证、成本和产品线冲突前置到概念收敛前。
- 由具名人工决策人批准或拒绝每个 Gate。

### 状态纪律

为所有交付、指标和主张标记状态：

- `Completed`：产物存在、可复现并通过对应 Gate；
- `In Progress`：正在执行，尚未通过 Gate；
- `Planned`：已定义验收条件，尚未执行；
- `Hypothesis`：需要真实数据或实验验证。

不要把目标样本量、预测指标、用户满意度、退货率、热实验结果或候选规格写成已完成结果。

### 合成用户纪律

只用合成用户发现边界场景、压力测试概念、生成访谈提纲或检查表达。不要用其估计市场比例、替代真实访谈、证明付费意愿或证明市场认可。

## 输入契约

开始任务时收集或保守补全以下字段，并写入 `run_manifest.yaml`：

| 字段 | 说明 |
|---|---|
| `category` | 产品品类 |
| `anchor_brand` | 核心品牌 |
| `target_market` | 地区、渠道和价格带 |
| `target_user_contexts` | 使用场景 |
| `comparison_scope` | 同品类边界与控制变量 |
| `historical_cutoff` | 预测阶段允许使用信息的截止日期 |
| `observation_window` | 解封后的观察区间 |
| `minimum_products` | 最少竞品数量 |
| `minimum_feedback_items` | 最少去重反馈数量 |
| `holdout` | 留出产品、产品族或品牌 |
| `decision_owner` | 最终人工决策人 |
| `constraints` | 时间、预算、数据权限、保密和工程边界 |

显式记录默认值与缺失项，不静默猜测。正式回测开始前冻结输入和验收阈值。

## 标准运行目录

为每次运行创建 `runs/<run_id>/`，至少包含：

```text
runs/<run_id>/
├── run_manifest.yaml
├── 01_scope/
│   ├── category_definition.md
│   └── control_variables.md
├── 02_evidence/
│   ├── evidence_ledger.csv
│   ├── source_register.csv
│   └── duplicate_clusters.csv
├── 03_market/
│   ├── product_benchmark.csv
│   ├── review_coding.csv
│   └── trend_summary.md
├── 04_jobs/
│   ├── jtbd_map.md
│   ├── pain_taxonomy.md
│   └── opportunity_scores.csv
├── 05_concepts/
│   ├── concept_candidates.md
│   ├── concept_selected.md
│   └── qfd_matrix.csv
├── 06_feasibility/
│   ├── engineering_review.md
│   ├── safety_compliance.md
│   ├── cost_business_review.md
│   └── risk_register.csv
├── 07_backtest/
│   ├── backtest_cases.csv
│   ├── predictions.csv
│   ├── observations.csv
│   ├── metrics.json
│   └── ablation_report.md
├── 08_validation/
│   ├── experiment_plan.md
│   └── acceptance_gates.md
└── 09_report/
    ├── executive_summary.md
    ├── methodology_report.md
    └── product_proposal.md
```

只通过结构化文件交换正式状态。原始证据只追加；修订使用新版本；红队和审计者不得覆盖提案原稿。

# GROVE 工作流

## G — Ground Evidence

### 1. 冻结边界

定义功能边界、价格带、市场、时间、容量/形态等控制变量。把相邻品类放入外部控制，不混入主样本。

### 2. 注册来源

按以下优先级组织来源：

1. 官方产品、支持、标准、认证和法规；
2. 独立实验室与可复核评测；
3. 零售平台验证购买反馈；
4. 社区、论坛与视频评论；
5. 二手汇总和模型生成内容。

社区内容用于发现问题，不用于估计市场比例。时间敏感信息在最终输出前刷新。

### 3. 建立 Evidence Ledger

记录 `evidence_id`、来源、日期、产品版本、市场、摘录摘要、主张类型、置信度、支持/反对对象和冲突状态。只保存必要短摘要，遵守版权和隐私限制。

### 4. 去重与编码反馈

按产品版本、语义、故障现象和上下文去重。保留场景、任务、痛点、严重度、可观察失败、替代行为与放弃行为。把“我想要某功能”与“我遇到某问题”分开。

### Gate G

仅在以下条件满足时进入机会分析：

- 同品类边界和控制变量明确；
- 关键结论可追溯；
- 正式数据与样例数据隔离；
- 来源冲突已裁决或显式保留；
- 回测预测区没有截止日后的信息；
- 决策人签署通过。

未通过时输出补证清单，停止概念生成。

## R — Reframe the Job

### 1. 从场景重构任务

按通勤、旅行、桌面、会议、运动等场景分组。使用格式：

```text
当……情境发生时，用户想要……，从而……；当前阻碍是……。
```

区分功能性、情绪性和社会性结果，不先绑定解决方案。

### 2. 形成痛点本体与机会

为痛点分配稳定代码，合并同义表达，保留上下文差异。使用模板中的维度计算机会排序，并把分数当作决策辅助而非真值。

每个候选机会必须包含：

- 支持 Evidence ID；
- 反证和来源冲突；
- 现有替代方案；
- 工程、安全和商业约束；
- 可能的产品线重叠；
- `FACT/INFERENCE/HYPOTHESIS` 与状态标签。

### Gate R

只选择一个核心 JTBD。选择不超过三个差异化方向。记录被否决机会及理由，优先否决证据不足、功能堆叠或工程冲突未解的方案。

## O — Orchestrate Agents

分配以下独立职责，可按任务规模合并非冲突角色：

| 角色 | 职责 | 不得做 |
|---|---|---|
| Evidence Researcher | 收集和登记证据 | 直接定义产品 |
| User Researcher | 编码反馈和场景 | 用合成用户替代真实数据 |
| Opportunity Analyst | 形成 JTBD 与机会 | 忽略反证 |
| Concept Proposer | 在 Gate 后提出概念 | 自我批准 |
| Engineering Expert | 审查热、电、结构和可靠性 | 修改原始证据 |
| Safety/Compliance Expert | 检查标准与失效模式 | 用经验代替地区规则 |
| Commercial Expert | 审查成本、价格带和产品线 | 把营销偏好写成事实 |
| Red Team | 寻找伪需求、冲突和过度承诺 | 覆盖提案原稿 |
| Evaluation Auditor | 审查时间切分、指标和泄漏 | 接触预测阶段禁用信息 |
| Decision Owner | 批准或拒绝 Gate | 把决定委托给模型投票 |

按 `references/collaboration_protocol.md` 交接，并使用 `templates/handoff.yaml`。无法裁决的冲突保留为阻塞项。

## V — Verify Adversarially

### 1. 预注册历史回测

冻结截止日期、来源白名单、预测字段、观察窗口、基线、留出样本、指标和通过标准。保存预测快照的时间戳与哈希。

### 2. 隔离预测与观察

预测阶段只读取截止日前资料。冻结后再解封后续产品、固件、评测和反馈。无法证明历史可得性的资料不得进入预测区。

### 3. 使用对照

至少设置：

- 简单频次或单模型总结基线；
- 一个外部品牌控制；
- 一个留出产品或产品族；
- 一个模块消融；
- 一个失败或被否决案例。

### 4. 计算并解释指标

运行 `scripts/backtest_metrics.py`，报告 Pain Recall@K、Trade-off Detection Rate 等预注册指标。使用 `scripts/validate_run.py` 检查运行目录。报告负面结果，不通过更换指标或删除案例追求漂亮数字。

### Gate V

要求泄漏率为 0、预测/观察可审计、失败案例保留、消融和基线齐全。若回测失败，说明错误来源和 Skill 修改是否可能造成历史过拟合。

## E — Engineer & Experiment

### 1. 收敛概念

只为通过 Gate 的机会创建 Concept Card。明确核心 JTBD、最多三个差异化、非目标、证据、反证、风险和产品线区隔。

### 2. 建立 QFD 与工程约束

把用户结果映射到可测工程指标，记录关系强度、目标、验证方法、风险和 Evidence ID。将规格标为 `Hypothesis`，直到样机或可靠来源验证。

### 3. 设计最小证伪实验

优先测试：

1. 安全和法规；
2. 核心物理可行性；
3. 核心 JTBD 是否成立；
4. AI 能力是否优于规则或非 AI 基线；
5. 可靠性、成本和量产风险。

为每项实验写明自变量、因变量、控制变量、样本、仪器、通过阈值、Kill Gate 和失败后的动作。

### Gate E

只有在工程、安全、商业审查和人工决策记录齐全后，才能把概念交付为 MVP 计划。不要把概念通过等同于产品效果已经成立。

## 品类适配

按任务只读取相关参考：

- 研究 10,000mAh 磁吸无线充电宝时，读取 `references/powerbank_adapter.md`；
- 研究 Soundcore 真无线耳机时，读取 `references/soundcore_adapter.md`；
- 设计历史回测时，读取 `references/methodology.md`；
- 编排角色与 Gate 时，读取 `references/collaboration_protocol.md`；
- 刷新官方、标准和法规入口时，读取 `references/source_seed.md`。

迁移到新消费电子品类时，创建一个适配器，至少定义：品类边界、控制变量、10 个关键规格字段、场景、痛点代码、工程/合规规则、一个候选机会、外部控制和留出策略。不要复制充电宝的字段和痛点。

## 最终交付

按任务输出必要文件，并至少包含：

1. 决策摘要：问题、核心 JTBD、机会、否决项和人工 Gate；
2. Evidence Ledger 与来源边界；
3. 竞品/产品基准和用户反馈编码；
4. 支持证据、反证、冲突和失败案例；
5. 工程、安全、商业和产品线约束；
6. 回测设计或结果，明确 `Planned` 与 `Completed`；
7. 概念、非目标、QFD 和 MVP 实验计划；
8. 可复用资产：本体、规则、模板和决策记录。

优先使用 `templates/` 与 `schemas/`，运行 `scripts/score_opportunities.py` 计算机会分数。任何脚本输出都需由人工 Gate 解释和批准。

## 完成前检查

- [ ] 主方案、验证品类、示范概念和产品内部 AI 能力层级清晰；
- [ ] 企业价值先于技术术语；
- [ ] 重要结论绑定 Evidence ID；
- [ ] FACT、INFERENCE、HYPOTHESIS 分离；
- [ ] Completed、In Progress、Planned、Hypothesis 状态清晰；
- [ ] Gate G 前未生成概念；
- [ ] 核心 JTBD 只有一个，差异化不超过三个；
- [ ] 有反证、失败或被否决案例；
- [ ] 提案、审查、红队和审计职责分离；
- [ ] 有具名人工决策人；
- [ ] 回测截止日期、外部控制、留出样本和消融明确；
- [ ] 泄漏率为 0 或明确标记回测失败；
- [ ] 目标指标没有被写成实际结果；
- [ ] AI 能力有非 AI 或规则基线；
- [ ] 输出包含风险、Kill Gate 与下一步行动。
