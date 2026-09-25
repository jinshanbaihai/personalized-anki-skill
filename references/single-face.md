# 单面阅读与桌面快捷键

用户只看一页完整讲解。没有题目面、翻面、遮盖与等待读完的步骤。Space 播放／暂停／继续／重播；Enter 提交 Good 并继续；1 提交 Again，下一 Anki 学习日再看。

## 为什么需要桌面适配

Anki 的 question／answer 是内部状态；仅把答案显示到 question HTML，不会让原生 Enter 直接评分。仅在 JavaScript 拦截 Space，也不保证抢先于 Qt 的快捷键。当前实现让 question 与 answer 模板使用同一个完整 BackHTML，并由 `scripts/single_face_addon.py` 在本卡首次呈现后切到可评分状态，显示内容保持一致。只生成一个 Anki card template，不生成反向卡。

桌面适配按模板中的 `data-ccpt-single` 标记限定范围。它替换本类卡 Space／Enter／1 的动作，其他卡仍调用原处理；不改 FSRS 权重、不直接修改 due，也不自动给任何卡评分。页面控制在 `assets/single-face.js`。只有用户按 Enter 或 1 才评分；Space 不记分。Anki 内部 reviewer 方法与版本有关，部署前核对当前源码。参考 [Anki reviewer](https://github.com/ankitects/anki/blob/main/qt/aqt/reviewer.py)。

将适配脚本安装为 Anki 数据目录 `addons21/ccpt_single_face/__init__.py`，配 meta.json 启用，并重启 Anki。只在用户已要求配置或交付可操作单面卡时安装。网页预览可验证完整内容与 Space 音频，但不能证明桌面评分有效。AnkiWeb／移动端需另行实现并验证，不宣称支持桌面插件。

## 迁移和调度

已有本技能卡片优先复用 BackHTML 完整讲解，只更新模板与键盘脚本，保留 note id、card id、字段、牌组和复习历史；若必要条件仅在旧 FrontHTML 中，要把必要场景补入完整阅读面，避免无脑丢弃。不要把这个变更当作重写全部知识内容的许可。

目标牌组采用单一 1d learning 和 1d relearning，leech 只标记。1 是“明天要再看”，不要求理由必须是完全遗忘，也不是重要旗标；这属于用户反馈映射，仍通过 Again 正常记入历史。随后 Good 回归 FSRS 正常调度。已有 retention 设置与历史按 review-planning.md 保留。检查父牌组、当日覆盖和 review cap，保证次日到期卡不会因限额隐藏；不批量重排无关卡。

## 验证

在实际 Anki 打开目标卡即看到完整内容与评分按钮；Space 启动、暂停、继续音频，不翻页、不记分；Enter 一次提交 Good；1 一次提交 Again 且 due 是 sched.today + 1，当日不重复。确认切卡停止旧音频、长按不连刷、编辑器和非目标卡不受影响。评分测试用隔离集合或测试后立即 Undo 并核对原卡状态和 revlog，不污染用户学习历史。实际听讲需检查当前页音频覆盖所有学习内容。
