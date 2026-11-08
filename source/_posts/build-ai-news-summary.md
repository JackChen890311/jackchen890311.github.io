---
title: Daily AI News Summary：在 Vibe Coding 時代快速打造 Web Service 的一些想法
categories:
  - 學習筆記
tags:
  - AI
  - Vibe Coding
cover: /img/cover/macbook.jpg
date: 2026-11-08 15:57:07
---

# TL;DR
我用 AI 花了一個晚上做了簡單的 Daily AI News Summary。每天自動抓取、總結、更新、部署，不需人工介入。
先來[這邊](https://jackchen890311.github.io/AI-News/)看看我的結果吧！也可以從我個人網站的右上角點進去。原始碼在[這邊](https://github.com/JackChen890311/AI-News)，歡迎自己複製一份使用。

（註：本文的 AI 指的多是 Coding Agent 如 Claude Code, Codex, OpenCode 等等，為求方便我用 AI 代替）

# How?
這篇文原本想走一般的技術文章風格，介紹整個服務在細節上怎麼處理等等，但我後來想想直接問 AI 可能還講得比我好（老實說，我也沒有對所有的細節瞭若指掌）。所以，我決定來分享一下我在打造這個網站的時候，我「實際上」做了什麼，跟我的一些想法。對細節有興趣的話，拿我的 Repo 貼給 AI 吧，他會很有耐心的跟你解釋的。

## Let's start with why
想做這件事情，只是偶然在 LinkedIn 上看到有人分享類似的東西，對於每天都要追 AI 新聞的我來說，此類工具必定是很有幫助的。當然，現成品一定一把抓，我的信箱裡面也各種 AI News 電子報，所以需不需要就見仁見智了，不過那時候我並無多想，只想說如果做一個屬於自己的 AI News Summary 感覺不錯，除了可以自己調整內容外，也是個不錯的 Side Project。

## And then...
於是，我就開始做了。我把別人分享的 Repo 貼給 AI，跟他說我也想做一個類似的東西。我用的是免費的 OpenCode，過程中不外乎就是選擇技術框架、呈現方式、細節的取捨等等，我沒想到的東西 AI 也都會幫我規劃好，有需要我做決定的也會幫我分析利弊。基本上我就像個出張嘴的傢伙，想到什麼就叫 AI 幫我做出來，懶得決定或沒什麼差異的就直接說好。

分享一些透過對話後，慢慢補上的小細節：
- 新聞來源：補上/刪掉一些我想看/不想看的
- 去重：不同來源會有一樣的新聞，用一些基本的字串比對方式來去重
- 多種呈現方式：手動跑 Skills + md、本機/雲端排程、網站介面（用簡單的 HTML + 個人美感微調）
- 免費的 Gemini API 容易 Failed，所以加了一些 Retry 機制

## Finally, deploy!
所以，除了指揮 AI 做事，我實際上做了什麼？為了讓這個服務 Deploy & Update Daily，我：
- 研究了免費的 Gemini API 使用方法，申請一把 Key 貼進去 Repo
- 請 AI 幫我寫了 Github Actions 的排程，並且確保排程跑起來沒問題
- 開啟 Repo 裡 Github Pages 的 Deployment，再從我的 [Blog](https://jackchen890311.github.io/) 連過去

對，就這樣。老實說我花在研究 Deployment 的心力可能還比 Coding 本身多。

## HackerTube
做完整件事情之後，我突然想到上週看到的一篇新聞：Andrej Karpathy 分享了他在週六早上，[用兩個小時打造了 HackerTube](https://karpathy.bearblog.dev/hacker-tube/)。

為什麼會想到這件事情呢？第一，整個成品完整到不可思議，基本上就是一個 YouTube 的替代品（當然，論流量跟網站量級來說還是完全不可比，但基本功能已經很完整了）。第二，他的介入少到不可思議，他自己在網站上提到，他實際上做的事情只有以下：
```
...
In this case, the only "manual work" I did was: 
1) I had to create some kind of API key from Google Cloud UI to query YouTube for video metadata, 
2) I booted up a VPS box and 
3) I bought the domain name.
...
```

我想了想，基本上跟我在做這件事情的時候遇到的狀況差不多。申請 API Keys，準備 Deployment 需要的東西，其他的都交給 AI 自己完成。當然我沒有 Karpathy 那麼厲害，我還是來回跟 AI 修了幾次，但你懂我想表達的意思。

BTW，他用的 Prompt 如下，使用的是 Claude Code + Opus 5.5：
```
"Hi Claude good morning how are you I'm great thx 
build me a YouTube-style site but restricted to videos 
that have been repeatedly recommended on HN over the years pls. 
Don't make any mistakes."
```
隨意到很好笑 XD 但也説明了，現在的 AI 只要給他一個目標，他就能自己想辦法完成。

# My take on this: Coding might be solved, but engineering is not
近期的 AI 實在是發展的太快，也徹底改寫了我們寫程式的方式。從這次的經驗來看，Coding 這件事情本身已經不再是一件難題，但我覺得，Engineering is a lot more than coding。也許我們接下來該關注的，是 Engineering 中除了 Coding 以外的那些東西。以上個人淺見，隨意聽聽就好，歡迎討論交流。有興趣的可以看：[Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next](https://www.youtube.com/watch?v=SlGRN8jh2RI)。

