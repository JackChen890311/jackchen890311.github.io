---
title: Python 教學系列文 (9) - OOP 三大精隨
categories:
  - Python 教學
tags:
  - Python
  - Tutorial
cover: /img/cover/python_clear.jpg
date: 2023-03-23 20:54:57
---

[HackMD 完整版請點我](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw?view)

### OOP 三大精隨 - 封裝、繼承、多型（補充）
#### 封裝（Encapsulation）
將物件的內部狀態和行為隱藏在物件內部，只公開必要的方法給外界使用。封裝可以保護物件免於外界的非法存取，並且讓物件更容易維護和修改。
```python=
class Animal:
    name = ''
    __private = '' # This cannot be accessed from the outside
    def __init__(self, name):
        self.name = name
        self.__private = '' # This cannot be accessed from the outside
```

#### 繼承（Inheritance）
子類別可以繼承父類別的屬性和方法，並且可以擴展或覆寫父類別的行為。繼承可以提高程式碼重複使用性，並且可以讓類別之間建立階層關係，方便對類別進行分類和管理。
```python=
class Animal:
    name = ''
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('walking')

    def eat(self):
        print('eating')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


A = Dog('A')
A.walk()
A.eat()
print(A.name)
```

```
Output:
walking
eating
A
```

#### 多型（Polymorphism）
同樣的方法名稱可以在不同的類別中有不同的實現方式，這稱為多型。多型可以讓程式碼更加靈活，並且可以讓不同的物件對相同的方法有不同的行為。多型可以通過繼承和介面實現，是物件導向設計中非常重要的概念。
```python=
class Animal:
    name = ''
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('walking')

    def eat(self):
        print('eating')

        
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print('{0} is using foot to walk'.format(self.name))

    def eat(self):
        print('{0} is eating bone'.format(self.name))
        
        
class Duck(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        print('{0} is using two feet to walk'.format(self.name))

    def eat(self):
        print('{0} is eating worm'.format(self.name))


A = Dog('A')
B = Duck('B')
A.eat()
B.eat()
```

```
Output:
A is eating bone
B is eating worm
```


> Code Source: [搞懂Python的OOP](https://ithelp.ithome.com.tw/articles/10200623)

## 小結
到這裡為止你已經學完絕大部分常用的 Python 語法了，簡單開發所需的語法基本上不太會超過本篇教學的範圍。然而，資訊工程的領域極其廣大，目前碰到的還僅止於皮毛，若有興趣可以繼續鑽研資料結構、演算法等等課題，也可以透過題目或專案來練習自己的 Coding 能力。另外，網路上有很多相關資訊或教學，透過網路自我學習、不斷成長，也是件很重要的事情，加油！

## 系列文結語
透過這次家教的機會，我也好好的重新複習了一次 Python 的基礎語法，自己在這個過程中也收穫了一些以前沒注意到的細節，難怪大家都說教學相長（但長的速度比較慢就是了）。我原本是想把上課講義做得像方便查找與複習的語法 & 概念精華，後來發現發成文章也不錯，希望這九篇的系列文對你有所幫助，有任何回饋都很歡迎提供給我喔！未來有時間或有機會的話，也許可以再整理一些更進階的議題（資料結構、演算法等等的），或者是我也會分享我學習的新東西，那麼就未來見啦～