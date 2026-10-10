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
- **29 张旧卡板书没有覆盖**，原样保留在 Anki 里（其中 T03 的画法与评分方案写法不同，见文末）。

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

## 内容以谁为准

考纲与评分方案（及其对应的官方教材）最高，板书其次，制作者自己的判断与第三方笔记最低。卡面、语音、批注都按上一级的说法讲，不“更正”上一级。旧卡组研究记录《板书与考试证据.md》里对板书和评分方案的“更正”（MS 的 decrease demand、MPC+subsidy、“实际产量”、“先免费提供”、“不是私人的”等）属于第三方判断，这一版全部没有采用：BD-T01 按评分方案原句讲 demand 下降；其余几处按板书原句讲。

## 板书旁的批注（6 处）

批注只在板书**模糊**或**未竟**（没讲完考纲、评分方案要的内容）时出现，材料取自第一级官方材料，必要时连上板书别处。产生过程：读这一块板书 → 对上评分方案、考官报告、考纲 → 看答题者要写出什么 → 补全模糊或未竟的地方。下面用到的官方原文都在 2026-10-10 下载核对过（考纲与样题评分方案的官网返回 403，分别用技能自带的考纲记录和板书上贴入的样题评分方案原样截图）。

| 卡 | 板书这里 | 类型 | 批注补了什么 | 取材 |
|---|---|---|---|---|
| BD-ESSAY | air travel 原题，只说“借助图” | 未竟 | 本题是消费的负外部性：画消费负外部性的图；关键的 market failure 是 overproduction 造成的 allocative inefficiency | F/M 2023 考官报告 p9（“Air travel relates to consumption not production”） |
| BD-T01 | 评分方案：tax 提高成本，demand 下降 | 未竟 | demand 下降即曲线左移 → 均衡航班数减少到 allocatively efficient 的数量；同页要求图上比较两者、标出 welfare loss | 9708/42 F/M 2023 评分方案 pp9–10 |
| BD-B07 | 红色草图向上那条线的手写标签 | 模糊 | 写的是 MPC（供给线）；后面 subsidy 图把同一条线标作 MPC = MSC | 板书 BP18；考纲 7.4.4；F/M 2023 评分方案 p9（clearly labelled, accurate diagram） |
| BD-S01 | 图中标 MPC+subsidy 的线 | 模糊 | 即有补贴之后的供给线，在 MPC = MSC 下方；补贴降低生产成本、MPC 下降；产量从 Qactual 增加到 Qoptimal | 样题评分方案 Q2（A subsidy will lower the cost of production…）；板书 |
| BD-I03 | merit good 对消费者有好处但被低估 | 未竟 | providing information → demand、consumption 增加 → output 上升，allocative efficiency 可能实现 | 样题评分方案 Q2（advertising to increase demand）；M/J 2023 考官报告 p22 |
| BD-POS-ESSAY | 评分方案：equilibrium output 上升，达到 allocative efficiency | 未竟 | 即 output 增加到 MSB = MSC 处的 Qoptimal；板书 MSB = MSC 的点才实现 allocative efficiency | 样题评分方案 Q2；M/J 2023 考官报告 p22；板书 BP07 |

## 保留旧卡中与评分方案写法不同的地方

保留的旧卡 T03（Negative consumption：tax 怎样把 Q 拉回 Q*）按“供给上移到 MPC + t”的画法讲，与 9708/42 F/M 2023 评分方案“tax … will decrease demand”的写法不同。它不在这次的板书卡里，旧卡组的制作源要另行按评分方案的写法改造。
