---
title: 資料結構與演算法教學系列文 (6) - 暴力法、貪婪演算法、回溯法
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:06
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


# 其他演算法與常見解題技巧
演算法（Algorithm）是在有限的步驟之內，提供明確的法則，求出問題正確答案的程序。它可以是一種方法、法則或者程序，讓資料可按照預先設計的方式處理。

- [認識演算法](https://hackmd.io/@howkii-studio/Bkf-2DQiw/https%3A%2F%2Fhackmd.io%2F%40howkii-studio%2Falgorithm)
- 推薦補充閱讀：[演算法筆記](https://web.ntnu.edu.tw/~algo/)
    - [Algorithm Design](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)

## 暴力法（Brute Force）
暴力法（Brute Force）是一種基本的解題策略，透過系統地嘗試所有可能的解決方案來找出答案。它的原理很簡單：列舉所有可能性，不斷嘗試，直到找到符合要求的解。

這種方法的優點是實現簡單，且保證能找到存在的解。但它的效率通常較低，特別是在處理大規模問題時，因此暴力法常用於簡單問題或作為其他算法的比較基準。

以下補充幾個以前教過，但其實都跟暴力法有關的演算法。
> 補充：[【舌尖上的演算法】Day6 -- Brute Force - Selection Sort](https://jumperc2p.github.io/InformisTry/posts/ithome-triathlon/brute_force_selection_sort/)
> 補充：[【舌尖上的演算法】Day7 -- Brute Force - Bubble Sort](https://jumperc2p.github.io/InformisTry/posts/ithome-triathlon/brute_force_bubble_sort/)
> 補充：[【舌尖上的演算法】Day8 -- Brute Force - Knapsack](https://jumperc2p.github.io/InformisTry/posts/ithome-triathlon/brute_force_knapsack/)
> 補充：[【舌尖上的演算法】Day9 -- Brute Force - DFS & BFS](https://jumperc2p.github.io/InformisTry/posts/ithome-triathlon/brute_force_dfs_bfs/)

## 貪婪演算法（Greedy Method）
![image](https://hackmd.io/_uploads/SkFiTx6U0.png)

貪婪演算法（Greedy Method）是一種在每一步都做出當前最佳選擇的問題解決策略。它通過在每個決策點選擇局部最優解，希望最終能達到整體最優解。

貪婪演算法的主要特點：

1. 在每一步選擇當前看起來最好的選項
2. 一旦做出選擇，就不會回頭重新考慮
3. 期望這些局部最優選擇能導致整體最優解

這種演算法通常簡單高效，適用於某些特定問題，然而它並不總是能得到最佳解決方案。貪婪演算法的優勢在於易於實現和速度快，但可能會錯過需要前瞻性思考或回溯的更優解。

### Leetcode
- [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/description/)
- [948. Bag of Tokens](https://leetcode.com/problems/bag-of-tokens/description/)
<!-- - [2037. Minimum Number of Moves to Seat Everyone](https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/) -->


## 回溯法（Backtracking）
![image](https://hackmd.io/_uploads/Bkad6xpLC.png)

回溯法（Backtracking）也是暴力法的一種，特別適用於需要窮舉所有可能性的情況。

回溯法的基本思想是:
1. 從一個可能的起點開始。
2. 按照問題要求，逐步向前探索。
3. 如果發現當前路徑無法得到有效解，就退回到上一步。
4. 在上一步選擇一個不同的方向繼續探索。
5. 重複這個過程，直到找到解或者探索完所有可能性。

回溯法的優點是能夠系統地搜索所有可能性，缺點是在最壞情況下可能需要很長的運行時間。這種方法像是在迷宮中探路：如果碰到死路，就退回到上一個路口，選擇另一條路繼續前進。


- [一次看懂遞迴 (Recursion) 的思維模式（三）- 窮舉可能性（Backtracking）](https://medium.com/appworks-school/%E9%80%B2%E5%85%A5%E9%81%9E%E8%BF%B4-recursion-%E7%9A%84%E4%B8%96%E7%95%8C-%E4%B8%89-d2fd70b5b171)

### Leetcode
- [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/)
- [46. Permutations](https://leetcode.com/problems/permutations/description/)
