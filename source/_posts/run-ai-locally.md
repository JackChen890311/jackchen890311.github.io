---
title: 在 Macbook 上跑 AI 模型 - LM Studio & Comfy UI
categories:
  - 學習筆記
tags:
  - AI
cover: /img/cover/macbook.jpg
date: 2026-08-20 15:57:07
---

# 前言
隨著近年來 AI 模型的快速發展，以及各家開源廠商朝向「強力小模型」的趨勢，AI 應用已經不再是 Server 的專利，只要善加利用你我手中的 Macbook，便能在本地端運行具有一定水準的 AI 模型。

這篇文章會非常簡單的介紹兩個最主流的本地 AI 工具：LM Studio (LLM / VLM) 與 ComfyUI (Image / Video)。因為我最近主要在研究 LM Studio，這篇文章會花比較多篇幅在他上面。

## 為什麼要在本地跑 AI 模型?
在本地跑 AI 模型有幾個好處：
- 隱私與資料安全：程式碼、文件、對話內容不會離開你的電腦，適合處理敏感資料。
- 零 API 費用：模型下載後可無限次使用，不用擔心 token 計費。
- 離線可用：沒有網路也能跑，適合出差或網路不穩定的環境。
- 客製化彈性：可以自由切換不同開源模型、調整參數，甚至微調(fine-tune)。

不過，在本地跑的模型能力通常不如 GPT-5、Claude 等雲端旗艦模型，且需要一定的硬體資源與設定門檻，運算時也會消耗較大量的電力。建議大家還是可以在雲端跟本地做取捨，或者是依情況選用不同方式。

## Macbook 的優勢
Macbook（M 系列晶片）最大的優勢是統一記憶體架構 - CPU、GPU、Neural Engine 共用同一塊高頻寬記憶體。這代表著，沒有傳統獨立顯卡「VRAM 不夠就跑不動」的硬限制，記憶體多大，模型理論上就能跑多大。例如 48GB 統一記憶體的機型，扣掉系統開銷後，大約能跑到 30B 參數等級、4-bit 量化的模型。缺點是記憶體頻寬仍不如專業級 GPU（如 H100），推論速度（tokens/s）通常較慢，適合中小型模型的日常使用，而非大規模訓練或極致速度需求。

# LM Studio
Installation: https://lmstudio.ai/

LM Studio 是一個免費的桌面應用程式，專門用於在本地端運行 LLM / VLM。它基於 llama.cpp 開發，支援 GGUF 與 MLX 格式的模型，提供直覺的圖形介面讓你輕鬆搜尋、下載、切換不同模型，也能開啟 Local Server 暫存 API 供其他應用程式呼叫。最大賣點是幾乎零設定門檻，下載裝好就能用。

安裝完成後，介面左邊會有幾個按鈕，分別是Chat, Local Server, My Models 跟 Model Zoo。先點進 Model Zoo，選擇一個你想嘗試的模型下載（e.g. Qwen/Qwen3.8-27b），回到 Chat 介面先載入對應模型，就可以開始聊天了！是不是很簡單好上手呢？

