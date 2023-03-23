---
title: Python 教學系列文 (7) - Lambda、套件、Git 簡介
categories:
  - Python 教學
tags:
  - Python
cover: /img/cover/python_clear.jpg
date: 2023-03-23 20:54:49
---


[HackMD 完整版請點我](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw?view)

### Lambda
Lambda 又叫做匿名函數，當我們需要快速簡潔的撰寫一個函數，但又不想幫他命名時（意即這個函數可能只會用一兩次），我們就會使用 Lambda 來幫助我們。Lambda 在使用上依然可以給予名稱，但非必要，函數內容也必須在一行內結束。

```python=
>>> print((lambda x : x ** 2)(10))
100
>>> print((lambda x, y: x * y)(4, 5))
20
>>> print((lambda x: x[1])([1,2,3]))
2
```

#### 與其他函數的搭配使用
 - filter()

```python=
numbers = [1,10,100,1000,10000]
bignums = filter((lambda x: x > 50), numbers)
print(list(bignums))
```
```
Output:
[100,1000,10000]
```

 - map()

```python=
numbers = [1,10,100,1000,10000]
doublenums = map((lambda x: x * 2), numbers)
print(list(doublenums))
```
```
Output:
[2, 20, 200, 2000, 20000]
```

 - sorted()

```python=
food = [('Apple',10),('Coke',30),('Bread',5),('Candy',25)]
food_sorted = sorted(food, key = lambda x: x[1])
print(food_sorted)
```
```
Output:
[('Bread', 5), ('Apple', 10), ('Candy', 25), ('Coke', 30)]
```

> 參考 [Python Lambda 應用技巧](https://www.learncodewithmike.com/2019/12/python-lambda-functions.html)

### 套件（Library）
Python 強大的地方就是其眾多的使用者，讓我們在網路上有許多參考資料，以及眾多的第三方套件可供我們使用。套件其實就是別人寫好的 .py 檔案，將其整理後丟到網路上，讓我們可以透過一行簡單的 `import [package]` 就能使用。
 - 安裝套件：使用 `pip install [package]`
    有些套件如 `os`, `random`, `time` 等等已預先包含在 python 中，就不需再另外下載
 - 載入套件
     - 整個套件載入
         - `import [package]`（推薦）
         - `from [package] import *`
     - 僅載入特定模組/函數
         - `from [package] import [module/function]`（推薦）
         - `import [package].[module]`
     - 載入且化名
         - `import [package] as [name]`
 - 使用套件：多以`[package].[function]`的方式，若是僅載入特定模組/函數的話，前面不須加套件名稱即可使用。以下四種方式結果皆相同，但為了方便管理我們一般會選用第一種，以便知道各個函數來自哪個套件，同時也不會不小心覆寫（Overwrite）某些函數。

```python=
import os
print(os.getcwd())
```
```python=
from os import getcwd
print(getcwd())
```
```python=
import os as O
print(O.getcwd())
```
```python=
from os import getcwd as gw
print(gw())
```

> 進階：參考 [Python 的 import 陷阱](https://medium.com/pyladies-taiwan/python-%E7%9A%84-import-%E9%99%B7%E9%98%B1-3538e74f57e3)

#### 常用套件
 - GUI：tkinter
 - 遊戲設計：pygame
 - 數學運算：math, random, numpy, scipy, random
 - 資料處理：numpy, pandas
 - 視覺化：matplotlib, seaborn
 - 機器學習：scikit-learn, pytorch, tensorflow, keras
 - 網站建置：flask, django
 - 資料庫處理：pymysql
 - 影像處理：cv2, PIL
 - 自然語言處理：nltk, jieba
 - 電腦操作：os, sys
 - 時間相關：time, datetime
 - 網路爬蟲：request, beautifulsoup, selenium
> 參考 [Python 第三方模組](https://cflin.com/course/python/Python_07.pdf)

## Git 版本控制
Git 是一種版本控制系統，它可以追蹤軟體開發過程中的變更，幫助開發人員更有效地管理程式碼。使用 Git 有許多好處：

1. 版本控制：Git 可以幫助開發人員追蹤檔案的更改，並在需要時輕鬆地回復到先前的版本。這樣可以減少錯誤和失誤，並提高程式碼品質。
2. 合作開發：Git 可以讓多個開發人員協同工作，讓他們在同一時間在同一份程式碼上工作，並且避免不同人員之間的衝突。
3. 分支管理：Git 可以讓開發人員在不影響主分支的情況下創建和管理多個分支。這可以讓開發人員在不同的功能上工作，而不必擔心對主分支的影響。
4. 遠端存儲：Git 可以讓開發人員將代碼儲存在遠端儲存庫中，讓多個開發人員在不同地方協同工作。

Git 在許多著名的開源軟體專案中得到廣泛使用，包括Linux核心、Ruby on Rails 和 jQuery。使用 Git 的方式一般有兩種：使用指令（Command Line）或是下載 Github Desktop 使用其軟體介面（GUI），我們這邊會先介紹如何使用 Github Desktop。

Credit: The world-wide famous [ChatGPT](https://chat.openai.com/chat)

參考以下連結：
- [官方說明](https://docs.github.com/zh/desktop/installing-and-configuring-github-desktop/overview/getting-started-with-github-desktop)
- [從 0 到 1 的 GitHub Pages 教學手冊](/cW7RxOjzQ4eqQlZbOW9BsA)
- [Git 教學 - 為你自己學 Git](https://gitbook.tw/)