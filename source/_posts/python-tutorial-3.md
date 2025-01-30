---
title: Python 教學系列文 (3) - 條件判斷、迴圈、字串處理
categories:
  - Python 教學
tags:
  - Python
  - Tutorial
cover: /img/cover/python_clear.jpg
date: 2023-03-23 20:54:35
---

[HackMD 完整版請點我](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw?view)

## Python 基礎 (1)
### 條件判斷（Conditionals）
```python=
price = int(input())
if price < 100:
    print("It's cheap.")
elif price >= 100 and price < 200:
    print("It's okay.")
else:
    print("It's too expensive!")
```
 - 若...則... (`if`) ，否則若...則... (`elif`) ，若以上皆非則... (`else`)
 - `if` 跟 `else` 是一組的，後面要放條件判斷 or 布林值，`elif` 可有可無
 - 底下的指令則需縮排，讓 Python 知道哪些是條件成立需要執行的
 - 裡面還可以再包 `if-else` （巢狀條件判斷）

```python=
if ...
    if ...
        ...
    else
        ...
else ...
    if ...
        ...
    else
        ...
```
 - 另一種寫法：A `if` condition `else` B（若 condition 為真，則執行 A ，否則執行 B）
 - 重要：在 Python 中，縮排是很重要的，Python 會用縮排來判斷每行程式碼的所在層級，縮排不同，執行起來的結果有可能完全不同！




### 迴圈（Iterations）
 - 我們很常需要電腦幫我們做重複的工作
 - 迴圈就可以幫我們達到此目的
 - 迴圈基本上分為兩種語法： `while` 跟 `for`
 - `while` 可以想成不斷執行的 `if`，直到條件不再成立為止
     - 要小心「無窮迴圈」的發生
 - `for` 則是針對清單內的元素，每個都執行一次所有指令
     - 常搭配 range() 或是清單一起使用

```python=
i = 0
while i < 3:
    print(i)
    i += 1
print("The loop ends.")
```
```python=
for i in [0,1,2]:  # Or for i in range(3):
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

> 備註：`i` is called 'Loop Counter' in above examples
> For 迴圈會自動更新 Loop Counter，While 迴圈則不會

#### 無窮迴圈（Infinite Loop）
 - 當一個迴圈無法停止執行時，就稱為無窮迴圈
 - 無窮迴圈只能透過強制停止的方式來結束！（Ctrl + C）
 - 示範：

```python=
while 4 > 3:  # A always true condidtion 
    print('Loop')
```

#### Range()
上面的例子中有使用到 range()，而 range() 是能夠幫助我們創造一個範圍的函數，其用法為：
- `range(n)` 會回傳 `[0,1,2,...n-1]` 的清單
- `range(m,n)` 會回傳 `[m,m+1,m+2,...n-1]` 的清單
- `range(m,n,k)` 會回傳 `[m,m+k,m+2k,...]` 的清單，最後一個元素不超過 n-1

一般的情況下使用第一個就好。

> 備註：回傳型態其實不完全是清單，但我們先把它當成清單用就好
> 可以透過 `list()` 將其轉為清單

#### 巢狀迴圈（Nested Loop）
 - 迴圈裡也可以再放迴圈，很多複雜的程式都需要用到
 - 要注意各個迴圈的執行順序與邏輯，同時撰寫避免不必要的迴圈

```python=
for i in range(3):
    print(i)
    for j in range(2):
        print(">",j)
    print('=====')
```
```
Output:
0
> 0
> 1
=====
1
> 0
> 1
=====
2
> 0
> 1
=====
```


#### 迴圈特殊處理 - break & continue
 - `break`：跳出迴圈外，直接結束迴圈執行
 - `continue`：跳過後面的指令，直接結束此次迴圈，並進行下一次迴圈
 - 用以控制迴圈，給予迴圈多個「出口」
 - 若放在多重迴圈內，只會跳出一層迴圈
 - 要小心不要寫出沒有意義的 `break` & `continue`！

```python=
i = 0
while (i < 10):
    i += 1
    if i == 2:
        continue
    if i == 6:
        break
    print(i)
```
```
Output:
1
3
4
5
```

### 字串處理
 - 字串基本上可視為字母陣列 (Array)，基本操作如下：

```
>>> s = 'String'
>>> print(type(s))
<class 'str'>

>>> print(s[0])
'S'

>>> print(s[-1])
'g'

>>> print(len(s))
6

>>> print(s+s)
'StringString'

>>> print(s,s)
String String

>>> print(s+"&"+s)
String&String

>>> print(s*3)
StringStringString

>>> print(s.replace('Str','do'))
doing

>>> print(s.find('ing'))
3

>>> print(s.upper())
STRING

>>> print(s.lower())
string

>>> print('t' in s)
True
```