---
title: 2025 年科技業正職預聘/研替面試心得（TSMC, Google, NVIDIA, MediaTek, Perfect Corp., Appier, PicCollage, Synology）
categories:
  - 工作紀錄
tags:
  - Fulltime
  - Interview
cover: /img/cover/perfect.png
date: 2025-05-19 15:57:07
---

# 面試紀錄
- 投遞履歷：9 家公司
- 面試邀請：7 家公司
- Offer Get：2 家公司

最後決定去玩美移動當 Machine Learning Engineer，另一個拿到的 Offer 是 TSMC（興趣不大）。

## TSMC
應徵職位：沒分，統一丟  
備註：有研替  
時程：
- 8/30 EPO interview invitation
- 9/12 EPO interview
- 10/1 EPO Thank you
- 9/16? 收到 IT 副理電話聊天詢問面試意願
- 9/23? 沒收到後續，打電話回去問，他好像說他忘記，當天就收到面試邀請
- 10/15 收到 IT 另一個處約時間，想約同天但卡到
- 10/18 IT interview (AAPD)
- 10/25 IT interview (MLAD)
- 11/1 收到資歷查核
- 11/5 資歷查核送出，有問是否需要廠測，對方說去年有紀錄不用
- 11/20 收到 HR 致電說明 Offer 細節並確認意願
- 11/28 Offer Get (MLAD)

台積電的面試是各部門自己安排，但大部分的形式似乎都差不多，就是請你自我介紹，然後再針對經歷提問。所以建議準備個簡單的簡報，照著講就好，不難準備。

### EBO OPC - SWE for Advanced Optical Lithography Technology
這是我最早收到的面試，在聽完我自我介紹後，他好像也沒有太多問題，就開始介紹部門工作，大致上是開發光照相關的內部軟體之類的。但我印象特別深刻的是他一直問我可不可以接受加班，還跟我打預防針說進來每天大概都是八點以後下班，不停的跟我確認可不可以接受。雖然打預防針是不錯啦，但我真的不知道怎麼回答，畢竟我也不想說不接受（雖然最後也稍微表達出不想加班了），搞得有點尷尬。過了一陣子收到感謝信，我想也是好啦，我也不想進去賣肝。

### Online Coding Test (For IT)
- 3 Questions 90 mins, no limit on language
- 當初忘記紀錄，以下依我的印象大概寫一下
- 聽說配分是 50, 50, 75，實習要 100 正職要 120，不確定真實性僅供參考
- 我後兩題全對，第一題大概對一半（竟然敗在第一題嗎...）

#### 題目內容
- 第一題：經典的 1/0 背包問題，但對時間的要求蠻嚴格的，我寫到我覺得最佳了還是有一半沒過，回去複習...
- 第二題：處理登入跟登出系統的 log，計算時間差並做一些判斷之類的，我用 hash table 輕鬆解決，不太難
- 第三題：我忘記詳細內容了，但印象是用 Heap 的概念解的，也沒有很難。

### IT AAID AAPD - AI/ML Engineer (LLM)
IT 也是台積最主要的核心 AI 部門，底下還有分幾個不同的處。這個單位的話，主要是在做給台積內部使用的工具，像是他們其實有內部自己的 Chatbot 叫 T-genie，去年實習的時候有用過，就是這個單位開發的。所以這個單位主要的服務對象是內部的 general user，主要接觸的工具應該比較偏 LLM 相關。
<!-- mainly focus on application in internal user (LLM) -->

### IT AAID MLAD - AI/ML Engineer (CV)
這個單位跟上面應該算是平行的單位，主要做的事情是把 AI 應用在 FAB 相關的場域上（我去年的是 FAC，不太一樣）。這邊的 FAB 就跟晶圓製造比較直接相關了，像是瑕疵檢測等等，技術方面的話應該比較偏重 CV。但我印象中他們對於 Gen AI 的應用相對較少，頂多就是有一些 Synthetic Data Generation 之類的。
<!-- mainly focus on application in FAB (CV) -->

