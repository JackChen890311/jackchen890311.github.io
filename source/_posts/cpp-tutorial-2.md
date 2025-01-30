---
title: C++ 教學系列文 (2) - 類別、延伸議題
categories:
  - C++ 教學
tags:
  - C++
  - Tutorial
cover: /img/cover/C++.png
date: 2023-12-02 16:07:18
---


[HackMD 完整版請點我](https://hackmd.io/C7kIxIuJQImM_x64fhuM_A?view)


## 類別（Class）
作為物件導向的程式語言，C++ 的 class 相關語法可以說是非常重要與常用，在大型專案的開發一定少不了他的身影，且多樣又彈性的語法支援，可以說是將物件導向的概念發揮到了極致。此處我們簡述一些常見的相關語法與概念，過於高深或少見的語法我們會先略過。

- 基本語法
```cpp=
class Car {
    private:
        int wheels;
        string plateID;
        string driver;
        bool engine;
        int meters;

    public:
        Car(string plateID, string driver);
        ~Car();
        void turnOnEngine();
        bool checkEngine();
        void drive(int distance);
        void turnOffEngine();
        void whoisDriving();
        int getMeters();
};

Car::Car(string plateID, string driver) {
    this->wheels = 4;
    this->plateID = plateID;
    this->driver = driver;
    this->engine = false;
    this->meters = 0;
    this->turnOnEngine();
}

Car::~Car() {
    // This is a Destructor
    // You can and you should delete dynamically allocated memory here
}

void Car::turnOnEngine() {
    if (this->checkEngine()) {
        this->engine = true;
        cout << "Engine Started!" << endl;
    }
}

bool Car::checkEngine() {
    return true;
}

void Car::drive(int distance) {
    if (engine) {
        this->meters += distance;
        cout << "Drive " << distance << " kilometers." << endl;
    }
    else {
        cout << "Engine is not turned on." << endl;
    }
}

void Car::turnOffEngine() {
    this->engine = false;
    cout << "Engine has been turned off." << endl;
}

void Car::whoisDriving() {
    cout << this->driver << " is driving the car." << endl;
}

int Car::getMeters() {
    return this->meters;
}
```

從上面的例子中，我們可以發現幾點與 Python 較不同的地方：

 - 甚麼是 private、public？
 - Constructor 與 Desturctor 在哪裡？
 - self 變成 this 了？
 - 為何所有 function 前面都有 Car::？

別擔心，我們一樣一樣來看。

### Private、Public、Protected
在C++中，private、public 和 protected 是用來定義類別中成員的可存取性（accessibility）的關鍵字，它們決定了這些成員在類別的內部和外部的可見性和可存取性。

- Private：僅限類別內部成員存取，不可透過外部存取（像是從外面寫 c.wheels 就是非法操作會報錯，必須透過額外的 getter 與 setter 才能對其進行操作），不會被繼承
- Protected：與 Private 類似，唯一不同是會被繼承
- Public：可以任意從外部取用，無任何限制

簡而言之，如果目前還沒有複雜的繼承需求，就簡單使用 public 與 private 區分即可！不想讓別人操作到的就用 private，沒差的就用 public！

> [參考：C++ public, protected, private 總和比較整理](https://www.wongwonggoods.com/all-posts/cplusplus/cpp-concept/c-public-protected-private/)
> [延伸：C++ public、protected、private 和 friend](https://blog.csdn.net/a3192048/article/details/82191795)

#### Getter & Setter
為了要存取與修改 Private member variable，我們會使用 Getter & Setter 來幫助我們。

- Getter
    * 用於獲取變數的值
    * 通常公開的方法，通常以 get 為前綴，後接要獲取的屬性名稱
- Setter
    * 用於設定變數的值
    * 通常公開的方法，通常以 set 為前綴，後接要設定的屬性名稱，並會接受參數以更新屬性的值

一個簡單的例子：
```cpp=
class MyClass {
private:
    int myValue;

public:
    int getValue() const {
        return myValue;
    }
    void setValue(const int& newValue) {
        this->myvalue = newValue;
    }
};
```

> 延伸問題：既然如此，為何不乾脆直接改成 Public 就好？
> 參考解答：因為透過 Getter & Setter，我們可以更好的控制 Private Member Variable 的獲取與修改，進而避免不想要或意外的情況產生

#### 封裝（Encapsulation）
上述的 Getter & Setter，其實就是實現了物件導向程式設計（OOP）中「封裝」的概念。（[複習：OOP 三大精隨](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw#OOP-%E4%B8%89%E5%A4%A7%E7%B2%BE%E9%9A%A8---%E5%B0%81%E8%A3%9D%E3%80%81%E7%B9%BC%E6%89%BF%E3%80%81%E5%A4%9A%E5%9E%8B%EF%BC%88%E8%A3%9C%E5%85%85%EF%BC%89)）

將物件的內部狀態和行為隱藏在物件內部，只公開必要的方法給外界使用。封裝可以保護物件免於外界的非法存取，並且讓物件更容易維護和修改。

```cpp=
class Animal {
private:
    string private_name; // This cannot be accessed from the outside

public:
    string public_name; // This can be accessed from the outside
    void setName(const string& name) {
        this->private_name = name; // Setter
    }
};
```

### Constructor & Destructor
constructor(建構函式) 與 destructor(解構函式) 是 class 中的兩種特別函式，當主程式中產生某 class 的物件時，該 class 的建構函式即會自動執行；而當物件生命周期結束，則在物件消滅前會自動執行解構函式。

其相應語法如下：
```cpp=
Car::Car(string plateID, string driver) {
    this->wheels = 4;
    this->plateID = plateID;
    this->driver = driver;
    this->engine = false;
    this->meters = 0;
    this->turnOnEngine();
}

Car::~Car() {
    // This is a Destructor
    // You can and you should delete dynamically allocated memory here
}
```
> 參考：[Constructor & Destructor](http://cpp2015.blogspot.com/2015/07/constructor-destructor.html)

### This
C++ 中的 this 就與 Python 中的 self 相同意思，但不同於 Python 的是，我們不需要將 this 寫在 member function 的第一個參數位置，就能夠直接使用。

- `self.` (python) <-> `this->` (C++)

事實上，當我們創建一個類別指標，並讓該指標指向一個實體物件後，也可以使用 `->` 來存取該物件的屬性或方法，如下所示。
```cpp=
Car mycar;
Car* carPtr = &mycar;
cout << mycar.driver << endl;
cout << carPtr->driver << endl;
```

### 成員函式的宣告與定義（Car::）
一般來說，我們會將函數的實作（Implementation）與函數宣告（Declaration）寫在一起，像是：
```cpp=
Class Test{
    public:
        Test(){
            cout << "Constructor!" << endl;
        }
        void hello(){
            cout << "Hello!" << endl;
        }
        ~Test(){
            cout << "Destructor!" << endl;
        }
};
```

不過此種寫法的壞處是，當我們成員函式太多時，整個 Class 會變得很常難以閱讀，因此我們也可以把實作部分（Implementation）拉出來寫，但為了要避免混淆，必須加上該函式的範籌說明（Test::）：
```cpp=
Class Test{
    public:
        Test();
        void hello();
        ~Test();
};

Test::Test(){
    cout << "Constructor!" << endl;
}
void Test::hello(){
    cout << "Hello!" << endl;
}
Test::~Test(){
    cout << "Destructor!" << endl;
}
```

## More on Class：繼承與多型
可參考之前講過的 [OOP 三大精隨](https://hackmd.io/w5n1Ow8NSea_-UAeXTJDSw#OOP-%E4%B8%89%E5%A4%A7%E7%B2%BE%E9%9A%A8---%E5%B0%81%E8%A3%9D%E3%80%81%E7%B9%BC%E6%89%BF%E3%80%81%E5%A4%9A%E5%9E%8B%EF%BC%88%E8%A3%9C%E5%85%85%EF%BC%89)。

### 繼承（Inheritance）
子類別可以繼承父類別的屬性和方法，並且可以擴展或覆寫父類別的行為。繼承可以提高程式碼重複使用性，並且可以讓類別之間建立階層關係，方便對類別進行分類和管理。

```cpp=
class Animal {
    protected:
        string name;

    public:
        Animal(const string& name) {
            this->name = name;
        }

        virtual void walk() const {
            cout << "walking" << endl;
        }

        virtual void eat() const {
            cout << "eating" << endl;
        }
};

class Dog : public Animal {
    public:
        Dog(const string& name) {
            this->name = name + " the dog";
        } // Constructor will not be inherited
};

int main() {
    Dog A("A");
    A.walk();
    A.eat();
    cout << A.name << endl;
    return 0;
}

```

```
Output:
walking
eating
A the dog
```

#### 繼承方法
上述的繼承使用 `class Dog : public Animal` 這行，這邊有個 keyword `public` 出現，這個 keyword 代表這邊使用的方法為 `public` 繼承方法，依照不同的繼承方法與不同的父類別可見度，會產生如下的表格：

![](https://hackmd.io/_uploads/ByFcnXoya.png)

這表格我認為參考就好，不用記下來，搞不清楚的話就都用 `public` 繼承方法即可。


### 多型（Polymorphism）
同樣的方法名稱可以在不同的類別中有不同的實現方式，這稱為多型。多型可以讓程式碼更加靈活，並且可以讓不同的物件對相同的方法有不同的行為。多型可以通過繼承和介面實現，是物件導向設計中非常重要的概念。
 
```cpp=
class Animal {
    protected:
        string name;

    public:
        Animal(const string& name) {
            this->name = name;
        }

        virtual void walk() const {
            cout << "walking" << endl;
        }

        virtual void eat() const {
            cout << "eating" << endl;
        }
};

class Dog : public Animal {
    public:
        Dog(const string& name) {
            this->name = name + " the dog";
        }

        void walk() const override {
            cout << name << " is using foot to walk" << endl;
        }

        void eat() const override {
            cout << name << " is eating bone" << endl;
        }
};

class Duck : public Animal {
    public:
        Duck(const string& name) {
            this->name = name + " the duck";
        }

        void walk() const override {
            cout << name << " is using two feet to walk" << endl;
        }

        void eat() const override {
            cout << name << " is eating worm" << endl;
        }
};

int main() {
    Dog A("A");
    Duck B("B");

    A.eat();
    B.eat();

    return 0;
}
```
 
```
Output:
A is eating bone
B is eating worm
```

### 相關補充
老實說我覺得這邊都太複雜了，但為了課程完整性還是簡單提及，除非你是 C++ 老手，不然根本不可能記得，所以我的建議是先了解概念，有需要再回來查。

- [C++ virtual 的兩種用法](https://shengyu7697.github.io/cpp-virtual/)
- [C++ 中的 Overload、Override 和 Overwrite](https://note.artchiu.org/2021/04/01/c%E4%B8%AD%E7%9A%84overload%E3%80%81override%E5%92%8Coverwrite/)
- [C++ const 的三種用法與範例](https://shengyu7697.github.io/cpp-const/)


## 延伸主題：Call by value / address / reference / assignment
 - [C++ call by value, call by address (pointer), call by reference ](https://www.wongwonggoods.com/all-posts/cplusplus/cpp-concept/cpp-value-address-pointer-reference/)
 - [Python 是 Pass By Value, Pass by Reference, 還是 Pass by Sharing？](https://medium.com/starbugs/python-%E4%B8%80%E6%AC%A1%E6%90%9E%E6%87%82-pass-by-value-pass-by-reference-%E8%88%87-pass-by-sharing-1873a2c6ac46)

## 延伸主題：C++ STL
- [C++ STL 全](https://4yu.dev/post/STL/)