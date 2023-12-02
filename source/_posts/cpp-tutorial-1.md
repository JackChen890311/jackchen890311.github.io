---
title: C++ 教學系列文 (1) - 基本語法速覽、指標
categories:
  - C++ 教學
tags:
  - C++
  - Tutorial
cover: /img/cover/C++.png
date: 2023-12-02 16:07:13
---


哈囉！許久沒有更新了，因為碩班真的是好忙呀嗚嗚，等我寒假或是比較有空的時候，會再開始更新一些東西。這次來發 C++ 的教學文章，延續之前的 Python 教學系列文，在教完 Python 之後，學生說想學 C++，身為好老師的我就又做了一份講義給他，抱持著造福社會的精神，就順便分享到我的網站上。（題外話：這個學生上個月剛教滿一年，也是我目前接最久的家教，甚至打這篇文章的現在也在幫他上課哈哈。之後還有一些其他主題的教學文，整理完以後我再發上來。）

此系列文只有兩篇，建立在你已經會寫基本的 Python，或是看完我的 Python 教學系列文的基礎上撰寫，所以如果還沒看過的可以點 [這邊](https://jackchen890311.github.io/categories/Python-%E6%95%99%E5%AD%B8/) 來看。那因為已經有一個程式語言的概念了，所以我會著重在 C++ 與 Python 不同的地方，那些差不多的語法（if-else, for, while...） 我會在最前面速速帶過，有不懂的話建議回去參照對應的 Python 教學文部分，或是我提供的參考連結。一樣要提的是，我原本是做講義用，文字部分不會太詳盡，有需要更詳盡的內容歡迎聯絡我，如果我有空就可以幫你上課 XD，最後就是轉載請記得標註來源！

[HackMD 完整版請點我](https://hackmd.io/C7kIxIuJQImM_x64fhuM_A?view)

## 基本語法
 - 參見 [C++ 語言自學手冊](https://cpp.enmingw32.dev/)，此不贅述
```cpp=
#include<iostream>
using namespace std;

int main(){
    // Your program starts here
    
    // Variable Types
    int a = 0;
    char b = 'b';
    float c = 3.14;
    double d = 3.1415;
    bool e = true;
    
    // Basic Input & Output
    cin >> a;
    cout << "hello world";
    
    // Control Flow
    if (a == 0){
        cout << "a is 0\n";
    }
    else if (a > 0){
        cout << "a is greater than 0\n";
    }
    else{
        cout << "a is less than 0\n";
    }
    
    switch (a) {
    case 1:
        cout << "a = 1";
        break;
    case 2:
        cout << "a = 2";
        break;
    default:
        cout << "a != 1 && a != 2";
        break;
    }
    
    // Loops
    // Both have continue & break
    int N = 10;
    for (int i = 0; i < N; i++){
        cout << "Loop " << i << endl;
    }
    
    int i = 0;
    while (i < N):{
        cout << "Loop " << i << endl;
        i++;
    }
    
    // Your program ends here
    return 0;
}
```


## 指標（Pointers）
指標是一個強大的工具，用於指向變數，或直接操作記憶體位置，也是 Python 中沒有的一種變數類別，但卻是個很重要的概念。指標能夠讓我們間接引用變數和物件，並在動態記憶體配置和資料結構中皆發揮了重要的作用。透過指標我們可以訪問和修改記憶體中的數據，提供更高的靈活性和效能。然而，正確使用指標很重要，因為錯誤的操作可能導致記憶體問題，像是存取到未分配的空間等等。

先介紹兩個運算子：
- &：Address-of Operator, 取址運算子，用以取出變數所在之記憶體位址
- \*：Dereference Operator, 取值運算子，用以取出變數所指向位置之值

> & 與 \* 可以互相抵銷，另外 \* 同時也是乘法運算元，要小心喔！

搭配以上兩者之使用，我們便可以使用指標：
- 創建指標並指向變數（我們通常將 int* 直接視為一個變數類別） 
```cpp=
int a = 10;
int* aPtr = nullptr; // or int *aPtr = nullptr;
aPtr = &a;
*aPtr = 20; // we can change the value of a variable by pointer
cout << a << endl; // 20

// Any type can be pointed at, for example:
int** aPtrPtr = &aPtr;
class Car{
    // Implementation of Class Car
}
Car c;
Car* cPtr = &c;
```

- 指標、變數、* 與 & 的關係
```cpp=
int a = 10;
int* aPtr = &a;
cout << "value of a = " << a << endl; // 10
cout << "value of aPtr = " << aPtr << endl; //0x123450
cout << "address of a = " << &a << endl; //0x123450
cout << "address of aPtr = " << &aPtr << endl; //0x543210
cout << "value of the variable pointed by aPtr = " << *aPtr << endl; // 10
```
<!-- ![](https://hackmd.io/_uploads/Sy31aVCS2.png) -->

- 動態記憶體配置（DMA）
```cpp=
// for integer
int* ptr = new int;
*ptr = 0
// Remember to do this at the end, to avoid memory leak!
delete ptr;
ptr = nullptr;
```
```cpp=
// for integer array
int N;
cin >> N;
int* ptr = new int[N];
for (int i = 0; i < N; i++){
    ptr[i] = 0;
}
// Remember to do this at the end, to aviod memory leak!
delete [] ptr;
ptr = nullptr;

/* 
Don't do this, this is for static memory allocation
int N = 10;
int arr[N];
*/
```
> 延伸閱讀：[Why must we use pointer during dynamic memory allocation in C++?](https://qr.ae/pyFiAo)

- 應用：swap() 實作
    - 錯誤示範（Recap：區域變數與全域變數）
    ```cpp=
    void badSwap(int a, int b) {
        int t = a;
        a = b;
        b = t;
    }
    ```
    - 正確示範（注意呼叫時要傳入 int* ！）
    ```cpp=
    void goodSwap(int *a, int *b) {
        int t = *a;
        *a = *b;
        *b = t;
    }
    ```

- 指標的概念圖
![](https://hackmd.io/_uploads/S11bK4Arh.png)

> 延伸閱讀：[圖解說明指標概念](https://husking-studio.com/cpp-pointer-tutorial/)