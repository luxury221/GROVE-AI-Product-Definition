# GROVE-AI Product Definition Skill

这是一个面向消费电子产品定义的 Agent Skill，内置“10,000mAh 磁吸无线充电宝”适配器，覆盖：

- 外部证据检索与证据账本；
- 用户反馈去重和主题编码；
- JTBD 与机会评分；
- 多智能体角色、交接与冲突裁决；
- 严格时间切分的历史桌面回测；
- 红队、消融实验与质量 Gate；
- 产品概念、QFD、工程可行性和 MVP 验证。

## 目录

```text
grove-ai-product-definition/
├── SKILL.md
├── README.md
├── references/
├── templates/
├── schemas/
├── scripts/
└── examples/
```

## Claude Code 安装

项目级：

```bash
mkdir -p .claude/skills
cp -r grove-ai-product-definition .claude/skills/
```

个人级：

```bash
mkdir -p ~/.claude/skills
cp -r grove-ai-product-definition ~/.claude/skills/
```

调用：

```text
/grove-ai-product-definition
```

也可直接提出与竞品研究、产品定义、用户洞察或桌面回测相关的任务，由智能体根据 description 自动加载。

## ChatGPT / Codex

在支持 Skills 上传的界面中上传整个 ZIP。该包以 `SKILL.md` 为入口，并使用相对路径引用支持文件。

## 推荐首次指令

```text
使用 GROVE-AI Skill，对 10,000mAh 磁吸无线充电宝进行一次严格时间切分的桌面回测。
核心品牌为 Anker，控制容量、磁吸形态和目标手机品类。
先建立证据账本和竞品矩阵，再生成 JTBD、机会排序、消融实验和产品概念。
所有结论区分 FACT、INFERENCE、HYPOTHESIS，不得使用截止日期后的信息。
```

## 运行脚本

机会评分：

```bash
python scripts/score_opportunities.py \
  templates/opportunity_scores.csv \
  /path/to/output/opportunity_scores_scored.csv
```

运行目录校验：

```bash
python scripts/validate_run.py /path/to/runs/<run_id>
```

回测指标：

```bash
python scripts/backtest_metrics.py \
  /path/to/predictions.csv \
  /path/to/observations.csv \
  /path/to/metrics.json
```

## 版本

- v1.0.0：GROVE-AI 主流程、充电宝适配器、回测指标、结构化模板与基础脚本。
