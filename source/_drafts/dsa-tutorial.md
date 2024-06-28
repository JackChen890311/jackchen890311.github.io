---
title: 資料結構與演算法
categories:
  - 
tags:
  - 
cover: /img/cover/C++.png
date: 
---

# 演算法與資料結構入門
本文所有內容與資料皆由本人蒐集與撰寫，轉載請註明出處。
本篇講義尚未完成。

![](https://hackmd.io/_uploads/Sy7FTNHea.png)

# 入門介紹
- [甚麼是演算法？](https://jason-chen-1992.weebly.com/home/-whats-algorithm)
- [甚麼是資料結構？](https://hackmd.io/@Aquamay/H1nxBOLcO/https%3A%2F%2Fhackmd.io%2F%40Aquamay%2Frk1C8ni5d)

來複習一下學習地圖，以臺大資工系必修為例：
![](https://i.imgur.com/Y2AdRO3.png =80%x)
以臺大資管系必修為例：
![](https://i.imgur.com/aC9lfrs.png =70%x)

而在演算法與資料結構的世界裡面，大概又可以分為以下幾種類別。在我們之後的課程中，會逐漸的介紹每個名詞以及其對應概念：
![image](https://hackmd.io/_uploads/BkmCHf7UR.png)



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
- [How to master DSA](https://blog.algomaster.io/p/how-i-mastered-data-structures-and-algorithms)

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
 

# 資料結構（Data Structure）
資料結構是一種設計、組織、儲存資料的方式，以實現最佳性能和效率。這些結構包含不同形式，像是陣列、鍊結列表、樹、圖等等。選擇適當的資料結構對於解決特定的問題至關重要，不同的資料結構可以用於不同的應用，並且可以極大地影響程序的運行時間和記憶體使用。

相關參考：
- [C++ STL 容器（一） - 基本介紹](https://jasonblog.github.io/note/c++/stl_rong_qi_4e0029_-_ji_ben_jie_shao.html)
- [C++ API / STL 整理](https://hackmd.io/@meyr543/BkgMaiV6Y)
- [演算法與資料結構](https://alrightchiu.github.io/SecondRound/mu-lu-yan-suan-fa-yu-zi-liao-jie-gou.html)

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

### 堆積排序法(Heap Sort)
- [[演算法(Algorithm)] 堆積排序法(Heap Sort)](https://notepad.yehyeh.net/Content/Algorithm/Sort/Heap/Heap.php)

對陣列做 Heapify 變成 Max Heap，再不斷把最大值往後擺。
> 練習：試著實作 Heap Sort 吧！

## 優先佇列（Priority Queue）
![image](https://hackmd.io/_uploads/S1CWOylZ0.png)

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
k = 3
H = [9,7,5,3,1]
heapq.heapify(H)
heapq.heappush(H,2)
element = heapq.heappop(H)
element = heapq.heappushpop(H,2)
klargest = heapq.nlargest(k, H)
ksmallest = heapq.nsmallest(k, H)
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
- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/description/)
- [387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/description/)
- [2441. Largest Positive Integer That Exists With Its Negative](https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/)

## 並查集（Disjoint Set / Union Find）
![image](https://hackmd.io/_uploads/ry305yeWA.png)
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
- [547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/description/)
- [1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/description/)

## 字典樹（Prefix Tree / Trie）
![image](https://hackmd.io/_uploads/BJdBwzXIR.png)
- [Trie（字典樹）](https://hackmd.io/@TienYi/trie)
### Leetcode

# 其他常見的演算法（Algorithms）
演算法（Algorithm）是在有限的步驟之內，提供明確的法則，求出問題正確答案的程序。它可以是一種方法、法則或者程序，讓資料可按照預先設計的方式處理。

- [認識演算法](https://hackmd.io/@howkii-studio/Bkf-2DQiw/https%3A%2F%2Fhackmd.io%2F%40howkii-studio%2Falgorithm)
- 推薦補充閱讀：[演算法筆記](https://web.ntnu.edu.tw/~algo/)
    - [Algorithm Design](https://web.ntnu.edu.tw/~algo/AlgorithmDesign.html)

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
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
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
遞迴方法耗時: 0.502652 秒
動態規劃方法耗時: 0.000011 秒
```

為什麼會差這麼多呢？我們來分析看看兩種方法的時間複雜度：

- 遞迴版本
時間複雜度：$O(2^n)$。對於每個 fibonacci_recursive(n)，它會呼叫 fibonacci_recursive(n-1) 和 fibonacci_recursive(n-2)，這種重複計算會導致呼叫函數的次數呈指數級數增長，因此時間複雜度為 $O(2^n)$。


- 動態規劃版本
時間複雜度：$O(n)$。它只需要計算一次每個費氏數列的值，並將結果存入列表中。迴圈從 2 執行到 n，所以時間複雜度為 $O(n)$。


對於較小的 n，遞迴可能更簡單易懂，並且兩者的速度可能相差不大。但是當 n 較大時，遞迴所需的時間會嚴重惡化，相較之下動態規劃會有更好的效能表現。

看到上述兩者的時間複雜度差異之大，是不是發現動態規劃的強大了？



### Leetcode
- [62. Unique Paths](https://leetcode.com/problems/unique-paths/description/)
- [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/description/)
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)
- [198. House Robber](https://leetcode.com/problems/house-robber/description/)

<!-- ### 動態規劃經典問題：背包問題（Knapsack Problem） -->
> 延伸閱讀：[演算法筆記：Knapsack Problem](https://web.ntnu.edu.tw/~algo/KnapsackProblem.html)

## KMP 演算法
![image](https://hackmd.io/_uploads/ry2SjfO4C.png)

KMP演算法是一種用於字串搜尋的高效方法。透過建立部分配對表，可以快速定位搜尋字串中的可能配對位置，減少不必要的重複比較，從而加速搜尋過程。

- [KMP algorithm，從自學到放棄 (1)](https://medium.com/@c.s.fangyolk/kmp-%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E8%87%AA%E5%AD%B8%E5%88%B0%E6%94%BE%E6%A3%84-1-7f71e65839a0)
- [KMP algorithm，從自學到放棄 (2)](https://medium.com/@c.s.fangyolk/kmp-%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E8%87%AA%E5%AD%B8%E5%88%B0%E6%94%BE%E6%A3%84-2-94dda22f80b2)
### Leetcode
- [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/)
## Backtracking
## Divide-and-Conquer
### Leetcode
- [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)
## Brute Force
## Greedy Method

## Graph 進階議題
### 最短路徑（Shortest Path）
- [Shortest Path：Intro(簡介)](https://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html)
### 戴克斯特拉演算法（Dijkstra's Algorithm）
- [基礎演算法系列 — Graph 資料結構與Dijkstra’s Algorithm](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E5%9F%BA%E7%A4%8E%E6%BC%94%E7%AE%97%E6%B3%95%E7%B3%BB%E5%88%97-graph-%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E8%88%87dijkstras-algorithm-6134f62c1fc2)

### Leetcode
- [743. Network Delay Time](https://leetcode.com/problems/network-delay-time/description/)
- [787. Cheapest Flights Within K Stops](https://leetcode.com/problems/cheapest-flights-within-k-stops/description/)
---

### 生成樹（Spanning Tree）
![image](https://hackmd.io/_uploads/S1zbFo8eC.png)


- [演算法筆記：Spanning Tree](https://web.ntnu.edu.tw/~algo/SpanningTree.html)

---

### 有向無環圖（Directed Acyclic Graph）與拓樸排序（Topological Sorting）
![image](https://hackmd.io/_uploads/B1txFj8gR.png)


- [演算法筆記：DAG](https://web.ntnu.edu.tw/~algo/DirectedAcyclicGraph.html)

### Leetcode
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)

# 附錄：Complexity Cheat Sheet
![](https://hackmd.io/_uploads/BkfMZStGp.png)
![](https://hackmd.io/_uploads/BJ50lHYGp.png)