---
title: Python 教學系列文 (1) - Overview、環境建置、基礎語法
categories:
  - Python 教學
tags:
  - Python
  - Tutorial
cover: /img/cover/python_clear.jpg
date: 2023-03-23 20:54:27
---

哈囉！這次來發一些關於 Python 的教學文章，會有這個系列文，主要是因為前陣子接了一個家教，就順便把辛苦整理的自編講義一起放上來了，內容雖然不深，但也涵蓋了初學 Python 所會碰到的各主題，若完全對 Python 不了解的話，這個系列文應該可以給你一些概念，完成後若想再自我進修也能大概有個方向。

此系列文預計會分十篇左右，內容涵蓋基礎語法、迴圈、函數、套件、類別等等主題，皆有範例程式碼可以參考，基本內容都會涵蓋到，不過因為我原本是做講義用，文字部分不會太詳盡。另外，雖然公開在網路上，但希望各位轉載還是標註一下來源，畢竟也是我辛辛苦苦整理的心血呢。~最後，有興趣的話，我還有在接學生（偷打廣告 XD）。~

[HackMD 完整版請點我](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw?view)

## Overview
程式語言分為高階語言、組合語言、機器語言等等，Python屬於高階語言的一種。機器語言與組合語言直接控制電腦硬體，但難以閱讀與開發；高階語言易於閱讀與開發，但需要「翻譯」給電腦聽。

> 來自 Python 官方網站的介紹：
> Python 是一種易學、功能強大的程式語言。它有高效能的高階資料結構，也有簡單但有效的方法去實現物件導向程式設計。Python 優雅的語法和動態型別，結合其直譯特性，使它成為眾多領域和大多數平臺上，撰寫腳本和快速開發應用程式的理想語言。

常見應用：網站開發、資料分析、機器學習、遊戲開發、網路爬蟲...
其他語言：C、C++、R、Java、JavaScript、SQL、Go、Ruby......


### 學習地圖
以臺大資工系必修為例：
![](https://i.imgur.com/Y2AdRO3.png)
以臺大資管系必修為例：
![](https://i.imgur.com/aC9lfrs.png)


## Python 入門
### 環境建置
 - 互動模式
     - Open Terminal（終端機） and input 'python'
     - Execute each line directly
     - If Python is not installed, go to [Python official website](https://www.python.org/downloads/)

```
>>> 1 + 2
3
```

 - 腳本模式
     - Need interpreter（直譯器） to help 'translate'
     - Execute the whole file or block at once
     - VSCode 示範 - .py 檔 與 .ipynb 檔

```python=
for i in range(3):
    print(i)
print("The loop ends.")
```
```
Output：
0
1
2
The loop ends.
```

 - [VSCode 安裝教學](https://www.citerp.com.tw/citwp2/2021/12/22/vs-code_python_01/)

> 補充：[使用 Anaconda 來建置開發環境](https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-c23859d2bde4)

### 基礎語法（Basic Syntax）
 - Our first program: `print("Hello World!")`
     - `print()` 是一個函數 （function）
     - "Hello World!" 是給予這個函數的輸入
     - 此函數會幫助我們印出給定的輸入，給使用者看

#### 計算（Computation）
```
>>> # This is a comment（註解）
>>> # A comment will not be executed by python
>>> 1 + 2
3
>>> 3 - 1
2
>>> 5 * 2
10
>>> 5 ** 2      # 5 的 2 次方
25
>>> 8 / 5       # 8 除以 5（回傳小數）
1.6
>>> 8 // 5      # 8 除以 5 的商
1
>>> 8 % 5       # 8 除以 5 的餘數（取 mod）
3
>>> (50 - 5 * 6) / 4
5.0
```


#### 變數（Variable）
- 我們會需要變數來存放數值運算的結果
- [基本命名規則](https://ithelp.ithome.com.tw/articles/10217188)
- `a = 10` 意為指派 10 給 a（右邊的值丟給左邊的容器）
- `a == 10` 意為比較 a 是否等於 10（為邏輯判斷式）

```
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```
- 讀取變數

```
>>> var = input()
3   # 使用者自行輸入
>>> print(var)
3   # 電腦將 var 的值印出
```

 > 進階：[Python 下劃線的意義](https://zhuanlan.zhihu.com/p/36173202)

#### 資料類別（Data Type）
 - 在宣告變數時，Python 自動幫我們決定資料類別
 - 其他語言（如 C++） 可能需要做類別宣告：`int a = 1`
 - 常見的基礎資料類別如下：
     - 整數 integer - `3`
     - 小數（浮點數） float - `3.0`
     - 字母 character - `'a'`
     - 字串 string - `"This is a string"`
     - 布林值 Boolean - `True` (Non-zero) / `False` (Zero)
    
 > 補充：String 是由 Character 組成的陣列，為了便於操作在 Python 內多使用 String
 > Python 在讀入長度為一的字母時，為了方便也會以 String 的方式儲存
#### 型別轉換（Casting）
```
>>> str(3)
'3'
>>> int("3")
3
>>> float(3)
3.0
>>> float("string")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'string'
>>> type(3)  # 檢查資料類別
<class 'int'>
```
#### 指派 & 自我指派 （Assignment & Self-assignment）
```python=
a = 10
print(a)
a = a + 2    # 把 a + 2 指派給 a
print(a)
a += 2       # a 自己等於自己 + 2
print(a)
```
```
Output:
10
12
14
```
> 相同的還有 `-=` `/=` `*=` `//=` `**=` `%=` ...

#### 比較/邏輯運算元（Comparison & Logical Operators）
 - < / <=：小於 / 小於等於
 - \> / >=：大於 / 大於等於
 - == / !=：等於 / 不等於
 - `and`：且
 - `or`：或
 - `not`：非