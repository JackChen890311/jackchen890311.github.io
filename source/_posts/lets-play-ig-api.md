---
title: 來玩玩 Instagram 的基本顯示 API 吧！
categories:
  - 學習筆記
tags:
  - Instagram
  - API
  - Python
  - Ramen
cover: /img/cover/IG.jpg
date: 2023-05-05 19:41:28
---
# 2025 更新：基本顯示 API 已被棄用
![Meta 的棄用公告](/img/post/2023_05/deprecation.png)

這下頭痛了，原本研究的都沒用了，之後再來看看新的方法要如何操作......只能說我真的越來越討厭 Meta 了（[來源](https://developers.facebook.com/docs/instagram-platform/)）。

---

先來 [這邊](https://jackchen890311.github.io/ramen/) 看看我把 Instagram 上的貼文整合到我的個人網站上的成果吧！

# 為啥要爬 Instagram API？
會有這個念頭，是我之前某天突然想到，如果可以把我的 [拉麵帳號](https://www.instagram.com/jacklovesramen/) 中的內容整合到我的個人網站上，那應該還不錯吧？不過，我一開始想的其實是做一個互動式地圖，並把我吃過的每間店標上去，讓使用者可以依地點挑選店家，還能馬上看到我的食評，感覺就很不錯。後來發現似乎不是很好做，那就留給未來吧 XD。這次我做的主要只是去爬取 Instagram 的 API，並把爬下來的內容作清理，再以我網站框架所要求的格式寫入上傳，其實沒什麼太技術的細節，但從結果來看應該可以說是有點樣子，之後也可以自動更新內容（但因為我的網站是使用靜態網站的框架，需要我手動上傳我更新的內容；如果是動態網站可以直接把呼叫 API 的部分寫在網站上，做動態的渲染等等），接著就來看看我怎麼做的吧！

# 來看看 [官方文檔](https://developers.facebook.com/docs/instagram-basic-display-api/getting-started) 吧！

若官方文檔太文謅謅看不太懂，也可以另外搜尋其他教學，像是 [這篇](https://www.letswrite.tw/instagram-basic-display-api/) 也不錯。如同文檔上寫的，前置準備需要：

> - Facebook 開發人員帳號。  
> - 含影音素材的 Instagram 帳號。  
> - 您所擁有的公開網站。可以是一般的免費網站，像是 Github 網頁或 Heroku 網路應用程式，或您的實際網站。  
> - 指令行工具，像是 Terminal 或可執行 cURL 要求的 Postman 等應用程式。  

開發人員帳號就依照說明申請即可，指令行工具我推薦 [Postman](https://www.postman.com/downloads/)，還蠻方便使用的，也可以避免編碼在 Terminal 上看不懂的問題。大部分都按照他的步驟設定即可，特別要提的是下圖中的幾個欄位，就填入你網站的網址就好，這個只是要讓他們知道是誰呼叫這個 API 請求，如果沒有網站可以用 Github Page 簡單搞一個，或是我猜隨便一個網站應該也沒差（此言論我不負責 XD）。

![三個都放一樣就好，如果你知道這在幹嘛就自己改吧，我用不到沒研究 XD](/img/post/2023_05/api_website.png)

之後就一路按照他的步驟，邀請完後回到 IG 帳號確認邀請（因此你要爬的帳號要是自己的，或是有得到對方同意！如果想爬其他公開 IG 帳號就不能用 API，但可以用其他爬蟲方式），並在瀏覽器輸入以下網址按下同意，就可以獲取短期的 Access Code。其中 {app-id} 是你的 Instagram 應用程式編號，{redirect-uri} 可以用跟上面填寫的相同網站，是按下同意後會被重新導向的網址：

```url
https://api.instagram.com/oauth/authorize
  ?client_id={app-id}
  &redirect_uri={redirect-uri}
  &scope=user_profile,user_media
  &response_type=code
```

按下確認後，你會被重新導向到上面設定的網站，在網址列應該會長得像如下的樣子，Code 後的參數就是你的 Access Code（不包含最後的 #_）：

```url
{redirect-uri}?code={access_code}#_
```

接著，你需要再用 Access Code 換取 Access Token。開啟 Postman，使用 POST 方法發出以下請求。這邊的 {app-id} 跟 {app-secret} 是你的 Instagram 應用程式編號與密鑰，{code} 就是前面的 Access Code：

```url
https://api.instagram.com/oauth/access_token
  ?client_id={app-id}
  &client_secret={app-secret}
  &grant_type=authorization_code
  &redirect_uri={redirect-uri}
  &code={code}
```

回傳結果就是 Access Token 啦：

```json
{ "access_token": "IGQVJ...", "user_id": 17841405793187218 }
```

不過這個也是短期（1 小時）的，可以用他再發 HTTP 請求，來更換長期（60 天）的 Token，詳情參考 [這裡](https://developers.facebook.com/docs/instagram-basic-display-api/guides/long-lived-access-tokens)。

或是其實這邊也可以獲取長期 Access Token，如果你是要跟我一樣爬下來處理，然後嫌前面太麻煩的話，也可以從這邊產生。不過這個一樣定期需要重新產生，目前還沒看到比較好的方式獲取永久 Token，有人知道的話歡迎跟我分享：

![點右邊的 Generate 就好，記得要存下來，不然就要重新產生](/img/post/2023_05/api_token.png)

> 題外話，看到上面的 {redirect-uri} 我才知道原來有 URI、URL、URN 這三種東西。想知道更多可以看 [這裡](https://ithelp.ithome.com.tw/articles/10266610) 及其後續文章，有簡單的介紹。

# 有了 Token，[如何拿到圖片與文章？](https://developers.facebook.com/docs/instagram-basic-display-api/guides/getting-profiles-and-media)

不囉嗦了，直接上 API 指令，可以參考 [API 說明文件](https://developers.facebook.com/docs/instagram-basic-display-api/reference/media#fields)，{user_id} 為上面拿 Access Token 時一起回傳的結果，也可以換成每篇文章的 ID，{limit} 則為回傳數量，最多是 100 篇貼文：

```url
https://graph.instagram.com/{user_id}/media
  ?fields={fields}
  &access_token={access_token}
  &limit={limit}
```

回傳結果是 JSON 格式，當 limit = 1 時如下，很貼心的幫你把往下取的方法也給你了：

![在 Postman 中的回傳結果，會順便幫你轉編碼，讓你可以看得懂](/img/post/2023_05/api_return.png)

那因為我只需要文章內容、第一張圖片跟貼文連結，所以就只拿了這些，有需要其他的可以自己以逗號方式加入 {fields} 中，像我的話就是用 `?fields=id,caption,media_url,permalink` 這樣。

# 我要怎麼處理 JSON 資料？
這部分就簡單啦，看你後面想要怎麼用，像我就是用 Python 做，先用 requests 套件來發送 API，再把結果交給 json 套件幫我處理，最後透過字串處理與寫檔把他寫到 Markdown 檔案中，就可以呈現在 Hexo 框架中了。每個人想呈現與處理的方式不同，因此這部分就看個人喜好吧，如果你真的想參考我的程式碼可以看 [這裡](https://github.com/JackChen890311/jackchen890311.github.io/tree/main/source/ramen/crawler.py)。

![我的排版結果，依照年份分類，這樣我一年改一次頁面就好](/img/post/2023_05/ramen_layout.png)

# 結語
想做這個也是臨時起意，所以花了一個下午爬完資料 + 排完版，再半個下午產出這篇文章，算是比我想的還要快一些。但我真的很想把他做成地圖啊！可是目前這個爬法好像沒辦法爬位置資訊，就算可以好了，地圖這件事情我也需要再花時間研究，應該不是甚麼簡單的事情。至少現在有點樣子了，那個遠大的目標，就當作未來的 Side Project 吧～如果看完這篇文章，有甚麼想說的都可以留言告訴我喔！

# 更新：圖片連結失效了？！
過了幾天再回來看，發現我所有的圖都不見了 QAQ，如下：
![我的圖呀 QQ](img/post/2023_05/ramen_broken.png)

後來發現用前面 API 的方法拿到的圖片連結只是暫時的，並不會永久存在。哎呀這下頭痛了，總不能把所有圖片都載下來吧？後來上網查了一下，發現 Instagram 還有提供常見的「內嵌功能」，從電腦版的網站就可以找到：
![從 Instagram 電腦版，貼文的右上角點進去選擇內嵌即可](img/post/2023_05/ig_embedded.png)

其他網站像是 Youtube，也會提供這種功能，基本上就是他會產出寫好的 HTML & CSS & JS原始碼，讓你可以貼到其他網站上使用，同時也能導回原始的頁面。（到頭來感覺前面都在做白工...）內嵌的效果如下：
![使用內嵌功能後的長相，下面的字是我另外加的](img/post/2023_05/ramen_new_layout.png)

所以最後我就把我原本的頁面全部替換成用內嵌的方式，並且也修改了我的程式碼，讓以後更新時也能以內嵌方式產生內容，結果到頭來根本就有現成的工具可以用嘛，我還在那邊 Call 人家 API XD。但總之就把我的心路歷程都記在這裡，給有需要的人參考。