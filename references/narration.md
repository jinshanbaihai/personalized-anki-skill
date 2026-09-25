# 新制卡的语音默认值

默认声音为微软云希 `zh-CN-YunxiNeural`，最终音频 **1.5×**。术语 English、解释中文；整页一个播放器，Space 开始／暂停／继续／重播。

优先使用当前可用的免费 Edge read-aloud 服务。它与 Azure Speech 的声音目录不同，不能用 Azure 官方列表证明 Edge 可用。每批先检测目标voice并合成短样本，不能仅见列表或 HTTP 成功就称播放通过。

`scripts/speech_backend.py --check` 检查目录与配置；`--probe /本机临时目录/probe.mp3` 实际合成。报告区分网络失败、声音缺失、Azure缺配置和真实合成成功。免费路径失败时先诊断重试；已配置且获授权的 Azure Speech 可作为同一voice的备选，环境变量 `AZURE_SPEECH_KEY` 与 `AZURE_SPEECH_REGION`，凭据不进 skill、日志或仓库。不静默换声，也不擅自开通收费资源。

合成原速音频，执行 `atempo=1.5` 后离线随卡携带，页面 `playbackRate=1`，仅加速一次。缓存与manifest包含真实voice、完整正文、速度、provider及实际时长。接口失败不保留空文件冒充缓存；已有缓存不能解码就重建。

讲图脚本与可见卡面共用图名和对象标签，按 `reader-first-teaching.md` 先定位再解释。切换图或从非讲图分支返回时重新说清目标；留出自然停顿供读者移动视线，不连续念坐标和字母代替讲解。朗读应覆盖内容含义，不必逐字念重复标签；卡面本身也必须有足够指向，不能只在语音补上。

验收检查可解码、原速与成品时长比约1.5、中文与English术语发音、图像解说的阅读顺序、公式意义、一页一个播放器、Space暂停续播及切卡停止。声音能播放不能证明讲解容易理解；听感须另外检查。既有其他卡片不因默认值变化而自动全量改写，按本次授权范围更新。

接口依据：[微软 REST 文档](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/rest-text-to-speech)、[edge-tts 项目](https://github.com/rany2/edge-tts)。
