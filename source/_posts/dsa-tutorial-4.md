---
title: 資料結構與演算法教學系列文 (4) - 矩陣、堆積、優先佇列
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:04
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


## 矩陣（Matrix）
![image](https://hackmd.io/_uploads/SyxulaZA6.png)

在介紹 Graph 的表示方法時，我們提到了兩種不同的表示方式，分別是鄰接串列（Adjacency List）與鄰接矩陣（Adjacency Matrix）。不過其實，矩陣本身也可以被當作一種資料結構來使用，舉凡像是迷宮、地圖等等具有 2D 性質的資料型態，都可以使用矩陣來表示。

Matrix 的相關操作其實都與 Graph 差不多，不外乎就是在 Matrix 中進行搜尋或遍歷，但因為我們可以以 $O(1)$ 的複雜度，直接取用 Matrix 內部中的任一元素（`matrix[row][col]`），所以 Matrix 在某些應用上具有較為快速的優勢。那接著就讓我們直接實戰演練吧！
### Leetcode
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)
- [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description/)
- [1351. Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/)

## 堆積（Heap）
![](https://hackmd.io/_uploads/BJqGCStzT.png)
一種具有特殊性質（Parent Node 大於或小於 Child Node）的 Complete Binary Tree。

### 堆積排序法(Heap Sort)
- [[演算法(Algorithm)] 堆積排序法(Heap Sort)](https://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php)

對陣列做 Heapify 變成 Max Heap，再不斷把最大值往後擺。
> 練習：試著實作 Heap Sort 吧！

## 優先佇列（Priority Queue）
![image](https://hackmd.io/_uploads/S1CWOylZ0.png)
具有優先權（Priority）來代表其進出順序的 Queue。

- [Priority Queue：Intro(簡介)](https://alrightchiu.github.io/SecondRound/priority-queueintrojian-jie.html)
- [Priority Queue：Binary Heap](https://alrightchiu.github.io/SecondRound/priority-queuebinary-heap.html)

### Stack / Queue v.s. Priority Queue?
Stack 與 Queue 其實可以被視作特殊狀況的 Priority Queue：
- Stack：加入 Priority Queue 的 Priority 是嚴格遞增的
    - 因此最後加入的元素 Priority 最高，會先被丟出 Stack
- Queue：加入 Priority Queue 的 Priority 是嚴格遞減的
    - 因此最先加入的元素 Priority 最高，會先被丟出 Queue
<!-- In a stack, the priority of each inserted element is monotonically increasing; thus, the last element inserted is always the first retrieved. In a queue, the priority of each inserted element is monotonically decreasing; thus, the first element inserted is always the first retrieved. -->

### Priority Queue v.s. Heap?
- Priority Queue：一種**抽象資料類別**，著重的點是描述這個資料類別應該具有甚麼性質與操作方法，不直接討論實作方法。
- Heap：一種**資料結構**，著重的點在以特定的結構儲存資料。

因為他們具有類似的性質，所以用 Heap 的結構來實作 Priority Queue 這個資料類別，可以說是非常適合，也因此乍看之下他們好像是一樣的東西。但兩者概念上有些微不同，亦可以用其他方式來實做  Priority Queue。

> 補充：[Difference between priority queue and a heap](https://stackoverflow.com/a/18993313/15894431)
> 補充：[What's the difference between heapq and PriorityQueue in python?](https://stackoverflow.com/questions/36991716/whats-the-difference-between-heapq-and-priorityqueue-in-python)

## Heap / Priority Queue in Python: heapq
- [Python heapq](https://docs.python.org/zh-tw/3.10/library/heapq.html)
```python=
import heapq
heap = [9,7,5,3,1]
heapq.heapify(heap)
heapq.heappush(heap, 2)
_ = heapq.heappop(heap)
_ = heapq.heappushpop(heap, 2)
# Will not modify the heap (but inefficient)
klargest = heapq.nlargest(k, heap)
ksmallest = heapq.nsmallest(k, heap)
# Use heap as priority queue
nodes = [(5, 'A'), (2, 'B'), (9, 'C')]
heap = []
for node in nodes:
    heapq.heappush(heap, (node[0], node[1])) # (priority, value)
```

### Leetcode
- [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/description/)
- [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/description/)
- [1642. Furthest Building You Can Reach](https://leetcode.com/problems/furthest-building-you-can-reach/description/)

