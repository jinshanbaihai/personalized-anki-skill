# 审查、交付与原生操作

## 一、内容审查（先于版式）

1. **冷读每张卡**（关掉语音）：读完能否说出主干与理由？哪一句会让基础不稳的读者停下来？定义里的每个词是否讲过作用？推导是否有跳步？因果链的每个箭头是否成立？发现问题就补解释或拆卡。
2. **关键词复现测试**：只看卡组，写出 MS 要求的定义关键词、推导得分步骤、结论句、essay 的 AO1/AO2/AO3 骨架。写不出的就是缺口。
3. **双向核对**：按 [coverage-ledger.md](coverage-ledger.md) 回扫考纲原文、板书点与真题需求清单（每条 demand 都能指出准备它的卡）；生成器的 `coverage` 报告只能证明连线没断，考点清单本身是否漏项要人读原文判断。
4. **独立评审**：内容成形后，交给没有参与制作的审阅者（子 agent），给它考纲条目、MS 摘录、板书和卡片预览，要求：找遗漏、误读、超纲、讲不透的地方，并对每条给出可执行的改法。采纳后让审阅者复查改动部分与整组连接；旧版通过不代表新版通过。没有子 agent 时，作者分开做冷读、反例检查和范围回扫，并如实说明。
5. **数值核算**：所有计算、概率、系数、图中数值用工具复算一遍。

## 二、版式与渲染

```bash
python scripts/build_cards.py deck.json out/ --preview
node scripts/render_check.mjs out/ --phone --dark
```

`render_check` 在真实 Chromium 中打开每页，桌面 1280×800、手机 390×844、亮／暗两种模式截图到 `out/check/`，并用 `ccptAudit()` 检查：正文不小于 15px、界面小字不小于 12px、数学上下标不小于 9.5px、没有横向滚动、没有被截断的块、导图节点不重叠、每页恰好一个播放器、无脚本错误。程序通过后仍要**看截图**：层级是否一眼可辨，图是否清楚，长卡在正常字号下是否读起来顺。读着累的卡要重新分卡，不靠缩小字号。

## 三、语音

```bash
python scripts/speech_backend.py --check --voice xiaoxiao     # 服务与声音是否可用
python scripts/speech_backend.py --probe /tmp/probe.mp3       # 实际合成一段
python scripts/build_cards.py deck.json out/                  # 合成全部语音并打包
```

检查：音频可解码；成品时长与“修剪后原速 ÷ 速度”一致（生成器自动校验）；段间没有超过设计停顿的空白；听一遍 `term-sampler.mp3` 确认 English 术语与缩写读音，读错就改 `speech_lexicon`；公式读法表达含义；讲图时先说看哪里；Space 暂停续播、结束重播、切卡停止；点速度按钮可在 2×／1.5× 之间切换且音高不变；1.5× 卡都有理由。`node scripts/render_check.mjs out/ --play` 在 Chromium 中实际按 Space 播放、检查高亮与切速。规则见 [narration.md](narration.md)。语音服务不可达时用 `--audio-pending` 先交付图文包（页面明示“语音待补”，播放器禁用），告诉用户在能访问服务的机器上去掉参数重跑并导入即可原位补上语音。不静默换声音。

## 四、打包与导入验证

```bash
python scripts/validate_package.py out/<牌组>.apkg --output out/validate.json [--allow-text-only-test]
```

在临时空 collection 中导入，检查每张卡单页、一个播放器、媒体可解码、无缺失媒体；再做一次真实评分后重复导入，确认卡片身份、排程与 revlog 不变。这一步不等于桌面操作测试。

## 五、单面卡的桌面操作

用户只看一页完整内容，没有题目面、翻面、输入答案或选择题。**Space** 播放／暂停／继续／重播语音，不评分；**Enter** 记 Good 并进入下一张；**1** 记 Again，下一个 Anki 学习日再看。

