# 板书01 Externalities（CIE 9708）· 改造工作区

这个文件夹不属于技能本身：`scripts/package_skill.py` 只打包 `SKILL.md`、`README.md`、`LICENSE`、`references/`、`scripts/`、`assets/`，这里的文件不会进技能包。

| 文件 | 来源 | 核对 |
|---|---|---|
| `source/board.png` | 云盘 `AI 工作区/学习/学习细项目/经济/Anki/cie-alevel-a2-econ-from260917/板书01 Externalities/sources/board.png` | 1280×9866，SHA-256 `a17f64f8101a66f4d07264124bcae12cba48dc7bacc90e1842db76442bd697c9`，与《板书与考试证据.md》记录一致 |
| `source/cards.json` | 同一文件夹的 `cards.json`（旧版导图卡制作源，53 张，测试身份 `ccpt-externality-board01-test-20261003`） | 只读，保留原样 |
| `deck.json` | 由 `make_deck.py` 生成的板书卡组 | 25 张板书卡、55 个考点；`build_cards.py` 检查通过，无卡级提醒 |
| `make_deck.py` | 生成 `deck.json` 的脚本：裁切框、语音讲解、批注、考点台账都写在这里 | 改卡就改它，再运行一次 |

## 怎样出包

在仓库根目录：

```bash
python3 work/econ-board01-externalities/make_deck.py work/econ-board01-externalities/deck.json   # 改过 make_deck.py 才需要
python3 scripts/build_cards.py work/econ-board01-externalities/deck.json out/board01/          # 合成语音并打包（电脑要能访问 speech.platform.bing.com）
```

语音服务连不上时加 `--audio-pending`：先出图文包，语音以后补，按输出文件夹里的 `补语音.txt` 做，同一张卡原位更新。2026-10-10 在云端构建时语音服务被代理拦截，所以只验证了图文包：`validate_package.py` 结果为 25 张卡、25 个 note、语音待补，重复导入时卡的身份与复习记录保留。

## 板书优先的改造结果

旧卡组 53 张，按“板书上有的直接贴板书原图”改造：

- **24 张旧卡的内容在板书上**，换成 23 张板书卡（旧卡 S01、S02 合成 BD-S01）。
- **另加 2 张板书卡**：BD-ESSAY（air travel 题的三大板块）、BD-POS-ESSAY（正外部性题），旧卡组里没有对应卡。
- **29 张旧卡板书没有覆盖**，原样保留在 Anki 里，不需要动。

| 旧卡 | 换成 | 旧卡 | 换成 |
|---|---|---|---|
| B01 | BD-B01 | S01、S02 | BD-S01 |
| B03 | BD-B03 | S04 | BD-S04 |
| B07 | BD-B07 | S05 | BD-S05 |
| I02 | BD-I02 | S06 | BD-S06 |
| I03 | BD-I03 | S07 | BD-S07 |
| I04 | BD-I04 | R02 | BD-R02 |
| I05 | BD-I05 | R03 | BD-R03 |
| T01 | BD-T01 | D01 | BD-D01 |
| T04 | BD-T04 | D02 | BD-D02 |
| T05 | BD-T05 | D03 | BD-D03 |
| J02 | BD-J02 | P01 | BD-P01 |
| — | BD-ESSAY、BD-POS-ESSAY | P02 | BD-P02 |

保留的 29 张：B02、B02b、B10、B04、B05、B06、B08、B09、B11、C01、C02、C03、I01、T07、T02、T03、T06、S03、R01、R04、D01b、P03、E01、E02、E03、J01、J03、J04、J04b。

板书卡是新的 notetype（ccpt-6），旧卡是更早的导图格式，GUID 也不同，所以**不能原位更新**：导入板书卡后，在 Anki 里把上表左列的 24 张旧卡暂停（Suspend）或删除，避免同一知识点复习两遍。旧卡的复习历史不会转到板书卡上。

## 板书旁的批注（10 处）

卡面内容大多直接来自板书，板书本身有几处容易读错。这些地方在板书旁加了一张小导图批注，标题写明需要的原因，底部写它服务的考试要求；只讲到考试所需为止。问题点取自旧卡组研究记录《板书与考试证据.md》（2026-10-03），并对照板书原图逐处核对了原话。

| 卡 | 板书原话或位置 | 类型 | 批注讲什么 | 考试依据 |
|---|---|---|---|---|
| BD-ESSAY | air travel 原题 | 跳步 | 本题要画 negative consumption 图，不是 production 图 | 9708 F/M 2023 ER p9 |
| BD-ESSAY | 老师：每个政策写两个 limitations | 说得过满 | 这是课堂组织办法，不是评分规则；题目给了政策数量按题目写 | specimen rubric pp5–6；M/J 2023 Q2 |
| BD-T01 | MS：tax … decrease demand | 易混 | 税是供给上移到 MPC + t、需求量沿原 D 下降；让 D 左移的是信息政策 | F/M 2023 MS pp9–10；F/M 2024 MS（图不准确最高 L2） |
| BD-B07 | 红色草图向上那条线的标签 | 字迹不清 | 按模型应是 MPC = MSC；考试时四条线都写清标签 | specimen MS pp9–10；F/M 2024 MS |
| BD-S01 | 下移的供给线标成 MPC + subsidy | 笔误 | 应是 MPC − s；原来的 MSC 不变，补贴是转移 | specimen MS pp9–10；F/M 2024 MS |
| BD-S04 | 补贴后的产量就到不了“实际产量” | 笔误 | 应是“最优产量”；补少了生产不足，补多了超过 Q* | specimen MS pp9–10 AO3 |
| BD-I03 | merit good 对消费者也有好处但被低估 | 易混 | 信息补的是私人 benefit 的低估，补不了给别人的 external benefit | specimen MS pp9–10；M/J 2023 ER pp21–22 |
| BD-R02 | 政府需要先免费提供，才能要求人们增加消费 | 说得过满 | 免费不是唯一办法，需要的是可负担、可获得 | 9708 syllabus 8.1.1；specimen rubric |
| BD-POS-ESSAY | MS：补贴使产量增加，达到 allocative efficiency | 跳步 | 中间一步：Q 升到 MSB = MSC 的 Q*，welfare loss 消失 | M/J 2023 ER pp21–22 |
| BD-P02 | 没有产权……因为这块地不是私人的 | 易混 | 关键不在私有还是公有，而在有没有可执行的权利与损害责任 | 9708/33 O/N 2017 Q16 |

原来这些更正写在卡底的“更正”文字块里，现在移到了板书旁边；只有 BD-D02 的“学校、医院关闭是课堂举例，未核实”仍是一条短提醒，因为它不是读板书的问题。
