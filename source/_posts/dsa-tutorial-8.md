---
title: 資料結構與演算法教學系列文 (8) 字串比對、位元運算、雙重指標
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:08
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


## 字串比對（String Matching）
### KMP 演算法
![image](https://hackmd.io/_uploads/ry2SjfO4C.png)

KMP 演算法是一種用於字串搜尋的高效方法。透過建立部分配對表（最長的相同前後綴），可以快速定位搜尋字串中的可能配對位置，減少不必要的重複比較，從而加速搜尋過程。

KMP 演算法其實相對複雜且較難實作，我個人認為有大概理解概念就好，實際上也很少遇到需要直接實作該演算法的情境。

- [初學者學 KMP 演算法](https://yeefun.github.io/kmp-algorithm-for-beginners/)
> 補充：[KMP algorithm，從自學到放棄 (1)](https://medium.com/@c.s.fangyolk/kmp-%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E8%87%AA%E5%AD%B8%E5%88%B0%E6%94%BE%E6%A3%84-1-7f71e65839a0)
> 補充：[KMP algorithm，從自學到放棄 (2)](https://medium.com/@c.s.fangyolk/kmp-%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E8%87%AA%E5%AD%B8%E5%88%B0%E6%94%BE%E6%A3%84-2-94dda22f80b2)
> 補充：[演算法筆記：substring](https://web.ntnu.edu.tw/~algo/Substring.html)
> 補充：[KMP Visualization](https://cmps-people.ok.ubc.ca/ylucet/DS/KnuthMorrisPratt.html)

### Leetcode
- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)



## 位元運算（Bit Manipulation）
![image](https://hackmd.io/_uploads/HyHM0lpLR.png)

Bit manipulation 是在電腦中用「位元」（bit）來進行操作的技巧，這種技巧常在程式設計競賽或像 Leetcode 這樣的題目中出現。位元是電腦中最基本的單位，由 0 或 1 組成，這跟開關一樣，只有開或關的狀態。這些 0 與 1 會再經由[二進位制](https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%BF%9B%E5%88%B6)與[二補數](https://zh.wikipedia.org/wiki/%E4%BA%8C%E8%A3%9C%E6%95%B8)的方式，組成所有的其他數字。常見的位元操作有：AND, OR, XOR, NOT, Shift 等等，參考以下：
![image](https://hackmd.io/_uploads/HkgbJHIDR.png)
- [Python 的位元運算](https://hackmd.io/@apcser/H14FONT4n?utm_source=preview-mode&utm_medium=rec)


### Leetcode
- [231. Power of Two](https://leetcode.com/problems/power-of-two/description/)
- [268. Missing Number](https://leetcode.com/problems/missing-number/description/)
- [2220. Minimum Bit Flips to Convert Number](https://leetcode.com/problems/minimum-bit-flips-to-convert-number/description/)

## 雙重指標（Two Pointers）
![image](https://hackmd.io/_uploads/BkqW-uvkyl.png)
常用於陣列當中，用兩個指標指著不同的位置，與滑動視窗（Sliding Window）有異曲同工之妙，兩者基本上是相同技巧。

### 快慢指標（Fast & Slow Pointers）
此種技巧為雙重指標的特殊版本，使用一快一慢的指標（一次走不同步數 or 一個先走一個後走），常用在 Linked List 當中。

這樣可以幹嘛呢？我們來看看以下的例子：

#### 尋找中點
![image](https://hackmd.io/_uploads/H1c7bdv1Jl.png)

#### 判斷 Cycle 是否存在 Linked List 中
![image](https://hackmd.io/_uploads/HkLZzOPJJg.png)
![image](https://hackmd.io/_uploads/Byf5Wdv11e.png)

#### 尋找倒數第 K 個節點
![image](https://hackmd.io/_uploads/ry3NMVU8yx.png)


- [演算法筆記系列 — Two Pointer 與Sliding Window](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E6%BC%94%E7%AE%97%E6%B3%95%E7%AD%86%E8%A8%98%E7%B3%BB%E5%88%97-two-pointer-%E8%88%87sliding-window-8742f45f3f55)

### Leetcode
 - [75. Sort Colors](https://leetcode.com/problems/sort-colors/)
 - [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
 - [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

