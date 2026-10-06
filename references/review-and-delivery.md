# 审查、交付与原生操作

## 一、内容审查（先于版式）

1. **冷读每张卡**（关掉语音）：读完能否说出主干与理由？哪一句会让基础不稳的读者停下来？定义里的每个词是否讲过作用？推导是否有跳步？因果链的每个箭头是否成立？发现问题就补解释或拆卡。
2. **关键词复现测试**：只看卡组，写出 MS 要求的定义关键词、推导得分步骤、结论句、essay 的 AO1/AO2/AO3 骨架。写不出的就是缺口。
3. **双向核对**：按 [coverage-ledger.md](coverage-ledger.md) 回扫考纲原文与板书点；生成器的 `coverage` 报告只能证明连线没断，考点清单本身是否漏项要人读原文判断。
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

检查：音频可解码；实测加速比与卡片速度一致（生成器自动校验）；中文与 English 术语发音；公式读法；讲图时先说看哪里；Space 暂停续播、结束重播、切卡停止；点速度按钮可在 2×／1.5× 之间切换。语音服务不可达时用 `--audio-pending` 先交付图文包（页面明示“语音待补”，播放器禁用），告诉用户在能访问服务的机器上去掉参数重跑并导入即可原位补上语音。不静默换声音。

## 四、打包与导入验证

```bash
python scripts/validate_package.py out/<牌组>.apkg --output out/validate.json [--allow-text-only-test]
```

在临时空 collection 中导入，检查每张卡单页、一个播放器、媒体可解码、无缺失媒体；再做一次真实评分后重复导入，确认卡片身份、排程与 revlog 不变。这一步不等于桌面操作测试。

## 五、单面卡的桌面操作

用户只看一页完整内容，没有题目面、翻面、输入答案或选择题。**Space** 播放／暂停／继续／重播语音，不评分；**Enter** 记 Good 并进入下一张；**1** 记 Again，下一个 Anki 学习日再看。

实现：question 与 answer 模板显示同一页；`scripts/single_face_addon.py` 安装为 Anki 数据目录下 `addons21/ccpt_single_face/__init__.py`（配 `meta.json` 启用，重启 Anki），只对模板含 `data-ccpt-single` 的卡生效：首次显示后自动切到可评分状态，接管 Space／Enter／1，长按不连发，其他卡与编辑器不受影响，不改调度参数。已核对 Anki 26.09.3（aqt 26.9.3）源码：`Reviewer._shortcutKeys`、`_answerCard`、`_showAnswer`、`state`、`reviewer_did_show_question`、`webview_did_receive_js_message` 均存在；26.x 的作答键来自可配置的 `get_answer_key`，插件在 `1` 被改键时会补回。Anki 升级后先在测试 profile 复核。AnkiMobile／AnkiDroid 不加载桌面插件：页面内容与语音可用，评分走各端自己的按钮。

实测项：打开卡即见完整内容；Space 只控制语音；Enter 一次 Good；1 一次 Again 且 due = 下一学习日；切卡停止旧音频。评分测试在测试 profile 或测试后立即撤销，并核对原卡状态与 revlog，不污染学习历史。

## 六、原位更新与新旧卡

- GUID = `namespace` + 卡 `id`。更新已有卡时两者都不能改；新卡用新的 `id`。拆分旧卡时，旧卡承接最接近的一个目标，拆出的部分用新 `id`。
- 先读取实际集合中的 note GUID、StableID、note／card ID、notetype 与牌组，再决定映射；不凭旧作者文件猜。
- 旧版本 skill 生成的卡（v5 导图卡，字段 FrontHTML／BackHTML）要改用 ccpt-6 时：先导入一个 ccpt-6 包让新 notetype 存在，在 Anki 浏览器里选中旧卡 → Change Note Type → ccpt-6（BackHTML → Page，StableID → StableID，Source → Source），复习历史随卡保留；再用同一 GUID 的 deck.json 生成新包导入覆盖内容。整个流程先在集合备份或测试 profile 中走一遍。
- 共享 notetype 的模板改动影响该类型全部卡，改前确认不会破坏未改的旧卡。
- 只操作用户授权的牌组；调度设置按 [review-planning.md](review-planning.md)，只在用户要求时改。

## 七、交付说明

告诉用户：锁定的考试与证据；实际读过的考纲、MS、ER、范文（以及取不到的）；考点总数、卡数与覆盖状态；板书中模糊或更正的位置；语音状态（已合成／待补）；导入方法与首次需要安装的插件。工程检查、制作者判断和用户实际体验分开说，不把程序通过说成学会了。
