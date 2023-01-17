---
title: 使用 Hexo + Github pages 建立個人網站
date: 2023-01-15 22:45:49
categories: 
    - [學習筆記]
tags: 
    - Hexo
    - Github
---
嗨！在經過一個假日的摸索之後，這個網站算是有點樣子了。很早以前就有建立個人網站的想法，但一直很忙（懶）所以沒有做，這次趁著進入研究所前的空檔，打算好好經營個人網站並且做一些有興趣的事，同時希望以後可以持續更新技術相關的學習筆記在這裡。今天來分享一下如何使用 Hexo + Github pages 建立個人網站，並修改一些基礎的 Configuration。  

## 靜態網站產生器
靜態網站產生器是快速架網站的實用工具，他提供了便於使用的框架以及多種不同的主題，讓一般使用者也能夠快速方便的建置自己的網站。常見的框架有 Jekyll、Hexo、Hugo，詳細比較有興趣可以參考[這裡](https://raychiutw.github.io/2019/Static-Site-Generator-Comparison/)，本篇會介紹 Hexo 框架的使用流程。


## 相關連結
 - [我參考的教學文章](https://blog.init.engineer/posts/HostYourBlogOnGitHub/)
 - [Node.js](https://nodejs.org/en/) 與 [Hexo](https://hexo.io/zh-tw/)
 - [Butterfly Theme Github](https://github.com/jerryc127/hexo-theme-butterfly/) 與 [Demo Website](https://butterfly.js.org/)

## 下載 Hexo 並建置第一個網站
 - 先下載 Node.js，完成以後用 `node -v` 檢查是否安裝成功
 - 完成後執行 `npm install hexo-cli -g` ，使用 npm 來安裝 hexo
 - 完成後先切換到你想存放檔案的路徑，再執行 `hexo init [repo_name]`
 - 再使用 `cd [repo_name]` 進入該資料夾，執行 `npm install`
 - 完成後執行 `hexo serve`，點擊 Terminal 中出現的網址 http://localhost:4000/[repo_name]/ ，大功告成！
 如上，是不是很簡單！接著我們來看看要怎麼配置 Butterfly 主題。

 ## 配置 Butterfly 主題
 ## 使用 Github Pages 來部署網站
 ## 如何設定 Configuration
 ## 如何新增頁面，page、draft、post？