---
title: Python 教學系列文 (5) - 函數、其他常見資料結構
categories:
  - Python 教學
tags:
  - Python
cover: /img/cover/python_clear.jpg
date: 2023-03-23 20:54:42
---


[HackMD 完整版請點我](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw?view)


## Python 基礎 (2)
### 函數（Function）
我們以前寫 print('Hello') 時，其實就是在呼叫函數，這個函數會幫我們把我們傳入的 'Hello' 印出來。其他像是 range()、type()、input() 等也都是函數，各有不同的用途。

我們也可以透過特定語法來定義自己的函數，透過函數可以幫我們達成「模組化」，省去重複的 code 同時提供更多彈性來執行類似的動作。

- 一個函數包含名稱、函數本體、輸入（Input）與輸出（Output）
    - 後兩者又叫做參數（Parameters）、回傳值（Return Values）
    - 參數與引數（Arguments）雖然都指函數輸入值，但有些微的差異，可以參考[這裡](https://notfalse.net/6/arg-vs-param)
- 函數的使用：
    - 用名稱來使用（或呼叫）函數，用 `def` 來定義函數
    - 函數的參數可以自行命名（如下例的 n），也可以傳入多個參數或給定預設值
    - 把要執行的程式碼包在函數本體中
    - 使用 `return` 來控制函數的結束點，並將回傳值放在後面（可放多個用逗號隔開）
    - 若沒有 `return` 則函數跑完所有 code 一樣會結束並回傳 `None`
    - 函數結束後會回到主程式，繼續執行後面的程式
- 例子：

```python=
def get_1_to_n(n = 5):
    print('Getting a list range from 1 to',n, end=': ')
    print(list(range(1,n+1)))
    return list(range(1,n+1))

x = get_1_to_n(10)  # or get_1_to_n(n = 10)
print('X = ',x)
print('~~~~~~~~~~')
y = get_1_to_n()
print('Y = ',y)
```
```
Output:
Getting a list range from 1 to 10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
X =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
~~~~~~~~~~
Getting a list range from 1 to 5: [1, 2, 3, 4, 5]
Y =  [1, 2, 3, 4, 5]
```

#### 變數範圍（Scope of Variable）
變數依據生命週期的不同，分為全域（Global）變數與區域（Local）變數
- 區域變數
    - 定義在函數內的變數稱為區域變數
    - 只能在函數內使用，函數結束後變數也會跟著消失
- 全域變數
    - 定義在函數外的變數稱為全域變數
    - 所有地方（包含函數內）都可以使用，直到程式結束執行才會消失
- 若函數內宣告與全域變數同名的變數，則會被當作是區域變數，對其進行的操作不影響全域變數
- 如果想在函數內修改全域變數，可以使用 `global var` 來進行（但不推薦，容易混亂）
- 通常若我們需要拿到函數內的某個變數，我們會直接使用 `return var`

```python=
def multiply_5(n):
    scale = 5
    return n * scale

# print(scale) will cause error
scale = 3
result = multiply_5(2)
print(result)
print(scale)
```
```
Output:
10
3
```

#### 可變物件（Mutable Object）與不可變物件（Immutable Object）
在 Python 中，不同資料類別又可以其性質分為可變物件與不可變物件。 

| 分類 | 可變物件  | 不可變物件 |
| ---- | -------- | -------- |
| 說明 | 被創造出來後，其值可以被改變的物件。 | 被創造出來後，其值無法被改變的物件。 |
| 舉例 | list, dict, set* | int, float, string, tuple |
| 修改 | 可以，依資料類別不同有不同修改方式，修改時記憶體位置不會改變。 | 無法，只能透過重新指派的方式，此時記憶體位置亦會被重新分配。 |


```python=
# Mutable Object
alist = [1,2,3]
alist[1] = 100
print(alist)
```
```
Output:
[1,100,3]
```

```python=
# Immutable Object
astring = 'string'
astring[3] = 'A'
```
```
Output:
TypeError: 'str' object does not support item assignment
```


接著我們來看看記憶體位址的變化：

```python=
# Let's take a look on the addresses of these objects
# id() is a function help finding address of a variable
alist = [1,2,3]
print(id(alist))
alist[1] = 100
print(id(alist))
print('=====')
astring = 'string'
print(id(astring))
astring = 'STRING'
print(id(astring))
```
```
Output:
1541330859072
1541330859072
=====
1541255790064
1541259351920
```


> 參考 [什麼是 Immutable & Mutable objects](https://www.maxlist.xyz/2021/01/26/python-immutable-mutable-objects/)
> *關於 set 可不可變其實有點爭議，在這裡先當作他是可變的，參考[這裡](https://stackoverflow.com/questions/14193438/are-python-sets-mutable)

#### Pass by Assignment - Example Illustration
此處我們「不會」深入講當傳參數時發生了什麼事情，因為牽扯到一些記憶體跟參照等等的概念，我們會用幾個例子來說明何謂 Python 的 Pass by Assignment。

Python 中函數依據傳入參數的類別不同，會有不同的行為。**當傳入參數可變物件時，若未經重新指派，而是在函數裡直接修改參數，則會原始變數的值也會一同被修改（若經重新指派則視為全新的變數，即不影響原始變數）；而當傳入參數為不可變物件時，任何對參數的操作都不影響原始變數（除非使用全域變數方式修改）**。

聽起來很複雜對吧？我們直接用例子來看會比較清楚一些：

```python=
def listchange(l):
    l[0] = 'A'
alist = [1,2,3]
listchange(alist)
print(alist)
```
```
Output:
['A',2,3]
```

```python=
def strchange(s):
    s = 'STRING'
astring = 'string'
strchange(astring)
print(astring)
```
```
Output:
string
```

在以上的例子中，`alist` 為可變物件，因此做為參數傳入並在函數中修改時，原始的 `alist` 也一同被修改；而 `astring` 為不可變物件，因此做為參數傳入時，我們並無法直接修改他的值，只能透過重新指派的方式給予 `'STRING'` 這個值，而原始的 `astring` 依然存放 `string` 這個值沒有改變。

我們在撰寫函數時，比較好的方式是不要直接修改原始參數的值，而是將修改後的值存放在新的變數中，並作為回傳值傳回給呼叫函數的地方，以避免混淆的狀況。

> 參考 [關於 Python 獨有的 Pass by Assignment](https://luka.tw/Python/%E5%9F%BA%E7%A4%8E%E6%95%99%E5%AD%B8/past/2021-09-21-is-python-call-by-sharing-122a4bf5a956/)，以及 [英文版本（Stackoverflow）](https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)


#### 遞迴（Recursion） - An example on factorial
```python=
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
    return result
```

關於函數還有很多可以講：Recursion 的設計方法、Call by Reference、Call by Value...
但有些東西太進階了，我們先停在這裡，以後有機會再細講。
> 補充：[遞迴深度的上限](https://clay-atlas.com/blog/2020/09/20/python-cn-recursionerror-maximum-recursion-depth-exceeded/)


### 其他常見資料結構
#### 元組（Tuple）
 - 與 list 類似，但是屬不可變物件
 - 不同於 list 使用 `[]` ，tuple 使用 `()` 
 - 一個元素的 tuple 須以 `(item, )` 表示
 - 因屬不可變物件，故僅能以重新指派的方式修改其值，如下例：

```
>>> mytuple = (11, 22, 33)
>>> saved = mytuple
>>> mytuple += (44,)
>>> mytuple
(11, 22, 33, 44)
>>> saved
(11, 22, 33)
```
 - zip()

```python=
num = [1,2,3]
char = ['a','b','c']
CHAR = ['A','B','C']
for i in zip(num,char,CHAR):
    print(i)
```
```
Output:
(1, 'a', 'A')
(2, 'b', 'B')
(3, 'c', 'C')
```

#### 字典（Dictionary）
當我們需要了解某個字的讀音時，我們會去查找字典，在其中尋找對應的讀音。這種 {字: 讀音} 的配對，在 Python 中可以透過字典來實現。
 - 字典的組成包含鍵（Keys，不可變）與值（Values，可變）
 - 使用 Key 來尋找對應的 Value，以上述例子來說即為使用字尋找讀音
 - Key 跟 Value 可以是任何資料類別，也可以不用一樣
 - 字典是無序的（在 collection 這個 library 中有提供有序字典）
 - 若查找不存在的 key 則會報錯，可以使用 `in` 或 `dict.get()` 來檢查

```python=
mydict = dict()  # or mydict = {}
print("Here is an empty dictionary:", mydict)
mydict[1] = 'one'
mydict[2] = 'two'
mydict[3] = 'three'
print(mydict)
print("2 is corresponding to:",mydict[2])
```
```
Output:
Here is an empty dictionary: {}
{1: 'one', 2: 'two', 3: 'three'}
2 is corresponding to: two
```

```python=
# Continued from last cell
print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(5 in mydict)
print(mydict.get(5))
```
```
Output:
dict_keys([1, 2, 3])
dict_values(['one', 'two', 'three'])
dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
False
None
```

#### 集合（Set）
 - 與數學中的集合概念類似，只能儲存唯一（Unique）元素，相同元素不會重複出現
 - 因為是無序，故我們不能使用 `set[0]` 的方式來取值
 - 可以使用 `set.add(item)` 與 `set.remove(item)` 來新增與刪除元素
 - 可以使用 `set(list)` 將 List 轉為 Set，藉此檢查清單中唯一元素個數
 - 相關操作有聯集、交集、差集等等

```python=
aset = {11, 22, 33}
bset = {33, 44, 55}
print("Union:", aset | bset)
print("Intersection:", aset & bset)
print("Difference(A-B):", aset - bset)
print("Difference(B-A):", bset - aset)
print("Symmetric difference:", aset ^ bset)
```
```
Output:
Union: {33, 22, 55, 11, 44}
Intersection: {33}
Difference(A-B): {11, 22}
Difference(B-A): {44, 55}
Symmetric difference: {11, 44, 22, 55}
```

> 特別注意 [運算元優先順序](https://june.monster/python-101-operators-and-priority/) ！

#### 統整
| 類別 | Tuple | List | Dict | Set |
| --- | --- | --- | --- | --- |
| 符號 | ( ) | [ ] | { } | { } |
| 可變性 | 不可變 | 可變 | 可變 | 可變 |
| 順序性 | 有序 | 有序 | 無序 | 無序 |