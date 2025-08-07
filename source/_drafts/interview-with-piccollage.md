---
title: 獨一無二的面試體驗：My Interview Experience with PicCollage
categories:
  - 工作紀錄
tags:
  - Fulltime
  - Interview
  - PicCollage
cover: /img/cover/piccollage.png
date: 2025-07-29 15:57:07
---

# 前言



## 面試過程
應徵職位：Machine Learning Engineer  
部門介紹：[Medium](https://piccollage-company.medium.com/%E6%B7%B1%E5%85%A5%E7%9E%AD%E8%A7%A3-piccollage-%E4%B8%80%E6%8E%A2-piccollage-mlad-%E5%9C%98%E9%9A%8A-1d3ceff7e35b)

時程：
- 5/2 朋友幫忙內推完成
- 5/7 朋友主管詢問畢業時間
- 5/20 收到一面邀請
- 5/27 ML Head + HR 線上一面
- 6/5 Engineer 線上二面
- 6/17 Engineer 線上三面
- 6/26 Engineer Director 線上四面
- 7/2 Onsite Interview 實體五面
- 7/8 Offer Get (Oral)
- 7/9 線上 Offer Call
- 7/10 主動約線上 Offer Call
- 7/24 Follow-up Offer Call
- 7/28 Offer Accepted

這間也跟玩美移動類似，是做圖片相關的 App，我之前丟過好幾次他們的實習，但都是沒下文或直接感謝信。之前就業博覽會前後剛好得知有認識的朋友在裡面工作，當天也跟他聊了一下，後來覺得有點懶所以沒丟。但過了一陣子之後又覺得很心動，原本想麻煩我朋友內推，結果他隔了好一陣子才看到我訊息，但總之最後推到已經是五月初了，時程上可以說是小晚，想說我沒啥損失就加減投投看。

### ML Head + HR 線上一面
原本等兩週了還是沒下文，正打算放棄並且總算填了玩美的替代役，結果一面邀請就來了！

#### Take-home Work
Explain attention to people with different background knowledge
<!-- How would you explain the idea of attention in transformers to:
- Someone with a knowledge of ML but no knowledge of transformers
- Someone with a strong math background but no knowledge of ML -->

#### 面試流程 (30 mins)：
- Follow-up on homework: 5-10 mins (Attention: shape of input / Q K V /output)
- Resume: 5-10 mins (Education / Master's Thesis)
- Behavioral Questions: 5-10 mins (Past Work Achievements / Difficulties / What do you want to build)
- Q & A

### Engineer 線上二面
這次的面試體驗數一數二的好，工程師人很好，會引導我寫題目，忘記的細節也可以向他提問；並且題目難度適中，順順的就可以在時間內解完。加上最後 Q & A 聽他描述工作內容、工作風氣等等，又讓我更想去了一點！

#### Take-home Work
Use numpy to speed up a simulation process
<!-- https://en.wikipedia.org/wiki/Logistic_map -->

#### 面試流程 (45 mins)
- Follow-up on homework: <5 mins 
- Coding (CV): 35 mins
- Q & A
<!-- - Find mask where R + G > B
- Rotation of 2d points
- Broadcasting: Pairwise l2 loss -->

### Engineer 線上三面
面完前面兩輪後，我被 HR 加入他們的 Slack Channel，第三階段的面試與討論都在裡面進行。原本想說是不是用來討論作法的，但問了 HR 他說「可以確認題目」，想了想還是不討論作法相關的問題。

#### Take-home Quiz
Train a small model that follows a given distribution (colored image, specific pattern)  
Can choose from various models like VAE, GAN, AR, Diffusion...  
<!-- Data: One 300 x 300 photo of a colored "Pi" notation, given in [x, y, r, g, b] -->
Focus:
- Problem Formulation, Solution Correctness, and their Explanation
- Code Organization
- Evaluation Method

#### 面試流程 (45 mins)
- Follow-up on quiz: Until finished (~30 mins)
- Q & A  

原本以為會有類似的 Follow-up，結果完全就是在討論這份作業而已，也因此他問得很細節，包含資料前處理、模型設計、參數選擇、可能的問題與解法、程式碼架構等等都有涵蓋到，也因此你要很清楚知道自己在幹嘛。雖然我對我的訓練結果還算滿意，但有點可惜的地方是我因為時間不足，加上可能稍微放錯重點，因此我選用了相較簡單的評估方式（i.e. 用眼睛看），因此也被工程師挑說這部分沒做蠻可惜的（週四給題目週二面試，加上我還邊上班邊搞論文，週末才開始做，確實是有點緊湊）。

最後問他下一關，他說下一關是 onsite session，會到公司跟他們討論題目 & pair programming，大概會要 4-5 hours，我想說天啊我以為下一關就是發 offer 了 QQ，雖然我成功挺進到第三關，但我越來越害怕下一關會被看得體無完膚......（說不定也沒有下一關）。

### Engineer Director 線上四面
等了一週多後，迎來的竟然不是 onsite session 也不是 thank you letter，而是一個 20 minutes 的 "Casual Chat with Engineer Director"。不太確定到底會問什麼，但反正是 Casual Chat，也只能直接上了吧。

#### 面試流程 (20 mins)
- Resume & Chat (~15 mins)
- Q & A  

面完之後的感想，就是確實是 Casual Chat，但我口說退步好多 QQ。這關我感覺不篩人，就是想了解一下人選而已。面試官人很好，英文也很順暢聽很清楚，主要就是問一些履歷上他好奇的問題，像是他問了我之前的面試體驗、論文內容、實習經歷、專案架構等等，基本上熟自己的履歷就可以答的不錯。此外，也有一些延伸問題，像是你的興趣、如何跟上最新 AI 發展等等，不會太難。最後我也問了他像是如何決定產品開發方向、目前遇到什麼問題等等，整體來說就是有收穫的聊天。


### Onsite Interview 實體五面
最終總算迎來大魔王 - Onsite Interview。這關要去他們辦公室，進行總共 5 小時半的面試，其中會有不同環節與不同面試官來跟你面試，也會有一些像是辦公室導覽的環節。這樣的面試模式算是非常少見，畢竟前面已經經歷了那麼多關，再加上把一堆環節塞在同一天，這過程中公司要耗費的人力可想而知。HR 說裡面的每位員工都經歷過這個環節，雖然我自己覺得到這關代表蠻有機會（這是最後一關），但我也有看到幾個面完這關後還是收到感謝信的例子。總之，懷抱著忐忑不安的心情，我來到了他們位於國館的辦公室。

#### 面試流程 (~5.5 hrs)
- 20 mins - Office Tour & Reminder：這部分主要以參觀辦公室環境以及介紹今天面試流程與注意事項為主，參加者是 HR
- 12 mins - Fast QA：這部分會有 10 個以上的員工參加，主要就是針對你的履歷問相關問題，藉由把大家聚在一起一次了解你
- 40 mins - Casual Lunch Chat：PicCollage 會提供午餐餐點，這邊就是跟他們團隊成員一起用餐聊天，氣氛算是輕鬆
- 20 mins - (Break)
- 40 mins - ML Problem Solving：ML 相關的問題，以數學為主，參加者是 ML Team Lead
- 50 mins - Pair Programming：非常簡單的 Coding 題，有 OOP 概念會加分，參加者是 ML Engineer
- 10 mins - (Break)
- 40 mins - Problem Solving：預測問題的解法討論，會有多個變體與 Follow-up，參加者是 Engineer Lead & CEO
- 10 mins - (Break)
- 45 mins - Product Ideas Discussion：針對產品新功能的發想、討論、規劃、實作等等，參加者是 Product Team (PM/PD)
- 5 mins - (Break)
- 30 mins - Closing Chat：簡單聊一下對面試整體的體驗與想法，參加者是 Engineer Head & Maybe COO/CFO

結束的時候只覺得天哪好累，還有我終於走完所有的面試流程了，好不容易（他應該是我面試生涯中面過最累人的一間公司）！整體的面試體驗是很不錯的，PicCollage 的員工人都很好，面試題目設計都很扎實有趣，也可以透過面試的過程來模擬體驗公司環境與風氣，還有以後工作的感覺。

整體的面試體驗我覺得我表現還可，沒有很好也沒有太失常，但有些應該要表現出來的地方沒有表現好，像是突然忘記某個東西的計算方法（結束後馬上想起來...）還有 Coding 時前面卡住太久（不過最後有完成，並且還有多時間）等等。

但我覺得值得開心的事情是他們似乎都對我的論文很有興趣，除了在吃飯時間有聊到之外，在面試時也很多人都有追問，可能我的碩論確實跟他們工作很有相關？我覺得這件事情是好的，第一是他們真的有想要深入了解我（還有人看過我的網站，受寵若驚 XD），還有就是如果碩論跟他們在做的事情相關，那應該更有理由錄取我了(？)。

附帶一提，PicCollage 的公司環境很不錯，有興趣的可以參考[這個影片](https://youtu.be/QpZibLTpFjI?si=L4pxDgQ7p9JlV_a7)。

### Offer Call
最後 Offer Get! 太開心了！

# 結語