---
title: 我的碩士論文 - AGTree：基於注意力引導的視覺概念分解
categories:
    - 學習筆記
tags:
    - Master
    - AI
    - Diffusion
cover: /img/cover/concept_decomp.png
date: 2025-10-01 23:30:58
---

# Author
國立臺灣大學 資訊工程學系研究所 R12 陳韋傑 Jack Chen  

## Professors
國立臺灣大學 資訊工程學系 許永真教授  
國立臺灣大學 資訊工程學系 鄭文皇教授  
長庚大學 人工智慧學系 楊智淵助理教授  

# AGTree

**[AGTree：基於注意力引導的視覺概念分解（AGTree: Attention Guided Visual Concept Decomposition）](https://drive.google.com/file/d/1Lhk0NEJsf9AXwXrjmoTl0_GAZG2sqX7o/view)**

![The flow of AGTree.](img/post/2025_10/agtree.png)

# 摘要
在設計嶄新的視覺概念時，設計師經常從既有的想法中汲取靈感，藉由重新組合各種元素，以創造出獨特且原創的作品。隨著文字轉圖像(Text-to-Image, T2I)模型的快速發展，機器現已能夠協助此一創作過程，特別是在分解複雜視覺概念並將其與現有概念重新組合方面。然而，現有的視覺概念分解方法通常依賴於多樣化的輸入圖像，當輸入圖像在視覺上過於相似時，這些方法往往難以將物體從顯著的背景中分離出來，導致所產出的結果難以理解或應用。

本研究揭示了被分解的視覺子概念與擴散模型中 U-Net 的交叉注意力 (cross-attention maps)之間的強烈關聯。基於此觀察，我們提出了一種新方法: AGTree。該方法使用交叉注意力圖作為內生遮罩，藉此有效抑制背景雜訊，並在訓練過程中引入隨機丟棄機制(random drop)，以提升語意上的關聯性。此外，我們擴展了現有的評估指標，使其能更全面地評估模型表現。我們的方法在基於 CLIP 的量化指標上提升了 8.62%，而質化分析也證實了其在將背景資訊從學習到的表徵中解耦的有效性。原始程式碼可於以下網址取得: https://github.com/JackChen890311/AGTree。

關鍵字：注意力機制、擴散模型、生成式人工智慧、視覺概念、概念分解

# Abstract
When designing novel visual concepts, designers often draw inspiration from existing ideas, recombining elements to create something unique and original. With the rapid advancement of text-to-image (T2I) models, machines can now assist in this creative process, particularly in decomposing complex visual concepts and recombining them with existing ones. However, current decomposition methods for visual concepts typically rely on diverse input images. When the inputs are visually similar, these methods struggle to isolate objects from prominent backgrounds, often resulting in outputs that are hard to interpret or apply.

In this work, we reveal a strong correlation between decomposed visual subconcepts and cross-attention maps within the diffusion U-Net. Building on this insight, we propose AGTree, a novel method that uses cross-attention maps as intrinsic masks to effectively suppress background noise, along with incorporating random dropout during training to further enhance semantic relevance. Additionally, we extend the existing evaluation metric to provide a more comprehensive assessment of model performance.

Quantitative results show that our method achieves an 8.62% improvement on a CLIP-based metric, while qualitative analyses demonstrate its effectiveness in disentangling background information from the learned representations. Code is available at: https://github.com/JackChen890311/AGTree.

Keywords: Attention Mechanism, Diffusion Model, Generative AI, Visual Concept, Concept Decomposition