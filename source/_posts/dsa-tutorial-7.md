---
title: 資料結構與演算法教學系列文 (7) - 分治法、動態規劃、前綴和
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:07
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


## 分治法（Divide-and-Conquer）
![image](https://hackmd.io/_uploads/r1NtDxTUR.png)

Divide-and-Conquer又稱為分治法。其中 Divide 指的是將一個較大的問題不斷切割成小問題。而 Conquer 是當最後切割成的小問題簡單到可以直接解決，就可以組合成大問題的答案。在程式語言中時常都會用到分治法的觀念，並結合遞迴的概念求解。
> Source: [分而治之法與遞迴關係](https://hackmd.io/@rd2865OAQZSLjri24DYcow/HkmNAB4aO)

還記得之前教過的 Merge Sort 嗎？（合併排序法：將陣列不斷細分，再將細分後的結果兩兩合併。）其實 Merge Sort 的精神本質上就是 Divide-and-Conquer！

- [【舌尖上的演算法】Day15 -- Divide and Conquer - Merge Sort](https://jumperc2p.github.io/InformisTry/posts/ithome-triathlon/dicon-ms/)

### Leetcode
<!-- - [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)
- [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/) -->
- [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)
- [148. Sort List](https://leetcode.com/problems/sort-list/description/)


## 動態規劃（Dynamic Programming）
![image](https://hackmd.io/_uploads/SkqV4HbSR.png)

**Dynamic Programming = Divide-and-Conquer + Memoization**

動態規劃是一種解決問題的方法，它將大問題拆解成小問題（Divide-and-Conquer），並記錄每個小問題的解答（Memoization），以便後續使用。這樣做能夠節省計算時間，讓我們更有效地解決問題，針對某些「透過前面答案來計算後面答案的問題」特別有用。

- 推薦閱讀：[演算法筆記：DP](https://web.ntnu.edu.tw/~algo/DynamicProgramming.html)

### Recursion v.s. Dynamic Programming?
我們來看看這題（Leetcode [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/description/)）：
- 費波納契數列
    給定輸入整數n，輸出第 n 項費波納契數列
    舉例：n = 8，輸出為 21 (1 1 2 3 5 8 13 21)

Recursion 寫法：
```python=
# Recursion
def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

Dynamic Programming 寫法：
```python=
# Dynamic Programming
def fibonacci_dp(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = [0, 1] + [-1] * (n - 1)
        for i in range(2, n + 1):
            fib[i] = fib[i - 1] + fib[i - 2]
        return fib[n]
```

#### 時間複雜度分析
接著我們來測量一下他們的速度差異：

```python=
import timeit
print("遞迴方法耗時: %.6f 秒"%(timeit.timeit(lambda: fibonacci_recursive(30),number=1)))
print("動態規劃方法耗時: %.6f 秒"%(timeit.timeit(lambda: fibonacci_dp(30),number=1)))
```
```
Output:
遞迴方法耗時: 1.373473 秒
動態規劃方法耗時: 0.000012 秒
```

為什麼會差這麼多呢？我們來分析看看兩種方法的時間複雜度：

- 遞迴版本
時間複雜度：$O(2^n)$。對於每個 fibonacci_recursive(n)，它會呼叫 fibonacci_recursive(n-1) 和 fibonacci_recursive(n-2)，這種重複計算會導致呼叫函數的次數呈指數級數增長，因此時間複雜度為 $O(2^n)$。


- 動態規劃版本
時間複雜度：$O(n)$。它只需要計算一次每個費氏數列的值，並將結果存入列表中。迴圈從 2 執行到 n，所以時間複雜度為 $O(n)$。


對於較小的 n，遞迴可能更簡單易懂，並且兩者的速度可能相差不大。但是當 n 較大時，遞迴所需的時間會嚴重惡化，相較之下動態規劃會有更好的效能表現。

看到上述兩者的時間複雜度差異之大，是不是發現動態規劃的強大了？



### Leetcode
<!-- - [62. Unique Paths](https://leetcode.com/problems/unique-paths/description/) -->
- [63. Unique Paths II]((https://leetcode.com/problems/unique-paths-ii/description/))
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/description/)
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)
- [198. House Robber](https://leetcode.com/problems/house-robber/description/)

<!-- ### 動態規劃經典問題：背包問題（Knapsack Problem） -->
> 延伸閱讀：[演算法筆記：Knapsack Problem](https://web.ntnu.edu.tw/~algo/KnapsackProblem.html)


## 前綴和（Prefix Sum）
![image](https://hackmd.io/_uploads/HJHhReT8R.png)
前綴和是一種用來快速計算數列中某一段連續元素的總和的技巧。它的概念是先建立一個新的數列，其中每個元素代表原數列從開頭到該位置的和。這樣一來，當我們需要計算某段範圍的總和時，只要用前綴和數列中對應位置的值相減，就能快速得出答案。

舉例來說，假設有一個數列 `A=[2, 3, 5, 7]`，我們可以建立前綴和數列 `P=[0, 2, 5, 10, 17]`。如果想知道從第2到第4個元素的總和（即 `A[2] + A[3] + A[4]`），只要計算 `P[4] − P[1]`，就可以得到總和 15。建立數列的過程中可以搭配動態規劃的技巧一起使用。

- [【演算法】前綴和（Prefix Sum）](https://huangmayor0905.github.io/cs/algo/prefix-sum/)

### Leetcode
- [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/description/)
- [1588. Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/description/)

> 延伸閱讀：[Python-LeetCode 581 第四招 前綴和 Prefix Sum](https://hackmd.io/@bangyewu/rJRpH9dhh)
> 延伸閱讀：[線段樹](https://hackmd.io/@wiwiho/CPN-segment-tree)

