---
id: "01"
title: 傷害預測
en: Injury Prediction
prop: 放大鏡
sources: Cohan 2021、Majumdar 2024、Zhou 2025
---

## 一句話定義
用機器學習從過去的傷病、比賽量、訓練負荷等資料，估算選手「接下來會不會受傷」。

## 三個重點
1. **資料從哪來**：過去傷病、近幾場上場時間、GPS 訓練負荷、身高體重年齡。[Cohan 2021] [Majumdar 2024]
2. **不要只看 accuracy**：受傷是少數事件，資料極度不平衡，要看 recall、precision、ROC AUC。[Cohan 2021]
3. **誤報也有代價**：precision 低代表很多假警報，選手可能被多休息；但真正高風險的人也被保護到了。[Majumdar 2024]

## 研究小抄
- NBA：METIC 模型 ROC AUC 0.80 [Cohan 2021]
- 英超：ANN 預測 7 天內非接觸性傷害，recall 77%、precision 13% [Majumdar 2024]

## 星冰樂小提醒
看到「準確率 95%」先別高興，先問：受傷的人有被抓到幾個？
