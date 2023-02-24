---
title: 安裝 Windows 與 Linux 雙系統
date: 2023-02-24 23:16:55
categories:
  - 學習筆記
tags:
  - 電腦
  - OS
  - Windows
  - Linux
cover: img/cover/windows_linux.png
---

繼上一篇選完電腦配件、下完單取完貨之後，拿回家第一件事就是裝作業系統啦，不然開機只有 BIOS 介面，都沒辦法使用呢。我對這塊一開始也是完全不熟，還好在慢慢摸索跟問朋友之後，花個一兩天總算是都搞定了。本文會簡單分享我裝雙系統的過程，還有途中遇到的一些小困難，順便也會分享一些實用的資源給大家。

本文圖少連結多，因為拍圖太麻煩了，還請見諒，提供的連結中很多圖跟影片，可以去那邊看。

## 事前準備
其實一般來說，買電腦時若有順便加購正版的 Windows，店家通常會幫你一起裝好再交給你，但我因為想省一些預算（正版真的太貴了，我預算都花在顯卡上嗚嗚，但這樣還是不太好大家不要學），所以我並沒有購買，而是打算自己上網研究如何自己安裝。

而 Linux 本身是個免費且完全開源的作業系統，也很推薦大家去使用，但使用的大多是有工作需求等等，或是想自己對作業系統有更多的操作及掌握，不然一般消費者主要還是用 Windows 居多。我自己本身是有學業需求，加上我需要 Windows 讓我玩遊戲（不然就白白浪費我的顯卡了！），所以決定以雙系統的方式，買兩顆硬碟一個系統各一顆，也建議雙系統最好買兩個硬碟，不然搞磁碟分割會大概搞死你。

