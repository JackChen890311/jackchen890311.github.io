---
title: Python 教學系列文 (2) - 寫程式的流程、電腦架構、二進位制、排版方式
categories:
  - Python 教學
tags:
  - Python
cover: /img/cover/python_clear.jpg
date: 2023-03-23 20:54:31
---


[HackMD 完整版請點我](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw?view)

### 寫程式的流程（Workflow）
 - Debug：在我們遇到各種 Error 時，需要去檢查程式哪裡寫錯
 - 有時候是語法錯、有時候是邏輯錯...
 - 整體的寫程式流程：
![](https://i.imgur.com/kDs6oep.png)

### 電腦架構
非常簡易版的架構圖如下：
 - Input：鍵盤、滑鼠、觸控螢幕、麥克風等等
 - Output：螢幕、喇叭、印表機等等
 - Storage：硬碟、光碟機等等
 - CPU（中央處理器）：負責電腦的大部分運算
 - Memory：電腦內暫存的記憶體空間

 > 補充 - GPU（顯示卡）：負責遊戲、3D繪圖、機器學習等等運算
 > 若對這個有興趣的話，可以去查「計算機結構」或修相關課程

![](https://i.imgur.com/pmeyrcm.png)

### 二進位制
 - 電腦使用二進位制來儲存數值，簡易的對照如下圖
 
 > 若對這個有興趣的話，可以去查「數位邏輯」、「電路學」或修相關課程

![](https://i.imgur.com/o0VuIPk.png)

### 排版方式（Formatting）
一些排版準則如下：
 - 通常在運算元前後會空白
 - 在每個區段的 code 前後會空行，才不會全部擠在一起不好分辨
 - 變數命名要有意義，讓別人也看得懂你在寫什麼
 - 加入註解提高程式易讀性，並說明撰寫邏輯、使用方法等等

寫程式除了讓他可以執行以外，讓別人看懂也是一件很重要的事情。
當未來需要進行多人的大型開發時，程式碼的簡潔易懂可以大大加快開發協作時間。
想了解更多可以搜尋 Google coding style 或 SOLID 原則。