---
title: 資料結構與演算法
categories:
  - 
tags:
  - 
cover: /img/cover/C++.png
date: 2025-03-28 15:57:07
---

# 演算法與資料結構入門
本文所有內容與資料皆由本人蒐集與撰寫，轉載請註明出處。
本篇講義尚未完成。

![](https://hackmd.io/_uploads/Sy7FTNHea.png)

# 入門介紹
- [Google Coding Style](https://google.github.io/styleguide/pyguide.html)
- [甚麼是演算法？](https://jason-chen-1992.weebly.com/home/-whats-algorithm)
- [甚麼是資料結構？](https://hackmd.io/@Aquamay/H1nxBOLcO/https%3A%2F%2Fhackmd.io%2F%40Aquamay%2Frk1C8ni5d)

來複習一下學習地圖，以臺大資工系必修為例：
![](https://i.imgur.com/Y2AdRO3.png =80%x)
以臺大資管系必修為例：
![](https://i.imgur.com/aC9lfrs.png =70%x)

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
- [2024/10 APCS](https://zerojudge.tw/Problems?tag=2024%E5%B9%B410%E6%9C%88) and [Solution](https://hackmd.io/@bangyewu/rJ5yJqEe1x)
- [2024/06 APCS](https://zerojudge.tw/Problems?tag=2024%E5%B9%B46%E6%9C%88) and [Solution](https://hackmd.io/cn9ndy19RbKHOJKBRx4aEA)
- [2024/01 APCS](https://zerojudge.tw/Problems?tag=2024%E5%B9%B41%E6%9C%88) and [Solution](https://hackmd.io/@bangyewu/SkKxG8Oua)
- [2023/10 APCS](https://zerojudge.tw/Problems?tag=2023%E5%B9%B410%E6%9C%88) and [Solution](https://hackmd.io/@bangyewu/SkxXo4QGa) or [Solution 2](https://dada878.com/blogs/apcs-2023-10-solution)
- [2023/06 APCS](https://zerojudge.tw/Problems?tag=2023%E5%B9%B46%E6%9C%88) and [Solution](https://hackmd.io/@bangyewu/B13lefwMp)

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


## 樹（Tree）
![](https://hackmd.io/_uploads/S13npBFMp.png)
基本單位為 Node，且只有一個 Node 是 Root（無人指向的 Node），且不存在任何 Cycle。每個 Node 可以指向多個 Child。
- [Tree(樹): Intro(簡介)](https://alrightchiu.github.io/SecondRound/treeshu-introjian-jie.html)

### 二元樹（Binary Tree）
![image](https://hackmd.io/_uploads/SJQuAds7a.png)
當樹中的每個 Node 都只有兩個 Child，即為 Binary Tree。

- [Binary Tree: Intro(簡介)](https://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html)
- [Binary Tree: Traversal(尋訪)](https://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html)
    以上面的 Binary Tree 為例：
    - Pre-Order Traversal: ABDECFG
    - In-Order Traversal: DBEAFCG
    - Post-Order Traversal: DEBFGCA
    ![image](https://hackmd.io/_uploads/rJEw81ajp.png)
> 延伸閱讀：[Binary Tree: 建立一棵Binary Tree](https://alrightchiu.github.io/SecondRound/binary-tree-jian-li-yi-ke-binary-tree.html)


### 二元搜尋樹（Binary Search Tree）
![image](https://hackmd.io/_uploads/rJ5d1tom6.png)
若一個二元樹中，所有 Node 都滿足 Node.left.value < Node.value < Node.right.value，就稱為二元搜尋樹。二元搜尋樹有良好的排序特質，可以幫助我們找到想要的資料。
- [Binary Search Tree: Intro(簡介)](https://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html)
- [Binary Search Tree: Search(搜尋資料)、Insert(新增資料)](https://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html)
- [Binary Search Tree: Sort(排序)、Delete(刪除資料)](https://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html)
> 注意：在 Binary Search Tree 上做 In-Order Traversal，即可得到排序好的資料！

### 進階 - 紅黑樹（Red Black Tree）
紅黑樹是一種進階的 BST（Binary Search Tree），透過將每個節點塗上紅色或黑色，並在新增或刪除資料時進行適當的結構調整（旋轉子樹），可以維持 BST 的高度不會相差太多，進而在搜尋時能有較好的效率。細節太過複雜這邊暫時跳過，之後有時間 or 有興趣再回來講。

![image](https://hackmd.io/_uploads/HyclMKj7p.png)
- [Red Black Tree: Intro(簡介)](https://alrightchiu.github.io/SecondRound/red-black-tree-introjian-jie.html)
> 延伸閱讀：
> - [Red Black Tree: Rotation(旋轉)](https://alrightchiu.github.io/SecondRound/red-black-tree-rotationxuan-zhuan.html)
> - [Red Black Tree: Insert(新增資料)與Fixup(修正)](https://alrightchiu.github.io/SecondRound/red-black-tree-insertxin-zeng-zi-liao-yu-fixupxiu-zheng.html)
> - [Red Black Tree: Delete(刪除資料)與Fixup(修正)](https://alrightchiu.github.io/SecondRound/red-black-tree-deleteshan-chu-zi-liao-yu-fixupxiu-zheng.html)

### 進階 - AVL 樹（AVL Tree）
![image](https://hackmd.io/_uploads/r1GAdTXt6.png)
AVL Tree 是一種 Binary search tree 實做方式，大部分的實做方式與 BST 一樣，差異在於 AVL tree 在過程中會透過計算並調整樹的結構來讓樹維持平衡，而不會導致 BST 過度傾斜(不平衡），與紅黑樹的目標類似。細節太過複雜這邊暫時跳過，之後有時間 or 有興趣再回來講。

> 延伸閱讀：[資料結構與演算法：AVL Tree](https://josephjsf2.github.io/data/structure/and/algorithm/2019/06/22/avl-tree.html)

### Leetcode
#### Basic - Traversal & Search
Please try to use both recursion and stack/queue to solve problem 102 and 144. (Hint: For 102(Level-Order) you should use **Queue**, for 144(Pre-Order) you should use **Stack**)
- [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)
- [102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)
- [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)
- [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)
- [700. Search in A Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/description/)

#### Applications
- [100. Same Tree](https://leetcode.com/problems/same-tree/description/)
- [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)
- [530. Minimum Absolute Difference in BST](https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/)
- [1026. Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/)
- [1609. Even Odd Tree](https://leetcode.com/problems/even-odd-tree/description)

#### Tools
- [BT Visualizer](https://eniac00.github.io/btv/)

## 圖（Graph）
![](https://hackmd.io/_uploads/S1v-AHFM6.png)
圖比樹的限制更少，給定一群節點與相連的邊，即可稱為圖。邊可以分為有向與無向，節點之間的連結並沒有限制，也因此圖並不像樹有 root、parent、siblings、height 等等屬性，且有可能會有 cycle 的出現。

### Graph & Tree 的比較
![](https://hackmd.io/_uploads/HkvhyNtf6.png)
Tree 可以被看成一種特殊的 Graph，就像 Binary Tree 是一種特殊的 Tree 一樣。

### Graph 的表示法
![image](https://hackmd.io/_uploads/H1otPi8gA.png)

- [Graph: Intro(簡介)](https://alrightchiu.github.io/SecondRound/graph-introjian-jie.html)

### Graph 的搜尋
![image](https://hackmd.io/_uploads/r1Ef-7Pnp.png)
最常見、也最常使用的搜尋方法有兩種：BFS 與 DFS。兩者的差異在於搜尋的優先順序不同，並且分別可以使用 Queue 與 Stack 來實作。

#### 廣度優先搜尋（Breadth First Search, BFS）
- [Breadth First Search or BFS for a Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

#### 深度優先搜尋（Depth First Search, DFS）
- [Depth First Search or DFS for a Graph](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)

#### 那 DFS 與 BFS 可以應用在 Tree 上嗎？
因為 Tree 也是 Graph 的一種，所以當然可以，而且非常常用！
> 延伸閱讀：[DFS、BFS 與 Pre-Order、In-Order、Post-Order、Level-Order 的關係](https://stackoverflow.com/a/57598470/15894431)

### Leetcode
- [133. Clone Graph](https://leetcode.com/problems/clone-graph/description/)
- [797. All Paths From Source to Target](https://leetcode.com/problems/all-paths-from-source-to-target/description/)
- [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)
- [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/description/)

---

#### 在圖中找環（Cycle）
上面的兩個例子中，都使用 `visited` 來紀錄該節點是否被拜訪過。因此，在**無向圖**中，若我們下一個要拜訪的節點的 `visited` 為 `True`，那我們就可以知道該圖中有環的存在。那在**有向圖**中呢？以下圖來說：
![image](https://hackmd.io/_uploads/rkSj6pq0a.png)
若我們在右邊的有向圖 b 中，用相同的 DFS 來尋找是否有環，假設第一次尋訪的路徑為 (1,2,4,5)，而第二次尋訪退回到 2 並往下尋訪 (3,4)，我們這時候會發現 `visited[4] == True`，並且判定該圖有環，但實際上是沒有的。那我們該怎麼做呢？

在往下看之前，先自己想想看喔！

---

答案：使用三個不同的值來表示每個節點不同的尋訪狀態（黑、白、灰）。黑色代表已經完成搜尋，白色代表還沒搜尋過，灰色代表正在這條 path 上搜尋，等搜尋完成後就會改為黑色。因此，若我們搜尋時遇到灰色節點，就可以知道該圖存在 cycle！
```python=
# Determine if a directed graph is acyclic
# True: Acyclic; False: Cyclic
graph = ... # adjacency list representation
N = len(graph)
visited = [0] * N
def checkNoCycle(node):
    if visited[node] == -1: # gray, currently visiting
        return False
    elif visited[node] == 1: # black, done visiting
        return True
    else: # white, not visited yet (visited[node] == 0)
        visited[node] = -1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        visited[node] = 1
        # print(node)
        return True
```

> 補充：[The purpose of grey node in graph depth-first search](https://cs.stackexchange.com/questions/9676/the-purpose-of-grey-node-in-graph-depth-first-search)

### 連通分量（Connected Components）
![image](https://hackmd.io/_uploads/r1EGVkc-A.png)
![ConnectedComponent4](https://hackmd.io/_uploads/BkStEJ9WR.png)


- [Connected Component - 演算法筆記](https://web.ntnu.edu.tw/~algo/ConnectedComponent.html)
- [Strongly Connected Components - Kosaraju 演算法](https://www.cnblogs.com/RioTian/p/14026585.html)

> 補充：[Connected Components in an Undirected Graph](https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/)
> 補充：[Strongly Connected Components](https://www.geeksforgeeks.org/strongly-connected-components/)
> 補充：[Tarjan 演算法與 Kosaraju 演算法](https://hackmd.io/@erichung0906/HkjZBH_IK)

### Leetcode
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)
- [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)


> 延伸閱讀：
> - [Graph: Breadth-First Search(BFS，廣度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)
> - [Graph: Depth-First Search(DFS，深度優先搜尋)](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)
> - [Graph: 利用DFS和BFS尋找Connected Component](https://alrightchiu.github.io/SecondRound/graph-li-yong-dfshe-bfsxun-zhao-connected-component.html)
> - [Graph: 利用DFS尋找Strongly Connected Component(SCC)](https://alrightchiu.github.io/SecondRound/graph-li-yong-dfsxun-zhao-strongly-connected-componentscc.html)
> - [Graph: 利用DFS尋找DAG的Topological Sort(拓撲排序)](https://alrightchiu.github.io/SecondRound/graph-li-yong-dfsxun-zhao-dagde-topological-sorttuo-pu-pai-xu.html)

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

## 雜湊表（Hash Table）
![](https://hackmd.io/_uploads/r1cQCHKMa.png)

### 雜湊函數的性質
雜湊函式是一種把輸入數據轉換成固定長度的字符串（雜湊值）的工具。它有以下特點：
* 固定長度輸出：無論輸入數據有多長，輸出都是固定長度。
* 無法回推：從雜湊值無法反推出原始輸入（即單向性），保證了數據的不可逆性。
* 抗碰撞性：難以找到兩個不同的輸入有相同的雜湊值。
* 快速計算：能快速生成雜湊值。

![image](https://hackmd.io/_uploads/ByQ3G5S7R.png)
![image](https://hackmd.io/_uploads/S1vaz9S7A.png)
![image](https://hackmd.io/_uploads/ByaTfqrXA.png)

- [[資料結構] 雜湊 (Hash)](https://ithelp.ithome.com.tw/articles/10208884)

> Images are from [什麼是Hash Function? 有什麼特性及用途?](https://homuchen.com/posts/what-is-hash-function-its-properties-and-usages/) 

### 雜湊函數的應用
* 資料完整性驗證：確保收到的資料是完整的，或確保文件未被篡改。
* 密碼儲存：儲存密碼的雜湊值，而不是明文密碼，提高安全性。常見的加密方式如 MD5、SHA-256 等等，若有興趣可以再研究密碼學。
* 資料結構：用於實現雜湊表，能夠快速存取資料。使用雜湊函數的常見資料結構包含集合（Set）、字典（Dictionary）等等。
* 數位簽章：保護資料完整性和驗證身份。

> 補充：[雜湊函數 - 維基百科](https://zh.wikipedia.org/zh-tw/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B8)

### Leetcode
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/description/)
- [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)
- [2441. Largest Positive Integer That Exists With Its Negative](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/)
<!-- - [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/) -->

## 字典樹（Prefix Tree / Trie）
![image](https://hackmd.io/_uploads/BJdBwzXIR.png)
以 N-ary Tree 的方式來表示一個字典，好處是當彼此有共同前綴（Common Prefix）時可以增加儲存與查找效率，常用於搜尋時的自動補字。

- [Trie（字典樹）](https://hackmd.io/@TienYi/trie)

實作上的話就跟正常的 N-ary Tree 差不多，可以使用 Dictionary 這種 key-value 的 Pair 來協助，同時要記得加註每個字結束的位置。以下為搭配`collections.defaultdict` 的 Trie 實作：

```python=
class Trie:
    def __init__(self):
        nested_ddict = lambda: defaultdict(nested_ddict)
        self.tree = nested_ddict()

    def insert(self, word: str) -> None:
        curr_tree = self.tree
        for c in word:
            curr_tree = curr_tree[c]
        curr_tree['END'] = ''

    def _search_tool(self, dest: str) -> tuple[bool, defaultdict]:
        curr_tree = self.tree
        for c in dest:
            if c not in curr_tree:
                return False, defaultdict()
            curr_tree = curr_tree[c]
        return True, curr_tree

    def search(self, word: str) -> bool:
        status, curr_tree = self._search_tool(word)
        if not status:
            return False
        return True if 'END' in curr_tree else False

    def startsWith(self, prefix: str) -> bool:
        status, curr_tree = self._search_tool(prefix)
        return status
```





### Leetcode
<!-- - [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/) -->
- [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/description/)
<!-- - [676. Implement Magic Dictionary](https://leetcode.com/problems/implement-magic-dictionary/description/) -->

## 並查集（Disjoint Set / Union Find）
![image](https://hackmd.io/_uploads/ry305yeWA.png)
由多個彼此沒有交集的 Set 組成，常用在需要分組與合併的情境中。

- [Union-Find / Disjoint-Set – 陪你刷題](https://haogroot.com/2021/01/29/union_find-leetcode/)

一個包含路徑壓縮，並以 rank (size of set) 來作為 union 依據的 Union-Find 資料結構，大概會是如下的形式：

```python=
class UF:
    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1] * N
        self.count = N

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.count -= 1
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
```

### Leetcode
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/description/)
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)
- [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)

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

- [演算法筆記：DP](https://web.ntnu.edu.tw/~algo/DynamicProgramming.html)

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

## 圖的進階議題（Advanced Topic on Graph）
### 最短路徑（Shortest Path）

最短路徑問題（Shortest Path Problem）是圖論中的一個重要課題，目的是尋找從一個起始節點到其他節點的最短路徑。相關的應用像是地圖中的導航系統、網路路由選擇等等，背後都是使用最短路徑的演算法。

- [path - 演算法筆記](https://web.ntnu.edu.tw/~algo/Path.html)


#### 戴克斯特拉演算法（Dijkstra's Algorithm）
![image](https://hackmd.io/_uploads/HyE20njxJx.png)

戴克斯特拉演算法是一種廣泛使用的方法，特別適用於權重非負的有向圖和無向圖，通過不斷選擇**當前距離最小的未訪問節點**，並更新其所有相鄰節點的最短距離，來尋找從起始節點到其他所有節點的最短路徑。

特別要注意的是，若存在負權重的邊，則戴克斯特拉演算法就不再適用。為什麼？讓我們看看以下的圖：
![image](https://hackmd.io/_uploads/BkrsVKGb1e.png)
你想到原因了嗎？在這張圖中，使用戴克斯特拉演算法會發生什麼事情？

- [基礎演算法系列 — Graph 資料結構與 Dijkstra’s Algorithm](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E5%9F%BA%E7%A4%8E%E6%BC%94%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97-graph-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E8%88%87dijkstras-algorithm-6134f62c1fc2)
- [Visualization of Above Example](https://graphicmaths.com/computer-science/graph-theory/dijkstras-algorithm/)

#### Bellman–Ford Algorithm
相較於戴克斯特拉演算法，Bellman–Ford Algorithm 可以用在含有負權重邊的情況，是一種能處理負權重邊的最短路徑演算法。

Bellman–Ford 的核心步驟是反覆對所有邊做 Relaxation（檢查是否可以利用某條邊縮短當前已知的最短路徑距離，若可以則更新），經過 V−1 次 Relaxation 的操作後（V 為節點數），可以找到從起點到其他所有節點的最短路徑。

雖然可以處理包含負權重邊的圖，但圖中不能存在負權重環（總和為負的環）。為什麼？
> 若圖中存在負權重環，我們可以一直在這個環中不斷遍歷，就會造成最短路徑變為負無限大。
> 反過來說，若在 V−1 次放鬆後，還有可以縮短的路徑，則代表該圖中存在負權重環，因此最短路徑不存在。
> 因此，Bellman–Ford 不僅適用於包含負權重邊的圖，還可以檢測負權重環。

- [[演算法] 最短路徑 (Bellman-Ford 演算法)](https://ithelp.ithome.com.tw/articles/10209748)

#### Floyd-Warshall Algorithm
Floyd-Warshall 演算法用於解決所有點對最短路徑問題（All-Pairs Shortest Paths Problem），是一種基於動態規劃的方法。與 Dijkstra 和 Bellman-Ford 不同的是，Floyd-Warshall 可以計算算任意兩個節點之間的最短路徑。

其主要的想法是：假設我們要從節點 i 到節點 j 找最短路徑，若能經由中間節點 k 獲得更短的距離，那麼我們就更新該最短路徑。用遞迴公式表示如下：$d[i][j] = min(d[i][j], d[i][k] + d[k][j])$。因此我們總共需要做 V 次更新，每次都檢查各點對之間的距離是否有更佳解。

- [[演算法] 最短路徑 (Floyd-Warshall 演算法)](https://ithelp.ithome.com.tw/articles/10209186)


#### Leetcode
- [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/description/)
- [1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance](https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/)
<!-- - [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/) -->
---

### 生成樹（Spanning Tree）
- [演算法筆記：Spanning Tree](https://web.ntnu.edu.tw/~algo/SpanningTree.html)

從一張圖取出一棵樹，樹上可以連接圖上所有點，就稱為該圖的生成樹，一個圖可能有不只一種生成樹。

![image](https://hackmd.io/_uploads/S1zbFo8eC.png)


#### 最小生成樹（Minimum Cost Spanning Tree）
顧名思義，最小生成樹就是最小的生成樹，這邊的最小指的是「連接所有節點所需的花費（所有邊的花費總和）最小」。

以下為兩個常見且易懂的貪婪演算法，來尋找圖中的最小生成樹：

##### Kruskal's algorithm
不斷從所有邊裡面選花費最小的邊，並判斷加入此邊可否連通兩個不同的 Component，直到所有的節點都被相連。（以所有邊作為每輪檢查的對象）

##### Prim's Algorithm
選定一個起點，挑選與其連接的邊中，花費最小且可連接兩個不同 Component 的相連，再把新連接的所有邊加入下一輪的檢查。其精神與 Dijkstra's Algorithm 有幾分類似。（以目前相連的點包含的所有邊，作為每輪檢查的對象）

> 備註：也有所謂的最大生成樹，概念一模一樣

#### Leetcode
- [1584. Min Cost to Connect All Points](https://leetcode.com/problems/min-cost-to-connect-all-points/description)

---

### 有向無環圖（Directed Acyclic Graph）與拓樸排序（Topological Sorting）

- [演算法筆記：DAG](https://web.ntnu.edu.tw/~algo/DirectedAcyclicGraph.html)

有向無環圖（Directed Acyclic Graph）又稱 DAG，顧名思義，是有方向且不包含環的 Graph。

拓樸排序（Topological Sorting）是一種將 DAG 中的所有節點排序的方式，使得每條有向邊的排序符合其方向性（舉例來說：u->v->w 的拓樸排序為 [u, v, w]）。


![image](https://hackmd.io/_uploads/B1txFj8gR.png)


以下介紹一個在有向無環圖中尋找拓樸排序的方法：

#### Kahn's Algorithm
透過找出圖中的 in-degree 為零的節點，逐步移除這些節點，並同時更新圖的 in-degree，從而達到拓樸排序。
- 若所有節點皆能被移除，則移除順序即為拓樸排序
- 若無法移除所有節點，則代表圖中有環（因此此圖不會是 DAG）



#### Leetcode
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)



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


假設數列 [6, 1, 5, 7]，求每個數的「下一個更大值」。
* 初始化：
    * stack = [] # index of element
    * result = [-1, -1, -1, -1] # next greater element
* 遍歷：
    * 2: stack = [0]
    * 1: stack = [0, 1]
    * 5: 
        * 5 > stack[1], pop 1 from stack, result[1] = 5
        * stack = [0, 2]
    * 7:
        * 7 > stack[2], pop 2 from stack, result[2] = 7
        * 7 > stack[0], pop 0 from stack, result[0] = 7
        * stack = [3]
* 結果：[7, 5, 7, -1]

- [參考：Monotonic Stack – 陪你刷題](https://haogroot.com/2020/09/01/monotonic-stack-leetcode/)

#### Leetcode
- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/description/)


### 單調佇列（Monotonic Queue）
與單調堆疊類似，但單調佇列不是嚴格意義上的佇列。單調佇列允許從兩端移除元素，與一般佇列的只能進先出不同，這麼做的好處是方便我們處理特定的問題。

#### 單調佇列的應用
![image](https://hackmd.io/_uploads/Syq69Jsrkg.png)
單調隊列的主要用途是處理「滑動窗口」問題。滑動窗口是指在數列中一段固定範圍內進行計算，像找最大值或最小值。


假設數列 [3, 1, -3, -1, 0]，求各個滑動窗口（k = 3）的最大值。
* 初始化：
    * queue = [] # index of element
    * result = [] # sliding window maximum
* 遍歷：
    * [3, 1, -3]: queue = [0, 1, 2], result = [3]
    * [1, -3, -1]: queue = [1, 3], result = [3, 1]
    * [-3, -1, 0]: queue = [3, 4], result = [3, 1, 0]
* 結果：[3, 1, 0]

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
 

## 背包問題（Knapsack Problem）
![image](https://hackmd.io/_uploads/SJHGJ6jgyx.png)

## 旅行銷售員問題（TSP, Traveling Salesman Problem）
![image](https://hackmd.io/_uploads/Sk8U16sekl.png) 


<!-- # Progress check
## 講義
- TODO: 尋找更多主題
- TODO: Update to blog

## 學生
- 進階演算法：Floyd-Warshall 實作
-->