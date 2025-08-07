---
title: 資料結構與演算法教學系列文 (10) - 差分陣列、單調堆疊/佇列
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:10
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


## 差分陣列（Difference Array）
![image](https://hackmd.io/_uploads/HkVH0QvMyl.png)

差分陣列是一種快速處理**區間更新**的技巧，特別適用於頻繁對陣列特定區間進行加減的情境，其基於前綴和（Prefix Sum）的概念來輔助實現。

其核心概念是透過維護一個輔助陣列 diff，來記錄原陣列的數值變化，使得區間的加減可以在 O(1) 時間內完成，而最終結果則可透過前綴和的技巧來計算。


### 輔助陣列的建立
輔助陣列 diff 的計算方法為：
diff[0] = nums[0]
diff[i] = nums[i] - nums[i-1] (i > 0) 

---

以上圖來看，原陣列 nums 是 [8, 2, 6, 3, 1]：
diff[0] = 8
diff[1] = nums[1] - nums[0] = 8 - 2 = -6
diff[2] = nums[2] - nums[1] = 6 - 2 = 4
...
diff = [8, -6, 4, -3, -2]

有注意到嗎？每個 diff 記錄的是「這個位置與上個位置的差異」。紀錄差異而不記錄實際數值，將會幫助我們更容易的更新整個區間。


### 區間的更新
在建立完輔助陣列 diff 後，若要對原陣列 nums 在區間 [L, R] 內的所有元素加上 X，則執行：
diff[L] += X（標記從 L 開始增加 X）
diff[R+1] -= X（標記從 R+1 開始減少 X）

最終透過前綴和來還原結果： 
nums[i] = nums[i-1] + diff[i]

---

以上圖來看，若我們想在 [1, 3] 之間的所有元素增加 2：
diff[1] += 2
diff[3] -= 2
diff = [8, -4, 4, -5, -2]

透過前綴和還原的結果為：
nums2 = [8, 4, 8, 3, 1]

相比原本的結果：
nums = [8, 2, 6, 3, 1]

是不是很神奇！

- [小而美的算法技巧：差分陣列](https://labuladong.online/algo/data-structure/diff-array/)

### Leetcode
- [1094. Car Pooling](https://leetcode.com/problems/car-pooling/description/)
- [1109. Corporate Flight Bookings](https://leetcode.com/problems/corporate-flight-bookings/description/)


## 單調堆疊/佇列（Monotonic Stack/Queue）
單調堆疊和單調佇列是處理數列問題的工具，與一般的堆疊/佇列類似，但差異是我們在遍歷陣列時，會持續保持堆疊/佇列裡面的元素「有規律地排序」，比如從小到大或從大到小，而那些不符合順序的會將其剔除，並拿來做我們需要的運算。

一般來說，比較常使用到的是單調堆疊，因此在 Leetcode 上也比較有機會看到。單調佇列的概念基本上差不多，只差在移除元素的方法與應用情景不同。

<!-- ![image](https://hackmd.io/_uploads/rypgyhjgkx.png) -->

<!-- - [演算法筆記系列 — Monotonic Stack/Queue](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E6%BC%94%E7%AE%97%E6%B3%95%E7%AD%86%E8%A8%98%E7%B3%BB%E5%88%97-monotonic-stack-queue-5ad1c35a3dfe) -->

### 單調堆疊（Monotonic Stack）
覺得上面有點複雜的話，我們可以來看看以下的例子：

#### 單調遞增堆疊（Monotonically Increasing Stack）
![image](https://hackmd.io/_uploads/r1gLZiqBye.png)
在遞增的情境下，我們遍歷原始陣列，並將元素加入堆疊中。但若新加入的元素比堆疊頂端的元素還小，我們就將頂端元素取出，再做一次檢查，重複執行直到「單調遞增」的性質被滿足為止。

#### 單調遞減堆疊（Monotonically Decreasing Stack）
![image](https://hackmd.io/_uploads/ByJw-ocByl.png)

#### 單調堆疊的應用
單調堆疊的主要應用是快速處理「最近相關」的問題，特別是數列中每個元素的上一個/下一個更大值/更小值。


假設數列 value = [6, 2, 5, 7]，求每個數的「下一個更大值」。
* 初始化：
    * stack = [] # (index, value) of element
    * result = [-1, -1, -1, -1] # next greater element
* 遍歷：
    * 6: stack = [(0, 6)], result = [-1, -1, -1, -1]
    * 2: stack = [(0, 6), (1, 2)], result = [-1, -1, -1, -1]
    * 5: stack = [(0, 6), (2, 5)], result = [-1, 5, -1, -1]
        * Remove (1, 2) (value[1] = 2 < value[2] = 5)
        * result[1] = value[2] = 5
    * 7: stack = [(3, 7)], result = [7, 5, 7, -1]
        * Remove (2, 5) (value[2] = 5 < value[3] = 7)
        * result[2] = value[3] = 7
        * Remove (0, 6) (value[0] = 6 < value[3] = 7)
        * result[0] = value[3] = 7
* 結果：[7, 5, 7, -1]

- [參考：Monotonic Stack – 陪你刷題](https://haogroot.com/2020/09/01/monotonic-stack-leetcode/)

#### Leetcode
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/description/)
- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/description/)
- [739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/description)


### 單調佇列（Monotonic Queue）
與單調堆疊類似，但單調佇列不是嚴格意義上的佇列。單調佇列允許從兩端移除元素，與一般佇列的只能進先出不同，這麼做的好處是方便我們處理特定的問題。

#### 單調佇列的應用
![image](https://hackmd.io/_uploads/Syq69Jsrkg.png)
單調隊列的主要用途是處理「滑動窗口」問題。滑動窗口是指在數列中一段固定範圍內進行計算，像找最大值或最小值。


假設數列 value = [3, 2, -3, -1, 0]，求各個滑動窗口（k = 3）的最大值。
* 初始化：
    * queue = [] # (index, value) of element
    * result = [] # sliding window maximum
* 遍歷：
    * [3, 2, -3]: queue = [(0, 3), (1, 2), (2, -3)], result = [3]
        * The value of queue is monotonic
        * Add value[0] = 3 to result
    * [2, -3, -1]: queue = [(1, 2), (3, -1)], result = [3, 2]
        * Remove (2, -3) (value[2] = -3 < value[3] = -1)
        * Remove (0, -3) (exceeding boundary)
        * Add value[1] = 2 to result
    * [-3, -1, 0]: queue = [(4, 0)], result = [3, 1, 0]
        * Remove (3, -1) (value[3] = -1 < value[4] = 0)
        * Add (4, 0) in queue for this round
        * Remove 1 for exceeding boundary
        * Add value[4] = 0 to result
* 結果：[3, 2, 0]

- [參考：Sliding Window Maximum – Monotonic queue 的應用](https://bengersay.com/sliding-window-maximum/)


#### Leetcode
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)


### 為什麼一個可以從兩端移除，一個只能從一端？
為什麼會有這樣的差異？
* 單調堆疊（Monotonic Stack）：
    * 資料的處理是單方向的（例如從左到右或從右到左）。
    * 只有最近加入的元素是相關的，因此僅需從頂部彈出即可。
* 單調隊列（Monotonic Queue）：
    * 資料是動態處理的，通常涉及一個範圍（例如滑動視窗）。
    * 兩端的元素都可能變得不相關：前端的元素可能因為超出視窗範圍而需要移除，而後端的元素可能因違反單調性而需要移除。


單調堆疊與單調佇列算是比較進階與特殊的資料結構，平常我們並不會常常使用，但在某些情況下，他們的單調性質可以很好的幫我們解決特定問題，因此也是值得學習的主題。
 
 
