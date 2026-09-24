# 新制卡的语音默认值

默认 voice 为微软云逸 `zh-CN-YunyiMultilingualNeural`，最终音频 1.5×；术语 English、解释中文，整页一个播放器，Space 控制开始／暂停／继续。用户明确指定的 voice 才覆盖默认。

微软官方 voice 列表列出云逸，但 Azure Speech 和免费 Edge read-aloud 服务的可用声音不相同。2026-09-24 实测当前 Edge 列表未提供 Yunyi；直接请求该 voice 返回 NoAudioReceived。不要据此把云逸改叫云希，也不要伪称音频验证通过。制卡前重新检查可用性；平台可能变化。[微软官方 voice 列表](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support)

`scripts/speech_backend.py` 优先用当前可用的免费 Edge voice；目标 voice 不在列表时，允许使用已经配置并获授权的 Azure Speech：环境变量 `AZURE_SPEECH_KEY` 与 `AZURE_SPEECH_REGION`。不把凭据写进 skill、仓库或日志；现有接口授权不等于允许擅自购买额度。没有目标声音的可用授权接口时，明确报告缺失条件，仍可完成文字、预览与规则修订，但不交付假音频或静默换声。

合成原速音频，随后执行 `atempo=1.5`，页面 `playbackRate=1`；只在一处加速。manifest 与缓存哈希包含 voice、正文、速度，避免旧 1.75× 或旧声音误命中缓存。检查实际可解码、音频长度与倍率、中文和英文术语发音、公式的意义表达，以及一页一个入口和切卡停止。速度偏好不等于研究证明的最佳理解速度。此次只改新制卡默认，既有卡音频需另有改卡授权。
