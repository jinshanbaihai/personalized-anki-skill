> 当前新卡请从 `logic-build.md` 与 `build_logic_deck.py` 开始。本页是旧卡维护说明；旧版逐段播音按钮不符合当前单入口要求，不能直接生成后交付。

# 完整概念教学：格式与构建

当前默认使用 `scripts/build_teaching_deck.py` 与同目录 `teaching_renderer.py`。模板为 `assets/teaching-card.css/js`，完整内容例子在 `assets/teaching-example.json`。旧构建器仅用于兼容已有资料。

## 构建

使用 Python 3.12 或更新版本，安装 genanki、edge-tts，并确保 ffmpeg 与 ffprobe 可调用：

```text
python scripts/build_teaching_deck.py assets/teaching-example.json 输出目录
```

输出 apkg、媒体、语音清单、内容 JSON 与 HTML 制作预览。`--preview-only` 仅检查布局；`--templates` 指向包含 teaching-card.css/js 的自定义目录。预览不能代替实际 Anki 导入。

## 数据结构

顶层提供 title、source、voice、guid_namespace、model_id、deck_id、cards。已有牌组沿用原稳定身份。每张卡提供 id、label、title、context、question、answer、target、source、front、back，可设置 voice。front/back 是讲解状态列表。

每个状态提供：

- heading：当前段落讲什么，作为目录和正文标题。
- section：概念讲解、理解检查或难点应用。
- caption：完整可读讲解，空行划分可单独朗读的段落。
- narration：当前段落完整语音文本，避免重复串读数值。
- svg：当前解释对应的图像，需要 viewBox 与明确对象含义。
- voice：可选，覆盖当前状态的微软声音。

状态数量来自教学规格。一个状态有多个段落并不意味着内容超量；先检查这些段落是否共同解释当前目标。图像保持可见，文字可以滚动。

## 理解检查

检查状态提供 quiz：question、四项 choices、零起算 correct、对应四项 reasons、零起算 repair。repair 指向这道题所需的讲解状态。每个选项都有针对其判断依据的解释。

题目确认前不显示反馈，点击后立即标记，确认后解释。正文、选项、按钮与图形检查实际点击范围。理解检查可以直接进入，也可以顺序学完概念后进入。不会自动提交 Anki 自评。

## 图像与交互

SVG 使用安全的静态元素；图中标签用 data-say 提供含义朗读。交互写在可信的模板中，由学科关系驱动。每个变量的单位与作用说明出现在图旁。

当前 lab 字段支持 measurement 和 moment。前者保留平均位置与分散的独立变化，后者计算作用线、垂线与 moment。需要其他概念时扩展 renderer 与 JS，测试其物理或数学不变量，不把现有图形当成所有卡片的模板。

## 媒体与身份

音频制作时处理为 1.75 倍速，播放器不再次加速。data-audio 引用同时登记为隐藏 audio src，让 Anki 导入器能够识别媒体。检查实际导入后的每个自定义引用均有文件，不能仅核对 zip 内容。

笔记字段为 StableID、Label、Prompt、Answer、FrontHTML、BackHTML、Source、Target。沿用 GUID namespace 与 id 更新原卡。真实导入时核对 note/card 身份、已有进度、媒体、重复导入和可见交互。
