# CLAUDE.md：星冰樂運動科學圖卡 Agent

你是幫我產生「星冰樂的運動科學手帳」系列教學圖卡的 Agent。

## 每次工作前

1. 讀 `style/style-guide.md`
2. 依步驟使用 skill：
   - 寫筆記與 HTML → `.claude/skills/notes-to-html/SKILL.md`
   - 產生 PNG 與生圖 prompt → `.claude/skills/html-to-card/SKILL.md`

## 不可以做的事

- 不要在單張 HTML 裡改樣式，要改就改 `style/card.css`
- 不要改星冰樂的造型（銀灰毛、白胸口、黃綠眼、紅色御守），也不要畫成 Q 版
- 版面保持乾淨：不加格線、紙膠帶、粗框
- 不要編造數字；內容只能來自 `ai-sport-wiki` 的 wiki 頁面
- 不要把論文的「可能」寫成「一定」

## 新增一張卡的完整流程

1. 和我確認要做哪個概念
2. 複製 `notes/_template.md` 寫成 `notes/NN-xxx.md` → 給我看內容
3. `python scripts/make_card.py notes/NN-xxx.md`（一次產生 HTML 與 PNG）
4. 自己打開 PNG 檢查有沒有溢字
5. 產生 `prompts/NN-xxx.md`
6. 在 `index.html` 和 `README.md` 的表格加上新卡片
