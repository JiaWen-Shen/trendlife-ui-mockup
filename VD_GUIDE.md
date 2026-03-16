# VD workflow：用 Claude Code 協作 UI Mockup

> 你不需要懂 git。所有版本控制操作都由 Claude 代勞。

---

## 開始工作前

```bash
cd trendlife-ui-mockup
claude
```

啟動後，第一句話說：

> **「我今天要改 `constellation/mockup-yuki-ipad.html`，branch 是 `vd/yukis-ipad`，請先 pull 最新版本」**

Claude 會自動切換 branch、拉最新版本，然後問你想改什麼。

---

## 做完修改後

確認預覽沒問題，說：

> **「好，可以 commit」**

Claude 會自動 commit → push → 開 PR，repo owner 會收到通知。
**你不需要開瀏覽器或 GitHub。**

---
---

## 開工前確認清單

以下資訊如果你還沒有，請先向 repo owner 確認再開始：

| 項目 | 說明 | 確認了？ |
|-----|------|--------|
| **GitHub 帳號已加入 repo** | 沒有權限就無法 push | ☐ |
| **Repo clone 到本機** | `trendlife-ui-mockup/` 資料夾存在 | ☐ |
| **Claude Code 已安裝並登入** | 可以在 terminal 執行 `claude` | ☐ |
| **你負責的 branch 名稱** | 本專案：`vd/yukis-ipad` | ☐ |
| **你負責的檔案路徑** | 本專案：`constellation/mockup-yuki-ipad.html` | ☐ |
| **預覽網址** | 如果需要對照線上版本 | ☐ |

---

## 附件

### A. 怎麼描述修改

直接用中文說就好。

| 你說的話 | Claude 會做的事 |
|--------|--------------|
| 「S3 的卡片背景改成深藍色 `#1a2744`」 | 找到 Screen 3 的卡片，修改背景色 |
| 「標題字體縮小，大概 18px」 | 調整對應 CSS |
| 「在右上角加一個設定 icon」 | 加入 icon 元素 |
| 「S5 跟 S3 的間距看起來不一致，對齊一下」 | 比對兩個 screen 的 padding |

不確定時先說：「你覺得這樣合理嗎？先跟我說想法，不要直接改」

---

### B. 確認修改 / 反悔

| 你想做的事 | 說這句話 |
|---------|--------|
| 在瀏覽器看結果 | 「在瀏覽器開給我看」 |
| 先不要 commit | 「先不要 commit，我想再看一下」 |
| 改錯了，還原 | 「還原剛才的修改」 |
| 看今天改了什麼 | 「顯示今天改了什麼」 |

---

### C. 第一次使用（只做一次）

請 repo owner 幫你完成：

1. 安裝 Claude Code
2. Clone repo 到本機：`git clone <repo-url> trendlife-ui-mockup`
3. 建立工作 branch（repo owner 執行）

你的資訊：
- **Branch**：`vd/yukis-ipad`
- **檔案**：`constellation/mockup-yuki-ipad.html`

---

### D. 常見問題

**Q：Claude 問了我看不懂的問題？**
> 截圖傳給 repo owner。

**Q：我不確定 Claude 的回答對不對？**
> 說「先不要動，我先問一下」，再找 repo owner 確認。