## 如何挑選模型？
如果不知道從何下手的話，基本上去搜尋看看開源模型排行榜像是 [artificialanalysis.ai](https://artificialanalysis.ai/?model-filters=open-source)，就可以找到一些當下比較厲害的開源模型了，但也要注意模型大小。Provider 的話，可以優先選擇 Unsloth，或官方發布者的版本。

> Q: Unsloth 是什麼？
> A: Unsloth 是一個讓 LLM 微調和量化都更快、更省資源的開源專案。核心賣點是透過優化過的 Triton kernel 和記憶體管理，讓 LoRA/QLoRA 這類微調方法速度提升數倍、VRAM 用量大幅下降，讓消費級顯卡也能微調大模型。除了訓練，Unsloth 也會針對熱門開源模型（Llama、Qwen、DeepSeek 等）釋出自家校準過的 GGUF/MLX 量化版本，通常在低位元下的精度保留比一般社群版本更細緻，這也是為什麼常在 LM Studio 上看到他們的量化模型被推薦。

### 模型大小怎麼選？
根據你 Macbook 的統一記憶體大小，大致可以判斷多大的模型適合你：

|統一記憶體|建議模型規模(4-bit 量化)|
|---|---|
|16GB|~8B|
|32GB|~13B|
|48GB|~30B|
|>64GB|~60B|

實際可跑的上限還要扣除系統與其他 App 佔用的記憶體,建議預留至少 20 - 30% 緩衝。

### 量化標記怎麼看？
在 LM Studio 裡，模型的量化標記主要分兩大系統：

#### GGUF（llama.cpp，跨平台）
- 開頭數字（如 Q4、Q5、Q8）：代表每個權重平均用幾個 bit 儲存。數字越小 → 檔案越小、跑得越快，但精度損失越大。
- `_0` / `_1`：早期較簡單的量化方式，較少見於新模型。
- `_K`：k-quant 系列，針對不同層使用混合精度，能在省空間的同時盡量保住品質，是目前主流。
- `_S` / `_M` / `_L`（Small/Medium/Large）：同一 bit 數下的細分變體，越大保留越多精度、檔案也稍大。
- `Q4_K_M` 是品質與檔案大小的甜蜜點，最常被推薦的預設選擇

#### MLX（Apple Silicon 專用）
- 標記通常直接寫 `4bit`、`8bit` 這類簡單位元數
- 因為針對 unified memory 架構優化，量化方式跟 GGUF 不完全對應，不會有 `_K_M` 這類細分後綴

實際在選擇上，除了依照記憶體大小來挑選之外，也可以先抓 `Q4_K_M`（GGUF）或 `4bit`（MLX）作為起點測試。其實量化方法 LM Studio 裡面都會照你電腦規格去做推薦，照著他推薦的選也可以。


## 進階玩法：CLI & API + Claude Code
前面提到的 Local Server，概念上就是 LM Studio 會在你本地開一個 API，讓你的其他應用程式可以直接呼叫。像是你可以把它當成 Claude Code 的免費替代品（[Documentation](https://lmstudio.ai/docs/integrations/claude-code)），讓 Claude Code 直接呼叫你本地的模型作為大腦。在你的 shell 設定檔（e.g. `~/.zshrc`）後面加上：

```bash
export ANTHROPIC_BASE_URL=http://localhost:1234
export ANTHROPIC_AUTH_TOKEN=lmstudio
export CLAUDE_CODE_ATTRIBUTION_HEADER=0
```

另外，LM Studio 也支援 CLI（[Documentation](https://lmstudio.ai/docs/cli)），這樣就不用每次都打開 App 了。設定好之後，你可以用以下的方式啟動 Local 版本的 Claude Code：

```bash
lms server start
lms load {model_name} --context_length 200000
CLAUDE_CODE_MAX_CONTEXT_TOKENS=200000 claude --model {model_name}
```

200k 的 Context Length 是 Claude code 預設，模型的話我是用 `unsloth/qwen3-coder-30b-a3b-instruct`，因為他在 hugging face 有 12M 的下載次數，蠻厲害的。我用起來是覺得還不賴，但就是電腦資源會吃到很滿，並且用起來還是沒有原生 Claude Code 順，但作為一個免費本地替代品還堪用。雖然我最後為了愛惜電腦以及效能考量跳槽用 [OpenCode](https://opencode.ai/zht) 了，但過程還是蠻好玩的，跟大家分享一下。


# ComfyUI
Installation: https://comfy.org/

ComfyUI 是一個開源的節點式（node-based）圖像與影片生成工具，基於 Stable Diffusion 等模型構建。不同於一般的文字輸入 -> 圖片輸出介面，ComfyUI 用視覺化的流程圖（Workflow）串接各種功能節點，例如模型載入、提示詞編輯、圖片後處理等，帶來極高的彈性與可控性。適合想要精細控制生成過程、嘗試複雜 pipeline 的使用者。

安裝完成後，照著他的教學走，建立一個新的 Instance。左邊的選單分別是 Assets, Nodes, Models, Workflows, Apps 跟 Templates。如果想要快速體驗看看 ComfyUI 的能力，直接點 Templates 選一個熱門的，他會在你的中間建立預設的 Workflow（以多個 Nodes 組成的有向圖），你可以修改圖中 Node 的內容（像是 Text Prompt），然後點擊右上角的 Run，就可以等待結果出現了！

除了官方提供的 Model 與 Workflow 之外，也可以到 [Civit AI](https://civitai.com) 去逛逛。ComfyUI 相較於 LM Studio 來說比較複雜，我也還沒有研究透徹，等哪天有更多心得再回來分享 XD。

> Q: Civit AI 是什麼？
> A: Civit AI 是一個以圖像生成模型為主的模型分享社群平台，類似圖像生成領域的 Hugging Face，但更偏向 Stable Diffusion 生態系（包含 SD1.5、SDXL、Flux 等）。使用者可以在上面上傳、下載各種 checkpoint、LoRA、embedding、ControlNet 模型，也能瀏覽其他人用該模型生成的範例圖片，通常會附上使用的 prompt、參數設定（steps、CFG、sampler）方便重現效果。它的特色是模型分類細緻，包含寫實風格、動漫風格、特定角色、特定畫風等各種微調 LoRA，社群會針對特定主題（例如某個角色、某種美術風格）持續發布優化版本，並有評分、留言、範例圖庫等機制讓使用者判斷模型品質。因為平台內容較開放，包含大量 NSFW 內容，所以也常伴隨版權與內容審核方面的爭議。

# 結語
MacBook已經是相當實用的本地 AI 運算平台，LM Studio 讓你用近乎零門檻的方式跑本地 LLM / VLM，而 ComfyUI 則提供高度彈性的圖像 / 影片生成工作流程。兩者搭配，幾乎可以在完全離線、零 API 成本的情況下，建立一套個人專屬的本地 AI 工作站。
