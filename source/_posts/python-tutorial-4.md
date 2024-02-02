---
title: Python 教學系列文 (4) - 清單、CSV 檔案
categories:
  - Python 教學
tags:
  - Python
  - Tutorial
cover: /img/cover/python_clear.jpg
date: 2023-03-23 20:54:38
---

[HackMD 完整版請點我](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw?view)

### 清單（List）
 - 清單是 Python 最常用、也最好用的資料類別，具順序性
 - 甚麼東西都可以裝，裝的東西也可以不同，也可以用清單包清單
 - 想成一個百寶袋，甚麼都可以塞，再拿出來
     - 32位python的儲存上限是536870912 個元素
     - 64位python的儲存上限是1152921504606846975 個元素
 - 前面提到的字母陣列其實概念跟清單很像

```
>>> l = [1, 1.0, 10, "test"]
>>> print(l[0])
1

>>> print(l[2])
10

>>> l[2] = 100
>>> print(l[2])
100

>>> print(l[-1])
"test"

>>> print(len(l))
4

>>> l.append("123")
>>> print(l)
[1, 1.0, 100, "test", "123"]

>>> l.pop()
"123"
>>> print(l)
[1, 1.0, 100, "test"]

>>> print(l + l)
[1, 1.0, 100, "test", 1, 1.0, 100, "test"]
```
 - Traverse a list：

```python=
l = [1,2,3,4,5]
for i in l:   # or for i in range(len(l))
    print(i * 2)
```
```
Output:
2
4
6
8
10
```
- 常見操作（Common Operations，供參考）：

| Method | Usage |
| -----  | ----- |
| list.append(x)  | Add element x to end of list. |
| list.sort()   | Sort (order) the list. A comparison function may be passed as a parameter. |
| list.reverse()  | Reverse the list. |
| list.index(x)   | Returns index of first occurrence of x. |
| list.insert(i, x)  | Insert x into list at index i. |
| list.count(x)   | Returns the number of occurrences of x in list. |
| list.remove(x)   | Deletes the first occurrence of x in list. |
| list.pop(i)  | Deletes the ith element of the list and returns its value. |

#### List Copying
- 在複製 List 時，要特別留意以下狀況，並非正確的 List 複製方法：
```python=
# Wrong Copy (Reference Copy Only)
aList = [1, 2, 3]
anotherList = aList
anotherList[0] = 5
print(aList)
# Check their address
print(id(aList), id(anotherList))
```
```
Output:
[5, 2, 3]
1805364504896 1805364504896
```
 - 當我們修改 `anotherList` 時，原本的 `aList` 也一同被修改
 - 主要是因為 List 儲存的是記憶體參照（或是說 List 是可變物件，後面會提到），第三行做的事情僅僅是將參照傳給另一個變數，因此也可以發現他們的記憶體其實是相同的

##### How to copy a list correctly?
有以下幾種方式可以正確地複製 List：

```python=
# Correct Copy
aList = [1, 2, 3]
# Three different ways to copy a list (Shallow)
anotherList = list(a)
anotherList = a[:]
anotherList = a.copy()

anotherList[0] = 5
print(aList)
# Check their address
print(id(aList), id(anotherList))
```
```
Output:
[1, 2, 3]
1805364505024 1805364643392
```

> 補充：此處使用的稱為「Shallow Copy」，僅複製容器中元素的地址
> 若連容器中的元素本身都想完全複製，需要使用「Deep Copy」
> 延伸閱讀： [Python - 淺複製(shallow copy)與深複製(deep copy)](https://ithelp.ithome.com.tw/articles/10221255)
    
    
### CSV（Comma-separated value）檔案
 - CSV 是常見的儲存資料格式
 - 簡潔、統一、格式化、方便處理

```
QuotaAmount,StartDate,OwnerName,Username
150000,2016-01-01,Chris Riley,trailhead9.ub20k5i9t8ou@example.com
150000,2016-02-01,Chris Riley,trailhead9.ub20k5i9t8ou@example.com
150000,2016-03-01,Chris Riley,trailhead9.ub20k5i9t8ou@example.com
150000,2016-01-01,Harold Campbell,trailhead14.jibpbwvuy67t@example.com
150000,2016-02-01,Harold Campbell,trailhead14.jibpbwvuy67t@example.com
150000,2016-03-01,Harold Campbell,trailhead14.jibpbwvuy67t@example.com
150000,2016-01-01,Jessica Nichols,trailhead19.d1fxj2goytkp@example.com
150000,2016-02-01,Jessica Nichols,trailhead19.d1fxj2goytkp@example.com
150000,2016-03-01,Jessica Nichols,trailhead19.d1fxj2goytkp@example.com
```

結合前面的字串與清單處理方式，我們可以輕鬆的處理 CSV file 中的每一行資料：
```
>>> line = 'amount,date,owner,user'
>>> data = line.split(',')
>>> print(data)
['amount', 'date', 'owner', 'user']
>>> print(data[0])
amount
```

那如何處理整個 CSV file？使用檔案處理相關函數（之後再講）：
```python=
result = []
with open('file.csv') as f:
    data = f.read()
    lines = data.split('\n')
for line in lines:
    result.append(line.split(','))
print(result)
```
```
Output:
[[QuotaAmount,StartDate,OwnerName,Username],
[150000,2016-01-01,Chris Riley,trailhead9.ub20k5i9t8ou@example.com],
[150000,2016-02-01,Chris Riley,trailhead9.ub20k5i9t8ou@example.com],
...]
```