# 当前原生交付

默认入口为 `build_logic_deck.py`。先按 `acceptance.md` 做教学与实际渲染检查，再用 `validate_package.py` 隔离导入，最后真实 Anki 导入和操作验证。当前question/answer均显示同一完整内容，不能用“正面不泄露答案”的旧标准检查。快捷键见 `single-face.md`。维护历史格式才使用带 `--legacy-maintenance` 的旧脚本，旧选择题和双面验收不适用于当前任务。

旧 `native_once.py` 已停用，不会导入、操作界面或评分。它的双面探测和只看 reps 的历史检查不足以验证当前卡；勿重新启用它作为单面交付捷径。