在電腦還沒來之前，我們可以先用 [Rufus](https://rufus.ie/zh_TW/) 來製作好開機隨身碟，等到電腦來就可以馬上安裝。開機隨身碟的意思就跟灌系統的光碟差不多，我們用 Rufus 來將系統映像檔（副檔名是 .iso）燒錄到隨身碟中，這樣就可以暫時先用該隨身碟開機，並且裡面的檔案會幫助我們將作業系統安裝到電腦上的硬碟中。

我的安裝順序：Windows 11 - Win 11 相關驅動 - Win 11 相關軟體 - Ubuntu 22.04 LTS - Ubuntu 深度學習環境建立 - Ubuntu 相關軟體，各位可以視自己需要哪些東西挑選查看。另外我主要的流程都是參照 [這個影片](https://www.youtube.com/watch?v=yMHOpOuyjdc)，他是在已有 Win 11 的狀況下安裝 Ubuntu，講解得非常詳細，也很推薦大家參考。

## Windows 環境建立
### 安裝 Windows 11
前面提到的 [映像檔](https://trnpp-my.sharepoint.com/personal/taiwan001ytshare01_trnpp_onmicrosoft_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Ftaiwan001ytshare01%5Ftrnpp%5Fonmicrosoft%5Fcom%2FDocuments%2FYT%20Files%2FWin11%20%E7%A0%B4%E8%A7%A3%E5%AE%89%E8%A3%9D%E6%AA%94&ga=1) 我是在網路上找到的，他還有附上 [教學影片](https://www.youtube.com/watch?v=On1ItiNo6qo)，應該算是蠻詳細的，基本上照著操作就好，Rufus 的操作方法則可以參考 [這裡](https://www.cc.ntust.edu.tw/var/file/50/1050/img/2915/USB_boot_disk(C)1105.pdf)，在硬碟都沒系統的狀況下，可開機 USB 插下去後打開電腦，應該就會自動從該 USB 進行開機，若沒有的話再進 BIOS 調整，這部分後面會提到。另外，如果安裝完成且連上網路後，Win 11 仍沒有啟用，可以參考相同作者開發的 [啟用器](https://www.youtube.com/watch?v=xmNmExsJeB4)，但我是沒有用到啦，他原本提供的破解版我是可以正常使用，連上網路後就一切正常。

### 如何安裝相關驅動
在安裝完 Win 11 後還沒結束，我們還需要做一些基本的設置，電腦才能正常使用。推薦大家參考 [這篇](https://ofeyhong.pixnet.net/blog/post/213842830-%E3%80%90%E7%B6%93%E9%A9%97%E8%AB%87%E3%80%91%E9%A9%85%E5%8B%95%E7%A8%8B%E5%BC%8F%E7%9A%84%E5%AE%89%E8%A3%9D%E9%A0%86%E5%BA%8F) 跟 [這篇](https://ofeyhong.pixnet.net/blog/post/223795851) 介紹，簡單來說就是要安裝主機板驅動、顯卡驅動跟做 Windows Update 啦。

安裝主機板驅動時，你可能會遇到跟我一樣的問題：我家中沒有有線網路，需要連 wifi 才能下載，但為甚麼我找不到相關的設定頁面？答案是：因為你還沒裝 wifi 驅動！我當初在這邊卡了好一段時間，家中找不到網路線，當時大半夜的也沒地方買，還好友人提供給我一個辦法：從筆電上下載再移到桌機中安裝，真的是解救我沒網路的困境。而三個東西都完成後，基本上 Windows 11 就安裝完成啦！你就可以去安裝你想安裝的各種軟體，開始正常使用它了~

補充：主機板驅動與顯卡驅動，到官網尋找對應型號下載，並視自己需求安裝即可，基本上主機板驅動有幾個是可以不用裝的，顯卡驅動應該是一定得裝除非你沒顯卡。Windows Update 就到設定裡讓他自己下載就好。另外有些主機板好像會連網後自動下載驅動，但因為我是下載驅動後才能連網所以我也不確定。

## Linux 環境建立
### 安裝 Ubuntu 22.04 LTS
現在我們已經裝好 Windows 11 了，下一步準備來裝 Ubuntu，因為我們現在的狀況跟第一部影片一樣，基本上可以跟著操作。Ubuntu 的系統映像檔在官網上就有了，應該很容易找到，下載後一樣用 Rufus 燒錄到隨身碟中。（補充：前面安裝的映像檔好像因為版本而不能關閉 Win 11 的快速啟動，不過沒關係這個不影響我們之後開機）

這邊要注意，因為我們已經有安裝好的作業系統了，開機預設便會是從已安裝好的地方啟動，因此我們在插入開機 USB 後，要進入 BIOS 手動修改開機順序，將 USB 的順位移到第一個，如同影片中所操作的，再重開機就可以進入 Ubuntu 安裝頁面了；或者是有些 BIOS 會有地方讓你直接點選想開機的裝置，直接選該 USB 即可進入 Ubuntu 安裝頁面，後面就跟隨說明安裝就好。

分配硬碟空間時要小心，盡量一次決定好如何分配，我第一次安裝時因為想說留點空間之後用，結果後來又想說全配給 Ubuntu，在那邊亂修改硬碟的 Partition Table，搞到最後無法開機，只好進 Windows 把 Ubuntu 的硬碟格式化全部重裝，浪費了我不少時間跟精力，也算是學個經驗吧。

### 如何建立深度學習環境（顯卡驅動、CUDA、cuDNN、Miniconda）
關於這些東西的安裝，網路上還蠻多一步一步的教學跟錯誤解釋，我就不贅述了，附上幾個連結給大家參考：
- [Ubuntu 20.04中安裝nvidia-driver-460版 & CUDA-11.4.2版 & cuDNN](https://medium.com/@scofield44165/ubuntu-20-04%E4%B8%AD%E5%AE%89%E8%A3%9Dnvidia-driver-cuda-11-4-2%E7%89%88-cudnn-install-nvidia-driver-460-cuda-11-4-2-cudnn-6569ab816cc5)
- [Ubuntu 20.04 安裝深度學習環境(Nvidia驅動、CUDA 10+CuDNN 7.6.5)](https://hackmd.io/@RinKu1998/B1MpzO3sD)
- [Ubuntu20.04 NVIDIA 显卡驱动，CUDA，CuDNN安装](https://zhuanlan.zhihu.com/p/474343311)

雖然三者的指令有些差異，安裝方法也不盡相同，但反正大家就參考一下，自己判斷如何安裝最適合，以下提供檢查是否安裝成功的指令：

- Nvidia Driver：`nvidia-smi`，也可以使用 `gpustat` 來檢查，有出現版本或顯卡名稱即可
- CUDA：`nvcc -V`，有出現版本及相關資訊即可
- cuDNN：
```bash=
cp -r /usr/src/cudnn_samples_v8/ .
cd  ./cudnn_samples_v8/mnistCUDNN
make clean && make
./mnistCUDNN
# 若出現 Test Passed 則代表安裝成功
```
``` bash=
# 若 make 時報 fatal error: FreeImage.h，則執行以下指令，並重新執行 make
sudo apt-get install libfreeimage3 libfreeimage-dev
```

至於 Miniconda 就到官網下載安裝就好，毫無難度，用來建立虛擬環境很方便；其他軟體也可以到 Ubuntu 的商店頁面尋找，或是上瀏覽器直接下載安裝包，也很簡單。

## BIOS 設定及開機方式
兩者都安裝完成後，再回到 BIOS 頁面，將開機順位中，Ubuntu 所在的硬碟設為第一順位，並順手關掉主機板的快速啟動，就完成整個雙系統的設定了。以後按下電腦的電源鍵後，會進入 Ubuntu 的開機選單頁面，這時候約十秒後預設會進入 Ubuntu，若要進入 Windows 則在時間內手動選擇即可。大功告成，是不是很有成就感呢！

## 結語
桌電相關的文章應該暫時告一段落了，之後有想到再回來補充分享，目前我已經可以正常使用雙系統，用 Windows 打遊戲、用 Linux 跑模型了，一機兩用真的是十分方便，也不會浪費我超貴的電腦配備，若是對雙系統有興趣，不仿自己試著裝裝看，在過程中也可以對電腦有更深入的理解。