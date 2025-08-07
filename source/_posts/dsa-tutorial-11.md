---
title: 資料結構與演算法教學系列文 (11) - 最大子數列問題、背包問題、換錢問題
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:11
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


## 最大子數列問題 (Maximum Subarray Problem)
最大子陣列問題是指在一個整數數列中，找出一段連續子陣列，使其元素總和最大。這是經典的動態規劃問題之一，常用於資料分析，如股價變動趨勢。

![image](https://hackmd.io/_uploads/BJFh7JLZxx.png)


- 例子：給定一個陣列 [-2, -3, 4, -1, -2, 1, 5, -3]，找出總和最大的子陣列。
- 解答：最大子陣列為 [4, -1, -2, 1, 5]，其總和為 7。

### Kadane's Algorithm
Kadane’s Algorithm 是一種專門用來解決此問題的演算法，可在線性時間內計算完成。要了解 Kadane's Algorithm，讓我們從暴力法一步一步來看。

- [滴滴面试手撕算法题-kadane算法](https://zhuanlan.zhihu.com/p/85188269)

#### 暴力法：遍歷全部連續子陣列
最簡單的方式，就是窮舉所有可能的連續子陣列，並計算每一個子陣列的總和，再從中找出最大值。

```python=
def maxSubArrayBF(nums):
    max_sum = nums[0]
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n+1):
            total = sum(nums[i:j])
            max_sum = max(max_sum, total)
    return max_sum
```

- 時間複雜度：$O(n^3)$
- 空間複雜度：$O(1)$

就算我們用小技巧 curr_sum，來優化 sum() 的計算，時間複雜度依舊很高。

```python=
def maxSubArrayBF2(nums):
    max_sum = nums[0]
    n = len(nums)
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum
```

- 時間複雜度：$O(n^2)$
- 空間複雜度：$O(1)$

#### 優化時間：動態規劃
如果我們知道「以某個位置結尾的最大子陣列和」，那我們就可以用它來推導下一個位置的最大值 -> 動態規劃！

* dp[i]: 表示 以 index i 結尾 的最大連續子陣列和。
* dp[i] = max(dp[i-1], 0)+ nums[i]
    * 延續之前的子陣列（dp[i-1] + nums[i]） or 重新開始（nums[i]）
    * 若前面總和小於 0，則完全不取前面，重新計算

```python=
def maxSubArrayDP(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    for i in range(1, n):
        dp[i] = max(dp[i-1], 0) + nums[i]
    return max(dp)
```

- 時間複雜度：$O(n)$
- 空間複雜度：$O(n)$


#### 優化空間：Kadane's Algorithm
如果我們仔細觀察動態規劃的解法，會發現其實根本不需要整個 dp 陣列，因為我們只關心上一個 dp[i-1] 和目前的值。因此，Kadane's Algorithm 利用以下兩個變數，來更進一步優化 dp 解法的空間複雜度：

- local_max：目前位置為結尾的最大子陣列和
-  global_max：迄今為止出現過的最大子陣列和

```python=
def maxSubArrayKadane(nums):
    local_max = global_max = nums[0]
    for i in range(1, len(nums)):
        local_max = max(local_max, 0) + nums[i]
        global_max = max(global_max, local_max)
    return global_max
```

- 時間複雜度：$O(n)$
- 空間複雜度：$O(1)$

至此，最大子數列問題已經被我們用僅僅 6 行的程式碼，加上 $O(n)$ 的時間與 $O(1)$ 的空間解決了。Kadane's Algorithm 是不是很精美呢？

### Leetcode
- [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)
- [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray)
 

## 背包問題（Knapsack Problem）
![image](https://hackmd.io/_uploads/SJHGJ6jgyx.png)

背包問題（Knapsack Problem）是最佳化中的經典問題之一。
該問題的基本形式是：
- 給定一個背包，其容量為固定的正整數（C）
- 給定 N 種物品，每個物品都有自己的重量（w）與價值（v）
- 目標是在不超過背包容量的前提下，選擇若干物品，使得它們的總價值最大

這個問題常用來模擬像是資源分配、投資選擇、或是行程安排等情境，也是一個常出現在演算法課程和競賽中的經典題型。

- [Knapsack Problem - 演算法筆記](https://web.ntnu.edu.tw/~algo/KnapsackProblem.html)
- [ADA Handout (DP), Vivian Chen, NTU CSIE](https://www.csie.ntu.edu.tw/~yvchen/f107-ada/doc/181011_DynamicProgramming2.pdf)

根據限制的種類，背包問題又可以分為以下幾種：

### 分數背包問題（Fractional Knapsack Problem）
- 每樣物品可以被切割（可放部分物品）
- 解法：用貪婪演算法，依據「單位價值」高到低排序放入背包

這個問題的解法很直覺，直接依據「單位價值」（v / w，也就是我們常說的 CP 值）的高低放入背包，直到背包裝滿為止。

```python=
def fractional_knapsack(weights, values, capacity):
    items = sorted(zip(weights, values), key=lambda x: x[1]/x[0], reverse=True)
    total_value = 0
    for w, v in items:
        if capacity >= w:
            total_value += v
            capacity -= w
        else:
            total_value += v * (capacity / w)
            break
    return total_value
```

### 0/1 背包問題（0/1 Knapsack Problem）
- 每樣物品只能選一次（不可切割），也是最經典的背包問題
- 解法：用動態規劃，考慮每一項物品「選」或「不選」

0/1 背包問題是最常見也最經典的背包問題，基本的解法是用 n x C 的 2D DP 矩陣，來代表在不同情況下，背包能達到的最大 total value，計算完後 dp[n][C] 即為解答。

![image](https://hackmd.io/_uploads/By0VJYKGgg.png)


```python=
def knapsack_2d(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]
```

我們也可以再更優化成 1D DP 來節省空間，並同時維持方法的正確性。要注意的是，若僅用一個 DP Array，則在內層迴圈要以倒序方式，才不會讓在該輪更新的值影響到計算。

```python=
def knapsack_1d(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for w in range(capacity, weights[i] - 1, -1):  # 倒序，避免重複選
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]
```


### 有限背包問題（Bounded Knapsack Problem）
- 每樣物品有固定數量，可能可以選擇大於 1 次
- 解法：將物品拆成多個 0/1 物品，把問題轉化成 0/1 背包問題來解

```python=
def bounded_knapsack(weights, values, counts, capacity):
    expanded_weights = []
    expanded_values = []
    for i in range(len(weights)):
        for _ in range(counts[i]):
            expanded_weights.append(weights[i])
            expanded_values.append(values[i])
    return knapsack_1d(expanded_weights, expanded_values, capacity)
```

### 無限背包問題（Unbounded Knapsack Problem）
- 每樣物品可以選無限次
- 解法：動態規劃，不同於 0/1 背包，內層迴圈需順序處理

因為每種物品可以選無限次，我們就不必用倒序方法來避免重複選擇，直接在內層迴圈順序選取即可。

```python=
def unbounded_knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):  # 順序，允許重複選
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]

```

## 換錢問題（Coin Change Problem）
![image](https://hackmd.io/_uploads/rkR7YYtfgg.png)

換錢問題是一個經典的演算法問題，目的是在給定一組硬幣面額與一個目標金額的情況下，找出可以湊出該金額所需的最少硬幣數量。

這個問題常用於訓練動態規劃（Dynamic Programming）技巧，並在許多實際應用中具有重要意義，例如金融系統、自動販賣機與資源分配等。


- [Knapsack Problem#Coin Problem - 演算法筆記](https://web.ntnu.edu.tw/~algo/KnapsackProblem.html)
- [Dynamic programming 深入淺出 - 以 Coin change 為例](https://medium.com/@cutesciuridae/dynamic-programming-%E6%B7%B1%E5%85%A5%E6%B7%BA%E5%87%BA-%E4%BB%A5coin-change%E7%82%BA%E4%BE%8B-4a4f3e7d98ea)

利用這個問題，我們順便來複習一下動態規劃（Dynamic Programming）：
![image](https://hackmd.io/_uploads/rJby5FtGex.png)


以這個問題為例：
1. 定義狀態 [我在哪裡]
DP[n] =找出n元最精簡的找零零錢數目(用最少數目的銅板湊出)
2. 定義狀態轉移關係式(通則) [我從哪裡來] => [答案從哪裡推導而來]
![image](https://hackmd.io/_uploads/HkegB9YFfgl.png)
3. 釐清初始狀態(終止條件) [第一步怎麼走，怎麼出發的]
用每個銅板去縮小找零問題的規模，從n元找零問題一直化簡，降到0元的找
終止狀態：
0元的找零方法：0，代表不拿任何一枚銅板
<0元的找零方法：不合法，應該停止計算，可用 float('inf') 來處理

### Leetcode
- [322. Coin Change](https://leetcode.com/problems/coin-change/description/)
<!-- - [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/description/) -->

<!-- ## 旅行銷售員問題（TSP, Traveling Salesman Problem）
![image](https://hackmd.io/_uploads/Sk8U16sekl.png)  -->


<!-- # Progress check
## 講義
- TODO: 尋找更多主題
- TODO: Update to blog

## 學生
- 進階演算法： LC 42, 239 not finished, Kadane finish
-->