---
title: Make your shell great again! 來安裝 Oh My Zsh 吧！
categories:
  - 學習筆記
tags:
  - Shell
  - Zsh
  - Oh My Zsh
cover: /img/cover/book_and_macbook.jpg
date: 2025-05-28 15:57:07
---

身為一個資工人，總是少不了每天跟 Shell 打交道，自從大二上過 OS 以後，什麼 `ls`、`cd`、~~`sudo rm -rf /*`~~，根本就是跟喝水一樣每天都會碰到（絕對不要試最後一個，後果自負 XD）。大多 OS 預設的 Shell 功能通常都不多，僅僅只能算是堪用而已，因此常常會遇到一些麻煩的狀況，像是你要進到很深的資料夾就要一直瘋狂 `cd`，或是要一直 `ls` 看這邊到底有什麼檔案等等。某天偶然聽到別人介紹 [Oh My Zsh](https://ohmyz.sh/)，感覺非常好用，就乾脆自己來玩玩看。（延伸閱讀：[什麼是 Shell？](https://ithelp.ithome.com.tw/articles/10216912)）

# 安裝方法
我主要綜合以下三篇文章的教學：
- [Oh my ZSH with plugins](https://gist.github.com/n1snt/454b879b8f0b7995740ae04c5fb5b7df)
- [Ubuntu 安裝 Zsh + Oh My Zsh + Powerlevel10k 與各種插件](https://www.kwchang0831.dev/dev-env/ubuntu/oh-my-zsh)
- [【分享】Oh My Zsh + powerlevel10k 快速打造好看好用的 command line 環境](https://holychung.medium.com/%E5%88%86%E4%BA%AB-oh-my-zsh-powerlevel10k-%E5%BF%AB%E9%80%9F%E6%89%93%E9%80%A0%E5%A5%BD%E7%9C%8B%E5%A5%BD%E7%94%A8%E7%9A%84-command-line-%E7%92%B0%E5%A2%83-f66846117921)

首先，如果你的作業系統不是 Mac，那通常預設 Shell 會是 Bash。可以透過以下 command 安裝 Zsh 並設置預設 Shell：
```bash
sudo apt install zsh
chsh -s $(which zsh)
```
然後重新登入應該就可以了。

接著安裝 Oh My Zsh：
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

到這裡應該就完成基本的 Oh My Zsh 安裝了。

# 擴充套件
到目前為止我們只安裝了 Oh My Zsh，但其相關擴充套件才是 Oh My Zsh 的精華所在。Oh My Zsh 完全開源，因此很多相應套件油然而生，我個人有安裝的套件如下：

- zsh-z
- zsh-autosuggestions
- zsh-syntax-highlighting
- fast-syntax-highlighting
- zsh-autocomplete

使用以下 Command 安裝：
```bash
git clone https://github.com/agkozak/zsh-z $ZSH_CUSTOM/plugins/zsh-z
git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting
git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete
```
這些操作是把相關的 Github Repo clone 到你電腦裡。

最後打開 Zsh 的 config file：
```bash
vim ~/.zshrc
```

若不熟悉 `vim` 可以使用其他程式開啟。找到 `plugins=(git)` 並取代成 `plugins=(git z zsh-autosuggestions zsh-syntax-highlighting fast-syntax-highlighting zsh-autocomplete)`，關掉 Terminal 重新打開就完成了。

# 主題
關於主題配置可以參考[官方說明](https://github.com/ohmyzsh/ohmyzsh/wiki/themes)，或是這裡有[別人的教學](https://github.com/Holychung/My_Terminal_Theme)，但我自己最後還是選用預設的主題，因為我覺得簡潔就很漂亮了。

# 結語
Shell 其實是門高深的學問，除了文中提及的 Bash 與 Zsh 之外，另外還有很多 Shell 像是 Fish 等等，本篇就不再多做贅述。總之，有了 Oh My Zsh 後，我覺得我的開發體驗又有變更好了，像是 `z` 可以輕鬆的跳來跳去，還有許多 autocomplete 的功能等等，只能說開源社群的力量太強大了！