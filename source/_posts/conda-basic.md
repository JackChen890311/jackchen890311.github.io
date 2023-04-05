---
title: 使用 Conda 管理 Python 開發環境
categories:
  - 學習筆記
tags:
  - Python
  - Conda
date: 2023-04-04 21:29:03
cover: /img/cover/conda.jpg
---

繼上篇 [安裝雙系統](https://jackchen890311.github.io/Website/2023/02/24/install-windows-and-linux/) 並順便安裝 Miniconda 完成後，這篇來稍微介紹一下使用 Conda 的好處在哪裡，順便記錄一些常用指令，不然我自己常常忘記怎麼刪環境，每次都要重新找 XD。

Conda 為一種套件管理工具，使用 Conda 來管理開發環境非常方便，指令簡單也能保持環境乾淨整潔，要匯出環境版本時也不會有其他多餘的套件干擾。常見的安裝方式有 Anaconda 與 Miniconda 兩種，相比之下 Miniconda 只提供必要功能，Anaconda 相對全面，但也比較複雜一些。Python 的 virtualenv 也有相似的虛擬環境功能，但我個人還是認為 Conda 好用一些，也很感謝實習讓我接觸到 Miniconda。

![Conda Comparison](/img/post/2023_04/conda_comparison.jpg)

Figure source is [here](https://www.machinelearningplus.com/deployment/conda-create-environment-and-everything-you-need-to-know-to-manage-conda-virtual-environment/).

## 常用指令
以下作業系統為 Ubuntu 22.04 LTS，括號請自行替換。
```bash=
# Check conda version and update conda
conda -V
conda update conda

# Create and remove an environment
conda create -n [env_name] python=[3.x]
conda env remove -n [env_name]

# Remove specific package in a environment
conda remove -n [env_name] [package_name]

# List all Environment
conda env list

# Get into / get out of an environment
conda activate [env_name]
conda deactivate

# Create an identical environment
conda list --explict > [spec_file_name].txt
conda create -n [env_name] --file [spec_file_name].txt
```

## 實際操作
安裝完 Miniconda 後，你的 Terminal 大概會變成這樣：
```bash=
(base) jack@jack-linux:~$
```
使用 `conda activate [env_name]` 進入環境後，會變成：
```bash=
(env_name) jack@jack-linux:~$
```

此時就正常操作即可，你就可以任意的 `pip install`，而不用擔心環境很亂了，大不了再刪掉就好，是不是很簡單！其實說穿了，最常用到的指令就那幾個，再多一點上面也都包含了，完全不難學也不複雜，還可以很輕鬆的切換不同環境，良好的管理 Python 與其套件版本。

## 結語
這篇文其實沒啥好寫的，因為 conda 就是個這麼簡單的東西，但是他卻提供了很實用的功能，來幫助開發者管理套件版本與環境。少量開發的話可能還好，但像是我實習時常常會需要調整套件版本，或是有新專案要啟動，這時 conda 就是個很實用的工具，心動的話趕快到 [官網](https://docs.conda.io/en/latest/miniconda.html) 下載吧！