# 单面语义阅读卡生成器

运行 `python scripts/build_logic_deck.py input.json output_dir`。依赖见 requirements.txt，并需要 FFmpeg。示例为 assets/logic-example.json。生成器是可改的起点，不是固定排版规范。每张卡保留导图结构；若现有字段或布局不能把表格、数据比较或图示放进节点，应扩展节点与渲染方式，不能为了复用 tree 把数值表硬塞进句子，也不能让图表脱离导图成为独立页面。

每张卡生成一份完整页面、一份整页讲解，以及一个 Anki template。question、context、answer、tree、figure_svg、diagram_narration 共同组成当前阅读面；scene 的必要条件与结论首次可见，不生成回忆题面。`recall_branches`、`figure_on_front`、`front_diagram_narration` 属于旧双面输入，当前忽略；图像始终完整显示。kind 只接受 concept／diagram，不默认生成选择题。

tree / children 是存储层级的起点，并不表示所有关系都是并列分类；因果、比较、分流与合并应按含义渲染，必要时扩展数据结构。节点表达不受当前字段限制，不能因只有文字、figure_svg 等字段就放弃更有解释力的组合。深层节点继续连线。可选 color_roles 只属于示例强调实现，不是固定色表。按材料选择布局，保证充分解释和完整关系一页可读。科学图必须另作内容核对。

整页语音随最终页面的实际阅读路径组织：标题与必要场景后，从核心沿有意义的分支讲解，图、案例或表格出现的位置与其讲解对应，覆盖全部学习文字。不把“先读所有图、再读所有文字”写死；调整布局时同时调整朗读顺序。图像必须提供 diagram_narration，解释对象和关系，不机械念标签。微软语音原速合成后 atempo=1.75，播放率为 1，避免双重加速；离线随卡打包。

为保留已有 note identity，存储字段仍叫 FrontHTML／BackHTML，但两字段写入同一完整页面，qfmt／afmt 都使用 BackHTML，不要求用户翻面。namespace、id、model_id 与旧卡保持一致；model_name 沿用实际已有名称，避免重复牌组。输出预览为 `<id>-read.html`，rendered.json 只有 page 内容。

Space 唯一播放器；Enter Good；1 次日再看。实际 Anki 需要部署 `single_face_addon.py`，见 single-face.md；仅浏览器测试不能代替桌面键盘与调度检查。

批量制作先保存可编辑的知识结构、范围与考试用途依据，再选择或改写渲染实现。当前样例只演示字段，不规定卡片数量、分支数量、讲解字数或图文布局。不同学习目标可有不同节点组合；概览不替代必要教学，完整解释不能留给随机出现的另一张卡。脚本成功产出只是工程步骤，须继续按 SKILL.md 做逐卡理解与应用验收。
