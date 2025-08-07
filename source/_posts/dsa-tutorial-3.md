---
title: 資料結構與演算法教學系列文 (3) - 樹、圖
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:03
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


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

