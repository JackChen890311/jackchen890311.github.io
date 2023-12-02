---
title: Python 教學系列文 (6) - 檔案讀取、例外處理、斷言
categories:
  - Python 教學
tags:
  - Python
  - Tutorial
cover: /img/cover/python_clear.jpg
date: 2023-03-23 20:54:46
---

[HackMD 完整版請點我](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw?view)

### 檔案讀取（File I/O）
在 Python 中，很常會用到檔案相關的操作，舉凡文字檔（.txt）、CSV檔（.csv）、圖片檔（.png, .jpg...）、影片檔（.mp4, .avi...）等等，都會需要讀取、寫入檔案。這邊先以文字檔作為示範，僅簡單講解基礎操作，其他檔案如圖片、影像有些會有專門的 library 來處理。

test.txt:
This is a test txt file.
This is another line.

 - 全部讀入

```python=
file = open('test.txt','r')
data = file.read()
file.close()
print(data)
data = data.split('\n')
print(data)
```

```
Output:
This is a test txt file.
This is another line.
['This is a test txt file.', 'This is another line.']
```
 - 逐行讀入

```python=
file = open('test.txt','r')
while True:
    line = file.readline()
    if not line:
        break
    print(line,end='')
file.close()
```
```
Output:
This is a test txt file.
This is another line.
```

 - 寫入檔案
     - 新增在原始資料後面

```python=
file = open('test.txt','a')
file.write('This is a new line.')
file.close()
```
test.txt:
This is a test txt file.
This is another line.
This is a new line.
- 從頭重新寫入（會覆蓋原始資料）

```python=
file = open('test.txt','w')
file.write('This is a new line.')
file.close()
```
test.txt:
This is a new line.

要記得加上 `file.close()` 來關閉檔案，以免造成潛在的 Memory Leak。有一個更好的寫法，使用 `with` 來達成，如下例：
```python=
with open('test.txt','r') as file:
    # Do some file-related operations
    # The file will close automatically when this block is finished
# Do other operations
```
將檔案相關操作放在 `with` 的區塊中，而非檔案相關操作放在外面，一方面能確保檔案有被關閉，一方面也能增加可讀性。

### 例外處理（Exception Handling）
寫程式難免會遇到 Error 的狀況，當我們不希望程式因為 Error 而停止執行並噴出一大堆錯誤訊息時，可以使用以下技巧來處理。
 - `try` 必須搭配 `except` ，預設先執行 `try` 裡的程式碼
 - 當 `try` 執行失敗時， `except` 裡才會被執行
 - 與 `if...else...` 有異曲同工之妙，但不會因遇到錯誤而停止執行
 - 有時候會造成難以 debug ，使用上要特別小心
 - 另外可以使用 `raise` 來定義自己想要的 Exception

```python=
x = input()
if not x.isdigit():
    raise Exception("Not A Integer")
else:
    x = int(x)
    
try:
    inv = 1/x
    print(inv)
except ZeroDivisionError:
    print('Denominator cannot be 0!')
except TypeError:
    print('Type is not correct!')
except:
    print('Other Error!')
```
```
Output (when input = 2): 0.5
Output (when input = 0): Denominator cannot be 0!
Output (when input = 'A'): ... Exception: Not A Integer
```
此處要注意的是，前兩種狀況程式可以順利結束，因為我們使用 `except` 來處理分母為0的例外；但第三種狀況 Python 會報錯，程式中斷無法繼續往下執行，因為我們 寫「當 x 不是數字時就 raise error」，Python raise error 後就會停止。

### 斷言 （Assertion）
Assertion 提供一種保護機制，確保執行到某個地方時，某樣我們預期的條件仍然成立。若不成立則會丟出 Assertion Error，可以加入自定義的訊息。

```python=
x = int(input())
assert x >= 0, 'x is not positive'
print('A Positive number is:',x)
```
```
Output (when input = 1): A Positive number is: 1
Output (when input = -1): ... AssertionError: x is not positive
```