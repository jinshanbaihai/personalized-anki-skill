> 当前只制作单面阅读卡，完整内容首次可见；Space 播音，Enter Good，1 次日再看。下文两面字段、J 和翻面描述仅是旧卡存储格式，不是当前交互要求。迁移见 `single-face.md`。

# 旧 teaching 格式的维护说明

新卡使用当前 SKILL.md 的概念导图／讲图工作流，可从 `logic-build.md` 与 `scripts/build_logic_deck.py` 起步。本页及 `build_teaching_deck.py`、`teaching_renderer.py` 只用于维护已有 teaching 格式，不是新任务的默认制作流程。consumer 与最早的 build_deck 也属于兼容实现。

## 旧数据和身份

旧输入提供 title、source、voice、guid_namespace、model_id、deck_id、cards。卡片包含 id、label、title、context、question、answer、target、source、front、back；front/back 是原版状态列表。状态中的 heading、section、caption、narration、svg、voice 要按原卡用途解释。保留身份时沿用 GUID namespace、id 与 model_id，不能为修播放器复制整副牌。

旧卡可能带 quiz（question、choices、correct、reasons、repair）、分段导航、图中 data-say、measurement／moment lab。这些字段描述存量内容，不表示新卡需要选择题、逐段翻页或每个标签独立播音。用户只要求修操作时，保留卡片正文；要迁移内容与版式时再按当前规范重组。

## 维护注意

旧构建命令是 `python scripts/build_teaching_deck.py input.json output_dir`，依赖见 scripts/requirements.txt，另需 ffmpeg／ffprobe。`--preview-only` 只检查版式，不生成可交付音频。旧输出不能因为构建成功就当作符合新规范；若它又生成分散播音入口，先按本面阅读顺序合并为一个播放器再交付。图中标签保留含义，朗读融入整面讲图，不逐标签放按钮。

笔记字段为 StableID、Label、Prompt、Answer、FrontHTML、BackHTML、Source、Target。自定义 data-audio 媒体引用还需登记为隐藏 audio src，使 Anki 识别并导入媒体。维护旧媒体时按其 manifest 核对既有倍率；新制音频默认云逸 1.5×，播放器不重复加速。维护后检查目标卡正反面、媒体、J 键、翻面清理、GUID 和原有复习历史；不要为验证旧选择题而制作新选择题。
