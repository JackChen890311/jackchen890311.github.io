---
title: 資料結構與演算法教學系列文 (5) - 雜湊表、字典樹、並查集
categories:
  - DSA 教學
tags:
  - Data Structure
  - Algorithm
  - Tutorial
cover: /img/cover/color_macbook.jpg
date: 2025-06-10 15:57:05
---

[HackMD 完整版請點我](https://hackmd.io/KM8DV4vRSzSnm9z3HZCC5Q)


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
