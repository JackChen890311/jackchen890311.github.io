---
title: Python 教學系列文 (8) - 物件導向程式設計、類別
categories:
  - Python 教學
tags:
  - Python
  - Tutorial
cover: /img/cover/python_clear.jpg
date: 2023-03-23 20:54:53
---

[HackMD 完整版請點我](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw?view)

## Python 進階
### 物件導向程式設計（Object-Oriented Programming, OOP）
物件導向程式設計是軟體設計的一種方法，它把軟體分成數個「物件」來撰寫。每個物件都有自己的屬性和行為，並且可以跟其他物件互動。這樣的好處是，軟體的各部分之間彼此獨立，不但便於重複使用，也更容易理解和修改，提高軟體的可維護性和可擴展性。

物件導向程式設計是目前最流行的軟體設計方法之一，被廣泛應用於各種領域，包括網站開發、商用軟體、遊戲開發等等。常見的物件導向程式設計語言包括 Java、C++、C#、Python 等。

Credit: The world-wide famous [ChatGPT](https://chat.openai.com/chat)

### 類別（Class） - 簡介
以下我們使用一個簡單的例子來說明類別的概念：在現實生活中，有各式各樣的車子，而每台車子雖然皆不相同，但都具有共同特徵，像是有四個輪胎、都有駕駛與車牌跟廠牌、都使用汽油前進等等，這時候就很適合使用物件導向的概念為車子建造一個類別。

在以下的例子中，`Car` 是一個類別名稱，這個類別包含 `driver, engine, meter` 等等屬性（Attribute），以及 `turnOnEngine, checkEngine, drive` 等等方法（Method）。

而 `mycar` 是一個屬於 `Car` 類別的物件或變數，我們也可以建立多個屬於 `Car` 類別的物件像是 `mycar1, mycar2...`，彼此之間的屬性與函數操作互不影響。

#### 宣告類別與建構函式（Constructor）
在宣告類別時，我們使用以下語法：
- `class Car` 代表這個類別的名稱，亦可使用 `class Car()` 或 `class Car(object)`
- `def __init__()` 是一種特殊的類別方法，也稱為建構函式
    - 一個類別只有一個建構函式，若未撰寫則預設什麼事情都不做
    - 名稱必為 `__init__()`，建立此類別物件時會自動執行，不須呼叫
    - 主要用途為初始化相關配置，像是車子必有車牌號碼等等

```python=
class Car:  # or class Car(): / class Car(object):
    def __init__(self, plateID, driver):
        self.wheels = 4
        self.plateID = plateID
        self.driver = driver
        self.engine = False
        self.meters = 0
        self.turnOnEngine()
```

> 補充：在其他語言（如 C++）中，時常會見到解構函式（Destructor）的使用
> 與建構函式相對應，解構函式在物件被銷毀時會自動執行
> 其使用主要是為了刪除 Runtime 時動態分配的記憶體空間，以避免 Memory Leak
> Python 中也有提供解構函式，但因為我們通常不會自己分配記憶體
> 所以大多狀況下不需要使用，Python 會自己幫我們刪除分配的空間


#### 屬性（Attribute）與方法（Method）
- 屬性（Attribute）：靜態，描述此物件的屬性
    - 車子有駕駛、引擎、公里數等等
    - 又稱為成員變數（Member Variable）
    - 其值可以是任何東西，像是 `list`、`int`、`string` 等等，甚至可以是另一個類別
    - 會一直保存並且隨程式進行而更新，直到物件消滅為止
- 方法（Method）：動態，對此物件執行一個動作
    - 車子可以點燃引擎、檢查引擎、往前開等等
    - 又稱為成員函式（Member Function）
    - 與一般的函式（Function）撰寫方式相同

```python=
class Car:  # or class Car(): / class Car(object):
    def __init__(self, plateID, driver):
        self.wheels = 4
        self.plateID = plateID
        self.driver = driver
        self.engine = False
        self.meters = 0
        self.turnOnEngine()
        
    def turnOnEngine(self):
        if self.checkEngine():
            self.engine = True
            print("Engine Started!")
            
    def checkEngine(self):
        return True
    
    def drive(self, distance):
        if self.engine:
            self.meters += distance
            print("Drive %d kilometers."%distance)
        else:
            print('Engine is not turned on.')
    
    def turnOffEngine(self):
        self.engine = False
        print("Engine has been turned off.")
        
    def whoisDriving(self):
        print('%s is driving the car.'%self.driver)
        return self.driver

    def getMeters(self):
        return self.meters
```

#### Self
你應該有注意到上面出現了很多個 `self` 這個關鍵字，這個關鍵字在類別中扮演了很重要的角色，且任何類別方法中，第一個參數一定要是 `self`，他的意思是「這個物件本身」，而因為 `self` 代表這個方法中的物件本身，所以這個位置不需要傳入任何東西，在呼叫時可以直接無視。

用以下的例子來說：
```python=
class Car:
    ...
    def drive(self, distance):
        if self.engine:
            self.meters += distance
            print("Drive %d kilometers."%distance)
        else:
            print('Engine is not turned on.')

    def getMeters(self):
        return self.meters
```

```python=
...
print(myCar1.getMeters())
myCar1.drive(100)
print(myCar1.getMeters())
print(myCar2.getMeters())
print(myCar3.getMeters())
```

```
Output:
100
200
1000
0
```

可以注意到幾個重點：
 - 每輛車的結果都不同，因為每輛車的 `self.meters` 都不同
 - 呼叫 `mycar1.getMeters()` 時，不用傳入任何參數，但定義時卻必須定義一個參數 `self`，也就是說，類別方法的傳入參數量 + 1 = 定義參數量
 - 也可以在類別方法內來呼叫其他類別方法，像是 `self.turnOnEngine()` 

#### 靜態變數（Static Variable）
上述例子中，有些屬性是屬於整個類別共享的，像是 `self.wheels`，所有車子都有四個輪子。此時我們可以利用靜態變數，來宣告整個類別的屬性。詳細作法如下：

```python=
class Car:  # or class Car(): / class Car(object):
    wheels = 4
    def __init__(self, plateID, driver):
        self.plateID = plateID
        self.driver = driver
        self.engine = False
        self.meters = 0
        self.turnOnEngine()
    ...

```
| 變數/屬性 | 說明 | 例子 | 語法 |
| ------ | -------- | -------- | -------- |
| 實體變數 | 每個物件的屬性 | 每輛車有不同的駕駛 | mycar.driver |
| 類別變數 | 整個類別的屬性 | 所有車都有 4 個輪子 | Car.wheels |

#### 使用方式
在完成以上的宣告後，接著我們來看使用方式：
- 使用 `Car()` 來建立一個類別物件
- 使用 `myCar.drive()` 來呼叫類別方法
- 使用 `myCar.driver` 來獲取類別屬性

```python=
myCar = Car("ABC-0311","Jack")
print('=====')
myCar.drive(100)
print('=====')
driverName = myCar.driver
print(driverName, "is driving the car.")
```

```
Output:
Engine Started!
=====
Drive 100 kilometers.
=====
Jack is driving the car.
=====
```

> 補充：在其他語言中，為了更好的管理獲取權限
> 有時候會限制類別屬性或方法的取的與使用
> 此舉可以避免類別屬性被意外的修改，像 C++ 中 `private` 與 `protected` 的使用

#### 完整程式碼
```python=
class Car:  # or class Car(): / class Car(object):
    wheels = 4
    def __init__(self, plateID, driver):
        self.plateID = plateID
        self.driver = driver
        self.engine = False
        self.meters = 0
        self.turnOnEngine()
        
    def turnOnEngine(self):
        if self.checkEngine():
            self.engine = True
            print("Engine Started!")
            
    def checkEngine(self):
        return True
    
    def drive(self, distance):
        if self.engine:
            self.meters += distance
            print("Drive %d kilometers."%distance)
        else:
            print('Engine is not turned on.')
    
    def turnOffEngine(self):
        self.engine = False
        print("Engine has been turned off.")
        
    def whoisDriving(self):
        print('%s is driving the car.'%self.driver)
        return self.driver

    def getMeters(self):
        return self.meters

myCar = Car("ABC-0311","Jack")
print('=====')
myCar.drive(100)
print('=====')
driverName = myCar.whoisDriving()
print('=====')
myCar.turnOffEngine()
print('=====')
myCar.drive(100)
print('=====')
myCar.turnOnEngine()
print('=====')
myCar.drive(100)
print('=====')
meter = myCar.getMeters()
print("Meters:",meter)
```

```
Output:
Engine Started!
=====
Drive 100 kilometers.
=====
Jack is driving the car.
=====
Engine has been turned off.
=====
Engine is not turned on.
=====
Engine Started!
=====
Drive 100 kilometers.
=====
Meters: 200
```