### 後續
後續應該是拿到 AAID MLAD 的 Offer，但我基本上只是拿來做保底的，因為[前年已經在 TSMC 實習過了](https://jackchen890311.github.io/2023/09/11/intern-at-TSMC/)，對這間公司覺得還好。

## Google
應徵職位：SWE New Grad, Silicon New Grad, Imaging and On-Device ML SWE (Silicon), Silicon Intern
時程：
- 10/1 請人內推，送出所有職位的申請
- 10/16 收到 Imaging and On-Device ML SWE 感謝信
- 10/21 收到 SWE 約面試
- 11/7 SWE 1st Round Coding Interview （原本敲定 10/31，後來臨時往後延）
- 11/15 主動寄信詢問後續，無聲卡
- 12/25 無聊丟一下 Silicon Intern
- 12/31 Silicon Intern 感謝信（聽學長說是畢業時間問題）
- 1/9 請學長內推 Silicon Intern
- 2/6 Silicon Intern 1st Round Tech Interview
- 2/19 Silicon Intern 2nd Round Tech Interview
- 2/25 Positive Feedback (But waiting for other interviewees)
- 3/21 Follow-up on Results but No Reply
- 4/15 Thank You Letter (Reason: Strong performance but found better fit candidate)

### SWE 1st Round
- 考官是中國人，但英文面試，所以有點痛苦
- 題目大概是 Multi-source distinct shortest path，只有一個 destination
- 走過的路徑只算一次，也就是說兩個 source 可以藉由 share path 來減少路徑
- Warm-up 就是給我一個 case 請我找出更好的走法
- 我答的蠻爛的，應該是涼了，英文 + 不熟悉的題目完全無法
- 但面試官還加時 20 mins 讓我把問題做完，最後有給出可行解，時間複雜度不算太糟

### Silicon Intern 1st Round Tech Interview
- English based
- 介紹自己的 ML 專案
- 介紹 GAN Diffusion
- GAN / Diffusion Training problems and solutions
- 介紹 Transformer and its pros and cons
- 有沒有能力自幹 Training code
- Training failed how to check
- Explain any DL optimization methods (Literally Any)
- Coding
	- Circular array calculate shortest distance between 2 indexes
	- Follow-up: shortest distance between given index and item

### Silicon Intern 2nd Round Tech Interview
- English based
- Activation Functions
  - Swish Analysis (Derivative, Choose of Constant, Characteristics, Compare with other Activation Functions)
  - Activation Functions in Transformer 
- Latent Diffusion Models
  - Conditioning, Inference
  - Extend to Video Generation: How to do that? Some related problems and how to solve it? 

### 後續
SWE 後來就無聲卡了，Silicon Intern 收到的回覆是表現很不錯，但請我等他們面完其他候選人。殊不知這一等就等了好久，過程中我主動 follow-up 也被無聲，後來到四月底才收到感謝信，說雖然我表現很好，但他們最後找了其他更適合的人。再更後來我有打聽到，最後好像是選隔壁實驗室，以前上過課的老師的學生，只能說長江後浪推前浪，前浪死在沙灘上...？


## NVIDIA
應徵職位：AI Engineer, DL Engineer  
備註：有研替（他們家研替叫 intern，沒有 RSU 跟不算年資的樣子）  
時程：
- 10/21 收到主管聯絡詢問 RDSS 意願
- 11/4 收到 AI Algorithm SWE (RDSS intern) Coding Test 邀請
- 11/25 收到一面邀請
- 12/5 線上一面
- 12/16 收到二面邀請
- 12/20 線上二面
- 12/26 寄信詢問後續（因為收到其他 Offer，想加快，但最後沒有理我）

### Online Coding Test
- 3 Coding + 21 Mutiple Choices, 90 minutes
- Coding 題蠻簡單的，感覺不著重考資結跟演算法
- 選擇題著重 AI / DL 相關觀念

#### Coding
- 第一題：色碼處理（字串/十六進位/整數轉換）
- 第二題：Scipy 基本操作（我對 Scipy 完全不熟，所以沒寫出來，到底誰做 AI 在用 scipy...）
- 第三題：座標點朝向彼此移動，判斷是否全部聚在同一點

#### Mutiple Choices
考的內容很多元，我覺得出的蠻好的，內容包含主要圍繞在 DL，常見的模型如 CNN, GAN, UNet, AutoEncoder 等等都有出現，也有考一些基本的 CV 與 NLP 概念，像是怎麼訓練、微調、特定任務的標籤要怎麼處理等等，也會詢問常見的 Library 像是 Transformers，需要具備紮實的 DL 基礎。

### 線上一面
流程：
- 同一天兩輪，一輪一人一小時
- 簡介工作內容，大約 5 分鐘
- 個人經歷介紹，大約 10 - 20 分鐘
- AI 相關技術問題，大約 0 - 10 分鐘 <!-- 有被問 GAN，還有 Model train 不起來的情境題 -->
- Coding 題與相關 Follow-up，大約 30 分鐘

先前有寄信問 HR 面試流程，但沒有得到回覆，只好隨意準備。  

Coding 題的部分沒有很難，但很考驗基礎功力，我遇到的題目如下：
- 實作 Convolution（可能會包含 Stride、Padding 等等設定） <!-- 最後還有加考 Dilated，但我來不及做完 -->
- 實作兩個知名 CV Backbone 裡面的 Block，包含 Layer 定義跟 Forward Process

#### 關於部門
我面的這個職缺聽他說是新成立的，主要負責打造內部用的 AI Toolkit（TAO），會把最新的 Paper 的 Code 整合進去，因此感覺是個介於 Research 與 Engineer 之間的存在，同時也有跟一些工廠合作，來推他們的這個 Toolkit，也會幫他們解決一些相關問題。我個人是覺得這東西感覺蠻好玩的，因為同時有 AI 跟 SWE，主要領域又是著重在 CV 上面，完全是很適合我，感覺我面的也還算不賴，希望還有機會。


### 線上二面
流程：
- 只有一輪一人一小時
- AI 相關技術問題，大約 30 分鐘 
- 個人經歷介紹與相關提問，大約 30 分鐘
- (Optional) Coding Test，我最後因為時間關係沒有遇到

前半部的 AI 相關討論跟第一次有點類似，但這次的更深入並更開放，如果對 AI 沒有很深刻的了解，我想是很難答的好的。像是他有問你覺得分類問題可以用 MSE Loss 嗎、L1 Loss 跟 L2 Loss 的好處壞處各是什麼、Bias Variance Tradeoff 的概念等等。雖然有些我大學上課有學過，但我當時還真的快忘光，因此我覺得我答的不太好 QQ，希望不要在這個階段告吹，畢竟前面技術關都通過了。後半部的個人經歷就一樣我介紹他問問題，這次的面試官問的蠻細節的，但也還好我都算有答出來，現在就是看前半的表現可不可以了。

### 後續
後來等一段時間後，我有寄信給 recruiter follow-up，但都被無聲卡，看來敗在第二面表現太爛了......QQ。

## Synology
應徵職位：Product Developer
時程：
- ? 投遞履歷

### 後續
很後來才發現投過，直接被無聲卡，QQ

## MediaTek
應徵職位：演算法開發_影像演算法、軟韌體開發_ AI & Computing Platform  
時程：
- 10/17 收到面談邀約
- 11/15 以前 完成線上測驗（適性、TOEIC、Coding）
- 11/15 第一次面試（演算法開發_影像演算法）
- 12/18 寄信問後續，對方回覆無後續
- 1/9 又收到另一個 Team 面試邀約
- 1/17 第一次面試（軟韌體開發_ AI & Computing Platform）

### Online Coding Test
- 2 Coding + 16 Mutiple Choices + 8 Blank filling, 90 minutes
- 語言限定 C / C++ (Coding 只有 C)
- 選擇與填空注重語法與 OOP 觀念，需要很熟悉 C / C++
- Coding 皆偏基礎（Palindrome, Swap with bit operation）

### 第一次面試（演算法開發_影像演算法）
有聽說 MTK 是多部門一起，但不知為啥當天只來一個部門的兩位主管（來面我的是 AIDE，就是 MTK 裡面主要負責 AI 的部門，達哥就是他們做的）。面試前有要求做簡報，所以前半部都在自我介紹，全部講完後主管開始提問，他們真的問蠻細的，每頁經歷有興趣的都會問，也會 follow 一些相關問題來看你的人格特質，還有你遇到問題會如何解決等等。但我覺得這部分相較好準備，就是把你的經歷都弄熟，展現出你的自信就好，相較之下 Google 的 Coding Interview 難多了。問完已經過一小時多，後面就換部門介紹與提問，整題感覺聊的很不錯，他們也有展現出一定的興趣，應該算蠻有機會的。

### 第一次面試（軟韌體開發_ AI & Computing Platform）
這個部門我上次也有收到邀請，但面試沒出現，後來拿到 Offer 了想說就加減隨意面。流程一樣自介 -> 提問 -> 部門介紹，這個部門好像主要是寫不同的 OS Driver，還有把 AI Model 放到他們特化的 Chips 上面，跟一些相關的 Evaluation 跟 Verification 等等。其實算是我相對不熟 & 沒興趣的職位，大部分都在碰蠻底層的東西，主要 Skill Set 也是 C/C++、OS 等等，加上他還說每年大概一個月需要加班，所以其實我沒啥興趣。但還是花了一個半小時講好講滿，他們還問了很多關於你對工作的選擇看法，可惜的是我應該沒有要選他們。

### 後續
後來都無聲卡，再更後來好像聽到 AIDE 被解散的風聲。

## 玩美移動
應徵職位：AI Engineer (Image processing)、Machine Learning Engineer  
備註：有研替  
時程：
- 11/18 收到 Mobile Development invitation，但我跑去投 AI / ML 的缺
- 11/19~11/21 收到面試詢問與邀約，有 Coding Test
- 11/28 IQ + 英文 + 主管面談（App AI）
- 12/12 主管面談（Gen AI）
- 12/13 收到 Gen AI 口頭 Offer & 約時間現場談薪水 + 參觀辦公室
- 12/25 現場談薪水 + 參觀辦公室
- 1/13 Offer Accepted

### Online Coding Test
限定語言：C / C++，有開放網路查詢語法
- 第一題（M）：String Reduction, given a reduction rule find minimum length
- 第二題（M）：Cipher (Rotation based) 
- 第三題（E）：String Changes, given a change rule (skip / duplicate) find changed string

<!-- 
String Reduction: ab, ba -> c / ac, ca -> b / bc, cb -> a
Caesar Cipher: Case Sensitive & General (Might have more than english character)
String Changes: N -> remove next / M -> duplicate previous
-->

### IQ + 英文 + 主管面談（App AI）
面試當天共兩小時，第一小時是 IQ + 英文測驗。IQ 的部分分為中文、數學、圖像理解，就跟一般的 IQ 測驗差不多，但時間蠻短的要自己注意速度。英文的部分就是標準的多益測驗，沒啥難度。HR 會看著你線上考，考完之後馬上看成績，確定沒問題後就進入面試環節（不知道太爛會不會直接結束面試 XD）。

主管面談的部分就一樣，由我講經歷他問問題，但有個比較特別的是他有針對我 Github 上整理的課程作業問細節，特別是 DLCV 的作業內容，我甚至一個一個作業開給他跟他解釋。這部分問蠻細的，包含這個 Task 在做什麼、你為什麼選這麼 Model、有遇到什麼狀況、Dataset 用啥、Performance 多好都有問，雖然我有些都忘記了但還是大致有回答出來。接著就是問一些基本的 DL 相關問題，像是你平常怎麼訓練 Model、參數怎麼選、如何避免 Overfitting 等等，同時也有確認我的一些相關技能，像是影像處理、計算機圖形等等。

最後部門介紹的部分，他們說他們部門主要做的是 App 端的 Model，也因此模型的大小與效率很重要，除了演算法的開發也會蠻多時間在考慮這個模型能否在手機端直接運算，或是能否用傳統的影像處理方式就做掉節省運算量等等。但也有 Gen AI 相關的應用，像是更換背景、去除物件，但比較是另一個 Team 做的事情。相較之下我其實對另一個 Team 會比較有興趣，所以也有跟面試官表達，也許之後還有機會可以面面看。

### 主管面談（Gen AI）
流程跟前面類似，但今天的主管似乎比較少提問，不知道是不是我講得太投入，他就聽著我講偶爾問一兩句這樣，沒有太深入的想了解我經歷的感覺。但後半的部門介紹他講了蠻多的，相較前面的部門，這個部門更著重在一些關於 Gen AI 相關的應用。從需求面出發的話，最近熱門的應用有虛擬試裝、圖片編輯（用自然語言）等等，而這些的相關技術大多圍繞在 Diffusion Models，因此也是主要用到的工具。令我意外的是，他們也有在做一些 LLM / VLM 相關的應用，像是 AI 櫃姐等等，還蠻酷的。整體來說這個 Team 做的東西感覺蠻好玩，也會用到很多最近熱門的技術，又跟我的研究大致有相關，只希望他對我還有興趣了。

### 現場談薪水 + 參觀辦公室
後來面完隔天就收到 HR 的電話，詢問我的意願並發給我口頭 Offer，同時想跟我約一天現場實體面談（但不是面試，應該就是談 Offer）。蠻驚喜的，因為還在想他面試時感覺沒有問太深入，結果就直接給我 Offer 了，後來就跟他敲定聖誕節去辦公室面談。

當天來到他們位於大坪林附近的辦公室，是在一般的辦公大樓裡，一共十幾層，大概 1/4 ~ 1/3 是屬於訊連科技與玩美移動的，兩者又差不多再佔各半。面談進行的還蠻順利的，應該是我未來的主管讓我對於工作提問，並且他也補充了很多他們部門正在做或過去的專案經驗等等。
他一開始就先問我有沒有在面其他家，然後再跟我分析說這些工作差異，並且有點像在說服我的感覺，確實聽完之後我又更想去了一點 XD。

主管還蠻健談的，我問了幾個問題就過了快一小時，最後問完後就是來到談薪水環節。來之前我有做了一點研究，也問了一下我學長有沒有什麼要注意的地方，跟他之前談的數字。一開始給的數字差不多跟我打聽的一致，但我用已經有的 Offer 跟他 Compete，試試看能不能談更高。
他看起來也沒有面露難色，並表示會幫我問問看，最後還跟我要了 Line，感覺應該是有機會！於是就獲得了人生第一次談薪水的經驗，還蠻有趣的但有點怕怕的就是了哈哈哈。（其實原本的薪水我覺得也可以接受啦，但如果我有這個市場價那當然越高越好 XD）

### 後續
後來主管聯繫我，跟我說他幫我談到的薪水，最後落在一開始的數字與我喊的數字之間（我原本以為會直接給到我的數字）。但我這邊因為還想等等看 NVIDIA，所以就請他在等我幾週，但 NVIDIA 那邊都沒有後續，所以最後決定先接受起來，之後再看狀況。

## Appier
應徵職位：Machine Learning Scientist & Engineer  
備註：有研替，原本在這實習，請主管幫忙問能否轉正，但是轉到不同 Team，一樣需要面試，並且是跟不同主管  
時程：
- 與現主管約 1-on-1 聊目前 Offer 狀況與轉正情形
- 2/5 收到 HR 聯絡說明並敲定面試時間
- 3/6 主管一面（技術面試）
- 3/20 Thank You Letter

### 主管一面（Bidding Team）
- 自我介紹與相關專案、Scientist Related Questions、Engineer Related Questions
- 每個 Session 各 20-30 分鐘，但最後總共面了 2 小時
- Scientist
  - Design Product Search Recommendation Model
  - Details: Feature / Model / Training / Online & Offline / Evaluation...
- Engineer
  - Pick one of your project and explain it from start to end
  - Two Dimensional Logs Processing & Transformation
  - Prefix Sum

### 後續
後來收到 Thank You Letter 了，不太確定原因，但過幾天原主管跟我跟我約了個 1-on-1 聊天，好像說聽到的 Feedback 是我在這邊的專案太簡單，他們覺得還好。Hmmm......確實是有點簡單，我當初做就有類似的想法，不過也有可能是我包裝不好，但我好像也無可奈何，畢竟就是主管給的專案，也沒有其他 junior 或 senior 一起做。後來想說算了，反正現在這個新 Team 做的內容我也還好，相比之下我可能比較會想選完美移動，不過 Appier 的薪水、地理位置、公司風氣真的都很香......


## PicCollage
應徵職位：Machine Learning Engineer  
時程：
- 5/2 朋友幫忙內推完成
- 5/7 朋友主管詢問畢業時間
- 5/20 收到一面邀請
- 5/27 主管 + HR 線上一面
- 6/5 Engineer 線上二面

這間也跟玩美移動類似，是做圖片相關的 App，我之前丟過好幾次他們的實習，但都是沒下文或直接感謝信。之前就業博覽會前後剛好得知有認識的朋友在裡面工作，當天也跟他聊了一下，後來覺得有點懶所以沒丟。但過了一陣子之後又覺得很心動，原本想麻煩我朋友內推，結果他隔了好一陣子才看到我訊息，但總之最後推到已經是五月初了，時程上可以說是小晚，想說我沒啥損失就加減投投看。

### 主管 + HR 線上一面
原本等兩週了還是沒下文，正打算放棄並且總算填了玩美的替代役，結果一面邀請就來了！

Take-home Homework
<!-- How would you explain the idea of attention in transformers to:
- Someone with a knowledge of ML but no knowledge of transformers
- Someone with a strong math background but no knowledge of ML -->

面試流程 (30 mins)：
- Follow-up on homework: 5-10 mins (Attention: shape of input / Q K V /output)
- Resume: 5-10 mins (Education / Master's Thesis)
- Behavioral Questions: 5-10 mins (Past Work Achievements / Difficulties / What do you want to build)
- Q & A

# 結語