"""Write ccpt_single_face.ankiaddon (double-click to install in Anki desktop).

Usage: python scripts/package_addon.py [out_dir]     → <out_dir>/ccpt_single_face.ankiaddon

The package holds __init__.py (scripts/single_face_addon.py, bytes unchanged), manifest.json, and the
add-on config shown under Tools → Add-ons → Config: config.json (defaults) and config.md (its help text).
Anki keeps the user's saved config in meta.json, so reinstalling a newer package keeps their decisions.
"""
import argparse
import json
import zipfile
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / 'single_face_addon.py'
MANIFEST = {'package': 'ccpt_single_face', 'name': 'CCPT 单面阅读卡（Space 播音 · Enter 继续 · 1 隔天再看）',
            'conflicts': [], 'mod': 1790000000, 'min_point_version': 50}  # 2.1.50+: deck-config and shortcut APIs used
CONFIG = {'auto_reading_preset': True, 'decided': {}}  # must equal DEFAULT_CONFIG in single_face_addon.py
CONFIG_MD = """**auto_reading_preset**（默认 `true`）：第一次复习某个牌组里的 CCPT 单面卡时，如果这个牌组的学习步长或重学步长短于 1 天（Anki 默认是 1m 10m，按 1 的卡几分钟后就会回来），插件自动把它（以及共用同一预设的子牌组）换成“CCPT 阅读（原预设名）”预设：新卡与遗忘卡的学习步长都设为 1 天，leech 只加标签；每日数量、FSRS、retention 等其余设置沿用原预设。有自己预设的子牌组、不含 CCPT 卡的牌组和筛选牌组不改。改完后右下角提示一次，不弹对话框。

设为 `false`：插件不自动修改任何牌组，需要时用“工具 → CCPT：牌组使用阅读预设（1 = 隔天再看）”。

**撤销**：工具 → CCPT：撤销阅读预设。恢复插件改动前的预设，此后插件不再自动修改这些牌组（仍可从工具菜单手动启用）。

**decided**：插件记下的决定（按 Anki 用户和牌组 id；`applied` = 已启用并记录原预设，`declined` = 已撤销）。由插件维护，一般不用手改；删掉某一项，下次复习时插件会重新判断那个牌组。

手机端（AnkiMobile、AnkiDroid）不加载插件：预设在桌面改一次即随同步生效；只用手机的话，在牌组选项里把学习步长与重学步长都设为 `1d`。
"""


def write_addon(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / 'ccpt_single_face.ankiaddon'
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(SOURCE, '__init__.py')  # bytes unchanged (UTF-8 source with Chinese UI text)
        z.writestr('manifest.json', json.dumps(MANIFEST, ensure_ascii=False, indent=1))
        z.writestr('config.json', json.dumps(CONFIG, ensure_ascii=False, indent=1))
        z.writestr('config.md', CONFIG_MD)
    return target


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Write ccpt_single_face.ankiaddon (Anki desktop add-on for CCPT reading cards).')
    parser.add_argument('out_dir', nargs='?', default='.', help='folder to write the .ankiaddon into (default: current folder)')
    print(write_addon(parser.parse_args().out_dir))
