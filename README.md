# 星冰樂的運動科學手帳 🐱🏸

一個專門產生**統一風格運動科學教學圖卡**的 AI Agent 專案。
生成式人工智慧 W12 作業：統一風格圖像產生的 Agent。

吉祥物是我家的英國短毛貓「星冰樂」，戴著薄荷綠運動頭帶，帶大家讀運動科學論文。
內容來自我在 W10 建立的 LLM Wiki [AI 在運動科學的應用](https://github.com/Yenchen-H/ai-sport-wiki)。

👉 **線上瀏覽：** https://yenchen-h.github.io/xingbingle-sport-cards/

| No. | 主題 | PNG |
|---|---|---|
| 01 | 傷害預測 Injury Prediction | [png](png/01-injury-prediction.png) |
| 02 | 訓練負荷 ACWR | [png](png/02-training-load.png) |
| 03 | SHAP 可解釋 AI | [png](png/03-shap.png) |
| 04 | AI 輔助選才 Talent Identification | [png](png/04-talent-identification.png) |

## 製作流程

```
LLM Wiki ──▶ notes/ ──[skill: notes-to-html]──▶ html/ ──[skill: html-to-card]──▶ png/
（W10）     內容筆記                          一頁式網頁                    教學圖卡
                                            只有內容、沒有插圖             A 程式截圖
                                                                         B AI 重新繪製
```

1. **notes**：從 Wiki 挑一個概念，照固定格式寫成筆記（一句話定義、三個重點、研究小抄、星冰樂小提醒），每個數字都附來源。
2. **notes → html**：`scripts/build_html.py` 把筆記套進同一個版型，樣式全部來自 `style/card.css`。
3. **html → png**：
   - **路線 A**：`scripts/render_png.py` 用無頭瀏覽器截圖，文字百分之百正確。
   - **路線 B**：把截圖和星冰樂角色設定圖一起交給 ChatGPT／Gemini，用 `prompts/` 裡的固定模板重新繪製成手繪插畫版。

兩個步驟都寫成 skill（`.claude/skills/`），之後只要對 Claude 說「幫我把『比賽結果預測』做成一張新圖卡」，它就會照同樣的規則做出同風格的卡片。

## 怎麼維持「統一風格」？

| 固定什麼 | 放在哪裡 |
|---|---|
| 色票、字體、版面規格、文字規則 | `style/style-guide.md` |
| 吉祥物造型 | `style/xingbingle.svg`、`style/character-sheet.png` |
| 版型與樣式 | `style/card.css`（改一次，全部卡片一起變） |
| 內容格式 | `notes/` 的固定標題 |
| AI 生圖指令 | `prompts/` 同一個模板，只換動作與小插圖 |

## 資料夾

```
.claude/skills/   notes-to-html、html-to-card 兩個 skill
style/            風格指南、card.css、星冰樂、道具圖示
notes/            內容筆記
html/             一頁式 HTML 圖卡
png/              程式截圖版 PNG（png/ai/ 放 AI 繪製版）
prompts/          ChatGPT／Gemini 生圖 prompt
scripts/          build_html.py、render_png.py
docs/             作業說明
```

## 自己跑一次

```bash
pip install playwright && playwright install chromium
python scripts/build_html.py
python scripts/render_png.py
```

---
本專案在 Claude 協助下完成：我決定主題、吉祥物與風格，Claude 協助撰寫 skill、版型與腳本，內容由我從 W10 Wiki 挑選並核對。
