---
title: 使用 Hexo + Github pages 建立個人網站
categories: 
  - 學習筆記
tags: 
  - Hexo
  - Github
cover: /img/cover/macbook.jpg
date: 2023-01-19 14:01:49
---
嗨！在經過一個假日的摸索之後，這個網站算是有點樣子了。很早以前就有建立個人網站的想法，但一直很忙（懶）所以沒有做，這次趁著進入研究所前的空檔，打算好好經營個人網站並且做一些有興趣的事，同時希望以後可以持續更新技術相關的學習筆記在這裡。

作為第一篇文章，先來分享一下如何使用 Hexo + Github pages 建立個人網站，並修改一些基礎的 Configuration。本網站的文章都會預設讀者有一定的技術了解，因此不會寫的完完全全白話，若有疑問歡迎下方留言，或是自己搜尋相關介紹。（又或是問強大的 ChatGPT，我都用他來 Debug 🤣）

## 靜態網站產生器
靜態網站產生器是快速架網站的實用工具，他提供了便於使用的框架以及多種不同的主題，讓一般使用者也能夠快速方便的建置自己的網站。常見的框架有 Jekyll、Hexo、Hugo，詳細的比較有興趣可以參考 [這裡](https://raychiutw.github.io/2019/Static-Site-Generator-Comparison/)，本篇會介紹 Hexo 框架的使用流程。


## 下載 [Hexo](https://hexo.io/zh-tw/) 並建置第一個網站
- 下載 [Node.js](https://nodejs.org/en/)，完成以後用 `node -v` 檢查是否安裝成功
- 執行 `npm install hexo-cli -g` ，使用 npm 來安裝 Hexo
- 完成後先切換到你想存放檔案的路徑，執行 `hexo init [repo_name]`
- 使用 `cd [repo_name]` 進入該資料夾，執行 `npm install` 安裝所需套件
- 完成後執行 `hexo server`，點擊 Terminal 中出現的網址 http://localhost:4000/[repo_name]/ ，大功告成！

如上，是不是很簡單！接著我們來看看要怎麼配置主題。


## 配置 [Butterfly 主題](https://github.com/jerryc127/hexo-theme-butterfly/)

完成上述安裝後，進入瀏覽器看到的會是預設的 Landscape 主題，但如果只用預設主題就太沒意思了，因此接著我們要來配置 Butterfly 主題，可以在 [這裡](https://butterfly.js.org/) 觀看該主題的 Demo。除此之外，Hexo 也有 [眾多主題](https://hexo.io/themes/) 可以挑選，大家可以自行比較挑選。在剛剛的路徑下執行：

```cmd=
npm install hexo-theme-butterfly
npm install hexo-renderer-pug hexo-renderer-stylus --save
```

安裝完成後，將目錄底下的 `_config.yml` 打開，修改以下配置：
```yaml=
theme: butterfly
```
最後執行 `hexo server`，就可以看到修改主題過後的結果了。

## 使用 Github Pages 來部署網站
有了主題之後，接著就是設定部署方式。這邊使用 Github Pages 來幫助我們部署網站，Github Pages 提供穩定的服務以及客製化的網域名，若不想花錢花時間搞自己的伺服器跟網域，可以說是相當不錯的選擇。

首先我們要先具備 Github 帳號以及 Github Desktop，如何申請及下載不在此贅述。打開 Github Desktop 後，找到剛才的路徑的上一層，並以 `[repo_name]` 來創建新的 Repository，這邊記得要選 Public Repository，才能使用 Github Pages 的相關功能，然後再將前面下載的檔案都 Push 上 Github。

將目錄底下的 `_config.yml` 打開，修改以下配置：
```yaml=
url: https://[user_name].github.io/[repo_name]
root: /Website/
...
deploy:
  type: git
  repo: https://github.com/[user_name]/[repo_name]
  branch: github-pages
```

後半部的 Deploy 設置部分，是為了讓我們日後可以快速部署所需的設定，另外還要下載 `hexo-deployer-git`，就能使用 `hexo deploy` 完成快速部署：
```cmd=
npm install hexo-deployer-git
hexo generate
hexo deploy
```

當我們輸入 `hexo generate` 後，Hexo 會幫我們產生靜態檔案，也就是常聽到的 HTML、CSS、JS等等，再使用 `hexo deploy` 推上 Github Repository 裡 github-pages 這個分支。我們的 Repository 上共會有兩個分支，main 存放主要程式碼及配置檔案，github-pages 則存放部署相關檔案。

接著我們需要再到 Github 網站上，設定使用 github-pages 這個分支來進行部署，可以在 `Repository -> Settings -> Pages` 裡找到相關的設置。設置完成後稍等幾分鐘，就可以到 https://github.com/[user_name]/[repo_name] 來觀看成果了。

## Hexo 常用指令
更詳細的說明可以到 [官方文件](https://hexo.io/zh-tw/docs/) 尋找，這邊列出幾個常用指令：
- `hexo generate`：產生靜態檔案到 `/public` 資料夾中
- `hexo clean`：清除 `/public` 資料夾
- `hexo deploy`：將 `/public` 資料夾中檔案推上 Github
- `hexo server`：在本地端執行 Server，可預覽網站呈現效果，同時監聽本地文件的修改
- `hexo server --draft`：可同時預覽草稿在網站上的呈現效果
- `hexo new [layout] [title]`：新增以 `layout` 為樣式的文件
- `hexo publish [layout] [title]`：將草稿以 `layout` 為樣式發布出去

不過有時候 `hexo server` 會怪怪的，突然無法監聽本地文件的修改，不太清楚原因。正常來說，除了修改 `_config.yml` 檔需要重啟 Server 外， Markdown 檔的修改應該都能直接即時更新，有人知道的話歡迎跟我分享。
 
## 如何設定 Configuration
Butterfly 主題提供了很大的彈性，讓我們可以自訂各種設置。詳細的設定可以直接到 [Butterfly 官方說明](https://butterfly.js.org/categories/Docs%E6%96%87%E6%AA%94/) 這裡參考，裡面解釋得很詳細，也有圖片展示不同的效果。可以先到 [Github 上的 _config.yml](https://github.com/jerryc127/hexo-theme-butterfly/blob/dev/_config.yml) 複製一份，另外存放在 `_config.butterfly.yml` 中，在以這個為基礎進行修改。注意不要刪除原本就有的 `_config.yml`，一個是配置 Butterfly 主題，另一個則是配置 Hexo。

## 如何新增內容
Hexo 框架中，頁面都是使用 Markdown 語法撰寫，若不熟悉的話可能要先去研究一下。Markdown 是一種簡單的標記語言，多用來排版與美化版面，像是 # 代表標題等等。透過上面的 `hexo new [layout] [title]` 指令，Hexo 會先去 `\scaffolds` 底下尋找名為 `[layout].md` 的檔案，並以其樣式為基礎，在 `\source` 或 `\source\_post` 底下新增名為 `[title].md` 的檔案，而我們直接編輯這個檔案即可。

使用 Markdown 的好處除了排版方便之外，之後若要更換框架，或是移動文章， Markdown 的相容性都很高，可以減少移動所需的成本。另外，若需要放其他類型的檔案，像是圖片檔等等，也可以自己在 `\source` 底下新增資料夾，執行 `hexo generate` 的時候 Hexo 會幫你一起搬過去。

### Page、Draft、Post?
`\scaffolds` 底下預設有三個檔案，分別為 Page、Draft、Post，分別對應到頁面、草稿、跟文章的模板。簡單來說，你需要使用與頁面放一些相關訊息時用 Page，想寫草稿時用 Draft，想直接寫文章就用 Post；而三者分別會存放於 `\source`、`\source\_drafts`、`\source\_posts`，而草稿不會展示在網站上。當然，你也可以自己新增自己所需的模板，再使用 `hexo new [layout] [title]` 時就能有更多彈性的選擇，也不用每次都重新修改頁面前面的設置。（可以參考 [這裡](https://butterfly.js.org/posts/dc584b87/) 了解更多關於前置設置的細節）

### Tags、Categories、Link?
這三個算是比較特別的頁面，分別存放所有的標籤、分類以及自定義的外部連結。標籤跟分類可以幫助你網站的使用者快速找到相關文章，日後要回顧時也比較方便。外部連結則視個人需求，想放什麼連結都可以。設定這三個頁面的方式是在頁面的前置設置加上 type：
```yaml=
type: tags/catrgories/link #三選一即可
```
前兩者基本上 Butterfly 會幫你配置好，沒有需要可以不用修改， Link 頁面就需要自己新增，看是要加在 `\source\link\index.md` 底下，或是依照官方說明加在 `\source\_data\link.yml` 都可以。

## 總結
這篇文章斷斷續續寫了五天，總算是把他完成了，赫然發現寫技術文章並沒有想像中的輕鬆。在本文內我盡量涵蓋到所有內容，同時以精簡的方式，整理架設個人網站所需要的所有指令與知識，若寫得不好還請多多包涵，也歡迎給予我一些回饋。

我認為對於資訊相關科系的學生來說，有一個自己的網站還是蠻不錯的，一來可以練習架設網站所需的技術，對於一些框架、服務能更加瞭解；二來可以分享在學期間的學習筆記，像是論文解讀、指令整理等等，分享之餘自己也能受惠；再來就是自己架網站彈性較大，也不用受限於其他網站的各種限制，更能自己擴充其他功能。希望在未來繁忙的研究所或工作生活中，還有時間回來這邊分享一些東西。

本文到此結束，感謝觀看的每一個你！