实现：question 与 answer 模板显示同一页；每次构建都在输出目录写出 `ccpt_single_face.ankiaddon`（也可 `python scripts/package_addon.py 目录/`），用户双击即安装（重启 Anki）。插件只对模板含 `data-ccpt-single` 的卡生效：首次显示后自动切到可评分状态，接管 Space／Enter／1，长按不连发，其他卡与编辑器不受影响，不改调度参数。插件通过公开钩子 `gui_hooks.state_shortcuts_will_change` 改写 reviewer 的 Space／Enter／1（旧版 Anki 回退到 `Reviewer._shortcutKeys`）；`_answerCard`、`_showAnswer` 不存在时只提示“需要更新插件”，不让 Anki 报错。已核对 Anki 26.09.3（aqt 26.9.3）源码中这些接口与钩子均存在；26.x 的作答键来自可配置的 `get_answer_key`，插件在 `1` 被改键时会补回。Anki 升级后先在测试 profile 复核。

**“1 = 下一学习日再看”依赖牌组的学习步长**：Anki 默认步长（1m、10m）下，按 1 的卡和 Enter 的新卡会在当天几分钟后再出现。插件在工具菜单提供“CCPT：当前牌组使用阅读预设”，确认后克隆当前预设，只把新卡与遗忘卡的步长改成 1 天、leech 只加标签，其余设置（每日数量、FSRS、retention）不变；当牌组步长短于 1 天时，第一次按 1 会弹出一句提示。交付时告诉用户这一步（一次性）。AnkiMobile／AnkiDroid 不加载桌面插件：卡片仍是同一张完整页面，点页面上的播放键听讲解（2×／1.5× 键同样可用），先点 Show Answer 再点 Good／Again（AnkiDroid 可在设置里把手势或音量键映射到这两个按钮）；“Again = 下一学习日”同样取决于牌组预设，预设在桌面改一次即同步到手机。

实测项：打开卡即见完整内容；Space 只控制语音；Enter 一次 Good；1 一次 Again 且 due = 下一学习日；切卡停止旧音频。评分测试在测试 profile 或测试后立即撤销，并核对原卡状态与 revlog，不污染学习历史。

## 六、原位更新与新旧卡

- GUID = `namespace` + 卡 `id`。更新已有卡时两者都不能改；新卡用新的 `id`。拆分旧卡时，旧卡承接最接近的一个目标，拆出的部分用新 `id`。
- 先读取实际集合中的 note GUID、StableID、note／card ID、notetype 与牌组，再决定映射；不凭旧作者文件猜。
- 旧版本 skill 生成的卡（v5 导图卡，字段 FrontHTML／BackHTML）要改用 ccpt-6 时：先导入一个 ccpt-6 包让新 notetype 存在，在 Anki 浏览器里选中旧卡 → Change Note Type → ccpt-6（BackHTML → Page，StableID → StableID，Source → Source），复习历史随卡保留；再用同一 GUID 的 deck.json 生成新包导入覆盖内容。整个流程先在集合备份或测试 profile 中走一遍。
- 共享 notetype 的模板改动影响该类型全部卡，改前确认不会破坏未改的旧卡。
- 只操作用户授权的牌组；调度设置按 [review-planning.md](review-planning.md)，只在用户要求时改。

## 七、交付说明

告诉用户：

- 锁定的考试与证据；有假设时（考季、另一候选考试）放在第一行，并说明另一种情况会改变哪些卡。
- 实际读过的考纲、MS、ER、范文与真题考季（以及取不到的）；真题需求清单的条数与饱和依据。
- 考点总数、卡数与覆盖状态；同节相邻、留给下一批的考点（`adjacent`）逐条列出，用户说一句即可续做。
- 板书中看不清（`legibility: low`）或更正的位置：看不清的请用户补发原始导出（例如 ClassIn 原图），补来后原位更新。
- 语音状态（已合成／待补，以及补语音的一条命令）。
- 首次使用：双击安装 `ccpt_single_face.ankiaddon`、重启 Anki、导入 `.apkg`，再用工具菜单把牌组设为阅读预设（一次性）；导入后先在真实客户端看一张导图卡和一张推导卡，确认字体、公式与图都正常。
- 工程检查、制作者判断和用户实际体验分开说，不把程序通过说成学会了。
