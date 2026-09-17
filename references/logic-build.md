# 可编辑语义卡生成器（一个可用起点）

运行 `python scripts/build_logic_deck.py input.json output_dir`。依赖沿用 requirements.txt，以及 ffmpeg/ffprobe。示例见 assets/logic-example.json。

输入 cards 可保存 question、context、answer、tree、figure_svg、source、namespace、deck、deck_id 等。tree 节点的 text 和 children 保存讲解关系。当前 kind 使用 concept 或 diagram；map_root 为根概念，recall_branches 可指定正面待回顾的分支。

`color_roles` 只是这一示例渲染器支持的可选强调映射，可以省略；不是制作必须填写的分类表。同色、多色或其他排版都可以改 renderer 实现。现有例子把完整导图适配在一页画布中，可按需放大细节。不在窄屏自动退回长页。需要中心分支或循环时可用 figure_svg 或扩展布局。

脚本不自动把教材切成树，也不保证输入内容教学合格。先组织概念与解释，再使用或修改渲染器。例子没有自足性或考纲正确性的自动保证，需要实际审核。

音频按内容缓存并离线打包；生成原速后 atempo=1.75，播放率为1。正面不内嵌答案。当前不生成选择题。共享模型包含旧模板兼容分支；正式迁移时依照目标牌库现状验证。旧卡 identity 用原 namespace、id、model_id。


## 整页朗读

当前渲染器每面只有标题旁的一个播音按钮。同一按钮播放、暂停、继续与结束重播。概念树按深度优先的视觉顺序读取；全部可见学习节点应覆盖。`diagram_narration` 是带图卡必须提供的讲图稿；需要不同的正面引导时使用 `front_diagram_narration`。讲图稿描述真实的图形，不读隐藏答案，也不机械报标签。实际 1.75× 已编码在音频，播放器保持 1×，避免双重加速。


## 键盘与复习节奏

J 操作本页的唯一播放器，不接管 Space、Enter 和数字评分键。翻面清理旧监听器与音频，输入框或组合输入不触发。用户节奏为 J → Space → J → Enter；Again 使用单一 1d learning/relearning step，下一学习日 Good 后恢复 FSRS。这是牌组配置，不是往每张卡植入修改评分或到期日的代码。
