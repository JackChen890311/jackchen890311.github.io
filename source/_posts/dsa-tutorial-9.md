---
title: 資料結構與演算法教學系列文 (9) - 圖的進階議題
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:09
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


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

拓樸排序（Topological Sorting）是一種將 DAG 中的所有節點排序的方式，使得每條有向邊的排序符合其方向性（舉例來說：u->v->w 的拓樸排序為 [u, v, w]）。因為 DAG 之中不會有環，故只要是 DAG 則必能找到一個拓樸排序。


![image](https://hackmd.io/_uploads/B1txFj8gR.png)


以下介紹一個在 DAG 中尋找拓樸排序的方法：

#### Kahn's Algorithm
透過找出圖中的 in-degree 為零的節點，逐步移除這些節點，並同時更新圖的 in-degree，從而達到拓樸排序。
- 若所有節點皆能被移除，則移除順序即為拓樸排序
- 若無法移除所有節點，則代表圖中有環（因此此圖不會是 DAG）


#### Leetcode
- [207. Course Schedule](https://leetcode.com/problems/course-schedule/description/)
- [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/description/)

