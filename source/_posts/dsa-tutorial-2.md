---
title: 資料結構與演算法教學系列文 (2) - 陣列、鏈結串列、堆疊、佇列
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:02
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


# 資料結構（Data Structure）
資料結構是一種設計、組織、儲存資料的方式，以實現最佳性能和效率。這些結構包含不同形式，像是陣列、鍊結列表、樹、圖等等。選擇適當的資料結構對於解決特定的問題至關重要，不同的資料結構可以用於不同的應用，並且可以極大地影響程序的運行時間和記憶體使用。

## 陣列（Array）
![](https://hackmd.io/_uploads/SJJ_pSKMa.png)
可隨機存取的一串連續記憶體位址。
- [陣列 (Array) 簡介](https://notfalse.net/15/array-intro)
> 補充：[List Are Arrays in Python](https://michaeliscoding.com/lists-are-arrays-in-python/)
### Leetcode
- [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [27. Remove Element](https://leetcode.com/problems/remove-element/description/)

## 鏈結串列（Linked List）
![](https://hackmd.io/_uploads/HkbKTHFG6.png)
元素間彼此串聯在一起，形成一條鍊子的資料結構。
![image](https://hackmd.io/_uploads/SkxzAOjQp.png)
也可以是上圖雙向連結的形式。

- [Linked List：Intro(簡介)](https://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)
- [Linked List：新增資料、刪除資料、反轉](https://alrightchiu.github.io/SecondRound/linked-list-xin-zeng-zi-liao-shan-chu-zi-liao-fan-zhuan.html)

### Leetcode
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## 堆疊（Stack, Last-In-First-Out, LIFO）
![](https://hackmd.io/_uploads/BkdcTSFMp.png)
單向進出，後進先出的資料結構，如同把東西堆疊起來。
- [Stack: Intro(簡介)](https://alrightchiu.github.io/SecondRound/stack-introjian-jie.html)
- [Stack: 以Array與Linked list實作](https://alrightchiu.github.io/SecondRound/stack-yi-arrayyu-linked-listshi-zuo.html)
- [Special Application: Min Stack](https://alrightchiu.github.io/SecondRound/stack-neng-gou-zai-o1qu-de-zui-xiao-zhi-de-minstack.html)

## 佇列（Queue, First-In-First-Out, FIFO）
![](https://hackmd.io/_uploads/H1tjpHFM6.png)
單向進出，先進先出的資料結構，如同在排隊一般。

- [Queue: Intro(簡介)，並以Linked list實作](https://alrightchiu.github.io/SecondRound/queue-introjian-jie-bing-yi-linked-listshi-zuo.html)
- [Queue: 以Array實作Queue](https://alrightchiu.github.io/SecondRound/queue-yi-arrayshi-zuo-queue.html)

## Stack & Queue in Python: Collections.deque()
Deque（發音類似 Deck）為 Double-Ended Queue 的縮寫，顧名思義，Deque 是一個支援雙向存取的 Queue，也就是說，你可以從頭跟尾插入或移除元素。
 - [官方說明文件](https://docs.python.org/zh-tw/3/library/collections.html#collections.deque)

```python=
from collections import deque
D = deque([1,2,3])
D.append(4)
D.appendleft(0)
print(D[2], D)
print(D.pop(), D)
print(D.popleft(), D)
```
```
Output:
2 deque([0,1,2,3,4])
4 deque([0,1,2,3])
0 deque([1,2,3])
```
Q：那他與 Stack 跟 Queue 有甚麼關係呢？
> A：
> Stack: 只使用 D.append() 與 D.pop() 的 deque
> Queue: 只使用 D.append() 與 D.popleft() 的 deque
>
> 其實只要符合 Stack 跟 Queue 的性質都可以。
> 因此以下使用方式也對，但較不建議使用：
> Stack: 只使用 D.appendleft() 與 D.popleft() 的 deque
> Queue: 只使用 D.appendleft() 與 D.pop() 的 deque

以下為使用 collections.deque 來實作 stack 與 queue 的例子：
```python=
from collections import deque

# For Stack, you can only use the following operations
S = deque()
# push from a stack:
S.append(val)
# pop from a stack:
val = S.pop()
# peek from a stack:
top = S[-1]
# check size of a stack:
size = len(S)
# check stack is empty:
isEmpty = (size == 0)

# =========================================
# For Queue, you can only use the following operations
Q = deque()
# push from a queue: 
Q.append(val)
# pop from a queue:
val = Q.popleft()
# peek from a queue:
top = Q[0]
# check size of a queue:
size = len(Q)
# check queue is empty:
isEmpty = (size == 0)
```
另外也可以參考 Python 官方對 [將 List 作為 Stack / Queue 使用](https://docs.python.org/zh-tw/3/tutorial/datastructures.html#using-lists-as-stacks) 的說明。

介紹完 collections.deque() 以後，讓我們來實際練習一下 Leetcode 的題目吧！

### Leetcode
#### Stack
- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [155. Min Stack](https://leetcode.com/problems/min-stack/description/)
- [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

#### Queue
- [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [341. Flatten Nested List Iterator](https://leetcode.com/problems/flatten-nested-list-iterator/)
- [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)


