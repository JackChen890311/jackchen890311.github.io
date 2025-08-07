---
title: 資料結構與演算法教學系列文 (1) - 概述、排序、搜尋、時間複雜度
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:01
---

哈囉！久違又來更新教學文系列了，這次的主題是在學完基礎程式設計後，一定也需要會的東西：資料結構與演算法。若你對程式設計還不太熟悉，或是想回去複習一下 Python 或 C++，可以參考我下面的系列文：
- [Python 教學](https://jackchen890311.github.io/categories/Python-%E6%95%99%E5%AD%B8/) 
- [C++ 教學](https://jackchen890311.github.io/categories/C-%E6%95%99%E5%AD%B8/) 

這個系列文應該會很長，因為 DSA（i.e. Data Structure and Algorithm）這個主題是在是涵蓋太多東西了，甚至我寫的內容也沒有到很完整。這次的來源一樣是拿來做家教講義，文字部分不會太詳盡，有需要更詳盡的內容歡迎聯絡我，如果我有空就可以幫你上課 XD。

最後就是轉載請記得標註來源，這裡面的內容都是作者本人收集的心血！

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


![](https://hackmd.io/_uploads/Sy7FTNHea.png)

# 入門介紹
- [Google Coding Style](https://google.github.io/styleguide/pyguide.html)
- [甚麼是演算法？](https://jason-chen-1992.weebly.com/home/-whats-algorithm)
- [甚麼是資料結構？](https://hackmd.io/@Aquamay/H1nxBOLcO/https%3A%2F%2Fhackmd.io%2F%40Aquamay%2Frk1C8ni5d)

來複習一下學習地圖，以臺大資工系必修為例：
![](https://i.imgur.com/Y2AdRO3.png)
以臺大資管系必修為例：
![](https://i.imgur.com/aC9lfrs.png)

而在演算法與資料結構的世界裡面，大概又可以分為以下幾種類別。在我們之後的課程中，會逐漸的介紹每個名詞以及其對應概念：
![image](https://hackmd.io/_uploads/BkmCHf7UR.png)

相關連結：
- [How to master DSA](https://blog.algomaster.io/p/how-i-mastered-data-structures-and-algorithms)
- [labuladong 的算法筆記](https://labuladong.online/algo/home/)
- [演算法與資料結構](https://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)

# 競賽相關
適合國 / 高中生參加的相關競賽有以下：
- [Bebras 國際運算思維挑戰（簡單）](https://bebras.csie.ntnu.edu.tw/)
- [APCS（個人）](https://apcs.csie.ntnu.edu.tw/)
- [ISSC（團體）](https://issc.csroc.org.tw/)
- [TOI（資訊奧林匹亞，較難）](https://tpmso.org/toi/)

建議可以向學校老師或相關社團與補習班詢問更多細節。

### APCS Practice
- [應試相關資訊](https://apcs.csie.ntnu.edu.tw/index.php/info/)
    - 建議每項都要讀過，特別是環境 / 作答系統 / 考場規則
#### 實作題
- [2025/01 APCS](https://zerojudge.tw/Problems?tag=2025%E5%B9%B41%E6%9C%88) and [Solution](https://hackmd.io/@bangyewu/rJlvXNP81g)
- [2024/10 APCS](https://zerojudge.tw/Problems?tag=2024%E5%B9%B410%E6%9C%88) and [Solution](https://hackmd.io/@bangyewu/rJ5yJqEe1x)
- [2024/06 APCS](https://zerojudge.tw/Problems?tag=2024%E5%B9%B46%E6%9C%88) and [Solution](https://hackmd.io/cn9ndy19RbKHOJKBRx4aEA)
- [2024/01 APCS](https://zerojudge.tw/Problems?tag=2024%E5%B9%B41%E6%9C%88) and [Solution](https://hackmd.io/@bangyewu/SkKxG8Oua)
- [2023/10 APCS](https://zerojudge.tw/Problems?tag=2023%E5%B9%B410%E6%9C%88) and [Solution](https://hackmd.io/@bangyewu/SkxXo4QGa)
- [2023/06 APCS](https://zerojudge.tw/Problems?tag=2023%E5%B9%B46%E6%9C%88) and [Solution](https://hackmd.io/@bangyewu/B13lefwMp)
- [All APCS Problems](https://zerojudge.tw/Problems?tag=APCS) and [Solution](https://hackmd.io/@bangyewu/B13lefwMp) and [Solution 2](https://yuihuang.com/apcs/)

#### 觀念題
- [APCS 觀念題分析系列](https://hackmd.io/@howkii-studio/apcs_overview/https%3A%2F%2Fhackmd.io%2F%40howkii-studio%2Fapcs_exercise_cs)
- [APCS 觀念題資源分享](https://hackmd.io/@apcser/B1N5GYEto)

#### 相關資源
- 推薦：[AP325 - 從 APCS 實作題檢測三級到五級（C++）](https://drive.google.com/file/d/1hX7q3wVKkLuoMhEEm7uuLjq4BuhZAEgn/view?usp=drive_link)
    - [AP325（Python）](https://hackmd.io/@bangyewu/Hy2kbYLI6/%2Fg2kqHh5_Q4eQnz-mfNu3Kw)
- [FB Group - APCS 實作題檢測](https://www.facebook.com/groups/359446638362710/)
- [PyAp45 Playlist - Python on APCS 四五級分](https://www.youtube.com/playlist?list=PLpmg1QLbgMuRQXHRkX9iDHyAVIW1D6OJF)


# 排序演算法（Sorting Algorithms）
![image](https://hackmd.io/_uploads/Hk0Xhj8x0.png)

排序演算法是一種將一組資料按照特定規則重新排列的方法。

常見的排序方法有：
- 選擇排序法(Selection Sort)
每次挑最大或最小的，依序移動到對應的位置。
- 插入排序法(Insertion Sort)
照順序每次拿一個，並插入正確的位置。
- 氣泡排序法(Bubble Sort)
就像有個氣泡，兩兩比對後留下大的，每次都把最大的帶到最後面。
- 合併排序法(Merge Sort)
將陣列不斷細分，再將細分後的結果兩兩合併。
- 快速排序法(Quick Sort)
選定一個 Pivot，將比他小的丟左邊比他大的丟右邊，再針對左右兩部分進行一次相同的事情。

練習：試著實作以上五種常見的 Sorting 方法吧！

> **推薦參考**：[介紹排序演算法的網站](http://notepad.yehyeh.net/Content/Algorithm/Sort/Sort.php)
> **推薦參考**：[寫程式的基本功：排序演算法](https://magiclen.org/sorting-algorithm/)
> 補充：[Python 中的 sorting](https://officeguide.cc/python-sort-sorted-tutorial-examples/)、[C++ 中的 sorting](https://shengyu7697.github.io/std-sort/)
> 補充：[最貼近現實的排序演算法 - Timsort](https://jason18153.medium.com/%E6%9C%80%E8%B2%BC%E8%BF%91%E7%8F%BE%E5%AF%A6%E7%9A%84%E6%8E%92%E5%BA%8F%E6%BC%94%E7%AE%97%E6%B3%95-timsort-a75da75b65a2)

補充：還有一些很奇怪的排序方法，看了會覺得很傻眼又好笑。如果有興趣可以參考 [10 Forbidden Sorting Algorithms](https://www.youtube.com/watch?v=ktgxMtWMflU) ，舉幾個例子像是：
- Bogo 排序法（Bogo Sort）
一直隨機重新排序，直到剛好符合大小順序。（猴子打字機定理）
- 史達林排序法（Stalin's Sort）
遇到大小順序不對的就直接刪掉。（所以最後的 list 有可能比原本的短）

# 搜尋演算法（Search Algorithms）
![image](https://hackmd.io/_uploads/HyNn3iIl0.png)

搜尋演算法是一種用來在資料集中尋找特定項目的方法或步驟。

## 適用於未排序或已排序的資料
### 線性搜尋（Linear Search）
直接一項一項搜尋，直到找到要的東西為止。
最基本的搜尋方式，時間複雜度為 $O(N)$。

## 僅適用於排序的資料
以下的搜尋演算法，會利用資料**已經排序過**的性質，來加速搜尋的過程。

### 二分搜尋（Binary Search）
很重要的搜尋演算法！將資料中間的與目標相比，若目標較大則往右再做一次搜尋，目標較小則往左，直到找到為止，可以參考 [二分搜尋法教學](https://magiclen.org/binary-search/) 與 [二分搜尋法的一些細節](https://medium.com/appworks-school/binary-search-%E9%82%A3%E4%BA%9B%E8%97%8F%E5%9C%A8%E7%B4%B0%E7%AF%80%E8%A3%A1%E7%9A%84%E9%AD%94%E9%AC%BC-%E4%B8%80-%E5%9F%BA%E7%A4%8E%E4%BB%8B%E7%B4%B9-dd2cd804aee1)。
#### Leetcode:
- [35. Search Insert Position](https://leetcode.com/problems/search-insert-position/)
- [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- [278. First Bad Version](https://leetcode.com/problems/first-bad-version)

### 指數搜尋（Exponential Search）
與二分搜尋類似，只是使用 2^N 作為搜尋的 index。
### 插補搜尋（Interpolation Search）
用線性插值的概念，來加速尋找的過程。

> **推薦參考**：[寫程式的基本功：搜尋演算法](https://magiclen.org/search-algorithm/)


# 時間複雜度（Time Complexity）
時間複雜度是衡量演算法執行效率的一個重要指標，表示隨著輸入規模增加，算法執行所需時間的增長速度。

常用的符號有：
- O-Notation：Big-O（Worst Case，最差）
- Θ-Notation：Big-Theta（Average Case，平均）
- Ω−Notation：Big-Omega（Best Case，最佳）

一般來說，我們最關心的是最差狀況下的時間複雜度（Big-O），關於詳細的數學推導可以參見補充。一些常見的時間複雜度與其例子為：
* $O(1)$：陣列讀取
* $O(n)$：簡易搜尋
* $O(log n)$：二分搜尋
* $O(nlogn)$：合併排序
* $O(n^2)$：選擇排序
* $O(2^n)$：費波那契數列（遞迴版本）

![](https://hackmd.io/_uploads/rk2-JzHlp.png)


我們來看看這些例子是如何被計算出來的：
- [初學者學演算法｜從時間複雜度認識常見演算法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E8%AA%8D%E8%AD%98%E5%B8%B8%E8%A6%8B%E6%BC%94%E7%AE%97%E6%B3%95-%E4%B8%80-b46fece65ba5)
- [初學者學演算法｜排序法進階：合併排序法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)
- [初學者學演算法｜從費氏數列認識何謂遞迴](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E8%B2%BB%E6%B0%8F%E6%95%B8%E5%88%97%E8%AA%8D%E8%AD%98%E4%BD%95%E8%AC%82%E9%81%9E%E8%BF%B4-dea15d2808a3)


> 補充：[複雜度與漸進符號之數學](http://alrightchiu.github.io/SecondRound/complexityasymptotic-notationjian-jin-fu-hao.html) 
> 補充：[時間複雜度與空間複雜度](https://jason-chen-1992.weebly.com/home/time-space-complexity)
 
## 補充：Complexity Cheat Sheet
若不知道圖中的資料結構是什麼的話，可以先往下看。
![](https://hackmd.io/_uploads/BkfMZStGp.png)
![](https://hackmd.io/_uploads/BJ50lHYGp.png)